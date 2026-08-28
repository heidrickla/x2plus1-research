"""Note O -- the multiplier tau, and why no window holds three shared moduli."""

from math import gcd, isqrt, sqrt

import pytest

from x2plus1.polyseq import close_pairs, ratio_classes

X = 1600   # >= 1507, so (1,53) shows both of its close pairs
CLASSES = ratio_classes(X)
PAIRS = list(close_pairs(CLASSES))

# Module-level vacuity guard.  Most tests below iterate PAIRS and would pass
# silently if it were ever empty -- a green result with no work behind it.
assert PAIRS, "no close pairs at this X -- every PAIRS-based test below is vacuous"
assert CLASSES, "no ratio classes at this X"


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
    """Parity lemma: X_k = Y_k mod 2, so V is even.  Explains g = 2.

    The filter can empty independently of PAIRS, so the count is asserted --
    otherwise this passes vacuously if no pair happens to have a, b both odd.
    """
    seen = 0
    for a, b, mi, mj, V, _t in PAIRS:
        if a % 2 and b % 2:
            seen += 1
            assert V % 2 == 0, (a, b, mi, mj, V)
    assert seen > 0, "no pair with a, b both odd -- this test proved nothing"


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


def test_the_non_fundamental_close_pair_is_53_423125():
    """A live class whose close pair sits at k = 12, not k = 1.

    Shows a triple's multipliers need not include tau_1 -- the p,q >= 2 gap
    Theorem O.3 does not cover.  M = 423072 is even AND non-squarefree, so O.3
    is mute, while O.3' reaches it: c = gcd(M, 2X) is 2 and 12, both <= 16, so
    it must PERMIT these two and forbid only a third.

    NOT (1, 423125), which has the same modulus values from different x and is
    one of 12 unexplained close pairs -- its nearest index k = 91 is 2.2% off.
    """
    from math import gcd
    a, b = 53, 423125
    for m in (10, 17):
        assert isqrt(a * m - 1) ** 2 == a * m - 1
        assert isqrt(b * m - 1) ** 2 == b * m - 1
    assert 17 < 2 * 10
    M, D = b - a, a * b
    assert M % 4 == 0                                   # outside O.3
    ks = [k for k in range(1, 4000)
          if isqrt(M * M + 4 * k * k * D) ** 2 == M * M + 4 * k * k * D]
    assert ks == [1, 12], ks
    tau1_sq = ((sqrt(b) + sqrt(a)) / (sqrt(b) - sqrt(a))) ** 2
    assert abs(tau1_sq - 1.7) / 1.7 > 0.3               # tau_1 EXCLUDED
    s = 4 * 12 * sqrt(D) / M
    assert ((s + sqrt(s * s + 4)) / 2) ** 2 == pytest.approx(1.7, rel=1e-3)
    for m in (10, 17):                                  # O.3' applies
        assert gcd(M, 2 * isqrt(a * m - 1)) <= 16


def test_theorem_O3_prime_identity_and_rho_bound():
    """M(rho^2-1) = 4ka(k-rho) with rho = B_k/M, and geometry forces rho < 1.06066."""
    from math import gcd
    from x2plus1.factorization import roots_of_minus_one

    def adm(k):
        return k == 1 or bool(roots_of_minus_one(k))

    def r_of(k, a, b):
        M, D = b - a, a * b
        s = 4 * k * sqrt(D) / M
        return ((s + sqrt(s * s + 4)) / 2) ** 2

    seen = 0
    for a in range(1, 60):
        if not adm(a):
            continue
        for b in range(134 * a, 60000):
            if gcd(a, b) != 1 or not adm(b) or r_of(1, a, b) >= 2:
                continue
            for k in range(2, 40):
                t = a * a + (4 * k * k - 2) * a * b + b * b
                if isqrt(t) ** 2 != t:
                    continue
                if r_of(1, a, b) * r_of(k, a, b) < 2:
                    M = b - a
                    rho = (isqrt(M * M + 4 * k * k * a * b) - 2 * k * a) / M
                    assert M * (rho * rho - 1) == pytest.approx(4 * k * a * (k - rho), rel=1e-9)
                    assert 1 < rho < 1.06066, (a, b, k, rho)
                    seen += 1
                break
    assert seen > 0, "no geometry-passing candidates -- test vacuous"


def test_r_of_is_the_modulus_ratio_not_the_X_ratio():
    """The convention that caused a cross-session collision, pinned.

    The modulus ratio is tau^2, not tau.  On the realised non-fundamental pair
    (53, 423125) the observed ratio is 17/10 = 1.70000, matched by the modulus
    ratio 1.70066 and NOT by tau = 1.30409.  So "both moduli in one window" is
    modulus-ratio < 2, i.e. M > 4 sqrt2 k sqrt(ab).
    """
    a, b, k = 53, 423125, 12
    M, D = b - a, a * b
    s = 4 * k * sqrt(D) / M
    modulus_ratio = ((s + sqrt(s * s + 4)) / 2) ** 2
    assert modulus_ratio == pytest.approx(17 / 10, rel=1e-3)
    assert sqrt(modulus_ratio) == pytest.approx(1.30409, rel=1e-4)
    # the window condition and its algebraic form agree
    assert (modulus_ratio < 2) == (M > 4 * sqrt(2) * k * sqrt(D))


def test_rho_bound_holds_under_the_modulus_ratio_condition():
    """rho^2 < 9/8 with zero violations -- but only under modulus-ratio < 2.

    Under the X-ratio reading (tau_k < 2) the bound is false, which is exactly
    the collision this test exists to prevent recurring.
    """
    from fractions import Fraction
    from math import gcd
    from x2plus1.factorization import roots_of_minus_one

    def adm(k):
        return k == 1 or bool(roots_of_minus_one(k))

    tight = loose_viol = 0
    for a in range(1, 40):
        if not adm(a):
            continue
        for b in range(2 * a, 40000):
            if gcd(a, b) != 1 or not adm(b):
                continue
            M, D = b - a, a * b
            for k in range(2, 120):
                t = M * M + 4 * k * k * D
                U = isqrt(t)
                if U * U != t:
                    continue
                s = 4 * k * sqrt(D) / M
                mr = ((s + sqrt(s * s + 4)) / 2) ** 2
                rho = Fraction(U - 2 * k * a, M)
                if mr < 2:                                   # correct condition
                    tight += 1
                    assert rho * rho < Fraction(9, 8), (a, b, k, float(rho))
                elif mr < 4:                                 # tau_k < 2 only
                    loose_viol += rho * rho >= Fraction(9, 8)
    assert tight > 0, "no multipliers inside a window -- test vacuous"
    assert loose_viol > 0, "the looser reading must actually violate, or the test proves nothing"


def test_delta_identity_and_that_it_vanishes_exactly_at_p_one():
    """delta_p (2M + delta_p + 4pa) = 4 p a M (p-1), with B_p = M + delta_p.

    Exact.  delta_p = 0 iff p = 1, which is why tau_1 is special -- the same
    fact as j = 2 <=> k = 1 and as M_2 = 1, seen as a single vanishing.
    """
    from math import gcd
    seen = one = 0
    for a in range(1, 40):
        for b in range(a + 1, 4000):
            if gcd(a, b) != 1:
                continue
            M, D = b - a, a * b
            for p in range(1, 40):
                t = M * M + 4 * p * p * D
                U = isqrt(t)
                if U * U != t:
                    continue
                d = (U - 2 * p * a) - M
                assert d * (2 * M + d + 4 * p * a) == 4 * p * a * M * (p - 1), (a, b, p)
                assert (d == 0) == (p == 1), (a, b, p, d)
                if p >= 2:
                    assert d < 2 * a * p * (p - 1), (a, b, p, d)   # exact bound
                seen += 1
                one += p == 1
    assert seen > 100 and one > 0


def test_at_most_one_acting_multiplier_lies_inside_a_window():
    """The sharp form of Conjecture O.2, measured with occupancy as the input.

    A third modulus in one window is exactly a SECOND in-window multiplier
    acting on the same xi.  None is ever found; when a second multiplier acts
    alongside an in-window one its ratio is an order of magnitude too large.
    """
    from x2plus1.polyseq import ratio_classes

    C = ratio_classes(700)
    checked = inwindow = 0
    for (a, b), ms in C.items():
        M, D = b - a, a * b
        ks = []
        for k in range(1, 120):
            t = M * M + 4 * k * k * D
            U = isqrt(t)
            if U * U == t:
                ks.append((k, U))
        if not ks:
            continue
        for m in ms:
            X, Y = isqrt(a * m - 1), isqrt(b * m - 1)
            act = [k for k, U in ks
                   if (U * X + 2 * k * a * Y) % M == 0 and (U * Y + 2 * k * b * X) % M == 0]
            if not act:
                continue
            checked += 1
            small = []
            for k in act:
                s = 4 * k * sqrt(D) / M
                if ((s + sqrt(s * s + 4)) / 2) ** 2 < 2:
                    small.append(k)
            assert len(small) <= 1, (a, b, m, small)
            inwindow += len(small) == 1
    assert checked > 0, "no acting multipliers -- test vacuous"
    assert inwindow > 0, "no in-window multiplier at all -- test proves nothing"


def test_second_moment_decomposition_is_exact():
    """Q2 = DIAG + OFF, the identity behind Note M's Cauchy-Schwarz reduction.

    DIAG counts squarefree incidences; OFF is the signed Gram sum
    sum_{x!=y} mu mu G_M(x,y).  Checked by computing both sides independently.
    """
    import numpy as np
    from x2plus1.factorization import roots_of_minus_one
    from x2plus1.mobius import mobius_x2plus1

    X, M = 4000, 60
    mu = mobius_x2plus1(X)
    Q2 = 0.0
    diag = 0
    off = 0.0
    for m in range(M, 2 * M):
        rs = roots_of_minus_one(m)
        starts = {r % m for r in rs} | {(m - r) % m for r in rs}
        starts.discard(0)
        if not starts:
            continue
        cols = [np.arange(r, X + 1, m, dtype=np.int64) for r in sorted(starts)]
        xs = np.unique(np.concatenate(cols))
        xs = xs[xs >= 1]
        v = mu[xs]
        Q2 += float(v.sum()) ** 2
        diag += int((v != 0).sum())
        s = float(v.sum())
        off += s * s - float((v * v).sum())          # the x != y part, directly
    assert diag > 0, "no incidences -- test vacuous"
    assert Q2 == pytest.approx(diag + off, rel=1e-9)
    assert abs(off) < diag, (off, diag)              # |OFF| << DIAG, the measured input


def test_the_tightest_near_counterexample_to_O2():
    """(2, 8321): everything a triple needs except occupancy.

    Live close pair at m = 8065, 8581 explained exactly by tau_1; a second
    in-window multiplier k = 9 exists; route 8 showed the residues permit both.
    The third modulus would land at ~13996 and is simply not there.
    """
    a, b = 2, 8321
    M, D = b - a, a * b
    for m in (8065, 8581):
        assert isqrt(a * m - 1) ** 2 == a * m - 1
        assert isqrt(b * m - 1) ** 2 == b * m - 1
    assert 8581 < 2 * 8065                                   # one window
    ratios = {}
    for k in (1, 9):
        t_ = M * M + 4 * k * k * D
        U = isqrt(t_)
        assert U * U == t_, k                                # both multipliers exist
        sk = 4 * k * sqrt(D) / M
        ratios[k] = ((sk + sqrt(sk * sk + 4)) / 2) ** 2
    assert ratios[1] == pytest.approx(8581 / 8065, rel=1e-4)  # tau_1 explains the pair
    assert ratios[9] < 2                                      # tau_9 would fit too
    third = round(8065 * ratios[9])
    for c in range(third - 4, third + 5):                     # and it is not there
        assert not (isqrt(a * c - 1) ** 2 == a * c - 1
                    and isqrt(b * c - 1) ** 2 == b * c - 1), c


def test_prop_O1_needs_its_window_hypothesis():
    """(1,5) at m = 2 is a counterexample to O.1 stated without the window.

    Coprime, m_i >= 2, and tau_1^2 = tau_3 DOES act -- the acting set is the
    whole tower 1, 3, 8, 21, 55, 144.  It escapes because a g^2 = 4 = M, failing
    the strict a g^2 < M, and it fails that because r_1 = 6.854 is nowhere near
    a window.  This test exists so the hypothesis cannot be dropped again.
    """
    from math import gcd
    a, b = 1, 5
    M, D = b - a, a * b
    U = isqrt(M * M + 4 * D)
    assert U * U == M * M + 4 * D and U == 6
    g = gcd(U, 2)
    assert a * g * g == M                      # equality: the strict bound fails
    s = 4 * sqrt(D) / M
    r1 = ((s + sqrt(s * s + 4)) / 2) ** 2
    assert r1 > 2                              # and tau_1 xi is outside the window
    # tau_3 = tau_1^2 really does act on the solution at m = 2
    m = 2
    X_, Y_ = isqrt(a * m - 1), isqrt(b * m - 1)
    t3 = M * M + 4 * 9 * D
    U3 = isqrt(t3)
    assert U3 * U3 == t3
    assert (U3 * X_ + 2 * 3 * a * Y_) % M == 0
    assert (U3 * Y_ + 2 * 3 * b * X_) % M == 0


def test_rational_gram_reaches_three_outside_a_window():
    """G(17,26) = 3 -- the rational Gram entry is not bounded by 2 in general.

    Shared moduli 1, 85, 2966965.  This does NOT contradict the window bound:
    those span seven orders, so no dyadic window holds two of them.  "Max 2" is
    a statement about windows, not about G, and a sweep reporting max 2 over
    cofactor bands has simply not looked at small enough N.
    """
    n1, n2 = 17, 26
    shared = [1, 85, 2966965]
    for m in shared:
        for n in (n1, n2):
            v = m * n
            assert isqrt(v - 1) ** 2 + 1 == v, (m, n, v)
    assert len(shared) == 3
    # ... but one of them is the UNIT modulus, which no Type II hypothesis admits
    assert 1 in shared
    assert len([m for m in shared if m > 1]) == 2, "excluding units the max is 2"
    # and no dyadic window holds two of them
    for i in range(len(shared) - 1):
        assert shared[i + 1] >= 2 * shared[i], shared


def test_O3_geometry_reduction_is_an_algebraic_identity():
    """Theorem O.3's key step, verified symbolically rather than numerically.

    Substituting M = 8kaw/e, b = a+M, k = (j+w)/2 into the geometry M^2 - 32k^2ab
    and clearing by e^2/a^2 gives exactly -8(j+w)^2 (e^2 + 4ejw + 2w^2(2e-1)).
    The ratio to the displayed quantity is 8(j+w)^2, positive -- so "geometry
    holds" and "that quantity is negative" are the SAME statement, as algebra.
    """
    from sympy import expand, factor, simplify, symbols

    k, a, j, w, e = symbols("k a j w e", positive=True)
    M = 8 * k * a * w / e
    b = a + M
    geom = expand(M**2 - 32 * k**2 * a * b).subs(k, (j + w) / 2)
    geom = simplify(expand(geom * e**2 / a**2))
    target = -(e**2 + 4 * e * j * w + 2 * w**2 * (2 * e - 1))
    assert simplify(factor(geom / target) - 8 * (j + w) ** 2) == 0

    # and the quantity is strictly positive on the admissible integer region
    for jj in range(3, 40):
        ee = jj * jj - 4
        for ww in range(1, 40):
            assert ee**2 + 4 * ee * jj * ww + 2 * ww**2 * (2 * ee - 1) > 0


def _kmin_surviving(c):
    """Smallest k >= 2 that Theorem O.3'' does NOT exclude at this c, or None."""
    for k in range(2, 200):
        A = 4 * k + sqrt(16 * k * k + 2)
        if A * (2 * c + 1) < c * (k * c - c - 1):
            return k
    return None


def _in_window_multipliers(amax=8, bmax=30000):
    """(a, b, k, U_k) for every multiplier with modulus ratio < 2.

    Enumerated over a coprime box rather than over PAIRS: the identity and the
    geometry are algebra in (a, b, k) and do not need the class to be realised.
    PAIRS at this X carries no k >= 2 in-window multiplier at all, so the guards
    in the tests below would (correctly) fire on it.
    """
    for a in range(1, amax + 1):
        for b in range(a + 1, bmax + 1):
            if gcd(a, b) != 1:
                continue
            M, D = b - a, a * b
            kw = int(M / (4 * sqrt(2) * sqrt(D)))
            if kw < 2:
                continue
            for k in range(1, kw + 1):
                t = M * M + 4 * k * k * D
                U = isqrt(t)
                if U * U == t:
                    yield a, b, k, U


def test_rho_is_exactly_one_at_k_one_and_strictly_above_it_after():
    """The boundary case that hid the sharpening: k = 1 has rho = 1 identically.

    U_1 = a+b, so B_1 = b-a = M and rho = 1 -- the identity reads M*0 = 4a*0 and
    Lambda = 0/0 is undefined.  For k >= 2, rho = 1 would force M*0 = 4ka(k-1),
    nonzero, so rho > 1 is strict there.  Theorem O.3'' rests on that.
    """
    from fractions import Fraction

    seen1 = seen2 = 0
    for a, b, k, U in _in_window_multipliers():
        rho = Fraction(U - 2 * k * a, b - a)
        if k == 1:
            seen1 += 1
            assert rho == 1 and U == a + b, (a, b, k, rho)
        else:
            seen2 += 1
            assert rho > 1, (a, b, k, rho)
    assert seen1 and seen2, (seen1, seen2)


def test_sharpened_rho_bound_holds_and_is_nearly_saturated():
    """rho^2 < 1 + (k-1)/A_k, the bound O.3' discards by using rho > 0."""
    from fractions import Fraction

    n, tightest = 0, 0.0
    for a, b, k, U in _in_window_multipliers():
        if k < 2:
            continue
        rho = Fraction(U - 2 * k * a, b - a)
        bound = sqrt(1 + (k - 1) / (4 * k + sqrt(16 * k * k + 2)))
        assert float(rho) < bound, (a, b, k, float(rho), bound)
        assert bound < 1.060661          # strictly better than O.3''s constant
        n += 1
        tightest = max(tightest, float(rho) / bound)
    assert n >= 100, f"only {n} k>=2 in-window multipliers -- widen the box"
    assert tightest > 0.99, tightest     # the bound is essentially saturated


def test_O3pp_reduces_to_t_equals_one():
    """A_k t(2c+t) < c(kc-c-t): LHS increases in t, RHS decreases, so t=1 binds."""
    for k in range(2, 12):
        A = 4 * k + sqrt(16 * k * k + 2)
        for c in range(2, 80):
            if A * (2 * c + 1) >= c * (k * c - c - 1):     # t = 1 excluded
                for t in range(2, 40):                     # then every t is
                    assert A * t * (2 * c + t) >= c * (k * c - c - t), (k, c, t)


def test_O3pp_recovers_O3prime_and_doubles_it_at_k_two():
    """c <= 16 excluded for every k (O.3'); k = 2 excluded for c <= 33."""
    for c in range(1, 17):
        assert _kmin_surviving(c) is None, c
    assert _kmin_surviving(17) == 35
    assert _kmin_surviving(18) == 13
    A2 = 4 * 2 + sqrt(16 * 4 + 2)
    for c in range(2, 34):
        assert A2 * (2 * c + 1) >= c * (2 * c - c - 1), c   # k = 2 excluded
    assert _kmin_surviving(34) == 2                          # and 34 is sharp


def test_realised_c_values_are_far_below_the_O3pp_threshold():
    """Recorded from the X = 4000 slice sweep (experiments/exp18_ck_region.py).

    Measured on configurations that DO occur, so this is not
    `triples-cannot-be-settled-by-measurement`.  Every acting in-window
    multiplier with k >= 2 has c = gcd(M,2X) in {2,4}, against a threshold of 17.
    """
    for c, k in [(2, 12), (2, 33), (2, 91), (4, 4)]:
        assert c <= 16
        assert _kmin_surviving(c) is None, (c, k)


def test_region_form_is_sharper_than_the_rho_bound_route():
    """The two routes differ by exactly 1 at k = 2,3,4 and agree from k = 5.

    Reading "c*rho in Z needs 1/(rho-1)" off rho < sqrt(1+(k-1)/A_k) spends
    rho > 1 on the -rho term; the region inequality substitutes rho >= (c+1)/c
    into BOTH places rho appears, so it is strictly sharper.  Not a discrepancy
    -- a corollary and its parent.
    """
    expected = {2: (33, 34), 3: (25, 26), 4: (22, 23), 5: (21, 21), 10: (19, 19)}
    for k, (want_rho, want_region) in expected.items():
        A = 4 * k + sqrt(16 * k * k + 2)
        bound = sqrt(1 + (k - 1) / A)
        c_rho = next(c for c in range(1, 500) if 1 + 1 / c < bound)
        c_region = next(
            c for c in range(1, 500) if A * (2 * c + 1) < c * (k * c - c - 1)
        )
        assert (c_rho, c_region) == (want_rho, want_region), (k, c_rho, c_region)
        assert c_region >= c_rho          # the region form is never weaker
    assert _kmin_surviving(17) == 35       # and both stabilise at 17


FOURTH = 2 ** 0.25
T_PAIR = (1 + sqrt(2)) ** 2
T_TRIPLE = (FOURTH + 1) / (FOURTH - 1)

TRIPLES = [(a, b, sorted(ms)) for (a, b), ms in CLASSES.items() if len(ms) >= 3]
assert TRIPLES, "no class with three shared moduli -- the O.4 tests would be vacuous"


def test_O4_thresholds_have_the_stated_closed_forms():
    """t_triple = (1+sqrt2)(1+sqrt2+2^{5/4}) = t_pair + 2^{5/4}(1+sqrt2)."""
    assert abs(T_TRIPLE - (1 + sqrt(2)) * (1 + sqrt(2) + 2 ** 1.25)) < 1e-12
    assert abs(T_TRIPLE - (T_PAIR + 2 ** 1.25 * (1 + sqrt(2)))) < 1e-12
    assert abs(T_PAIR**2 - 33.970562748) < 1e-8        # the pair threshold
    assert abs(T_TRIPLE**2 - 133.8747813272) < 1e-8   # the triple threshold
    # M > 4(2^{1/4} + 2^{3/4}) sqrt(ab), and that beats the determinant route
    m_over_sqrtD = T_TRIPLE - 1 / T_TRIPLE
    assert abs(m_over_sqrtD - 4 * (FOURTH + FOURTH**3)) < 1e-9
    assert m_over_sqrtD > 8 * sqrt(2)                  # 11.4840 vs 11.3137


def test_O4_step_one_the_automorph_map_holds_on_every_pair():
    """X_j = (U X_i + V a Y_i)/M for every consecutive pair, across orbits too."""
    n = 0
    for a, b, ms in [(a, b, sorted(ms)) for (a, b), ms in CLASSES.items()
                     if len(ms) >= 2]:
        D, M = a * b, b - a
        xs = [isqrt(a * m - 1) for m in ms]
        ys = [isqrt(b * m - 1) for m in ms]
        for i in range(len(ms) - 1):
            u, w, Yi, Yj = xs[i], xs[i + 1], ys[i], ys[i + 1]
            U = b * u * w - a * Yi * Yj
            V = u * Yj - w * Yi
            assert U * U - D * V * V == M * M, (a, b, ms[i])
            assert any(
                su * U * u + sv * V * a * Yi == M * w
                and su * U * Yi + sv * V * b * u == M * Yj
                for su in (1, -1) for sv in (1, -1)
            ), (a, b, ms[i], ms[i + 1], U, V)
            n += 1
    assert n > 100, n


def test_O4_step_two_X_grows_by_at_least_tau():
    """a Y_i > X_i sqrt(D) gives X_j > tau_V X_i -- exact, and the a cancels."""
    n = 0
    for a, b, ms in [(a, b, sorted(ms)) for (a, b), ms in CLASSES.items()
                     if len(ms) >= 2]:
        D, M = a * b, b - a
        xs = [isqrt(a * m - 1) for m in ms]
        ys = [isqrt(b * m - 1) for m in ms]
        for i in range(len(ms) - 1):
            if xs[i] < 1:
                continue
            assert a * ys[i] * a * ys[i] > xs[i] * xs[i] * D   # the exact step
            V = abs(xs[i] * ys[i + 1] - xs[i + 1] * ys[i])
            tau = (sqrt(M * M + D * V * V) + V * sqrt(D)) / M
            assert xs[i + 1] > tau * xs[i], (a, b, ms[i])
            n += 1
    assert n > 100, n


def test_O4_gap_bound_holds_exactly_and_the_clean_form_does_not():
    """The +1 in m = (X^2+1)/a is load-bearing: dropping it makes it false."""
    clean_failures = 0
    n = 0
    for a, b, ms in TRIPLES:
        tau4 = ((sqrt(b) + sqrt(a)) / (sqrt(b) - sqrt(a))) ** 4
        xs = [isqrt(a * m - 1) for m in ms]
        for i in range(len(ms) - 2):
            if xs[i] < 1:
                continue
            n += 1
            obs = ms[i + 2] / ms[i]
            exact = (tau4 * xs[i] ** 2 + 1) / (xs[i] ** 2 + 1)
            assert obs > exact, (a, b, ms[i], ms[i + 2], obs, exact)
            clean_failures += obs < tau4
    assert n > 20, n
    assert clean_failures > 0, "the clean form did not fail -- widen X"


def test_O4_window_condition_is_tau_min_fourth_below_two_plus_one_over_X_squared():
    """Rearrangement: m3/m1 < 2 and the gap bound force tau_1^4 < 2 + 1/X_1^2."""
    for xi, want in [(1, 53.694), (2, 97.990), (3, 115.295), (10, 131.978)]:
        thr = 2 + 1 / xi**2
        t = (thr**0.25 + 1) / (thr**0.25 - 1)
        assert abs(t * t - want) < 1e-3, (xi, t * t)
        # and the exact rearrangement it comes from
        assert (thr * xi**2) == pytest.approx(2 * xi**2 + 1)
    # the X_1 -> infinity limit is the closed form
    assert abs((2 ** 0.25 + 1) / (2 ** 0.25 - 1) - T_TRIPLE) < 1e-12


def test_O4_is_not_binding_on_realised_classes():
    """Classes clearing b/a > 133.87 with three moduli stay far from a window."""
    adm = [(a, b, ms) for a, b, ms in TRIPLES if b > T_TRIPLE**2 * a]
    assert adm, "no class clears the threshold -- the check would be vacuous"
    best = min(min(ms[i + 2] / ms[i] for i in range(len(ms) - 2))
               for _a, _b, ms in adm)
    assert best > 2, best        # none is anywhere near a window
    assert best > 7              # in fact not within a factor of 7
