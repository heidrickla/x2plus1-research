"""Experiment 17 -- the sharp form of Conjecture O.2, measured on live solutions.

Supports Note O.  O.2 says no dyadic window holds three shared moduli.  Stated
that way it cannot be measured: the configuration never occurs, so every sweep
is vacuous, which is `triples-cannot-be-settled-by-measurement`.  Stated this way
it can be:

    SHARP FORM.  On any solution xi, at most one ACTING multiplier has
                 modulus ratio r < 2.

The two are equivalent -- a third modulus inside the window IS a second
in-window multiplier acting on the same xi -- but the sharp form is a statement
about configurations that DO occur, so a violation would be exhibited rather
than inferred from an absence.

WHAT "ACTING" MEANS.  tau_k acts on xi = (X, Y) when tau_k xi is again integral:

    M | U_k X + 2 k a Y    and    M | U_k Y + 2 k b X,     U_k^2 = M^2 + 4k^2 D.

Acting is orbit-invariant, because mod M we have b = a and the automorph
diagonalises S = X+Y, T = X-Y with UNIT eigenvalues -- so tau_k acts on every
member of a ratio class or on none.

MULTIPLIERS ACT FREELY, which is worth knowing before reading the result: the
acting set can be a whole cyclic semigroup.  (1,5) at m = 2 admits
k = 1, 3, 8, 21, 55, 144 -- exactly tau_1, tau_1^2, tau_1^3, since
tau_3 = (7+3 sqrt5)/2 = phi^4.  So "tau^2 is never integral" is FALSE in general;
Theorem O.3' forbids it only in the window regime, and (1,5) has r_1 = 6.854.
The content of O.2 is the window, not the integrality.

TWO BOUNDS MAKE A LARGE X REACHABLE.  A second in-window multiplier needs
M/sqrt(D) >= 5.657, i.e. b/a >= 33.97, i.e. y >= (3+2 sqrt2) x -- a thin slice of
the (x,y) square.  And an in-window multiplier has index k < M/(4 sqrt2 sqrt D),
so the k-loop is bounded by the geometry rather than by an arbitrary ceiling.
This script reaches past that bound deliberately, to report the margin.

READ THE INFORMATIVE COUNT, NOT THE TOTAL.  A solution whose (a,b) has only ONE
in-window multiplier could never have carried two, so it is vacuous for O.2.  At
X = 3000 there are 449 solutions carrying one and only THREE that are
informative; at X = 14000, 2093 and NINE.  Quoting the total is
`triples-cannot-be-settled-by-measurement` one level down, and this script
reported only the total until that was noticed.

Usage:  python experiments/exp17_sharp_form.py [X]
"""

import sys
from collections import Counter, defaultdict
from math import gcd, isqrt, sqrt

import _bootstrap  # noqa: F401

SLOPE = 3 + 2 * sqrt(2)          # y/x ~ sqrt(b/a) >= 3+2 sqrt2 = 5.8284


def ratio_classes_in_slice(X):
    """{(a,b): shared moduli} over pairs that could hold two in-window multipliers."""
    sq = [x * x + 1 for x in range(X + 1)]
    out = defaultdict(set)
    for x in range(1, int(X / SLOPE) + 2):
        sx = sq[x]
        for y in range(int(SLOPE * x), X + 1):
            g = gcd(sx, sq[y])
            if g > 1:
                out[(sx // g, sq[y] // g)].add(g)
    return out


def acting(a, b, m, mult):
    """Indices in `mult` whose multiplier is integral on the solution at m."""
    M = b - a
    X_, Y_ = isqrt(a * m - 1), isqrt(b * m - 1)
    return [(k, r) for k, U, r in mult
            if (U * X_ + 2 * k * a * Y_) % M == 0
            and (U * Y_ + 2 * k * b * X_) % M == 0]


def multipliers(a, b, reach=6):
    """(k, U_k, modulus ratio) for k up to `reach` times the in-window bound."""
    M, D = b - a, a * b
    kmax = int(reach * M / (4 * sqrt(2) * sqrt(D))) + 4
    out = []
    for k in range(1, kmax + 1):
        t = M * M + 4 * k * k * D
        U = isqrt(t)
        if U * U == t:
            s = 4 * k * sqrt(D) / M
            out.append((k, U, ((s + sqrt(s * s + 4)) / 2) ** 2))
    return out


def main(X=3000):
    classes = ratio_classes_in_slice(X)
    hist = Counter()
    nsol = 0
    informative = 0
    worst = None
    for (a, b), ms in classes.items():
        mult = multipliers(a, b)
        if not mult:
            continue
        for m in sorted(ms):
            act = acting(a, b, m, mult)
            if not act:
                continue
            nsol += 1
            if sum(1 for _k, _U, r in mult if r < 2) >= 2:
                informative += 1
            inwin = [r for _k, r in act if r < 2]
            hist[len(inwin)] += 1
            if len(inwin) == 1:
                rest = sorted(r for _k, r in act if r >= 2)
                if rest and (worst is None or rest[0] < worst[0]):
                    worst = (rest[0], a, b, m, [k for k, _ in act])

    print(f"X = {X}   slice y/x >= {SLOPE:.4f}   ratio classes in slice: {len(classes)}")
    print(f"  solutions with at least one acting multiplier : {nsol}")
    print(f"  in-window acting multipliers per solution     : {dict(sorted(hist.items()))}")
    print(f"  INFORMATIVE -- their (a,b) has >=2 in-window multipliers, so a")
    print(f"                 second COULD have acted                : {informative}")
    two = sum(v for k, v in hist.items() if k >= 2)
    print()
    print(f"  SOLUTIONS WITH TWO OR MORE IN-WINDOW (i.e. a triple): {two}")
    if two:
        print("  ^^ Conjecture O.2 is FALSE and this is the counterexample.")
    elif informative:
        print(f"  none, over {informative} INFORMATIVE solutions -- and note that is the")
        print(f"  number that matters, not the {hist.get(1,0)} carrying one.  A solution whose")
        print(f"  (a,b) has only ONE in-window multiplier could never have carried two.")
    elif hist.get(1):
        print(f"  none -- but ZERO solutions were informative, so this run proves nothing")
        print(f"  about O.2.  Raise X until the informative count is positive.")
    else:
        print("  none, and none carried even ONE -- this run proves nothing, raise X")
    if worst:
        r, a, b, m, act = worst
        print()
        print(f"  margin: smallest competing ratio alongside an in-window multiplier"
              f" is {r:.2f},")
        print(f"          at (a,b)=({a},{b}), m={m}, acting k={act[:6]} -- against the 2")
        print(f"          a window needs, so the nearest miss is a factor {r / 2:.1f} away.")


def chain_census(X=1500):
    """How many classes admit TWO in-window multipliers?  That is O.2's population.

    A triple needs a CHAIN: two indices k with M^2 + 4k^2 D a perfect square and
    tau_k^2 < 2.  This counts them over every reduced ratio class, which is the
    right denominator for O.2 -- not classes above a threshold, not classes with
    three shared moduli.

    CAUTION: "realises two moduli" is NOT "realises two moduli in one window".
    The two first diverge at X = 6000, where (13,27145) has moduli 2 and 530, a
    ratio of 265.  Both are reported.
    """
    from math import isqrt, sqrt
    from x2plus1.polyseq import ratio_classes
    cls = ratio_classes(X)
    hist = {}
    two = []
    for (a, b), ms in cls.items():
        M, D = b - a, a * b
        ks = []
        for k in range(1, int(M / (4 * sqrt(2) * sqrt(D))) + 1):
            t = M * M + 4 * k * k * D
            U = isqrt(t)
            if U * U == t:
                ks.append(k)
        hist[len(ks)] = hist.get(len(ks), 0) + 1
        if len(ks) >= 2:
            two.append((a, b, ks, sorted(ms)))
    print()
    print(f"CHAIN CENSUS at X = {X}: {len(cls)} reduced ratio classes")
    for k in sorted(hist):
        print(f"   in-window multipliers = {k}: {hist[k]:>9}")
    print(f"  classes admitting a CHAIN (>= 2): {len(two)}  <- O.2's population")
    nm = {}
    inwin = 0
    for _a, _b, _k, ms in two:
        nm[len(ms)] = nm.get(len(ms), 0) + 1
        if len(ms) >= 2 and any(ms[j] < 2 * ms[i]
                                for i in range(len(ms)) for j in range(i + 1, len(ms))):
            inwin += 1
    print(f"  moduli realised by those: {dict(sorted(nm.items()))}")
    print(f"  of them, with two moduli IN ONE WINDOW: {inwin}")
    for a, b, ks, ms in two:
        if len(ms) >= 2:
            r = ms[1] / ms[0]
            print(f"     (a,b)=({a},{b})  k={ks}  moduli={ms}  ratio {r:.3f}"
                  f"  {'in one window' if r < 2 else 'NOT in one window'}")
    mx = max(nm) if nm else 0
    print(f"  Maximum moduli realised at THIS X: {mx}, against the three a triple")
    print(f"  needs.  Across X = 1500/3000/6000 the maxima are 1/2/2.")
    print("  A chain needs u = b/a > 129.9923 = (4sqrt2+sqrt33)^2, while the")
    print("  modulus supply FALLS with u -- the two requirements pull opposite")
    print("  ways, which is why this set is empty.")


if __name__ == "__main__":
    XX = int(sys.argv[1]) if len(sys.argv) > 1 else 3000
    main(XX)
    chain_census(min(1500, XX))
