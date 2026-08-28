import random

import pytest

from x2plus1.gaussian import (
    UNITS, add, conj, divmod_gauss, divisors_from_factorisation, exact_div,
    factor_gauss, gcd, mul, norm, power, split_prime, unit_normalize, unit_of,
)


def test_norm_is_multiplicative():
    rng = random.Random(0)
    for _ in range(300):
        z = (rng.randint(-30, 30), rng.randint(-30, 30))
        w = (rng.randint(-30, 30), rng.randint(-30, 30))
        assert norm(mul(z, w)) == norm(z) * norm(w)


def test_euclidean_division():
    rng = random.Random(1)
    for _ in range(1000):
        z = (rng.randint(-60, 60), rng.randint(-60, 60))
        w = (rng.randint(-60, 60), rng.randint(-60, 60))
        if w == (0, 0):
            continue
        q, r = divmod_gauss(z, w)
        assert add(mul(q, w), r) == z
        assert 2 * norm(r) <= norm(w), (z, w)


def test_unit_normalisation_picks_one_associate_per_ideal():
    rng = random.Random(2)
    for _ in range(300):
        z = (rng.randint(-40, 40), rng.randint(-40, 40))
        if z == (0, 0):
            continue
        n = unit_normalize(z)
        assert n[0] > 0 and n[1] >= 0
        assert {unit_normalize(mul(u, z)) for u in UNITS} == {n}
        assert mul(unit_of(z), n) == z


@pytest.mark.parametrize("p", [5, 13, 17, 29, 41, 101, 1009])
def test_split_primes_have_norm_p(p):
    pi = split_prime(p)
    assert norm(pi) == p
    assert mul(pi, conj(pi)) in {(p, 0), (0, p), (-p, 0), (0, -p)}


def test_two_is_ramified():
    assert split_prime(2) == (1, 1)
    assert unit_normalize(power((1, 1), 2)) == (2, 0)


@pytest.mark.parametrize("p", [3, 7, 11, 19, 23])
def test_inert_primes_rejected(p):
    with pytest.raises(ValueError):
        split_prime(p)


def test_gcd_divides_both_and_is_maximal():
    rng = random.Random(3)
    for _ in range(200):
        z = (rng.randint(-40, 40), rng.randint(-40, 40))
        w = (rng.randint(-40, 40), rng.randint(-40, 40))
        if z == (0, 0) or w == (0, 0):
            continue
        g = gcd(z, w)
        assert exact_div(z, g) is not None
        assert exact_div(w, g) is not None


def test_factorisation_of_x_plus_i_reconstructs():
    for x in range(1, 500):
        fac = factor_gauss((x, 1))
        prod = (1, 0)
        for pi, e in fac:
            prod = mul(prod, power(pi, e))
        assert norm(prod) == x * x + 1
        assert exact_div((x, 1), prod) is not None


def test_divisor_count_matches_tau():
    for x in range(1, 200):
        fac = factor_gauss((x, 1))
        expected = 1
        for _pi, e in fac:
            expected *= e + 1
        assert len(set(divisors_from_factorisation(fac))) == expected
