# Note H — Numerical pilot

*Plan §2.4.4. Status: draft. Produced by
[`experiments/exp02_bilinear_pilot.py`](../experiments/exp02_bilinear_pilot.py).*

## What is being measured, and why not the obvious thing

The plan says "compute S for moderate X with random bounded coefficients;
measure the observed cancellation exponent". **Random coefficients measure
nothing**: any fixed matrix against random signs gives square-root cancellation
by the central limit theorem, whatever its arithmetic content. The Type II
hypothesis is a statement about the *worst* case, so three quantities are
reported instead:

| quantity | definition | meaning |
|---|---|---|
| `S_random` | one random sign vector each side | sanity floor only |
| `S_worst` | max over α, β ∈ {±1} (alternating maximisation, lower bound) | what the incidence structure alone permits |
| `S_mobius` | Σ_m \|Σ_n μ(n)·1[mn ∈ A]\| | **the faithful sieve quantity** |

`S_mobius` is the right one: the asymptotic sieve's Type II hypothesis carries
the absolute value outside the m-sum (so α is effectively arbitrary) but
supplies β = μ, not an adversary. Exponents are reported as θ with |S| = T^θ,
where T is the number of (m, n) pairs; θ = 1 is no cancellation, θ = ½ is
square-root.

## Results, X = 2×10⁴ (Q = 4×10⁸, |A| = 20 000)

| N(m) range | rows | cols | T | D_m | d_n | S_mobius | θ | √(MX) |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| [10, 10²) | 44 | 24 666 | 24 691 | 561.16 | 1.00 | 570 | 0.627 | 795 |
| [10², 10³) | 430 | 21 788 | 22 011 | 51.19 | 1.01 | 2 324 | 0.775 | 2 515 |
| [10³, 10⁴) | 4 294 | 19 760 | 21 983 | 5.12 | 1.11 | 7 209 | 0.888 | 7 953 |
| [10⁴, 10⁵) | 20 154 | 8 498 | 22 017 | 1.09 | 2.59 | 18 519 | 0.983 | 25 149 |
| [10⁵, 10⁶) | 21 996 | 1 633 | 21 996 | 1.00 | 13.47 | 20 058 | 0.991 | 79 527 |
| [10⁶, 10⁷) | 21 967 | 190 | 21 967 | 1.00 | 115.62 | 20 273 | 0.992 | 251 487 |

Worst-case θ over the same ranges: **0.993–1.000**. No cancellation at all —
the C₄-free lemma of [Note F](note-F-failure-localisation.md) in numerical
form.

## The empirical law

For M ≤ X the μ-coefficient sum tracks **√(MX)** to within ~2%:

> Σ_m |Σ_n μ(n)·1[mn ∈ A]| ≍ √(MX) for M ≤ X, and saturates at ≍ T ≍ X for M ≥ X.

Writing M = X^u this is θ = (1 + u)/2, against measured 0.627 (u = 0.34),
0.775 (u = 0.58), 0.888 (u = 0.81), 0.983 (u ≥ 1). The heuristic is exactly
what one expects if μ behaves randomly along each fibre: row m has D_m ≍ X/M
terms with square-root cancellation, and there are ≍ M rows, giving
M·√(X/M) = √(MX).

## What this says about plausibility

**Corrected after [Note C](note-C-requirements.md).** The earlier reading of
this table — "cancellation for every M ≤ X^{1−δ}, so the obstruction looks
technical rather than structural" — was measuring the wrong window.

[ASP] hypothesis (B1) requires the bilinear estimate for N ∈ (Δ^{−1}√D,
δ^{−1}√x). Even taking the largest D this sequence could conceivably support,
D = x^{1/2}, that is N ∈ (x^{1/4}, x^{1/2}), i.e. **M = x/N ∈ (X, X^{3/2})** in
the variables of this note. Reading the table in that window:

| M range | S_μ | A(x) = X | S_μ / A(x) |
|---:|---:|---:|---:|
| [10⁴, 10⁵) | 18 519 | 20 000 | 0.93 |
| [10⁵, 10⁶) | 20 058 | 20 000 | 1.00 |
| [10⁶, 10⁷) | 20 273 | 20 000 | 1.01 |

**No saving at all, where (B) demands a factor (log x)^{−222}.** The √(MX)
cancellation is real but lives at M < X, *outside* the range the sieve needs.
Cancellation exists exactly where it is not required and vanishes exactly where
it is.

The mechanism is the one in [Note F](note-F-failure-localisation.md): for
M > X = A(x) the mean row degree D_m ≍ X/M drops below 1, so almost every m
divides just one element of A and the inner sum is a single term with nothing
to cancel against. (B1) forces M ≥ √x while cancellation forces M ≤ A(x), and
both hold at once iff A(x) > √x — that is, iff κ > 1. For x² + 1, κ = 1 and the
two windows share only the endpoint.

So the honest reading is the opposite of the earlier one: **at the density
x^{1/2} the Type II hypothesis fails numerically in precisely the range the
sieve requires**, and it fails for a structural reason. This is moot for [ASP]
in any case, since [Note C](note-C-requirements.md) shows hypothesis (R1) is
already unsatisfiable — but it matters for any future sieve that might relax
(R1), because it says relaxing (R1) alone would not be enough.

## Caveats — read before quoting any of this

- ~~**X = 2×10⁴ is small.**~~ Superseded: [Note J](note-J-mobius-in-progressions.md)
  reaches X = 10⁷ and fits c = 0.00 ± 0.04, so √(MX) is separated from
  √(MX)(log X)^c. What is still **not** distinguished is o(X) from X/(log X)^A —
  that is a statement about the constant and the log factors in the *aggregate*
  sum, and it remains the distinction that matters for the sieve.
- **μ is not adversarial, but it is also not random.** The fit shows μ behaving
  randomly at this size; the parity barrier is precisely the statement that
  proving it does so is the whole problem.
- **The pilot cannot see parity.** A numerical measurement of a true statement
  reveals nothing about provability. Its only legitimate use is the one the
  plan assigns it: sanity-checking whether the target saving is plausible.

## To do

- ~~Run the sweep at X = 10⁵.~~ **Done, and the law is stable.** Ratio of the
  measured sum to √(MX), for M < X:

  | u = log M / log X | X = 2×10⁴ | X = 10⁵ |
  |---:|---:|---:|
  | ≈ 0.3–0.35 | 0.72 | 0.88 |
  | ≈ 0.5–0.58 | 0.92 | 0.93 |
  | ≈ 0.7–0.81 | 0.91 | 0.88 |
  | ≈ 0.9 | — | 0.90 |

  and for M ≥ X the saturation is exact at both sizes: S_μ/A(x) = 1.00, 1.00,
  1.01 (X = 2×10⁴) and 1.00, 1.00, 1.01 (X = 10⁵). A factor of 5 in X moves
  nothing.
- ~~Separate √(MX) from √(MX)(log X)^c.~~ **Done — and the answer is c = 0.**
  This required the reformulation in [Note J](note-J-mobius-in-progressions.md),
  which drops the Gaussian divisor enumeration and reaches X = 10⁷. Fitting the
  per-progression saving ρ ~ (log X)^c over prime moduli gives c = −0.026 and
  +0.039 in the two best-sampled bands (8 348 and 68 784 pairs), against wild
  scatter in bands with only 20–138 pairs. At fixed M the drift is under 1%
  across two decades. **The law is √(MX) with no log-power correction**, and the
  caveat this note has carried from the beginning is discharged. Details and the
  unexplained constant (ρ ≈ 0.655 against a predicted 0.755) are in Note J.
- Restrict n to Gaussian *primes* (the case the sieve actually applies to) and
  compare.
- Repeat for a² + b⁴ at matched norm and diff against FI's proved Type II range
  — that is [Note I](note-I-a2b4-replay.md).

## Adversarial review

- *Two-parameter freedom smuggled in?* No; the pilot only counts.
- *Where is parity broken?* Nowhere — and this note must not be read as
  evidence that it can be. It measures a quantity, not a proof.
