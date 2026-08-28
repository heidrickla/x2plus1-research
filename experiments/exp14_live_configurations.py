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

from x2plus1.factorization import roots_of_minus_one

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


def close_pairs_streaming(X: int):
    """Every realised close pair reachable from a first solution with x, y <= X.

    Storing all ratio classes to find the few with two close moduli costs O(X^2)
    memory -- 1.8M classes at X = 3000, and it is the reason this experiment
    could not be pushed further. It is also unnecessary. If (a,b) has moduli
    m1 < m2 < 2 m1 then a m1 = x1^2+1 and a m2 = x2^2+1 give

        x2 / x1 = sqrt(m2/m1) < sqrt 2,

    so the second solution is a SHORT search away from the first, in the known
    residues x = +-r (mod a). Streaming the first solution and searching for the
    second costs O(1) memory.

    It is also strictly more complete at fixed X: the second modulus is accepted
    on b*m2 - 1 being square, whether or not its own y2 is below X, so this sees
    close pairs a ratio-class sweep at the same X cannot.
    """
    sq = [x * x + 1 for x in range(X + 1)]
    root_cache: dict[int, list[int]] = {}
    for x1 in range(1, X + 1):
        s1 = sq[x1]
        for y1 in range(x1 + 1, X + 1):
            m1 = gcd(s1, sq[y1])
            if m1 == 1:
                continue
            a, b = s1 // m1, sq[y1] // m1
            if a not in root_cache:
                root_cache[a] = roots_of_minus_one(a) if a > 1 else [0]
            limit = int(x1 * 1.41421356) + 1
            for r in root_cache[a]:
                start = x1 + 1 + ((r - (x1 + 1)) % a if a > 1 else 0)
                for x2 in range(start, limit + 1, max(a, 1)):
                    n2 = x2 * x2 + 1
                    if n2 % a:
                        continue
                    m2 = n2 // a
                    if m2 >= 2 * m1:
                        break
                    v = b * m2 - 1
                    t = isqrt(v)
                    if t * t == v:
                        yield a, b, m1, m2, m2 / m1


def main() -> int:
    X = int(sys.argv[1]) if len(sys.argv) > 1 else 3000

    seen = set()
    close = []
    for a, b, mi, mj, ratio in close_pairs_streaming(X):
        if (a, b, mi, mj) in seen:
            continue
        seen.add((a, b, mi, mj))
        close.append((a, b, mi, mj, ratio))

    print(f"X = {X}   (streaming enumeration, O(1) memory)")
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
