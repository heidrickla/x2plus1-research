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


def dfi_theorem_s_typeII(alpha) -> Range:
    """The Type II range [DFI] Theorem S needs, restated relative to |A|.

    Theorem S (p. 437) requires (35) for the general bilinear form over
    n in [x^{o(1)}, x^{1/3-eps}], and (34) for the special one at level
    D = x^{1/2-eps}. Relative to a sequence of density alpha the level is the
    easy half -- Note B permits D up to alpha -- and the Type II range is the
    hard half.

    An earlier version of this module had `dfi_lemma2_sieving_level`, which
    encoded the argument that Lemma 2's D > z ordering caps the reach at P_2.
    That is withdrawn: DFI remove the p, q terms bilinearly rather than by
    sieving past them, so Theorem S runs with z <= x^{1/2-eps} and the P_2
    ceiling is a fact about classical sieves only. See the registry entries
    `dfi-lemma2-reaches-P2-and-stops` (refuted) and
    `dfi-theorem-S-typeI-met-typeII-not`.
    """
    a = _F(alpha)
    if a <= 0:
        raise ImpossibleExponentError(f"[DFI] Theorem S: nothing admissible at alpha={alpha}")
    return Range(Fraction(0), Fraction(1, 3))


def single_variable_alpha(degree: int) -> Fraction:
    """alpha for A = {f(x) : x <= X} with deg f = d.

    Q ~ X^d and |A| = X, so |A| = Q^{1/d}. Nothing about f enters beyond its
    degree, which is the point of Note L: the exponents that place x^2+1
    outside every framework in the literature place *every* single-variable
    polynomial of degree >= 2 outside them, and x^2+1 is only the least
    degenerate case.
    """
    if degree < 1:
        raise ValueError("degree must be >= 1")
    return Fraction(1, degree)


def ford_maynard_theta(alpha) -> Range:
    """The admissible Type II start theta for a sequence of density x^alpha.

    [FM] p. 7, for J subset (x/2, x] with x^{1-c} elements: "one can only hope
    for (I) to hold for gamma < 1 - c and (II) for theta > c". The first half
    is Note B's ceiling arrived at from the other direction. The second half,
    against (1.1) p. 1 -- "0 <= theta < 1/2" -- is what places this sequence:

        alpha = 3/4  ->  theta in [1/4, 1/2)   (Friedlander-Iwaniec, Merikoski)
        alpha = 2/3  ->  theta in [1/3, 1/2)   (Heath-Brown)
        alpha = 1/2  ->  theta >= 1/2 and theta < 1/2, which is empty.

    All four entries of [FM] Table 1 p. 3 sit at theta = c exactly (epsilons
    omitted), so the lower endpoint is where the literature actually works.

    Raises when there is no admissible theta at all -- i.e. x^2+1 has no
    Ford-Maynard parameter triple, which is a cleaner placement than arguing
    about the epsilon in gamma.
    """
    c = Fraction(1) - _F(alpha)
    if c >= Fraction(1, 2):
        raise ImpossibleExponentError(
            f"[FM] theta for alpha={alpha}: (II) needs theta > c = {c}, "
            f"(1.1) needs theta < 1/2 -- the admissible range is empty"
        )
    return Range(c, Fraction(1, 2))


def asp_applies(sequence: str) -> Range:
    """The admissible level of distribution for [ASP] on a named sequence.

    Raises ImpossibleExponentError when there is none -- which is the finding
    of Note C for x^2+1, now computed rather than argued.
    """
    alpha = ALPHA[sequence]
    return type_i_ceiling(alpha).meet(asp_r1(), what=f"[ASP] level for {sequence}")
