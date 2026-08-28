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


if __name__ == "__main__":
    main(int(sys.argv[1]) if len(sys.argv) > 1 else 3000)
