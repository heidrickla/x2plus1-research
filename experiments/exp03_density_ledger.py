"""Experiment 03 -- the comparison ledger against a^2 + b^4.

Supports Notes D and I.  Both sequences live in Z[i] at the *same norm bound*:

    x^2 + 1   = N(x + i)        Im z = 1
    a^2 + b^4 = N(a + b^2 i)    Im z a perfect square

and the quantity that decides whether a bilinear form has anything to work
with is the rectangle density

    kappa := |A|^2 / Q          (Q = norm bound)

because for a dyadic split N(m) ~ M, N(n) ~ Q/M the mean degrees are

    D_m ~ |A| / M     d_n ~ |A| M / Q     =>     D_m * d_n ~ kappa,

independent of M.  So kappa alone says whether *any* split gives an incidence
matrix that is more than a matching:

    x^2 + 1     |A| ~ Q^{1/2}   kappa ~ 1          degenerate at every split
    x^3 + 2y^3  |A| ~ Q^{2/3}   kappa ~ Q^{1/3}
    a^2 + b^4   |A| ~ Q^{3/4}   kappa ~ Q^{1/2}

Usage:  python experiments/exp03_density_ledger.py [norm_bound]
"""

import sys
from math import sqrt

import _bootstrap  # noqa: F401

from x2plus1.sequences import a2b4_sequence, x2plus1_sequence
from x2plus1.typeII import analyse


def main(Q: int = 10**7) -> None:
    seqs = [x2plus1_sequence(Q), a2b4_sequence(Q)]
    print(f"norm bound Q = {Q}\n")
    for s in seqs:
        kappa = len(s) ** 2 / Q
        print(f"  {s.name:>8}: |A| = {len(s):>8}   |A|/Q^(1/2) = {len(s) / sqrt(Q):>8.3f}"
              f"   kappa = |A|^2/Q = {kappa:>10.2f}")
    print()
    print(f"{'sequence':>9} {'M range':>17} {'rows':>7} {'cols':>7} {'T':>8} "
          f"{'D_m':>9} {'d_n':>9} {'min':>7} {'theta(mu)':>9}")
    print("-" * 96)
    lo = 100
    while lo * 10 <= Q:
        hi = lo * 10
        for s in seqs:
            try:
                r = analyse(s, lo, hi)
            except ValueError:
                continue
            dm, dn = r.T / r.n_rows, r.T / r.n_cols
            print(f"{s.name:>9} [{lo:>6},{hi:>8}) {r.n_rows:>7} {r.n_cols:>7} "
                  f"{r.T:>8} {dm:>9.2f} {dn:>9.2f} {min(dm, dn):>7.2f} "
                  f"{r.exponent(r.S_mobius):>9.3f}")
        lo = hi
    print()
    print("The invariant is the 'min' column.  Over dyadic splits M its maximum")
    print("is ~ sqrt(kappa) = |A| / Q^{1/2}: exactly 1 for x^2+1 (a matching at")
    print("every split, so no bilinear cancellation is available at any M) and")
    print("~ Q^{1/4} for a^2+b^4 (a genuinely two-dimensional incidence matrix).")
    print("That single line is where the two-parameter freedom of (a, b) enters.")


if __name__ == "__main__":
    main(int(sys.argv[1]) if len(sys.argv) > 1 else 10**7)
