"""Exact arithmetic in Z[i].

A Gaussian integer is a pair of Python ints ``(a, b)`` meaning ``a + b*i``.
Everything here is exact integer arithmetic -- no floats, no complex().

Normalisation convention
------------------------
``unit_normalize`` sends z != 0 to the unique associate with ``Re > 0`` and
``Im >= 0`` (the "first quadrant" representative).  Because Z[i] is a PID with
unit group {1, i, -1, -i}, this representative is a canonical name for the
*ideal* (z), which is the object the sieve actually cares about.
"""

from __future__ import annotations

from sympy import factorint
from sympy.ntheory.residue_ntheory import sqrt_mod

Gauss = tuple[int, int]

UNITS: tuple[Gauss, ...] = ((1, 0), (0, 1), (-1, 0), (0, -1))


def norm(z: Gauss) -> int:
    a, b = z
    return a * a + b * b


def conj(z: Gauss) -> Gauss:
    a, b = z
    return (a, -b)


def mul(z: Gauss, w: Gauss) -> Gauss:
    a, b = z
    c, d = w
    return (a * c - b * d, a * d + b * c)


def add(z: Gauss, w: Gauss) -> Gauss:
    return (z[0] + w[0], z[1] + w[1])


def sub(z: Gauss, w: Gauss) -> Gauss:
    return (z[0] - w[0], z[1] - w[1])


def power(z: Gauss, e: int) -> Gauss:
    result: Gauss = (1, 0)
    base = z
    while e:
        if e & 1:
            result = mul(result, base)
        base = mul(base, base)
        e >>= 1
    return result


def exact_div(z: Gauss, w: Gauss) -> Gauss | None:
    """Return z/w if it lies in Z[i], else None."""
    nw = norm(w)
    if nw == 0:
        raise ZeroDivisionError("division by zero in Z[i]")
    p, q = mul(z, conj(w))
    if p % nw or q % nw:
        return None
    return (p // nw, q // nw)


def divides(w: Gauss, z: Gauss) -> bool:
    return exact_div(z, w) is not None


def divmod_gauss(z: Gauss, w: Gauss) -> tuple[Gauss, Gauss]:
    """Euclidean division: z = q*w + r with norm(r) <= norm(w)/2."""
    nw = norm(w)
    if nw == 0:
        raise ZeroDivisionError("division by zero in Z[i]")
    p, q = mul(z, conj(w))
    # floor(t + 1/2) rounds to nearest for every sign; Python's // is a true floor.
    quot = ((2 * p + nw) // (2 * nw), (2 * q + nw) // (2 * nw))
    return quot, sub(z, mul(quot, w))


def gcd(z: Gauss, w: Gauss) -> Gauss:
    """Gaussian gcd, returned unit-normalised."""
    while w != (0, 0):
        z, w = w, divmod_gauss(z, w)[1]
    return unit_normalize(z)


def unit_normalize(z: Gauss) -> Gauss:
    """Canonical associate: Re > 0 and Im >= 0.  Names the ideal (z)."""
    if z == (0, 0):
        return z
    a, b = z
    for _ in range(4):
        if a > 0 and b >= 0:
            return (a, b)
        a, b = -b, a  # multiply by i
    raise AssertionError(f"no normal associate for {z}")


def unit_of(z: Gauss) -> Gauss:
    """The unit u with z = u * unit_normalize(z)."""
    n = unit_normalize(z)
    for u in UNITS:
        if mul(u, n) == z:
            return u
    raise AssertionError(f"{z} is not a unit multiple of {n}")


# --------------------------------------------------------------------------
# Primes of Z[i]
# --------------------------------------------------------------------------

def split_prime(p: int) -> Gauss:
    """For p = 2 or p == 1 (mod 4), a Gaussian prime above p (normalised).

    p = 2 is ramified: (2) = (1+i)^2 up to a unit, since 2 = -i(1+i)^2.
    p == 1 (mod 4) splits: (p) = (pi)(conj pi) with N(pi) = p.
    p == 3 (mod 4) is inert and has no Gaussian prime of norm p; ValueError.
    """
    if p == 2:
        return (1, 1)
    if p % 4 == 3:
        raise ValueError(f"{p} is inert in Z[i]; the prime above it is (p) itself")
    r = sqrt_mod(-1, p)
    if r is None:
        raise ValueError(f"-1 is not a square mod {p}")
    return gcd((p, 0), (int(r), 1))


def factor_gauss(z: Gauss) -> list[tuple[Gauss, int]]:
    """Factor a nonzero Gaussian integer into normalised primes with exponents.

    General-purpose (used for spot checks and for the a^2+b^4 sequence);
    for the x+i sequence prefer ``factorization.sieve_factor_x_plus_i``,
    which is far faster in bulk.
    """
    if z == (0, 0):
        raise ValueError("cannot factor 0")
    out: list[tuple[Gauss, int]] = []
    rest = z
    for p, e in sorted(factorint(norm(z)).items()):
        if p % 4 == 3:
            # Inert: p | z forces p^(e/2) || z.
            k = e // 2
            if k:
                out.append(((p, 0), k))
                rest = exact_div(rest, power((p, 0), k))
            continue
        pi = split_prime(p)
        for cand in ((pi, conj(pi)) if p != 2 else (pi,)):
            cand = unit_normalize(cand)
            k = 0
            while (nxt := exact_div(rest, cand)) is not None:
                rest = nxt
                k += 1
            if k:
                out.append((cand, k))
    assert norm(rest) == 1, f"leftover {rest} factoring {z}"
    return out


def divisors_from_factorisation(fac: list[tuple[Gauss, int]]) -> list[Gauss]:
    """All normalised divisors (i.e. all divisor *ideals*) of the factored element."""
    divs: list[Gauss] = [(1, 0)]
    for pi, e in fac:
        powers = [power(pi, k) for k in range(e + 1)]
        divs = [unit_normalize(mul(d, pk)) for d in divs for pk in powers]
    return divs
