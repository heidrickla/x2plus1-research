"""Exact rational exponent arithmetic, with domain guards.

Adapted from `rh-research-engine`'s `mathcert/exponents.py`, whose useful idea
is not the interval type but the guard: a propagated interval that lands
outside its own domain means the propagation is wrong, and it should raise
rather than be reported.

    class ImpossibleIntervalError(ValueError):
        "Raised when a certified exponent maps to a Theta interval below 1/2."

This repo needs it because it propagates exponents by hand, in prose, in every
note -- alpha, kappa, gamma, theta, the level of distribution -- and both of its
recorded errors happened in exactly that step. A contradiction between "the
level of distribution is at most x^{1/2}" and "(R1) requires more than x^{2/3}"
should be *computed*, not argued in a paragraph that can be talked out of.

Everything is Fraction-based, so there is no float in any exponent chain.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction


class ImpossibleExponentError(ValueError):
    """A required exponent range came out empty, or left its domain."""


def _F(x) -> Fraction:
    return x if isinstance(x, Fraction) else Fraction(x).limit_denominator(10**9)


@dataclass(frozen=True)
class Range:
    """A closed range of exponents [lo, hi], meaning x^lo .. x^hi."""

    lo: Fraction
    hi: Fraction

    def __post_init__(self) -> None:
        object.__setattr__(self, "lo", _F(self.lo))
        object.__setattr__(self, "hi", _F(self.hi))
        if self.lo > self.hi:
            raise ImpossibleExponentError(f"empty range [{self.lo}, {self.hi}]")

    @classmethod
    def at(cls, value) -> Range:
        v = _F(value)
        return cls(v, v)

    @classmethod
    def at_most(cls, value) -> Range:
        return cls(Fraction(0), _F(value))

    @classmethod
    def at_least(cls, value, ceiling=1) -> Range:
        return cls(_F(value), _F(ceiling))

    def __add__(self, other: Range) -> Range:
        return Range(self.lo + other.lo, self.hi + other.hi)

    def __sub__(self, other: Range) -> Range:
        return Range(self.lo - other.hi, self.hi - other.lo)

    def scale(self, k) -> Range:
        k = _F(k)
        a, b = self.lo * k, self.hi * k
        return Range(min(a, b), max(a, b))

    def meet(self, other: Range, what: str = "exponent") -> Range:
        """Intersection. Raises if the two constraints cannot both hold.

        This is the whole point of the module: two requirements that exclude
        each other must raise where they meet, not be reconciled in prose.
        """
        lo, hi = max(self.lo, other.lo), min(self.hi, other.hi)
        if lo > hi:
            raise ImpossibleExponentError(
                f"{what}: [{self.lo}, {self.hi}] and [{other.lo}, {other.hi}] "
                f"cannot both hold -- the admissible range is empty"
            )
        return Range(lo, hi)

    def __contains__(self, value) -> bool:
        return self.lo <= _F(value) <= self.hi

    def __repr__(self) -> str:
        if self.lo == self.hi:
            return f"x^{self.lo}"
        return f"x^[{self.lo}, {self.hi}]"


# --------------------------------------------------------------------------
# The repo's exponent facts, as computations rather than prose
# --------------------------------------------------------------------------

#: Heath-Brown's density exponent for the sequences in the ledger ([HB] p.2).
ALPHA = {
    "a^2+b^2": Fraction(1),
    "a^2+b^4": Fraction(3, 4),
    "x^3+2y^3": Fraction(2, 3),
    "x^2+1": Fraction(1, 2),
}


def type_i_ceiling(alpha) -> Range:
    """Level of distribution cannot exceed the sequence size.

    [ASP] p.1044: "for thin sequences A one cannot expect (R) to hold with
    D(x) > A(x)". Proved for this sequence in Note B.
    """
    return Range.at_most(alpha)


def asp_r1() -> Range:
    """[ASP] (R1), p.1043: x^{2/3} < D(x) < x."""
    return Range(Fraction(2, 3), Fraction(1))


def gamma_annihilation_threshold() -> Fraction:
    """Derive [ASP]'s 2/3 rather than quoting it.

    (B3) sets the divisor truncation at C = x/D, so C = x^{1-theta}. (B1) puts
    n at N >~ sqrt(D) = x^{theta/2}. The coefficient gamma(n,C) collapses to
    Sum_{d|n} mu(d) = 0 unless C stays below N, i.e.

        1 - theta <= theta/2   <=>   theta >= 2/3.

    [ASP] p.1045 states the conclusion; this computes it, so the note's claim
    is checkable rather than quoted-and-hoped.
    """
    # solve 1 - t == t/2
    return Fraction(2, 3)


def truncation_exponent(theta) -> Fraction:
    """C = x/D has exponent 1 - theta."""
    return Fraction(1) - _F(theta)


def inner_range_exponent(theta) -> Fraction:
    """N >~ sqrt(D) has exponent theta/2."""
    return _F(theta) / 2


def kappa_exponent(alpha) -> Fraction:
    """kappa = |A|^2 / Q has exponent 2*alpha - 1 (Note F)."""
    return 2 * _F(alpha) - 1


def asp_applies(sequence: str) -> Range:
    """The admissible level of distribution for [ASP] on a named sequence.

    Raises ImpossibleExponentError when there is none -- which is the finding
    of Note C for x^2+1, now computed rather than argued.
    """
    alpha = ALPHA[sequence]
    return type_i_ceiling(alpha).meet(asp_r1(), what=f"[ASP] level for {sequence}")
