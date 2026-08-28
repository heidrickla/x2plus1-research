"""Experiment 11 -- why no dyadic window ever holds three shared moduli.

BACKGROUND.  For coprime a < b, a shared modulus is an m with

    a*m = x^2 + 1   and   b*m = y^2 + 1,

i.e. a solution of the conic  b x^2 - a y^2 = a - b.  Note L measures that no
dyadic window [m, 2m) ever contains three shared moduli, while pairs get
arbitrarily tight (ratios 1.0783 -> 1.0412 as X grows).  Dickson bounds the
number of CLASSES by 2^{omega(|a-b|)+O(1)}, which is 32 or more for many pairs,
so the count of classes does not explain the 2.  Two probability models were
proposed -- one by each session -- and both are refuted by the fact that the
two-step ratio m_{i+2}/m_i has a FLOOR at 13.0 with an empty bin below it,
rather than a tail approaching 2.

THIS EXPERIMENT IDENTIFIES THE MULTIPLIER AND SHOWS IT ACTS AT MOST ONCE.

Write M = b - a, D = ab.  Two shared moduli m_i < m_j give solutions
(X_i, Y_i), (X_j, Y_j) with X = sqrt(a m - 1), Y = sqrt(b m - 1).  Put

    U = b X_i X_j - a Y_i Y_j        V = X_i Y_j - X_j Y_i

Then  U^2 - D V^2 = M^2  identically, and V = 0 exactly when the two solutions
are proportional.  Estimating V for a pair inside one window gives

    |V| ~ (M / 2 sqrt(D)) * (r - 1/r),      r = X_j / X_i <= sqrt(2),

so a pair in a window needs |V| >= 1, hence M >= 2.83 sqrt(D).  MEASURED: the
smallest |V| is 2, never 1, so the true threshold is 5.657 -- against an
observed minimum of 5.667 over every class that achieves a pair.

|V| = 2 is not a coincidence.  U^2 - 4D = M^2 forces U^2 = (a-b)^2 + 4ab =
(a+b)^2, so (U, V) = (a+b, 2) is the TRIVIAL solution of the auxiliary
equation, always available.  The corresponding multiplier is

    tau = (U + V sqrt D) / M = (sqrt b + sqrt a) / (sqrt b - sqrt a),

and the modulus ratio of a close pair is tau^2.

WHY IT ACTS ONLY ONCE -- the point of the experiment.  A solution corresponds to
an element xi of norm +-M in the order of Q(sqrt D).  The multiplier is P / M
where P = (U + V sqrt D) has norm M^2 = N((M)).  Integrality of xi_2 = P xi_1 / M
consumes all of N(xi_1) = M.  A third modulus would need xi_3 = P1 P2 xi_1 / M^2,
i.e. norm M^2 absorbed by an element of norm M.  Impossible unless P2 = conj(P1),
which returns xi_3 = xi_1.

The prediction is sharp and falsifiable: whenever tau^4 < 2 a third modulus
WOULD fit inside the window, so every such pair is a chance to see three.

Usage:  python experiments/exp11_tau_multiplier.py [X]
"""

import sys
from collections import Counter, defaultdict
from math import gcd, isqrt, sqrt

import _bootstrap  # noqa: F401


def ratio_classes(X):
    """Bucket every reduced ratio (y^2+1)/(x^2+1); value list = shared moduli."""
    sq = [x * x + 1 for x in range(X + 1)]
    out = defaultdict(set)
    for x in range(1, X + 1):
        sx = sq[x]
        for y in range(x + 1, X + 1):
            g = gcd(sx, sq[y])
            if g > 1:
                out[(sx // g, sq[y] // g)].add(g)
    return {k: sorted(v) for k, v in out.items()}


def close_pairs(classes):
    """(a, b, m_i, m_j, V, tau) for every pair of shared moduli inside a window."""
    for (a, b), ms in classes.items():
        tau = (sqrt(b) + sqrt(a)) / (sqrt(b) - sqrt(a))
        for i, mi in enumerate(ms):
            for mj in ms[i + 1:]:
                if mj >= 2 * mi:
                    break
                Xi, Yi = isqrt(a * mi - 1), isqrt(b * mi - 1)
                Xj, Yj = isqrt(a * mj - 1), isqrt(b * mj - 1)
                yield a, b, mi, mj, Xi * Yj - Xj * Yi, tau


def main(X=4000):
    classes = ratio_classes(X)
    pairs = list(close_pairs(classes))
    print(f"X = {X}   ratio classes {len(classes)}   pairs inside a window {len(pairs)}\n")

    # -- 1. the rigidity of V ------------------------------------------------
    vs = Counter(abs(p[4]) for p in pairs)
    print(f"|V| distribution: {dict(sorted(vs.items()))}")
    vmin = min(vs)
    share = vs[vmin] / len(pairs)
    print(f"  minimum |V| = {vmin}, attained by {share:.1%} of pairs")
    bad = [(a, b) for a, b, _mi, _mj, V, _t in pairs if abs(V) == 1]
    print(f"  pairs with |V| = 1 (would need a^2-ab+b^2 square): {len(bad)}")
    thr = 2 * vmin / (sqrt(2) - 1 / sqrt(2))
    obs = min((b - a) / sqrt(a * b) for a, b, *_ in pairs)
    print(f"  gap-principle threshold M/sqrt(D) >= {thr:.3f}   observed minimum {obs:.3f}\n")

    # -- 2. the tau^2 law ----------------------------------------------------
    dev = [(abs(mj / mi - t * t) / (t * t), mi) for _a, _b, mi, mj, _V, t in pairs]
    big = [d for d, mi in dev if mi >= 1000]
    print(f"modulus ratio against tau^2:")
    print(f"  worst relative deviation overall      {max(d for d, _ in dev):.3f}")
    print(f"  worst relative deviation for m >= 1000 {max(big):.2e}  ({len(big)} pairs)")
    print(f"  worst (relative deviation * m)         {max(d * m for d, m in dev):.1f}")
    print(f"  -> the law is asymptotic, error O(1/m), exact in the limit.\n")

    # -- 3. tau acts at most once -------------------------------------------
    room = [p for p in pairs if p[5] ** 4 < 2]
    hits = 0
    by_a = Counter()
    for a, b, mi, mj, _V, _t in room:
        by_a["a == 1" if a == 1 else "a >= 2"] += 1
        third = [m for m in classes[(a, b)] if mi < m < 2 * mi and m not in (mi, mj)]
        if third:
            hits += 1
    print(f"pairs with tau^4 < 2, i.e. ROOM for a third inside the window: {len(room)}")
    for k in sorted(by_a):
        print(f"    {k}: {by_a[k]}")
    print(f"  third shared modulus actually found: {hits}")
    verdict = "acts exactly once" if hits == 0 else f"acts twice in {hits} cases"
    print(f"  -> tau {verdict}, over {len(room)} chances.")
    if by_a.get("a >= 2"):
        print(f"  -> and {by_a['a >= 2']} of those chances have a >= 2, so this is not")
        print("     an artefact of the unit-cofactor family a = 1.")


if __name__ == "__main__":
    main(int(sys.argv[1]) if len(sys.argv) > 1 else 4000)
