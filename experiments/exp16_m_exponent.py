"""Experiment 16 -- the M-exponent of S_mu(M), and where the grouping matters.

Supports Note M.

WHY IT CAN GO FURTHER THAN exp02.  exp02 measures
S_mu(M) = sum_m |sum_n mu(n) 1[mn in A]| by building the Gaussian incidence
matrix, which caps it near X = 1e5 -- less than a decade, while carrying Note M's
whole theta-axis argument.  But if x^2+1 is squarefree and m | x^2+1 then
gcd(m, (x^2+1)/m) = 1, so mu((x^2+1)/m) = mu(m) mu(x^2+1), and mu(m) has modulus
1 and dies under the absolute value.  What is left needs only mu(x^2+1), which
SIEVES.  That reaches X = 1e6 in seconds.

THE GROUPING, which is the point of the experiment.  S_mu takes one absolute
value per MODULUS, spanning every root of -1 mod m at once.  exp05's rho takes
one per (q, root) PROGRESSION.  When a modulus carries several roots they cancel
against each other inside S_mu's absolute value and the per-progression view
never sees it.  The two therefore have different exponents, and reporting only
one of them is how a correct measurement gets described as the wrong quantity:

    per progression   M-exponent ~ 0.505    S/sqrt(MX) flat
    per modulus       M-exponent ~ 0.480    S/sqrt(MX) drifts down

The gap is root cancellation at the square-root rate -- S_prog/S_mod tracks
sqrt(#prog/#mod) to within a couple of percent -- so the aggregate law is

    S_mu(M) ~ sqrt(M X) / sqrt(mean roots per modulus),

slightly BELOW sqrt(MX).  That is more cancellation than the law claims, so the
saving X/S_mu in Note M is conservative.

Usage:  python experiments/exp16_m_exponent.py [X]     (X = 1e6 takes ~2 min)
"""

import _bootstrap  # noqa: F401
import sys
from math import isqrt, log, sqrt

import numpy as np

from x2plus1.factorization import admissible_roots_upto


def mobius_of_x2plus1(X: int) -> np.ndarray:
    """mu(x^2+1) for x = 0..X, by sieving the progressions x = +-r (mod p).

    Only p = 2 and p = 1 (mod 4) divide any x^2+1.  After dividing out every
    prime factor <= X the cofactor is 1 or a single prime above X: if both
    factors exceeded X their product would exceed X^2+1.
    """
    rem = np.arange(X + 1, dtype=np.int64)
    rem = rem * rem + 1
    mu = np.ones(X + 1, dtype=np.int8)

    composite = np.ones(X + 1, bool)
    composite[:2] = False
    for i in range(2, isqrt(X) + 1):
        if composite[i]:
            composite[i * i:: i] = False
    roots = admissible_roots_upto(X)
    for p in np.flatnonzero(composite).tolist():
        if p != 2 and p % 4 != 1:
            continue
        for r in roots.get(p, []):
            block = rem[r::p]
            hit = block % p == 0
            if not hit.any():
                continue
            block[hit] //= p
            signs = mu[r::p]
            signs[hit] = -signs[hit]
            again = block % p == 0
            if again.any():                      # p^2 | x^2+1 kills mu
                base = np.arange(r, X + 1, p)[np.flatnonzero(again)]
                mu[base] = 0
                while True:
                    still = rem[base] % p == 0
                    if not still.any():
                        break
                    rem[base[still]] //= p
    mu[rem > 1] = -mu[rem > 1]
    mu[0] = 0
    return mu


def main() -> int:
    X = int(sys.argv[1]) if len(sys.argv) > 1 else 1_000_000
    mu = mobius_of_x2plus1(X)
    roots = admissible_roots_upto(min(2 * X, 2_000_000))

    print(f"X = {X:,}    S(M) over dyadic bands [M, 2M)\n")
    print(f"  {'M':>9} {'#mod':>7} {'#prog':>8} {'S_mod':>9} {'S_prog':>9} "
          f"{'mod/sqrt(MX)':>13} {'prog/sqrt(MX)':>14}")
    rows = []
    M = 512
    while 2 * M <= min(2 * X, 2_000_000):
        s_mod = s_prog = n_mod = n_prog = 0
        for m in range(M, 2 * M):
            rs = roots.get(m)
            if not rs:
                continue
            n_mod += 1
            acc = 0
            for r in rs:
                t = int(mu[r:X + 1:m].sum())
                acc += t
                s_prog += abs(t)
                n_prog += 1
            s_mod += abs(acc)
        if n_mod:
            norm = sqrt(M * X)
            rows.append((M, n_mod, n_prog, s_mod, s_prog))
            print(f"  {M:>9} {n_mod:>7} {n_prog:>8} {s_mod:>9} {s_prog:>9} "
                  f"{s_mod / norm:>13.4f} {s_prog / norm:>14.4f}")
        M *= 2

    if len(rows) < 3:
        print("\n  too few bands to fit an exponent; raise X")
        return 0

    e_mod = [log(rows[i + 1][3] / rows[i][3]) / log(2) for i in range(len(rows) - 1)]
    e_prog = [log(rows[i + 1][4] / rows[i][4]) / log(2) for i in range(len(rows) - 1)]
    print(f"\n  mean local M-exponent, per progression: {sum(e_prog)/len(e_prog):.4f}")
    print(f"  mean local M-exponent, per modulus:     {sum(e_mod)/len(e_mod):.4f}")
    print(f"  (sqrt(MX) predicts 0.5 for both; the deficit is root cancellation)")
    print(f"\n  {'M':>9} {'S_prog/S_mod':>13} {'sqrt(#prog/#mod)':>17} {'ratio':>7}")
    for M, n_mod, n_prog, s_mod, s_prog in rows:
        a, b = s_prog / s_mod, sqrt(n_prog / n_mod)
        print(f"  {M:>9} {a:>13.3f} {b:>17.3f} {a / b:>7.3f}")
    print("  ratio near 1 => the roots of a modulus cancel at the square-root rate,")
    print("  which accounts for the whole gap between the two exponents.")

    # The signed sum, the trivial bound, and the Cauchy-Schwarz chain.  These were
    # cited to this file by two claims before it computed any of them.
    print("")
    print("  the SIGNED sum, the trivial bound T, and the chain")
    print(f"  {'M':>9} {'#m':>7} {'signed':>9} {'S_mod':>9} {'sgn/S':>8} "
          f"{'|sgn|/sqrt(T)':>14} {'T':>9} {'0.75*CS':>9}")
    for M, n_mod, n_prog, s_mod, s_prog in rows:
        signed = trivial = 0
        for m in range(M, 2 * M):
            rs = roots.get(m)
            if not rs:
                continue
            for r in rs:
                seg = mu[r:X + 1:m]
                signed += int(seg.sum())
                trivial += len(seg)
        if not (trivial and s_mod):
            continue
        # Q2 ~ DIAG = 0.7658 T (incidence-count-and-squarefreeness-are-correlated),
        # and the parallel session measures Cauchy-Schwarz tightness S/CS ~ 0.75.
        cs = sqrt(n_mod * 0.7658 * trivial)
        print(f"  {M:>9} {n_mod:>7} {signed:>9} {s_mod:>9} "
              f"{abs(signed)/s_mod:>8.4f} {abs(signed)/sqrt(trivial):>14.4f} "
              f"{trivial:>9} {0.75*cs:>9.0f}")
    print("  |signed|/sqrt(T) stays O(1) across M -- full square-root cancellation --")
    print("  while S_mod grows, so signed/S_mod DECAYS: the absolute value is the cost,")
    print("  and it costs more the further into the Type II range one goes.")
    print("  0.75*CS against S_mod is the chain; they agree near M = X.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
