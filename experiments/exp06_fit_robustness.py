"""Experiment 06 -- is the fitted log-power an artefact of choices nobody made?

Note J's headline is that the per-progression saving rho is flat in X, i.e. the
law is sqrt(MX) with no log-power correction, fitted as c = 0.00 +- 0.04. That
number depends on two things chosen by nobody:

  * the **band boundaries** -- decades [10^k, 10^{k+1}) rather than any other
    phase;
  * the **X ladder** -- powers of sqrt(10) starting at 10^4.

The rh-research-engine session found exactly this failure in its own exponent
fit: shifting the sample grid inside the same range moved a fitted exponent from
0.214 to 1.061, and the recorded value had been one draw with no error bar. The
general move is theirs: vary the thing nobody chose and see if the answer moves.

So this experiment reports the fitted c across band phases, and takes the spread
as the error bar. It also runs two injected-signal controls, without which a
"stable" answer means nothing:

  * a **null** (iid mu at the same density) must return c ~ 0;
  * an **injected damping** mu * (log X)^{-1/2} must be recovered as c ~ -1/2.

If the injected control does not come back, the estimator cannot see a
log-power at all and a measured c ~ 0 is vacuous rather than informative.

Usage:  python experiments/exp06_fit_robustness.py [X_max] [n_phases]
"""

import sys
from math import log, sqrt

import numpy as np
from sympy import primerange

import _bootstrap  # noqa: F401

from x2plus1.mobius import _sqrt_minus_one, mobius_x2plus1


def band_rho(mu: np.ndarray, lo: int, hi: int, seed: int = 0) -> tuple[float, int]:
    """(rho, pairs) over prime moduli in [lo, hi), normalised by actual length."""
    import random
    rng = random.Random(seed)
    total = pairs = terms = 0
    for p in primerange(max(int(lo), 3), int(hi)):
        if p % 4 != 1:
            continue
        r = _sqrt_minus_one(p, rng)
        for root in {r, p - r}:
            sl = mu[root::p]
            total += abs(int(sl.sum()))
            pairs += 1
            terms += len(sl)
    if pairs == 0:
        return float("nan"), 0
    return (total / pairs) / sqrt(terms / pairs), pairs


def fit_c(points: list[tuple[int, float]]) -> float:
    """OLS of log rho against log log X."""
    xs = [log(log(x)) for x, _ in points]
    ys = [log(r) for _, r in points]
    mx, my = sum(xs) / len(xs), sum(ys) / len(ys)
    den = sum((x - mx) ** 2 for x in xs)
    return sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / den if den else float("nan")


def sweep(arrays: dict[str, dict[int, np.ndarray]], ladder: list[int],
          phases: list[float], band_decades: float = 1.0) -> dict:
    """For each signal and band phase, fit c on the widest well-sampled band."""
    out: dict[str, list[float]] = {}
    for name, per_x in arrays.items():
        cs = []
        for phase in phases:
            # widest band that has >= 3 ladder points and decent statistics
            best: list[tuple[int, float]] = []
            k = 3.0
            while 10 ** (k + phase + band_decades) <= max(ladder):
                lo, hi = 10 ** (k + phase), 10 ** (k + phase + band_decades)
                pts = []
                for X in ladder:
                    if hi > X:
                        continue
                    rho, pairs = band_rho(per_x[X], lo, hi)
                    if pairs >= 2000 and not np.isnan(rho):
                        pts.append((X, rho))
                if len(pts) > len(best):
                    best = pts
                k += 1.0
            if len(best) >= 3:
                cs.append(fit_c(best))
        out[name] = cs
    return out


def main(X_max: int = 10**6, n_phases: int = 8) -> None:
    ladder = []
    X = 10**4
    while X <= X_max:
        ladder.append(X)
        X = int(X * sqrt(10))
    phases = [i / n_phases for i in range(n_phases)]
    print(f"X ladder: {ladder}")
    print(f"band phases (log10): {[round(p, 3) for p in phases]}\n")

    g = np.random.default_rng(11)
    signals: dict[str, dict[int, np.ndarray]] = {"actual": {}, "iid null": {}, "damped -0.5": {}}
    for X in ladder:
        mu = mobius_x2plus1(X)
        d = float((mu[1:] != 0).mean())
        signals["actual"][X] = mu
        signals["iid null"][X] = np.where(
            g.random(X + 1) < d, g.choice([-1, 1], X + 1), 0
        ).astype(np.int8)
        # Inject a (log X)^{-1/2} damping by thinning the null's density, which
        # scales |Sum| by the same factor and so shows up as c = -1/2.
        scale = (log(ladder[0]) / log(X))
        signals["damped -0.5"][X] = np.where(
            g.random(X + 1) < d * scale, g.choice([-1, 1], X + 1), 0
        ).astype(np.int8)

    res = sweep(signals, ladder, phases)
    print(f"{'signal':>14} {'phases':>7} {'mean c':>8} {'spread':>8} {'min':>8} {'max':>8}")
    print("-" * 60)
    for name, cs in res.items():
        if not cs:
            print(f"{name:>14} {'--':>7}")
            continue
        print(f"{name:>14} {len(cs):>7} {np.mean(cs):>8.3f} {np.ptp(cs):>8.3f} "
              f"{min(cs):>8.3f} {max(cs):>8.3f}")

    print()
    print("Reading it: 'iid null' must sit near 0 and 'damped -0.5' near -0.5,")
    print("or the estimator cannot see a log-power and 'actual' means nothing.")
    print("The spread column is the error bar the earlier single-phase fit lacked.")


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    main(int(args[0]) if args else 10**6, int(args[1]) if len(args) > 1 else 8)
