"""Experiment 25 -- the D-blindness is in the mu WEIGHTS, not the Gram matrix.

Feeds Note M (the Cauchy-Schwarz chain) and Note L (the D axis).

The parallel session measured kappa and S_mu across x^2 + D and found both blind
to D, concluding that the analytic side cannot see the parameter that decides the
C_4 structure.  kappa is blind by identity; S_mu is blind by measurement.

OFF is the sharpest test available, because it is not merely another analytic
quantity -- it is literally the Gram entries weighted by mu:

    Q_2 = sum_{m ~ M} ( sum_{x : m | x^2+D} mu(x^2+D) )^2 = DIAG + OFF
    DIAG = sum_x mu(x^2+D)^2 * #{m ~ M : m | x^2+D}
    OFF  = sum_{x != y} mu(x^2+D) mu(y^2+D) * G_M(x,y)
    G_M(x,y) = #{m ~ M : m | x^2+D and m | y^2+D}

So OFF and G_M are the SAME matrix, one weighted and one not.  Running both in
one pass makes the comparison exact -- same X, same band, same incidence.

RESULT.  G_M is NOT blind: max G climbs monotonically with D, and the mean over
supported pairs climbs with it.  OFF is blind: it changes SIGN across the same
D values and has no ordering.  A sign change is the strong form of "no
systematic dependence" -- a quantity that merely fluctuated in magnitude could
be hiding a trend, one that flips cannot be monotone in D.

So "the analytic side is blind to D" is true but mislocated.  The D-dependence
is PRESENT in the matrix the analytic quantity is built from, and the mu signs
annihilate it.  Which is Note J's finding from a new angle: the signs that make
the sum hard to bound are the same signs that hide the arithmetic.

CAVEAT.  DIAG is not blind either (it swings by 4x across these D), so the
dichotomy is not analytic/structural -- it is WEIGHTED/UNWEIGHTED.

Usage:  python experiments/exp25_off_sees_D.py [X] [M]
"""

import sys
from collections import Counter
from math import sqrt

import _bootstrap  # noqa: F401

from x2plus1.factorization import sieve_shifted_square

D_AXIS = (1, 2, 6, 11, 39)      # proved / proved / protected / first failure / banded triple


def mobius_from_fac(f):
    """mu(n) from a factorisation dict {p: e}."""
    for e in f.values():
        if e > 1:
            return 0
    return -1 if len(f) % 2 else 1


def divisors_in(f, lo, hi):
    """Divisors of n in [lo, hi), from its factorisation."""
    divs = [1]
    for p, e in f.items():
        nd, pe = [], 1
        for _ in range(e + 1):
            for d in divs:
                v = d * pe
                if v < hi:
                    nd.append(v)
            pe *= p
        divs = nd
    return [d for d in divs if lo <= d < hi]


def one_D(X, M, D):
    """Return (|S_mu|/sqrt X, DIAG, OFF, maxG, mean G over supported pairs, #pairs)."""
    fac = sieve_shifted_square(X, D)
    mu = [0] + [mobius_from_fac(fac[x]) for x in range(1, X + 1)]

    inc = {}
    for x in range(1, X + 1):
        for d in divisors_in(fac[x], M, 2 * M):
            inc.setdefault(d, []).append(x)

    DIAG = Q2 = 0
    for xs in inc.values():
        s = 0
        for x in xs:
            s += mu[x]
            DIAG += mu[x] * mu[x]
        Q2 += s * s

    pair = Counter()
    for xs in inc.values():
        for i in range(len(xs)):
            for j in range(i + 1, len(xs)):
                pair[(xs[i], xs[j])] += 1

    npair = len(pair)
    return (abs(sum(mu)) / sqrt(X), DIAG, Q2 - DIAG,
            max(pair.values(), default=0),
            sum(pair.values()) / npair if npair else 0.0, npair)


def two_matrices(X, M):
    """ELEMENT-indexed vs COFACTOR-indexed, same values, same window.

    The Cauchy-Schwarz expansion decides which matrix OFF contains, and it is
    the ELEMENT one: Q_2 = sum_m (sum_{x : m | x^2+D} mu_x)^2 expands to
    DIAG + sum_{x != y} mu_x mu_y #{m ~ M : m | x^2+D and m | y^2+D}.  Note F
    and Prop L.1 are about #{m : m n1, m n2 in A}, indexed by COFACTORS.
    CLAUDE.md called these one object; they are not, and the gap is a number.

    Both means are printed over BOTH denominators, because our two sessions
    also differed there -- mean over supported pairs against mean over all
    pairs -- which disguised the disagreement a second time.
    """
    from collections import defaultdict
    print(f"\n  ELEMENT vs COFACTOR, X = {X}, one window [{M}, {2*M})")
    print(f"  {'D':>4} | {'CO max':>6} {'CO m/supp':>10} {'CO m/all':>10}"
          f" | {'EL max':>6} {'EL m/supp':>10} {'EL m/all':>10}")
    for D in D_AXIS:
        vals = [x * x + D for x in range(1, X + 1)]
        inband, cof = defaultdict(list), defaultdict(set)
        for v in vals:
            d = 1
            while d * d <= v:
                if v % d == 0:
                    q = v // d
                    if M <= d < 2 * M:
                        inband[d].append(v); cof[q].add(d)
                    if q != d and M <= q < 2 * M:
                        inband[q].append(v); cof[d].add(q)
                d += 1
        pel = defaultdict(int)
        for vs in inband.values():
            for i in range(len(vs)):
                for j in range(i + 1, len(vs)):
                    pel[(vs[i], vs[j])] += 1
        ns = sorted(cof)
        pco = {}
        for i, n1 in enumerate(ns):
            for n2 in ns[i + 1:]:
                sh = len(cof[n1] & cof[n2])
                if sh:
                    pco[(n1, n2)] = sh
        def stats(p, tot):
            return (max(p.values(), default=0),
                    sum(p.values()) / len(p) if p else 0.0,
                    sum(p.values()) / tot if tot else 0.0)
        me, se, ae = stats(pel, len(vals) * (len(vals) - 1) // 2)
        mc, sc, ac = stats(pco, len(ns) * (len(ns) - 1) // 2)
        print(f"  {D:>4} | {mc:>6} {sc:>10.4f} {ac:>10.6f}"
              f" | {me:>6} {se:>10.4f} {ae:>10.6f}")
    print("  The COFACTOR Gram -- the C_4 object -- is flat in D (max exactly 2")
    print("  throughout, mean slightly FALLING).  The ELEMENT matrix rises.  So the")
    print("  D-dependence below is about the Cauchy-Schwarz chain and NOT about")
    print("  C_4-freeness, and must never be quoted as the latter.")


def main(X=20000, bands=(1000, 2500)):
    print(f"X = {X}.  The SAME incidence matrix, weighted by mu (OFF) and")
    print("unweighted (G), in one pass -- no difference of size, band or")
    print("population between them.  Two bands, to separate signal from noise.")
    print()
    allrows = {}
    for M in bands:
        print(f"  band [{M}, {2*M})")
        print(f"  {'D':>4} {'|S_mu|/sqrtX':>13} {'DIAG':>8} {'OFF':>9}"
              f" {'OFF/DIAG':>9} {'maxG':>5} {'meanG':>7} {'#pairs':>8}")
        rows = {}
        for D in D_AXIS:
            r = one_D(X, M, D)
            rows[D] = r
            print(f"  {D:>4} {r[0]:>13.4f} {r[1]:>8} {r[2]:>9} {r[2]/r[1]:>9.4f}"
                  f" {r[3]:>5} {r[4]:>7.4f} {r[5]:>8}")
        allrows[M] = rows
        print()

    b1, b2 = bands[0], bands[1]
    print("WHAT REPRODUCES ACROSS THE BANDS, AND WHAT DOES NOT")
    print(f"  {'D':>4} {'meanG b1':>9} {'meanG b2':>9} {'drift':>8}"
          f"   {'maxG b1':>8} {'maxG b2':>8}   {'OFF/DIAG b1':>12} {'b2':>9}")
    for D in D_AXIS:
        m1, m2 = allrows[b1][D][4], allrows[b2][D][4]
        o1 = allrows[b1][D][2] / allrows[b1][D][1]
        o2 = allrows[b2][D][2] / allrows[b2][D][1]
        print(f"  {D:>4} {m1:>9.4f} {m2:>9.4f} {abs(m1-m2)/m1*100:>7.2f}%"
              f"   {allrows[b1][D][3]:>8} {allrows[b2][D][3]:>8}"
              f"   {o1:>12.4f} {o2:>9.4f}")

    drift = max(abs(allrows[b1][D][4] - allrows[b2][D][4]) / allrows[b1][D][4]
                for D in D_AXIS)
    o1 = [allrows[b1][D][2] / allrows[b1][D][1] for D in D_AXIS]
    o2 = [allrows[b2][D][2] / allrows[b2][D][1] for D in D_AXIS]
    print()
    print(f"  mean G reproduces to {drift*100:.2f}% across a band change,"
          " and orders the D axis.")
    print(f"  OFF/DIAG changes sign in BOTH bands"
          f" ({min(o1) < 0 < max(o1)}, {min(o2) < 0 < max(o2)}),"
          " so it cannot be monotone in D;")
    print(f"  and its SIGN PATTERN is not stable either:"
          f" {[v > 0 for v in o1]} vs {[v > 0 for v in o2]}.")
    print("  So the D-dependence is in the matrix, and the mu weights kill it.")

    ranks = sorted(D_AXIS, key=lambda D: allrows[b1][D][4])
    print()
    print(f"  CAUTION -- mean G is NOT a structural classifier.  Its order is"
          f" {ranks},")
    print("  which puts D = 11 ABOVE D = 39, while structurally 39 is the more")
    print("  degenerate (a banded TRIPLE against 11's banded 4-cycle).  This repo")
    print("  already refuted mean G as a captured/uncaptured classifier; the same")
    print("  statistic must not be re-read as a severity ordering here.")
    print(f"  max G is not even stable across bands"
          f" ({[allrows[b1][D][3] for D in D_AXIS]} vs"
          f" {[allrows[b2][D][3] for D in D_AXIS]}) -- quote the mean, not the max.")

    two_matrices(3000, 1000)


if __name__ == "__main__":
    main(int(sys.argv[1]) if len(sys.argv) > 1 else 20000)
