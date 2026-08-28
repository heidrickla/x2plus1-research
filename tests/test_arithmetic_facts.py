"""Tests of the arithmetic facts the notes rely on.

These are not unit tests of code so much as machine-checked statements of the
lemmas in Note A.  If one of these fails, a note is wrong.
"""

import math

import pytest
from sympy import factorint

from x2plus1.factorization import (
    check_factorisation, gauss_factor_x_plus_i, rho, roots_of_minus_one,
    sieve_factor_x2plus1, sieve_shifted_square,
)
from x2plus1.gaussian import exact_div, norm
from x2plus1.typeI import count_in_progression, type_i_x2plus1

X_SMALL = 3000
FAC = sieve_factor_x2plus1(X_SMALL)


def test_sieve_agrees_with_sympy():
    for x in [1, 2, 3, 7, 239, 1234, X_SMALL]:
        assert FAC[x] == factorint(x * x + 1)


def test_shifted_square_sieve_agrees_with_sympy():
    for c in (1, 16, 81, 625):
        F = sieve_shifted_square(300, c)
        for a in (1, 2, 5, 137, 300):
            assert F[a] == factorint(a * a + c), (c, a)


def test_no_prime_3_mod_4_divides_x2_plus_1():
    for x in range(1, X_SMALL + 1):
        assert all(p % 4 != 3 for p in FAC[x])


def test_two_divides_x2_plus_1_exactly_once_for_odd_x():
    for x in range(1, X_SMALL + 1):
        assert FAC[x].get(2, 0) == (1 if x % 2 else 0)


def test_gaussian_factorisation_of_x_plus_i():
    for x in range(1, X_SMALL + 1):
        assert check_factorisation(x, gauss_factor_x_plus_i(x, FAC[x]))


def test_rho_is_multiplicative_and_matches_the_local_rules():
    assert rho(1) == 1 and rho(2) == 1 and rho(4) == 0
    for p in (3, 7, 11, 19, 23, 31):
        assert rho(p) == 0
    for p in (5, 13, 17, 29, 37):
        assert rho(p) == 2 and rho(p * p) == 2
    for m, n in [(5, 13), (2, 5), (5, 17), (13, 29)]:
        assert rho(m * n) == rho(m) * rho(n)


def test_roots_really_are_roots():
    for q in range(1, 400):
        for r in roots_of_minus_one(q):
            assert (r * r + 1) % q == 0


def test_divisibility_is_the_congruence_of_note_a():
    """d | x + i  <=>  x == r_d (mod N(d)).  The whole Type I story."""
    from x2plus1.gaussian import gcd
    for q in range(2, 120):
        for r in roots_of_minus_one(q):
            d = gcd((q, 0), (r, 1))
            assert norm(d) == q
            for x in range(1, 400):
                assert (exact_div((x, 1), d) is not None) == (x % q == r % q)


def test_type_i_error_per_modulus_is_at_most_one():
    """|r_d| <= 1 for every ideal: an interval meets a class in floor/ceil points."""
    X = 500
    for q in range(1, 1200):
        for r in roots_of_minus_one(q):
            err = abs(count_in_progression(X, q, r) - X / q)
            assert err <= 1.0 + 1e-12, (q, r, err)


def test_admissible_ideal_count_matches_zeta_L_over_zeta2():
    """#{d : N(d) <= D} ~ (3/2pi) D, the residue of zeta(s)L(s,chi_4)/zeta(2s)."""
    D = 60000
    rep = type_i_x2plus1(100, D)
    predicted = 3 / (2 * math.pi)
    assert rep.n_moduli / D == pytest.approx(predicted, rel=0.01)


def test_mu_of_x2plus1_is_not_multiplicative_in_x():
    """Note M: mu(n^2+1) is not a multiplicative function of n.

    This is why Granville-Shao's theory, and multiplicative-function machinery
    generally, does not apply here *as stated* rather than merely being too
    weak. It fails at n = 1 already -- mu(1^2+1) = mu(2) = -1, not 1 -- and it
    fails non-degenerately too.
    """
    from math import gcd
    from sympy import mobius
    assert mobius(1 * 1 + 1) == -1                     # f(1) != 1
    witnesses = [
        (2, 7),                                        # mu(5)mu(50) = 0, mu(197) = -1
        (2, 9),                                        # mu(5)mu(82) = -1, mu(325) = 0
        (2, 11),                                       # mu(5)mu(122) = -1, mu(485) = 1
    ]
    for a, b in witnesses:
        assert gcd(a, b) == 1
        assert mobius(a * a + 1) * mobius(b * b + 1) != mobius((a * b) ** 2 + 1), (a, b)


def test_bulk_root_table_agrees_with_the_per_modulus_reference():
    """admissible_roots_upto is a bulk rebuild of roots_of_minus_one.

    Built for Note J's all-moduli cross-check, which sympy's factorint per
    modulus had capped at X <= 10^5.
    """
    from x2plus1.factorization import admissible_roots_upto, roots_of_minus_one
    table = admissible_roots_upto(3000)
    for q in range(1, 3001):
        assert table.get(q, []) == roots_of_minus_one(q), q


def test_bulk_root_table_reproduces_the_admissible_ideal_density():
    """sum_q rho(q) / Q -> 3/(2 pi), Note B's calibration, from the other side.

    The Type I harness measures this by enumerating Gaussian ideals; this counts
    roots of r^2+1 = 0 (mod q). Two independent code paths, same constant.
    """
    import math
    from x2plus1.factorization import admissible_roots_upto
    Q = 200000
    table = admissible_roots_upto(Q)
    ideals = sum(len(v) for v in table.values())
    assert ideals / Q == pytest.approx(3 / (2 * math.pi), rel=0.002)


def _multipliers_in_box(a_max, b_max, k_max):
    """(a, b, k, M, D, U, B) for every multiplier with k >= 2 in a box.

    A multiplier is a solution of U^2 - D V^2 = M^2 with V = 2k, D = ab,
    M = b - a -- a ratio between solution CLASSES of the modulus equation
    Y^2 - D X^2 = aM. The two are different equations; see Note L.
    """
    from math import gcd, isqrt
    from x2plus1.factorization import roots_of_minus_one

    def admissible(n):
        return n % 4 != 0 and bool(roots_of_minus_one(n))

    out = []
    for a in range(1, a_max + 1):
        if not admissible(a):
            continue
        for b in range(a + 1, b_max + 1):
            if not admissible(b) or gcd(a, b) != 1:
                continue
            M, D = b - a, a * b
            for k in range(2, k_max + 1):
                v = M * M + 4 * k * k * D
                u = isqrt(v)
                if u * u == v:
                    out.append((a, b, k, M, D, u, u - 2 * k * a))
    return out


def test_O3prime_identity_is_exact():
    """M(rho^2 - 1) = 4ka(k - rho) with rho = B_k/M -- Note O's Theorem O.3'.

    Substituting U_k = rho M + 2ka into U_k^2 = M^2 + 4k^2 a(a+M) cancels the
    M^2 and 4k^2 a^2 terms and leaves this. Checked in exact rationals, because
    the whole point of rho is that its denominator is what the theorem counts.
    """
    from fractions import Fraction
    rows = _multipliers_in_box(40, 12000, 30)
    assert rows, "the box must contain multipliers or the test proves nothing"
    for a, b, k, M, D, U, B in rows:
        rho = Fraction(B, M)
        assert M * (rho * rho - 1) == 4 * k * a * (k - rho), (a, b, k)


def test_window_condition_is_r_squared_not_r():
    """The modulus ratio is tau^2, so a dyadic window needs r_k^2 < 2.

    Note O first stated Theorem O.3' under 'r_k < 2'. That is a different and
    weaker condition -- r_k^2 < 2 is equivalent to M > 4 sqrt2 k sqrt(D), the
    constant the proof actually uses, while r_k < 2 gives only M > (8/3) k
    sqrt(D). The rho bound below holds under the first and fails under the
    second, so the distinction decides the theorem.
    """
    from math import sqrt
    rows = _multipliers_in_box(40, 12000, 30)
    for a, b, k, M, D, U, B in rows:
        r = (U + 2 * k * sqrt(D)) / M
        assert (r * r < 2) == (M > 4 * sqrt(2) * k * sqrt(D)), (a, b, k)


def test_O3prime_rho_bound_holds_exactly_on_the_right_hypothesis():
    """rho < sqrt(9/8) under r_k^2 < 2, and NOT under r_k < 2.

    sqrt(9/8) = 1.06066 is what forces c = gcd(M, 2X) >= 17: c*rho is an integer
    in (c, 1.06066c), which is empty until 1.06066c >= c+1. The bound is the
    theorem, so both halves are asserted -- the second half is what caught the
    misstated hypothesis.
    """
    from math import sqrt
    bound = sqrt(9 / 8)
    rows = _multipliers_in_box(40, 12000, 30)
    tight = loose = 0
    for a, b, k, M, D, U, B in rows:
        r = (U + 2 * k * sqrt(D)) / M
        rho = B / M
        if r * r < 2:
            tight += 1
            assert 1 < rho < bound, (a, b, k, rho)
        elif r < 2 and rho >= bound:
            loose += 1
    assert tight, "no multiplier satisfies the window condition; box too small"
    assert loose, "the loose hypothesis must admit violations, else nothing was shown"


def test_O3prime_permits_the_two_observed_moduli_of_the_live_pair():
    """(53, 423125) has moduli 10 and 17 in one window; O.3' must allow both.

    M = 423072 is even and non-squarefree, so the earlier Theorem O.3 is mute on
    it. This is the concrete falsifier for any extension: c = gcd(M, 2X) must
    come out <= 16 at both moduli, or the extension forbids a configuration that
    demonstrably exists.
    """
    from math import gcd, isqrt
    a, b = 53, 423125
    M = b - a
    assert M % 2 == 0 and M % 9 == 0                   # even and non-squarefree
    for m, expected_c in ((10, 2), (17, 12)):
        x2 = a * m - 1
        x = isqrt(x2)
        assert x * x == x2, m                          # a*m is in the sequence
        y2 = b * m - 1
        y = isqrt(y2)
        assert y * y == y2, m                          # and so is b*m
        assert gcd(M, 2 * x) == expected_c <= 16, m


def test_mobius_of_the_cofactor_factors_when_the_value_is_squarefree():
    """mu((x^2+1)/m) = mu(m) mu(x^2+1) whenever x^2+1 is squarefree.

    Elementary, and it is what links exp02's S_mu to exp05's per-progression
    sums: if N = x^2+1 is squarefree and m | N then gcd(m, N/m) = 1, so
    mu(N) = mu(m) mu(N/m), and mu(m)^2 = 1 gives the stated form. Under the
    absolute value in S_mu(M) = sum_m |sum_x mu((x^2+1)/m)| the mu(m) is a
    constant of modulus 1 and drops out, leaving exactly the quantity exp05
    measures per progression. See Note M.
    """
    from sympy import divisors, factorint, mobius
    checked = 0
    for x in range(1, 400):
        n = x * x + 1
        f = factorint(n)
        if any(e > 1 for e in f.values()):
            continue
        for m in divisors(n):
            assert mobius(n // m) == mobius(m) * mobius(n), (x, m)
            checked += 1
    assert checked > 1000, f"only {checked} pairs checked; the range proves little"


def test_squarefree_density_of_x2plus1_is_flat():
    """The correction between the two normalisations is an asymptotic constant.

    Only p = 2 and p = 1 (mod 4) admit p^2 | x^2+1, and each costs density
    2/p^2, so truncating at P = 20000 costs under 1e-5. Measured 0.895200,
    0.894900, 0.894860, 0.894847 at X = 1e4 .. 1e7 -- flat to four places. A
    constant factor cannot move the exponent in S(M) ~ sqrt(M X), which is why
    exp05's four decades bear on exp02's law and not merely on an analogue.
    """
    import numpy as np
    from math import isqrt
    from sympy import sqrt_mod

    P = 4000
    s = np.ones(P + 1, bool)
    s[:2] = False
    for i in range(2, isqrt(P) + 1):
        if s[i]:
            s[i * i:: i] = False
    roots = {}
    for p in np.flatnonzero(s).tolist():
        if p != 2 and p % 4 != 1:
            continue
        r = sqrt_mod(-1, p * p, all_roots=True)
        if r:
            roots[p * p] = [int(t) for t in r]

    def density(X):
        ok = np.ones(X + 1, bool)
        for q, rs in roots.items():
            for r in rs:
                if r <= X:
                    ok[r:: q] = False
        return ok[1:X + 1].sum() / X

    d1, d2 = density(20_000), density(200_000)
    assert abs(d1 - 0.8952) < 2e-3, d1
    assert abs(d2 - d1) < 1e-3, (d1, d2)


def test_a_modulus_root_pair_is_a_primitive_gaussian_ideal():
    """#roots of -1 mod m = #ideals of norm m coprime to their conjugate.

    This is what makes the two groupings of S_mu the Z and Z[i] versions of one
    sum: an absolute value per (m, root) is one per primitive Gaussian ideal,
    while an absolute value per rational m merges them. ASP's (B) asks for the
    second, so the sieve-relevant exponent is the per-modulus one.

    Primitivity carries the content -- (5) has norm 25 but 5 never divides
    x^2+1, while p^2 and pbar^2 give the two roots mod 25. Both counts are
    2^{#odd primes}: CRT and Hensel on the root side, a choice of p^e or pbar^e
    at each odd prime on the ideal side.
    """
    from sympy import factorint
    from x2plus1.factorization import roots_of_minus_one

    def primitive_ideals(m):
        n = 1
        for p, e in factorint(m).items():
            if p == 2:
                if e > 1:
                    return 0
            elif p % 4 == 1:
                n *= 2
            else:
                return 0
        return n

    checked = 0
    for m in range(2, 3000):
        if m % 4 == 0:
            continue
        roots = roots_of_minus_one(m)
        if not roots:
            continue
        assert len(roots) == primitive_ideals(m), m
        checked += 1
    assert checked > 400, f"only {checked} moduli checked"


def test_the_mobius_sieve_agrees_with_sympy_on_x2plus1():
    """exp16's mobius_of_x2plus1 against sympy, value by value.

    That sieve is what makes S_mu computable past exp02's ceiling -- it underpins
    root-grouping-splits-the-two-normalisations and
    saving-law-measured-through-theta-half -- and it was written in one sitting
    with no independent check. Its delicate parts are the p^2 branch (which must
    zero mu rather than flip it) and the leftover cofactor above X (which must be
    a single prime, since two factors above X would multiply past X^2+1).

    A sieve that is wrong in the same way everywhere would still produce a smooth
    law and a clean exponent, so agreement with an independent implementation is
    the only thing that distinguishes "the measurement is right" from "the
    measurement is self-consistent".
    """
    import sys
    from pathlib import Path
    from sympy import mobius

    repo = Path(__file__).resolve().parent.parent
    sys.path.insert(0, str(repo / "experiments"))
    from exp16_m_exponent import mobius_of_x2plus1

    X = 4000
    sieved = mobius_of_x2plus1(X)
    for x in range(1, X + 1):
        assert sieved[x] == mobius(x * x + 1), (x, x * x + 1, int(sieved[x]))
    # and the non-squarefree values must actually be present, or the p^2 branch
    # is untested by the comparison above
    zeros = sum(1 for x in range(1, X + 1) if sieved[x] == 0)
    assert zeros > 300, f"only {zeros} zero values; the p^2 branch is barely exercised"


def test_ratio_classes_agrees_with_an_independent_construction():
    """polyseq.ratio_classes against a divisor-built incidence table.

    A dozen tests consume ratio_classes and none checks it: if it were wrong they
    would agree with each other and all be wrong together. This rebuilds the same
    object from divisors of x^2+1 rather than from pairwise gcds, so an error in
    either construction shows as a disagreement.
    """
    from collections import defaultdict
    from math import gcd

    from x2plus1.polyseq import ratio_classes

    X = 500
    mine = defaultdict(set)
    values = {x: x * x + 1 for x in range(1, X + 1)}
    for x in range(1, X + 1):
        for y in range(x + 1, X + 1):
            g = gcd(values[x], values[y])
            if g > 1:
                mine[(values[x] // g, values[y] // g)].add(g)
    theirs = ratio_classes(X)
    assert set(mine) == set(theirs), "class sets differ"
    for key in mine:
        assert sorted(mine[key]) == sorted(theirs[key]), key
    assert len(mine) > 5000, f"only {len(mine)} classes; range too small to mean much"


def test_the_type_I_sum_constant_is_one_over_two_pi():
    """sum_{N(d)<=D} |r_d| ~ D/(2 pi), not ~ D.

    `type-I-level` states the sum as "~ D", which is right about the ORDER and
    wrong by a factor of 2 pi read as an equality. The constant is forced:

      r_d = 1 - r/q - theta with r/q and theta both roughly uniform, so r_d is
      triangular on (-1,1) and E|r_d| = int_0^1 2t(1-t) dt = 1/3;
      admissible (q, root) pairs of norm <= D number ~ (3/2 pi) D;
      hence sum |r_d| ~ (1/3)(3/2 pi) D = D/(2 pi) = 0.159155.

    Nothing downstream moves -- the argument needs the sum to be of order D, and
    a constant cannot change D = o(X) into anything else. This pins the constant
    so the claim cannot be read as an equality.
    """
    import math

    from x2plus1.factorization import admissible_roots_upto

    X, D = 400_000, 40_000
    table = admissible_roots_upto(D)
    total = 0.0
    pairs = 0
    for q, roots in table.items():
        if q < 2:
            continue
        for r in roots:
            count = (X - r) // q + 1 if r <= X else 0
            total += abs(count - X / q)
            pairs += 1
    assert pairs > 15_000, f"only {pairs} pairs; range too small"
    assert total / pairs == pytest.approx(1 / 3, rel=0.02), total / pairs
    assert total / D == pytest.approx(1 / (2 * math.pi), rel=0.02), total / D


def test_the_full_graph_growth_slope_is_one_over_log_phi_squared():
    """G'(1,5) = log X / log(phi^2) + O(1), slope 1.0390.

    `full-graph-growth-is-pell` says the Gram maximum "grows like log X" with no
    constant. Unlike the other order-statements swept for this, the constant here
    is 1.0390 -- near enough to 1 that the loose reading is not misleading. Pinned
    anyway, because "the category does not apply here" is only worth saying if the
    number is known.

    The family is x = 1, 3, 8, 21, 55, 144, ... with y = 3, 7, 18, 47, 123, 322,
    and y_k ~ phi^{2k}, so the count with y <= X is log X / log(phi^2).
    """
    from math import isqrt, log, sqrt

    phi = (1 + sqrt(5)) / 2
    slope = 1 / log(phi ** 2)
    assert slope == pytest.approx(1.0390, abs=1e-3)

    # x runs over F_2, F_4, F_6, ... which satisfy x_{k+1} = 3 x_k - x_{k-1}.
    # Searching for them by incrementing x costs 10^8 steps to reach the tenth.
    family = []
    prev, cur = 0, 1
    while cur <= 20_000:
        m = cur * cur + 1
        r = isqrt(5 * m - 1)
        assert r * r == 5 * m - 1, cur      # the recurrence must stay on the family
        family.append((cur, r))
        prev, cur = cur, 3 * cur - prev

    # reproduces the repo's recorded full-graph maxima 6, 7, 7, 8, 9
    recorded = {500: 6, 1000: 7, 2000: 7, 4000: 8, 8000: 9}
    for X, expected in recorded.items():
        got = sum(1 for a, b in family if a <= X and b <= X)
        assert got == expected, (X, got, expected)
        assert -1.0 < got - slope * log(X) < 0.0, (X, got - slope * log(X))


def test_kappa_is_exactly_Q_to_the_two_alpha_minus_one():
    """kappa = |A|^2/Q = Q^{2 alpha - 1}, so kappa > 1 is exactly alpha > 1/2.

    Note D's ledger prints alpha and "kappa > 1?" as separate columns and Note K's
    headline reads as a finding about kappa. It is a finding about density: the
    two conditions are identical, not merely correlated. Checked on the four
    sequences the ledger carries.
    """
    from fractions import Fraction

    for alpha in (Fraction(3, 4), Fraction(2, 3), Fraction(1, 2), Fraction(5, 6)):
        for logQ in (10, 20, 40):
            size = 2.0 ** (float(alpha) * logQ)      # |A| = Q^alpha
            Q = 2.0 ** logQ
            kappa = size * size / Q
            assert abs(kappa - 2.0 ** (float(2 * alpha - 1) * logQ)) < 1e-6 * kappa
            assert (kappa > 1) == (alpha > Fraction(1, 2))
            assert (kappa == 1) == (alpha == Fraction(1, 2))


def test_every_single_line_is_c4_free_and_has_kappa_one():
    """Note F's lemma is not about x^2+1. It is about *a line*.

    For A_c = {a + ci : a >= 1, a^2 + c^2 <= Q} the C4-free argument is the same
    one Note F gives for c = 1: (a1+ci)(a4+ci) = (a2+ci)(a3+ci) forces
    a1 a4 = a2 a3 and a1 + a4 = a2 + a3, so {a1,a4} = {a2,a3}. And |A_c| =
    isqrt(Q - c^2), so kappa = |A|^2/Q = 1 - c^2/Q -- **exactly 1 in the limit,
    for every c**. A single line cannot have kappa > 1; the geometry forbids it.

    This is why kappa and C4-freeness cross at the same threshold in Note K's
    A_B family: kappa = |B|^2 counts the lines, and C4-freeness permits one.
    They measure the same integer. The coincidence is not evidence that a
    density statistic detects 4-cycles.
    """
    from math import isqrt

    from x2plus1.gaussian import UNITS, mul

    Q = 10**6
    for c in (1, 2, 3, 5, 7):
        n = isqrt(Q - c * c)
        assert abs(n * n / Q - (1 - c * c / Q)) < 2e-3       # kappa -> 1
        A = [(a, c) for a in range(1, isqrt(40000 - c * c) + 1)]
        assert len(A) > 150, (c, len(A))     # floor: absurd at zero, so the
        seen: dict[tuple[int, int], tuple[int, int]] = {}   # C4 half cannot
        pairs = 0                                           # pass vacuously
        for i, z in enumerate(A):
            for j in range(i, len(A)):
                pr = mul(z, A[j])
                for u in UNITS:
                    k = mul(u, pr)
                    assert seen.get(k, (i, j)) == (i, j), (c, k)
                seen[pr] = (i, j)
                pairs += 1
        assert pairs > 15000, (c, pairs)


def test_two_lines_always_admit_a_four_cycle():
    """And the moment there are two lines, the freedom is back.

    Checked on pairs that avoid both artefacts Note K identified -- no c = 1,
    and neither c dividing the other -- so the cycle is not a dilation. The
    witness at (2,3) is (1+2i)(6+2i) = 2+14i = (2+2i)(4+3i).
    """
    from math import isqrt

    from x2plus1.gaussian import UNITS, mul

    assert mul((1, 2), (6, 2)) == (2, 14) == mul((2, 2), (4, 3))
    for c1, c2 in ((2, 3), (2, 5), (3, 5), (3, 7), (5, 7), (4, 6)):
        A = [(a, c) for c in (c1, c2)
             for a in range(1, isqrt(40000 - c * c) + 1)]
        seen: dict[tuple[int, int], tuple[int, int]] = {}
        found = False
        for i, z in enumerate(A):
            for j in range(i, len(A)):
                pr = mul(z, A[j])
                for u in UNITS:
                    k = mul(u, pr)
                    if seen.get(k, (i, j)) != (i, j):
                        found = True
                seen[pr] = (i, j)
            if found:
                break
        assert found, (c1, c2)


def test_two_points_destroy_c4_freeness_without_moving_kappa():
    """kappa cannot see C4-freeness even AT the threshold Note K called sharp.

    Adjoin exactly two Gaussian integers to the line: A = {x+i : x <= X} u
    {2+2i, 4+2i}. Then kappa = (X+2)^2/(X^2+1) -> 1, indistinguishable from the
    pure line, while

        (1+i)(4+2i) = 2+6i = (2+i)(2+2i)

    is a 4-cycle. So the A_B family's coincidence of thresholds is a property of
    that PARAMETERISATION, not of kappa: O(1) elements flip C4-freeness at fixed
    kappa.

    Stated narrowly on purpose. This shows kappa cannot see the BINARY property.
    It does not show kappa fails to track the QUANTITY of 4-cycles -- one cycle
    moves max G from 1 to 2 and leaves mean G at O(1/X), and this repo's own
    measurements say mean G is the load-bearing statistic, not max G. The
    refinement is to Note K's "must not be demoted on these grounds", not to the
    Type II obstruction, which is about the whole graph.
    """
    from x2plus1.gaussian import UNITS, mul

    assert mul((1, 1), (4, 2)) == (2, 6) == mul((2, 1), (2, 2))
    for X in (10**3, 10**4, 10**5):
        Q = X * X + 1
        kappa = (X + 2) ** 2 / Q
        assert 1.0 < kappa < 1.0 + 5.0 / X          # -> 1, as for the bare line
        assert abs(kappa - X * X / Q) < 5.0 / X     # and indistinguishable from it
    A = [(x, 1) for x in range(1, 200)] + [(2, 2), (4, 2)]
    seen: dict[tuple[int, int], tuple[int, int]] = {}
    cycles = 0
    for i, z in enumerate(A):
        for j in range(i, len(A)):
            pr = mul(z, A[j])
            for u in UNITS:
                if seen.get(mul(u, pr), (i, j)) != (i, j):
                    cycles += 1
            seen[pr] = (i, j)
    assert cycles > 0


def test_odd_squarefree_M_always_has_a_prime_not_dividing_V():
    """The pigeonhole that removes O.7's primality hypothesis.

    O.7 needs a prime p | M with p not dividing V, so that p | A_V and p | B_V
    cannot both hold (they give p | A_V - B_V = 2Va, and p is odd with
    gcd(a,M) = 1). For M an odd PRIME that is immediate from |V| < M. For M odd
    SQUAREFREE it is still immediate: if every p | M divided V then their
    product, which is M, would divide V, and 0 < |V| < 0.40825 M forbids it.

    So the hypothesis is free on all odd squarefree M, not just primes -- 29.0%
    of realised close pairs at X = 6000 rather than 12.0%. Non-squarefree M
    needs rad(M) not dividing V, which is not automatic (rad(M) can be far below
    |V|'s ceiling) but held on 77/77 realised in-window pairs.
    """
    from math import gcd, isqrt

    from sympy import factorint

    from x2plus1.polyseq import ratio_classes

    checked = squarefree = 0
    for (a, b), ms in ratio_classes(3000).items():
        M = b - a
        if M < 2 or M % 2 == 0:
            continue
        ms = sorted(ms)
        rad = 1
        for p in factorint(M):
            rad *= p
        for i in range(len(ms) - 1):
            if ms[i + 1] >= 2 * ms[i]:
                continue
            X1, Y1 = isqrt(a * ms[i] - 1), isqrt(b * ms[i] - 1)
            X2, Y2 = isqrt(a * ms[i + 1] - 1), isqrt(b * ms[i + 1] - 1)
            if X1 < 1:
                continue
            V = abs(X1 * Y2 - X2 * Y1)
            assert 0 < V < M                      # the in-window bound
            assert gcd(a, M) == 1                 # needed for p | 2Va => p | V
            checked += 1
            if rad == M:                          # squarefree: forced
                squarefree += 1
                assert any(V % p for p in factorint(M)), (a, b, M, V)
            assert V % rad or rad < M             # rad | V only if M is not squarefree
    assert checked > 50 and squarefree > 20


def test_p_divides_V_exactly_when_the_local_subcase_agrees():
    """p | V <=> the two moduli sit in the SAME local subcase at p.

    For M odd squarefree and p | M, with gcd(a,M) = 1:

      aY^2 - bX^2 = M and b = a+M give a(Y^2 - X^2) = 0 mod p, so p | S or p | T
      where S = X+Y, T = X-Y. Not both: p | S and p | T give p | 2X and p | 2Y,
      so p | X (p odd), so am = X^2+1 = 1 mod p and p does not divide m; then
      S T = -M m forces v_p(S) + v_p(T) = 1 + 0 = 1, while both being positive
      makes it >= 2. So EXACTLY one holds, and p does not divide X.

      Write Y = eps X mod p, eps = -1 in subcase p | S and +1 in p | T. Then
      V = X_i Y_j - X_j Y_i = X_i X_j (eps_j - eps_i) mod p. Same subcase gives
      V = 0; different gives V = +-2 X_i X_j, nonzero since p is odd and p does
      not divide either X.

    So Prop O.6's alternation and the gcd(V,M) = 1 hypothesis are the SAME
    statement, not two independent ones: the subcase flips at a step precisely
    when p does not divide that step's V.

    Consequence, and it costs one hypothesis less than Theorem O.8 assumes: if
    gcd(V_12, M) = gcd(V_23, M) = 1 then the subcase differs across 1-2 and
    across 2-3, so 1 and 3 AGREE, so every p | M divides V_13, so M | V_13 for M
    squarefree -- contradicting 0 < |V_13| < M. Two consecutive steps suffice;
    the third is implied.
    """
    from math import isqrt
    from sympy import factorint
    from x2plus1.polyseq import ratio_classes

    tot = same_div = diff_ndiv = 0
    for (a, b), ms in ratio_classes(3000).items():
        M = b - a
        if M < 3 or M % 2 == 0:
            continue
        f = factorint(M)
        if any(e > 1 for e in f.values()):
            continue
        ms = sorted(ms)
        dat = [(isqrt(a * m - 1), isqrt(b * m - 1)) for m in ms]
        for i in range(len(ms) - 1):
            Xi, Yi = dat[i]
            Xj, Yj = dat[i + 1]
            if Xi < 1:
                continue
            V = Xi * Yj - Xj * Yi
            for p in f:
                assert Xi % p and Xj % p                 # p never divides X
                si, ti = (Xi + Yi) % p == 0, (Xi - Yi) % p == 0
                sj, tj = (Xj + Yj) % p == 0, (Xj - Yj) % p == 0
                assert si != ti and sj != tj             # exactly one subcase
                tot += 1
                if si == sj:
                    assert V % p == 0, (a, b, p)
                    same_div += 1
                else:
                    assert V % p, (a, b, p)
                    diff_ndiv += 1
    assert same_div > 10 and diff_ndiv > 100 and tot > 500


def test_O8_hypothesis_is_proved_below_the_plucker_threshold():
    """O.8's open hypothesis gcd(V,M) = 1 is a THEOREM when M/sqrt(D) is small.

    Three ingredients, all proved, no measured input:

    1. The |V| bound. From V W = M(m_i - m_j) with W = X_j Y_i + X_i Y_j, and
       Y > X sqrt(b/a) since Y^2 = (b/a)(X^2+1) - 1, we get W > 2 X_i X_j
       sqrt(b/a) and hence |V| < (M/2 sqrt D)(R - 1/R) with R = X_j/X_i. In a
       window R^2 < r := 2 + 1/X_i^2, so |V| < (M/2 sqrt D)(sqrt r - 1/sqrt r).

    2. V is EVEN whenever M is odd. M odd means a, b are not both = 2 mod 4, so:
       if a and b are both odd then m must be odd (m even would force X and Y
       both odd, making M = b - a even), so X^2 = am-1 and Y^2 = bm-1 are both
       even and X, Y are both even; if a = 2 mod 4 and b is odd then m is odd, X
       is odd and Y is even. Either way X_i Y_j - X_j Y_i is even.

    3. V != 0, since V = 0 forces the two solutions proportional.

    So |V| < 4 gives |V| = 2, and gcd(V,M) = gcd(2,M) = 1 for M odd. And
    |V| >= 4 requires M/sqrt(D) > 8/(sqrt r - 1/sqrt r) -- which is exactly the
    Plucker threshold, 4 sqrt 3 = 6.9282 at X_i = 1 rising to 8 sqrt 2 = 11.3137.

    Below that threshold O.8 applies unconditionally: 95 of the in-window M-odd
    pairs at X = 4000, 47.0% of all in-window pairs.
    """
    from math import gcd, isqrt, sqrt

    from x2plus1.polyseq import ratio_classes

    below = odd_below = 0
    for (a, b), ms in ratio_classes(3000).items():
        M = b - a
        if M < 3:
            continue
        D = a * b
        ms = sorted(ms)
        dat = [(isqrt(a * m - 1), isqrt(b * m - 1)) for m in ms]
        for i in range(len(ms) - 1):
            Xi, Yi = dat[i]
            Xj, Yj = dat[i + 1]
            if Xi < 1 or ms[i + 1] >= 2 * ms[i]:
                continue
            V = Xi * Yj - Xj * Yi
            W = Xj * Yi + Xi * Yj
            assert V * W == M * (ms[i] - ms[i + 1])          # the identity
            assert V != 0
            if M % 2:
                assert V % 2 == 0, (a, b, M, V)              # parity, for M odd
            r = 2 + 1.0 / (Xi * Xi)
            assert abs(V) < (M / (2 * sqrt(D))) * (sqrt(r) - 1 / sqrt(r)) + 1e-9
            if M / sqrt(D) <= 8.0 / (sqrt(r) - 1 / sqrt(r)):
                below += 1
                assert abs(V) == 2, (a, b, M, V)             # forced
                if M % 2:
                    odd_below += 1
                    assert gcd(V, M) == 1                    # therefore proved
    assert below > 100 and odd_below > 40


def test_the_sign_argument_needs_only_an_odd_prime_exactly_dividing_M():
    """O.9 generalises off M odd squarefree, and reaches M even.

    Nothing in the sign argument is about M. It is about a single odd prime p
    with p || M: then Y^2 == X^2 mod p, p does not divide X (else p | S and
    p | T, while S T = -M m with v_p(M) = 1 forces v_p(S) + v_p(T) = 1), so each
    solution carries sigma = +-1 with Y == sigma X, and p | V_ij iff
    sigma_i = sigma_j. Three signs in {+-1} cannot be pairwise distinct, so p
    divides one of V_12, V_23, V_13.

    Let M_1 = product of the odd primes p with p || M. The V's are divisible
    accordingly, M_1 is squarefree, so M_1 | V_12 V_23 V_13, and |V| < M/sqrt(3D)
    gives M_1 < M^3/(3D)^{3/2}, i.e.

        a window holds three moduli only if  3ab < (M^3/M_1)^{2/3}.

    For M odd squarefree M_1 = M and this is O.9's 3ab < M^{4/3}. It is silent
    only when M_1 = 1 -- M a power of two times a powerful odd part -- which is
    1.02% of classes at X = 3000, against 74.56% with M even that O.9 as stated
    does not reach. 95.68% of all classes are excluded outright.

    Checked here on M EVEN, which is the new range.
    """
    from math import isqrt

    from sympy import factorint

    from x2plus1.polyseq import ratio_classes

    checked = 0
    for (a, b), ms in ratio_classes(2000).items():
        M = b - a
        if M < 4 or M % 2:                       # M EVEN only
            continue
        odd_exact = [int(p) for p, e in factorint(M).items() if int(p) != 2 and int(e) == 1]
        if not odd_exact:
            continue
        ms = sorted(ms)
        dat = [(isqrt(a * m - 1), isqrt(b * m - 1)) for m in ms]
        for i in range(len(ms) - 1):
            Xi, Yi = dat[i]
            Xj, Yj = dat[i + 1]
            if Xi < 1:
                continue
            V = Xi * Yj - Xj * Yi
            for p in odd_exact:
                assert Xi % p and Xj % p                      # p never divides X
                si = (Xi + Yi) % p == 0
                ti = (Xi - Yi) % p == 0
                sj = (Xj + Yj) % p == 0
                tj = (Xj - Yj) % p == 0
                assert si != ti and sj != tj                  # sign well defined
                assert (V % p == 0) == (si == sj), (a, b, p)  # p | V iff signs agree
                checked += 1
    assert checked > 200


def test_the_sign_arguments_blind_spot_is_enriched_among_rich_classes():
    """M = 2^e carries no odd prime, so the sign argument says nothing there --
    and those classes are exactly the modulus-rich ones.

    The sign needs an odd p | M. When M is a pure power of two there is none, at
    any exponent, so O.9 and its generalisation are silent on the whole class.
    That looks negligible by class count and is not:

        X = 3000    all classes  0.013%     >=3 moduli  8.3%    >=5 moduli  50.0%
        X = 6000    all classes  0.004%     >=3 moduli  6.2%    >=5 moduli  33.3%

    a 600x to 4000x enrichment, stable across a doubling of X. The single
    richest class in the data -- (1,5), M = 4, eight shared moduli 2, 10, 65,
    442, 3026, 20737, 142130, 974170 -- is one of them, and so are (1,17) and
    (1,65). These are b = 2^e + 1 with a = 1: the Pell chains, which are the
    structurally deepest configurations in the problem.

    So the blind spot is not a small uniform residue. It is concentrated on the
    configurations where a triple is most likely to be found if one exists.
    """
    from x2plus1.polyseq import ratio_classes

    rows = [(len(ms), (b - a) & (b - a - 1) == 0)
            for (a, b), ms in ratio_classes(3000).items() if b - a >= 3]
    base = sum(1 for n, p in rows if p) / len(rows)
    rich = [r for r in rows if r[0] >= 5]
    rich_rate = sum(1 for n, p in rich if p) / len(rich)
    assert base < 0.001                       # negligible by class count
    assert rich_rate > 0.3                    # dominant among the rich ones
    assert rich_rate / base > 500             # and the enrichment is enormous
    mid = [r for r in rows if r[0] >= 3]
    assert sum(1 for n, p in mid if p) / len(mid) > 0.05


def test_the_VW_identity_generalises_with_a_factor_c_squared():
    """V W = c^2 M (m_i - m_j) for x^2 + c^2, and O.12's proof does NOT survive it.

    Derivation, done before measuring. With a m = X^2 + c^2 and b m = Y^2 + c^2,

        V W = X_i^2 Y_j^2 - X_j^2 Y_i^2
            = (a m_i - c^2)(b m_j - c^2) - (a m_j - c^2)(b m_i - c^2)
            = c^2 (b - a)(m_i - m_j) = c^2 M (m_i - m_j),

    the c = 1 case being the identity Note O uses. Y > X sqrt(b/a) still holds
    (Y^2/X^2 = (bm - c^2)/(am - c^2) > b/a exactly when b > a), so the same route
    gives |V| < c^2 (M/2 sqrt D)(R - 1/R) -- a factor c^2 WEAKER.

    So O.12's threshold scales as 1/c^2: at X_1 = 1 it is M/sqrt(D) > 1.7321/c^2,
    which drops below what a dyadic band supplies as soon as c >= 2. **The proof
    does not extend.** The conclusion appears to anyway -- banded cofactors share
    at most one in-window modulus at c = 2 and c = 3, measured to X = 3000 -- so
    what fails is the argument, not the fact.

    And the obvious repair fails too: the bound is SATURATED (max |V| divided by
    the bound is 1.0000, 3.9997, 8.9993 at c = 1,2,3), so it cannot be tightened,
    and min |V| is 2, 4, 6, 4, 6 at c = 1..5 -- not c^2, so no lower bound on |V|
    of that shape restores the threshold.
    """
    from math import gcd, isqrt
    from collections import defaultdict

    X = 700
    for c in (1, 2, 3):
        sq = [x * x + c * c for x in range(X + 1)]
        cls = defaultdict(set)
        for x in range(1, X + 1):
            for y in range(x + 1, X + 1):
                g = gcd(sq[x], sq[y])
                if g > 1:
                    a, b = sq[x] // g, sq[y] // g
                    if a < b:
                        cls[(a, b)].add(g)
        seen = 0
        for (a, b), ms in cls.items():
            M = b - a
            ms = sorted(ms)
            for i in range(len(ms) - 1):
                sqs = [a * ms[i], a * ms[i + 1], b * ms[i], b * ms[i + 1]]
                rt = [isqrt(v - c * c) for v in sqs]
                if any(r * r != v - c * c for r, v in zip(rt, sqs)) or rt[0] < 1:
                    continue
                Xi, Xj, Yi, Yj = rt[0], rt[1], rt[2], rt[3]
                V = Xi * Yj - Xj * Yi
                W = Xj * Yi + Xi * Yj
                assert V * W == c * c * M * (ms[i] - ms[i + 1]), (c, a, b)
                seen += 1
        assert seen > 20, (c, seen)


def test_doubly_dyadic_c4_freeness_fails_at_c_equals_six():
    """The Z[i] -> Z-banded transfer is NOT automatic: c = 6 refutes it.

    A_c = {a+ci} is C4-free over Z[i] for EVERY c (the line argument: the product
    and the sum of the two a's are both determined). But over Z, on the
    doubly-dyadic configuration, C4-freeness holds only for c in {1,2,3,4,5,7}
    and FAILS from c = 6 onward. Witness at c = 6, all four verified:

        cofactors (5, 8), u = 1.6 < 2      moduli 9 and 17, ratio 1.889 < 2
        5*9  = 45  = 3^2 + 6^2      8*9  = 72  = 6^2 + 6^2
        5*17 = 85  = 7^2 + 6^2      8*17 = 136 = 10^2 + 6^2

    The mechanism is visible in Z[i] and is exactly the Z[i]/Z gap:

        (3+6i)(10+6i) = -6 + 78i        (6+6i)(7+6i) = 6 + 78i

    **conjugate, not associate** -- so there is no Gaussian 4-cycle, while the
    norms coincide at 6120 and the rational cycle is real.

    So Theorem O.12 at c = 1 is not an instance of a general principle about
    lines. Over c = 1..20 the property holds at 1,2,3,4,5,7 and fails at the
    other fourteen, stable from X = 1500 to 3000 on the survivors.
    """
    from math import gcd, isqrt
    from collections import defaultdict

    from x2plus1.gaussian import UNITS, mul

    # the witness, term by term
    for m, cof, x in ((9, 5, 3), (9, 8, 6), (17, 5, 7), (17, 8, 10)):
        assert cof * m == x * x + 36, (m, cof, x)
    assert 8 / 5 < 2 and 17 / 9 < 2                 # doubly dyadic
    p1, p2 = mul((3, 6), (10, 6)), mul((6, 6), (7, 6))
    assert p1 == (-6, 78) and p2 == (6, 78)
    assert p1[0] ** 2 + p1[1] ** 2 == p2[0] ** 2 + p2[1] ** 2 == 6120
    assert not any(mul(u, p1) == p2 for u in UNITS)          # not associate
    assert any(mul(u, (p1[0], -p1[1])) == p2 for u in UNITS)  # but conjugate

    # A_6 really is C4-free over Z[i]
    A = [(a, 6) for a in range(1, 120)]
    assert len(A) > 100
    seen: dict[tuple[int, int], tuple[int, int]] = {}
    for i, z in enumerate(A):
        for j in range(i, len(A)):
            pr = mul(z, A[j])
            for u in UNITS:
                assert seen.get(mul(u, pr), (i, j)) == (i, j)
            seen[pr] = (i, j)

    # and the Z-side banded graph is not, at c = 6 but not at c = 5
    def banded_hits(c, X=700):
        sq = [x * x + c * c for x in range(X + 1)]
        cls = defaultdict(set)
        for x in range(1, X + 1):
            for y in range(x + 1, X + 1):
                g = gcd(sq[x], sq[y])
                if g > 1:
                    a, b = sq[x] // g, sq[y] // g
                    if a < b:
                        cls[(a, b)].add(g)
        assert len(cls) > 500, (c, len(cls))
        n = 0
        for (a, b), ms in cls.items():
            if b / a >= 2:
                continue
            ms = sorted(ms)
            n += sum(1 for i in range(len(ms) - 1)
                     if ms[i] > 1 and ms[i + 1] < 2 * ms[i])
        return n

    assert banded_hits(6) > 0, "c = 6 must have a doubly-dyadic 4-cycle"
    assert banded_hits(5) == 0, "c = 5 must not"


def test_four_consecutive_x_give_a_cycle_exactly_when_D_is_k2_plus_3k_plus_1():
    """Why x^2+1 escapes: its member of the generic family is the unit case.

    For f(x) = x^2 + D, four consecutive arguments k, k+1, k+2, k+3 satisfy

        (k^2+D)((k+3)^2+D) - ((k+1)^2+D)((k+2)^2+D) = 4(D - k^2 - 3k - 1)

    -- since k(k+3) and (k+1)(k+2) differ by 2, and the D-linear parts differ by
    4. So the product of the outer two equals the product of the inner two, i.e.
    a 4-cycle, EXACTLY when

        D = k^2 + 3k + 1:   D = 1, 5, 11, 19, 29, 41, 55, ...

    and the escapes are two, both special:

      k = 0, D = 1   values 1, 2, 5, 10 -- the first is the UNIT modulus, which
                     no Type II hypothesis admits. This is x^2+1.
      k = 1, D = 5   values 6, 9, 14, 21 -- cofactor ratio 1.5 but modulus ratio
                     14/6 = 2.333, so not doubly dyadic.
      k >= 2         both ratios below 2 and falling to 1: (1.333, 1.800) at
                     D = 11, (1.250, 1.571) at 19, (1.200, 1.444) at 29.

    So doubly-dyadic C4-freeness fails for an infinite explicit family of degree-2
    sequences, and x^2+1 is not merely a member that happens to survive -- it is
    the k = 0 member, whose cycle is degenerate for the same reason the unit
    cofactor is excluded everywhere else in this repo.
    """
    for k in range(0, 40):
        for D in range(1, 200):
            lhs = (k * k + D) * ((k + 3) ** 2 + D) \
                - ((k + 1) ** 2 + D) * ((k + 2) ** 2 + D)
            assert lhs == 4 * (D - k * k - 3 * k - 1), (k, D)

    seen_unit = seen_wide = seen_cycle = 0
    for k in range(0, 8):
        D = k * k + 3 * k + 1
        v = [(k + j) ** 2 + D for j in range(4)]
        assert v[0] * v[3] == v[1] * v[2], (k, v)        # the cycle, always
        cof, mod = v[1] / v[0], v[2] / v[0]
        if v[0] == 1:
            seen_unit += 1
            assert (k, D) == (0, 1)                      # only x^2+1
        elif mod >= 2:
            seen_wide += 1
            assert (k, D) == (1, 5)                      # only D = 5
        else:
            seen_cycle += 1
            assert cof < 2 and mod < 2                   # genuinely doubly dyadic
    assert (seen_unit, seen_wide, seen_cycle) == (1, 1, 6)


def test_c4_freeness_holds_at_the_B1_relevant_top_of_the_range():
    """`c4-free` says "at every split"; the named test stops at m < 10^5.

    (B1) forces M >= sqrt(x) = X, so the splits a Type II hypothesis actually
    uses are m >= X -- and at X = 4000 the values run to 1.6 x 10^7, so the four
    decade windows in test_bilinear cover only the bottom of the range. This
    extends the check to the top, which is the part that matters:

        [10^4, 10^5)   4394 rows, 573 cols, C4-free, max Gram 0
        [10^5, 10^6)   4393 rows,  74 cols, C4-free, max Gram 0
        [10^6, 10^7)   4392 rows,   8 cols, C4-free, max Gram 0

    The Gram is 0 rather than 1 up there because the cofactor side collapses --
    above m = X the cofactor n = (x^2+1)/m is below X, and few cofactors admit
    two moduli in one window at all. Which is the same observation as the mean-G
    decay, seen at the coarsest possible resolution: the range the sieve needs is
    the range where the graph has almost no edges to cancel over.

    Nothing was wrong here. The wording check that found exp09's anchoring asks
    whether the experiment quantifies over the same set as the statement; for
    `c4-free` the answer was "the proof does, the test samples", and this closes
    the sampling gap at the end that carries the argument.
    """
    from x2plus1.sequences import by_x_range
    from x2plus1.typeII import incidence, is_c4_free, max_offdiagonal_gram

    seq = by_x_range(4000)
    checked = 0
    for lo, hi in ((10**4, 10**5), (10**5, 10**6), (10**6, 10**7),
                   (10**7, 2 * 10**7)):
        C, *_ = incidence(seq, lo, hi)
        if not len(C.indices):
            continue
        assert is_c4_free(C), (lo, hi)
        assert max_offdiagonal_gram(C) <= 1, (lo, hi)
        checked += 1
    assert checked == 4, checked


def test_x2_plus_39_has_a_banded_triple_so_O2_is_special_to_D_equals_one():
    """Conjecture O.2's analogue is FALSE for x^2+39, in the strongest form.

        cofactors (5, 8)        ratio 1.6  -- one dyadic BAND
        moduli    8, 11, 15     15 < 16    -- one dyadic WINDOW

        5*8  =  40 = 1^2+39     8*8  =  64 = 5^2+39
        5*11 =  55 = 4^2+39     8*11 =  88 = 7^2+39
        5*15 =  75 = 6^2+39     8*15 = 120 = 9^2+39

    Three shared moduli in one window, with the two cofactors inside one band.
    That refutes the analogue of Conjecture O.2 (no window holds three) AND of
    Theorem O.12 (banded cofactors share at most one) simultaneously, for D = 39.

    Over D <= 60 there are seven such unit-free triples -- D = 29, 39, 42, 44, 52,
    53, 59 -- and D = 1 is not among them. So the triple question, like the
    4-cycle question, has an answer special to x^2+1 rather than a general one
    about degree-2 sequences.

    This does NOT refute O.2 or O.12 for x^2+1. Both remain exactly as they were:
    O.12 proved, O.2 open with no counterexample to X = 8000. What it removes is
    any reading of them as instances of something general -- the same correction
    the D = k^2+3k+1 family makes for the 4-cycle, one level up.
    """
    from math import isqrt

    for cof in (5, 8):
        for m in (8, 11, 15):
            v = cof * m
            x = isqrt(v - 39)
            assert x * x + 39 == v, (cof, m, v)
    assert 8 / 5 < 2                     # cofactors banded
    assert 15 < 2 * 8                    # moduli in one window

    # and the same configuration does not occur for D = 1 at this size
    from math import gcd
    from collections import defaultdict

    X = 600
    vals = [x * x + 1 for x in range(1, X + 1)]
    cls = defaultdict(set)
    for i in range(len(vals)):
        for j in range(i + 1, len(vals)):
            g = gcd(vals[i], vals[j])
            if g > 1:
                a, b = vals[i] // g, vals[j] // g
                if a < b:
                    cls[(a, b)].add(g)
    assert len(cls) > 200, len(cls)
    for (a, b), ms in cls.items():
        if a < 2:
            continue
        ms = sorted(m for m in ms if m > 1)
        for i in range(len(ms) - 2):
            assert ms[i + 2] >= 2 * ms[i], (a, b, ms[i:i + 3])


def test_the_whole_note_O_apparatus_generalises_with_M_replaced_by_M_times_D():
    """Why x^2+1 is special: it is the D = 1 end where every bound is tightest.

    For f(x) = x^2 + D with a m = X^2 + D and b m = Y^2 + D:

        b(X^2+D) = abm = a(Y^2+D)   =>   a Y^2 - b X^2 = (b-a) D = M D

    so the invariant Note O calls M is really **M D**, and every bound built on
    it weakens by a factor of D. In particular:

        invariant   a Y^2 - b X^2 = M D
        identity    V W = D M (m_i - m_j)          (0 failures / 5354 pairs)
        O.9 bound   3ab < (M D)^{4/3}

    That explains every D-result at once rather than leaving them as a list of
    coincidences. At cofactors (5,8), M = 3:

        D = 39:  3ab = 120 < (117)^{4/3} = 572   -- permitted, AND IT OCCURS
        D =  1:  3ab = 120 vs (3)^{4/3} = 4.33   -- forbidden, and none occurs

    Same bound; D is the whole difference. It also subsumes the c-family, where
    D = c^2 and the |V| bound weakens by exactly c^2, and the 4-cycle family
    D = k^2+3k+1.

    So x^2+1 is not special in an arbitrary way. It is the extreme member of a
    one-parameter family, the end at which every bound in the Note O apparatus is
    at its tightest -- which is why the conclusions hold there and nowhere else.
    """
    from math import gcd, isqrt
    from collections import defaultdict

    X = 400
    checked = 0
    for D in (1, 2, 5, 11, 39):
        vals = [x * x + D for x in range(1, X + 1)]
        cls = defaultdict(set)
        for i in range(len(vals)):
            for j in range(i + 1, len(vals)):
                g = gcd(vals[i], vals[j])
                if g > 1:
                    a, b = vals[i] // g, vals[j] // g
                    if a < b:
                        cls[(a, b)].add(g)
        assert len(cls) > 100, (D, len(cls))
        for (a, b), ms in cls.items():
            M = b - a
            ms = sorted(ms)
            for i in range(len(ms) - 1):
                q = [a * ms[i], a * ms[i + 1], b * ms[i], b * ms[i + 1]]
                r = [isqrt(v - D) for v in q]
                if any(t * t != v - D for t, v in zip(r, q)) or r[0] < 1:
                    continue
                Xi, Xj, Yi, Yj = r
                assert a * Yi * Yi - b * Xi * Xi == M * D, (D, a, b, ms[i])
                V = Xi * Yj - Xj * Yi
                W = Xj * Yi + Xi * Yj
                assert V * W == D * M * (ms[i] - ms[i + 1]), (D, a, b)
                checked += 1
    assert checked > 500, checked

    # the bound at (5,8) separates D = 39 from D = 1
    a, b, M = 5, 8, 3
    assert 3 * a * b < (M * 39) ** (4 / 3)      # permitted at D = 39
    assert 3 * a * b > (M * 1) ** (4 / 3)       # forbidden at D = 1


def test_the_invariant_is_M_times_f_of_zero_with_a_leading_coefficient_caveat():
    """The general form, and the one prediction that failed refining it.

    For f(x) = k x^d + D with D = f(0), a m = f(X) and b m = f(Y) give

        b f(X) = abm = a f(Y)  =>  k (a Y^d - b X^d) = (b-a) D = M D

    so the axis is **f(0)**, and every bound weakens by D. Predicted: f(0) = 1
    should be as tight as x^2+1, f(0) = 39 as loose as x^2+39. Measured at
    X = 1200, banded max Gram and unit-free triples:

        x^2+1, x^2+x+1, 2x^2+1, x^3+1   f(0)=1    max 1, no triple   as predicted
        x^2+39, x^2+x+39                f(0)=39   max 2, triple      as predicted
        2x^2+39                         f(0)=39   max 1, NO triple   **fails**

    The failure is the refinement. k(aY^d - bX^d) = M D forces **k | M D**, so at
    k = 2 with D = 39 odd, M must be EVEN -- and it is, for every one of 45,289
    classes, with the invariant holding over 45,459 solutions. A non-monic f can
    therefore be tighter than f(0) alone predicts, because the leading
    coefficient imposes a divisibility that thins the class population.

    So: the axis is f(0); the leading coefficient is a second, tightening
    parameter. x^2+1 is at the tight end of the first with nothing to add on the
    second.
    """
    from math import gcd, isqrt
    from collections import defaultdict

    X = 500
    vals = [2 * x * x + 39 for x in range(1, X + 1)]
    cls = defaultdict(set)
    for i in range(len(vals)):
        for j in range(i + 1, len(vals)):
            g = gcd(vals[i], vals[j])
            if g > 1:
                a, b = vals[i] // g, vals[j] // g
                if a < b:
                    cls[(a, b)].add(g)
    assert len(cls) > 1000, len(cls)
    checked = 0
    for (a, b), ms in cls.items():
        M = b - a
        assert M % 2 == 0, (a, b, M)              # forced by 2 | 39 M
        for m in ms:
            if (a * m - 39) % 2 or (b * m - 39) % 2:
                continue
            Xq, Yq = (a * m - 39) // 2, (b * m - 39) // 2
            Xv, Yv = isqrt(Xq), isqrt(Yq)
            if Xv * Xv != Xq or Yv * Yv != Yq:
                continue
            assert 2 * (a * Yv * Yv - b * Xv * Xv) == 39 * M, (a, b, m)
            checked += 1
    assert checked > 500, checked


def test_tau_moves_between_orbits_and_epsilon_within_them():
    """The bridge between Note L's spacing and Note O's multiplier.

    Both notes act on the same solution set of a Y^2 - b X^2 = M and neither
    relates its group to the other's. They are different actions:

      Note L's eps -- the fundamental automorph, u^2 - D v^2 = 1 -- moves WITHIN
      an orbit, and Prop L.1's spacing m'/m -> eps^2 >= phi^4 = 6.854 is why a
      window holds at most one member of each orbit.

      Note O's tau_k -- the multiplier, U^2 = M^2 + 4k^2 D -- moves BETWEEN
      orbits, and tau_1^2 can be well below 2, which is exactly how two moduli
      land in one window.

    At (a,b) = (1,41), the pair Note L records as its windowed witness:

        eps = 2049 + 320 sqrt 41 = 4098,  so within-orbit m'/m ~ eps^2 = 1.7e7
        tau_1 = (42 + 2 sqrt 41)/40 = 1.37016,  tau_1^2 = 1.87733
        observed 1370/730 = 1.87671

    tau_1^2 matches the observed ratio to four places (the gap is the finite "+1"
    correction), while eps^2 is seven orders larger. So the two moduli in that
    window are in DIFFERENT orbits, brought together by tau and not by eps --
    and the windowed Gram entry counts orbits that tau reaches inside one window.
    Conjecture O.2 is the statement that it never reaches three.
    """
    from math import isqrt, sqrt

    a, b = 1, 41
    M, D = b - a, a * b
    u, v = 2049, 320
    assert u * u - D * v * v == 1                      # fundamental automorph
    eps = u + v * sqrt(D)
    assert eps ** 2 > 1e7                              # within-orbit: enormous

    t = M * M + 4 * D
    U = isqrt(t)
    assert U * U == t and U == 42                      # fundamental multiplier
    tau2 = ((U + 2 * sqrt(D)) / M) ** 2
    assert abs(tau2 - 1.87733) < 1e-5                  # between-orbit: under 2
    assert abs(tau2 - 1370 / 730) < 1e-3               # and it is the observed ratio

    for m, x in ((730, 27), (1370, 37)):               # both really are moduli
        assert m == x * x + 1
        y = isqrt(b * m - 1)
        assert y * y + 1 == b * m


def test_the_chain_threshold_is_four_root_two_plus_root_thirty_three_squared():
    """A second in-window multiplier needs b/a > (4 sqrt2 + sqrt33)^2 = 129.9923.

    tau_k^2 < 2 requires k < 0.17678 M/sqrt(D) asymptotically, so k >= 2 needs
    M/sqrt(D) > 8 sqrt2 = 11.3137 -- the same constant as O.12's asymptotic bound
    and the corrected Plucker value, since it is |V| >= 4 read as k >= 2. With
    M/sqrt(D) = (u-1)/sqrt(u) for u = b/a, solving v^2 - 8sqrt2 v - 1 = 0 at
    v = sqrt(u) gives v = 4 sqrt2 + sqrt33 and

        a CHAIN is possible only for  u > (4 sqrt2 + sqrt33)^2 = 129.9923

    against O.4's asymptotic TRIPLE threshold of 133.8748. The chain threshold
    sits 3.88 below, which it must: a triple needs a chain and something more.

    And the two requirements pull in opposite directions, which is the mechanism
    behind the emptiness. A chain needs u > 130; but the maximum modulus count
    over all classes falls with u -- 8 at u in [2,10), 6 at [10,100), 4 at
    [100,1000), 3 above 1000 -- so the range where a chain is possible is the
    range where the moduli to use it are scarcest. At X = 3000 the 43
    chain-admitting classes have at most two moduli, against the three a triple
    needs.
    """
    from math import sqrt

    v = 4 * sqrt(2) + sqrt(33)
    assert abs(v * v - 129.9923) < 1e-3
    assert abs((v * v - 1) / v - 8 * sqrt(2)) < 1e-9      # v solves the equation
    assert v * v < 133.8748                               # chain before triple
    assert 133.8748 - v * v < 4                           # and only just

    # the constant is O.12's, i.e. |V| >= 4 read as k >= 2
    assert abs(8 * sqrt(2) - 11.3137) < 1e-4


def test_all_the_window_thresholds_are_one_formula_in_V():
    """The pair and chain thresholds are the same expression at |V| = 2 and 4.

    |V| < (M/2 sqrt D)(R - 1/R) with R^2 < 2 gives |V| < 0.35355 M/sqrt(D), so
    |V| >= V0 requires M/sqrt(D) > 2 sqrt2 V0. Converting with
    M/sqrt(D) = (u-1)/sqrt(u) and solving v^2 - 2 sqrt2 V0 v - 1 = 0 at v = sqrt u:

        u > (sqrt2 V0 + sqrt(2 V0^2 + 1))^2

    which is one formula for the whole table:

        V0 = 2   M/sqrt D > 4 sqrt2  = 5.6569    u > 33.9706  = (1+sqrt2)^4
        V0 = 4   M/sqrt D > 8 sqrt2  = 11.3137   u > 129.9923 = (4sqrt2+sqrt33)^2
        V0 = 6                        16.9706         289.9966
        V0 = 8                        22.6274         513.9981

    So the doubling 4 sqrt2 -> 8 sqrt2 between the pair and chain thresholds is
    exactly |V| >= 2 -> |V| >= 4, and (1+sqrt2)^2 = 2 sqrt2 + 3 = sqrt2*2 +
    sqrt(9) is the V0 = 2 case of sqrt2 V0 + sqrt(2 V0^2 + 1).

    Expanding, u = 4 V0^2 + 1 + 2 sqrt2 V0 sqrt(2 V0^2 + 1) -> **8 V0^2 + 2**
    from below, with the gap falling 0.029, 0.008, 0.003, 0.002.
    """
    from math import sqrt

    def thresh(V0):
        return (sqrt(2) * V0 + sqrt(2 * V0 * V0 + 1)) ** 2

    assert abs(thresh(2) - (1 + sqrt(2)) ** 4) < 1e-9      # the pair threshold
    assert abs(thresh(2) - 33.9706) < 1e-3
    assert abs(thresh(4) - (4 * sqrt(2) + sqrt(33)) ** 2) < 1e-9   # the chain
    assert abs(thresh(4) - 129.9923) < 1e-3
    assert abs(sqrt(2) * 2 + sqrt(9) - (1 + sqrt(2)) ** 2) < 1e-12

    prev = 1.0
    for V0 in (2, 4, 6, 8):
        u = thresh(V0)
        gap = (8 * V0 * V0 + 2) - u
        assert 0 < gap < prev                              # approached from below
        prev = gap
        assert abs((u - 1) / sqrt(u) - 2 * sqrt(2) * V0) < 1e-9   # solves it


def test_kappa_is_blind_to_the_D_axis_which_decides_everything():
    """The strongest form of "kappa cannot see the obstruction".

    For x^2 + D the sequence has |A| = X and Q = X^2 + D, so

        kappa = X^2/(X^2 + D) -> 1  for EVERY fixed D.

    At X = 10^4 the whole family sits within 4 x 10^-7 of 1: kappa = 0.999999990
    at D = 1 and 0.999999610 at D = 39, a spread in the ninth decimal. Meanwhile
    D decides the structure completely -- D = 1, 2 hold unconditionally, D = 4
    holds on parity, and D = 6, 11, 19, 36, 39 fail with explicit witnesses,
    D = 39 with a banded TRIPLE.

    So an entire one-parameter family has kappa -> 1 throughout and splits into
    proved-holds and proved-fails. That is stronger than the two earlier
    demonstrations: "kappa counts lines" explains why the A_B threshold
    coincidence carries no information, and "two points flip C4-freeness at fixed
    kappa" needs an O(1) perturbation of the sequence. This one needs no
    perturbation at all -- these are natural sequences, and the parameter kappa
    is blind to is the parameter that decides the answer.

    Found by placing two finished results next to each other, which is the whole
    operation: the D axis and the kappa formula were both already recorded.
    """
    for X in (10**3, 10**4):
        kappas = {D: X * X / (X * X + D) for D in (1, 2, 4, 6, 11, 19, 36, 39)}
        assert all(k > 0.9999 for k in kappas.values())       # all essentially 1
        spread = max(kappas.values()) - min(kappas.values())
        assert spread < 4e-5                                   # and indistinguishable
        if X == 10**4:
            assert spread < 4e-7                               # ninth decimal
        assert kappas[1] > kappas[39]                          # ordered, but barely
    # at X = 1e4 the spread is in the ninth decimal
    X = 10**4
    assert abs(X * X / (X * X + 1) - 0.999999990) < 1e-9
    assert abs(X * X / (X * X + 39) - 0.999999610) < 1e-9


def test_the_D_reach_has_two_versions_and_D_equals_eight_is_the_crossover():
    """D <= 4 for all X_1; D <= 7 asymptotically; D = 8 exactly at the boundary.

    With the invariant M*D, the threshold M/sqrt(ab) > 2 sqrt2 V becomes
    M*D/sqrt(ab) > 2 sqrt2 V, i.e. (u-1)/sqrt(u) > 2 sqrt2 V / D -- **divided by
    D**. A dyadic band supplies (u-1)/sqrt(u) < 1/sqrt2, so a banded pair needs
    D > 4V. That is the asymptotic form, from R^2 < 2.

    The worst-case form, from tau_V^2 < 3 at X_1 = 1, gives D > V sqrt6 instead.
    So there are two reaches and they differ:

        X_1 = 1, all X   |V| >= 1: D <= 2     |V| >= 2: D <= 4
        asymptotic       |V| >= 1: D <= 3     |V| >= 2: D <= 7

    and **D = 8 is exactly the crossover**: (u-1)/sqrt(u) = 4 sqrt2 / 8 =
    1/sqrt2 at u = 2 on the nose.

    That reconciles the measurements. D = 5, 6, 7 are asymptotically protected
    but not protected at small X_1, which is precisely why they hold to X = 8000
    without being proved -- a failure there would have to come from X_1 small.
    D = 8, 9, 10 are permitted by both forms and unfallen: the
    necessary-not-sufficient gap again. D = 11 is the first observed failure and
    its threshold u_0 = 1.6632 sits well inside a band.
    """
    from math import sqrt

    def u0(D, V=2):
        r = 2 * sqrt(2) * V / D
        return ((r + sqrt(r * r + 4)) / 2) ** 2

    # D = 8 is the LAST COVERED value, not the crossover: the threshold there is
    # 4 sqrt2/8 = 1/sqrt2 exactly, u0 = 2 exactly, and a band gives u < 2
    # STRICTLY -- so no banded u attains it. Note the float trap: u0(8) evaluates
    # to 1.9999999998, so a bare `< 2` test reports D = 8 as uncovered.
    assert abs(u0(8) - 2.0) < 1e-9                     # exactly 2, up to float
    for D in (5, 6, 7):
        assert u0(D) > 2, D                            # banded impossible
    for D in (9, 10, 11, 39):
        assert u0(D) < 2 - 1e-6, D                     # banded possible, strictly
    # and the first uncovered value is D = 9, witnessed at u = 1.9
    assert (1.9 - 1) / sqrt(1.9) > 2 * sqrt(2) * 2 / 9
    assert abs(u0(11) - 1.6632) < 1e-4
    assert abs(u0(39) - 1.1559) < 1e-4

    # the two reaches: worst case D <= V sqrt6, asymptotic D <= 4V (inclusive)
    assert int(1 * sqrt(6)) == 2 and int(2 * sqrt(6)) == 4      # worst case
    assert 4 * 1 == 4 and 4 * 2 == 8                            # asymptotic


def test_the_mobius_cancellation_is_blind_to_D_as_well():
    """Both analytic quantities this repo measures are blind to the D axis.

    kappa = X^2/(kX^2+D) -> 1/k, which cannot resolve D at all. And the Mobius
    side is no better: |sum_{x<=X} mu(x^2+D)| / sqrt(X) at X = 20000 and 40000 is

        D =  1  0.4950  0.2100   HOLDS (proved)
        D =  2  0.2546  0.4450   HOLDS (proved)
        D =  6  1.3506  0.9200   holds (asymptotically protected)
        D = 11  0.2687  0.0250   FAILS
        D = 39  1.5698  1.0800   FAILS, with a banded triple

    every value O(1) -- square-root cancellation uniformly in D -- and the
    ordering matching the structure at neither size: the two largest are D = 6,
    which holds, and D = 39, which fails worst.

    So the parameter that decides the C4 structure completely is invisible to the
    density statistic AND to the Mobius cancellation. Which is the sharpest form
    of the repo's own position: Note F's obstruction is arithmetic, and both
    analytic measures available here cannot see the arithmetic.

    Recorded at two sizes and five D as rigorous_finite. No law is fitted -- the
    point is the ABSENCE of a relation, and O(1) fluctuation is what square-root
    cancellation predicts for every D alike.
    """
    from sympy import factorint

    def mob(n):
        f = factorint(n)
        if any(e > 1 for e in f.values()):
            return 0
        return -1 if len(f) % 2 else 1

    from math import sqrt

    X = 4000
    vals = {}
    for D in (1, 2, 6, 11, 39):
        s = sum(mob(x * x + D) for x in range(1, X + 1))
        vals[D] = abs(s) / sqrt(X)
    assert all(v < 3 for v in vals.values()), vals        # O(1) for every D
    # and no ordering: the holds and fails interleave
    holds = [vals[1], vals[2], vals[6]]
    fails = [vals[11], vals[39]]
    assert max(holds) > min(fails), vals                  # they interleave
    assert len(vals) == 5


def test_the_analytic_and_structural_obstructions_peak_at_the_same_scale():
    """Note M's theta = 1/2 and Note L's Gram-mean minimum are the same place.

    Note M measures the mu-saving as Q^{(1/2-theta)/2}, exactly zero at
    theta = 1/2 -- so the cancellation available to a Type II estimate vanishes
    there. Note L measures the mean of G over cofactor bands as U-shaped with its
    minimum at N = 1.37 X, independently, from a divisor-built incidence table.

    Converting the second to Note M's coordinate: with m n = Q ~ X^2, a cofactor
    N = 1.37 X is a modulus m = Q/N, so

        theta = log_Q(m) = 0.48034, 0.48191, 0.48633, 0.48861
                at X = 3000, 6000, 1e5, 1e6  ->  1/2

    **The scale where no cancellation is available is the scale where there are
    fewest edges to cancel over.** Both are governed by the balanced split
    m = n = sqrt(Q): the saving exponent vanishes there by construction, and the
    Gram U-shape bottoms there for structural reasons. So the coincidence has a
    mechanism and is not a mystery -- but the two facts were measured by
    completely different routes, one analytic and one combinatorial, and neither
    note observes that they land together.
    """
    from math import log

    prev = 0.0
    for X in (3000, 6000, 10**5, 10**6):
        N = 1.37 * X
        Q = X * X + 1
        theta = log(Q / N) / log(Q)
        assert 0.47 < theta < 0.5, (X, theta)      # below 1/2 and rising
        assert theta > prev                         # monotone toward 1/2
        prev = theta
    assert abs(prev - 0.48861) < 1e-4               # and still short of it at 1e6


def test_the_D_failures_survive_both_variables_being_large():
    """The D-dependence is not an artefact of small cofactors or small moduli.

    Every failure witness found first had one variable tiny -- D = 11 at
    cofactors (3,4), D = 39 at (5,8) -- and a Type II split has BOTH large, so
    the natural worry is that the whole D axis is an artefact of the corner the
    hypothesis excludes. It is not. Requiring cofactors >= 200 AND moduli >= 200
    at X = 4000, four of D <= 40 still fail:

        D = 23  cofactors (1131, 1432) ratio 1.266   moduli (6672, 9617) 1.441
        D = 31  cofactors (1055, 1808) ratio 1.714   moduli ( 625, 1120) 1.792
        D = 35  cofactors (2249, 3756) ratio 1.670   moduli ( 459,  879) 1.915
        D = 39  cofactors ( 781, 1180) ratio 1.511   moduli ( 688,  880) 1.279

    all banded on both axes, all four products verified. **D = 1 is not among
    them.** The D = 39 case in full:

        781*688 = 537328 = 733^2+39      781*880 = 687280 = 829^2+39
       1180*688 = 811840 = 901^2+39     1180*880 = 1038400 = 1019^2+39

    So O.12's configuration -- both variables banded -- is the one in which the
    structure sees D, and the failures it admits at D > 1 are genuine Type II
    shapes rather than corner cases.
    """
    from math import isqrt

    cases = ((23, 1131, 1432, 6672, 9617), (31, 1055, 1808, 625, 1120),
             (35, 2249, 3756, 459, 879), (39, 781, 1180, 688, 880))
    for D, a, b, m1, m2 in cases:
        for cof in (a, b):
            for m in (m1, m2):
                v = cof * m
                x = isqrt(v - D)
                assert x * x + D == v, (D, cof, m)
        assert b / a < 2 and m2 < 2 * m1, D          # banded on both axes
        assert min(a, m1) >= 200, D                  # and both variables large
    assert 1 not in [c[0] for c in cases]


def test_the_pair_bound_is_sharp_to_a_third_of_a_percent():
    """O.12 is loose by 7.11x as stated and by 0.33% with the parity lemma.

    The extremal unit-free witness for x^2+1 is (37, 1261) sharing moduli 866 and
    1730, cofactor ratio u = 34.081081. Against the two thresholds:

        |V| >= 1, O.12 as stated   u > (5+sqrt21)/2 = 4.7913    ratio 7.1131
        |V| >= 2, the parity lemma u > (1+sqrt2)^4  = 33.9706   ratio 1.0033

    So the "7.11x loose" reading compares nature against the WEAKER form. With
    |V| >= 2 -- which holds, since V is even whenever M is odd -- **the bound is
    sharp to a third of a percent**.

    And the witness is a tau_1 step: (sqrt u + 1)/(sqrt u - 1) = 1.413402, whose
    square 1.997707 matches the observed modulus ratio 1730/866 = 1.997691 to
    five decimals. Its modulus ratio is within 0.12% of the window's own bound of
    2, which is why the cofactor ratio is nearly extremal -- the two are the same
    constraint seen on two axes.

    **The 0.33% is conditional and must not be quoted bare.** It is sharpness
    against the |V| >= 2 threshold, and |V| >= 2 binds only because every
    realised extremum measured is a tau_1 step -- measured absence over a finite
    range, not a theorem. The non-tau_1 case is the cross-orbit configuration
    multipliers do not predict, so the gap between O.12's 4.7913 and 33.9706 is
    NAMED, not closed.

    Worth stating against this repo's own "size bounds permit far more than
    occurs at every scale": **this one does not**. The three instances recorded
    there -- 39 of 60 admissible classes, the D = 9,10 strip, O.11's falling
    reach -- are all about configurations a bound ADMITS and nature declines. The
    pair bound is the opposite case, and it is the only one found so far.
    """
    from math import sqrt

    u = 1261 / 37
    assert abs(u - 34.081081) < 1e-5
    tau1 = (sqrt(u) + 1) / (sqrt(u) - 1)
    assert abs(tau1 ** 2 - 1730 / 866) < 1e-4        # the witness is a tau_1 step
    assert abs(tau1 ** 2 - 1.997707) < 1e-5
    assert 1730 / 866 < 2                            # and inside a window, barely

    weak = (5 + sqrt(21)) / 2                        # |V| >= 1
    strong = (1 + sqrt(2)) ** 4                      # |V| >= 2, parity
    assert abs(u / weak - 7.1131) < 1e-3
    assert abs(u / strong - 1.0033) < 1e-3
    assert u > strong                                # nature clears it, barely
