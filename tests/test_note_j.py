"""The two facts Note J's reduction rests on.

Note J turns the Type II sum into a Bombieri-Vinogradov statement for
mu(x^2+1) over arithmetic progressions. Two steps, both checked here:

1. The fibre {n : mn in A} is the arithmetic progression n_0 + Z*conj(m).
2. Up to the non-squarefree correction, summing mu over that fibre equals
   mu(m) times summing mu(x^2+1) over the residue class x == r_m (mod N(m)).
"""

import pytest

from x2plus1.factorization import roots_of_minus_one
from x2plus1.gaussian import conj, exact_div, factor_gauss, norm
from x2plus1.sequences import by_x_range
from x2plus1.typeII import divisors_in_norm_range, divisors_with_complement_mobius

SEQ = by_x_range(2000)


def _mobius_ideal(z):
    m = 1
    for _pi, e in factor_gauss(z):
        if e >= 2:
            return 0
        m = -m
    return m


def _fibres(seq):
    fib = {}
    for z, fac in seq:
        for m in divisors_in_norm_range(fac, 2, 10**9):
            fib.setdefault(m, []).append(exact_div(z, m))
    return fib


def test_fibres_are_arithmetic_progressions_with_difference_conj_m():
    """Im(mn) = 1 is a line, whose homogeneous solutions are n = t*conj(m).

    This is what makes the Type II sum a statement about progressions rather
    than about Gaussian divisors, and it is the whole of Note J's reduction.
    """
    checked = 0
    for m, ns in _fibres(SEQ).items():
        if len(ns) < 2:
            continue
        checked += 1
        base, cm = ns[0], conj(m)
        for n in ns[1:]:
            step = exact_div((n[0] - base[0], n[1] - base[1]), cm)
            assert step is not None and step[1] == 0, (m, n)
    assert checked > 200, f"only {checked} multi-element fibres; test is vacuous"


def test_fibre_length_matches_the_residue_class_count():
    """|{n : mn in A}| = #{x <= X : x == r_m (mod N(m))}."""
    X = 2000
    for m, ns in _fibres(SEQ).items():
        q = norm(m)
        r = next((rr for rr in roots_of_minus_one(q)
                  if exact_div((rr, 1), m) is not None), None)
        assert r is not None, m
        first = r if r else q
        expected = 0 if first > X else (X - first) // q + 1
        assert len(ns) == expected, (m, len(ns), expected)


def test_mobius_over_a_fibre_equals_the_progression_sum():
    """sum_{n : mn in A} mu(n) = mu(m) * sum_{x == r_m (N(m))} mu(x^2+1).

    Exact whenever every x+i in the fibre is squarefree as an ideal; the
    failures are exactly the non-squarefree ones, which is the correction term
    Note J carries explicitly.
    """
    X = 2000
    mu_a = {z[0]: _mobius_ideal(z) for z, _ in SEQ}
    lhs = {}
    for z, fac in SEQ:
        for m, mun in divisors_with_complement_mobius(fac, 2, 10**9):
            lhs[m] = lhs.get(m, 0) + mun

    agree = disagree = 0
    for m, val in lhs.items():
        q = norm(m)
        r = next((rr for rr in roots_of_minus_one(q)
                  if exact_div((rr, 1), m) is not None), None)
        assert r is not None
        rhs = _mobius_ideal(m) * sum(
            mu_a[x] for x in range(1, X + 1) if x % q == r % q
        )
        if val == rhs:
            agree += 1
        else:
            disagree += 1
            # every disagreement must be explained by a non-squarefree fibre
            assert any(mu_a[x] == 0 for x in range(1, X + 1) if x % q == r % q), m
    assert agree > 5 * disagree, f"{agree} agree vs {disagree} disagree -- too many failures"


@pytest.mark.parametrize("X", [200, 800])
def test_mobius_of_the_ideal_equals_mobius_of_the_norm(X):
    """mu_{Z[i]}((x+i)) = mu(x^2+1). Underpins the fast sieve in ``mobius``."""
    from x2plus1.mobius import mobius_x2plus1
    fast = mobius_x2plus1(X)
    for x in range(1, X + 1):
        assert _mobius_ideal((x, 1)) == fast[x], x
