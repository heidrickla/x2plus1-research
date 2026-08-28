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
