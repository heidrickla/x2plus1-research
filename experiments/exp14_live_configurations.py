"""Experiment 14 -- live configurations, found by inverting the search.

Supports Note L, section "Generate from the realised side".

WHY THIS EXISTS. Both sessions working on this repo built candidate lists the
same way: enumerate multipliers (solutions of U^2 - D V^2 = M^2, V = 2k), keep
those whose r-product is under 2, and call the result "pairs where a dyadic
window could hold three moduli". Every such list was refuted. A multiplier is a
ratio between solution CLASSES of the modulus equation Y^2 - D X^2 = aM, and it
is well defined whether or not any class is occupied -- so those lists counted
configurations that mostly are not there, and misdescribed the ones that are.
On (1, 115921), the tightest candidate either session produced, the criterion
predicts a ratio near 1.3 and the real moduli are spaced 33.77 apart.

THE INVERSION. Enumerate REALISED ratio classes first, keep the ones that
genuinely put two moduli inside a dyadic window, and only then ask which
multiplier index explains the observed ratio. Occupancy is the input rather than
a filter applied afterwards, so this cannot produce a dead configuration.

WHAT IT REPORTS. For each realised close pair, the observed modulus ratio and
the multiplier index k that accounts for it. The interesting population is
k >= 2 -- a close pair realised at a NON-fundamental multiplier, which is the
shape Conjecture O.2 concerns. Theorem O.3 settles the k = 1 shape for M odd and
squarefree, so the k >= 2 rows in the even-M column are exactly the open region.

The first run of this method, as a residual of a positive control at X = 3000,
produced (1, 423125): moduli 10 and 17, ratio 1.70, explained by k = 91 and not
by tau_1^2 = 1.00617, with M = 423124 even so O.3 is mute on it.

Usage:  python experiments/exp14_live_configurations.py [X]   (X = 3000 ~ 1 min)
"""

import _bootstrap  # noqa: F401
import sys
from collections import Counter
from math import gcd, isqrt, sqrt

from x2plus1.polyseq import ratio_classes

#: how far to look for a multiplier index explaining an observed ratio
K_SEARCH = 4000
#: relative tolerance -- the tau^2 identification is exact only up to O(1/m)
TOL = 2e-3


def _is_square(n: int) -> bool:
    if n < 0:
        return False
    r = isqrt(n)
    return r * r == n


def multipliers(a: int, b: int, k_max: int = K_SEARCH):
    """k with U^2 = M^2 + 4 k^2 D solvable -- the separations between classes."""
    M, D = b - a, a * b
    for k in range(1, k_max + 1):
        v = M * M + 4 * k * k * D
        if _is_square(v):
            yield k, (isqrt(v) + 2 * k * sqrt(D)) / M


def explain(a: int, b: int, ratio: float):
    """Smallest k whose multiplier accounts for an observed modulus ratio."""
    for k, r in multipliers(a, b):
        if abs(ratio / (r * r) - 1) < TOL or abs(ratio / r - 1) < TOL:
            return k, r
    return None, None


def squarefree(n: int) -> bool:
    p = 2
    while p * p <= n:
        if n % (p * p) == 0:
            return False
        while n % p == 0:
            n //= p
        p += 1 if p == 2 else 2
    return True


def main() -> int:
    X = int(sys.argv[1]) if len(sys.argv) > 1 else 3000
    classes = ratio_classes(X)

    close = []
    for (a, b), ms in classes.items():
        ms = sorted(ms)
        for i in range(len(ms) - 1):
            if ms[i + 1] < 2 * ms[i]:
                close.append((a, b, ms[i], ms[i + 1], ms[i + 1] / ms[i]))

    print(f"X = {X}   realised ratio classes: {len(classes)}")
    print(f"close pairs (two moduli in one dyadic window): {len(close)}")

    rows, unexplained = [], 0
    for a, b, mi, mj, ratio in close:
        k, r = explain(a, b, ratio)
        if k is None:
            unexplained += 1
        else:
            rows.append((k, a, b, mi, mj, ratio, r * r, b - a))

    tally = Counter(k for k, *_ in rows)
    print(f"  explained by some multiplier index: {len(rows)}"
          f"   unexplained within k <= {K_SEARCH}: {unexplained}")
    print(f"  index distribution: {dict(sorted(tally.items())[:8])}"
          + (" ..." if len(tally) > 8 else ""))

    live = sorted((r for r in rows if r[0] >= 2), key=lambda r: r[5])
    print(f"\nLIVE NON-FUNDAMENTAL close pairs (k >= 2): {len(live)}")
    if not live:
        print("  none at this X -- the k >= 2 shape is realised only rarely.")
        return 0

    print(f"  {'k':>5} {'a':>6} {'b':>10} {'m_i':>10} {'m_j':>10} "
          f"{'ratio':>8} {'r_k^2':>8}  {'M':>10} {'M odd&sqfree':>13}")
    for k, a, b, mi, mj, ratio, rk2, M in live:
        flag = "O.3 applies" if (M % 2 and squarefree(M)) else "O.3 MUTE"
        print(f"  {k:5d} {a:6d} {b:10d} {mi:10d} {mj:10d} "
              f"{ratio:8.4f} {rk2:8.4f}  {M:10d} {flag:>13}")

    mute = sum(1 for k, a, b, mi, mj, ra, rk2, M in live if not (M % 2 and squarefree(M)))
    print(f"\n  of the live non-fundamental pairs, {mute} of {len(live)} "
          f"sit in the even-or-non-squarefree M regime Theorem O.3 cannot reach.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
