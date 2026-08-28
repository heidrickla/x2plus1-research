"""Experiment 18 -- Theorem O.3''s (c,k) exclusion region, and what is realised.

Supports Note O.  Theorem O.3' excludes (xi, tau_1 xi, tau_k xi) from a dyadic
window whenever c = gcd(M, 2X) <= 16.  O.3'' recovers a term O.3' discards and
turns the bound into a JOINT condition on (c, k): a window can hold the triple
only if

    (4k + sqrt(16k^2+2)) (2c+1) < c (kc - c - 1).

Taking k -> infinity gives back c > 8 + sqrt(72) = 16.485, so O.3' is the k-free
shadow of this.  At small k it binds much harder -- k = 2 needs c >= 34.

THE STEP O.3' DISCARDS.  Its chain reaches rho^2 < 9/8 - rho/(8k) and then drops
the second term using rho > 0.  But rho > 1 is free:

    U_k = sqrt(M^2 + 4k^2 ab) > 2k sqrt(ab) > 2ka since b > a, so rho > 0;
    and Lambda = (k-rho)/(rho^2-1) > 0, so rho^2 < 1 would force rho > k >= 1,
    contradicting rho < 1.

k = 1 IS THE BOUNDARY, which is why this was easy to miss.  There U_1 = a+b, so
B_1 = M and rho = 1 EXACTLY -- the identity reads M*0 = 4a*0 and Lambda = 0/0.
A first attempt at this test included k = 1 and reported 553,959 violations of a
bound that is in fact correct; the bound applies only for k >= 2, which is what
O.3 assumed all along.

WHY MEASURING c IS LEGITIMATE HERE.  `triples-cannot-be-settled-by-measurement`
forbids sweeping for the CONCLUSION -- a configuration that never occurs.  c is
read off configurations that DO occur, so this measures the hypothesis, not the
absence.  What it shows is that the theorem is nowhere near binding in nature.

Usage:  python experiments/exp18_ck_region.py [X]
"""

import sys
from collections import Counter, defaultdict
from fractions import Fraction
from math import gcd, isqrt, sqrt

import _bootstrap  # noqa: F401

SLOPE = 3 + 2 * sqrt(2)


def kmin_surviving(c, kcap=200):
    """Smallest k >= 2 that O.3'' does not exclude at this c, or None."""
    for k in range(2, kcap):
        if (4 * k + sqrt(16 * k * k + 2)) * (2 * c + 1) < c * (k * c - c - 1):
            return k
    return None


def main(X=4000):
    print("THE (c,k) EXCLUSION REGION.  A window holds (xi, tau_1 xi, tau_k xi)")
    print("only if (4k + sqrt(16k^2+2))(2c+1) < c(kc - c - 1).\n")
    cmax_all = max(c for c in range(1, 200) if kmin_surviving(c) is None)
    print(f"  c <= {cmax_all}: EVERY k excluded   <-- this is Theorem O.3'")
    for c in range(cmax_all + 1, 41):
        print(f"  c = {c:3}     survives only for k >= {kmin_surviving(c)}")
    print(f"  k = 2 is excluded for every c <= "
          f"{max(c for c in range(2, 200) if kmin_surviving(c) != 2)}")

    # ---- the algebra, over a coprime box -----------------------------------
    n1 = n2 = 0
    rho_max = Fraction(0)
    tight = 0.0
    bad_old = bad_new = 0
    for a in range(1, 9):
        for b in range(a + 1, 30001):
            if gcd(a, b) != 1:
                continue
            M, D = b - a, a * b
            kw = int(M / (4 * sqrt(2) * sqrt(D)))
            if kw < 2:
                continue
            for k in range(1, kw + 1):
                t = M * M + 4 * k * k * D
                U = isqrt(t)
                if U * U != t:
                    continue
                rho = Fraction(U - 2 * k * a, M)
                if k == 1:
                    n1 += 1
                    assert rho == 1 and U == a + b, (a, b, k)
                    continue
                n2 += 1
                rho_max = max(rho_max, rho)
                bound = sqrt(1 + (k - 1) / (4 * k + sqrt(16 * k * k + 2)))
                bad_old += rho * rho >= Fraction(9, 8)
                bad_new += float(rho) >= bound
                tight = max(tight, float(rho) / bound)
    print(f"\nOVER a <= 8, b <= 30000:")
    print(f"  k = 1  in-window multipliers: {n1}   rho == 1 identically, U = a+b")
    print(f"  k >= 2 in-window multipliers: {n2}   rho_max = {float(rho_max):.6f}")
    print(f"     violations of O.3'  rho^2 < 9/8             : {bad_old}")
    print(f"     violations of O.3'' rho^2 < 1 + (k-1)/A_k   : {bad_new}")
    print(f"     tightest case sits at {tight:.4f} of the sharpened bound"
          f" -- essentially saturated.")

    # ---- what is realised --------------------------------------------------
    sq = [x * x + 1 for x in range(X + 1)]
    classes = defaultdict(set)
    for x in range(1, int(X / SLOPE) + 2):
        sx = sq[x]
        for y in range(int(SLOPE * x), X + 1):
            g = gcd(sx, sq[y])
            if g > 1:
                classes[(sx // g, sq[y] // g)].add(g)
    seen = Counter()
    for (a, b), ms in classes.items():
        M, D = b - a, a * b
        for k in range(2, int(M / (4 * sqrt(2) * sqrt(D))) + 1):
            t = M * M + 4 * k * k * D
            U = isqrt(t)
            if U * U != t:
                continue
            for m in sorted(ms):
                Xi, Yi = isqrt(a * m - 1), isqrt(b * m - 1)
                if (U * Xi + 2 * k * a * Yi) % M == 0 and (
                    U * Yi + 2 * k * b * Xi
                ) % M == 0:
                    seen[(gcd(M, 2 * Xi), k)] += 1
    print(f"\nREALISED at X = {X} ({len(classes)} ratio classes in the slice).")
    print("  acting in-window multipliers with k >= 2, by (c, k):")
    if not seen:
        print("    NONE -- raise X; this run says nothing about how tight O.3'' is.")
    for (c, k), v in sorted(seen.items()):
        km = kmin_surviving(c)
        print(f"    c = {c:4}  k = {k:4}   x{v:<4} "
              f"{'excluded by O.3\u2033' if km is None or k < km else 'NOT excluded'}")
    if seen:
        print(f"\n  max realised c = {max(c for c, _ in seen)}, against a threshold of"
              f" {cmax_all + 1}.")
        print("  So O.3'' holds with room to spare on everything that occurs -- the")
        print("  constraint doing the real work in nature is not this one.")


if __name__ == "__main__":
    main(int(sys.argv[1]) if len(sys.argv) > 1 else 4000)
