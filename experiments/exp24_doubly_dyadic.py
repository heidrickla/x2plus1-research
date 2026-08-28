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


if __name__ == "__main__":
    XX = int(sys.argv[1]) if len(sys.argv) > 1 else 1200
    main(XX)
    control(min(60000, max(20000, XX * XX // 20)))
    line_family(min(1200, max(400, XX)))
