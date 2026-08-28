"""Experiment 05 -- the Type II sum as Moebius in arithmetic progressions.\n\nSupports Note J. The reduction there (verified in tests/test_note_j.py) is that\nthe fibre {n : mn in A} is the arithmetic progression n_0 + Z*conj(m), so that\nup to the non-squarefree correction\n\nSum_m | Sum_n mu(n) 1[mn in A] |  =  Sum_q | Sum_{x<=X, x==r_q (q)} mu(x^2+1) |\n\nwith q = N(m) and r_q the root of r^2+1 == 0 (mod q). The right-hand side needs\nno Gaussian divisor enumeration, so it reaches X far beyond the incidence-matrix\nroute in ``typeII``.\n\nThe point of going far: Note H's law S ~ sqrt(MX) was fitted over one decade of\nX, which cannot separate sqrt(MX) from sqrt(MX)(log X)^c. This sweeps several\ndecades and fits the log-power.\n\nPrimary object is *prime* moduli q = p == 1 (mod 4), which is the clean\nsub-family and is cheap to enumerate; ``--all-moduli`` cross-checks against all\nadmissible q at smaller X.\n\nUsage:  python experiments/exp05_mobius_progressions.py [X_max] [--all-moduli]\n"""

import json
import sys
import time
from math import log, sqrt
from pathlib import Path

import numpy as np
from sympy import primerange

import _bootstrap  # noqa: F401

from x2plus1.mobius import _sqrt_minus_one, mobius_x2plus1

RESULTS = Path(__file__).resolve().parent / "results"


def band_sum_prime_moduli(mu: np.ndarray, X: int, lo: int, hi: int, seed: int = 0) -> tuple[int, int]:
    """(Sum over prime q in [lo,hi) of |Sum_{x==r (q)} mu|, number of (q,root) pairs)."""
    import random
    rng = random.Random(seed)
    total = 0
    pairs = 0
    for p in primerange(max(lo, 3), hi):
        if p % 4 != 1:
            continue
        r = _sqrt_minus_one(p, rng)
        for root in {r, p - r}:
            total += abs(int(mu[root::p].sum()))
            pairs += 1
    return total, pairs


def band_sum_all_moduli(mu: np.ndarray, X: int, lo: int, hi: int) -> tuple[int, int]:
    """Same over every admissible modulus, prime or not. Slower; a cross-check."""
    from x2plus1.factorization import roots_of_minus_one
    total = 0
    pairs = 0
    for q in range(max(lo, 2), hi):
        for r in roots_of_minus_one(q):
            total += abs(int(mu[(r if r else q)::q].sum()))
            pairs += 1
    return total, pairs


def main(X_max: int = 10**7, all_moduli: bool = False) -> None:
    """Sweep X, and for each dyadic band of moduli report the per-progression saving.\n\nThe headline statistic is\n\nrho = S / (pairs * sqrt(X/M))\n\ni.e. the mean |Sum mu| over one progression, divided by the square root of\nits length. Square-root cancellation makes rho ~ sqrt(2/pi) = 0.798,\nconstant in both M and X. Any log-power loss shows up as rho drifting with\nlog X, and that drift is what Note H could not resolve over one decade.\n\nrho is used rather than S/sqrt(MX) because the number of admissible moduli\nin a band carries its own arithmetic factor -- ~M/log M for prime moduli,\n~(3/2pi)M for all admissible moduli -- which would otherwise be confounded\nwith the quantity of interest.\n"""
    RESULTS.mkdir(exist_ok=True)
    rows = []
    ladder = []
    X = 10**4
    while X <= X_max:
        ladder.append(X)
        nxt = int(X * sqrt(10))
        if nxt > X_max and X < X_max:
            nxt = X_max
        X = nxt if nxt > X else X * 10
    for X in ladder:
        t = time.time()
        mu = mobius_x2plus1(X)
        build = time.time() - t
        print(f"\nX = {X:>11}   (mu sieve {build:5.1f}s)", flush=True)
        print(f"    {'M band':>22} {'pairs':>9} {'S':>12} {'mean|sum|':>10} "
              f"{'sqrt(X/M)':>10} {'rho':>7}", flush=True)
        M = 10
        while M * 10 <= X:
            hi = M * 10
            t0 = time.time()
            f = band_sum_all_moduli if all_moduli else band_sum_prime_moduli
            S, pairs = f(mu, X, M, hi)
            if pairs == 0:
                M = hi
                continue
            Mgeo = sqrt(M * hi)
            length = X / Mgeo
            rho = (S / pairs) / sqrt(length)
            print(f"    [{M:>9},{hi:>10}) {pairs:>9} {S:>12} {S / pairs:>10.2f} "
                  f"{sqrt(length):>10.2f} {rho:>7.4f}  [{time.time()-t0:.0f}s]", flush=True)
            rows.append(dict(X=X, M_lo=M, M_hi=hi, M=Mgeo, pairs=pairs, S=S,
                             rho=rho, u=log(Mgeo) / log(X)))
            M = hi
        del mu
    tag = "all" if all_moduli else "prime"
    out = RESULTS / f"exp05_{tag}_moduli.json"
    out.write_text(json.dumps(rows, indent=1), encoding="utf-8")
    print(f"\nwrote {out}")

    print("\nSquare-root cancellation predicts rho = sqrt(2/pi) = 0.798, flat in X.")
    print("Fitting rho ~ (log X)^c at fixed u = log M / log X:\n")
    print(f"    {'u~':>6} {'points':>7} {'X range':>22} {'fitted c':>9} {'rho span':>18}")
    for target in (0.3, 0.4, 0.5, 0.6, 0.7, 0.8):
        by_x = {}
        for r in rows:
            if abs(r["u"] - target) < 0.06:
                cur = by_x.get(r["X"])
                if cur is None or abs(r["u"] - target) < abs(cur["u"] - target):
                    by_x[r["X"]] = r
        pts = sorted(by_x.items())
        if len(pts) >= 3:
            xs = [log(log(x)) for x, _ in pts]
            ys = [log(r["rho"]) for _, r in pts]
            mx, my = sum(xs) / len(xs), sum(ys) / len(ys)
            den = sum((x - mx) ** 2 for x in xs)
            c = sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / den if den else float("nan")
            span = f"{pts[0][1]['rho']:.3f} -> {pts[-1][1]['rho']:.3f}"
            print(f"    {target:>6.2f} {len(pts):>7} {pts[0][0]:>10}..{pts[-1][0]:>10} "
                  f"{c:>9.3f} {span:>18}")
        else:
            print(f"    {target:>6.2f} {len(pts):>7} {'':>22} {'--':>9} {'too few':>18}")


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    main(int(args[0]) if args else 10**7, "--all-moduli" in sys.argv)
