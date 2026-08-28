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
            inwin = [r for _k, r in act if r < 2]
            hist[len(inwin)] += 1
            if len(inwin) == 1:
                rest = sorted(r for _k, r in act if r >= 2)
                if rest and (worst is None or rest[0] < worst[0]):
                    worst = (rest[0], a, b, m, [k for k, _ in act])

    print(f"X = {X}   slice y/x >= {SLOPE:.4f}   ratio classes in slice: {len(classes)}")
    print(f"  solutions with at least one acting multiplier : {nsol}")
    print(f"  in-window acting multipliers per solution     : {dict(sorted(hist.items()))}")
    two = sum(v for k, v in hist.items() if k >= 2)
    print()
    print(f"  SOLUTIONS WITH TWO OR MORE IN-WINDOW (i.e. a triple): {two}")
    if two:
        print("  ^^ Conjecture O.2 is FALSE and this is the counterexample.")
    elif hist.get(1):
        print(f"  none, over {hist[1]} solutions that carry one -- so every chance was taken")
    else:
        print("  none, and none carried even ONE -- this run proves nothing, raise X")
    if worst:
        r, a, b, m, act = worst
        print()
        print(f"  margin: smallest competing ratio alongside an in-window multiplier"
              f" is {r:.2f},")
        print(f"          at (a,b)=({a},{b}), m={m}, acting k={act[:6]} -- against the 2")
        print(f"          a window needs, so the nearest miss is a factor {r / 2:.1f} away.")


if __name__ == "__main__":
    main(int(sys.argv[1]) if len(sys.argv) > 1 else 3000)
