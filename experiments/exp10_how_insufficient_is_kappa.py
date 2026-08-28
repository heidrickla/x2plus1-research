"""Experiment 10 -- how insufficient is kappa? Dial the second variable.

Supports Note M. Note K showed kappa is necessary and not sufficient, using
two sequences of equal density. This asks the sharper quantitative question by
dialling the second variable one element at a time:

    A_B = { a + b^2 i : a >= 1, b in B, a^2 + b^4 <= Q },   kappa = |B|^2.

So kappa exceeds 1 as soon as |B| = 2 -- two values of b. The Friedlander-
Iwaniec set is B = [1, Q^{1/4}]; the x^2+1 line is B = {1}. Everything between
is available, and the question is where the incidence graph actually acquires
the 4-cycles that a dispersion argument needs.

If structure appears only when |B| is a positive power of Q, then kappa is
satisfied a whole power of Q before anything usable exists, and "necessary, not
sufficient" understates it: kappa is off by an exponent, not by a constant.
For calibration, Merikoski's sparse-set theorem (arXiv:2302.11331) needs
|B| >> Y^{1-delta}.

Usage:  python experiments/exp10_how_insufficient_is_kappa.py [norm_bound]
"""

import sys

import _bootstrap  # noqa: F401

from x2plus1.sequences import a2b4_restricted_sequence
from x2plus1.typeII import incidence, is_c4_free, max_offdiagonal_gram


#: Gram entries above this are all equally "there is structure"; stopping early
#: keeps the wide windows from costing sum-of-degrees-squared time.
GRAM_CAP = 64


def sweep(seq):
    """max off-diagonal Gram over norm windows, and where it occurs."""
    best, where, c4 = 0, None, True
    lo = 4
    while lo < seq.norm_bound:
        C, *_ = incidence(seq, lo, lo * 4)
        if C.data.size:
            g = max_offdiagonal_gram(C, stop_at=GRAM_CAP)
            if g > best:
                best, where = g, lo
            if not is_c4_free(C):
                c4 = False
        lo *= 4
    return best, where, c4


def main(Q: int = 10**7) -> None:
    Bmax = int(round(Q ** 0.25))
    print(f"norm bound Q = {Q},  full FI range is B = [1, {Bmax}]\n")
    print(f"{'|B|':>6} {'B':>22} {'|A|':>8} {'kappa':>10} {'max Gram':>9} "
          f"{'at M':>8} {'C4-free?':>9}")
    print("-" * 78)

    sizes = [1, 2, 3, 4, 6, 8, 12, 16, 24, 32]
    sizes = [k for k in sizes if k <= Bmax] + ([Bmax] if Bmax not in sizes else [])
    for k in sizes:
        B = list(range(1, k + 1))
        seq = a2b4_restricted_sequence(Q, B)
        n = len(seq)
        gram, where, c4 = sweep(seq)
        shown = str(B if k <= 4 else f"[1,{k}]")
        print(f"{k:>6} {shown:>22} {n:>8} {n * n / Q:>10.1f} {gram:>9} "
              f"{str(where):>8} {('yes' if c4 else 'no'):>9}")

    print("\nkappa = |B|^2 exactly, so the kappa criterion is met at |B| = 2.")
    print("The max Gram column says when there is anything for a bilinear form")
    print("to work with. The gap between those two columns is how insufficient")
    print("kappa is -- and it should be read as an exponent in Q, not a constant.")


if __name__ == "__main__":
    main(int(sys.argv[1]) if len(sys.argv) > 1 else 10**7)
