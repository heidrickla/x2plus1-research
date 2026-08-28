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
