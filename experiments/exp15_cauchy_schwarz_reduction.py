"""Experiment 15 -- the sqrt(MX) upper bound as a Cauchy-Schwarz reduction.

Supports Note M. `sqrt-MX-law` is `extrapolated` and carries Note M's whole
theta-axis argument, which is uncomfortable because a fitted exponent
extrapolated past its data is exactly the class of claim this repo has been
burned by. But section 1 needs only the UPPER bound S_mu(M) << sqrt(MX), and
that half is not a fit.

THE REDUCTION.  With T_m = sum_{x <= X, m | x^2+1} mu(x^2+1),

    S_mu(M) = sum_{m ~ M} |T_m|,      S_mu(M)^2 <= #{m ~ M} * Q2,   Q2 = sum T_m^2

by Cauchy-Schwarz, and expanding the square gives the EXACT decomposition

    Q2 = DIAG + OFF,
    DIAG = #{(m,x) : m ~ M, m | x^2+1, x^2+1 squarefree},
    OFF  = sum_{x != y} mu(x^2+1) mu(y^2+1) G_M(x,y),
    G_M(x,y) = #{m ~ M : m | gcd(x^2+1, y^2+1)}.

OFF is built from exactly the Gram entries Prop L.1 bounds and Theorem O.3'
constrains -- so this ties the theta axis to the Gram axis.

WHAT IS PROVED AND WHAT IS NOT.  Cauchy-Schwarz and the decomposition are exact.
DIAG ~ X is a divisor count (each x has O(1) divisors in a dyadic band).
#{m ~ M : -1 is a QR mod m} ~ M/sqrt(log M) is Landau-Ramanujan.  ONLY
OFF = o(DIAG) is measured.  So this does NOT promote `sqrt-MX-law`; it changes
what would have to be proved.

IT ALSO EXPLAINS THE ROOT-GROUPING GAP.  DIAG counts incidences and is therefore
index-independent, so the only thing that moves between the per-modulus and
per-progression normalisations is the outer count:

    S_prog / S_mod ~ sqrt(#prog / #mod) = sqrt(mean roots per modulus),

which is the ratio the parallel session measured to within 2% at X = 1e6.  It is
range-dependent -- this script reports 11% at X = 1e5 -- so quote the X with the
figure.  The robust part is the sign: it predicts the per-modulus exponent
falling BELOW 1/2, which is what they observe (0.4803 against 0.5046).

Usage:  python experiments/exp15_cauchy_schwarz_reduction.py [X]
"""

import sys
from math import sqrt

import numpy as np

import _bootstrap  # noqa: F401

from x2plus1.factorization import roots_of_minus_one
from x2plus1.mobius import mobius_x2plus1


def band(mu, M, X):
    """(#moduli, #progressions, S_per_modulus, S_per_progression, Q2, DIAG)."""
    nmod = nprog = 0
    S_mod = S_prog = Q2 = 0.0
    diag = 0
    for m in range(M, 2 * M):
        rs = roots_of_minus_one(m)
        if not rs:
            continue
        starts = {r % m for r in rs} | {(m - r) % m for r in rs}
        starts.discard(0)
        if not starts:
            continue
        nmod += 1
        cols = []
        for r in sorted(starts):
            xs = np.arange(r, X + 1, m, dtype=np.int64)
            xs = xs[xs >= 1]
            if xs.size == 0:
                continue
            nprog += 1
            S_prog += abs(float(mu[xs].sum()))
            cols.append(xs)
        if not cols:
            continue
        xs = np.unique(np.concatenate(cols))
        v = mu[xs]
        T = float(v.sum())
        S_mod += abs(T)
        Q2 += T * T
        diag += int((v != 0).sum())
    return nmod, nprog, S_mod, S_prog, Q2, diag


def main(X=200_000):
    mu = mobius_x2plus1(X)
    print(f"X = {X}\n")
    hdr = ("M", "#mod", "Q2", "DIAG", "OFF/DIAG", "S_mu", "CS", "S/CS", "roots", "ratio/pred")
    print(f"{hdr[0]:>7} {hdr[1]:>6} {hdr[2]:>9} {hdr[3]:>9} {hdr[4]:>9} "
          f"{hdr[5]:>8} {hdr[6]:>9} {hdr[7]:>6} {hdr[8]:>6} {hdr[9]:>10}")
    diags, offs, ratios = [], [], []
    M = 200
    while M * 2 <= max(400, X // 4):
        nmod, nprog, S_mod, S_prog, Q2, diag = band(mu, M, X)
        if nmod == 0 or diag == 0:
            M *= 4
            continue
        off = Q2 - diag
        cs = sqrt(nmod * Q2)
        roots = nprog / nmod
        # Cauchy-Schwarz predicts S_prog/S_mod ~ sqrt(#prog/#mod)
        pred = sqrt(nprog / nmod)
        obs = S_prog / S_mod if S_mod else float("nan")
        diags.append(diag)
        offs.append(off / diag)
        ratios.append(obs / pred)
        print(f"{M:7} {nmod:6} {Q2:9.0f} {diag:9} {off / diag:9.3f} "
              f"{S_mod:8.0f} {cs:9.1f} {S_mod / cs:6.3f} {roots:6.3f} {obs / pred:10.3f}")
        M *= 4
    print()
    if len(diags) > 1:
        spread = max(diags) / min(diags)
        print(f"DIAG varies by a factor {spread:.2f} across the range -> DIAG ~ X, flat in M.")
    if offs:
        worst = max(abs(o) for o in offs)
        print(f"OFF/DIAG runs {offs[0]:+.3f} -> {offs[-1]:+.3f}, worst |OFF|/DIAG = {worst:.3f}")
        print("  The reduction needs |OFF| << DIAG, NOT monotone decay -- OFF is a signed")
        print("  sum and changes sign with X and M.  Small is what matters.")
    if ratios:
        print(f"observed/predicted root-grouping ratio stays within "
              f"{max(abs(r - 1) for r in ratios):.1%} of 1.")
    print()
    print("Only OFF = o(DIAG) is measured; everything else in the chain is exact or")
    print("standard.  `sqrt-MX-law` stays `extrapolated`.")


if __name__ == "__main__":
    main(int(sys.argv[1]) if len(sys.argv) > 1 else 200_000)
