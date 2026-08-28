# x² + 1 — research repo

Working repo for the programme in [x2plus1-research-plan.md](x2plus1-research-plan.md):
attack Landau's fourth problem via the Friedlander–Iwaniec asymptotic sieve,
reformulated over **Z[i]**.

The plan's working principle governs this repo too: **do not try to prove the
theorem — locate the exact lemma in the a² + b⁴ argument that fails at density
x^{1/2}.** Everything here is instrumentation for that search.

## Layout

| path | what it is |
|---|---|
| [x2plus1-research-plan.md](x2plus1-research-plan.md) | the charter. Not edited by work; amended only deliberately. |
| [notes/](notes/) | Notes A–I, the deliverables named in the plan. |
| [x2plus1/](x2plus1/) | the library: Z[i] arithmetic, sieving, Type I and Type II harnesses. |
| [experiments/](experiments/) | runnable scripts; each names the note it supports. |
| [tests/](tests/) | unit tests, plus `test_arithmetic_facts.py` — machine-checked statements of the lemmas the notes rely on. |
| [refs/](refs/) | bibliography and a literature-scan log. |

## Quick start

```bash
python -m pytest -q
```

```bash
python experiments/exp01_type_i_level.py 4000
```

```bash
python experiments/exp02_bilinear_pilot.py 20000
```

```bash
python experiments/exp03_density_ledger.py 10000000
```

No installation needed — the scripts put the repo root on `sys.path`. Requires
Python ≥ 3.11 with `sympy` and `numpy`.

## State of play

Step 1 is substantially done for the x² + 1 side; Step 2 has a first pass.
Notes C, G and I are the open ones. Two findings so far, both numerically
confirmed and both needing a rigorous write-up:

**Type I stops at N^{1/2}, and not for a soft reason.** Divisibility by a
Gaussian ideal `d` is exactly one residue class mod N(d), so the error `r_d` is
at most 1 in absolute value — and that is sharp, since an interval of length X
meets a class in ⌊X/q⌋ or ⌈X/q⌉ points. The number of admissible ideals of norm
≤ D is ~ (3/2π)·D (residue of ζ(s)L(s,χ₄)/ζ(2s); measured at 0.4771 against a
predicted 0.47746). So Σ|r_d| ≍ D, and the constraint Σ|r_d| = o(|A|) gives
**D = o(X) = o(N^{1/2})**. See [Note B](notes/note-B-type-I.md).

**The Type II incidence matrix is a forest, provably.** Splitting a = mn and
writing G(n₁, n₂) = #{m : mn₁ ∈ A and mn₂ ∈ A} — the sum every dispersion
argument must evaluate — we have the

> **Lemma.** For A = {x + i}, G(n₁, n₂) ≤ 1 whenever n₁ ≠ n₂.
>
> *Proof.* A 4-cycle gives a₁a₄ = u·a₂a₃ for a unit u. Since (x+i)(y+i) =
> (xy−1) + i(x+y) has Re ≥ 0 and Im ≥ 2 for x, y ≥ 1, both sides lie in the
> first quadrant, forcing u = 1; then x₁+x₄ = x₂+x₃ and x₁x₄ = x₂x₃, so
> {x₁,x₄} = {x₂,x₃}, which collapses the cycle. ∎

So there is no congruence to detect, no exponential sum, no Weil bound — the
count is already 0 or 1 and Cauchy–Schwarz has discarded everything. Measured
dispersion exponent: **θ = 1.00–1.03 at every split, worse than trivial.** The
same fact from the density side: for A of size |A| with norms ≍ Q the mean
degrees satisfy D_m·d_n ≍ |A|²/Q =: κ independent of the split, so

```
max over M of  min(D_m, d_n)  ≍  √κ  =  |A| / Q^{1/2}
```

which is **exactly 1** for x² + 1 and ≍ Q^{1/4} for a² + b⁴ (predicted 48.7,
measured 41.2 at Q = 10⁷; maximum off-diagonal Gram entry 1 versus **667**).
Density Q^{1/2} is not merely thin — it is the critical density at which κ = 1.
**This is the line where the two-parameter freedom of (a, b) enters.** See
[Note F](notes/note-F-failure-localisation.md) and
[Note D](notes/note-D-comparison-ledger.md).

The sieve does not need adversarial β, only β = μ. With β = μ the measured law
is Σ_m |Σ_n μ(n)·1[mn ∈ A]| ≍ √(MX), fitting to ~2% over four dyadic ranges,
which is o(X) only for M = o(X) — the **same N^{1/2} wall** as Type I. So the
obstruction currently looks technical rather than structural: the truth appears
to have the required size, and what is missing is a method that can reach it.
See [Note H](notes/note-H-numerical-pilot.md).

**Blocking next step.** [Note C](notes/note-C-requirements.md) is deliberately
unfilled: it needs the asymptotic sieve's hypotheses quoted from the source,
not from memory. If the sieve requires a Type I level above Q^{1/2}, Step 1 has
found a second, prior obstruction and Step 2 is attacking the wrong half.

## Conventions

Fix one normalisation and keep it. Throughout:

- **Q** (or **N**) is the *norm* bound — the sieve's own variable, `n ≤ Q`.
- **X** = √Q is the range of x, so |A| = X for the x² + 1 sequence.
- "Level N^{1/2}" and "level X" are the same statement. Confusing the two is
  the easiest available mistake; the plan's §1.3.2 parenthetical is in the
  norm normalisation.
- Gaussian integers are `(a, b)` int pairs meaning a + bi. Ideals are named by
  their unit-normalised generator (Re > 0, Im ≥ 0).
