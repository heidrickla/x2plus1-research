"""Experiment 22 -- why the integrality route cannot close Conjecture O.2.

Supports Note O.  After O.3'' closed the tau_1-assuming cases and O.5 closed the
equal-multiplier case, what survived of O.2 was exactly two DISTINCT multipliers.
This script is the attempt to close that for M = b-a an odd prime, and the
finding is that it CANNOT be closed this way -- with a mechanism.

THE SETUP.  Mod M we have b == a, so tau_p acting on xi = (X,Y) gives

    M | A_p S   and   M | B_p T,     A_p = U_p + 2pa, B_p = U_p - 2pa,
                                     S = X+Y, T = X-Y.

For M an odd prime, U_p^2 == (2pa)^2 (mod M) makes the SIGN eps_p well defined:
U_p == eps_p * 2pa, i.e. M | B_p or M | A_p but not both (both would give
M | 4pa, hence M | p, impossible for an in-window p < M).

THE DICHOTOMY.  M | S and M | T cannot both hold: they give M | 2X and M | 2Y,
so M | X and M | Y for M odd, so M^2 | a Y^2 - b X^2 = M, i.e. M = 1.  And for an
in-window multiplier neither failing is impossible, so EXACTLY ONE holds -- and
it forces the sign: M | S => M | B_p, M | T => M | A_p.

THE ALTERNATION, which is the point.  The exact identities are

    M S' = A_p S + V_p M X    and    M T' = B_p T - V_p M X

-- NOT S' = A_p S / M, which is what a first pass gives and which fails on every
single pair (1947 of 1947).  In subcase A (M | S) write B_p = M beta; then
A_p beta = M + 4 p^2 a with A_p == 4pa forces beta == p (mod M), and T == 2X
gives T' == 2X(beta - p) == 0.  So xi' is in subcase B.  Symmetrically B -> A.

    THE SUBCASE ALTERNATES AT EVERY STEP.

THE CONSEQUENCE.  A triple xi_1 -> xi_2 -> xi_3 therefore has eps_p = +1 and
eps_q = -1, and then both of the composite's integrality conditions are
AUTOMATIC:

    q U_p + p U_q   ==  2pqa - 2pqa  == 0     (mod M)
    U_p U_q + 4pq D ==  -4pq a^2 + 4pq a^2 == 0

So the route dies.  The structure that lets tau_p act on xi_1 is the same
structure that makes tau_q's action on xi_2 integrality-free.  Same-sign pairs
WOULD be constrained -- 34 of 234 fail both conditions -- but the alternation
never produces them.

This is the mechanism behind the recorded observation that all 95 candidates are
satisfiable mod M, i.e. that O.2 is not a congruence statement.  That was an
empirical remark about 95 cases; for M odd prime it is now a proof.

Usage:  python experiments/exp22_sign_alternation.py [X]
"""

import sys
from math import gcd, isqrt

import _bootstrap  # noqa: F401

from sympy import isprime

from x2plus1.polyseq import ratio_classes


def oriented(a, b, u, Yi, w, Yj):
    """(U, V) signed so that X_j = (U X_i + V a Y_i)/M, or None."""
    M = b - a
    U0 = b * u * w - a * Yi * Yj
    V0 = u * Yj - w * Yi
    for su in (1, -1):
        for sv in (1, -1):
            if su * U0 * u + sv * V0 * a * Yi == M * w:
                return su * U0, sv * V0
    return None


def alternation(X):
    """The subcase alternates at every step, and eps is forced by it."""
    classes = ratio_classes(X)
    alt = same = neither = 0
    n_eps = bad_eps = n_beta = bad_beta = 0
    n_id = bad_id = bad_naive = 0
    for (a, b), ms in classes.items():
        M = b - a
        if M < 3 or M % 2 == 0 or not isprime(M):
            continue
        ms = sorted(ms)
        xs = [isqrt(a * m - 1) for m in ms]
        ys = [isqrt(b * m - 1) for m in ms]
        for i in range(len(ms) - 1):
            u, w, Yi, Yj = xs[i], xs[i + 1], ys[i], ys[i + 1]
            got = oriented(a, b, u, Yi, w, Yj)
            if got is None:
                continue
            U, V = got
            A, B = U + V * a, U - V * a
            S1, T1, S2, T2 = u + Yi, u - Yi, w + Yj, w - Yj
            n_id += 1
            bad_id += M * S2 != A * S1 + V * M * u or M * T2 != B * T1 - V * M * u
            bad_naive += M * S2 != A * S1        # the wrong first pass
            c1 = (S1 % M == 0, T1 % M == 0)
            c2 = (S2 % M == 0, T2 % M == 0)
            if not any(c1) or not any(c2):
                neither += 1
                continue
            alt += c1 != c2
            same += c1 == c2
            if V % 2:
                continue
            p = V // 2
            n_eps += 1
            if c1[0]:                                    # M | S  => M | B
                bad_eps += B % M != 0
                if B % M == 0 and p % M:
                    n_beta += 1
                    bad_beta += ((B // M) - p) % M != 0   # beta == p
            else:                                        # M | T  => M | A
                bad_eps += A % M != 0
                if A % M == 0 and p % M:
                    n_beta += 1
                    bad_beta += ((A // M) + p) % M != 0   # alpha == -p
    print(f"  exact identities M S' = A S + V M X, M T' = B T - V M X:"
          f" {n_id} steps, {bad_id} failures")
    print(f"     the naive S' = A S / M, which a first pass gives:"
          f" {bad_naive} of {n_id} FAIL")
    print(f"  subcase ALTERNATES: {alt}   stays the SAME: {same}"
          f"   neither subcase at an end: {neither}")
    print(f"  eps forced by the subcase: {n_eps} steps, {bad_eps} failures")
    print(f"  beta == p (resp. alpha == -p) mod M: {n_beta} steps,"
          f" {bad_beta} failures")
    return alt, same


def composite_is_automatic(amax=30, bmax=3000, kcap=60):
    """Opposite signs make both composite conditions vacuous; same signs do not."""
    n = badV = badU = 0
    m = badV2 = badU2 = 0
    for a in range(1, amax + 1):
        for b in range(a + 1, bmax + 1):
            if gcd(a, b) != 1:
                continue
            M, D = b - a, a * b
            if M < 3 or M % 2 == 0 or not isprime(M):
                continue
            plus, minus = [], []
            for k in range(1, kcap + 1):
                t = M * M + 4 * k * k * D
                U = isqrt(t)
                if U * U != t:
                    continue
                if (U - 2 * k * a) % M == 0:
                    plus.append((k, U))
                if (U + 2 * k * a) % M == 0:
                    minus.append((k, U))
            for p, Up in plus:
                for q, Uq in minus:
                    n += 1
                    badV += (2 * (q * Up + p * Uq)) % M != 0
                    badU += (Up * Uq + 4 * p * q * D) % M != 0
            for p, Up in plus:
                for q, Uq in plus:
                    if p == q:
                        continue
                    m += 1
                    badV2 += (2 * (q * Up + p * Uq)) % M != 0
                    badU2 += (Up * Uq + 4 * p * q * D) % M != 0
    print(f"  OPPOSITE signs -- what the alternation FORCES: {n} (p,q) pairs")
    print(f"     M | 2(q U_p + p U_q): {badV} failures;"
          f"  M | U_p U_q + 4pq D: {badU} failures")
    print(f"  SAME signs, for contrast: {m} pairs")
    print(f"     M | 2(q U_p + p U_q): {badV2} failures;"
          f"  M | U_p U_q + 4pq D: {badU2} failures")
    print("  -> the conditions DO have content; the alternation is exactly what")
    print("     removes it.  So the integrality route cannot close O.2.")
    return n, badV, badU, m, badV2


def non_vacuity(X):
    """The M-prime case is worth closing: it is a seventh of realised close pairs."""
    from x2plus1.polyseq import close_pairs
    classes = ratio_classes(X)
    pairs = list(close_pairs(classes))
    pr = [1 for a, b, *_ in pairs if (b - a) % 2 and isprime(b - a)]
    print(f"  close pairs at X = {X}: {len(pairs)}; with M an odd prime:"
          f" {len(pr)} ({len(pr) / max(1, len(pairs)):.0%})")
    print("  -- so this is not a vacuous case; it is the case the route would")
    print("  have covered, and the route is what fails.")


def main(X=3000):
    print("1. THE ALTERNATION")
    alternation(X)
    print()
    print("2. WHY IT KILLS THE ROUTE")
    composite_is_automatic()
    print()
    print("3. THE CASE IS NOT VACUOUS")
    non_vacuity(X)


if __name__ == "__main__":
    main(int(sys.argv[1]) if len(sys.argv) > 1 else 3000)
