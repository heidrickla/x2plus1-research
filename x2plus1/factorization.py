"""Bulk factorisation of x^2 + 1 = N(x + i), and of x + i in Z[i].

Factoring x^2+1 one value at a time is wasteful.  The saving grace of this
sequence is that divisibility is a *congruence*:

    p | x^2 + 1   <=>   x == r (mod p) for a root r of r^2 + 1 == 0 (mod p),

so the whole range x <= X can be sieved by walking arithmetic progressions.
This is the same structural fact the Type I estimate rests on, which is why
it is worth having the sieve be the primary tool rather than a convenience.
"""

from __future__ import annotations

import random

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


def _spf_sieve(limit: int) -> list[int]:
    """Smallest prime factor for every n <= limit."""
    spf = list(range(limit + 1))
    i = 2
    while i * i <= limit:
        if spf[i] == i:
            for j in range(i * i, limit + 1, i):
                if spf[j] == j:
                    spf[j] = i
        i += 1
    return spf


def admissible_roots_upto(Q_max: int) -> dict[int, list[int]]:
    """{q: roots of r^2+1 == 0 (mod q)} for every admissible q <= Q_max.

    Same content as calling `roots_of_minus_one` on each q, but built in bulk:
    a smallest-prime-factor sieve, one square root of -1 per prime p == 1 (4)
    lifted to prime powers by Hensel, then CRT along each q's factorisation.
    `roots_of_minus_one` calls sympy's `factorint` and `sqrt_mod` per modulus,
    which is what capped Note J's all-moduli cross-check at X <= 10^5.

    Admissible means q = 1, or q = 2^e0 * prod p^e with e0 <= 1 and every
    p == 1 (mod 4); everything else has no root and is omitted.
    """
    if Q_max < 1:
        return {}
    spf = _spf_sieve(Q_max)
    rng = random.Random(0)

    # one root per prime power, by Hensel lifting from the prime
    prime_power_roots: dict[int, list[int]] = {}
    for p in range(2, Q_max + 1):
        if spf[p] != p:
            continue
        if p == 2:
            prime_power_roots[2] = [1]          # and 4 | r^2+1 is insoluble
            continue
        if p % 4 == 3:
            continue
        r = _sqrt_minus_one_pow(p, rng)
        pe, prev = p, r
        while pe <= Q_max:
            prime_power_roots[pe] = sorted({prev, pe - prev})
            nxt = pe * p
            if nxt > Q_max:
                break
            # Hensel: lift prev mod pe to a root mod pe*p
            f = prev * prev + 1
            inv = pow(2 * prev % nxt, -1, nxt)
            prev = (prev - f * inv) % nxt
            pe = nxt

    out: dict[int, list[int]] = {1: [0]}
    for q in range(2, Q_max + 1):
        residues, modulus, ok = [0], 1, True
        n = q
        while n > 1:
            p = spf[n]
            e = 0
            while n % p == 0:
                n //= p
                e += 1
            pe = p**e
            if (p == 2 and e >= 2) or p % 4 == 3:
                ok = False
                break
            local = prime_power_roots.get(pe)
            if local is None:
                ok = False
                break
            inv = pow(modulus, -1, pe)
            residues = [
                (a + modulus * ((b - a) * inv % pe)) % (modulus * pe)
                for a in residues
                for b in local
            ]
            modulus *= pe
        if ok:
            out[q] = sorted(residues)
    return out


def _sqrt_minus_one_pow(p: int, rng: random.Random) -> int:
    """A square root of -1 mod p for p == 1 (mod 4). pow-based, not sqrt_mod."""
    while True:
        a = rng.randrange(2, p)
        r = pow(a, (p - 1) // 4, p)
        if (r * r) % p == p - 1:
            return r
