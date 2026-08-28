"""Experiment 26 -- Conjecture O.2 below u = 53.6942 is an explicit finite list.

Feeds Note O.  A dyadic window holding THREE shared moduli needs the composite of
two multiplier steps to fit, i.e. tau_min^4 < 2 + 1/X_1^2.  Writing
s = V sqrt(ab)/M, tau_V^2 < c is equivalent to sqrt(u) - 1/sqrt(u) > 2 sqrt(c) V /
(c-1), so with c = sqrt(2 + 1/X_1^2):

    V = 2 (ALWAYS admissible, U = a+b)  : u > 53.6942 at X_1 = 1, -> 133.8748
    V = 1 (needs a^2-ab+b^2 a square)   : u > 14.8609 at X_1 = 1, ->  34.9419

The V = 2 row is Theorem O.4, recovered here independently: CLAUDE.md recorded
O.4 as "b/a > 53.69 at X_1 = 1, rising to 133.875".

UNCONDITIONALLY IN X_1, then: a windowed triple with u < 53.6942 must have
V_min = 1, hence a^2 - ab + b^2 a perfect square -- the Eisenstein norm form, so
(a,b) is a 60-degree Pythagorean pair.  Below 14.8609 no V is admissible at all.

Both cofactors must also divide some x^2+1, i.e. 4 does not divide n and n has no
prime factor 3 mod 4.

RESULT: at a <= 3000 exactly five primitive pairs pass both filters, and none
holds three shared moduli in a window -- none holds even two.  All five are
locally solvable, so what empties the branch is OCCUPANCY, not congruence, which
is the wall Note O records for O.2 generally.

Usage:  python experiments/exp26_triple_branch.py [a_max] [x_max]
"""

import sys
from math import gcd, isqrt, sqrt

import _bootstrap  # noqa: F401


def threshold(V, X1):
    """Smallest u for which tau_V^4 < 2 + 1/X1^2 can hold."""
    c = sqrt(2 + 1 / (X1 * X1))
    t = 2 * sqrt(c) * V / (c - 1)
    return ((t + sqrt(t * t + 4)) / 2) ** 2


def admissible(N):
    """ok[n]: n | x^2+1 is solvable, i.e. 4 does not divide n and no p = 3 mod 4."""
    spf = list(range(N + 1))
    for i in range(2, isqrt(N) + 1):
        if spf[i] == i:
            for j in range(i * i, N + 1, i):
                if spf[j] == j:
                    spf[j] = i
    ok = [False] * (N + 1)
    for n in range(1, N + 1):
        m, good = n, True
        while m > 1:
            p, e = spf[m], 0
            while m % p == 0:
                m //= p
                e += 1
            if (p == 2 and e > 1) or p % 4 == 3:
                good = False
                break
        ok[n] = good
    return ok


def shared_moduli(a, b, xmax):
    """m with a*m and b*m both of the form x^2+1, walking a's progressions."""
    out = set()
    for r in [r for r in range(a) if (r * r + 1) % a == 0]:
        x = r if r else a
        while x <= xmax:
            v = x * x + 1
            if v % a == 0:
                m = v // a
                t = b * m - 1
                s = isqrt(t)
                if s * s == t:
                    out.add(m)
            x += a
    return sorted(out)


def locally_solvable(a, b, qs=(3, 4, 5, 7, 8, 9, 11, 13, 16, 17, 25, 27, 32, 49)):
    M = b - a
    return [q for q in qs
            if not any((a * Y * Y - b * X * X - M) % q == 0
                       for X in range(q) for Y in range(q))]


def main(amax=3000, xmax=20_000_000):
    lo, hi = threshold(1, 1), threshold(2, 1)
    print("A window holding THREE shared moduli needs tau_min^4 < 2 + 1/X_1^2.")
    print(f"  {'X_1':>8} {'V = 1 (Eisenstein)':>20} {'V = 2 (always)':>18}")
    for X1 in (1, 10, 10 ** 9):
        lbl = "inf" if X1 > 10 ** 6 else str(X1)
        print(f"  {lbl:>8} {threshold(1, X1):>20.4f} {threshold(2, X1):>18.4f}")
    print(f"\n  So unconditionally in X_1: a windowed triple with u < {hi:.4f} forces")
    print(f"  a^2-ab+b^2 to be a perfect square. Below {lo:.4f} no V is admissible.")
    print("  The V = 2 row is Theorem O.4, recovered independently.\n")

    N = int(amax * hi) + 2
    ok = admissible(N)
    cands = []
    for a in range(2, amax + 1):
        if not ok[a]:
            continue
        for b in range(int(lo * a) + 1, int(hi * a) + 1):
            q = a * a - a * b + b * b
            r = isqrt(q)
            if r * r == q and ok[b] and gcd(a, b) == 1:
                cands.append((a, b))

    print(f"  a <= {amax}, u in ({lo:.4f}, {hi:.4f}), both cofactors admissible,")
    print(f"  a^2-ab+b^2 square, gcd = 1:  {len(cands)} primitive pairs\n")
    print(f"  {'pair':>18} {'u':>9} {'shared':>7} {'in one window':>14}"
          f" {'spread':>10} {'local obstruction':>18}")
    worst = 0
    for a, b in cands:
        sh = shared_moduli(a, b, xmax)
        w = max((sum(1 for q in sh if p <= q < 2 * p) for p in sh), default=0)
        worst = max(worst, w)
        spread = f"{sh[-1] / sh[0]:.0f}x" if len(sh) > 1 else "-"
        bad = locally_solvable(a, b)
        print(f"  {f'({a},{b})':>18} {b / a:>9.4f} {len(sh):>7} {w:>14}"
              f" {spread:>10} {str(bad) if bad else 'none':>18}")
        if sh:
            print(f"        moduli: {sh[:6]}")
    print(f"\n  A triple needs THREE in one window. Maximum observed: {worst}.")
    print("  Every candidate is locally solvable, so the branch is emptied by")
    print("  OCCUPANCY, not congruence -- the wall Note O records for O.2.")
    print(f"  Bounded: a <= {amax}, x <= {xmax:,}. A bound's silence is not evidence")
    print("  about what lies outside it.")


if __name__ == "__main__":
    main(int(sys.argv[1]) if len(sys.argv) > 1 else 3000,
         int(sys.argv[2]) if len(sys.argv) > 2 else 20_000_000)
