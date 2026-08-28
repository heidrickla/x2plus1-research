"""Experiment 09 -- is the degeneracy about x^2+1, or about degree >= 2?

Supports Note L. Everything else in this repo works in Z[i], where Note F's
lemma gives G(n1,n2) <= 1 exactly. But the Type II hypothesis of [ASP], [DFI]
and [FM] is stated over Z, and the rational incidence graph is a *coarsening*
of the Gaussian one: one rational modulus m carries several Gaussian ideals of
norm m, and merging rows can only create 4-cycles. So the lemma has to be
re-measured in the setting the literature actually uses.

Two questions, one table:

  1. Does the degeneracy survive translation back to Z? The sharp constant 1 is
     a Gaussian fact and does not survive -- but boundedness does, which is all
     the argument needs. A Gram entry of 2 has no more of a main term than one
     of 1.
  2. Is it special to x^2+1? For A = {f(x) : x <= X} with deg f = d, the norm
     bound is Q ~ X^d and |A| = X, so alpha = 1/d and kappa = X^{2-d}. That is
     <= 1 for every d >= 2, with equality only at d = 2. So x^2+1 should be the
     *least* degenerate member of the class, and d = 1 -- arithmetic
     progressions, i.e. the solved case -- the only degree with kappa > 1.

Method: for each f, sweep dyadic modulus windows [M, 2M) up to sqrt(Q) and
report the largest off-diagonal Gram entry found over all of them, following
exp04. Cofactors n = 1 are excluded (a unit is not a Type II variable, and in
Z[i] associates are normalised away); everything else is kept, including very
unbalanced splits, since Note F claims C4-freeness at every split.

Usage:  python experiments/exp09_degree_ladder.py [X] [M_max]
"""

import sys

import _bootstrap  # noqa: F401

from x2plus1.polyseq import degrees, incidence, ladder, max_offdiagonal_gram


def sweep(seq, M_cap: int):
    """max off-diagonal Gram over dyadic windows, and the window achieving it."""
    best, where, stats = 0, None, (0.0, 0.0)
    M = 2
    while M <= M_cap:
        ip, idx, shape, _, _ = incidence(seq, M, 2 * M, min_cofactor=1)
        if len(idx):
            g = max_offdiagonal_gram(ip, idx, shape)
            if g > best:
                best, where, stats = g, M, degrees(ip, idx, shape)
        M *= 2
    return best, where, stats


def main(X: int = 4000, M_cap: int = 2048) -> None:
    print(f"X = {X}, dyadic modulus windows [M, 2M) for M <= {M_cap}\n")
    print(f"{'f':>10} {'d':>2} {'alpha':>6} {'kappa':>12} {'max Gram':>9} "
          f"{'at M':>6} {'mean d_m':>9} {'mean d_n':>9}")
    print("-" * 78)
    for seq in ladder(X):
        cap = min(M_cap, max(2, int(seq.norm_bound ** 0.5)))
        gram, where, (dm, dn) = sweep(seq, cap)
        print(f"{seq.name:>10} {seq.degree:>2} {seq.alpha:>6.3f} {seq.kappa:>12.4g} "
              f"{gram:>9} {str(where):>6} {dm:>9.2f} {dn:>9.2f}")

    print("\nkappa = |A|^2/Q = X^{2-d}: above 1 only for d = 1, exactly 1 at d = 2,")
    print("vanishing for d >= 3. The max Gram column is the structural half. If it")
    print("stays bounded for every d >= 2 while growing with the window for d = 1,")
    print("then the obstruction is a property of the degree, not of x^2+1, and")
    print("d = 1 -- Dirichlet -- is the only single-variable case with anything")
    print("for a bilinear form to cancel.")


if __name__ == "__main__":
    X = int(sys.argv[1]) if len(sys.argv) > 1 else 4000
    M_cap = int(sys.argv[2]) if len(sys.argv) > 2 else 2048
    main(X, M_cap)
