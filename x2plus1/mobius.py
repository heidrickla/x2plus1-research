"""Fast Moebius values of x^2 + 1, for the Type II reduction of Note J.

Why this module exists
----------------------
Note J reduces the Type II sum to a Bombieri-Vinogradov statement for
mu(x^2+1) over arithmetic progressions. That object needs no Gaussian divisor
enumeration at all -- only mu(x^2+1) for x <= X -- so it can be computed a long
way past what the incidence-matrix route in ``typeII`` can reach.

Two facts make it cheap.

1. **mu of the ideal equals mu of the norm.** Each rational prime p | x^2+1
   contributes exactly one prime ideal to (x+i), with the same exponent
   (``factorization.gauss_factor_x_plus_i``). So (x+i) is squarefree as an ideal
   iff x^2+1 is squarefree as an integer, and the two omega's agree. Hence

       mu_{Z[i]}((x+i)) = mu(x^2 + 1).

2. **No primality test is needed.** After sieving *every* prime p <= X, the
   leftover L divides x^2+1 <= X^2+1 and has all prime factors > X. If L were
   composite, L = pq with p, q > X gives pq > X^2, so q < (X^2+1)/X = X + 1/X,
   leaving no room for an integer q > X. So L is 1 or a single prime, and
   omega picks up exactly ``L > 1``. L = p^2 is impossible for the same reason.

Both are checked in ``tests/test_mobius.py`` against the tested-but-slow
``factorization.sieve_factor_x2plus1``.
"""

from __future__ import annotations

import random

import numpy as np
from sympy import primerange


def _sqrt_minus_one(p: int, rng: random.Random) -> int:
    """A square root of -1 mod p, for p == 1 (mod 4).

    pow()-based rather than ``sympy.sqrt_mod``: measured 1.6 us against 9.6 us,
    which matters when this is called once per prime up to X.
    """
    while True:
        a = rng.randrange(2, p)
        r = pow(a, (p - 1) // 4, p)
        if (r * r) % p == p - 1:
            return r


def mobius_x2plus1(X: int, seed: int = 0) -> np.ndarray:
    """mu(x^2 + 1) for 0 <= x <= X, as int8. Index 0 is unused.

    Memory: 8 bytes/x for the residual plus 2 more, so ~1 GB at X = 10^8.
    """
    rem = np.arange(X + 1, dtype=np.int64)
    rem *= rem
    rem += 1
    omega = np.zeros(X + 1, dtype=np.int8)
    squarefree = np.ones(X + 1, dtype=bool)

    # p = 2: v_2(x^2+1) = 1 for odd x, 0 for even x.
    rem[1::2] //= 2
    omega[1::2] += 1

    rng = random.Random(seed)
    for p in primerange(3, X + 1):
        if p % 4 != 1:
            continue                       # p == 3 (mod 4) never divides x^2+1
        r = _sqrt_minus_one(p, rng)
        for root in {r, p - r}:
            sl = rem[root::p]
            sl //= p
            omega[root::p] += 1
            # p^2 | x^2+1 requires x == root (mod p^2); rare, so loop.
            while True:
                mask = (sl % p) == 0
                if not mask.any():
                    break
                squarefree[root::p][mask] = False
                sl[mask] = sl[mask] // p

    omega[rem > 1] += 1                    # the leftover is 1 or a single prime
    mu = np.where(squarefree, np.where(omega & 1, -1, 1), 0).astype(np.int8)
    mu[0] = 0
    return mu
