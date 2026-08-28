"""The sifted sets, as subsets of Z[i].

Both sequences in this project are sets of Gaussian integers whose *norm* is
the quantity being tested for primality.  Writing them in the same language is
the point of Note A / Note D:

    x^2 + 1  = N(x + i)          A_1 = { z : Im z = 1 }
    a^2 + b^4 = N(a + b^2 i)     A_2 = { z : Im z is a perfect square }

So Friedlander-Iwaniec sift Gaussian integers lying over a *parabola* of
imaginary parts, and this project sifts those lying on the single horizontal
line Im = 1.  The two-parameter freedom that FI exploit is exactly the freedom
to move b; here that freedom is gone.  Counted by norm bound N:

    |A_1 (N)| ~ N^{1/2}      |A_2 (N)| ~ c N^{3/4}

which is the density gap the plan flags.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from math import isqrt

from .factorization import gauss_factor_x_plus_i, sieve_shifted_square
from .gaussian import Gauss, conj, exact_div, factor_gauss, norm, split_prime, unit_normalize


@dataclass
class GaussianSequence:
    """A finite multiset A of Gaussian integers together with their factorisations."""

    name: str
    norm_bound: int
    elements: list[Gauss]
    factorisations: list[list[tuple[Gauss, int]]] = field(repr=False)

    def __len__(self) -> int:
        return len(self.elements)

    def __iter__(self):
        return zip(self.elements, self.factorisations)


def _gauss_factor_shifted(z: Gauss, rational_fac: dict[int, int]) -> list[tuple[Gauss, int]]:
    """Factor z in Z[i] given the rational factorisation of N(z).

    Unlike x + i, a general z may be divisible by an inert prime or by both
    primes above a split p, so each prime power must be tested.
    """
    out: list[tuple[Gauss, int]] = []
    rest = z
    for p, e in sorted(rational_fac.items()):
        if p % 4 == 3:
            k = e // 2
            if k:
                out.append(((p, 0), k))
                for _ in range(k):
                    rest = exact_div(rest, (p, 0))
            continue
        pi = split_prime(p)
        for cand in ({unit_normalize(pi), unit_normalize(conj(pi))}):
            k = 0
            while (nxt := exact_div(rest, cand)) is not None:
                rest, k = nxt, k + 1
            if k:
                out.append((cand, k))
    assert norm(rest) == 1, f"leftover {rest} factoring {z}"
    return out


def x2plus1_sequence(norm_bound: int) -> GaussianSequence:
    """A = { x + i : 1 <= x, x^2 + 1 <= norm_bound }."""
    X = isqrt(max(norm_bound - 1, 0))
    F = sieve_shifted_square(X, 1)
    elements = [(x, 1) for x in range(1, X + 1)]
    facs = [gauss_factor_x_plus_i(x, F[x]) for x in range(1, X + 1)]
    return GaussianSequence("x^2+1", norm_bound, elements, facs)


def a2b4_sequence(norm_bound: int) -> GaussianSequence:
    """A = { a + b^2 i : a, b >= 1, a^2 + b^4 <= norm_bound }.

    The Friedlander-Iwaniec set, in the same coordinates.  Note that b >= 1 is
    imposed (b = 0 would give the squares, which are never prime).
    """
    elements: list[Gauss] = []
    facs: list[list[tuple[Gauss, int]]] = []
    b = 1
    while b**4 < norm_bound:
        c = b**4
        A = isqrt(norm_bound - c)
        if A >= 1:
            F = sieve_shifted_square(A, c)
            for a in range(1, A + 1):
                z = (a, b * b)
                elements.append(z)
                facs.append(_gauss_factor_shifted(z, F[a]))
        b += 1
    return GaussianSequence("a^2+b^4", norm_bound, elements, facs)


def by_x_range(X: int) -> GaussianSequence:
    """A = { x + i : 1 <= x <= X }.  Convenience wrapper in the x variable."""
    return x2plus1_sequence(X * X + 1)
