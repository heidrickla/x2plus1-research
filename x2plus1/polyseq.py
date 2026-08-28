"""Single-variable polynomial sequences, over Z rather than Z[i].

Everything else in this repo is Z[i]-specific, because x^2+1 = N(x+i) is what
makes the Type I story a congruence and the Type II story a lemma. This module
deliberately leaves that setting, for one question:

    Is the degeneracy of A = {x+i} a fact about x^2+1, or about *every*
    single-variable polynomial of degree >= 2?

The exponent half is immediate. For A = {f(x) : x <= X} with deg f = d, the
norm bound is Q ~ X^d and |A| = X, so

    alpha = 1/d,    kappa = |A|^2/Q = X^{2-d}

and kappa <= 1 for every d >= 2, with equality exactly at d = 2. So x^2+1 is
not a special case -- it is the *least* degenerate member of a class where the
bilinear structure is degenerate throughout, and d = 1 (arithmetic
progressions, i.e. Dirichlet) is the only single-variable case with kappa > 1.

The structural half needs measuring, and that is what this module is for. The
incidence graph is built without factoring anything:

    m | f(x)  <=>  x = r (mod m) for some root r of f mod m

which is the same observation Note A makes for x^2+1 -- divisibility in a
polynomial sequence *is* a congruence -- so enumerating moduli and their roots
enumerates the edges directly. Cost is sum_m rho_f(m) X/m, not a factorisation.

No sympy, no factorint: roots are found by direct search mod prime powers and
lifted by CRT, which is fast enough for the ranges an experiment needs and has
no dependency beyond the standard library.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import prod


def evaluate(coeffs: tuple[int, ...], x: int) -> int:
    """f(x) for f = coeffs[0] + coeffs[1] x + ... (exact integer arithmetic)."""
    total = 0
    for c in reversed(coeffs):
        total = total * x + c
    return total


def degree(coeffs: tuple[int, ...]) -> int:
    d = len(coeffs) - 1
    while d > 0 and coeffs[d] == 0:
        d -= 1
    return d


def roots_mod(coeffs: tuple[int, ...], m: int) -> list[int]:
    """All r in [0, m) with f(r) = 0 (mod m).

    Direct search. Callers keep m small (this repo's experiments run to
    m ~ 10^4), and being obviously correct matters more here than being fast:
    the whole point of the module is to test a lemma, not to set a record.
    """
    return [r for r in range(m) if evaluate(coeffs, r) % m == 0]


def rho(coeffs: tuple[int, ...], m: int) -> int:
    """The local root count, the same rho as Note A when f = x^2+1."""
    return len(roots_mod(coeffs, m))


@dataclass
class PolySequence:
    """A = { f(x) : 1 <= x <= X }, with the exponents that go with it."""

    name: str
    coeffs: tuple[int, ...]
    X: int

    @property
    def degree(self) -> int:
        return degree(self.coeffs)

    @property
    def norm_bound(self) -> int:
        """Q ~ f(X): the size of the integers being tested for primality."""
        return evaluate(self.coeffs, self.X)

    @property
    def alpha(self) -> float:
        """|A| = Q^alpha. Equals 1/d up to the constant in f."""
        return 1.0 / self.degree

    @property
    def kappa(self) -> float:
        """|A|^2 / Q, measured rather than assumed."""
        return self.X * self.X / self.norm_bound

    def values(self) -> list[int]:
        return [evaluate(self.coeffs, x) for x in range(1, self.X + 1)]


def incidence(seq: PolySequence, M_lo: int, M_hi: int, min_cofactor: int | None = None):
    """Edges (m, n) with m n = f(x), m in [M_lo, M_hi), as a CSR triple.

    Returns (indptr, indices, shape, m_list, n_list). Rows are moduli m, columns
    are the cofactors n = f(x)/m. Built from congruences, never factorisations.

    `min_cofactor` drops columns with n <= it, defaulting to M_hi. This matters:
    without it the column n = 1 appears (whenever f(x) itself lands in the
    modulus window) and it shares moduli with almost everything, which is an
    artefact of the window and not a property of the sequence. A Type II split
    has both variables large by construction, so excluding small n is the
    faithful thing to measure.
    """
    floor = M_hi if min_cofactor is None else min_cofactor
    rows: dict[int, int] = {}
    cols: dict[int, int] = {}
    pairs: list[tuple[int, int]] = []
    for m in range(max(M_lo, 2), M_hi):
        rs = roots_mod(seq.coeffs, m)
        if not rs:
            continue
        for r in rs:
            x = r if r >= 1 else m
            while x <= seq.X:
                v = evaluate(seq.coeffs, x)
                n = v // m
                if v % m == 0 and n > floor:
                    i = rows.setdefault(m, len(rows))
                    j = cols.get(n)
                    if j is None:
                        j = cols[n] = len(cols)
                    pairs.append((i, j))
                x += m
    pairs = sorted(set(pairs))
    nr, nc = len(rows), len(cols)
    indptr = [0] * (nr + 1)
    for i, _ in pairs:
        indptr[i + 1] += 1
    for i in range(nr):
        indptr[i + 1] += indptr[i]
    indices = [j for _, j in pairs]
    m_list = [m for m, _ in sorted(rows.items(), key=lambda kv: kv[1])]
    n_list = [n for n, _ in sorted(cols.items(), key=lambda kv: kv[1])]
    return indptr, indices, (nr, nc), m_list, n_list


def max_offdiagonal_gram(indptr, indices, shape, stop_at: int | None = None) -> int:
    """max over n1 != n2 of #{m : m n1 and m n2 both in A}. Note F's G.

    Computed column-wise: for each row, every pair of columns it touches
    contributes 1 to that pair's count. Rows here have small degree, so the
    quadratic-in-row-degree cost is not a problem.
    """
    nr, _ = shape
    counts: dict[tuple[int, int], int] = {}
    best = 0
    for i in range(nr):
        cols = indices[indptr[i]:indptr[i + 1]]
        for a in range(len(cols)):
            for b in range(a + 1, len(cols)):
                key = (cols[a], cols[b]) if cols[a] < cols[b] else (cols[b], cols[a])
                counts[key] = c = counts.get(key, 0) + 1
                if c > best:
                    best = c
                    if stop_at is not None and best >= stop_at:
                        return best
    return best


def is_c4_free(indptr, indices, shape) -> bool:
    """No two cofactors share two moduli: the Note F degeneracy, over Z."""
    return max_offdiagonal_gram(indptr, indices, shape, stop_at=2) < 2


def degrees(indptr, indices, shape) -> tuple[float, float]:
    nr, nc = shape
    total = float(len(indices))
    if not (nr and nc and total):
        return 0.0, 0.0
    return total / nr, total / nc


#: The ladder the experiment walks. d = 1 is the control: it is the only
#: single-variable degree with kappa > 1, and it is exactly the solved case
#: (primes in arithmetic progressions).
LADDER = [
    PolySequence("2x+1", (1, 2), 0),
    PolySequence("x^2+1", (1, 0, 1), 0),
    PolySequence("x^2+x+1", (1, 1, 1), 0),
    PolySequence("x^3+2", (2, 0, 0, 1), 0),
    PolySequence("x^4+1", (1, 0, 0, 0, 1), 0),
]


def ladder(X: int) -> list[PolySequence]:
    return [PolySequence(p.name, p.coeffs, X) for p in LADDER]


# --- shared moduli of a ratio class -----------------------------------------
#
# For coprime a < b, m is a SHARED MODULUS of (a, b) when a*m = x^2+1 and
# b*m = y^2+1 -- i.e. a solution of the conic b x^2 - a y^2 = a - b.  Bucketing
# the reduced ratios (y^2+1)/(x^2+1) finds each (a, b) together with all of its
# shared moduli in one pass, without reference to the incidence graph, so it
# sees configurations a dyadic window would hide.  See Note L and Note O.


def ratio_classes(X: int) -> dict[tuple[int, int], list[int]]:
    """{(a, b): sorted shared moduli} over every reduced ratio with x < y <= X."""
    from collections import defaultdict
    from math import gcd

    sq = [x * x + 1 for x in range(X + 1)]
    out: dict[tuple[int, int], set[int]] = defaultdict(set)
    for x in range(1, X + 1):
        sx = sq[x]
        for y in range(x + 1, X + 1):
            g = gcd(sx, sq[y])
            if g > 1:
                out[(sx // g, sq[y] // g)].add(g)
    return {k: sorted(v) for k, v in out.items()}


def close_pairs(classes: dict[tuple[int, int], list[int]]):
    """Yield (a, b, m_i, m_j, V, tau) for shared moduli inside one dyadic window.

    V = X_i Y_j - X_j Y_i is the invariant of Note O: it vanishes exactly when
    the two solutions are proportional, and it satisfies U^2 - D V^2 = M^2 with
    D = ab, M = b - a.  tau = (sqrt b + sqrt a)/(sqrt b - sqrt a) is the
    multiplier; the modulus ratio of a close pair is tau^2 up to O(1/m).
    """
    from math import isqrt, sqrt

    for (a, b), ms in classes.items():
        tau = (sqrt(b) + sqrt(a)) / (sqrt(b) - sqrt(a))
        for i, mi in enumerate(ms):
            for mj in ms[i + 1:]:
                if mj >= 2 * mi:
                    break
                Xi, Yi = isqrt(a * mi - 1), isqrt(b * mi - 1)
                Xj, Yj = isqrt(a * mj - 1), isqrt(b * mj - 1)
                yield a, b, mi, mj, Xi * Yj - Xj * Yi, tau
