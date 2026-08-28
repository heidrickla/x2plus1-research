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


def test_O5_tau_p_squared_in_T_forces_M_divides_8p_squared():
    """U' = M + 8p^2 D/M, and D == a^2 mod M with gcd(a,M) = 1."""
    n = 0
    for a in range(1, 40):
        for b in range(a + 1, 2000):
            if gcd(a, b) != 1:
                continue
            M, D = b - a, a * b
            assert D % M == (a * a) % M          # D = a(a+M) == a^2 mod M
            assert gcd(a, M) == 1                 # because the class is reduced
            for p in range(1, 20):
                t = M * M + 4 * p * p * D
                U = isqrt(t)
                if U * U != t:
                    continue
                if (8 * p * p * D) % M == 0 and (4 * p * U) % M == 0:
                    assert (8 * p * p) % M == 0, (a, b, p)   # M | 8p^2
                    n += 1
    assert n > 100, n


def test_O5_at_p_one_it_is_an_equivalence_with_M_divides_8():
    """tau_1^2 in T  <=>  M | 8, exactly."""
    n = 0
    for a in range(1, 60):
        for b in range(a + 1, 900):
            if gcd(a, b) != 1:
                continue
            M = b - a
            in_T = (4 * (a + b)) % M == 0 and ((a + b) ** 2 + 4 * a * b) % M == 0
            assert in_T == (8 % M == 0), (a, b, M)
            n += 1
    assert n > 10000, n


def test_O5_the_window_contradicts_M_divides_8p_squared():
    """tau_p^4 < 3 forces 8p^2 < 0.1548 M^2/D, against M <= 8p^2 and M < D."""
    c = 3 ** 0.25                      # O.4 with X_1 >= 1 gives tau_p^4 < 3
    w = (c * c - 1) / (2 * c)          # tau_V < c  =>  V s < w
    assert abs(w - 0.278119) < 1e-6
    C = 8 * (w / 2) ** 2
    assert abs(C - 0.154701) < 1e-6
    assert C < 1                        # so D < C*M < M is the contradiction
    # M < D always, for a >= 1 and b > a
    for a in range(1, 60):
        for b in range(a + 1, 300):
            assert b - a < a * b, (a, b)


def test_O5_realised_classes_where_tau_1_squared_acts_all_have_M_dividing_8():
    """Recorded from the X = 3000 sweep in experiments/exp19_composition_bound.py."""
    for a, b, M in [(1, 5, 4), (1, 2, 1)]:
        assert b - a == M and 8 % M == 0
        assert (4 * (a + b)) % M == 0      # tau_1^2 really is in T there


def _oriented(a, b, u, Yi, w, Yj):
    """(U, V) signed so that X_j = (U X_i + V a Y_i)/M, or None."""
    M = b - a
    U0 = b * u * w - a * Yi * Yj
    V0 = u * Yj - w * Yi
    for su in (1, -1):
        for sv in (1, -1):
            if su * U0 * u + sv * V0 * a * Yi == M * w:
                return su * U0, sv * V0
    return None


def _prime_steps():
    """Oriented consecutive pairs of classes whose M is an odd prime."""
    from sympy import isprime
    for (a, b), ms in CLASSES.items():
        M = b - a
        if M < 3 or M % 2 == 0 or not isprime(M):
            continue
        ms = sorted(ms)
        xs = [isqrt(a * m - 1) for m in ms]
        ys = [isqrt(b * m - 1) for m in ms]
        for i in range(len(ms) - 1):
            got = _oriented(a, b, xs[i], ys[i], xs[i + 1], ys[i + 1])
            if got:
                yield a, b, xs[i], ys[i], xs[i + 1], ys[i + 1], got


def test_O6_exact_identities_and_that_the_naive_form_is_wrong():
    """M S' = A S + V M X, not S' = A S / M -- the latter fails on every pair."""
    n = naive_fail = 0
    for a, b, u, Yi, w, Yj, (U, V) in _prime_steps():
        M = b - a
        A, B = U + V * a, U - V * a
        S1, T1, S2, T2 = u + Yi, u - Yi, w + Yj, w - Yj
        assert M * S2 == A * S1 + V * M * u, (a, b)
        assert M * T2 == B * T1 - V * M * u, (a, b)
        assert (A * S1) % M == 0 and (B * T1) % M == 0     # necessary conditions
        naive_fail += M * S2 != A * S1
        n += 1
    assert n > 50, n
    assert naive_fail == n, (naive_fail, n)   # the natural guess is always wrong


def test_O6_dichotomy_and_that_the_subcase_alternates():
    """Exactly one of M|S, M|T -- and it flips at every step."""
    alt = same = n = 0
    for a, b, u, Yi, w, Yj, _uv in _prime_steps():
        M = b - a
        c1 = ((u + Yi) % M == 0, (u - Yi) % M == 0)
        c2 = ((w + Yj) % M == 0, (w - Yj) % M == 0)
        assert sum(c1) == 1 and sum(c2) == 1, (a, b, c1, c2)   # exactly one
        alt += c1 != c2
        same += c1 == c2
        n += 1
    assert n > 50, n
    assert same == 0, same
    assert alt == n


def test_O6_sign_is_forced_and_beta_is_congruent_to_p():
    """M|S => M|B with B/M == p; M|T => M|A with A/M == -p."""
    n = 0
    for a, b, u, Yi, w, Yj, (U, V) in _prime_steps():
        M = b - a
        if V % 2:
            continue
        p = V // 2
        A, B = U + V * a, U - V * a
        if (u + Yi) % M == 0:
            assert B % M == 0, (a, b)
            if p % M:
                assert ((B // M) - p) % M == 0, (a, b, p)
        else:
            assert A % M == 0, (a, b)
            if p % M:
                assert ((A // M) + p) % M == 0, (a, b, p)
        n += 1
    assert n > 50, n


def test_O6_opposite_signs_make_the_composite_conditions_vacuous():
    """The alternation forces eps_p = -eps_q, and then both conditions hold free.

    Same-sign pairs WOULD be constrained -- this checks that too, so the
    conclusion is 'the alternation removes the content', not 'there was none'.
    """
    from sympy import isprime

    opp = bad_opp = same = bad_same = 0
    for a in range(1, 20):
        for b in range(a + 1, 1500):
            if gcd(a, b) != 1:
                continue
            M, D = b - a, a * b
            if M < 3 or M % 2 == 0 or not isprime(M):
                continue
            plus, minus = [], []
            for k in range(1, 40):
                t = M * M + 4 * k * k * D
                U = isqrt(t)
                if U * U != t:
                    continue
                if (U - 2 * k * a) % M == 0:
                    plus.append((k, U))
                if (U + 2 * k * a) % M == 0:
                    minus.append((k, U))
            for p, Up in plus:
                for q, Uq in minus:
                    opp += 1
                    bad_opp += (2 * (q * Up + p * Uq)) % M != 0 or (
                        Up * Uq + 4 * p * q * D
                    ) % M != 0
                for q, Uq in plus:
                    if p == q:
                        continue
                    same += 1
                    bad_same += (2 * (q * Up + p * Uq)) % M != 0
    assert opp > 100, opp
    assert bad_opp == 0, bad_opp          # automatic, so the route is dead
    assert same > 50 and bad_same > 0     # but the conditions do have content


def test_O7_the_V_identity_carries_a_factor_of_a():
    """a |V| (X_j Y_i + X_i Y_j) = M (X_j^2 - X_i^2), over ALL pairs.

    Dropping the a is the natural slip and makes the bound come out with a
    spurious factor; with it, the M/(2 sqrt D) form is exact.
    """
    n = 0
    for (a, b), ms in CLASSES.items():
        M = b - a
        ms = sorted(ms)
        xs = [isqrt(a * m - 1) for m in ms]
        ys = [isqrt(b * m - 1) for m in ms]
        for i in range(len(ms)):
            for j in range(i + 1, len(ms)):
                V = abs(xs[i] * ys[j] - xs[j] * ys[i])
                assert a * V * (xs[j] * ys[i] + xs[i] * ys[j]) == M * (
                    xs[j] ** 2 - xs[i] ** 2
                ), (a, b, ms[i], ms[j])
                n += 1
    assert n > 200, n


def test_O7_in_window_forces_M_does_not_divide_V():
    """|V| < 0.57735 M/sqrt(D) <= 0.40825 M < M on every in-window pair."""
    bound = (sqrt(3) - 1 / sqrt(3)) / 2
    assert abs(bound - 0.5773502692) < 1e-9
    n, worst = 0, 0.0
    for (a, b), ms in CLASSES.items():
        M, D = b - a, a * b
        ms = sorted(ms)
        xs = [isqrt(a * m - 1) for m in ms]
        ys = [isqrt(b * m - 1) for m in ms]
        for i in range(len(ms)):
            if xs[i] < 1:
                continue
            for j in range(i + 1, len(ms)):
                if ms[j] >= 2 * ms[i]:
                    continue
                V = abs(xs[i] * ys[j] - xs[j] * ys[i])
                assert 0 < V < bound * M / sqrt(D), (a, b, ms[i], ms[j], V)
                assert V % M != 0, (a, b, ms[i], ms[j], V)
                worst = max(worst, V * sqrt(D) / M)
                n += 1
    assert n > 100, n
    assert worst < bound          # and the bound is not attained


def test_O7_dichotomy_and_flip_hold_on_every_in_window_prime_pair():
    """The two ingredients of O.7, on the configurations that do occur."""
    from sympy import isprime

    n = 0
    for (a, b), ms in CLASSES.items():
        M = b - a
        if M < 3 or M % 2 == 0 or not isprime(M):
            continue
        ms = sorted(ms)
        xs = [isqrt(a * m - 1) for m in ms]
        ys = [isqrt(b * m - 1) for m in ms]
        for i in range(len(ms)):
            for j in range(i + 1, len(ms)):
                if ms[j] >= 2 * ms[i]:
                    continue
                c1 = ((xs[i] + ys[i]) % M == 0, (xs[i] - ys[i]) % M == 0)
                c2 = ((xs[j] + ys[j]) % M == 0, (xs[j] - ys[j]) % M == 0)
                assert sum(c1) == 1 and sum(c2) == 1, (a, b, c1, c2)
                assert c1 != c2, (a, b, ms[i], ms[j])
                n += 1
    assert n > 20, n


def test_O7_realised_prime_triples_escape_exactly_by_M_dividing_V():
    """The proof's only hypothesis is M nmid V, and every realised triple has M | V.

    Recorded from experiments/exp22_sign_alternation.py at X = 6000. These are
    real triples, far outside any window (ratios of 1e4 and up), which is how
    |V| gets past 0.57735 M/sqrt(D).
    """
    for a, b, m1, m3, V in [(2, 13, 5, 48985, 110), (2, 5, 13, 18241, 18),
                            (2, 25, 13, 499001, 322)]:
        M = b - a
        assert V % M == 0, (a, b, V, M)
        assert m3 > 2 * m1                        # nowhere near one window
        x1, y1 = isqrt(a * m1 - 1), isqrt(b * m1 - 1)
        x3, y3 = isqrt(a * m3 - 1), isqrt(b * m3 - 1)
        assert abs(x1 * y3 - x3 * y1) == V, (a, b)


def test_O8_the_ST_identity():
    """S T = -M m, from a(Y^2 - X^2) = M(X^2+1) = M a m."""
    n = 0
    for (a, b), ms in CLASSES.items():
        M = b - a
        for m in ms:
            x, y = isqrt(a * m - 1), isqrt(b * m - 1)
            assert (x + y) * (x - y) == -M * m, (a, b, m)
            n += 1
    assert n > 1000, n


def test_O8_factorisation_lemma_and_the_step_it_turns_on():
    """gcd(M,S) gcd(M,T) = M for M odd; and p|S, p|T => p|X => p nmid m."""
    from sympy import factorint

    n = both = 0
    for (a, b), ms in CLASSES.items():
        M = b - a
        if M < 3 or M % 2 == 0:
            continue
        primes = list(factorint(M))
        for m in ms:
            x, y = isqrt(a * m - 1), isqrt(b * m - 1)
            S, T = x + y, x - y
            assert gcd(M, S) * gcd(M, T) == M, (a, b, m)
            for p in primes:
                if S % p == 0 and T % p == 0:
                    assert x % p == 0 and m % p != 0, (a, b, m, p)
                    both += 1
            n += 1
    assert n > 1000 and both > 0, (n, both)


def test_O8_local_flip_for_squarefree_M_under_coprimality():
    """gcd(V,M)=1 makes the subcase flip at EVERY p | M, hence the pair swaps."""
    from sympy import factorint

    n = 0
    for (a, b), ms in CLASSES.items():
        M = b - a
        if M < 3 or M % 2 == 0:
            continue
        fac = factorint(M)
        if any(e > 1 for e in fac.values()):
            continue
        ms = sorted(ms)
        xs = [isqrt(a * m - 1) for m in ms]
        ys = [isqrt(b * m - 1) for m in ms]
        for i in range(len(ms)):
            for j in range(i + 1, len(ms)):
                V = abs(xs[i] * ys[j] - xs[j] * ys[i])
                if gcd(V, M) != 1:
                    continue
                for p in fac:
                    assert ((xs[i] + ys[i]) % p == 0) != (
                        (xs[j] + ys[j]) % p == 0
                    ), (a, b, ms[i], ms[j], p)
                # and therefore the whole pair swaps
                assert (gcd(M, xs[i] + ys[i]), gcd(M, xs[i] - ys[i])) == (
                    gcd(M, xs[j] - ys[j]), gcd(M, xs[j] + ys[j])
                ), (a, b, ms[i], ms[j])
                n += 1
    assert n > 100, n


def test_O8_coprimality_is_equivalent_to_gcd_U_V_being_one():
    """gcd(V,M) = 1 <=> g = gcd(U,V) = 1, so it is Prop O.1's quantity."""
    n = 0
    for (a, b), ms in CLASSES.items():
        M, D = b - a, a * b
        ms = sorted(ms)
        xs = [isqrt(a * m - 1) for m in ms]
        ys = [isqrt(b * m - 1) for m in ms]
        for i in range(len(ms)):
            for j in range(i + 1, len(ms)):
                U = abs(b * xs[i] * xs[j] - a * ys[i] * ys[j])
                V = abs(xs[i] * ys[j] - xs[j] * ys[i])
                assert U * U - D * V * V == M * M
                g = gcd(U, V)
                assert M % g == 0                      # g | M, the known step
                assert (gcd(V, M) == 1) == (g == 1), (a, b, ms[i], ms[j])
                n += 1
    assert n > 200, n


def test_O8_in_window_pairs_are_observed_coprime_but_it_is_not_proved():
    """Every in-window pair has gcd(V,M)=1 here -- recorded as measured.

    The window bound |V| < 0.57735 M/sqrt(D) bounds V without making it coprime
    to M, and all that is known in-window about g = gcd(U,V) is a g^2 < M, which
    permits g > 1.  So this is the hypothesis of O.8 and not a consequence.

    M ODD IS REQUIRED and is not a convenience: if a and b are both odd then M is
    even and so is V, so gcd(V,M) >= 2 automatically.  Dropping the filter fails
    this test, which is how the condition was pinned down.
    """
    n = 0
    for (a, b), ms in CLASSES.items():
        M = b - a
        if M % 2 == 0:
            continue
        ms = sorted(ms)
        xs = [isqrt(a * m - 1) for m in ms]
        ys = [isqrt(b * m - 1) for m in ms]
        for i in range(len(ms)):
            if xs[i] < 1:
                continue
            for j in range(i + 1, len(ms)):
                if ms[j] >= 2 * ms[i]:
                    continue
                V = abs(xs[i] * ys[j] - xs[j] * ys[i])
                assert gcd(V, M) == 1, (a, b, ms[i], ms[j], V, M)
                n += 1
    assert n > 50, n


def test_the_plucker_constant_equals_O4s_and_the_route_gives_less():
    """4/(2^{1/4} - 2^{-1/4}) = 4(2^{1/4} + 2^{3/4}), but Plucker yields 8 sqrt2.

    The note recorded 11.484 as coming from the Plucker-parity argument.  The
    value is right and the attribution was not: |V| < (M/2 sqrt D)(R - 1/R) with
    R < sqrt2 and |V| >= 4 gives 8 sqrt2 = 11.3137, and only 6.93 at X_1 = 1.
    11.484 comes from O.4, where 2^{1/4} enters via the composite tau_1^2 < sqrt2.
    """
    x = 2 ** 0.25
    assert abs(4 / (x - 1 / x) - 4 * (x + x**3)) < 1e-12
    assert abs(4 * (x + x**3) - 11.4839997820) < 1e-9
    # the Plucker route, done exactly
    for xi, want in [(1, 6.9282), (2, 9.6000), (10, 11.2297)]:
        R = sqrt(2 + 1 / xi**2)
        assert abs(4 / ((R - 1 / R) / 2) - want) < 1e-3, (xi,)
    R = sqrt(2)
    assert abs(4 / ((R - 1 / R) / 2) - 8 * sqrt(2)) < 1e-9      # 11.3137
    assert 8 * sqrt(2) < 4 * (x + x**3)                          # O.4 is stronger


def test_O9_the_VW_identity_has_no_cofactor():
    """V W = M (m_i - m_j), with W = X_j Y_i + X_i Y_j.  The a cancels."""
    n = 0
    for (a, b), ms in CLASSES.items():
        M = b - a
        ms = sorted(ms)
        xs = [isqrt(a * m - 1) for m in ms]
        ys = [isqrt(b * m - 1) for m in ms]
        for i in range(len(ms)):
            for j in range(i + 1, len(ms)):
                V = xs[i] * ys[j] - xs[j] * ys[i]
                W = xs[j] * ys[i] + xs[i] * ys[j]
                assert V * W == M * (ms[i] - ms[j]), (a, b, ms[i], ms[j])
                n += 1
    assert n > 200, n


def test_O9_the_sign_is_well_defined_and_p_divides_V_iff_signs_agree():
    """sigma_i = +-1 with Y_i == sigma_i X_i mod p; p | V_ij <=> sigma_i = sigma_j."""
    from sympy import factorint

    n_sig = n_eq = 0
    for (a, b), ms in CLASSES.items():
        M = b - a
        if M < 3 or M % 2 == 0:
            continue
        fac = factorint(M)
        if any(e > 1 for e in fac.values()):
            continue
        ms = sorted(ms)
        xs = [isqrt(a * m - 1) for m in ms]
        ys = [isqrt(b * m - 1) for m in ms]
        sig = []
        for i in range(len(ms)):
            d = {}
            for p in fac:
                assert xs[i] % p != 0, (a, b, ms[i], p)      # p nmid X
                assert (ys[i] - xs[i]) % p == 0 or (ys[i] + xs[i]) % p == 0
                d[p] = 1 if (ys[i] - xs[i]) % p == 0 else -1
                n_sig += 1
            sig.append(d)
        for i in range(len(ms)):
            for j in range(i + 1, len(ms)):
                V = xs[i] * ys[j] - xs[j] * ys[i]
                for p in fac:
                    assert (V % p == 0) == (sig[i][p] == sig[j][p]), (
                        a, b, ms[i], ms[j], p)
                    n_eq += 1
    assert n_sig > 500 and n_eq > 100, (n_sig, n_eq)


def test_O9_pigeonhole_forces_M_to_divide_the_product_of_the_three_Vs():
    """Three signs in {+-1} collide, so every p | M divides one of the V's."""
    from sympy import factorint

    n = 0
    for (a, b), ms in CLASSES.items():
        M = b - a
        if M < 3 or M % 2 == 0:
            continue
        if any(e > 1 for e in factorint(M).values()):
            continue
        ms = sorted(ms)
        xs = [isqrt(a * m - 1) for m in ms]
        ys = [isqrt(b * m - 1) for m in ms]
        for i in range(len(ms)):
            for j in range(i + 1, len(ms)):
                for k in range(j + 1, len(ms)):
                    v12 = xs[i] * ys[j] - xs[j] * ys[i]
                    v23 = xs[j] * ys[k] - xs[k] * ys[j]
                    v13 = xs[i] * ys[k] - xs[k] * ys[i]
                    assert abs(v12 * v23 * v13) % M == 0, (a, b, ms[i], ms[j], ms[k])
                    n += 1
    assert n > 5, n


def test_O9_the_window_bound_and_the_resulting_inequality():
    """|V| < M/sqrt(3D) in-window; hence 3ab < (b-a)^{4/3} for a triple."""
    n, worst = 0, 0.0
    for (a, b), ms in CLASSES.items():
        M, D = b - a, a * b
        ms = sorted(ms)
        xs = [isqrt(a * m - 1) for m in ms]
        ys = [isqrt(b * m - 1) for m in ms]
        for i in range(len(ms)):
            if xs[i] < 1:
                continue
            for j in range(i + 1, len(ms)):
                if ms[j] >= 2 * ms[i]:
                    continue
                V = abs(xs[i] * ys[j] - xs[j] * ys[i])
                assert 0 < V < M / sqrt(3 * D), (a, b, ms[i], ms[j])
                worst = max(worst, V * sqrt(3 * D) / M)
                n += 1
    assert n > 100 and worst < 1, (n, worst)
    # M <= |V12 V23 V13| < (M/sqrt(3D))^3  <=>  (3D)^{3/2} < M^2  <=>  3D < M^{4/3}
    for t in (133.875, 1000.0, 10000.0):
        assert int((t - 1) ** 2 / (3 * t) ** 1.5) == {133.875: 2, 1000.0: 6,
                                                      10000.0: 19}[t]


def _vp(n, p):
    if n == 0:
        return 10 ** 9
    v = 0
    while n % p == 0:
        n //= p
        v += 1
    return v


def test_O10_valuation_split_and_the_V_lower_bound_for_every_M():
    """s_i + t_i >= e, and v_p(V_ij) >= max(min(s,s), min(t,t)).  Any M."""
    from sympy import factorint

    n_st = n_lb = 0
    for (a, b), ms in CLASSES.items():
        M = b - a
        if M < 2:
            continue
        ms = sorted(ms)
        xs = [isqrt(a * m - 1) for m in ms]
        ys = [isqrt(b * m - 1) for m in ms]
        for p, e in factorint(M).items():
            assert a % p != 0, (a, b, p)            # gcd(a,M) = 1
            s = [min(e, _vp(x + y, p)) for x, y in zip(xs, ys)]
            t = [min(e, _vp(x - y, p)) for x, y in zip(xs, ys)]
            for i in range(len(ms)):
                assert s[i] + t[i] >= e, (a, b, ms[i], p, s[i], t[i])
                n_st += 1
            for i in range(len(ms)):
                for j in range(i + 1, len(ms)):
                    V = xs[i] * ys[j] - xs[j] * ys[i]
                    assert _vp(V, p) >= max(min(s[i], s[j]), min(t[i], t[j])), (
                        a, b, ms[i], ms[j], p)
                    n_lb += 1
    assert n_st > 1000 and n_lb > 200, (n_st, n_lb)


def test_O10_M_divides_the_product_of_the_three_Vs_for_every_M():
    """The ordered two-term sum gives p^e, hence M | V12 V23 V13 -- any M."""
    from sympy import factorint

    n = 0
    kinds = set()
    for (a, b), ms in CLASSES.items():
        M = b - a
        if M < 2 or len(ms) < 3:
            continue
        ms = sorted(ms)
        xs = [isqrt(a * m - 1) for m in ms]
        ys = [isqrt(b * m - 1) for m in ms]
        fac = factorint(M)
        kinds.add((M % 2 == 0, any(e > 1 for e in fac.values())))
        # the ordered two-term bound, per prime
        for p, e in fac.items():
            s = [min(e, _vp(x + y, p)) for x, y in zip(xs, ys)]
            order = sorted(range(len(ms)), key=lambda i: s[i])
            for q in range(len(order) - 2):
                i1, i2, i3 = order[q], order[q + 1], order[q + 2]
                v12 = xs[i1] * ys[i2] - xs[i2] * ys[i1]
                v23 = xs[i2] * ys[i3] - xs[i3] * ys[i2]
                assert _vp(v12, p) + _vp(v23, p) >= e, (a, b, p)
        for i in range(len(ms)):
            for j in range(i + 1, len(ms)):
                for k in range(j + 1, len(ms)):
                    v12 = xs[i] * ys[j] - xs[j] * ys[i]
                    v23 = xs[j] * ys[k] - xs[k] * ys[j]
                    v13 = xs[i] * ys[k] - xs[k] * ys[i]
                    assert abs(v12 * v23 * v13) % M == 0, (a, b, ms[i], ms[j], ms[k])
                    n += 1
    assert n > 5, n
    assert len(kinds) >= 2, kinds       # more than one parity/squarefree class


def test_O10_the_sign_is_the_e_equals_one_shadow():
    """At v_p(M) = 1, S T = -M m forces s + t = 1, so (s,t) is (1,0) or (0,1)."""
    from sympy import factorint

    n = 0
    for (a, b), ms in CLASSES.items():
        M = b - a
        if M < 2:
            continue
        for p, e in factorint(M).items():
            if e != 1:
                continue
            for m in ms:
                x, y = isqrt(a * m - 1), isqrt(b * m - 1)
                s, t = min(1, _vp(x + y, p)), min(1, _vp(x - y, p))
                assert s + t == 1, (a, b, m, p)     # exactly one, i.e. a sign
                n += 1
    assert n > 500, n


def test_O10_coverage_is_measured_over_the_informative_population():
    """~35% of classes that COULD host a triple, not ~99% of all classes.

    A class with fewer than three shared moduli cannot host a triple whatever any
    theorem says, so it is vacuous for this question.  At X = 3000 only 60 of
    1,815,154 classes have three shared moduli, so a percentage over all classes
    measures the vacuity and not the reach.
    """
    allc = inf = exc_all = exc_inf = 0
    for (a, b), ms in CLASSES.items():
        M = b - a
        if M < 2:
            continue
        allc += 1
        bad = 3 * a * b >= M ** (4 / 3)
        exc_all += bad
        if len(ms) >= 3:
            inf += 1
            exc_inf += bad
    assert inf >= 5, inf
    assert inf / allc < 0.001, (inf, allc)          # the denominator is vacuous
    assert exc_all / allc > 0.95                    # the misleading figure
    assert 0.2 < exc_inf / inf < 0.6, (exc_inf, inf)  # the honest one, ~35%


def _C(X1):
    """(sqrt rho - 1/sqrt rho)^3 (sqrt rho + 1/sqrt rho), rho = sqrt(2+1/X1^2)."""
    r = sqrt(sqrt(2 + 1 / X1**2))
    return (r - 1 / r) ** 3 * (r + 1 / r)


def test_O11_the_equal_split_maximises_the_product():
    """sinh(u) sinh(w-u) is maximised at u = w/2, so the three R's interact."""
    from math import sinh

    for w in (0.2, 0.34657359, 0.5, 1.0):
        grid = [(sinh(u) * sinh(w - u), u) for u in
                [i * w / 4000 for i in range(1, 4000)]]
        best_v, best_u = max(grid)
        assert abs(best_u - w / 2) < w / 1000, (w, best_u)
        assert abs(best_v - sinh(w / 2) ** 2) < 1e-12


def test_O11_constant_and_that_it_beats_O10_by_the_stated_factor():
    """C(X1)/8 to the 2/3; asymptotically 0.048628 against O.10's 1/3."""
    assert abs((_C(10**6) / 8) ** (2 / 3) - 0.048628) < 1e-5
    assert abs((_C(1) / 8) ** (2 / 3) - 0.125873) < 1e-5
    assert abs((1 / 3) / ((_C(10**6) / 8) ** (2 / 3)) - 6.855) < 0.01
    # monotone in X1, and always stronger than O.10
    prev = 1.0
    for X1 in (1, 2, 3, 5, 10, 100, 10**6):
        c = (_C(X1) / 8) ** (2 / 3)
        assert c < prev and c < 1 / 3
        prev = c


def test_O11_is_never_weaker_than_O10_on_realised_classes():
    """Every class O.10 excludes, O.11 excludes -- and strictly more."""
    old = new = inf = 0
    for (a, b), ms in CLASSES.items():
        M = b - a
        if M < 2 or len(ms) < 3:
            continue
        inf += 1
        X1 = max(1, isqrt(a * min(ms) - 1))
        o = 3 * a * b >= M ** (4 / 3)
        n = a * b >= (_C(X1) / 8) ** (2 / 3) * M ** (4 / 3)
        assert not (o and not n), (a, b)      # O.11 never weaker
        old += o
        new += n
    assert inf >= 5, inf
    assert new > old, (old, new)


def test_O11_admits_only_unit_cofactor_classes_in_this_range():
    """No informative class with a >= 2 is admitted for X <= 8000.

    A RANGE EFFECT, NOT A LAW: O.11 admits (a,b) as soon as ab < c (b-a)^{4/3},
    and for fixed a the right side wins as b -> infinity.  The crossover is
    b ~ 9.0e3 at a = 1, 7.0e4 at a = 2, 2.4e5 at a = 3.  The a >= 2 column is
    empty because the sweep does not reach far enough in b.

    It matters because `full-graph-growth-is-pell` records that n1 = 1 cannot
    occur in a Type II hypothesis, where both variables are confined to ranges.
    """
    inf2 = adm2 = inf1 = 0
    for (a, b), ms in CLASSES.items():
        M = b - a
        if M < 2 or len(ms) < 3:
            continue
        X1 = max(1, isqrt(a * min(ms) - 1))
        admitted = a * b < (_C(X1) / 8) ** (2 / 3) * M ** (4 / 3)
        if a == 1:
            inf1 += 1
        else:
            inf2 += 1
            adm2 += admitted
    assert inf1 > 0 and inf2 > 0, (inf1, inf2)
    assert adm2 == 0, adm2
    # and the law that says this must eventually fail
    c = (_C(10 ** 6) / 8) ** (2 / 3)
    for a, floor in ((1, 5000), (2, 40000), (3, 150000)):
        b = next(b for b in range(a + 1, 3 * 10 ** 6, 97)
                 if a * b < c * (b - a) ** (4 / 3))
        assert b > floor, (a, b)      # admitted at large b for every a


def test_O12_threshold_and_that_a_dyadic_band_is_inside_it():
    """u > (5+sqrt21)/2 = 4.7913 is needed for two shared moduli in a window."""
    thr = (5 + sqrt(21)) / 2
    assert abs(thr - 4.7912878475) < 1e-9
    # tau(1)^2 < 3  =>  s < 1/sqrt3  =>  M/sqrtD > sqrt3;  M/sqrtD = (u-1)/sqrt u
    assert abs((thr - 1) / sqrt(thr) - sqrt(3)) < 1e-12
    assert thr > 2                       # a dyadic band cannot reach it
    assert thr / 2 > 2.39                # with a factor 2.4 to spare
    # the asymptotic version, and the |V| >= 2 version, for contrast
    asym = 5 + 2 * sqrt(6)
    assert abs((asym - 1) / sqrt(asym) - 2 * sqrt(2)) < 1e-12
    assert abs(asym - 9.8989794856) < 1e-9
    assert (1 + sqrt(2)) ** 4 > asym > thr > 2


def test_O12_banded_cofactors_share_at_most_one_modulus_per_window():
    """C_4-free on the doubly-dyadic configuration; free cofactors reach 2.

    "ANY dyadic window" means ANY two shared moduli within a factor 2 of each
    other -- NOT windows anchored at powers of two.  An anchored sweep is a
    strictly WEAKER test: [8,16) and [16,32) between them miss the pair (9,17),
    which is the witness that breaks this property at c = 6.  The first version
    of this test anchored, and would have passed on a counterexample.
    """
    from collections import defaultdict

    XX = 700
    inc = defaultdict(set)
    for x in range(1, XX + 1):
        v = x * x + 1
        d = 1
        while d * d <= v:
            if v % d == 0:
                inc[v // d].add(d)
                if d * d != v:
                    inc[d].add(v // d)
            d += 1
    ns = sorted(inc)
    worst_banded = worst_free = 0
    n_banded = 0
    for i, n1 in enumerate(ns):
        for n2 in ns[i + 1:]:
            sh = sorted(inc[n1] & inc[n2])
            if not sh:
                continue
            best = max(
                (sum(1 for q in sh if p <= q < 2 * p) for p in sh), default=0
            )
            if n2 < 2 * n1:                      # cofactors in one band
                n_banded += 1
                assert best <= 1, (n1, n2, sh)   # O.12
                worst_banded = max(worst_banded, best)
            worst_free = max(worst_free, best)
    assert n_banded > 500, n_banded
    assert worst_banded == 1, worst_banded
    assert worst_free >= 2, worst_free       # free cofactors DO reach 2


def test_O12_has_slack_so_the_range_may_be_read_loosely():
    """4.7913 uses only |V| >= 1; |V| >= 2 gives 13.93 / 33.97, observed min 43.79."""
    thr1 = (5 + sqrt(21)) / 2
    # |V| >= 2: tau_1 = (t+1)/(t-1), t = sqrt(b/a).  A PAIR needs
    # tau_1^2 < 2 + 1/X1^2, so the bound on tau_1 is the SQUARE root -- the
    # fourth root is the TRIPLE condition tau_1^4 < 2 + 1/X1^2, which gives
    # 53.694 at X1 = 1 and is O.4's number, not this one.
    for X1, want in ((1, 13.9282), (10 ** 9, 33.9706)):
        B = sqrt(2 + 1 / X1 ** 2)
        t = (B + 1) / (B - 1)
        assert abs(t * t - want) < 1e-3, (X1, t * t)
    for X1, want in ((1, 53.6942), (10 ** 9, 133.8748)):        # the triple case
        B = (2 + 1 / X1 ** 2) ** 0.25
        t = (B + 1) / (B - 1)
        assert abs(t * t - want) < 1e-3, (X1, t * t)
    assert thr1 < 13.9282 < 33.9706
    # and the smallest ratio actually realised, recorded from exp24's sweep
    assert 1489 / 34 > 43.7 and abs(1489 / 34 - 43.7941) < 1e-3
    assert (1489 / 34) / thr1 > 9        # 9.1x the proved bound


def test_windowed_gram_bound_holds_for_UNANCHORED_windows_too():
    """"Every dyadic window [M,2M)" means every M, not every power of two.

    `rational-gram-bounded-on-windows` is measured by exp09, whose sweep is
    `M = 2; while M <= cap: ...; M *= 2` -- anchored.  That is strictly weaker
    than the claim's wording: [8,16) and [16,32) between them miss the pair
    (9,17), which is exactly how the line-family sweep passed on a counterexample
    at c = 6.  Here the stronger statement is checked directly, and holds.
    """
    from collections import defaultdict

    XX = 900
    inc = defaultdict(set)
    for x in range(1, XX + 1):
        v = x * x + 1
        d = 1
        while d * d <= v:
            if v % d == 0:
                inc[v // d].add(d)
                if d * d != v:
                    inc[d].add(v // d)
            d += 1
    ns = sorted(inc)
    anchored = unanchored = 0
    pairs = 0
    for i, n1 in enumerate(ns):
        for n2 in ns[i + 1:]:
            sh = sorted(inc[n1] & inc[n2])
            if len(sh) < 2:
                continue
            pairs += 1
            M = 1
            while M <= XX * XX:
                anchored = max(anchored, sum(1 for m in sh if M <= m < 2 * M))
                M *= 2
            unanchored = max(
                unanchored,
                max(sum(1 for q in sh if p <= q < 2 * p) for p in sh),
            )
    assert pairs > 50, pairs
    assert anchored == 2, anchored
    assert unanchored == 2, unanchored       # the stronger statement holds too


def test_O13_tau1_window_threshold_is_seventeen_plus_twelve_root_two():
    """Prop O.13: tau_1^2 < 2 <=> u > (1+sqrt2)^4 = 17 + 12 sqrt 2.

    Guards the closed form against both algebra slips and the float-boundary
    trap: the threshold is exact, so it is checked symbolically, and the
    equivalence is checked strictly on both sides of it.
    """
    from sympy import Rational, nsimplify, simplify, sqrt as ssqrt, symbols, solve

    u = symbols("u", positive=True)
    thr = (1 + ssqrt(2)) ** 4
    assert simplify(thr - (17 + 12 * ssqrt(2))) == 0

    # tau_1^2 = ((sqrt u + 1)/(sqrt u - 1))^2 = 2  has the threshold as its root
    roots = solve(((ssqrt(u) + 1) / (ssqrt(u) - 1)) ** 2 - 2, u)
    assert any(simplify(r - thr) == 0 for r in roots), roots

    t = float(thr)
    tau2 = lambda v: ((v ** 0.5 + 1) / (v ** 0.5 - 1)) ** 2
    assert tau2(t * 1.001) < 2.0      # above the threshold: fits a window
    assert tau2(t * 0.999) > 2.0      # below it: cannot


def test_O13prime_threshold_family_and_the_V_equals_one_condition():
    """O.13': u > (sqrt2 V + sqrt(2V^2+1))^2, and V=1 needs a^2-ab+b^2 square.

    Checks the closed forms symbolically (V = 1 and V = 2 collapse to
    5 + 2 sqrt 6 and 17 + 12 sqrt 2), that V = 2 is ALWAYS admissible via
    U = a+b, and that the identity U^2 = M^2 + D equals a^2 - ab + b^2 -- which
    is what turns the V = 1 case into a Diophantine condition.
    """
    from math import isqrt
    from sympy import simplify, sqrt as ssqrt

    thr = lambda V: (ssqrt(2) * V + ssqrt(2 * V ** 2 + 1)) ** 2
    assert simplify(thr(1) - (5 + 2 * ssqrt(6))) == 0
    assert simplify(thr(2) - (17 + 12 * ssqrt(2))) == 0
    assert simplify(thr(2) - (1 + ssqrt(2)) ** 4) == 0

    for a, b in ((37, 1261), (25, 481), (13, 449), (2, 82)):
        M, D = b - a, a * b
        # V = 2 is admissible for every pair, with U = a + b
        assert (a + b) ** 2 - D * 2 ** 2 == M * M
        # V = 1 needs U^2 = M^2 + D, and that quantity IS a^2 - ab + b^2
        assert M * M + D == a * a - a * b + b * b

    # thresholds increase with V, so no V >= 3 rescues what V = 2 rejects
    vals = [float(thr(V)) for V in (1, 2, 3)]
    assert vals == sorted(vals), vals

    # WITHDRAWN READING, pinned so it cannot come back: (25,481) at D = 4 has
    # a^2-ab+b^2 = 469^2, which was read as "V = 1, hence sub-threshold".  At
    # D = 4 the invariant is M*D, so the V = 1 test is whether (M*D)^2 + ab is
    # square -- and it is not.  The D-generalisation is not done.
    a, b, Ds = 25, 481, 4
    M, Dc = b - a, a * b
    assert isqrt(a * a - a * b + b * b) ** 2 == a * a - a * b + b * b
    assert isqrt((M * Ds) ** 2 + Dc) ** 2 != (M * Ds) ** 2 + Dc
