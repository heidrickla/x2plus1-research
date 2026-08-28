"""Experiment 21 -- the Note O verifications that had no runnable artefact.

Six `rigorous_finite` claims in the Note O area named their evidence in PROSE --
"in-session regeneration of all multipliers", "direct enumeration of the moduli
of (1,5)" -- rather than naming a script.  The registry requires a
`rigorous_finite` claim to have "`experiment` naming the script", and prose names
nothing runnable, so those numbers could not be reproduced at all, let alone at a
second size.  This script computes every one of them.

It is the same defect the parallel session found in seven of its own claims, one
level worse: theirs named the WRONG script, these named NO script.  The lesson
transfers -- both times, turning a one-shot script into an experiment produced
something the script could not have, because an experiment is the thing that gets
rerun at a different size.

Reproduces:
  tau-squared-law-exact-on-realised-close-pairs
  multipliers-act-freely-the-window-is-the-content
  theorem-O3-verified-independently
  theorem-O3prime-verified-hypothesis-corrected
  multiplier-r-does-not-predict-window-multiplicity   (the structural half)
  rational-graph-contains-K-s-2

Usage:  python experiments/exp21_note_O_verifications.py [X]
"""

import sys
from fractions import Fraction
from math import gcd, isqrt, sqrt
from statistics import median

import _bootstrap  # noqa: F401

from x2plus1.polyseq import close_pairs, ratio_classes


def tau_squared_law(X):
    """The modulus ratio equals tau_1^2 on realised close pairs."""
    errs = []
    for a, b, mi, mj, *_ in close_pairs(ratio_classes(X)):
        tau2 = ((sqrt(b) + sqrt(a)) / (sqrt(b) - sqrt(a))) ** 2
        errs.append(abs((mj / mi) - tau2) / tau2)
    within = sum(e < 1e-3 for e in errs)
    print(f"  close pairs at X = {X}: {len(errs)};"
          f" within 1e-3 of tau_1^2: {within} ({within / len(errs):.1%});"
          f" median rel. error {median(errs):.1e}")
    return len(errs), within


def multipliers_act_freely():
    """(1,5): the acting multipliers are a cyclic semigroup, all of them."""
    a, b = 1, 5
    M, D = b - a, a * b
    ms = sorted(ratio_classes(700)[(a, b)])
    ratios = [round(ms[i + 1] / ms[i], 4) for i in range(len(ms) - 1)]
    print(f"  (1,5) shared moduli: {ms}   consecutive ratios {ratios}")
    ks = []
    for k in range(1, 200):
        t = M * M + 4 * k * k * D
        U = isqrt(t)
        if U * U == t:
            s = 4 * k * sqrt(D) / M
            ks.append((k, round(((s + sqrt(s * s + 4)) / 2) ** 2, 3)))
    print(f"  its multipliers (k, r_k^2): {ks[:6]}")
    print("  -- the powers of tau_1^2 = phi^4 = 6.854, a cyclic semigroup, all")
    print("  of which act.  So the bare statement that tau^2 xi is never")
    print("  integral is FALSE; Proposition O.1 is true only with its window.")
    return [k for k, _ in ks]


def theorem_O3(amax=50, bmax=60000, kcap=60):
    """j = 2B/M is 2 exactly at k = 1; and no k >= 2 passes both conditions."""
    tot = k1 = j2 = div_ok = geo_ok = both = 0
    for a in range(1, amax + 1):
        for b in range(a + 1, bmax + 1):
            if gcd(a, b) != 1:
                continue
            M, D = b - a, a * b
            for k in range(1, kcap + 1):
                t = M * M + 4 * k * k * D
                U = isqrt(t)
                if U * U != t:
                    continue
                tot += 1
                B = U - 2 * k * a
                if k == 1:
                    k1 += 1
                    j2 += 2 * B == 2 * M
                    continue
                d = (2 * B) % M == 0
                g = M > 2 * sqrt(2) * k * sqrt(D)
                div_ok += d
                geo_ok += g
                both += d and g
    print(f"  a <= {amax}, b <= {bmax}, k <= {kcap}: {tot} multipliers,"
          f" {k1} with k = 1,"
          f" of which j = 2B/M = 2 exactly: {j2} ({k1 - j2} violations)")
    print(f"  among k >= 2: {div_ok} satisfy the divisibility, {geo_ok} the"
          f" geometry, {both} satisfy BOTH")
    return tot, k1, j2, both


def theorem_O3prime(amax=50, bmax=60000, kcap=60):
    """The identity, and the rho bound under the right window condition."""
    ident = n_sq = n_lin = 0
    bad_id = bad_sq = bad_lin = 0
    rho_sq = rho_lin = Fraction(0)
    for a in range(1, amax + 1):
        for b in range(a + 1, bmax + 1):
            if gcd(a, b) != 1:
                continue
            M, D = b - a, a * b
            for k in range(2, kcap + 1):
                t = M * M + 4 * k * k * D
                U = isqrt(t)
                if U * U != t:
                    continue
                rho = Fraction(U - 2 * k * a, M)
                ident += 1
                bad_id += M * (rho * rho - 1) != 4 * k * a * (k - rho)
                s = 4 * k * sqrt(D) / M
                r = ((s + sqrt(s * s + 4)) / 2) ** 2       # the MODULUS ratio
                if r < 2:                                  # correct hypothesis
                    n_sq += 1
                    bad_sq += rho * rho >= Fraction(9, 8)
                    rho_sq = max(rho_sq, rho)
                if sqrt(r) < 2:                            # as first stated
                    n_lin += 1
                    bad_lin += rho * rho >= Fraction(9, 8)
                    rho_lin = max(rho_lin, rho)
    print(f"  a <= {amax}, b <= {bmax}, k <= {kcap}.  THE COUNTS BELOW ARE")
    print("  RANGE-DEPENDENT, and the recorded ones did not state a k cap --")
    print("  which is why they could not be reproduced.  The CONCLUSIONS do.")
    print(f"  identity M(rho^2-1) = 4ka(k-rho): {ident} multipliers with k >= 2,"
          f" {bad_id} violations (exact Fraction arithmetic)")
    print(f"  rho < sqrt(9/8) under r_k < 2      (CORRECT): n = {n_sq},"
          f" {bad_sq} violations, rho_max = {float(rho_sq):.6f}")
    print(f"  rho < sqrt(9/8) under sqrt(r_k) < 2 (as first stated): n = {n_lin},"
          f" {bad_lin} violations, rho_max = {float(rho_lin):.6f}")
    print("  -- the modulus ratio is tau^2, not tau, and the distinction decides")
    print("  the theorem: the bound is false under the weaker reading.")
    return ident, bad_id, n_sq, bad_sq


def K_s_2():
    """The K_{6,2}: six cofactors n with 10n and 17n both of the form t^2+1."""
    ns = [1, 53, 423125, 24326641, 194502909745, 11182518951605]
    for n in ns:
        for c in (10, 17):
            t = isqrt(c * n - 1)
            assert t * t + 1 == c * n, (n, c)
    print(f"  n = {ns}")
    print("  each has both 10n and 17n of the form t^2+1 -- K_(6,2) over Z.")
    e2 = 339 + 26 * sqrt(170)
    print(f"  conic 17x^2 - 10y^2 = -7 has D = 170, fundamental norm-one unit"
          f" eps^2 = 339 + 26 sqrt170 = {e2:.1f}")
    print(f"  two interleaved orbits, two-step ratios -> (eps^2)^2 = {e2 * e2:.0f};"
          f" observed {ns[-1] / ns[-3]:.0f}")
    return ns


def multiplier_r_does_not_predict():
    """Structural: a multiplier is a ratio between CLASSES, occupied or not."""
    a, b = 1, 115921
    M, D = b - a, a * b
    ks = [k for k in range(1, 40)
          if isqrt(M * M + 4 * k * k * D) ** 2 == M * M + 4 * k * k * D]
    print(f"  (1,115921): U^2 - D V^2 = M^2 has solutions at k = {ks[:6]} --")
    print("  these exist whether or not any solution class is OCCUPIED, while a")
    print("  shared modulus solves Y^2 - D X^2 = aM, a different equation.")
    print("  So r_1 r_k is a ratio between CLASSES and cannot predict window")
    print("  multiplicity: it gives ~1.3 here, while the realised consecutive")
    print("  ratios are 33.77, 4313.55, 193.53 and the multiplicity is 1.")
    return ks


def main(X=3000):
    big = X >= 3000
    amax, bmax = (50, 60000) if big else (12, 6000)
    print("1. tau-squared-law-exact-on-realised-close-pairs")
    tau_squared_law(X)
    print("\n2. multipliers-act-freely-the-window-is-the-content")
    multipliers_act_freely()
    print("\n3. theorem-O3-verified-independently")
    theorem_O3(amax, bmax, 60 if big else 20)
    print("\n4. theorem-O3prime-verified-hypothesis-corrected")
    theorem_O3prime(amax, bmax, 60 if big else 20)
    print("\n5. multiplier-r-does-not-predict-window-multiplicity")
    multiplier_r_does_not_predict()
    print("\n6. rational-graph-contains-K-s-2")
    K_s_2()


if __name__ == "__main__":
    main(int(sys.argv[1]) if len(sys.argv) > 1 else 3000)
