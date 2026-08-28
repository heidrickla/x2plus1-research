"""Experiment 19 -- Theorem O.4, the bound that assumes no multiplier acts.

Supports Note O.  O.3, O.3' and O.3'' all assume tau_1 acts, so none of them
touches the p, q >= 2 gap where Conjecture O.2 is actually open.  O.4 does:

    Three shared moduli of the class (a,b) lie in one dyadic window only if
    tau_min^4 < 2 + 1/X_1^2,   X_1 = sqrt(a m_1 - 1) the smallest of the three.

The argument is composition.  Two steps m_1 -> m_2 -> m_3 have multipliers
tau_12, tau_23 -- whatever they happen to be -- so the composite the window has
to fit is at least tau_min^2, and tau_min is tau_1 unless a^2 - ab + b^2 is a
perfect square.

THE STEP TO GET RIGHT is X_j > tau_V X_i.  It comes from the automorph
X_j = (U X_i + V a Y_i)/M together with a Y_i > X_i sqrt(D), and there the
factor a cancels exactly.  Bounding the symmetric form
|V| = M (X_j^2 - X_i^2)/(X_j Y_i + X_i Y_j) instead gives tau evaluated at V/a --
true, but weaker, and wrong for a > 1.  Both are checked below.

THE FINITE TERM IS NOT DECORATION.  The modulus ratio is tau^2 only
asymptotically; exactly, m = (X^2+1)/a.  Dropping the +1 gives the clean-looking
"m_{i+2}/m_i >= tau_1^4", which FAILS -- 9 times in 110 gaps at X = 4000.  This
script reports both so the failure stays visible.

Usage:  python experiments/exp19_composition_bound.py [X]
"""

import sys
from math import isqrt, sqrt

import _bootstrap  # noqa: F401

from x2plus1.polyseq import ratio_classes

FOURTH = 2 ** 0.25
T_PAIR = (1 + sqrt(2)) ** 2                       # 3 + 2 sqrt 2
T_TRIPLE = (FOURTH + 1) / (FOURTH - 1)            # = T_PAIR + 2^{5/4}(1+sqrt2)


def main(X=4000):
    print("THRESHOLDS, in closed form.  t = sqrt(b/a).")
    print(f"  a PAIR   in one window needs t > (1+sqrt2)^2      = {T_PAIR:.6f},"
          f"  b/a > {T_PAIR**2:.4f}")
    print(f"  a TRIPLE in one window needs t > {T_TRIPLE:.6f},"
          f"  b/a > {T_TRIPLE**2:.4f}")
    print(f"     equivalently M > 4(2^(1/4) + 2^(3/4)) sqrt(ab) ="
          f" {4*(FOURTH + FOURTH**3):.4f} sqrt(ab)")
    print(f"     and t_triple - t_pair = 2^(5/4)(1+sqrt2) ="
          f" {2**1.25*(1+sqrt(2)):.6f} exactly")
    print(f"  the determinant route (|V_13| >= 4) gives only"
          f" {8*sqrt(2):.4f} sqrt(ab), and needs the asymptotic |V| law")

    print("\n  the finite term tightens the threshold as m_1 grows:")
    print("     X_1     tau_1^4 <     b/a >")
    for xi in (1, 2, 3, 5, 10, 100):
        thr = 2 + 1 / xi**2
        t = (thr**0.25 + 1) / (thr**0.25 - 1)
        print(f"     {xi:5}    {thr:8.4f}   {t*t:9.4f}")

    classes = ratio_classes(X)
    steps = bad_step = bad_weak = 0
    gaps = bad_exact = bad_clean = 0
    tight_step = tight_gap = 9e9
    ws = wg = wclean = None
    for (a, b), ms in classes.items():
        ms = sorted(ms)
        D, M = a * b, b - a
        tau1 = (sqrt(b) + sqrt(a)) / (sqrt(b) - sqrt(a))
        xs = [isqrt(a * m - 1) for m in ms]
        ys = [isqrt(b * m - 1) for m in ms]
        for i in range(len(ms) - 1):
            if xs[i] < 1:
                continue
            V = abs(xs[i] * ys[i + 1] - xs[i + 1] * ys[i])
            tau = (sqrt(M * M + D * V * V) + V * sqrt(D)) / M
            # the weaker constant the symmetric route yields: tau at V/a
            wk = V / a
            tau_w = (sqrt(M * M + D * wk * wk) + wk * sqrt(D)) / M
            steps += 1
            r = (xs[i + 1] / xs[i]) / tau
            bad_step += r <= 1
            bad_weak += (xs[i + 1] / xs[i]) <= tau_w
            if r < tight_step:
                tight_step, ws = r, (a, b, ms[i], ms[i + 1], V)
        for i in range(len(ms) - 2):
            if xs[i] < 1:
                continue
            gaps += 1
            obs = ms[i + 2] / ms[i]
            exact = (tau1**4 * xs[i] ** 2 + 1) / (xs[i] ** 2 + 1)
            bad_exact += obs <= exact
            if obs < tau1**4:
                bad_clean += 1
                if wclean is None:
                    wclean = (a, b, ms[i], ms[i + 2], obs, tau1**4)
            if obs / exact < tight_gap:
                tight_gap, wg = obs / exact, (a, b, ms[i], ms[i + 2], exact, obs)

    print(f"\nX = {X}:  {len(classes)} ratio classes")
    print(f"  STEP  X_j > tau(|V|) X_i        : {steps} steps,"
          f" {bad_step} violations   (tightest {tight_step:.6f} at {ws})")
    print(f"        the weaker tau(|V|/a) form: {bad_weak} violations"
          f" -- true but not sharp, which is why the proof goes via the map")
    print(f"  GAP   exact  m3/m1 > (tau_1^4 X^2+1)/(X^2+1): {gaps} gaps,"
          f" {bad_exact} violations")
    print(f"        clean  m3/m1 >= tau_1^4 (the +1 dropped) : {bad_clean}"
          f" VIOLATIONS -- the finite term is load-bearing")
    if wclean:
        a, b, mi, mk, obs, pr = wclean
        print(f"           e.g. (a,b)=({a},{b}) m {mi}->{mk}: observed {obs:.4f}"
              f" against tau_1^4 = {pr:.4f}")
    if wg:
        a, b, mi, mk, lo, obs = wg
        print(f"  the exact bound is SHARP: at (a,b)=({a},{b}) m {mi}->{mk}"
              f" it gives {lo:.4f} against an observed {obs:.4f}")

    adm = [(a, b) for (a, b), ms in classes.items()
           if b > T_TRIPLE**2 * a and len(ms) >= 3]
    print(f"\n  classes clearing b/a > {T_TRIPLE**2:.2f} AND holding three moduli:"
          f" {len(adm)}")
    if adm:
        best = min(
            (min(sorted(classes[k])[i + 2] / sorted(classes[k])[i]
                 for i in range(len(classes[k]) - 2)), k) for k in adm)
        print(f"    smallest two-step ratio among them: {best[0]:.4f} at {best[1]}")
        print(f"    -- a window needs < 2, so O.4 is not binding: the nearest"
              f" configuration is a factor {best[0]/2:.2f} away.")


if __name__ == "__main__":
    main(int(sys.argv[1]) if len(sys.argv) > 1 else 4000)
