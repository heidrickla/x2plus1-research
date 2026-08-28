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


def o15_coverage(sizes=(3000, 6000)):
    """How much of the LIVE population does O.15's threshold remove?

    O.15: a windowed triple needs u > 82.5571 (117.4171 if a, b both odd).  The
    question is what that excludes, and the answer depends entirely on the
    denominator -- which is the trap this repo records most often.

      all unit-free classes            millions; a coverage figure over these is
                                       meaningless, since almost none can host a
                                       triple at all
      >= 3 shared moduli ANYWHERE      the informative population: a class with
                                       fewer cannot hold three in a window
      2 in one window                  the near-miss population

    Reported with the direction of travel, because a reach that FALLS with X is a
    different object from one that is flat, and this one falls.
    """
    from x2plus1.polyseq import ratio_classes

    def win(ms):
        ms = sorted(ms)
        return max((sum(1 for q in ms if p <= q < 2 * p) for p in ms), default=0)

    print("  O.15 threshold u > 82.5571 (unconditional branch)")
    print(f"  {'X':>6} {'all':>10} {'>=3 moduli':>11} {'excluded':>10}"
          f" {'2 in window':>12} {'excluded':>10}")
    for X in sizes:
        cls = ratio_classes(X)
        tot = three = three_hi = two = two_hi = 0
        for (a, b), ms in cls.items():
            if a == 1:                     # unit cofactor: no Type II hypothesis admits it
                continue
            tot += 1
            u = b / a
            if len(ms) >= 3:
                three += 1
                three_hi += u > 82.5571
            if win(ms) >= 2:
                two += 1
                two_hi += u > 82.5571
        e3 = f"{100*(three-three_hi)/three:.0f}%" if three else "-"
        e2 = f"{100*(two-two_hi)/two:.0f}%" if two else "-"
        print(f"  {X:>6} {tot:>10} {three:>11} {e3:>10} {two:>12} {e2:>10}")
    print("  The informative reach FALLS with X (88% -> 70%), so no claim is made")
    print("  about its limit.  Quoting the figure over all classes instead would")
    print("  give ~99% and mean nothing.")


def alternation_does_not_extend(X=3000):
    """O.18 -- route nine on O.2, closed.

    O.7 closes O.2 for M an odd PRIME by parity: two steps flip the subcase
    twice, the one-step composite flips it once, and O.6's dichotomy forbids
    both.  O.17 shows the composite integrality criterion is a PER-PRIME sign,
    which suggests the alternation is too -- and if it were, the parity argument
    would run at each prime of any odd M and close O.2 for all odd M.

    It does not.  O.6's dichotomy (exactly one of M | S, M | T) is proved using
    M prime: both holding would give M | 4pa hence M | p.  At a prime power
    dividing a composite M that step does not survive, which is what the
    dichotomy failures below are.

    Unit-free only (a >= 2): a = 1 is inadmissible for any Type II hypothesis, so
    counterexamples there would prove nothing.
    """
    from collections import Counter
    from math import isqrt

    from sympy import factorint

    from x2plus1.polyseq import ratio_classes

    cls = ratio_classes(X)
    stat = Counter()
    examples = []
    for (a, b), ms in cls.items():
        M = b - a
        if M % 2 == 0 or M == 1 or a == 1:
            continue
        ms = sorted(ms)
        if len(ms) < 2:
            continue
        primes = list(factorint(M))
        if len(primes) < 2:                  # M odd PRIME is O.7's case
            continue
        Xs = [isqrt(a * m - 1) for m in ms]
        Ys = [isqrt(b * m - 1) for m in ms]
        if any(x * x != a * m - 1 for x, m in zip(Xs, ms)):
            continue
        for r in primes:
            sub = [((xi + yi) % r == 0, (xi - yi) % r == 0) for xi, yi in zip(Xs, Ys)]
            if any(s[0] == s[1] for s in sub):
                stat["dichotomy fails -- no local sign"] += 1
                continue
            code = [1 if s[0] else -1 for s in sub]
            same = sum(1 for i in range(len(code) - 1) if code[i] == code[i + 1])
            stat["alternates at every step" if same == 0 else "does NOT always alternate"] += 1
            if same and len(examples) < 6:
                examples.append((a, b, M, r, code))

    print(f"  X = {X}, unit-free classes with M odd COMPOSITE and >= 2 shared moduli,")
    print("  per prime r | M:")
    for k, v in stat.most_common():
        print(f"    {v:>6}  {k}")
    print("  counterexamples (a, b, M, r, subcase codes):")
    for e in examples:
        print(f"    {e}")
    print("  So the alternation is a statement about M PRIME, not about each prime")
    print("  of M: the per-prime structure O.17 exposes for the composite criterion")
    print("  does not propagate to the alternation.  Ninth route closed.")


if __name__ == "__main__":
    main(int(sys.argv[1]) if len(sys.argv) > 1 else 3000,
         int(sys.argv[2]) if len(sys.argv) > 2 else 20_000_000)
    o15_coverage()
    alternation_does_not_extend(min(3000, max(800, int(sys.argv[1]) if len(sys.argv) > 1 else 3000)))
    bipartite_structure(min(4000, max(1200, int(sys.argv[1]) if len(sys.argv) > 1 else 4000)), top=60)


def bipartite_structure(X=4000, top=120):
    """BD_2(-1): the bipartite Diophantine tuple structure of x^2+1.

    Tsang-Yip (arXiv:2512.03441v3) define (A,B) to have property BD_k(n) when
    ab + n is a k-th power for every a in A, b in B.  With k = 2, n = -1 that is
    exactly this repo's object: A a set of cofactors, B a set of moduli, ab - 1 a
    square, since a*m = x^2+1.

    Their Question 1.3 asks for the smallest l such that |A| = l forces |B|
    absolutely bounded.  They record l <= 9, 6, 5, 4 for k = 3, 4, 5, >= 6, and
    then: "when k = 2, we do not know any upper bound on l."  Under the
    uniformity conjecture they predict l <= 5 for k = 2.

    MEASURED HERE: l = 3.  |A| = 2 does not bound |B| -- (1,5) already shares 8
    moduli, and each Pell solution class contributes an infinite geometric family.
    |A| = 3 appears to force |B| <= 2: no K_{3,3} among the highest-degree
    cofactors, while K_{3,2} occurs.

    Evidence of absence in the region where the configuration would be most
    likely, NOT a proof -- and sharper than the conjectural bound, which is
    exactly the situation this repo's rules say to distrust.
    """
    from collections import defaultdict
    from itertools import combinations

    inc = defaultdict(set)
    for x in range(1, X + 1):
        v = x * x + 1
        d = 1
        while d * d <= v:
            if v % d == 0:
                inc[v // d].add(d)
                if d * d != v:
                    inc[d].add(v // d)
            d += 1

    print(f"  X = {X}: {len(inc)} cofactors in the bipartite (cofactor, modulus) incidence")
    pool = sorted(inc)[:1500]
    best = max(((len(inc[a] & inc[b]), a, b) for a, b in combinations(pool, 2)),
               default=(0, 0, 0))
    print(f"  |A| = 2: largest |B| among the first 1500 cofactors is {best[0]}"
          f" at ({best[1]}, {best[2]}) -- unbounded as X grows")

    ns = sorted(inc, key=lambda n: -len(inc[n]))[:top]
    k33 = k32 = None
    triples = 0
    for a, b, c in combinations(ns, 3):
        triples += 1
        s = inc[a] & inc[b] & inc[c]
        if len(s) >= 3 and k33 is None:
            k33 = (a, b, c, sorted(s)[:4])
        if len(s) >= 2 and k32 is None:
            k32 = (a, b, c, sorted(s))
    print(f"  K_3,3 over the {top} highest-degree cofactors ({triples:,} triples):"
          f" {k33 if k33 else 'NONE FOUND'}")
    print(f"  K_3,2 (three cofactors, two shared moduli): {k32 if k32 else 'none'}")
    print("  So the measured l is 3, against a literature with no bound for k = 2")
    print("  and a conjectural l <= 5.  Measured, not proved.")
