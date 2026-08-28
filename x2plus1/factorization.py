"""Bulk factorisation of x^2 + 1 = N(x + i), and of x + i in Z[i].

Factoring x^2+1 one value at a time is wasteful.  The saving grace of this
sequence is that divisibility is a *congruence*:

    p | x^2 + 1   <=>   x == r (mod p) for a root r of r^2 + 1 == 0 (mod p),

so the whole range x <= X can be sieved by walking arithmetic progressions.
This is the same structural fact the Type I estimate rests on, which is why
it is worth having the sieve be the primary tool rather than a convenience.
"""

from __future__ import annotations

from sympy import factorint, primerange
from sympy.ntheory.residue_ntheory import sqrt_mod

from .gaussian import Gauss, conj, exact_div, mul, norm, power, split_prime, unit_normalize


def roots_of_minus_one(q: int) -> list[int]:
    """All r in [0, q) with r^2 + 1 == 0 (mod q).

    Multiplicative in q; empty unless q is 1, or 2 times a product of prime
    powers with p == 1 (mod 4).  |roots| = rho(q) in the notes.
    """
    if q <= 0:
        raise ValueError("q must be positive")
    if q == 1:
        return [0]
    residues = [0]
    modulus = 1
    for p, e in sorted(factorint(q).items()):
        pe = p**e
        if p == 2:
            if e >= 2:
                return []          # r^2 == -1 (mod 4) is insoluble
            local = [1]
        elif p % 4 == 3:
            return []              # -1 is a non-residue mod p
        else:
            r = sqrt_mod(-1, pe)
            if r is None:
                return []
            r = int(r) % pe
            local = sorted({r, pe - r})
        # CRT-merge
        inv = pow(modulus, -1, pe)
        residues = [
            (a + modulus * ((b - a) * inv % pe)) % (modulus * pe)
            for a in residues
            for b in local
        ]
        modulus *= pe
    return sorted(residues)


def rho(q: int) -> int:
    """rho(q) = #{r mod q : r^2 + 1 == 0}.  Counts admissible ideals of norm q."""
    return len(roots_of_minus_one(q))


def sieve_shifted_square(X: int, c: int, prime_bound: int | None = None) -> list[dict[int, int]]:
    """Rational factorisations of a^2 + c for 1 <= a <= X.

    Returns ``F`` with ``F[a] == {p: e}`` (``F[0]`` unused).  ``prime_bound``
    only affects speed, never correctness: whatever survives the progression
    walk is handed to ``factorint``.

    c = 1 gives the sequence of this project; c = b^4 gives one row of the
    Friedlander-Iwaniec comparison set a^2 + b^4 (see ``sequences.py``).
    """
    if prime_bound is None:
        prime_bound = X
    rem = [a * a + c for a in range(X + 1)]
    fac: list[dict[int, int]] = [dict() for _ in range(X + 1)]

    for p in primerange(2, prime_bound + 1):
        roots = sqrt_mod(-c, p, all_roots=True)
        if not roots:
            continue                       # -c a non-residue: p never divides a^2+c
        for r0 in {int(r) % p for r in roots}:
            for a in range(r0 if r0 else p, X + 1, p):
                v, t = 0, rem[a]
                while t % p == 0:
                    t //= p
                    v += 1
                if v:
                    fac[a][p] = v
                    rem[a] = t

    for a in range(1, X + 1):
        if rem[a] > 1:
            for p, e in factorint(rem[a]).items():
                fac[a][p] = fac[a].get(p, 0) + e
    return fac


def sieve_factor_x2plus1(X: int, prime_bound: int | None = None) -> list[dict[int, int]]:
    """Rational factorisations of x^2 + 1 for 1 <= x <= X."""
    return sieve_shifted_square(X, 1, prime_bound)


def gauss_factor_x_plus_i(x: int, rational_fac: dict[int, int]) -> list[tuple[Gauss, int]]:
    """Factor x + i in Z[i] given the rational factorisation of x^2 + 1.

    For each p | x^2+1 exactly one of the two primes above p divides x+i
    (both would force p | (x+i) - (x-i) = 2i), and its exponent equals
    v_p(x^2+1) because N(pi) = p.  p == 3 (mod 4) cannot occur.
    """
    z = (x, 1)
    out: list[tuple[Gauss, int]] = []
    for p, e in sorted(rational_fac.items()):
        if p % 4 == 3:
            raise AssertionError(f"{p} == 3 (mod 4) divides {x}^2+1 -- impossible")
        pi = split_prime(p)
        if p != 2 and exact_div(z, pi) is None:
            pi = unit_normalize(conj(pi))
        out.append((pi, e))
    return out


def check_factorisation(x: int, fac: list[tuple[Gauss, int]]) -> bool:
    prod: Gauss = (1, 0)
    for pi, e in fac:
        prod = mul(prod, power(pi, e))
    return norm(prod) == x * x + 1 and exact_div((x, 1), prod) is not None
