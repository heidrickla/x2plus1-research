"""Note L, machine-checked: the same question over Z, and over every degree.

The distinction this file exists to keep honest is that Note F's lemma is a
statement about Z[i] while the Type II hypotheses it is cited against are
statements about Z. If those two ever get conflated again, one of these fails.
"""

from math import isqrt

from x2plus1.polyseq import (
    PolySequence, evaluate, incidence, is_c4_free, ladder, max_offdiagonal_gram, rho,
)
from x2plus1.sequences import x2plus1_sequence
from x2plus1.typeII import incidence as gauss_incidence, max_offdiagonal_gram as gauss_gram


def test_the_rational_four_cycle_is_real():
    """The explicit counterexample to C4-freeness over Z. Note L.

    Four products, all of the form x^2+1, on two moduli and two cofactors.
    """
    n1, n2 = 1189, 71978
    for m, x1, x2 in [(65, 278, 2163), (109, 360, 2801)]:
        assert m * n1 == x1 * x1 + 1
        assert m * n2 == x2 * x2 + 1


def test_the_merged_row_is_where_the_cycle_comes_from():
    """65 carries four Gaussian ideals, 109 carries two: rows merge over Z."""
    assert rho((1, 0, 1), 65) == 4        # roots 8, 18, 47, 57 of nu^2+1 = 0 (65)
    assert rho((1, 0, 1), 109) == 2
    assert sorted(r for r in range(65) if (r * r + 1) % 65 == 0) == [8, 18, 47, 57]


def test_rational_graph_has_four_cycles_where_the_gaussian_one_does_not():
    """The scope question, as a single assertion on one shared window."""
    X, M = 4000, 60
    rat = PolySequence("x^2+1", (1, 0, 1), X)
    ip, idx, shape, _, _ = incidence(rat, M, 2 * M, min_cofactor=2 * M)
    assert not is_c4_free(ip, idx, shape)
    assert max_offdiagonal_gram(ip, idx, shape) == 2

    gauss = x2plus1_sequence(X * X + 1)
    C, *_ = gauss_incidence(gauss, M, 2 * M)
    assert gauss_gram(C) == 1


def test_the_full_graph_maximum_is_a_pell_equation():
    """G'(1,5) counts y^2 - 5x^2 = 4: Fibonacci/Lucas, spaced by phi^4.

    This is why the full rational graph grows like log X while every dyadic
    window stays bounded -- and why n = 1, which no Type II hypothesis admits,
    is the pair that drives the growth.
    """
    ms = []
    for x in range(1, 40000):
        v = 5 * (x * x + 1) - 1
        r = isqrt(v)
        if r * r == v:
            ms.append(x * x + 1)
    assert ms[:5] == [2, 10, 65, 442, 3026]
    ratios = [ms[i + 1] / ms[i] for i in range(3, len(ms) - 1)]
    phi4 = ((1 + 5 ** 0.5) / 2) ** 4
    assert all(abs(r - phi4) < 0.05 for r in ratios), ratios


def test_alpha_and_kappa_exponents_depend_only_on_the_degree():
    """|A| = X and Q ~ c X^d, so alpha = 1/d and kappa = X^{2-d}/c. Note L.

    The *exponent* is a function of the degree alone; the constant is the
    reciprocal of the leading coefficient, which is why 2x+1 gives X/2 and not
    X. Nothing in Note L uses the constant.
    """
    X = 2000
    for seq in ladder(X):
        d, lead = seq.degree, seq.coeffs[seq.degree]
        assert abs(seq.alpha - 1.0 / d) < 1e-12
        expected = X ** (2 - d) / lead
        assert 0.9 < seq.kappa / expected < 1.1, (seq.name, seq.kappa, expected)
    kappas = {s.name: s.kappa for s in ladder(X)}
    assert kappas["2x+1"] > 1          # Dirichlet: the solved case, recovered
    assert abs(kappas["x^2+1"] - 1) < 1e-5   # X^2/(X^2+1), exactly 1 in the limit
    assert kappas["x^3+2"] < 1
    assert kappas["x^4+1"] < kappas["x^3+2"]


def test_only_degree_one_has_bilinear_structure():
    """The degree ladder's structural half, at a window each degree can reach.

    Bounded Gram for every d >= 2; at d = 1 the Gram grows with the window,
    which is the whole difference between Dirichlet and Landau.
    """
    X, M = 2000, 32
    grams = {}
    for seq in ladder(X):
        ip, idx, shape, _, _ = incidence(seq, M, 2 * M, min_cofactor=1)
        grams[seq.name] = max_offdiagonal_gram(ip, idx, shape) if len(idx) else 0
    assert grams["2x+1"] >= 8                      # grows with M; >= M/4 here
    assert grams["x^2+1"] <= 2
    assert grams["x^2+x+1"] <= 2
    assert grams["x^3+2"] <= 2
    assert grams["x^4+1"] <= 2
    assert grams["2x+1"] > 4 * max(
        grams[k] for k in ("x^2+1", "x^2+x+1", "x^3+2", "x^4+1")
    )


def test_divisibility_is_a_congruence_for_any_polynomial():
    """The one fact the Z harness rests on, so it is not assumed silently."""
    coeffs = (2, 0, 0, 1)                      # x^3 + 2
    for m in range(2, 60):
        rs = set(r for r in range(m) if evaluate(coeffs, r) % m == 0)
        for x in range(1, 300):
            assert (evaluate(coeffs, x) % m == 0) == (x % m in rs)


def test_the_conic_reduction_is_exact():
    """Proposition L.1's algebra: m shared <=> b x^2 - a y^2 = a - b.

    Checked against the two pairs Note L uses, by direct search rather than by
    trusting the derivation.
    """
    from math import gcd
    for n1, n2, expected in [(1, 5, [2, 10, 65, 442, 3026]), (1189, 71978, [65, 109])]:
        d = gcd(n1, n2)
        a, b = n1 // d, n2 // d
        found = []
        for m in range(1, 4000 if n1 == 1 else 200):
            v1, v2 = m * n1 - 1, m * n2 - 1
            if v1 < 0 or v2 < 0:
                continue
            x, y = isqrt(v1), isqrt(v2)
            if x >= 1 and y >= 1 and x * x == v1 and y * y == v2:
                found.append(m)
                assert b * (x * x + 1) == a * (y * y + 1)      # the conic
                assert b * x * x - a * y * y == a - b
        assert found == [m for m in expected if m < (4000 if n1 == 1 else 200)]


def test_phi_squared_is_the_smallest_fundamental_automorph():
    """Proposition L.1's constant, over every non-square discriminant < 1200.

    eps >= phi^2 = 2.618..., attained at Delta = 5 -- which is the pair (1,5),
    the same pair that attains the full graph's maximum. So the constant that
    bounds the spacing and the extremal pair are the same object.
    """
    phi2 = (3 + 5 ** 0.5) / 2
    best = (float("inf"), None)
    for D in range(2, 1200):
        r = isqrt(D)
        if r * r == D:
            continue
        for u in range(1, 60000):
            v = D * u * u + 4
            t = isqrt(v)
            if t * t == v:
                eps = (t + u * D ** 0.5) / 2
                if eps < best[0]:
                    best = (eps, D)
                break
    assert abs(best[0] - phi2) < 1e-9, best
    assert best[1] == 5
    assert phi2 ** 2 > 2          # m'/m >= phi^4 = 6.854 > 2: one per window


def test_V_is_always_even_so_never_one():
    """Note L / Note O: |V| >= 2 is parity, not a coincidence.

    A shared modulus m of (a, b) gives X^2 = am - 1 and Y^2 = bm - 1. For a, b
    both odd: if m is odd then am and bm are odd, so X^2 and Y^2 are even, so X
    and Y are both even; if m is even then both are odd. Either way

        X_k = Y_k  (mod 2),

    hence V = X_i Y_j - X_j Y_i = X_i X_j - X_j X_i = 0 (mod 2).

    So |V| = 1 is impossible and the minimum is 2. That much is a lemma; "|V| is
    always 2" is not -- see `V-is-the-asymptotic-not-the-constant-2`, where |V|
    takes the values 24, 66 and 182 for pairs with large M/sqrt(D).
    """
    from x2plus1.polyseq import ratio_classes
    classes = ratio_classes(900)
    checked = 0
    for (a, b), ms in classes.items():
        if a % 2 == 0 or b % 2 == 0 or len(ms) < 2:
            continue
        for i in range(len(ms) - 1):
            mi, mj = ms[i], ms[i + 1]
            Xi, Yi = isqrt(a * mi - 1), isqrt(b * mi - 1)
            Xj, Yj = isqrt(a * mj - 1), isqrt(b * mj - 1)
            if Xi * Xi != a * mi - 1 or Yi * Yi != b * mi - 1:
                continue
            if Xj * Xj != a * mj - 1 or Yj * Yj != b * mj - 1:
                continue
            checked += 1
            assert (Xi - Yi) % 2 == 0 and (Xj - Yj) % 2 == 0, (a, b, mi, mj)
            assert (Xi * Yj - Xj * Yi) % 2 == 0, (a, b, mi, mj)
    assert checked > 100, f"only {checked} pairs exercised; the test is too weak"
