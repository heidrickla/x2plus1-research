"""Type I: level of distribution of A in Gaussian ideals.

For an ideal d we want

    A_d(N) := #{ a in A : d | a }  =  g(d) |A|  +  r_d ,

and the level of distribution is the largest D for which

    Sigma_{N(d) <= D} |r_d|  =  o(|A|).

For A = {x + i}, admissible ideals are in bijection with roots of r^2+1:

    d | x + i   <=>   x == r_d  (mod N(d)),

one residue class, so |r_d| <= 1 always.  The Type I sum is therefore
bounded by the *number of admissible ideals*, which is ~ (3/2pi) D:

    Sigma_{admissible d} N(d)^{-s} = zeta(s) L(s, chi_4) / zeta(2s),

with residue L(1,chi_4)/zeta(2) = (pi/4)/(pi^2/6) = 3/(2 pi) = 0.47746...

Hence Sigma_{N(d)<=D} |r_d| ~ c D, and the constraint is D = o(|A|).  In the
sieve's own variable (n <= N, so |A| ~ N^{1/2}) that reads D = N^{1/2 - eps}.
This is the computation Note B has to make unimprovable-by-this-argument.
"""

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass

from .factorization import roots_of_minus_one
from .gaussian import Gauss, norm, unit_normalize
from .sequences import GaussianSequence


def count_in_progression(X: int, q: int, r: int) -> int:
    """#{ 1 <= x <= X : x == r (mod q) }."""
    first = r % q
    if first == 0:
        first = q
    return 0 if first > X else (X - first) // q + 1


@dataclass
class TypeIReport:
    D: int
    n_moduli: int          # number of admissible ideals of norm <= D
    total_error: float     # Sigma |r_d|
    max_error: float
    main_mass: float       # Sigma g(d)|A|, for scale
    size: int              # |A|

    @property
    def ratio(self) -> float:
        """Sigma|r_d| / |A|.  Type I holds at level D while this is o(1)."""
        return self.total_error / self.size if self.size else float("nan")


def type_i_x2plus1(X: int, D: int) -> TypeIReport:
    """Exact Type I sum for A = {x + i : x <= X}, over all ideals of norm <= D.

    Uses the congruence description, so D may greatly exceed X.
    """
    total = 0.0
    worst = 0.0
    main = 0.0
    count = 0
    for q in range(1, D + 1):
        for r in roots_of_minus_one(q):
            count += 1
            err = abs(count_in_progression(X, q, r) - X / q)
            total += err
            worst = max(worst, err)
            main += X / q
    return TypeIReport(D, count, total, worst, main, X)


def divisor_ideal_counts(seq: GaussianSequence, D: int) -> dict[Gauss, int]:
    """A_d for every ideal d with N(d) <= D, by walking divisors of each a in A.

    Works for any sequence (used for the a^2+b^4 ledger).  Cost is
    Sigma_a #{divisors of a of norm <= D}.
    """
    counts: dict[Gauss, int] = defaultdict(int)
    for _z, fac in seq:
        divs: list[Gauss] = [(1, 0)]
        for pi, e in fac:
            npi = norm(pi)
            grown: list[Gauss] = []
            for d in divs:
                nd, cur = norm(d), d
                for _ in range(e + 1):
                    if nd > D:
                        break
                    grown.append(cur)
                    cur = unit_normalize((cur[0] * pi[0] - cur[1] * pi[1],
                                          cur[0] * pi[1] + cur[1] * pi[0]))
                    nd *= npi
            divs = grown
        for d in divs:
            counts[d] += 1
    return dict(counts)


def type_i_generic(seq: GaussianSequence, D: int, g=None) -> TypeIReport:
    """Type I sum for an arbitrary sequence.

    ``g(d)`` defaults to 1/N(d), the local density for both sequences here on
    admissible d.  Ideals with A_d = 0 and g(d) > 0 still contribute, so the
    admissible set is enumerated independently of what actually occurred.
    """
    if g is None:
        def g(d: Gauss) -> float:
            return 1.0 / norm(d)

    counts = divisor_ideal_counts(seq, D)
    size = len(seq)
    total = 0.0
    worst = 0.0
    main = 0.0
    n_mod = 0
    for q in range(1, D + 1):
        for r in roots_of_minus_one(q):
            n_mod += 1
    # Only ideals that are admissible for *this* sequence can have g > 0;
    # for both of our sequences that is exactly the r^2+1 ideals.
    seen: set[Gauss] = set(counts)
    for q in range(1, D + 1):
        for r in roots_of_minus_one(q):
            d = _ideal_from_root(q, r)
            expected = g(d) * size
            err = abs(counts.get(d, 0) - expected)
            total += err
            worst = max(worst, err)
            main += expected
            seen.discard(d)
    # Anything divided A but was not enumerated as admissible: report it loudly.
    for d in seen:
        total += counts[d]
        worst = max(worst, counts[d])
    return TypeIReport(D, n_mod, total, worst, main, size)


def _ideal_from_root(q: int, r: int) -> Gauss:
    """The ideal d of norm q with d | x + i exactly when x == r (mod q)."""
    from .gaussian import gcd
    return gcd((q, 0), (r, 1))


def sweep(X: int, exponents: list[float]) -> list[tuple[float, TypeIReport]]:
    """Type I sum at D = X^theta, for the exponents given (theta relative to X)."""
    return [(t, type_i_x2plus1(X, max(1, int(X**t)))) for t in exponents]
