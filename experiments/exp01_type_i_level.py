"""Experiment 01 -- the Type I level of distribution for A = {x + i}.

Supports Note B.  Two things are measured:

1. The number of admissible ideals of norm <= D, against the prediction
   ~ (3/2pi) D coming from  Sigma_d N(d)^{-s} = zeta(s) L(s,chi_4) / zeta(2s).
2. The Type I error sum  Sigma_{N(d)<=D} |A_d - |A|/N(d)|  against |A| = X.

The level of distribution is the D at which the ratio in (2) stops being o(1).

Usage:  python experiments/exp01_type_i_level.py [X]
"""

import sys

import _bootstrap  # noqa: F401

from x2plus1.typeI import type_i_x2plus1

PI = 3.14159265358979323846


def main(X: int = 4000) -> None:
    print(f"A = {{x + i : 1 <= x <= {X}}},  |A| = {X},  norms up to {X * X + 1}")
    print(f"predicted admissible-ideal density  3/(2pi) = {3 / (2 * PI):.6f}\n")
    print(f"{'D':>10} {'D/X':>8} {'#ideals':>10} {'/D':>8} "
          f"{'Sum|r_d|':>12} {'/|A|':>9}")
    print("-" * 62)
    D = 25
    while D <= 64 * X:
        rep = type_i_x2plus1(X, D)
        print(f"{D:>10} {D / X:>8.2f} {rep.n_moduli:>10} "
              f"{rep.n_moduli / D:>8.4f} {rep.total_error:>12.1f} {rep.ratio:>9.4f}")
        D *= 2
    print("\nType I holds at level D while the last column is o(1).")
    print("It crosses 1 near D ~ X, i.e. D ~ (norm bound)^{1/2}: this is the")
    print("N^{1/2} wall of Note B.  The error per modulus is <= 1 and cannot be")
    print("improved -- one residue class meets an interval of length X in")
    print("floor(X/q) or ceil(X/q) points, full stop.")


if __name__ == "__main__":
    main(int(sys.argv[1]) if len(sys.argv) > 1 else 4000)
