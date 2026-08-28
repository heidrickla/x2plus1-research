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

**Note C is answered, and it reorders the programme.** Reading Friedlander–
Iwaniec directly ([arXiv:math/9811186](https://arxiv.org/abs/math/9811186),
[arXiv:math/9811185](https://arxiv.org/abs/math/9811185)):

> **The asymptotic sieve for primes cannot be applied to x² + 1, and the
> obstruction is Type I, not Type II.**

Hypothesis (R1) requires a level of distribution **D > x^{2/3}** (ASP p. 1043).
FI also note, p. 1044, that "for thin sequences A one cannot expect (R) to hold
with D(x) > A(x)". For x² + 1, A(x) = x^{1/2} < x^{2/3}: **the admissible range
for D is empty.** The sieve's own density threshold is stated outright at
p. 1059 — it needs **A(x) ≥ x^{2/3+2ε}**. Details, with the hypotheses quoted
and three independent failure modes, in [Note C](notes/note-C-requirements.md).

So Step 2 of the plan — the whole bilinear programme — is downstream of a
constraint that binds first. The live question is now:

> **Is there a version of the asymptotic sieve for primes valid for sequences
> with A(x) ≍ x^{1/2}?** Equivalently: where in ASP §§3–8 is the x^{2/3} spent?

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

The plan's required literature scan (does anything supersede Iwaniec 1978 or
FI 1998?) has **not** been run — only the 1998 hypotheses have been verified.
See [refs/literature-log.md](refs/literature-log.md), which also flags
[arXiv:2112.03617](https://arxiv.org/abs/2112.03617) as unread and relevant.

## Conventions

Fix one normalisation and keep it. Throughout:

- **Q** (or **N**) is the *norm* bound — the sieve's own variable, `n ≤ Q`.
- **X** = √Q is the range of x, so |A| = X for the x² + 1 sequence.
- "Level N^{1/2}" and "level X" are the same statement. Confusing the two is
  the easiest available mistake; the plan's §1.3.2 parenthetical is in the
  norm normalisation.
- Gaussian integers are `(a, b)` int pairs meaning a + bi. Ideals are named by
  their unit-normalised generator (Re > 0, Im ≥ 0).
