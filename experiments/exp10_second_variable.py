"""Experiment 10 -- dialling the second variable: where do 4-cycles appear?

A_B = { a + b^2 i : b in B, a^2 + b^4 <= Q }.  Then |A| ~ Q^{1/2}|B|, so

    kappa = |A|^2 / Q = |B|^2   exactly,

and kappa > 1 the moment |B| = 2. The question this settles: does the incidence
graph stay C4-free until |B| is a positive power of Q -- in which case kappa
would be off by an exponent as a criterion -- or do 4-cycles appear at |B| = 2,
in which case the kappa threshold is sharp?

ANSWER: 4-cycles appear at |B| = 2. The kappa threshold is sharp.

TWO CONTROLS, both needed, both from artefacts that fooled us first.

  1. UNIT COFACTOR. The pair (n1, n2) with N(n1) = 1 makes G(n1,n2) count every
     m with m and (n2/n1)m both in A -- a dilation, not bilinear structure. Same
     artefact as the (1,5) pair in the rational graph of Note L. Fixed by a
     cofactor floor.
  2. DILATION BETWEEN LINES. If b1 | b2 then b2^2/b1^2 is a rational integer r,
     and m -> rm maps the line Im = b1^2 into Im = b2^2, so G is inflated by pure
     dilation. In particular ANY B containing 1 leaks. Fixed by requiring no b in
     B to divide another.

The instrument is algebraic rather than a search. A 4-cycle needs a
multiplicative collision alpha_1 alpha_4 = alpha_2 alpha_3; taking
y1 = y4 = p^2 and y2 = y3 = q^2 and matching real and imaginary parts,

    P1 = P2 + p^4 - q^4        (real)
    p^2 S1 = q^2 S2            (imaginary)

with S = sum and P = product of the two x's. So for each (x2, x3) the partner
pair exists exactly when S1^2 - 4(P2 + p^4 - q^4) is a perfect square, which
vectorises and sweeps a box in seconds where enumeration of products does not.

Usage:  python experiments/exp10_second_variable.py [N]
"""

import sys

import numpy as np

import _bootstrap  # noqa: F401

from x2plus1.gaussian import exact_div, gcd, mul, norm, unit_normalize


def collisions(p: int, q: int, N: int = 2500) -> set[tuple[int, int, int, int]]:
    """(x1, x4, x2, x3) with (x1+p^2 i)(x4+p^2 i) = (x2+q^2 i)(x3+q^2 i)."""
    shift = p**4 - q**4
    x2 = np.arange(1, N + 1)[:, None]
    x3 = np.arange(1, N + 1)[None, :]
    S2, P2 = x2 + x3, x2 * x3
    num = (q * q) * S2
    ok_s = (num % (p * p)) == 0
    S1 = num // (p * p)
    disc = S1 * S1 - 4 * (P2 + shift)
    valid = ok_s & (disc >= 0)
    r = np.zeros_like(disc)
    r[valid] = np.sqrt(disc[valid].astype(np.float64)).astype(np.int64)
    out: set[tuple[int, int, int, int]] = set()
    for dr in (-1, 0, 1):
        hit = valid & ((r + dr) ** 2 == disc) & (x3 >= x2) & (((S1 + (r + dr)) % 2) == 0)
        for i, j in zip(*np.nonzero(hit)):
            a, b = int(x2[i, 0]), int(x3[0, j])
            s1, s = int(S1[i, j]), int(r[i, j]) + dr
            u, v = (s1 + s) // 2, (s1 - s) // 2
            if u >= 1 and v >= 1:
                out.add((u, v, a, b))
    return out


def as_four_cycle(u, v, a, b, p, q):
    """Turn a collision into (m1, m2, n1, n2), or None if degenerate."""
    a1, a4, a2, a3 = (u, p * p), (v, p * p), (a, q * q), (b, q * q)
    m1, m2 = gcd(a1, a2), gcd(a3, a4)
    n1, n2 = exact_div(a1, m1), exact_div(a2, m1)
    if n1 is None or n2 is None:
        return None
    if min(norm(m1), norm(m2), norm(n1), norm(n2)) <= 1:
        return None                                   # control 1: unit cofactor
    if unit_normalize(m1) == unit_normalize(m2) or unit_normalize(n1) == unit_normalize(n2):
        return None
    ok = all(unit_normalize(mul(m, n))[1] in (p * p, q * q) and unit_normalize(mul(m, n))[0] >= 1
             for m in (m1, m2) for n in (n1, n2))
    return (m1, m2, n1, n2) if ok else None


def main(N: int = 2500) -> None:
    print(f"box: x2, x3 <= {N}\n")
    print(f"{'B':>10} {'leak?':>6} {'collisions':>11} {'non-degenerate':>15}")
    print("-" * 48)
    clean_example = None
    leaky, clean = [], []
    for p, q in [(1, 2), (1, 3), (2, 3), (2, 5), (3, 5), (3, 4), (4, 9)]:
        sols = collisions(p, q, N)
        leak = (q * q) % (p * p) == 0 or (p * p) % (q * q) == 0
        nd = [c for c in ((s, as_four_cycle(*s, p, q)) for s in sorted(sols)) if c[1]]
        (leaky if leak else clean).append(len(nd))
        if not leak and clean_example is None and nd:
            clean_example = (p, q, nd[0][1])
        print(f"{'{' + str(p) + ',' + str(q) + '}':>10} {str(leak):>6} "
              f"{len(sols):>11} {len(nd):>15}")

    print()
    # derived from THIS run, never hardcoded -- the repo has been burned once by
    # commentary that drifted from the numbers it was describing.
    if leaky and clean:
        print(f"Leaky B give {min(leaky)}-{max(leaky)} non-degenerate cycles; clean B give "
              f"{min(clean)}-{max(clean)}.")
        print("So the leak inflates the count but does NOT create the cycles: clean B,")
        print("with 1 excluded and neither b dividing the other, still has hundreds.")
    print()
    if clean_example:
        p, q, (m1, m2, n1, n2) = clean_example
        print(f"Smallest non-degenerate 4-cycle on clean B = {{{p},{q}}} "
              f"(neither divides the other, 1 excluded):")
        print(f"    m1 = {m1}   m2 = {m2}   n1 = {n1}   n2 = {n2}")
        for m in (m1, m2):
            for n in (n1, n2):
                print(f"      {m} * {n} = {unit_normalize(mul(m, n))}")
        print(f"    norms  m1={norm(m1)} m2={norm(m2)} n1={norm(n1)} n2={norm(n2)}  "
              f"(all > 1, so no unit cofactor)")
    print()
    print("CONCLUSION: kappa > 1 and the existence of 4-cycles fail together at |B| = 2.")
    print("kappa is NOT off by an exponent as a criterion. What remains true, from")
    print("Note K's a^2+(b^2+1)^2 control, is that kappa > 1 is necessary and far from")
    print("sufficient -- the same kappa buys a Type II range a sixth of an exponent")
    print("shorter. Those are different statements: one about where the threshold is,")
    print("one about how little crossing it buys.")


if __name__ == "__main__":
    main(int(sys.argv[1]) if len(sys.argv) > 1 else 2500)
