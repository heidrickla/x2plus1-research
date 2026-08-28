"""Experiment 04 -- is kappa a real invariant, or three coincidences?

Supports Note D's standing question. The sequences

    A_k = { a + b^k i : a, b >= 1, a^2 + b^{2k} <= Q },    |A_k| ~ Q^{1/2 + 1/(2k)}

interpolate between the solved cases and this project's:

    k = 1  alpha = 1     all of Z[i]
    k = 2  alpha = 3/4   the Friedlander-Iwaniec set a^2 + b^4
    k = 3  alpha = 2/3   the density of Heath-Brown's x^3 + 2y^3
    k -> oo  alpha -> 1/2  the line Im z = 1, i.e. x^2 + 1

Note D's claim is that for a dyadic split N(m) ~ M the mean degrees obey
D_m * d_n ~ kappa = |A|^2/Q independently of M, so that

    max over M of min(D_m, d_n)  ~  sqrt(kappa)  =  |A| / Q^{1/2}  =  Q^{1/(2k)}.

Three published sequences cannot distinguish a law from a coincidence. This
sweeps k and checks the predicted exponent, and watches the incidence graph
collapse to a forest as alpha -> 1/2.

Usage:  python experiments/exp04_kappa_family.py [norm_bound] [k_max]
"""

import sys

import _bootstrap  # noqa: F401

from x2plus1.sequences import a2b2k_sequence, x2plus1_sequence
from x2plus1.typeII import incidence, is_c4_free


def degrees(seq, lo, hi):
    C, *_ = incidence(seq, lo, hi)
    T = float(C.data.sum())
    if T == 0:
        return None
    return T / C.shape[0], T / C.shape[1], C


def main(Q: int = 10**7, k_max: int = 6) -> None:
    print(f"norm bound Q = {Q}\n")
    print(f"{'sequence':>10} {'alpha':>6} {'|A|':>8} {'kappa':>10} "
          f"{'sqrt(kappa)':>11} {'max min-deg':>11} {'ratio':>6} {'C4-free?':>9}")
    print("-" * 80)

    seqs = [(k, a2b2k_sequence(Q, k)) for k in range(2, k_max + 1)]
    seqs.append((None, x2plus1_sequence(Q)))

    for k, seq in seqs:
        n = len(seq)
        kappa = n * n / Q
        best, best_C = 0.0, None
        lo = 10
        while lo < Q:
            hi = lo * 10
            d = degrees(seq, lo, hi)
            if d:
                dm, dn, C = d
                if min(dm, dn) > best:
                    best, best_C = min(dm, dn), C
            lo = hi
        alpha = 0.5 + 1 / (2 * k) if k else 0.5
        c4 = "yes" if best_C is not None and is_c4_free(best_C) else "no"
        print(f"{seq.name:>10} {alpha:>6.3f} {n:>8} {kappa:>10.1f} "
              f"{kappa**0.5:>11.2f} {best:>11.2f} {best / kappa**0.5:>6.2f} {c4:>9}")

    print("\nThe 'ratio' column is the test: Note D predicts it is O(1) across the")
    print("whole family, not just at the three published densities.  The last row")
    print("is x^2+1, where sqrt(kappa) = 1 and the graph is provably a forest.")


if __name__ == "__main__":
    Q = int(sys.argv[1]) if len(sys.argv) > 1 else 10**7
    k_max = int(sys.argv[2]) if len(sys.argv) > 2 else 6
    main(Q, k_max)
