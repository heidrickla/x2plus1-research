"""Type II: the bilinear form, and the dispersion bookkeeping it needs.

The object of Step 2 is

    S = Sigma_m Sigma_n alpha_m beta_n 1[ m n in A ],     N(m) ~ M, N(n) ~ N,

for *arbitrary* bounded alpha, beta.  Random coefficients always give
square-root cancellation and so measure nothing about the hypothesis; the
sieve needs the worst case.  What this module computes are the quantities the
dispersion argument of the plan (step 2.2) actually manipulates.

Write C for the incidence matrix, rows indexed by ideals m with N(m) in the
requested range, columns by ideals n, and C[m,n] = 1 when m n in A.  Then

    T   = ||C||_1 = #{(m,n) : mn in A}     the trivial bound on |S|
    d_n = column sums = #{m : mn in A}
    D_m = row sums    = #{n : mn in A}

Cauchy-Schwarz in m (steps 2.2.1-2) gives

    |S|^2 <= |rows| * Sigma_{n1,n2} beta_{n1} beta_{n2} G[n1,n2],   G = C^T C,

and opening the square (step 2.2.3) splits that into

    diagonal     Sigma_n G[n,n]           = Sigma_n d_n = T
    off-diagonal Sigma_{n1 != n2} G[.,.]  = Sigma_m D_m^2 - T

The diagonal is what the trivial bound already gives; every saving must come
out of the off-diagonal, which is exactly the sum Note F has to name.

The headline number is the exponent theta with |S| = T^theta: theta = 1 is no
cancellation, theta = 1/2 is square-root cancellation.  Note C fixes the theta
the sieve demands; Note H asks whether it is attainable at all.

Units.  Rows and columns are indexed by *ideals* (unit-normalised generators).
Since alpha and beta are arbitrary bounded coefficients, absorbing the unit u
in a = u m n into either one changes nothing.
"""

from __future__ import annotations

from dataclasses import dataclass, field

import numpy as np

from .gaussian import Gauss, exact_div, mul, norm, unit_normalize
from .sequences import GaussianSequence


def divisors_in_norm_range(fac: list[tuple[Gauss, int]], lo: int, hi: int) -> list[Gauss]:
    """Normalised divisors d with lo <= N(d) < hi.  Prunes on norm while building."""
    divs: list[Gauss] = [(1, 0)]
    for pi, e in fac:
        npi = norm(pi)
        grown: list[Gauss] = []
        for d in divs:
            cur, nd = d, norm(d)
            for _ in range(e + 1):
                if nd >= hi:
                    break
                grown.append(cur)
                cur = unit_normalize(mul(cur, pi))
                nd *= npi
        divs = grown
    return [d for d in divs if lo <= norm(d) < hi]


def divisors_with_complement_mobius(
    fac: list[tuple[Gauss, int]], lo: int, hi: int
) -> list[tuple[Gauss, int]]:
    """Divisors m with lo <= N(m) < hi, each paired with mu(n) for n = a/m.

    mu here is the Moebius function of the *ideal* n: 0 if n is not squarefree,
    else (-1)^(number of prime ideal factors).  This is the coefficient the
    asymptotic sieve actually supplies in its Type II hypothesis -- the outer
    coefficient alpha_m is arbitrary (it appears under an absolute value), but
    beta_n is mu, not adversarial.
    """
    items: list[tuple[Gauss, tuple[int, ...]]] = [((1, 0), ())]
    for pi, e in fac:
        npi = norm(pi)
        grown: list[tuple[Gauss, tuple[int, ...]]] = []
        for d, exps in items:
            cur, nd = d, norm(d)
            for k in range(e + 1):
                if nd >= hi:
                    break
                grown.append((cur, exps + (k,)))
                cur = unit_normalize(mul(cur, pi))
                nd *= npi
        items = grown

    totals = [e for _, e in fac]
    out: list[tuple[Gauss, int]] = []
    for d, exps in items:
        if not lo <= norm(d) < hi:
            continue
        mu = 1
        for total, taken in zip(totals, exps):
            r = total - taken
            if r >= 2:
                mu = 0
                break
            if r == 1:
                mu = -mu
        out.append((d, mu))
    return out


@dataclass
class Sparse:
    """Minimal CSR matrix with 0/1 data; avoids a scipy dependency."""

    indptr: np.ndarray
    indices: np.ndarray
    data: np.ndarray
    shape: tuple[int, int]
    row_idx: np.ndarray = field(init=False, repr=False)

    def __post_init__(self) -> None:
        self.row_idx = np.repeat(np.arange(self.shape[0]), np.diff(self.indptr))

    def matvec(self, v: np.ndarray) -> np.ndarray:
        out = np.zeros(self.shape[0])
        np.add.at(out, self.row_idx, self.data * v[self.indices])
        return out

    def rmatvec(self, v: np.ndarray) -> np.ndarray:
        out = np.zeros(self.shape[1])
        np.add.at(out, self.indices, self.data * v[self.row_idx])
        return out

    def row_sums(self) -> np.ndarray:
        out = np.zeros(self.shape[0])
        np.add.at(out, self.row_idx, self.data)
        return out

    def col_sums(self) -> np.ndarray:
        out = np.zeros(self.shape[1])
        np.add.at(out, self.indices, self.data)
        return out


def incidence(seq: GaussianSequence, M_lo: int, M_hi: int):
    """Build C for the factorisations a = m n of A with N(m) in [M_lo, M_hi).

    Returns (C, m_list, n_list, col_mu) where col_mu[j] = mu(n_list[j]).
    """
    rows: dict[Gauss, int] = {}
    cols: dict[Gauss, int] = {}
    col_mu: list[int] = []
    pairs: list[tuple[int, int]] = []
    for z, fac in seq:
        for m, mu in divisors_with_complement_mobius(fac, M_lo, M_hi):
            n = exact_div(z, m)
            assert n is not None, (z, m)
            i = rows.setdefault(m, len(rows))
            key = unit_normalize(n)
            j = cols.get(key)
            if j is None:
                j = cols[key] = len(cols)
                col_mu.append(mu)
            pairs.append((i, j))
    pairs.sort()
    nr, nc = len(rows), len(cols)
    counts = np.zeros(nr + 1, dtype=np.int64)
    for i, _ in pairs:
        counts[i + 1] += 1
    indptr = np.cumsum(counts)
    indices = np.array([j for _, j in pairs], dtype=np.int64) if pairs else np.zeros(0, np.int64)
    data = np.ones(len(pairs))
    m_list = [m for m, _ in sorted(rows.items(), key=lambda kv: kv[1])]
    n_list = [n for n, _ in sorted(cols.items(), key=lambda kv: kv[1])]
    return Sparse(indptr, indices, data, (nr, nc)), m_list, n_list, np.array(col_mu, float)


def gram_split(C: Sparse) -> tuple[float, float]:
    """(diagonal, off-diagonal L1) mass of G = C^T C.

    diagonal     = Sigma_n G[n,n]           = Sigma_n d_n = T
    off-diagonal = Sigma_{n1!=n2} G[n1,n2]  = Sigma_m D_m^2 - T   (entries >= 0)
    """
    diag = float(C.col_sums().sum())
    rs = C.row_sums()
    return diag, float((rs * rs).sum() - diag)


def mobius_bilinear(C: Sparse, col_mu: np.ndarray) -> float:
    """Sigma_m | Sigma_n mu(n) C[m,n] |  -- the faithful Type II quantity.

    The absolute value outside is the sup over bounded alpha_m, so this equals
    max_{|alpha|<=1} |S| with beta = mu.  Contrast ``worst_case_signs``, which
    also lets beta be adversarial; the gap between the two is the difference
    between "the incidence structure forbids cancellation" and "mu fails to
    cancel", and only the latter is the sieve's problem.
    """
    return float(np.abs(C.matvec(col_mu)).sum())


def sigma_max(C: Sparse, iters: int = 300, tol: float = 1e-12, seed: int = 0) -> float:
    """Largest singular value, by power iteration on C^T C."""
    rng = np.random.default_rng(seed)
    v = rng.standard_normal(C.shape[1])
    v /= np.linalg.norm(v)
    s = 0.0
    for _ in range(iters):
        w = C.rmatvec(C.matvec(v))
        nw = float(np.linalg.norm(w))
        if nw == 0.0:
            return 0.0
        v = w / nw
        s_new = float(np.sqrt(nw))
        if abs(s_new - s) < tol * max(s_new, 1.0):
            return s_new
        s = s_new
    return s


def worst_case_signs(C: Sparse, restarts: int = 12, iters: int = 80, seed: int = 0) -> float:
    """Alternating +-1 maximisation of |alpha^T C beta|.

    Each half-step is optimal given the other, so the objective is
    non-decreasing; the result is a lower bound on max over |alpha|,|beta| <= 1
    of |S|, which is the quantity the Type II hypothesis constrains.
    """
    rng = np.random.default_rng(seed)
    best = 0.0
    for _ in range(restarts):
        beta = rng.choice([-1.0, 1.0], size=C.shape[1])
        prev = -1.0
        for _ in range(iters):
            alpha = np.sign(C.matvec(beta))
            alpha[alpha == 0] = 1.0
            beta = np.sign(C.rmatvec(alpha))
            beta[beta == 0] = 1.0
            val = float(abs(alpha @ C.matvec(beta)))
            if val <= prev:
                break
            prev = val
        best = max(best, prev)
    return best


@dataclass
class TypeIIReport:
    label: str
    M_lo: int
    M_hi: int
    n_rows: int
    n_cols: int
    T: int
    diag: float
    offdiag: float
    sigma: float
    S_random: float
    S_worst: float
    S_mobius: float

    def exponent(self, value: float) -> float:
        """theta with value = T^theta.  1 = no cancellation, 1/2 = square-root."""
        if self.T <= 1:
            return float("nan")
        return float(np.log(max(value, 1e-30)) / np.log(self.T))

    @property
    def dispersion_bound(self) -> float:
        """|S| <= sqrt(rows * (diag + offdiag)): step 2.2 with no saving taken."""
        return float(np.sqrt(self.n_rows * (self.diag + self.offdiag)))

    def summary(self) -> str:
        off_ratio = self.offdiag / self.diag if self.diag else float("nan")
        return (
            f"{self.label}: N(m) in [{self.M_lo}, {self.M_hi})   "
            f"C is {self.n_rows} x {self.n_cols},  T = {self.T}\n"
            f"    Gram   diag = {self.diag:.5g}   offdiag = {self.offdiag:.5g}   "
            f"off/diag = {off_ratio:.4g}\n"
            f"    dispersion bound |S| <= {self.dispersion_bound:.5g}  "
            f"(theta = {self.exponent(self.dispersion_bound):.3f})\n"
            f"    sigma_max = {self.sigma:.5g}\n"
            f"    |S| random signs = {self.S_random:.5g}  "
            f"(theta = {self.exponent(self.S_random):.3f})\n"
            f"    |S| worst case  >= {self.S_worst:.5g}  "
            f"(theta = {self.exponent(self.S_worst):.3f})\n"
            f"    |S| beta = mu    = {self.S_mobius:.5g}  "
            f"(theta = {self.exponent(self.S_mobius):.3f})"
        )


def analyse(seq: GaussianSequence, M_lo: int, M_hi: int, seed: int = 0) -> TypeIIReport:
    C, _m_list, _n_list, col_mu = incidence(seq, M_lo, M_hi)
    T = int(C.data.sum())
    if T == 0:
        raise ValueError(f"no factorisations of {seq.name} with N(m) in [{M_lo}, {M_hi})")
    diag, off = gram_split(C)
    rng = np.random.default_rng(seed)
    a = rng.choice([-1.0, 1.0], size=C.shape[0])
    b = rng.choice([-1.0, 1.0], size=C.shape[1])
    return TypeIIReport(
        label=seq.name,
        M_lo=M_lo,
        M_hi=M_hi,
        n_rows=C.shape[0],
        n_cols=C.shape[1],
        T=T,
        diag=diag,
        offdiag=off,
        sigma=sigma_max(C, seed=seed),
        S_random=float(abs(a @ C.matvec(b))),
        S_worst=worst_case_signs(C, seed=seed),
        S_mobius=mobius_bilinear(C, col_mu),
    )


def max_offdiagonal_gram(C: Sparse, stop_at: int | None = None) -> int:
    """max over n1 != n2 of G[n1,n2] = #{m : m n1 in A and m n2 in A}.

    This is 1 exactly when the bipartite incidence graph contains no 4-cycle,
    which for A = {x + i} is a theorem (Note F): the line Im z = 1 admits no
    multiplicative coincidence a1 a4 = a2 a3.  Dispersion needs this quantity
    to be large and to have a main term; when it is identically 0 or 1 there is
    nothing for Cauchy-Schwarz to extract.

    ``stop_at`` returns early once that value is reached (use 2 to test
    C4-freeness on sequences where the full count is expensive).
    """
    from collections import defaultdict
    from itertools import combinations

    pair_counts: dict[tuple[int, int], int] = defaultdict(int)
    best = 0
    for i in range(C.shape[0]):
        cols = sorted(set(C.indices[C.indptr[i]:C.indptr[i + 1]].tolist()))
        for a, b in combinations(cols, 2):
            pair_counts[(a, b)] += 1
            if pair_counts[(a, b)] > best:
                best = pair_counts[(a, b)]
                if stop_at is not None and best >= stop_at:
                    return best
    return best


def is_c4_free(C: Sparse) -> bool:
    """True when no two columns share two rows: the Note F degeneracy."""
    return max_offdiagonal_gram(C, stop_at=2) < 2
