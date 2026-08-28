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

Note C is answered from the sources ([ASP](https://arxiv.org/abs/math/9811186),
[X2Y4](https://arxiv.org/abs/math/9811185),
[HB](https://ora.ox.ac.uk/objects/uuid:ebb25eb4-a19e-4049-8117-3269e140b0fe)).

**The asymptotic sieve for primes, as stated, does not apply to x² + 1.**
Hypothesis (R1) needs a level of distribution D > x^{2/3} (ASP p. 1043), and
[Note B](notes/note-B-type-I.md) proves this sequence caps at D ≤ A(x) = x^{1/2}.

**And "Type I or Type II?" turns out to be a false dichotomy.** ASP p. 1045:

> "Here d must be quite a bit smaller than N to ensure that μ(d) does not
> completely neutralize μ(n). By (B1–B3) we know that d < C < (x/Δ)·N·D^{−3/2},
> so our hypothesis (B) can be realistic only if D is somewhat larger than
> x^{2/3+ε}."

x^{2/3} is the threshold below which the bilinear hypothesis is *vacuous*: the
truncation C = xD^{−1} must stay under N ≈ √D, or γ(n,C) = Σ_{d|n, d≤C} μ(d)
collapses to Σ_{d|n} μ(d) = 0. So (R1) is the condition that (B) has content,
and one fact — no room for the parity-breaking mechanism at A(x) = x^{1/2} —
surfaces three ways:

| symptom | where |
|---|---|
| (R1) unsatisfiable: D ≤ A(x) = x^{1/2} < x^{2/3} | [Note B](notes/note-B-type-I.md) |
| (B) vacuous: C = x^{1/2} against N ≈ x^{1/4}, so C/N ≈ x^{1/4} | [Note C](notes/note-C-requirements.md) |
| incidence matrix is a forest: κ = 1 | [Note F](notes/note-F-failure-localisation.md) |

Combining C ≲ √D with D ≤ A(x) re-derives the sieve's density threshold
**A(x) ≳ x^{2/3}** from the mechanism rather than from a hypothesis.

| sequence | α | κ > 1? | (R1) | level achieved |
|---|---|---|---|---|
| a² + b⁴ (FI 1998) | 3/4 | ✅ | ✅ met | x^{3/4−5ε} |
| x³ + 2y³ (HB 2001) | 2/3 | ✅ | ❌ short by **x^ε** — HB wrote his own sieve | x^{2/3−ε} |
| x² + 1 | **1/2** | ❌ (κ = 1) | ❌ short by **x^{1/6}** | x^{1/2}(log x)^{−222} |

Heath-Brown judged (R1) "possible … to relax" for a gap of ε; this needs a
sixth of an exponent, where the coefficient does not weaken but vanishes. The
record at α = 1/2 remains Iwaniec 1978: P₂, from a lower-bound weighted sieve.

**Supersession scan: run, and Iwaniec 1978 still stands.** The nearest recent
result is Green–Sawhney, *Primes of the form p² + nq²*
([arXiv:2410.04189](https://arxiv.org/abs/2410.04189), 2024) — an asymptotic
for p² + nq² with p, q prime, n ≡ 0, 4 (mod 6), settling FI's "Gaussian primes
conjecture" at n = 4, over **Q(i)**. Unread, and the highest-value item in the
repo. Their Type II input is Gowers-norm technology, which the plan's
§Cross-cutting rules out — that exclusion now needs re-arguing rather than
standing unexamined.

### The two supporting results

**Type I stops at Q^{1/2}, sharply.** Divisibility by a Gaussian ideal is
exactly one residue class mod N(d), so |r_d| ≤ 1 — and that is best possible,
since an interval of length X meets a class in ⌊X/q⌋ or ⌈X/q⌉ points. The
admissible ideals of norm ≤ D number ~(3/2π)·D — the residue of
ζ(s)L(s,χ₄)/ζ(2s), measured at 0.4771 against a predicted 0.47746, which
validates the harness. So Σ|r_d| ≍ D must be o(|A|) = o(Q^{1/2}).
[Note B](notes/note-B-type-I.md).

**The Type II incidence matrix is a forest, provably.** Writing
G(n₁, n₂) = #{m : mn₁ ∈ A and mn₂ ∈ A} — the sum every dispersion argument must
evaluate:

> **Lemma.** For A = {x + i}, G(n₁, n₂) ≤ 1 whenever n₁ ≠ n₂.
>
> *Proof.* A 4-cycle gives a₁a₄ = u·a₂a₃ for a unit u. Since (x+i)(y+i) =
> (xy−1) + i(x+y) has Re ≥ 0 and Im ≥ 2 for x, y ≥ 1, both sides lie in the
> first quadrant, forcing u = 1; then x₁+x₄ = x₂+x₃ and x₁x₄ = x₂x₃, so
> {x₁,x₄} = {x₂,x₃}, which collapses the cycle. ∎

So there is no congruence to detect, no exponential sum, no Weil bound — the
count is already 0 or 1. Measured dispersion exponent: **θ = 1.00–1.03 at every
split, worse than trivial.** From the density side, mean degrees satisfy
D_m·d_n ≍ |A|²/Q =: κ independent of the split, so max over splits of
min(D_m, d_n) ≍ √κ = |A|/Q^{1/2} — **exactly 1** for x² + 1 and ≍ Q^{1/4} for
a² + b⁴ (predicted 48.7, measured 41.2 at Q = 10⁷; maximum off-diagonal Gram
entry 1 versus **667**). [Note F](notes/note-F-failure-localisation.md).

κ turns out to be exactly the condition for FI's required bilinear range (B1)
to be non-degenerate: (B1) forces M ≥ √x, cancellation forces M ≤ A(x), and
both hold iff κ > 1. That was not built in — it is a consistency check between
the repo's derived invariant and the paper's stated hypothesis. In the window
(B1) actually requires, the measured bilinear sum shows **no saving at all**
(S_μ/A(x) = 0.93, 1.00, 1.01), which corrects the earlier reading in
[Note H](notes/note-H-numerical-pilot.md).

### The density ledger

| sequence | A(x) | κ > 1? (Type II non-degenerate) | A(x) > x^{2/3}? (ASP applies) |
|---|---|---|---|
| a² + b⁴ (FI 1998) | x^{3/4} | ✅ | ✅ — D = x^{3/4−5ε} achieved |
| x³ + 2y³ (Heath-Brown 2001) | x^{2/3} | ✅ | at the boundary **[VERIFY]** |
| x² + 1 | **x^{1/2}** | ❌ (κ = 1) | ❌ |

### Not yet done

- **Read Green–Sawhney**, then decide whether the plan's Green–Tao exclusion
  survives. Other unread leads:
  [arXiv:2302.11331](https://arxiv.org/abs/2302.11331) (Gaussian primes in
  sparse sets — our problem is its sparse set having one element),
  [arXiv:2407.14368](https://arxiv.org/abs/2407.14368),
  [arXiv:2112.03617](https://arxiv.org/abs/2112.03617).
- **The scan was three searches, not a literature review.** Enough to say
  nothing obvious supersedes Iwaniec 1978; not enough to be sure.
- **Iwaniec 1978 is second-hand.** The original is paywalled; its statement and
  method were read from an MSc exposition.
- **[Note G](notes/note-G-spectral.md) is still a skeleton**, and Note F's
  lemma says it may have nothing to act on.
- **Reading-list items 6–9 (BFI, EGM, Motohashi, Zhang/Polymath/Maynard) were
  deliberately skipped**, with the reasoning written out at the end of
  [refs/bibliography.md](refs/bibliography.md). In short: the spectral sources
  estimate Kloosterman sums and Note F shows there are none here, and the
  large-moduli sources raise the level for a *dense* sequence, which cannot
  lift a counting bound that comes from |A| itself. That is reasoning, not a
  reading of those papers.

## Conventions

Fix one normalisation and keep it. Throughout:

- **Q** (or **N**) is the *norm* bound — the sieve's own variable, `n ≤ Q`.
- **X** = √Q is the range of x, so |A| = X for the x² + 1 sequence.
- "Level N^{1/2}" and "level X" are the same statement. Confusing the two is
  the easiest available mistake; the plan's §1.3.2 parenthetical is in the
  norm normalisation.
- Gaussian integers are `(a, b)` int pairs meaning a + bi. Ideals are named by
  their unit-normalised generator (Re > 0, Im ≥ 0).
