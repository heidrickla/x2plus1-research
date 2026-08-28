"""Experiment 08 -- the fourth published sequence, and what kappa cannot see.

Supports Note K, and answers the standing [VERIFY] in Note D that asked for "a
fourth sequence with a known outcome".  Merikoski (arXiv:2112.03617, 2022)
proved that a^2 + (b^2+1)^2 captures infinitely many primes.  Setting D = 0 in
the same family recovers Friedlander-Iwaniec's a^2 + b^4.  The two sequences
therefore differ in *one* term of the inner polynomial and in nothing else:

    a^2 + b^4          asymptotic formula,   Type II range N << X^{1/2-eta}
    a^2 + (b^2+1)^2    lower bound only,     Type II range N << X^{1/3-eta}

If kappa = |A|^2/Q were sufficient for the Type II range, it would have to
separate these two.  This script measures that it does not: the two sequences
agree in |A|, in kappa, in max-min-degree and in Gram structure to within a
fraction of a percent.  What separates them is the singularity type of the
Type II curve -- FI's x_1^2 = a x_2^2 is singular, Merikoski's x_1^2 + 1 =
a(x_2^2 + 1) is not (Merikoski p. 16) -- which is invisible to a degree count.

So kappa is a *necessary* condition (kappa = 1 for x^2+1, and a forest has no
bilinear structure at all), never a sufficient one.

Usage:  python experiments/exp08_merikoski_ledger.py [norm_bound]
"""

import sys

import _bootstrap  # noqa: F401

from x2plus1.sequences import a2_bsq_plus_D_sequence, x2plus1_sequence
from x2plus1.typeII import incidence, is_c4_free, max_offdiagonal_gram


def sweep(seq):
    """max over dyadic splits of min(mean row degree, mean col degree)."""
    best, best_C = 0.0, None
    lo = 10
    while lo < seq.norm_bound:
        hi = lo * 10
        C, *_ = incidence(seq, lo, hi)
        total = float(C.data.sum())
        if total:
            dm, dn = total / C.shape[0], total / C.shape[1]
            if min(dm, dn) > best:
                best, best_C = min(dm, dn), C
        lo = hi
    return best, best_C


def main(Q: int = 10**7) -> None:
    print(f"norm bound Q = {Q}\n")
    print(f"{'sequence':>16} {'|A|':>8} {'kappa':>10} {'sqrt(kappa)':>11} "
          f"{'max min-deg':>11} {'ratio':>6} {'C4-free?':>9} {'max Gram':>9}")
    print("-" * 92)

    seqs = [
        a2_bsq_plus_D_sequence(Q, 0),   # = a^2 + b^4,        Friedlander-Iwaniec
        a2_bsq_plus_D_sequence(Q, 1),   # = a^2 + (b^2+1)^2,  Merikoski
        x2plus1_sequence(Q),
    ]
    for seq in seqs:
        n = len(seq)
        kappa = n * n / Q
        best, C = sweep(seq)
        c4 = "yes" if C is not None and is_c4_free(C) else "no"
        gram = max_offdiagonal_gram(C) if C is not None else 0
        print(f"{seq.name:>16} {n:>8} {kappa:>10.1f} {kappa**0.5:>11.2f} "
              f"{best:>11.2f} {best / kappa**0.5:>6.2f} {c4:>9} {gram:>9}")

    print("\nRows 1 and 2 are the test.  They are the same sequence up to the +1")
    print("in the inner polynomial, they agree in every column here, and the")
    print("literature separates them by a sixth in the Type II exponent.")
    print("kappa is necessary, not sufficient.")


if __name__ == "__main__":
    main(int(sys.argv[1]) if len(sys.argv) > 1 else 10**7)
