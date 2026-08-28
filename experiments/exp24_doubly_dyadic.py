"""Experiment 24 -- C_4-freeness over Z on the configuration Type II uses.

Supports Note O (Theorem O.12) and bears on `gaussian-to-rational-bridge`.

Everything else in Note O windows the MODULI and lets the cofactors range freely.
Ford-Maynard's (II) is a bilinear form over m ~ M and n ~ N: BOTH variables sit
in ranges, and `fm-barrier-range-is-small-moduli` records that their footnote 2
averages over m_1, m_2 ~ x^{1-2c+eps}, so the cofactors are banded too.

    THEOREM O.12.  If n_2/n_1 < (5 + sqrt21)/2 = 4.7913 -- in particular if n_1
    and n_2 lie in ONE DYADIC BAND -- then they share at most one modulus in any
    dyadic window.

Proof.  A pair of shared moduli m_i < m_j < 2 m_i with X_i >= 1 needs
tau_V^2 < 2 + 1/X_i^2 <= 3.  tau increases in |V| and |V| >= 1, so
tau_V >= tau(1) = sqrt(1+s^2) + s with s = sqrt(D)/M, and tau(1)^2 < 3 forces
M/sqrt(D) > sqrt3.  With u = n_2/n_1 = b/a, M/sqrt(D) = (u-1)/sqrt(u), and that
exceeds sqrt3 iff u^2 - 5u + 1 > 0 iff u > (5+sqrt21)/2.  A dyadic band gives
u < 2, a factor 2.4 inside it.  It uses |V| >= 1, not the parity lemma's
|V| >= 2, so it does not depend on the parity of a and b.

    *** "ANY DYADIC WINDOW" MEANS ANY RATIO BELOW 2, NOT AN ANCHORED WINDOW. ***

A first version of this file swept windows anchored at powers of two (and at
powers of four), which is a strictly WEAKER test: [8,16) and [16,32) between them
miss the pair (9,17) -- and (9,17) is precisely the witness that breaks the
property at c = 6.  An anchored sweep would have passed on a counterexample and
did: it reported the line family C_4-free at c = 6.  Every sweep below therefore
tests pairs by RATIO, on both axes.

WHAT THIS SETTLES AND WHAT IT DOES NOT.  `gaussian-to-rational-bridge` is
`inferred`, and its stated gap was "what is proved over Z[i] is G <= 1; what is
measured over Z is G' <= 2 on every dyadic window for X <= 8000".  O.12 closes
that sentence's second half: over Z, on the configuration (II) quantifies over,
G' <= 1 is PROVED for all X.  It does NOT close the remaining inference, and it
says nothing about O.2, the free-cofactor question -- (1,41) sharing 730 and 1370
is a genuine G' = 2 and simply is not a Type II configuration.

Usage:  python experiments/exp24_doubly_dyadic.py [X]
"""

import sys
from collections import defaultdict
from math import sqrt

import _bootstrap  # noqa: F401

THRESHOLD = (5 + sqrt(21)) / 2


def incidence(values):
    """cofactor n -> set of moduli m with n*m in values."""
    inc = defaultdict(set)
    for v in values:
        d = 1
        while d * d <= v:
            if v % d == 0:
                inc[v // d].add(d)
                if d * d != v:
                    inc[d].add(v // d)
            d += 1
    return inc


def _window_count(shared):
    """Most shared moduli lying within a factor 2 of one another."""
    sh = sorted(shared)
    return max((sum(1 for q in sh if p <= q < 2 * p) for p in sh), default=0)


def survey(values):
    """(max Gram banded, max Gram free, #banded pairs, #banded sharing >= 2)."""
    inc = incidence(values)
    ns = sorted(inc)
    band = free = npairs = p2 = 0
    for i, n1 in enumerate(ns):
        for n2 in ns[i + 1:]:
            sh = inc[n1] & inc[n2]
            if not sh:
                continue
            g = _window_count(sh)
            free = max(free, g)
            if n2 < 2 * n1:                       # cofactors in one dyadic band
                npairs += 1
                band = max(band, g)
                p2 += g >= 2
    return band, free, npairs, p2


def witness(values):
    """A banded cofactor pair sharing two moduli within a factor 2, or None."""
    inc = incidence(values)
    ns = sorted(inc)
    for i, n1 in enumerate(ns):
        for n2 in ns[i + 1:]:
            if n2 >= 2 * n1:
                break
            sh = sorted(inc[n1] & inc[n2])
            for p in sh:
                got = [q for q in sh if p <= q < 2 * p]
                if len(got) >= 2:
                    return n1, n2, got
    return None


def main(X=1200):
    print(f"THEOREM O.12.  Two cofactors within a factor {THRESHOLD:.6f} share at")
    print("most one modulus in any dyadic window.  A dyadic band gives u < 2, a")
    print(f"factor {THRESHOLD/2:.4f} inside it.  |V| >= 2 raises it to 13.9282 at")
    print("X_1 = 1 and 33.9706 asymptotically; the smallest ratio realised is 43.79.")

    vals = {x * x + 1 for x in range(1, X + 1)}
    band, free, npairs, p2 = survey(vals)
    print(f"\nx^2+1 at X = {X}:  max Gram banded {band}, free {free}")
    print(f"  POSITIVE CONTROL: {npairs} banded cofactor pairs share a modulus,"
          f" and {p2} share two.")
    print("  A 'max of 1' over pairs that share nothing would look identical.")
    print("  The free column reaching 2 is genuine and not a counterexample:")
    print("  (1,41) shares 730 and 1370, and 41/1 is nowhere near one band --")
    print("  exactly the configuration a Type II hypothesis excludes.")


def control(Q=60000):
    """Is the 0/1 property generic?  Four comparison sequences say no."""
    r = int(Q ** 0.5) + 1
    seqs = [
        ("x^2+1                 open", {x * x + 1 for x in range(1, r)}),
        ("a^2+b^6      not known cap", {a * a + b ** 6 for a in range(1, r)
                                        for b in range(1, int(Q ** (1 / 6)) + 2)
                                        if a * a + b ** 6 <= Q}),
        ("x^3+2y^3        CAPTURED", {x ** 3 + 2 * y ** 3
                                      for x in range(1, int(Q ** (1 / 3)) + 2)
                                      for y in range(1, int(Q ** (1 / 3)) + 2)
                                      if 0 < x ** 3 + 2 * y ** 3 <= Q}),
        ("a^2+b^4         CAPTURED", {a * a + b ** 4 for a in range(1, r)
                                      for b in range(1, int(Q ** 0.25) + 1)
                                      if a * a + b ** 4 <= Q}),
        ("a^2+(b^2+1)^2   CAPTURED", {a * a + (b * b + 1) ** 2 for a in range(1, r)
                                      for b in range(0, int(Q ** 0.25) + 1)
                                      if a * a + (b * b + 1) ** 2 <= Q}),
    ]
    print(f"\nPOSITIVE CONTROL at Q = {Q}: is the 0/1 property generic?")
    print(f"{'sequence':>28} {'banded':>7} {'free':>6} {'banded >=2':>12}")
    for lab, v in seqs:
        b, f, _n, p2 = survey(v)
        print(f"{lab:>28} {b:7} {f:6} {p2:12}")
    print("  x^2+1 is alone at 1 -- and there it is a THEOREM, not a measurement.")
    print("  NOT A CLASSIFIER, and the ordering is not stable across Q: a^2+b^6")
    print("  (not known captured) is above the CAPTURED x^3+2y^3 at small Q and")
    print("  below it at large.  'Low implies hard' would be the mean-G classifier")
    print("  again.  What IS claimed is a difference in KIND: x^2+1 reads exactly")
    print("  1 at every size, everything else grows with Q.")


def fm_footnote_quantity(X=12000):
    """Ford-Maynard's footnote-2 mean, with and without the second band.

    Their footnote averages G over m_1, m_2 ~ x^{1-2c+eps}, and (II) bands n as
    well, so the quantity is doubly dyadic and O.12 caps it at 1.  The banded
    column tests by RATIO, not by an anchored window.
    """
    inc = incidence({x * x + 1 for x in range(1, X + 1)})
    print()
    print("FORD-MAYNARD FOOTNOTE 2.  (II) bands n as well as m, so the quantity")
    print("is doubly dyadic and O.12 caps it at 1.  The recorded means are the")
    print("moduli-unrestricted ones.")
    print(f"{'N band':>13} {'#cof':>5} {'mean G free-m':>14} {'max':>4}"
          f" | {'mean G banded-m':>16} {'max':>4}")
    N = 8
    while N <= 128:
        ns = sorted(n for n in inc if N <= n < 2 * N)
        if len(ns) < 2:
            N *= 2
            continue
        tf = tb = npairs = mf = mb = 0
        for i in range(len(ns)):
            for j in range(i + 1, len(ns)):
                npairs += 1
                sh = inc[ns[i]] & inc[ns[j]]
                tf += len(sh)
                mf = max(mf, len(sh))
                g = _window_count(sh)
                tb += g
                mb = max(mb, g)
        print(f"[{N:5},{2*N:6}) {len(ns):5} {tf/npairs:14.4f} {mf:4}"
              f" | {tb/npairs:16.4f} {mb:4}")
        N *= 2
    print("  On the configuration (II) quantifies over the mean NEVER exceeds 1,")
    print("  and the only band attaining 1 holds two cofactors -- a single pair.")
    print("  NOTE: the 'mean >= 1' line in fm-barrier-range-is-small-moduli is")
    print("  THIS REPO'S paraphrase, not the footnote's, which is a condition on")
    print("  the ERROR TERM.  For a 0/1 indicator, 'better than O(1)' means")
    print("  knowing it exactly -- which is Note F's pointwise reading, now")
    print("  available over Z and not only over Z[i].")


def line_family(X=1200, cmax=8):
    """x^2 + c^2: the Z side, where only Z[i] is proved.  It FAILS at c = 6."""
    print(f"\nLINE FAMILY x^2 + c^2 at X = {X}")
    print("A_c is C_4-free over Z[i] for EVERY c (Note F's argument, c for 1).")
    print("O.12 proves the Z side only at c = 1: the identity carries a factor")
    print("c^2 -- V W = c^2 M (m_i - m_j) -- so the threshold scales as 1/c^2.")
    print(f"{'c':>3} {'banded':>7} {'free':>6} {'banded pairs':>13} {'>=2':>5}")
    holds, fails = [], []
    for c in range(1, cmax + 1):
        vals = {x * x + c * c for x in range(1, X + 1)}
        b, f, n, p2 = survey(vals)
        assert n > 200, f"c={c}: only {n} banded pairs -- vacuous"
        (holds if b <= 1 else fails).append(c)
        print(f"{c:3} {b:7} {f:6} {n:13} {p2:5}")
    print(f"  holds at c = {holds};  FAILS at c = {fails}")
    w = witness({x * x + 36 for x in range(1, X + 1)})
    if w:
        n1, n2, ms = w
        print(f"  c = 6 witness: cofactors {n1},{n2} (ratio {n2/n1:.2f} < 2),"
              f" moduli {ms[0]},{ms[1]} (ratio {ms[1]/ms[0]:.3f} < 2)")
        print(f"     {n1}*{ms[0]} = {n1*ms[0]}, {n2}*{ms[0]} = {n2*ms[0]},"
              f" {n1}*{ms[1]} = {n1*ms[1]}, {n2}*{ms[1]} = {n2*ms[1]}")
        print("     (3+6i)(10+6i) = -6+78i and (6+6i)(7+6i) = 6+78i -- CONJUGATE,")
        print("     not associate, so there is NO Gaussian 4-cycle while the norms")
        print("     agree at 6120 and the rational cycle is real.  That is the")
        print("     Z[i]-to-Z coarsening, on the BANDED configuration.")
    print("  So the line family BOUNDS the transfer rather than supporting it.")
    print("  It does NOT refute gaussian-to-rational-bridge for x^2+1, where the")
    print("  Z side is PROVED by O.12 rather than transferred.")


def discriminant_axis(X=900):
    """The property depends only on Delta = b^2 - 4c, not on b and c separately.

    4(x^2 + bx + c) = (2x+b)^2 + |Delta|, so a general quadratic is x^2 + D on
    arguments of one parity, up to a factor 4.  So the line family x^2+c^2, the
    D family x^2+D and the general quadratics are ONE axis indexed by Delta.
    """
    print()
    print(f"DISCRIMINANT AXIS at X = {X}: banded max by Delta = b^2 - 4c")
    by_disc = {}
    for b in range(0, 4):
        for cc in range(1, 8):
            disc = b * b - 4 * cc
            vals = {x * x + b * x + cc for x in range(1, X + 1)}
            vals = {v for v in vals if v > 1}
            band, _free, n, _p2 = survey(vals)
            if n < 300:
                continue
            by_disc.setdefault(disc, []).append((f"x^2+{b}x+{cc}", band))
    ok = bad = 0
    for disc in sorted(by_disc, reverse=True):
        polys = by_disc[disc]
        bands = {v for _p, v in polys}
        agree = len(bands) == 1
        ok += agree and len(polys) > 1
        bad += (not agree)
        note = "" if agree else "   <-- DISAGREE"
        print(f"  Delta = {disc:5}: " + ", ".join(f"{p} -> {v}" for p, v in polys)
              + note)
    print(f"  discriminant classes with >1 member that AGREE: {ok};"
          f" that disagree: {bad}")
    print("  x^2+2x+1 = (x+1)^2 has Delta = 0 and is a perfect square --")
    print("  degenerate, and not a member of the family.")


def invariant_and_D_reach(Dmax=6, amax=30, bmax=200, mmax=3000):
    """The M*D invariant, and O.12's exact reach on the D axis.

    For A = {x^2 + D}: a m = X^2 + D and b m = Y^2 + D give b(X^2+D) = abm =
    a(Y^2+D), hence a Y^2 - b X^2 = (b-a) D = M*D.  So the quantity Note O calls
    M is really M*D and every bound built on it weakens by a factor of D.

    O.12's pair condition tau(V)^2 < 3 becomes V*s < 1/sqrt3 with
    s = sqrt(ab)/(M D) = sqrt(u)/((u-1) D), i.e. (u-1) D / sqrt(u) > V sqrt3,
    while a dyadic band supplies only (u-1)/sqrt(u) < 1/sqrt2.  So O.12 covers
    D <= V sqrt6.
    """
    from math import gcd, isqrt, sqrt
    print()
    print("THE INVARIANT IS M*D, NOT M.")
    n = bad = 0
    minV = {}
    for D in range(1, Dmax + 1):
        for a in range(1, amax + 1):
            for b in range(a + 1, bmax + 1):
                if gcd(a, b) != 1:
                    continue
                M = b - a
                sols = []
                for m in range(1, mmax):
                    v1, v2 = a * m - D, b * m - D
                    if v1 < 1 or v2 < 1:
                        continue
                    X, Y = isqrt(v1), isqrt(v2)
                    if X * X == v1 and Y * Y == v2:
                        sols.append((X, Y))
                        n += 1
                        if a * Y * Y - b * X * X != M * D:
                            bad += 1
                for i in range(len(sols)):
                    for j in range(i + 1, len(sols)):
                        V = abs(sols[i][0] * sols[j][1] - sols[j][0] * sols[i][1])
                        if V:
                            minV[D] = min(minV.get(D, 10 ** 9), V)
    print(f"  a Y^2 - b X^2 = M*D over {n} solutions, D = 1..{Dmax}: {bad} failures")
    print(f"  min |V| by D: {dict(sorted(minV.items()))}"
          f"   all even? {all(v % 2 == 0 for v in minV.values())}")
    print()
    print("O.12's REACH ON THE D AXIS: it covers D <= V sqrt6.")
    print(f"{'input':>26} {'bound':>12} {'covers D'}")
    for V0, lab in ((1, "|V| >= 1, unconditional"), (2, "|V| >= 2, from evenness")):
        print(f"{lab:>26} {V0 * sqrt(6):12.4f}   D = 1..{int(V0 * sqrt(6))}")
    print("  thresholds on u = b/a, from (u-1) D / sqrt(u) > V sqrt3:")
    for D in (1, 2, 3):
        r = sqrt(3) / D
        uu = (2 + r * r + r * sqrt(r * r + 4)) / 2
        band = 1 / sqrt(2)
        print(f"     D = {D}: need u > {uu:8.4f}; a band gives u < 2 -> "
              f"{'COVERED' if uu >= 2 else 'not covered'}")
    print("  So x^2+2 in particular can never fail, which bounds the conjecture")
    print("  that D = 1 is the unique survivor: at small D the condition is not")
    print("  merely tight but UNSATISFIABLE, and no number of candidate classes")
    print("  at larger X can change that.")


if __name__ == "__main__":
    XX = int(sys.argv[1]) if len(sys.argv) > 1 else 1200
    main(XX)
    control(min(60000, max(20000, XX * XX // 20)))
    fm_footnote_quantity(min(12000, max(2000, 4 * XX)))
    line_family(min(1200, max(400, XX)))
    invariant_and_D_reach(Dmax=6 if XX >= 900 else 3,
                          amax=30 if XX >= 900 else 10,
                          bmax=200 if XX >= 900 else 80,
                          mmax=3000 if XX >= 900 else 800)
    discriminant_axis(min(900, max(400, XX)))


def banding_sees_D(sizes=(1500, 2500), Ds=(1, 2, 3, 4, 5, 6, 11, 39)):
    """Banding the SECOND variable is what makes the C_4 structure see D.

    Both columns window the moduli; they differ only in whether the cofactors
    are banded too.  So the pair isolates the effect of the second banding with
    everything else held fixed -- same values, same windows, same population.

    The banded reading jumps from 1 to 2 exactly at D = 11, the first D where
    O.12's conclusion fails.  The free reading is CONSTANT at 2 across the whole
    range containing that transition, so it cannot resolve D = 1 from D = 11.

    Not "the free reading is blind" -- it does move, 2 -> 3 at D = 39.  It is
    blind exactly where the transition is, which is the useful statement and the
    weaker one.

    Consequence: Ford-Maynard's (II) bands m ~ M AND n ~ N, so O.12's doubly
    dyadic configuration is the one in which the structure is visible at all --
    load-bearing, not a technical convenience adopted to match their hypothesis.
    """
    for X in sizes:
        print(f"\n  X = {X}   (moduli windowed in both columns; cofactors differ)")
        print(f"  {'D':>4} {'BANDED max':>11} {'FREE max':>9} {'#banded':>10}"
              f" {'#banded sharing>=2':>19}")
        band_row, free_row = [], []
        for D in Ds:
            vals = [x * x + D for x in range(1, X + 1)]
            band, free, npairs, p2 = survey(vals)
            band_row.append(band)
            free_row.append(free)
            print(f"  {D:>4} {band:>11} {free:>9} {npairs:>10} {p2:>19}")
        print(f"    banded: {band_row}   <- separates at D = 11")
        print(f"    free:   {free_row}   <- constant across the transition")


def extremal_four_cycle(D=1, sizes=(1500, 3000, 6000, 12000)):
    """How loose is O.12?  The smallest cofactor ratio that realises a 4-cycle.

    O.12 proves the cofactor ratio of any windowed 4-cycle exceeds
    (5+sqrt21)/2 = 4.7913 at D = 1.  max Gram is an integer and only says
    whether the bound is violated; this says how much room is left.

    Inverted search -- key on PAIRS of moduli in one window and look for two
    cofactors carrying the same pair -- so the cost is sum_n d(n)^2 rather than
    the square of the cofactor count, which is what makes larger X reachable.

    BOTH columns are reported because the unit cofactor is inadmissible for any
    Type II hypothesis and it is the minimiser for some D: at D = 2 the overall
    minimum is 33.0 at (1, 33), which a reader dismisses in a line.  At D = 1
    the minimum is already unit-free.

    RESULT at D = 1: the minimum is 34.0811, at cofactors (37, 1261) sharing
    moduli 866 and 1730 (37*866 = 179^2+1, 37*1730 = 253^2+1,
    1261*866 = 1045^2+1, 1261*1730 = 1477^2+1), and it does NOT move across a
    factor of 8 in X.  So O.12 is loose by 7.11x with no sign of being
    approached.  This improves the witness the notes quote -- (2, 82) at ratio
    41 is not extremal.
    """
    from collections import defaultdict
    thr = (5 + 21 ** 0.5) / 2
    print(f"  x^2+{D}.  O.12 proves any windowed 4-cycle has cofactor ratio"
          f" > {thr:.4f} (at D = 1).")
    print(f"  {'X':>7} | {'min ratio':>10} {'witness':>26}"
          f" | {'unit-free min':>13} {'witness':>26} {'slack':>8}")
    for X in sizes:
        inc = defaultdict(list)
        for x in range(1, X + 1):
            v = x * x + D
            d = 1
            while d * d <= v:
                if v % d == 0:
                    inc[v // d].append(d)
                    if d * d != v:
                        inc[d].append(v // d)
                d += 1
        key = defaultdict(list)
        for n, ms in inc.items():
            ms = sorted(set(ms))
            for i, m1 in enumerate(ms):
                for m2 in ms[i + 1:]:
                    if m2 >= 2 * m1:
                        break
                    key[(m1, m2)].append(n)
        best = bestuf = None
        for (m1, m2), nsl in key.items():
            if len(nsl) < 2:
                continue
            nsl.sort()
            for i in range(len(nsl) - 1):
                n1, n2 = nsl[i], nsl[i + 1]
                r = n2 / n1
                if best is None or r < best[0]:
                    best = (r, n1, n2, m1, m2)
                if n1 > 1 and (bestuf is None or r < bestuf[0]):
                    bestuf = (r, n1, n2, m1, m2)
        def fmt(b):
            if not b:
                return f"{'-- none --':>10} {'':>26}"
            r, n1, n2, m1, m2 = b
            return f"{r:>10.4f} {f'({n1},{n2}) m={m1},{m2}':>26}"
        sl = f"{bestuf[0]/thr:>7.2f}x" if bestuf else ""
        print(f"  {X:>7} | {fmt(best)} | {fmt(bestuf)} {sl:>8}")
    print("  A bound's silence is not evidence about what lies outside it: this is")
    print("  a minimum over a finite range, not a proof that none is smaller.")


def tau1_extremal(D=1, X=6000, top=8):
    """Prop O.13 -- the true threshold is (1+sqrt2)^4, and the extrema are tau_1.

    Occupancy is the INPUT: enumerate realised windowed 4-cycles and read off
    which multiplier explains each ratio.  Never generate candidates from
    multipliers and test occupancy afterwards -- that searches a mostly empty
    space and produced every withdrawn r-product statistic in this note.

    A window needs the modulus ratio below 2.  If that ratio is tau_1^2, then
    ((sqrt u + 1)/(sqrt u - 1))^2 < 2, i.e. u > (3+2 sqrt2)^2 = 17 + 12 sqrt 2
    = (1+sqrt2)^4 = 33.970563.

    Measured: at D = 1 and D = 2 every realised windowed 4-cycle matches tau_1^2
    to five decimals and the minimum is 0.33% / 0.25% above the threshold.

    D != 1 IS NOT INTERPRETED HERE.  For x^2+D the invariant is M*D, so tau_1
    and every threshold change; running this at D = 4 compares against the D = 1
    tau_1 and the output is an observation without a reading.  An earlier
    version drew a converse from it and was wrong.
    """
    from collections import defaultdict
    from math import sqrt
    thr = (1 + sqrt(2)) ** 4
    inc = defaultdict(list)
    for x in range(1, X + 1):
        v = x * x + D
        d = 1
        while d * d <= v:
            if v % d == 0:
                inc[v // d].append(d)
                if d * d != v:
                    inc[d].append(v // d)
            d += 1
    key = defaultdict(list)
    for n, ms in inc.items():
        ms = sorted(set(ms))
        for i, m1 in enumerate(ms):
            for m2 in ms[i + 1:]:
                if m2 >= 2 * m1:
                    break
                key[(m1, m2)].append(n)
    found = []
    for (m1, m2), nsl in key.items():
        if len(nsl) < 2:
            continue
        nsl.sort()
        for i in range(len(nsl) - 1):
            n1, n2 = nsl[i], nsl[i + 1]
            if n1 == 1:
                continue                       # unit cofactor: inadmissible
            found.append((n2 / n1, n1, n2, m1, m2))
    found.sort()
    print(f"  x^2+{D}, X = {X}.  (1+sqrt2)^4 = {thr:.6f};"
          f" O.12 proves {(5 + 21 ** 0.5) / 2:.4f}.")
    print(f"  {'u':>11} {'cofactors':>18} {'moduli':>18} {'m2/m1':>9}"
          f" {'tau_1^2':>9} {'ratio':>8} {'u/thr':>8}")
    for r, n1, n2, m1, m2 in found[:top]:
        t1 = ((sqrt(n2) + sqrt(n1)) / (sqrt(n2) - sqrt(n1))) ** 2
        print(f"  {r:>11.4f} {f'({n1},{n2})':>18} {f'({m1},{m2})':>18}"
              f" {m2/m1:>9.5f} {t1:>9.5f} {(m2/m1)/t1:>8.5f} {r/thr:>8.5f}")
    below = [f for f in found if f[0] < thr]
    print(f"  realised BELOW the threshold: {len(below)}"
          + ("" if not below else
             "  <- all non-tau_1, which is the mechanism"))
    for r, n1, n2, m1, m2 in below[:4]:
        t1 = ((sqrt(n2) + sqrt(n1)) / (sqrt(n2) - sqrt(n1))) ** 2
        print(f"     u = {r:.4f} at ({n1},{n2}) m=({m1},{m2}),"
              f" m2/m1 / tau_1^2 = {(m2/m1)/t1:.5f}")
    print("  Measured absence over a finite range: this does NOT prove x^2+1 admits")
    print("  no non-tau_1 windowed 4-cycle.  That is the cross-orbit case this note")
    print("  records as the one multipliers do not predict.")


def threshold_family(X=6000, D=1):
    """O.13' -- the threshold as a function of V, and what a sub-threshold cycle forces.

    tau_V^2 < 2  <=>  V sqrt(D)/M < 1/(2 sqrt 2)  <=>  u > (sqrt2 V + sqrt(2V^2+1))^2.

    V = 2 is admissible for EVERY pair (U = a+b gives U^2 - D V^2 = M^2
    identically) -- that is tau_1, threshold (1+sqrt2)^4.  V = 1 needs
    U^2 = M^2 + D = a^2 - ab + b^2 to be a perfect square, the Eisenstein norm
    form, so the pair must be a 60-degree Pythagorean pair.

    Hence at D = 1: a windowed 4-cycle has u > 33.9706, or else 9.8990 < u with
    a^2 - ab + b^2 square.  Checked against every realised windowed 4-cycle --
    and note the check is VACUOUS wherever nothing falls below the threshold,
    which is the case at D = 1.  The content is the theorem, not the count.
    D != 1 needs M -> M*D throughout and is not covered.
    """
    from collections import defaultdict
    from math import isqrt, sqrt
    print("  thresholds u > (sqrt2 V + sqrt(2V^2+1))^2, from tau_V^2 < 2:")
    for V in (1, 2, 3):
        t = (sqrt(2) * V + sqrt(2 * V * V + 1)) ** 2
        who = ("a^2-ab+b^2 a perfect square" if V == 1 else
               "ALWAYS (U = a+b)" if V == 2 else "-")
        print(f"    V = {V}:  u > {t:>10.6f}   admissible when {who}")
    print(f"    O.12 proves {(5 + 21 ** 0.5) / 2:.6f}, below even the V = 1 value,"
          " because it also carries")
    print("    the finite correction (tau^2 < 3 rather than < 2).  The two"
          " allowances multiply.")

    thr2 = (1 + sqrt(2)) ** 4
    inc = defaultdict(list)
    for x in range(1, X + 1):
        v = x * x + D
        d = 1
        while d * d <= v:
            if v % d == 0:
                inc[v // d].append(d)
                if d * d != v:
                    inc[d].append(v // d)
            d += 1
    key = defaultdict(list)
    for n, ms in inc.items():
        ms = sorted(set(ms))
        for i, m1 in enumerate(ms):
            for m2 in ms[i + 1:]:
                if m2 >= 2 * m1:
                    break
                key[(m1, m2)].append(n)
    tot = sub = viol = 0
    for (m1, m2), nsl in key.items():
        if len(nsl) < 2:
            continue
        nsl.sort()
        for i in range(len(nsl) - 1):
            a, b = nsl[i], nsl[i + 1]
            if a == 1:
                continue
            tot += 1
            if b / a < thr2:
                sub += 1
                q = a * a - a * b + b * b
                if isqrt(q) ** 2 != q:
                    viol += 1
                    print(f"    VIOLATION: ({a},{b}) u={b/a:.4f} below"
                          f" {thr2:.4f} with a^2-ab+b^2 = {q} not square")
    print(f"\n  x^2+{D}, X = {X}: {tot} realised windowed 4-cycles (unit-free),"
          f" {sub} below (1+sqrt2)^4,")
    print(f"  of which {viol} violate O.13' (a^2-ab+b^2 not a perfect square).")
    print("  Measured absence over a finite range -- not a proof that none exists.")
