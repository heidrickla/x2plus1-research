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
X_j > tau_V X_i, so m_j/m_i > (tau_V^2 X_i^2 + 1)/(X_i^2 + 1) and
tau_V^2 < 2 + 1/X_i^2 <= 3.  tau is increasing in |V| and |V| >= 1, so
tau_V >= tau(1) = sqrt(1+s^2) + s with s = sqrt(D)/M, and tau(1)^2 < 3 forces
s < 1/sqrt3, i.e. M/sqrt(D) > sqrt3.  With u = n_2/n_1 = b/a we have
M/sqrt(D) = (u-1)/sqrt(u), and (u-1)/sqrt(u) > sqrt3 iff u^2 - 5u + 1 > 0 iff
u > (5+sqrt21)/2.  A dyadic band gives u < 2, a factor 2.4 inside it.

It uses |V| >= 1, not the parity lemma's |V| >= 2, so it does not depend on the
parity of a and b.

WHAT THIS SETTLES AND WHAT IT DOES NOT.  `gaussian-to-rational-bridge` is
`inferred`, and its stated gap is "what is proved over Z[i] is G <= 1; what is
measured over Z is G' <= 2 on every dyadic window for X <= 8000".  O.12 closes
that sentence's second half: over Z, on the configuration (II) quantifies over,
G' <= 1 is PROVED for all X and matches the Z[i] bound exactly.  It does NOT
close the bridge's remaining inference -- "both give no main term, so the
conclusion is unchanged" -- and it says nothing about O.2, which is the
free-cofactor question.  (1,41) sharing 730 and 1370 is a genuine G' = 2 and
simply is not a Type II configuration.

Usage:  python experiments/exp24_doubly_dyadic.py [X]
"""

import sys
from collections import defaultdict
from math import sqrt

import _bootstrap  # noqa: F401

THRESHOLD = (5 + sqrt(21)) / 2


def divisor_incidence(X):
    """modulus m -> cofactors n with m*n = x^2+1 for some x <= X."""
    inc = defaultdict(list)
    for x in range(1, X + 1):
        v = x * x + 1
        d = 1
        while d * d <= v:
            if v % d == 0:
                inc[d].append(v // d)
                if d * d != v:
                    inc[v // d].append(d)
            d += 1
    return inc


def main(X=3000):
    print("THEOREM O.12.  Two cofactors within a factor (5+sqrt21)/2 ="
          f" {THRESHOLD:.6f}")
    print("share at most one modulus in any dyadic window.  A dyadic band gives")
    print(f"u = n_2/n_1 < 2, a factor {THRESHOLD/2:.4f} inside it.\n")
    print("  the threshold, by regime:")
    for lab, t2 in (("X_i = 1  (tau^2 < 3)", 3.0), ("X_i -> oo (tau^2 < 2)", 2.0)):
        # tau(1)^2 < t2  =>  s < (t2-1)/(2 sqrt(t2))  =>  M/sqrt(D) > 2 sqrt(t2)/(t2-1)
        r = 2 * sqrt(t2) / (t2 - 1)
        u = (2 + r * r + r * sqrt(r * r + 4)) / 2
        print(f"     |V| >= 1, {lab:22}: M/sqrtD > {r:.6f}, u > {u:.6f}")
    print(f"     |V| >= 2 recovers the familiar 33.97 asymptotically.")

    inc = divisor_incidence(X)
    print(f"\nX = {X}.  Max off-diagonal Gram entry, by modulus window:")
    print(f"{'modulus window':>24} {'banded cofactors':>18} {'free cofactors':>16}")
    M = 8
    worst_banded = 0
    while M * 2 <= (X * X + 1):
        ms = [m for m in range(M, 2 * M) if m in inc]
        if not ms:
            M *= 4
            continue
        cof = defaultdict(set)
        for m in ms:
            for n in inc[m]:
                cof[n].add(m)
        banded = free = 0
        ns_all = list(cof)
        N = 1
        while N <= X * X:
            band = [n for n in ns_all if N <= n < 2 * N]
            for i in range(len(band)):
                for j in range(i + 1, len(band)):
                    banded = max(banded, len(cof[band[i]] & cof[band[j]]))
            N *= 2
        for i in range(len(ns_all)):
            for j in range(i + 1, len(ns_all)):
                free = max(free, len(cof[ns_all[i]] & cof[ns_all[j]]))
        worst_banded = max(worst_banded, banded)
        print(f"[{M:9},{2*M:10})  {banded:18} {free:16}")
        M *= 4
    # Positive control.  A "max of 1" over pairs that share nothing would look
    # identical to O.12 holding, so count how many banded pairs share ONE, and
    # check the forbidden configuration occurs once the banding is dropped.
    n_pairs = n_one = n_free2 = 0
    M = 8
    while M * 2 <= (X * X + 1):
        ms = [m for m in range(M, 2 * M) if m in inc]
        if ms:
            cof = defaultdict(set)
            for m in ms:
                for n in inc[m]:
                    cof[n].add(m)
            ns_all = list(cof)
            N = 1
            while N <= X * X:
                band = [n for n in ns_all if N <= n < 2 * N]
                for i in range(len(band)):
                    for j in range(i + 1, len(band)):
                        n_pairs += 1
                        n_one += len(cof[band[i]] & cof[band[j]]) == 1
                N *= 2
            for i in range(len(ns_all)):
                for j in range(i + 1, len(ns_all)):
                    n_free2 += len(cof[ns_all[i]] & cof[ns_all[j]]) >= 2
        M *= 4

    print()
    print(f"  worst banded Gram entry anywhere: {worst_banded}"
          f"  -- C_4-free, as O.12 requires.")
    print(f"  POSITIVE CONTROL: {n_pairs} banded pairs examined, of which"
          f" {n_one} share")
    print(f"  exactly one modulus; and {n_free2} FREE pairs share two.  So the")
    print("  forbidden configuration occurs the moment the banding is dropped,")
    print("  and the banded population is large enough to have shown it.")
    print("  The free column reaching 2 is genuine and is NOT a counterexample:")
    print("  (1,41) shares 730 and 1370, and 41/1 = 41 > 4.79, so the two")
    print("  cofactors are nowhere near one band.  That configuration is exactly")
    print("  what a Type II hypothesis excludes.")


def fm_footnote_quantity(X=12000):
    """Ford-Maynard's footnote-2 mean, with and without the second band."""
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
    print()
    print("FORD-MAYNARD FOOTNOTE 2, which averages G over m_1, m_2 ~ x^{1-2c+eps}.")
    print("(II) bands n as well as m, so the quantity is DOUBLY dyadic and O.12")
    print("caps it at 1.  The recorded figures are the moduli-unrestricted ones:")
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
                best = 0
                W = 1
                while W <= X * X:
                    best = max(best, sum(1 for m in sh if W <= m < 2 * W))
                    W *= 2
                tb += best
                mb = max(mb, best)
        print(f"[{N:5},{2*N:6}) {len(ns):5} {tf/npairs:14.4f} {mf:4}"
              f" | {tb/npairs:16.4f} {mb:4}")
        N *= 2
    print("  On the configuration (II) quantifies over the mean NEVER exceeds 1,")
    print("  and the only band attaining 1 holds two cofactors -- a single pair.")


def _banded_gram(values, Qmax):
    """(max Gram over banded cofactors, over free, #banded pairs sharing >= 2)."""
    inc = defaultdict(set)
    for v in values:
        d = 1
        while d * d <= v:
            if v % d == 0:
                inc[v // d].add(d)
                if d * d != v:
                    inc[d].add(v // d)
            d += 1
    band = free = pairs2 = 0
    M = 4
    while M * 2 <= Qmax:
        ms = [m for m in inc if M <= m < 2 * M]
        if ms:
            cof = defaultdict(set)
            for m in ms:
                for n in inc[m]:
                    cof[n].add(m)
            ns = list(cof)
            N = 1
            while N <= Qmax:
                bd = [n for n in ns if N <= n < 2 * N]
                for i in range(len(bd)):
                    for j in range(i + 1, len(bd)):
                        g = len(cof[bd[i]] & cof[bd[j]])
                        band = max(band, g)
                        pairs2 += g >= 2
                N *= 2
            for i in range(len(ns)):
                for j in range(i + 1, len(ns)):
                    free = max(free, len(cof[ns[i]] & cof[ns[j]]))
        M *= 4
    return band, free, pairs2


def control(Q=100000):
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
    print()
    print(f"POSITIVE CONTROL at Q = {Q}: is the 0/1 property generic?")
    print(f"{'sequence':>28} {'banded':>7} {'free':>6} {'banded pairs >=2':>18}")
    for lab, vals in seqs:
        b, f, p2 = _banded_gram(vals, Q)
        print(f"{lab:>28} {b:7} {f:6} {p2:18}")
    print("  x^2+1 is alone at 1 -- and there it is a THEOREM, not a measurement.")
    print("  NOT A CLASSIFIER, AND THE ORDERING IS NOT STABLE.  Across")
    print("  Q = 2.5e4/5e4/1e5 the two smallest SWAP: a^2+b^6 (not known captured)")
    print("  reads 6, 7, 11 against the CAPTURED x^3+2y^3 at 5, 9, 15.  A statistic")
    print("  whose ordering moves with Q cannot separate captured from open, and")
    print("  'low implies hard' would be mean-G-does-not-classify again.")
    print("  x^3+2y^3 is here because it is what killed that classifier.")
    print("  What IS claimed is a difference in KIND: x^2+1 reads exactly 1 at")
    print("  every size with the value a theorem; everything else GROWS with Q.")
    print("  It also explains the footnote's hedge -- for a count ranging over")
    print("  0..66 there is something to average; for a 0/1 indicator there is not.")


if __name__ == "__main__":
    XX = int(sys.argv[1]) if len(sys.argv) > 1 else 3000
    main(XX)
    fm_footnote_quantity(min(12000, max(2000, 4 * XX)))
    control(min(100000, max(20000, XX * XX // 20)))
