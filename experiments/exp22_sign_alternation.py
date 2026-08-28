"""Experiment 22 -- the sign alternation, and Conjecture O.2 for M an odd prime.

Supports Note O.  After O.3'' closed the tau_1-assuming cases and O.5 closed the
equal-multiplier case, what survived of O.2 was exactly two DISTINCT multipliers.
This script closes that for M = b-a an odd prime.

    CORRECTED.  This file first concluded "the integrality route cannot close
    O.2".  That was TOO STRONG and is the repo's most-repeated error: the
    evidence showed only that the COMPOSITE'S INTEGRALITY CONDITIONS are vacuous
    (section 2, which stands).  The ALTERNATION itself is a different kind of
    constraint -- a consistency condition rather than a divisibility -- and it
    closes the case (section 4).  Kept as a correction rather than a rewrite.

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

So those two conditions carry no information.  The structure that lets tau_p act
on xi_1 is the same structure that makes tau_q's action on xi_2
integrality-free.  Same-sign pairs WOULD be constrained -- 40 of 246 fail both --
but the alternation never produces them.

THEOREM O.7, which is what the alternation does close.  Three moduli in one
window make xi_1 -> xi_2 -> xi_3 flip TWICE, back to subcase A, while the single
step xi_1 -> xi_3 flips ONCE, to B.  The dichotomy forbids both.  Its only
hypothesis is M nmid V, and the window supplies it:

    a |V| (X_j Y_i + X_i Y_j) = M (X_j^2 - X_i^2)    [exact; the factor a is
                                                      easy to drop, and I did]
    Y > X sqrt(b/a)  =>  |V| < (M/2 sqrt D)(R - 1/R),  R = X_j/X_i
    ratio < 2 with X_i >= 1  =>  R^2 < 3  =>  |V| < 0.57735 M/sqrt(D) < M.

So for M an odd prime, no dyadic window holds three shared moduli -- Conjecture
O.2 on that slice, assuming nothing about which multipliers act.  Realised
triples escape exactly where the proof says they must: all three at X = 6000 have
M | V on their two-step, and sit at ratios of 1e4 and up.

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
    print("     removes it.  But that kills only THESE TWO CONDITIONS -- see 4.")
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


def theorem_O7(X):
    """The in-window V bound, and how realised triples escape it."""
    from math import sqrt
    classes = ratio_classes(X)
    BOUND = (sqrt(3) - 1 / sqrt(3)) / 2
    n_id = bad_id = n_win = bad_bound = bad_div = 0
    worst = 0.0
    n_alt = bad_alt = 0
    tri = []
    for (a, b), ms in classes.items():
        M, D = b - a, a * b
        if M < 3:
            continue
        ms = sorted(ms)
        xs = [isqrt(a * m - 1) for m in ms]
        ys = [isqrt(b * m - 1) for m in ms]
        for i in range(len(ms)):
            if xs[i] < 1:
                continue
            for j in range(i + 1, len(ms)):
                V = abs(xs[i] * ys[j] - xs[j] * ys[i])
                n_id += 1
                bad_id += a * V * (xs[j] * ys[i] + xs[i] * ys[j]) != M * (
                    xs[j] ** 2 - xs[i] ** 2)
                if ms[j] >= 2 * ms[i]:
                    continue
                n_win += 1
                bad_bound += not V < BOUND * M / sqrt(D)
                bad_div += V % M == 0
                worst = max(worst, V * sqrt(D) / M)
                if M % 2 and isprime(M):
                    c1 = ((xs[i] + ys[i]) % M == 0, (xs[i] - ys[i]) % M == 0)
                    c2 = ((xs[j] + ys[j]) % M == 0, (xs[j] - ys[j]) % M == 0)
                    n_alt += 1
                    bad_alt += sum(c1) != 1 or sum(c2) != 1 or c1 == c2
        if len(ms) >= 3 and M % 2 and isprime(M):
            V13 = abs(xs[0] * ys[2] - xs[2] * ys[0])
            tri.append((a, b, M, ms[0], ms[2], V13, V13 % M == 0))
    print(f"  a|V|(X_j Y_i + X_i Y_j) = M(X_j^2 - X_i^2): {n_id} pairs,"
          f" {bad_id} failures   (the factor a is easy to drop)")
    print(f"  IN-WINDOW pairs: {n_win}")
    print(f"     |V| < {BOUND:.5f} M/sqrt(D): {bad_bound} failures;"
          f" max |V|sqrt(D)/M = {worst:.6f}")
    print(f"     M | V: {bad_div} occurrences -- so M nmid V, which is O.7's")
    print(f"     ONLY hypothesis.")
    print(f"  M odd prime, in-window: {n_alt} pairs; dichotomy+flip failures:"
          f" {bad_alt}")
    print("  THEOREM O.7.  Three moduli in one window would make xi_1 -> xi_2 ->")
    print("  xi_3 flip twice (back to subcase A) while the single step")
    print("  xi_1 -> xi_3 flips once (to B).  The dichotomy forbids both.")
    print("  So for M an odd prime, no window holds three -- Conjecture O.2 on")
    print("  that slice, with no hypothesis on which multipliers act.")
    print("  Realised triples escape exactly where the proof says they must:")
    for a, b, M, m1, m3, V, d in tri:
        print(f"     (a,b)=({a},{b}) M={M}: {m1} -> {m3}, V = {V},"
              f" M | V ? {d}  (V/M = {V // M if d else '-'})")


def theorem_O8(X):
    """M odd squarefree: the dichotomy becomes a factorisation that swaps."""
    from sympy import factorint
    classes = ratio_classes(X)
    n_st = bad_st = n_f = bad_f = 0
    n_loc = bad_loc = 0
    n_win = bad_win = 0
    noswap = {}
    for (a, b), ms in classes.items():
        M = b - a
        if M < 3 or M % 2 == 0:
            continue
        fac = factorint(M)
        sqfree = all(e == 1 for e in fac.values())
        ms = sorted(ms)
        xs = [isqrt(a * m - 1) for m in ms]
        ys = [isqrt(b * m - 1) for m in ms]
        for i, m in enumerate(ms):
            S, T = xs[i] + ys[i], xs[i] - ys[i]
            n_st += 1
            bad_st += S * T != -M * m
            n_f += 1
            bad_f += gcd(M, S) * gcd(M, T) != M
        f = [(gcd(M, xs[i] + ys[i]), gcd(M, xs[i] - ys[i])) for i in range(len(ms))]
        for i in range(len(ms)):
            if xs[i] < 1:
                continue
            for j in range(i + 1, len(ms)):
                V = abs(xs[i] * ys[j] - xs[j] * ys[i])
                sw = f[i] == (f[j][1], f[j][0])
                if gcd(V, M) == 1 and sqfree:
                    n_loc += 1
                    bad_loc += not sw
                if not sw:
                    noswap[M] = noswap.get(M, 0) + 1
                if ms[j] < 2 * ms[i]:
                    n_win += 1
                    bad_win += gcd(V, M) != 1
    print(f"  S T = -M m                : {n_st} solutions, {bad_st} failures")
    print(f"  gcd(M,S) gcd(M,T) = M     : {n_f} solutions, {bad_f} failures")
    print(f"  M squarefree & gcd(V,M)=1 : {n_loc} pairs, {bad_loc} swap failures")
    print(f"  IN-WINDOW pairs (M odd)   : {n_win}, of which gcd(V,M) != 1:"
          f" {bad_win}")
    print("  -- so the coprimality O.8 assumes is OBSERVED without exception")
    print("     in-window, and is NOT proved: the bound |V| < 0.57735 M/sqrt(D)")
    print("     bounds V without making it coprime to M.")
    print(f"  non-swaps by M: {dict(sorted(noswap.items())[:6])}")
    print("     -- these are NOT confined to non-squarefree M (3, 11, 15, 21, 23")
    print("     all appear).  EVERY non-swap has gcd(V,M) > 1; that, and not")
    print("     squarefreeness, is what separates them.  Squarefreeness is")
    print("     needed for a different reason: it makes gcd(M,S) gcd(M,T) = M a")
    print("     dichotomy per prime rather than a partial split.  M = 9 gives")
    print("     (3,3), which is neither p|S nor p|T.")


def theorem_O9(X):
    """The sign, the pigeonhole, and 3ab < (b-a)^{4/3} -- no hypothesis."""
    from math import sqrt
    from sympy import factorint
    classes = ratio_classes(X)
    n_vw = bad_vw = n_sig = bad_sig = n_eq = bad_eq = 0
    n_tri = bad_tri = n_win = bad_win = 0
    worst = 0.0
    tot = fails = 0
    for (a, b), ms in classes.items():
        M, D = b - a, a * b
        ms = sorted(ms)
        xs = [isqrt(a * m - 1) for m in ms]
        ys = [isqrt(b * m - 1) for m in ms]
        for i in range(len(ms)):
            for j in range(i + 1, len(ms)):
                V = xs[i] * ys[j] - xs[j] * ys[i]
                W = xs[j] * ys[i] + xs[i] * ys[j]
                n_vw += 1
                bad_vw += V * W != M * (ms[i] - ms[j])
        if M < 3 or M % 2 == 0:
            continue
        fac = factorint(M)
        if any(e > 1 for e in fac.values()):
            continue
        tot += 1
        fails += 3 * a * b >= M ** (4 / 3)
        sig = []
        for i in range(len(ms)):
            dd = {}
            for p in fac:
                n_sig += 1
                if xs[i] % p == 0:
                    bad_sig += 1
                    dd[p] = 0
                else:
                    dd[p] = 1 if (ys[i] - xs[i]) % p == 0 else -1
                    if (ys[i] - dd[p] * xs[i]) % p:
                        bad_sig += 1
            sig.append(dd)
        for i in range(len(ms)):
            for j in range(i + 1, len(ms)):
                V = xs[i] * ys[j] - xs[j] * ys[i]
                for p in fac:
                    n_eq += 1
                    bad_eq += (V % p == 0) != (sig[i][p] == sig[j][p])
                if xs[i] >= 1 and ms[j] < 2 * ms[i]:
                    n_win += 1
                    bad_win += not abs(V) < M / sqrt(3 * D)
                    worst = max(worst, abs(V) * sqrt(3 * D) / M)
                for k in range(j + 1, len(ms)):
                    v12 = V
                    v23 = xs[j] * ys[k] - xs[k] * ys[j]
                    v13 = xs[i] * ys[k] - xs[k] * ys[i]
                    n_tri += 1
                    bad_tri += abs(v12 * v23 * v13) % M != 0
    print(f"  V W = M (m_i - m_j), W = X_j Y_i + X_i Y_j: {n_vw} pairs,"
          f" {bad_vw} failures  (no cofactor -- the a cancels)")
    print(f"  sigma = +-1 with Y == sigma X mod p: {n_sig} determinations,"
          f" {bad_sig} failures")
    print(f"  p | V_ij  <=>  sigma_i = sigma_j   : {n_eq} (p,pair),"
          f" {bad_eq} failures")
    print(f"  PIGEONHOLE: M | V12 V23 V13        : {n_tri} triples,"
          f" {bad_tri} failures")
    print(f"  |V| < M/sqrt(3D) in-window         : {n_win} pairs,"
          f" {bad_win} failures, max ratio {worst:.6f}")
    print("  So M <= |V12 V23 V13| < (M/sqrt(3D))^3, i.e. 3ab < (b-a)^{4/3}.")
    if tot:
        print(f"  classes with M odd squarefree: {tot}; those FAILING that and so")
        print(f"  provably unable to hold a triple: {fails} ({fails/tot:.1%})")
    print("  With O.4's t = b/a > 133.875 the admissible a is tiny:")
    for t in (133.875, 1000, 10**4):
        print(f"     t = {t:>9}: a <= {int((t-1)**2/(3*t)**1.5)}")
    print("  Recovers O.7 for M prime with NO hypothesis, and supersedes O.8's")
    print("  coprimality assumption, which turned out not to be needed.")


def _vp(n, p):
    if n == 0:
        return 10 ** 9
    v = 0
    while n % p == 0:
        n //= p
        v += 1
    return v


def theorem_O10(X):
    """The valuation form: no hypothesis on M at all."""
    from sympy import factorint
    classes = ratio_classes(X)
    n_st = bad_st = n_lb = bad_lb = n_two = bad_two = 0
    tot = exc = 0
    cat = {}
    for (a, b), ms in classes.items():
        M = b - a
        if M < 2:
            continue
        tot += 1
        exc += 3 * a * b >= M ** (4 / 3)
        ms = sorted(ms)
        xs = [isqrt(a * m - 1) for m in ms]
        ys = [isqrt(b * m - 1) for m in ms]
        fac = factorint(M)
        for p, e in fac.items():
            sv = [min(e, _vp(x + y, p)) for x, y in zip(xs, ys)]
            tv = [min(e, _vp(x - y, p)) for x, y in zip(xs, ys)]
            for i in range(len(ms)):
                n_st += 1
                bad_st += sv[i] + tv[i] < e
            for i in range(len(ms)):
                for j in range(i + 1, len(ms)):
                    V = xs[i] * ys[j] - xs[j] * ys[i]
                    n_lb += 1
                    bad_lb += _vp(V, p) < max(min(sv[i], sv[j]),
                                              min(tv[i], tv[j]))
            if len(ms) >= 3:
                order = sorted(range(len(ms)), key=lambda i: sv[i])
                for q in range(len(order) - 2):
                    i1, i2, i3 = order[q], order[q + 1], order[q + 2]
                    v12 = xs[i1] * ys[i2] - xs[i2] * ys[i1]
                    v23 = xs[i2] * ys[i3] - xs[i3] * ys[i2]
                    n_two += 1
                    bad_two += _vp(v12, p) + _vp(v23, p) < e
        if len(ms) >= 3:
            sq = all(e == 1 for e in fac.values())
            k = ("even" if M % 2 == 0 else "odd") + ("-sqfree" if sq else "-non")
            for i in range(len(ms)):
                for j in range(i + 1, len(ms)):
                    for kk in range(j + 1, len(ms)):
                        v12 = xs[i] * ys[j] - xs[j] * ys[i]
                        v23 = xs[j] * ys[kk] - xs[kk] * ys[j]
                        v13 = xs[i] * ys[kk] - xs[kk] * ys[i]
                        good = abs(v12 * v23 * v13) % M == 0
                        c = cat.setdefault(k, [0, 0])
                        c[0 if good else 1] += 1
    print(f"  s_i + t_i >= e                              : {n_st} checks,"
          f" {bad_st} failures")
    print(f"  v_p(V) >= max(min(s,s), min(t,t))           : {n_lb} checks,"
          f" {bad_lb} failures")
    print(f"  ordered by s: v_p(V12) + v_p(V23) >= e      : {n_two} checks,"
          f" {bad_two} failures")
    print("  M | V12 V23 V13, by category of M:")
    for k in sorted(cat):
        good, bad = cat[k]
        print(f"     {k:14} {good:5} hold, {bad:5} fail")
    print(f"  So 3ab < (b-a)^(4/3) for ANY M.  Of {tot} classes with M >= 2,")
    print(f"  {exc} are excluded outright ({exc/tot:.2%}); NONE is silent.")
    print("  The sign of section 4 is the e = 1 shadow: there S T = -M m forces")
    print("  s + t = 1 exactly, so (s,t) is (1,0) or (0,1).")


def main(X=3000):
    print("1. THE ALTERNATION")
    alternation(X)
    print()
    print("2. WHY IT KILLS THE ROUTE")
    composite_is_automatic()
    print()
    print("3. THE CASE IS NOT VACUOUS")
    non_vacuity(X)
    print()
    print("4. THEOREM O.7 -- and the composite conditions being vacuous does NOT")
    print("   mean the route is dead; the ALTERNATION itself closes it.")
    theorem_O7(X)
    print()
    print("5. THEOREM O.8 -- the same argument for M odd squarefree, on one")
    print("   hypothesis (gcd(V,M) = 1), which is observed but not proved.")
    theorem_O8(X)
    print()
    print("6. THEOREM O.9 -- the same conclusion with NO hypothesis, by")
    print("   pigeonhole on a two-valued sign.")
    theorem_O9(X)
    print()
    print("7. THEOREM O.10 -- the sign becomes a VALUATION, and then there is no")
    print("   hypothesis on M at all, and no remaining case.")
    theorem_O10(X)


if __name__ == "__main__":
    main(int(sys.argv[1]) if len(sys.argv) > 1 else 3000)
