"""The repo's exponent chains, computed rather than argued.

Every assertion here is a claim some note makes in prose. If a note and this
file disagree, one of them is wrong and the disagreement is now visible.
"""

from fractions import Fraction

import pytest

from x2plus1.exponents import (
    ALPHA, ImpossibleExponentError, Range, asp_applies, asp_r1,
    ford_maynard_theta, gamma_annihilation_threshold, inner_range_exponent,
    kappa_exponent, truncation_exponent, type_i_ceiling,
)


def test_ranges_reject_emptiness_at_construction():
    with pytest.raises(ImpossibleExponentError):
        Range(Fraction(2, 3), Fraction(1, 2))


def test_asp_does_not_apply_to_x2plus1_and_says_so_by_raising():
    """Note C's central finding, as a computation.

    Type I caps at alpha = 1/2; (R1) demands more than 2/3; the intersection is
    empty. Previously a paragraph, which is how it got over-read twice.
    """
    with pytest.raises(ImpossibleExponentError, match="empty"):
        asp_applies("x^2+1")


def test_asp_does_apply_to_a2b4():
    """The control: at alpha = 3/4 the same computation must NOT raise."""
    admissible = asp_applies("a^2+b^4")
    assert admissible.lo == Fraction(2, 3)
    assert admissible.hi == Fraction(3, 4)
    assert Fraction(3, 4) in admissible          # FI achieve x^{3/4-5eps}


def test_x3_2y3_sits_exactly_on_the_boundary():
    """Heath-Brown's case: the admissible range degenerates to a point.

    Which is exactly why he wrote "their condition (R1) is not quite met in our
    case" -- the range is the single point 2/3, and he had x^{2/3-eps}.
    """
    admissible = asp_applies("x^3+2y^3")
    assert admissible.lo == admissible.hi == Fraction(2, 3)


def test_the_two_thirds_is_derived_not_quoted():
    """C = x^{1-theta} must stay under N = x^{theta/2}; solve for theta."""
    t = gamma_annihilation_threshold()
    assert t == Fraction(2, 3)
    # at the threshold the two exponents coincide
    assert truncation_exponent(t) == inner_range_exponent(t)
    # below it the truncation overruns the inner range, so gamma(n,C) dies
    assert truncation_exponent(Fraction(1, 2)) > inner_range_exponent(Fraction(1, 2))
    # above it there is room
    assert truncation_exponent(Fraction(3, 4)) < inner_range_exponent(Fraction(3, 4))


def test_the_truncation_overruns_by_a_quarter_at_alpha_half():
    """Note C says C/N ~ x^{1/4} for x^2+1. Check the arithmetic."""
    theta = Fraction(1, 2)
    assert truncation_exponent(theta) - inner_range_exponent(theta) == Fraction(1, 4)


def test_kappa_is_one_exactly_at_alpha_half():
    """Note F: kappa = |A|^2/Q, so its exponent is 2 alpha - 1."""
    assert kappa_exponent(ALPHA["x^2+1"]) == 0          # kappa = x^0 = 1
    assert kappa_exponent(ALPHA["a^2+b^4"]) == Fraction(1, 2)
    assert kappa_exponent(ALPHA["x^3+2y^3"]) == Fraction(1, 3)
    assert kappa_exponent(ALPHA["a^2+b^2"]) == 1


def test_kappa_exceeds_one_exactly_when_alpha_exceeds_half():
    for name, alpha in ALPHA.items():
        assert (kappa_exponent(alpha) > 0) == (alpha > Fraction(1, 2)), name


def test_dfi_level_half_is_reachable_where_asp_is_not():
    """Note C: DFI's Type I *exponent* is reachable here where ASP's is not.

    DFI needs theta ~ 1/2; the ceiling is alpha = 1/2; so the admissible set is
    the single point 1/2 -- tight, but non-empty, unlike ASP.

    This is a statement about exponents only. It is NOT the claim that x^2+1
    satisfies DFI's Type I hypothesis, which is `refuted` in the registry
    (x2plus1-meets-dfi-typeI): DFI's Theorem S is normalised to x and is
    vacuous on a sequence of mass x^{1/2}. The exponents line up; the
    hypothesis does not.
    """
    ceiling = type_i_ceiling(ALPHA["x^2+1"])
    dfi = Range.at_least(Fraction(1, 2))
    admissible = ceiling.meet(dfi, what="DFI level for x^2+1")
    assert admissible.lo == admissible.hi == Fraction(1, 2)
    # and ASP over the same ceiling is empty
    with pytest.raises(ImpossibleExponentError):
        ceiling.meet(asp_r1(), what="ASP level for x^2+1")


def test_note_j_moduli_range_sits_below_the_sequence_size():
    """Note J: moduli to X^{3/4} for a sequence of X terms.

    The counting bound bites only above X, so 3/4 < 1 leaves room -- this is
    why the Type I argument does not transfer to the Type II input.
    """
    moduli = Range.at(Fraction(3, 4))
    assert moduli.hi < 1


def test_ford_maynard_admits_the_solved_densities_and_not_this_one():
    """[FM] p.7 with (1.1) p.1: theta > c = 1 - alpha, and theta < 1/2.

    Note C's placement of x^2+1 used to run through the epsilon in gamma. This
    is the same conclusion without the epsilon: at alpha = 1/2 there is no
    admissible theta at all, so the sequence has no Ford-Maynard triple.
    """
    assert ford_maynard_theta(Fraction(3, 4)).lo == Fraction(1, 4)   # FI, Merikoski
    assert ford_maynard_theta(Fraction(2, 3)).lo == Fraction(1, 3)   # Heath-Brown
    with pytest.raises(ImpossibleExponentError):
        ford_maynard_theta(ALPHA["x^2+1"])


def test_the_literature_sits_at_theta_equal_to_c():
    """Every entry of [FM] Table 1 p.3 with a known density has theta = 1 - alpha.

    (gamma, theta, nu) as tabulated, epsilons omitted by their own caption.
    """
    table = {                    # alpha,        gamma,        theta,        nu
        "a^2+b^4":       (Fraction(3, 4), Fraction(3, 4), Fraction(1, 4), Fraction(1, 2)),
        "x^3+2y^3":      (Fraction(2, 3), Fraction(2, 3), Fraction(1, 3), Fraction(1, 3)),
        "a^2+(b^2+1)^2": (Fraction(3, 4), Fraction(3, 4), Fraction(1, 4), Fraction(1, 12)),
    }
    for name, (alpha, gamma, theta, nu) in table.items():
        assert gamma == alpha, name                       # gamma = 1 - c
        assert theta == Fraction(1) - alpha, name         # theta = c
        assert theta in ford_maynard_theta(alpha), name
        assert nu > 0, name                               # (1.1) needs nu > 0
