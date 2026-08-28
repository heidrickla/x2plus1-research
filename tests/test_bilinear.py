import numpy as np
import pytest

from x2plus1.sequences import by_x_range
from x2plus1.typeII import (
    analyse, divisors_with_complement_mobius, gram_split, incidence,
    mobius_bilinear, sigma_max,
)
from x2plus1.gaussian import exact_div, mul, norm, unit_normalize

SEQ = by_x_range(1500)


def test_incidence_entries_are_genuine_factorisations():
    C, m_list, n_list, _mu = incidence(SEQ, 10, 1000)
    elements = {unit_normalize(z) for z in SEQ.elements}
    for i in range(C.shape[0]):
        for k in range(C.indptr[i], C.indptr[i + 1]):
            m, n = m_list[i], n_list[C.indices[k]]
            assert 10 <= norm(m) < 1000
            assert unit_normalize(mul(m, n)) in elements


def test_incidence_total_matches_divisor_count():
    lo, hi = 10, 1000
    C, *_ = incidence(SEQ, lo, hi)
    expected = sum(
        len(divisors_with_complement_mobius(fac, lo, hi)) for _z, fac in SEQ
    )
    assert int(C.data.sum()) == expected


def test_mobius_values_are_correct():
    for z, fac in list(SEQ)[:200]:
        for m, mu in divisors_with_complement_mobius(fac, 1, 10**9):
            n = exact_div(z, m)
            exps = []
            rest = n
            for pi, _e in fac:
                k = 0
                while (nxt := exact_div(rest, pi)) is not None:
                    rest, k = nxt, k + 1
                exps.append(k)
            expected = 0 if any(k >= 2 for k in exps) else (-1) ** sum(exps)
            assert mu == expected, (z, m, exps, mu)


def test_gram_split_matches_dense_computation():
    C, *_ = incidence(SEQ, 100, 1000)
    dense = np.zeros(C.shape)
    for i in range(C.shape[0]):
        for k in range(C.indptr[i], C.indptr[i + 1]):
            dense[i, C.indices[k]] += C.data[k]
    G = dense.T @ dense
    diag, off = gram_split(C)
    assert diag == np.trace(G)
    assert off == np.sum(G) - np.trace(G)


def test_matvec_agrees_with_dense():
    C, *_ = incidence(SEQ, 100, 1000)
    dense = np.zeros(C.shape)
    for i in range(C.shape[0]):
        for k in range(C.indptr[i], C.indptr[i + 1]):
            dense[i, C.indices[k]] += C.data[k]
    rng = np.random.default_rng(0)
    v = rng.standard_normal(C.shape[1])
    w = rng.standard_normal(C.shape[0])
    assert np.allclose(C.matvec(v), dense @ v)
    assert np.allclose(C.rmatvec(w), dense.T @ w)
    exact = float(np.linalg.svd(dense, compute_uv=False)[0])
    assert sigma_max(C) == pytest.approx(exact, rel=1e-9)


def test_bounds_are_ordered():
    r = analyse(SEQ, 100, 1000)
    assert r.S_random <= r.S_worst <= r.T
    assert r.S_mobius <= r.T
    assert r.diag == r.T


def test_mobius_bilinear_is_the_row_absolute_sum():
    C, _m, _n, mu = incidence(SEQ, 100, 1000)
    assert mobius_bilinear(C, mu) == float(np.abs(C.matvec(mu)).sum())


def test_incidence_graph_of_the_line_is_c4_free():
    """Note F's lemma, checked directly at several splits."""
    from x2plus1.typeII import is_c4_free, max_offdiagonal_gram
    seq = by_x_range(4000)
    for lo, hi in [(10, 100), (100, 1000), (1000, 10000), (10000, 100000)]:
        C, *_ = incidence(seq, lo, hi)
        assert is_c4_free(C), (lo, hi)
        assert max_offdiagonal_gram(C) <= 1


def test_line_admits_no_multiplicative_coincidence():
    """(x1+i)(x4+i) = u (x2+i)(x3+i) forces {x1,x4} = {x2,x3}.

    The algebraic content of Note F's lemma, checked exhaustively on a box.
    """
    from x2plus1.gaussian import UNITS
    N = 60
    seen: dict[tuple[int, int], tuple[int, int]] = {}
    for x1 in range(1, N):
        for x4 in range(x1, N):
            prod = mul((x1, 1), (x4, 1))
            for u in UNITS:
                key = mul(u, prod)
                if key in seen:
                    assert seen[key] == (x1, x4), (key, seen[key], (x1, x4))
            seen[prod] = (x1, x4)


def test_a2b4_incidence_graph_is_not_c4_free():
    """The contrast: two-parameter freedom makes 4-cycles abundant."""
    from x2plus1.sequences import a2b4_sequence
    from x2plus1.typeII import is_c4_free
    C, *_ = incidence(a2b4_sequence(10**5), 100, 1000)
    assert not is_c4_free(C)
