"""Experiment 20 -- the MEAN of the Gram entry, and what it does and does not show.

Supports Note L ("There is no main term") and Note K.

WHY THE MEAN AND NOT THE MAXIMUM.  Note F bounds G(n1,n2) = #{m : m n1, m n2 in A}
and the repo has spent most of its effort on that bound.  Dispersion needs more
than a bound: it needs count = main term + error with the error genuinely
smaller.  A bounded INTEGER-valued count whose mean is far below 1 has no such
decomposition at any bound, so the mean is what decides whether the argument has
anything to be about.

WHAT IT PRINTS, and every column exists because a claim rests on it:

  * mean G over dyadic cofactor bands, with the pair count, because a "mean" over
    one pair is not an average and the small-N end has exactly that problem;
  * the trivial incidence count T and the squarefree-weighted DIAG, which are NOT
    the same object -- they differ by a factor 0.766, not by the squarefree
    density 0.895, because divisor count and squarefreeness are correlated;
  * the same statistic for the sequences with known outcomes, which is the control
    that keeps the mean-o(1) argument from proving too much.

WHAT IT REFUSES TO PRINT.  No fitted law for the decay.  Three were tried during
this work -- 1/N, (log X)/N, and N/X for the left arm of the U -- and all three
failed, while the VALUES reproduced exactly between two independent
constructions.  See `the-main-term-is-smaller-than-the-granularity`.

AND ONE NEGATIVE RESULT WORTH THE RUNTIME.  mean G does NOT classify: x^3+2y^3 is
captured by Heath-Brown and sits BELOW a^2+b^6, which has no known outcome.  The
control (x^2+1 against a^2+b^4) is sound; generalising it to a classifier was not.

Usage:  python experiments/exp20_gram_mean.py [Q]      (Q = 4e6 takes a few min)
"""

import _bootstrap  # noqa: F401
import sys
from collections import defaultdict
from itertools import combinations
from math import isqrt


def incidence(values):
    """cofactor -> set of moduli, from the divisors of each sequence value."""
    by_cofactor = defaultdict(set)
    for v in values:
        d = 1
        while d * d <= v:
            if v % d == 0:
                by_cofactor[d].add(v // d)
                by_cofactor[v // d].add(d)
            d += 1
    return by_cofactor


def band_stats(by_cofactor, lo, hi):
    """(pairs, mean G, max G) over cofactors in [lo, hi)."""
    ns = [n for n in by_cofactor if lo <= n < hi]
    total = pairs = biggest = 0
    for a, b in combinations(ns, 2):
        g = len(by_cofactor[a] & by_cofactor[b])
        total += g
        pairs += 1
        biggest = max(biggest, g)
    return pairs, (total / pairs if pairs else 0.0), biggest


def x2plus1(Q):
    return {x * x + 1 for x in range(1, isqrt(Q) + 1)}


def two_variable(Q, f):
    out = set()
    b = 1
    while f(1, b) <= Q:
        a = 1
        while f(a, b) <= Q:
            out.add(f(a, b))
            a += 1
        b += 1
    return out


def main() -> int:
    Q = int(sys.argv[1]) if len(sys.argv) > 1 else 4_000_000
    X = isqrt(Q)

    print(f"Q = {Q:,}   X = sqrt(Q) = {X:,}\n")
    print("x^2+1, mean G over dyadic cofactor bands")
    print(f"  {'N':>9} {'N/X':>8} {'pairs':>9} {'mean G':>9} {'max G':>6}")
    by = incidence(x2plus1(Q))
    N = 8
    while 2 * N <= Q // 2:
        pairs, mean, biggest = band_stats(by, N, 2 * N)
        if pairs:
            note = "   <- 1 pair, not an average" if pairs == 1 else ""
            print(f"  {N:>9} {N/X:>8.3f} {pairs:>9} {mean:>9.4f} {biggest:>6}{note}")
        N *= 4
    print("  no law is fitted to this decay; three were tried and all three failed")

    print("\nT (all incidences) vs DIAG (squarefree-weighted), band [2048, 4096)")
    from x2plus1.factorization import roots_of_minus_one          # noqa: F401
    T = DIAG = 0
    for x in range(1, X + 1):
        v = x * x + 1
        sqfree = True
        m, p = v, 2
        while p * p <= m:
            if m % (p * p) == 0:
                sqfree = False
                break
            while m % p == 0:
                m //= p
            p += 1 if p == 2 else 2
        d = 1
        while d * d <= v:
            if v % d == 0:
                for cof in {d, v // d}:
                    if 2048 <= cof < 4096:
                        T += 1
                        if sqfree:
                            DIAG += 1
            d += 1
    print(f"  T = {T}   DIAG = {DIAG}   DIAG/T = {DIAG/T:.4f}"
          f"   (squarefree density is 0.8948 -- they are correlated)")

    print("\nthe control, and the classifier it does NOT support")
    print(f"  {'sequence':>16} {'|A|':>8} {'kappa':>10} {'mean G':>9} {'max G':>6}  outcome")
    family = [
        ("x^2+1", x2plus1(Q), "open"),
        ("x^3+2y^3", two_variable(Q, lambda a, b: b**3 + 2*a**3), "CAPTURED (HB)"),
        ("a^2+b^6", two_variable(Q, lambda a, b: a*a + b**6), "no source read"),
        ("a^2+b^4", two_variable(Q, lambda a, b: a*a + b**4), "CAPTURED (FI)"),
        ("a^2+(b^2+1)^2", two_variable(Q, lambda a, b: a*a + (b*b+1)**2), "CAPTURED (MER)"),
    ]
    for name, vals, outcome in family:
        _, mean, biggest = band_stats(incidence(vals), 2048, 4096)
        print(f"  {name:>16} {len(vals):>8} {len(vals)**2/Q:>10.2f} "
              f"{mean:>9.4f} {biggest:>6}  {outcome}")
    print("  the CONTROL is x^2+1 against a^2+b^4: the mean-o(1) argument does not")
    print("  prove too much.  It is NOT a classifier -- x^3+2y^3 is captured and")
    print("  sits below a^2+b^6, which has no known outcome.")
    return 0


def anchored_vs_ratio(Q=9_000_000):
    """The bands above are ANCHORED; "one dyadic band" means ratio < 2.

    A pair like (9, 17) has ratio 1.89 and is plainly in one band, but a sweep
    stepping N by powers of two or four puts 9 in [8,16) and 17 in [16,32) and
    never forms the pair.  This repo has now recorded three instances of that
    defect, one of which corrupted a value (Note O's minimum, 43.79 for 34.0811).

    So: re-measure the decay with n1 in [N, 2N) and n2 ranging over ALL cofactors
    with n1 < n2 < 2*n1, and print both.

    OUTCOME: the conclusion is unchanged and slightly stronger.  The ratio means
    are LOWER at every sieve-relevant scale (0.0213 against 0.0243 at N = 2048)
    over roughly three times the pairs, and the U-shape survives.  The one
    visible difference is max G = 3 in the smallest band, which the anchored
    sweep could not see because it held a single pair -- and that 3 is the
    recorded (10, 17) case whose three shared moduli include the UNIT m = 1, so
    excluding units it is 2, exactly as the notes already say.
    """
    by = incidence(x2plus1(Q))
    ns = sorted(by)
    print(f"  Q = {Q:,}  (X = {int(Q ** 0.5)})")
    print(f"  {'N':>8} | {'ANCH pairs':>10} {'mean':>9} {'max':>4}"
          f" | {'RATIO pairs':>11} {'mean':>9} {'max':>4}")
    N = 8
    while 2 * N <= Q // 2:
        band = [n for n in ns if N <= n < 2 * N]
        ta = na = ma = 0
        for i in range(len(band)):
            for j in range(i + 1, len(band)):
                g = len(by[band[i]] & by[band[j]])
                ta += g
                ma = max(ma, g)
                na += 1
        tr = nr = mr = 0
        for n1 in band:
            s1 = by[n1]
            for n2 in ns:
                if n1 < n2 < 2 * n1:
                    g = len(s1 & by[n2])
                    tr += g
                    mr = max(mr, g)
                    nr += 1
        if na or nr:
            am = ta / na if na else float("nan")
            rm = tr / nr if nr else float("nan")
            print(f"  {N:>8} | {na:>10} {am:>9.4f} {ma:>4}"
                  f" | {nr:>11} {rm:>9.4f} {mr:>4}")
        N *= 4
    print("  No law is fitted to either column; three were tried and all failed.")


if __name__ == "__main__":
    _rc = main()
    # the faithful (ratio) reading of the same decay -- the claims quote BOTH
    anchored_vs_ratio(min(9_000_000, max(250_000, (int(sys.argv[1]) if len(sys.argv) > 1 else 9_000_000))))
    sys.exit(_rc)
