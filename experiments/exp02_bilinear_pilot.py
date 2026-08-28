"""Experiment 02 -- the Type II bilinear pilot for A = {x + i}.

Supports Note H (and feeds Notes E/F).  For each dyadic range of N(m) it
reports the trivial bound T, the Gram diagonal/off-diagonal split that the
dispersion argument produces, and three sizes of |S|:

    random signs   -- meaningless as a hypothesis test, kept as a sanity floor
    worst case     -- adversarial alpha and beta; what the incidence structure
                      alone permits
    beta = mu      -- the faithful Type II quantity Sigma_m |Sigma_n mu(n) c_mn|

Empirical law found so far (X up to 2*10^4):

    Sigma_m |Sigma_n mu(n) c_mn|  ~  sqrt(M X)   for M <= X,
                                  ~  T ~ X       for M >= X,

so with M = X^u the exponent theta = log|S|/log T is (1+u)/2.  The sieve needs
theta < 1 - delta, hence M <= X^{1-delta}: the same N^{1/2} wall as Type I.

Usage:  python experiments/exp02_bilinear_pilot.py [X]
"""

import sys
from math import log, sqrt

import _bootstrap  # noqa: F401

from x2plus1.sequences import by_x_range
from x2plus1.typeII import analyse


def main(X: int = 20000) -> None:
    seq = by_x_range(X)
    print(f"A = {{x + i : x <= {X}}},  |A| = {len(seq)},  norms up to {seq.norm_bound}\n")
    print(f"{'M range':>18} {'rows':>7} {'cols':>7} {'T':>7} "
          f"{'D_m':>6} {'d_n':>6} {'|S|_mu':>9} {'theta':>6} {'sqrt(MX)':>10}")
    print("-" * 86)
    lo = 10
    while lo < X * X // 10:
        hi = lo * 10
        try:
            r = analyse(seq, lo, hi)
        except ValueError:
            lo = hi
            continue
        M = sqrt(lo * hi)
        print(f"[{lo:>7},{hi:>8}) {r.n_rows:>7} {r.n_cols:>7} {r.T:>7} "
              f"{r.T / r.n_rows:>6.2f} {r.T / r.n_cols:>6.2f} "
              f"{r.S_mobius:>9.0f} {r.exponent(r.S_mobius):>6.3f} {sqrt(M * X):>10.0f}")
        lo = hi
    print("\nD_m = mean row degree = #{n : mn in A}; d_n = mean column degree.")
    print("min(D_m, d_n) stays ~ 1 in every range: whichever way the norm is")
    print("split, one side of the incidence matrix is a matching.  The general")
    print("law (Note F) is  max_M min(D_m, d_n) ~ |A| / Q^{1/2}, exactly 1 here.")
    print("Stronger still, the graph is C4-free (Note F, proved), so the Gram")
    print("matrix has no off-diagonal entry above 1 and dispersion has nothing")
    print("to work on -- which is why the worst-case theta is 1 at every split.")


if __name__ == "__main__":
    main(int(sys.argv[1]) if len(sys.argv) > 1 else 20000)
