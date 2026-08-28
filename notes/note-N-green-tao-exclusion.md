# Note N — The Green–Tao exclusion, re-argued

*Not in the plan's deliverable list. Written because the plan's §Cross-cutting
rule — "**Don't** pursue Green–Tao / nilsequence methods; single-variable
polynomials are outside their scope" — was contested by Green–Sawhney and the
repo's no-go rule `green-tao-excluded` was left deliberately **non-fatal**
awaiting a re-argument from the actual paper. This is that re-argument.*

*Status: draft. Source read: Green & Sawhney, "Primes of the form p² + nq²",
[arXiv:2410.04189v3](https://arxiv.org/abs/2410.04189) (6 Jun 2026, accepted
Acta Math., 59 pp.), Sections 1–8 and Appendices A–C, from the PDF. Page numbers
are v3's and do **not** match v1/v2, which differ in §§8.3 and 8.7.*

## Verdict

> **The exclusion survives, and it survives for quantitative reasons stated in
> the paper — not because single-variable polynomials are "outside their
> scope".** The plan's rule is right in outcome and wrong in reason, and should
> be re-worded rather than kept.

## Why it was in doubt

Green–Sawhney obtain a Type II estimate **over Q(i)** — this repo's own setting
— using exactly the toolkit the plan excludes: Gowers norms, the concatenation
theorems of Kuca and Kravitz–Kuca–Leng, and the Leng–Sah–Sawhney
quasipolynomial inverse theorem. At n = 4 they settle Friedlander–Iwaniec's
Gaussian Primes Conjecture. A rule that excludes the only modern technique to
have reached anything in this shape needs a better justification than scope.

## Their object, and where ours sits inside it

Their weight (Definition 2.2, p. 8) is a **product over two free coordinates**;
in the Gaussian case they spell it out (p. 3) as

> w(x + 2iy) = f(x) f′(y), and w(x + iy) = 0 for y odd,

with f, f′ 1-bounded and supported on [±2n X^{1/2}]. So the support carries ~X
lattice points and total mass ~X, and **the trivial bound X in every hypothesis
is the mass of the two-dimensional box**.

Our A = {x + i} is the degenerate specialisation y ≡ 1, i.e. **f′ = δ₁**.

Their hypotheses (Definition 3.1, p. 9), for the record, are Type I to
X^{1/2}(log X)^{−C} and Type II on [(log X)^C, X^{3/8}] with savings
(log X)^{−12}, the Type II quantified over **any 1-bounded α_a, β_b** — the
arbitrary-coefficient class, matching [Note F](note-F-failure-localisation.md)'s
target exactly.

## Four independent reasons it dies at f′ = δ₁

**1. The hypotheses can never be satisfied.** Propositions 4.2 and 4.3 (pp. 20–21)
fire only when the relevant sum is ≥ δX with δ = (log X)^{−12}. With f′ = δ₁ the
total mass drops from ~X to Σ_a |w(a)| ≪ X^{1/2} log X. The propositions become
**vacuously true**: their premise is unreachable by a factor X^{1/2}.

**2. The conclusion carries no information either.** Their normalisation (4.12)
is ‖f‖_{U^k[N]} = ‖f‖_{U^k(ℤ)} / ‖1_{[N]}‖_{U^k(ℤ)}, with (4.13)
‖1_{[N]}‖^{2^k}_{U^k(ℤ)} ≍_k N^{k+1}. For a delta, ‖δ₁‖_{U^k(ℤ)} = 1 exactly, so

> ‖δ₁‖_{U^k[N]} = N^{−(k+1)/2^k}.

At k = 3 that is N^{−1/2}, genuinely small. But the k in Proposition 4.3 is, by
their own remark (Appendix B, p. 51), "roughly on the order of 2^347, that is to
say surprisingly close to a googol". At k ≈ 2^347 the exponent (k+1)/2^k is
astronomically small and **‖δ₁‖_{U^k[X^{1/2}]} = 1 − o(1) — maximal**. Prop 4.3
concludes "f and f′ have large Gowers norm"; for δ₁ that holds for every δ and
says nothing.

> The Gowers norm of a delta function is *maximal* at the k they need. The
> conclusion of their key proposition is satisfied trivially and vacuously by
> our sequence.

**3. The concrete step that breaks, before any concatenation.** Type II, (7.6)
p. 33: the inner sum runs over x, y in a box of side ~(X/L)^{1/2}, and
f₂ = f₄ = f′ (the imaginary-part functions, (7.4) p. 32). Setting f′ = δ₁
imposes **two linear conditions** on (x, y) — independent, because Q is chosen
with a′b − ab′ ≠ 0 at (7.3) p. 32 — so the inner sum has **at most one surviving
point**: the left side is ≤ 1 against a required ≫ δ^{26}·X/L. Type I, (6.13)
p. 29, dies the same way with one condition instead of two, collapsing a
(X/L)^{1/2} × (X/L)^{1/2} box to a line.

**4. The machine that manufactures the measures needs a second coordinate.**
The h-shift x ↦ x′ + b₁h, y ↦ y′ − a₁h (p. 33) translates along a lattice
direction *inside* the two-dimensional box; with one free variable there is no
such direction and no h-average to Cauchy–Schwarz over. Lemma 7.1 (p. 35), which
certifies that the convolved measures equidistribute, is a count over an
L²-sized family of quadruples.

## What would be needed, quantitatively

To make the degenerate case work one would need δ ~ X^{−1/2}, hence a
**power-saving** Gowers bound ‖Λ′ − Λ_Cramér‖_{U^k} ≪ X^{−c}. Their arithmetic
input, Proposition 4.4 (p. 21) quoting Leng at (4.17), supplies only

> ≪_A (log X)^{−A}, from a bound of shape e^{−(log X)^{c_k}}.

That is not a technicality to be improved; it is the difference between a
log-power and a power, in a theorem whose k is near a googol.

## And they say so themselves

Green and Sawhney name **x² + 4 with x prime — exactly y = 1** — as what their
method does not reach (p. 3).

## Re-worded rule

The plan's exclusion should read, in substance:

> Green–Sawhney is not a counterexample; reading it strengthens the exclusion.
> Their Gowers-norm machinery acts on the two **one-variable** coordinate
> functions of a product weight with both coordinates free over an interval of
> length X^{1/2}. Under the specialisation f′ = δ₁ their hypotheses are
> unsatisfiable (mass X^{1/2} against a required δX), their conclusions are
> vacuous (‖δ₁‖_{U^k} maximal at k ≈ 2^347), the Type II step collapses to at
> most one lattice point, and the measure-manufacturing shift has no direction
> to move in. Making it work would need a power-saving Gowers bound where only
> a log-power is known.

That is a **narrower and stronger** rule than "outside their scope", and it
explains why: this is the same α = 1/2 wall as everywhere else in the repo, seen
from the additive-combinatorics side.

## What does transfer, flagged honestly

Their Definition 3.1 and Lemma 3.2 — the Duke–Friedlander–Iwaniec sieve
transplanted to Ideals(O_K) — are stated for a **general** weight on ideals and
do not assume the product form. That part is reusable, and it is what
[Note C](note-C-requirements.md) already discusses.

**[VERIFY] discharged, against this note's first reading.** A reviewer flagged
that Proposition 3.4 might not be as general as 3.1 and 3.2. Read at source
(p. 17), it is not, and the paper says so twice:

> "In Section 3.1 these can be quite general, but for most of the paper we will
> take K = Q(√−n) and the weight functions will be of a **special product
> form**." (p. 8, introducing Definition 2.2)

> "Combining Lemmas 3.2 and 3.3 and taking A = 4 immediately leads to the
> following, which is **the only result from this section that we will need in
> what follows**. **Proposition 3.4.** … suppose that w : Ideals(O_K) → ℂ is in
> **product form (2.2)** with some frequency ℓ ∈ Z, and suppose moreover that
> f, f′ in that definition satisfy the pointwise bound
> |f(x)|, |f′(x)| ⩽ (Λ_Cramér + Λ′)(x)." (p. 17)

So the general machinery of §3.1 is set up and then **not exported**: the single
packaged conclusion carries the product-form hypothesis. The reusable surface is
smaller than this note first claimed, and nothing should lean on 3.4 as a
general ideal-sieve statement.

**But it does not supply a fifth failure, and it would be convenient to pretend
otherwise.** Two hypotheses of 3.4 that look like they might exclude f′ = δ₁
both hold:

- *Product form.* w(x + 2iy) = f(x)δ₁(y) **is** of the form (2.2). The
  degenerate case is inside their definition, not outside it.
- *The pointwise bound.* Λ′(1) = 0, since 1 is not prime, but
  Λ_Cramér(1) = ∏_{p⩽Q}(1 − 1/p)^{−1} ≍ e^γ log Q with
  Q = exp(log^{1/10}(X^{1/2})) at (1.7), so
  Λ_Cramér(1) ≍ e^γ·(½ log X)^{1/10} → ∞. Comfortably ≥ 1 = δ₁(1).

So A = {x + i} satisfies the *structural* hypotheses of Proposition 3.4 and
fails only its *quantitative* ones — which is reason 1 above, and is the same
α = 1/2 wall yet again. The exclusion is unchanged; its reason is narrower than
"the shape is wrong".

## Adversarial review

- *Two-parameter freedom smuggled in?* The opposite: this note is a catalogue of
  the places their argument uses the second variable, so the reasoning is
  entirely about where that freedom is spent.
- *Where is parity broken?* In their argument, at the Gowers-norm Type II input.
  This note establishes that the input is unavailable at f′ = δ₁; it does not
  supply a replacement.
- *Is the exclusion being kept for comfort?* That was the risk, and it is why the
  rule was left non-fatal and the paper read rather than argued from. The four
  reasons above are quantitative and each is independently fatal, which is more
  than the original rule had.
- *Reviewer corrections applied.* One quoted display, (7.6)'s right-hand side,
  was transcribed with a fraction the page does not print; it is recorded here as
  δ^{26}·X/L following the surrounding text, and anyone relying on the exact form
  should read p. 33. One further plank of the original argument — that isolating
  Im z = 1 needs angular frequencies ~X^{1/2} beyond their |ℓ| bounds — was
  **dropped** as inflated: Definition 2.2 permits f′ to be an arbitrary function,
  so no Fourier expansion in the angle is forced.
