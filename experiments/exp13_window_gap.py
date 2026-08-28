"""Experiment 13 -- why no ratio class ever puts three moduli in one window.

Supports Note L. Two sessions measured that the rational incidence graph's
off-diagonal Gram entries never exceed 2 on a dyadic window, and neither could
prove it. This script is the evidence, and it is built to answer the question
the measurement raises rather than to restate it.

THE OBJECT. A pair (n1, n2) = (d a, d b) shares a modulus m for each solution of
b(x^2+1) = a(y^2+1). Bucketing the reduced ratios (y^2+1)/(x^2+1) therefore finds
each pair (a, b) together with ALL of its shared moduli, in one pass and without
reference to the incidence graph -- so it sees configurations the graph's dyadic
windows would hide.

THE STATISTIC. Three moduli in one dyadic window is exactly m_{i+2}/m_i < 2, so
the two-step ratio is what decides it. Reporting the minimum alone is not enough:
a minimum can be an isolated small example. The distribution's lower tail is what
separates "a floor" from "scarcity", and this prints both.

THE RESTRICTION THAT MATTERS. a = 1 means n1 = d, so at d = 1 it is the unit
cofactor -- the degenerate case that drives the full graph's log X growth and
that no Type II split admits. The run therefore reports the floor twice: over all
classes, and over the pairs a split can actually meet. They differ by a factor
of five, and the extremal objects are all in the excluded population.

Usage:  python experiments/exp13_window_gap.py [X]  (X = 5000 takes a few minutes)
"""

import sys
from collections import Counter, defaultdict
from math import gcd

import _bootstrap  # noqa: F401


def ratio_classes(X: int) -> dict[tuple[int, int], list[int]]:
    """{(a, b): sorted shared moduli} over every reduced ratio (y^2+1)/(x^2+1)."""
    vals = [x * x + 1 for x in range(1, X + 1)]
    buckets: dict[tuple[int, int], list[int]] = defaultdict(list)
    for i in range(X):
        u = vals[i]
        for j in range(i + 1, X):
            g = gcd(u, vals[j])
            buckets[(u // g, vals[j] // g)].append(i + 1)
    out = {}
    for (a, b), xs in buckets.items():
        ms = sorted(vals[x - 1] // a for x in xs if vals[x - 1] % a == 0)
        if len(ms) >= 2:
            out[(a, b)] = ms
    return out


def window_max(ms: list[int]) -> int:
    """Most moduli of this class inside one dyadic window [m, 2m)."""
    return max((sum(1 for m in ms if m0 <= m < 2 * m0) for m0 in ms), default=0)


def main(X: int = 5000) -> None:
    classes = ratio_classes(X)
    print(f"X = {X}:  {len(classes)} ratio classes with at least two shared moduli\n")

    hist = Counter(window_max(ms) for ms in classes.values())
    print("  moduli in one dyadic window, over every class:")
    for k in sorted(hist):
        print(f"      {k} : {hist[k]:>6} classes")
    if 3 not in hist:
        print("      3 : none  <- the measurement neither session can prove")

    steps = sorted(
        (ms[i + 2] / ms[i], a, b, ms[i], ms[i + 1], ms[i + 2])
        for (a, b), ms in classes.items()
        for i in range(len(ms) - 2)
    )
    if not steps:
        print("\n  no class has three moduli at this X")
        return

    print(f"\n  two-step ratios m_(i+2)/m_i  ({len(steps)} of them; < 2 would be a third"
          " in a window)")
    print("      ten smallest:")
    for r, a, b, m0, m1, m2 in steps[:10]:
        print(f"      {r:11.4f}   (a,b) = ({a}, {b})   m = {m0}, {m1}, {m2}")
    q = [steps[0][0], steps[len(steps) // 20][0], steps[len(steps) // 4][0],
         steps[len(steps) // 2][0]]
    print(f"      min {q[0]:.3f}   5% {q[1]:.3f}   25% {q[2]:.3f}   median {q[3]:.3f}")

    # a = 1 is n1 = d: at d = 1 the unit cofactor, which no Type II split admits
    rest = [s for s in steps if s[1] >= 2 and s[2] >= 2]
    nrest = sum(1 for (a, b) in classes if a >= 2 and b >= 2)
    print(f"\n  restricted to both cofactors >= 2 -- the pairs a split can meet:")
    print(f"      {nrest} classes, {len(rest)} triples")
    if rest:
        print(f"      minimum two-step ratio {rest[0][0]:.4f} at (a,b) = ({rest[0][1]}, {rest[0][2]})"
              f"   m = {rest[0][3]}, {rest[0][4]}, {rest[0][5]}")
        wm = max(window_max(ms) for (a, b), ms in classes.items() if a >= 2 and b >= 2)
        print(f"      window maximum over that population: {wm}")

    print("\n  Read the lower tail, not the minimum. A cluster resting on a floor with an")
    print("  empty bin beneath it is what a theorem looks like; a smooth approach to 2")
    print("  would be scarcity. Both sessions built a probability model predicting the")
    print("  latter, and the pinned minimum refutes it.")


if __name__ == "__main__":
    main(int(sys.argv[1]) if len(sys.argv) > 1 else 5000)
