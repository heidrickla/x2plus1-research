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


# --- Theorem O.3: the divisibility and the geometry are incompatible ---------

def _multipliers(a, b, kmax=25):
    """(k, U_k) for every |V| = 2k multiplier of the pair (a, b)."""
    M = b - a
    for k in range(1, kmax):
        t = M * M + 4 * k * k * a * b
        u = isqrt(t)
        if u * u == t:
            yield k, u


def test_j_equals_two_exactly_at_k_one():
    """j = 2 B_k / M satisfies j = 2 iff k = 1, and j >= 3 for k >= 2.

    This is what makes the trivial multiplier special and forces e = j^2-4 >= 5
    in Theorem O.3.
    """
    seen = 0
    for a, b in [(1, 5), (2, 85), (1, 85), (5, 481), (1, 65), (13, 449)]:
        M = b - a
        for k, U in _multipliers(a, b):
            seen += 1
            j2 = 2 * (U - 2 * k * a)
            assert (j2 == 2 * M) == (k == 1), (a, b, k)
            if k >= 2:
                assert j2 > 2 * M, (a, b, k)
    assert seen > 5


def test_divisibility_forces_the_M_formula():
    """M | 2B_k with j = 2B_k/M forces M = 8ka(2k-j)/(j^2-4)."""
    checked = 0
    for a in range(1, 60):
        for b in range(a + 1, 900):
            if __import__("math").gcd(a, b) != 1:
                continue
            M = b - a
            for k, U in _multipliers(a, b):
                if (2 * (U - 2 * k * a)) % M:
                    continue
                j = 2 * (U - 2 * k * a) // M
                if j == 2:
                    continue
                assert M * (j * j - 4) == 8 * k * a * (2 * k - j), (a, b, k, j)
                checked += 1
    assert checked > 0, "no k >= 2 divisibility instances found -- test vacuous"


def test_the_incompatibility_quantity_is_always_positive():
    """e^2 + 4jwe + 2w^2(2e-1) > 0 for j >= 3, so Theorem O.3's chain closes."""
    for j in range(3, 200):
        e = j * j - 4
        for w in range(1, 200):
            assert e * e + 4 * j * w * e + 2 * w * w * (2 * e - 1) > 0


def test_M_is_never_two_mod_four():
    """a, b admissible and coprime => M = b-a is odd or divisible by 4.

    Both odd forces a = b = 1 mod 4 hence 4 | M; one even forces M odd.  So
    "M squarefree" already implies "M odd" and Theorem O.3's parity hypothesis
    is redundant -- while the family it misses is exactly 4 | M.
    """
    from x2plus1.factorization import roots_of_minus_one
    from math import gcd

    def adm(k):
        return k == 1 or bool(roots_of_minus_one(k))

    seen = 0
    for a in range(1, 200):
        if not adm(a):
            continue
        for b in range(a + 1, 1200):
            if gcd(a, b) != 1 or not adm(b):
                continue
            seen += 1
            assert (b - a) % 4 != 2, (a, b)
    assert seen > 1000


def test_the_non_fundamental_close_pair_of_1_423125():
    """A live class whose close pair sits at k = 91, not k = 1.

    Shows a triple's multipliers need not include tau_1 -- the p,q >= 2 gap
    Theorem O.3 does not cover -- and M = 423124 is even, so O.3 is mute here.
    Any extension to even M must still PERMIT these two in a window.
    """
    a, b = 1, 423125
    for m in (10, 17):
        assert isqrt(a * m - 1) ** 2 == a * m - 1
        assert isqrt(b * m - 1) ** 2 == b * m - 1
    assert 17 < 2 * 10                       # both in one dyadic window
    M, D = b - a, a * b
    assert M % 2 == 0 and M % 4 == 0         # outside O.3's hypothesis
    ks = [k for k in range(1, 120)
          if isqrt(M * M + 4 * k * k * D) ** 2 == M * M + 4 * k * k * D]
    assert ks == [1, 91], ks
    tau1_sq = ((sqrt(b) + sqrt(a)) / (sqrt(b) - sqrt(a))) ** 2
    assert tau1_sq == pytest.approx(1.00617, rel=1e-3)
    s = 4 * 91 * sqrt(D) / M
    r91 = ((s + sqrt(s * s + 4)) / 2) ** 2
    assert r91 == pytest.approx(17 / 10, rel=0.03)   # the REALISED ratio
