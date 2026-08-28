"""Note O -- the multiplier tau, and why no window holds three shared moduli."""

from math import isqrt, sqrt

import pytest

from x2plus1.polyseq import close_pairs, ratio_classes

X = 1600   # >= 1507, so (1,53) shows both of its close pairs
CLASSES = ratio_classes(X)
PAIRS = list(close_pairs(CLASSES))


def test_the_pair_invariant_is_an_identity():
    """U^2 - D V^2 = M^2 for every pair of shared moduli, with no exceptions."""
    for a, b, mi, mj, V, _tau in PAIRS:
        Xi, Yi = isqrt(a * mi - 1), isqrt(b * mi - 1)
        Xj, Yj = isqrt(a * mj - 1), isqrt(b * mj - 1)
        U = b * Xi * Xj - a * Yi * Yj
        assert U * U - (a * b) * V * V == (b - a) ** 2, (a, b, mi, mj)


def test_V_is_never_zero_and_never_one():
    """V = 0 would mean proportional solutions; |V| = 1 needs a^2-ab+b^2 square."""
    assert PAIRS, "no close pairs found -- X too small"
    assert all(V != 0 for *_h, V, _t in PAIRS)
    assert min(abs(V) for *_h, V, _t in PAIRS) == 2


def test_gap_principle_threshold_is_respected():
    """|V| >= 2 with r <= sqrt(2) forces M/sqrt(D) >= 2*2/(sqrt2 - 1/sqrt2)."""
    threshold = 4 / (sqrt(2) - 1 / sqrt(2))
    observed = min((b - a) / sqrt(a * b) for a, b, *_ in PAIRS)
    assert observed >= threshold * 0.999, (observed, threshold)


def test_tau_squared_law_holds_with_error_O_one_over_m():
    """m_j/m_i = tau^2 (1 + O(1/m)).  Asymptotic, NOT exact -- see Note O."""
    worst = max(
        abs(mj / mi - tau * tau) / (tau * tau) * mi
        for _a, _b, mi, mj, _V, tau in PAIRS
    )
    assert worst < 200, worst
    tight = [
        abs(mj / mi - tau * tau) / (tau * tau)
        for _a, _b, mi, mj, _V, tau in PAIRS
        if mi >= 1000
    ]
    assert tight and max(tight) < 1e-3, max(tight)


def test_tau_acts_at_most_once_per_solution():
    """Proposition O.1.  tau^4 < 2 means a third WOULD fit; none is ever there.

    Per SOLUTION, not per class: a class may hold several close pairs at
    separated positions -- see test_a_class_may_hold_two_close_pairs.
    """
    chances = 0
    nontrivial = 0
    for a, b, mi, mj, _V, tau in PAIRS:
        if tau**4 >= 2:
            continue
        chances += 1
        nontrivial += a >= 2
        third = [m for m in CLASSES[(a, b)] if mi < m < 2 * mi and m not in (mi, mj)]
        assert not third, (a, b, mi, mj, third)
    assert chances > 0, "no falsification chances -- test is vacuous"
    assert nontrivial > 0, "all chances have a = 1 -- would not cover the Type II case"


@pytest.mark.parametrize("a,b,expected", [(2, 85, 1.8525), (13, 449, 1.9880)])
def test_named_multipliers_from_the_note(a, b, expected):
    tau = (sqrt(b) + sqrt(a)) / (sqrt(b) - sqrt(a))
    assert tau * tau == pytest.approx(expected, rel=2e-3)


def test_a_class_may_hold_two_close_pairs():
    """The qualifier in Prop O.1 is load-bearing: (1,53) has two close pairs.

    tau acting twice in a CLASS is fine and observed; what Prop O.1 forbids is
    tau acting twice on one solution, i.e. a third modulus in one window.
    """
    per_class = {}
    for a, b, mi, mj, _V, _t in PAIRS:
        per_class.setdefault((a, b), []).append((mi, mj))
    multi = {k: v for k, v in per_class.items() if len(v) > 1}
    assert multi, "expected at least one class with two close pairs"
    for (a, b), prs in multi.items():
        tau2 = ((sqrt(b) + sqrt(a)) / (sqrt(b) - sqrt(a))) ** 2
        for mi, mj in prs:
            assert mj < 2 * mi
            assert abs(mj / mi - tau2) / tau2 * mi < 200


def test_the_AB_identity_that_carries_the_proof():
    """A - B = -(m_j - m_i) M exactly, where V = sqrt(A) - sqrt(B).

    This is the step that makes the window hypothesis bite: m_j - m_i < m_i.
    """
    for a, b, mi, mj, _V, _t in PAIRS:
        A = (a * mi - 1) * (b * mj - 1)
        B = (a * mj - 1) * (b * mi - 1)
        assert A - B == -(mj - mi) * (b - a), (a, b, mi, mj)


def test_V_is_below_M_over_sqrt_D():
    """|V| < M/sqrt(D) for m_i >= 2 -- the bound that closes M > g^2."""
    for a, b, mi, mj, V, _t in PAIRS:
        if mi < 2:
            continue
        assert abs(V) < (b - a) / sqrt(a * b), (a, b, mi, mj, V)


def test_solution_element_has_norm_a_times_M():
    """N(xi) = aM, NOT +-M.  The factor a is load-bearing in Prop O.1."""
    for a, b, mi, _mj, _V, _t in PAIRS:
        Xi, Yi = isqrt(a * mi - 1), isqrt(b * mi - 1)
        assert a * a * Yi * Yi - (a * b) * Xi * Xi == a * (b - a), (a, b, mi)


def test_ratio_of_solutions_is_P_over_M():
    """xi_2 conj(xi_1) = -a (U + V sqrt D), so xi_2/xi_1 = -P/M."""
    for a, b, mi, mj, V, _t in PAIRS:
        Xi, Yi = isqrt(a * mi - 1), isqrt(b * mi - 1)
        Xj, Yj = isqrt(a * mj - 1), isqrt(b * mj - 1)
        U = b * Xi * Xj - a * Yi * Yj
        assert a * a * Yi * Yj - (a * b) * Xi * Xj == -a * U, (a, b, mi, mj)
        assert a * (Yi * Xj - Yj * Xi) == -a * V, (a, b, mi, mj)


def test_M_exceeds_a_times_gcd_UV_squared():
    """The single inequality Prop O.1 turns on, with no hypothesis on V.

    A third modulus needs M <= a g^2; the window forces a g^2 < M^2/b < M.
    """
    from math import gcd
    for a, b, mi, mj, V, _t in PAIRS:
        Xi, Yi = isqrt(a * mi - 1), isqrt(b * mi - 1)
        Xj, Yj = isqrt(a * mj - 1), isqrt(b * mj - 1)
        g = gcd(abs(b * Xi * Xj - a * Yi * Yj), abs(V))
        M = b - a
        assert M % g == 0, "g must divide M"
        assert M > a * g * g, (a, b, mi, mj, M, a, g)


def test_V_is_even_when_a_and_b_are_both_odd():
    """Parity lemma: X_k = Y_k mod 2, so V is even.  Explains g = 2."""
    for a, b, mi, mj, V, _t in PAIRS:
        if a % 2 and b % 2:
            assert V % 2 == 0, (a, b, mi, mj, V)
