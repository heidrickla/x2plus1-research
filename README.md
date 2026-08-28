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
| [research_state/claims.json](research_state/claims.json) | every claim with an enforced epistemic status — `proved` / `quoted` / `measured` / `inferred` / `refuted` — checked by `tests/test_claims.py`. |

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

```bash
python experiments/exp04_kappa_family.py 10000000 6
```

No installation needed — the scripts put the repo root on `sys.path`. Requires
Python ≥ 3.11 with `sympy` and `numpy`.

## State of play

**The obstruction is Type II, and it is [Note F](notes/note-F-failure-localisation.md)'s
C₄-free lemma.** That took three revisions to get right; the earlier framings
are kept as `refuted` entries in
[`research_state/claims.json`](research_state/claims.json).

Friedlander–Iwaniec's asymptotic sieve requires Type I to level **D > x^{2/3}**
((R1), ASP p. 1043), which x² + 1 cannot reach — [Note B](notes/note-B-type-I.md)
caps it at x^{1/2}. And ASP p. 1045 shows x^{2/3} is precisely where the
bilinear coefficient γ(n,C) is annihilated, so within ASP the two hypotheses are
one. **But x^{2/3} is ASP's threshold, not prime detection's:**

| | ASP | **DFI** (used by Green–Sawhney) |
|---|---|---|
| Type I needed | x^{2/3} | **x^{1/2}(log X)^{−C}** |
| x² + 1 meets it? | ❌ short by x^{1/6} | ✅ **yes** ([Note B](notes/note-B-type-I.md)) |
| Type II coefficients | μ, truncated | **arbitrary 1-bounded** |
| x² + 1 meets it? | vacuous (γ ≡ 0) | ❌ **fails outright**, θ ≈ 1.000 |

So a level-1/2 prime-detecting sieve exists and is in current use, x² + 1
satisfies its Type I hypothesis, and the whole obstruction lands on Type II —
where the incidence graph being C₄-free means the worst case has **no
cancellation at any split**. With β = μ the same ranges give θ = 0.63–0.83; it
is specifically the arbitrary-coefficient requirement that fails.

Ford–Maynard map the parameter space and put x² + 1 on a knife-edge: their
Thm 4.16 gives C⁻ = 0 for γ < 1/2 outside [θ, θ+ν], and Thm 2.4 gives C⁻ = 0 at
**γ = 1/2 with ε losses**, escaping only via divisor-bounded weights. Two sieves
break parity below x^{2/3} — Li unconditionally to ≈ x^{0.6418}, Merikoski
conditionally at 5/8 — and neither reaches x^{1/2}. Maynard's ICM survey asks
(Question 21) whether adapting them below 1/2 is even plausible.

**Supersession scan: Iwaniec 1978 still stands.** Green–Sawhney
([arXiv:2410.04189](https://arxiv.org/abs/2410.04189), Acta Math.) settle FI's
Gaussian Primes Conjecture at n = 4, but their sequence has **α = 1** — sharing
Dirichlet's rung, not thin at all — so the plan's exclusion of Green–Tao methods
survives on its stated grounds. Merikoski's sparse-set work
([arXiv:2302.11331](https://arxiv.org/abs/2302.11331)) runs at α ≈ 1 − δ, and
b = 1 is off its chart rather than a limit of it.

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

- **Read Duke–Friedlander–Iwaniec §6 directly** (*Ann. of Math.* **141** (1995),
  423–441). Everything above about DFI is at two removes, and the claim that
  x² + 1 *meets* its Type I hypothesis is `inferred` and load-bearing.
- **Ford–Maynard Thm 2.4's escape is divisor-bounded weights**, which is the DFI
  setting. Does it apply to x² + 1's weight or exempt it? Sharpest live question.
- Iwaniec 1978 is second-hand (paywalled); BFI I–III and *Opera de Cribro*
  Ch. 24–25 unobtained.
- [Note G](notes/note-G-spectral.md) is still a skeleton, and Note F's lemma
  says it may have nothing to act on.

## Conventions

Fix one normalisation and keep it. Throughout:

- **Q** (or **N**) is the *norm* bound — the sieve's own variable, `n ≤ Q`.
- **X** = √Q is the range of x, so |A| = X for the x² + 1 sequence.
- "Level N^{1/2}" and "level X" are the same statement. Confusing the two is
  the easiest available mistake; the plan's §1.3.2 parenthetical is in the
  norm normalisation.
- Gaussian integers are `(a, b)` int pairs meaning a + bi. Ideals are named by
  their unit-normalised generator (Re > 0, Im ≥ 0).
