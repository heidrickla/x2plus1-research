# Note J — The Type II sum is Möbius in arithmetic progressions

*Not in the plan's original deliverable list. Added because Notes C and F
between them left one well-posed question — what exactly is the missing
arithmetic input? — and it turns out to have a recognisable answer.*

*Status: draft. The reduction is machine-checked in
[`tests/test_note_j.py`](../tests/test_note_j.py); the measurements are
[`exp05`](../experiments/exp05_mobius_progressions.py).*

## Where this note sits

[Note F](note-F-failure-localisation.md) proves the incidence graph of
A = {x + i} is C₄-free, so a bilinear form over it with **arbitrary** bounded
coefficients has no cancellation at any split. [Note C](note-C-requirements.md)
shows that is fatal under Duke–Friedlander–Iwaniec, whose Type II hypothesis
asks for exactly that — while its Type I hypothesis, at level x^{1/2}, x² + 1
*meets*.

But the sieve's own coefficient is **μ**, and with β = μ the same sum does
cancel. So the live question is not "does the bilinear form cancel" — it does —
but "what is the statement that would have to be proved, and is it recognisable?"

This note answers that. It is a reformulation, not a proof strategy, and
probably routine to a specialist; its value is that it names the target.

## The reduction

**Step 1 — the fibres are lines.** Fix m = a + bi and let n = c + di. Then

> mn = (ac − bd) + (ad + bc)i,

so the condition mn ∈ A — that is, Im(mn) = 1 — is the **line** ad + bc = 1 in
(c, d). Its homogeneous solutions are (c, d) = t(a, −b), i.e. n = t·m̄. Hence

> **{n : mn ∈ A} = n₀ + ℤ·m̄**, an arithmetic progression in Z[i] of common
> difference m̄, with ≍ X/N(m) terms.

Checked at every m occurring for X = 2000, with the fibre length independently
matched against #{x ≤ X : x ≡ r_m (mod N(m))}
(`test_fibres_are_arithmetic_progressions_with_difference_conj_m`,
`test_fibre_length_matches_the_residue_class_count`).

**Step 2 — μ of the ideal is μ of the norm.** Each rational prime p | x²+1
contributes exactly one prime ideal to (x+i) with the same exponent, so (x+i)
is squarefree as an ideal iff x²+1 is squarefree as an integer, and the two ω
agree:

> **μ_{Z[i]}((x+i)) = μ(x² + 1).**

(`test_mobius_of_the_ideal_equals_mobius_of_the_norm`.)

**Step 3 — combine.** Writing x + i = m·n, μ(x+i) = μ(m)μ(n) whenever x+i is
squarefree, so

> Σ_{N(m)≍M} | Σ_n μ(n)·1[mn ∈ A] |
>  =  Σ_{q ≍ M} | Σ_{x ≤ X, x ≡ r_q (mod q)} μ(x² + 1) |  + (non-squarefree),

with q = N(m) and r_q the root of r² + 1 ≡ 0 (mod q) — the admissible ideals of
[Note A](note-A-dictionary.md). Verified directly, with every disagreement
confirmed to come from a non-squarefree fibre
(`test_mobius_over_a_fibre_equals_the_progression_sum`).

## What that makes the missing input

> **The Type II hypothesis for x² + 1 is a Bombieri–Vinogradov theorem for
> μ(x² + 1) in arithmetic progressions**, at moduli up to X^{3/4} for a
> sequence of X terms — beyond BV's level 1/2, below Elliott–Halberstam.

The range comes from DFI's Type II window N(b) ∈ [(log X)^C, Q^{3/8}], which in
this note's variables is q ≤ X^{3/4}.

Two things this buys. It removes the Gaussian divisor enumeration entirely —
the object needs only μ(x²+1), which sieves in linear time
([`x2plus1/mobius.py`](../x2plus1/mobius.py), 47 s at X = 10⁷ against minutes
for the incidence route) — and it makes the target recognisable, connecting to
the BFI/Zhang/Maynard literature on moduli beyond 1/2.

## Measurement: the law has no log-power correction

The reformulation makes the question directly measurable. The right statistic is
the **per-progression saving**

> ρ = S / (pairs · √(X/M)),

the mean |Σ μ| over one progression divided by the square root of its length.
Square-root cancellation makes ρ constant in both M and X; a log-power loss
shows as ρ drifting with log X. Note H could not resolve this over one decade.

Swept over prime moduli from X = 10⁴ to 10⁷ (`exp05`), fitting ρ ~ (log X)^c:

| M band | pairs in band | fitted c |
|---|---:|---:|
| [10, 10²) | 20 | +0.126 |
| [10², 10³) | 138 | −0.356 |
| [10³, 10⁴) | 1 058 | −0.101 |
| [10⁴, 10⁵) | 8 348 | **−0.026** |
| [10⁵, 10⁶) | 68 784 | **+0.039** |

**c → 0 as the statistics improve.** The scatter in the small bands is
sample-size noise — 20 pairs cannot fit an exponent — and the two well-sampled
bands both give |c| < 0.04. At fixed M the drift is flat to within 1%:
ρ = 0.7221 → 0.7158 across X = 3×10⁵ → 10⁷.

The fit is taken at **fixed M band**, not at fixed u = log M/log X. That matters:
ρ carries a finite-n dependence (short progressions sit above the Gaussian
limit), and at fixed u the progression length varies with the band, confounding
the finite-n effect with the log-power being measured. At fixed band, n scales
cleanly with X and the two separate. Fitting at fixed u instead gives scatter
from −0.31 to +0.13, which is the confounding, not a signal.

> **Conclusion: the law is √(MX) with no log-power correction.** Per-progression
> cancellation is clean square-root. This discharges the caveat Note H has
> carried since it was first measured.

### The constant, and a control that matters more than it

An earlier run reported ρ ≈ 0.655 against a predicted √(2/π)·√0.8948 = 0.755 and
flagged the gap as unexplained. It was an artefact: the statistic normalised by
the *nominal* band length X/√(lo·hi) rather than the actual mean progression
length, understating it by ~9%. Corrected, ρ ≈ 0.72, and the residual gap is the
finite-n approach to the Gaussian limit. **The fitted c is unaffected** — the
correction is a constant factor per band, which cancels in the drift — so the
headline survived the bug, which is the only reason it is worth reporting rather
than quietly fixing.

The control is the more interesting part. Recomputing ρ against two nulls at
X = 10⁶ — the same μ values randomly **shuffled** (destroying all arithmetic
structure), and a synthetic **iid** ±1/0 sequence at the same density:

| M band | mean length n | ρ actual | ρ shuffled | ρ iid |
|---|---:|---:|---:|---:|
| [10³, 10⁴) | 268.9 | 0.7255 | 0.7185 | 0.7311 |
| [10⁴, 10⁵) | 26.5 | 0.7157 | 0.7114 | 0.7163 |
| [10⁵, 10⁶) | 2.6 | 0.7326 | 0.7283 | 0.7278 |

> **μ(x²+1) along these progressions is statistically indistinguishable from
> random**, by this statistic, at this scale — actual, shuffled and iid agree to
> within 1–2% in every band.

That is a negative result and should be read as one: it says no *obstruction* is
visible in the correlation structure, not that μ is random. It is the outcome
one wants — the required cancellation appears to hold for the reason one would
hope — and it is exactly as far from a proof as it was before, since the parity
barrier is a statement about provability, not about truth.

## Honest assessment as a pathway

**This is a target, not a route.** Three reasons to keep expectations low:

1. Any such theorem **breaks parity**, so it cannot follow from sieve axioms —
   it needs genuine arithmetic input, which is what nobody has at this density.
2. A BV theorem for μ along a thin polynomial sequence is open **even at level
   1/2**, let alone 3/4.
3. Ford–Maynard put γ = 1/2 with ε losses at C⁻ = 0 absent extra assumptions,
   and x² + 1 sits at γ = 1/2 exactly.

What it does change: it makes the required input a **statement about μ in
progressions** rather than about Gaussian bilinear forms, and that is a
literature with real machinery in it.

## This reopens something the repo had closed

[refs/bibliography.md](../refs/bibliography.md) argues that BFI, Zhang,
Polymath 8 and Maynard cannot help, because they raise the level for *primes in
APs* while our cap is a counting bound on the sequence. That argument is sound
for **Type I**. It does **not** transfer to the Type II input identified here:
that is a μ-weighted sum over x ≤ X to moduli ≤ X^{3/4} < X, where the counting
bound does not bite. So well-factorable weights and the dispersion machinery may
be relevant after all — applied to μ(x²+1), not to primes.

The registry claim `large-moduli-cannot-help` is scoped to Type I accordingly.

## Adversarial review

- *Two-parameter freedom smuggled in?* No. The reduction uses only that
  elements of A have imaginary part exactly 1 — the same hypothesis as Note F's
  lemma, and it is what makes the fibre a line.
- *Where is parity broken?* Nowhere. This note relocates the parity-breaking
  requirement into a recognisable statement; it does not supply it, and the
  measurement that the statement is *true* is not evidence that it is provable.
- *Is the reduction novel?* Almost certainly not — the link between Type II sums
  and Möbius in progressions is routine. Do not present it as new. Its value
  here is naming the target and making it cheap to compute.
- *Is c = 0 over-read?* The fit is consistent with c = 0 to |c| < 0.04 in the
  best-sampled bands, over 1.5–3 decades of X. That is evidence about the
  **truth**, not about provability, and it is prime moduli only — the
  all-moduli cross-check is **[VERIFY]** and not yet run at scale.
- *Is the X^{3/4} range right?* It comes from DFI's window, which this repo
  knows at two removes. If DFI's Type II range is different, the level changes.
  **[VERIFY]** — the same dependency Note C flags.
