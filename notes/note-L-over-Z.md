# Note L — The same question over Z, and over every degree

*Added. Status: draft. Supported by
[`exp09`](../experiments/exp09_degree_ladder.py),
[`x2plus1/polyseq.py`](../x2plus1/polyseq.py), and
`tests/test_polyseq.py`. Two of the measurements were reproduced independently
by a second session before being recorded here.*

This note exists because of a scope question nobody had asked:

> [Note F](note-F-failure-localisation.md)'s lemma is about the **Gaussian**
> incidence graph — m and n range over ideals of Z[i]. The Type II hypothesis
> of [ASP], [DFI] and [FM] is stated over **Z** — m and n are rational
> integers, and w is indexed by integers. Those are not the same bilinear form.

A rational modulus m carries several Gaussian ideals of norm m, so the rational
graph is a *coarsening* of the Gaussian one, and merging rows can only create
4-cycles. Note F is proved and true; the question is what it implies about the
object the literature's hypotheses are about.

## The rational graph is not C₄-free

Same sequence, same X = 4000, same modulus window m ∈ [60, 120):

| formulation | max off-diagonal Gram |
|---|---:|
| Gaussian ideals (Note F) | **1** |
| rational integers | **2** |

An explicit 4-cycle, verified term by term:

> n₁ = 1189, n₂ = 71978
>
> m = 65 : 65·1189 = 278² + 1  65·71978 = 2163² + 1
> m = 109 : 109·1189 = 360² + 1  109·71978 = 2801² + 1

The mechanism is visible in the repo's own machinery: 65 has **four** admissible
Gaussian ideals (roots 8, 18, 47, 57 of ν²+1 ≡ 0 mod 65) against 109's two, so
the single rational row m = 65 merges four Gaussian rows.

## What a rational 4-cycle actually is

A 4-cycle m₁n₁, m₁n₂, m₂n₁, m₂n₂ ∈ A gives

> (x₁²+1)(x₄²+1) = (x₂²+1)(x₃²+1),  {x₁,x₄} ≠ {x₂,x₃}

— a **multiplicative coincidence among values of x²+1**. In Z[i]: a₁a₄ and a₂a₃
have the same norm without being associates. Note F's proof excludes the
*associate* case, by the first-quadrant argument. It says nothing about the
same-norm-non-associate case, and cannot: an integer M has r₂(M)/4 essentially
distinct representations as a sum of two squares, and Note F's lemma is not
about r₂.

That this is more than conjugation was checked and is worth recording, because
"conjugate one factor" is the obvious guess and it is wrong. Of the 504
coincidences with x ≤ 1200, only **332** have a₁ā₄ ∼ a₂a₃; the other **172** do
not. The smallest is

> (1²+1)(18²+1) = (3²+1)(8²+1) = 650,

and 650 = 5² + 25² = 11² + 23² = 17² + 19² has three representations, of which
conjugation reaches two. So the rational coincidences are governed by r₂ in
full, not by the Galois action alone.

## How much of it there is

**Multiplicative coincidences are sparse, and their number grows like X, not
X².** Counting products (x₁²+1)(x₄²+1) over x₁ ≤ x₄ ≤ X:

| X | pairs | colliding values | excess representations | max reps |
|---:|---:|---:|---:|---:|
| 300 | 45 150 | 126 | 131 | 3 |
| 600 | 180 300 | 251 | 256 | 3 |
| 1 200 | 720 600 | 490 | 497 | 3 |
| 2 400 | 2 881 200 | 905 | 916 | 3 |

The excess roughly doubles when X doubles (ratios 1.95, 1.94, 1.84), so over
this range it is consistent with ≍ X against ≍ X² pairs. The drift in the
implied exponent (0.96 → 0.88) is larger than the range can resolve, so **no
asymptotic law is being claimed here** — the table is `rigorous_finite` and
stops there. What it does settle is the order of magnitude: the 4-cycle count is
nothing like the X²/M mass a dispersion main term would need.

**On any dyadic window the Gram is 2, uniformly in X. On the full graph it
grows.** Reproduced independently:

| X | full graph | worst dyadic [M, 2M) |
|---:|---:|---:|
| 500 | 6 | 2 |
| 1 000 | 7 | 2 |
| 2 000 | 7 | 2 |
| 4 000 | 8 | 2 |
| 8 000 | 9 | 2 |

The full-graph maximum is always attained at (n₁, n₂) = (1, 5), and that is a
**Pell equation**: G′(1,5) counts m with m ∈ A and 5m ∈ A, i.e. y²+1 = 5(x²+1),
i.e. **y² − 5x² = 4**, whose solutions are x = F₂ₖ, y = L₂ₖ. Enumerated to
x ≤ 10⁷:

> m = 2, 10, 65, 442, 3026, 20737, …, 32 522 920 134 770

with consecutive ratios converging to **6.8541 = φ⁴**. Geometric spacing at that
rate puts at most one solution in any dyadic window — which is exactly why the
full graph grows like log X while every window stays at 2.

Two conclusions follow, and they point the same way. n₁ = 1 cannot occur in a
Type II hypothesis, where both variables are confined to ranges; and even where
Pell families do occur, a range restriction sees O(1) of each. **The windowed
statement is the faithful one, not a patch.**

## Why the window bound holds: one solution per class, and the constant is φ⁴

The uniformity of that "2" is not a coincidence, and the mechanism identifies
the extremal case.

> **Proposition L.1.** Let n₁ ≠ n₂ be positive integers, d = gcd(n₁, n₂),
> n₁ = da, n₂ = db with (a, b) = 1. Then m ∈ S(n₁) ∩ S(n₂) — i.e. mn₁ and mn₂
> are both of the form x²+1 — if and only if
>
>     b x² − a y² = a − b
>
> has a solution with mn₁ = x²+1. Assume ab is not a square (otherwise the form
> factors and the solution set is finite). The solutions fall into finitely many
> classes, each an orbit under multiplication by the fundamental norm-one unit ε
> of the relevant real quadratic order. Consecutive solutions in a class satisfy
> x′/x → ε, hence **m′/m → ε² ≥ φ⁴ = 6.8541…**, so a dyadic window [M, 2M)
> contains at most one member of each class, and
>
>     G′(n₁, n₂) restricted to a dyadic window ≤ (number of classes).

**The extremal case is the observed argmax.** ε ≥ φ² = 2.618… over real
quadratic orders, with equality at discriminant 5 — and discriminant 5 is
exactly the pair (n₁, n₂) = (1, 5), whose equation is y² − 5x² = 4 and whose
solutions are the Fibonacci/Lucas pairs. So the constant that bounds the
spacing, and the pair that attains the full graph's maximum, are the same
object. Measured ratios for that family converge to 6.8541 = φ⁴, as they must.

Both halves of the earlier table follow: within a class the spacing is ≥ φ⁴ > 2,
so windows see one; across all M the number of visible solutions is ≍ log X,
which is the full graph's growth.

**Status, corrected: the class count is unbounded, so the proposition does not
reach the constant 2.**

The reduction to the conic is algebra and is proved. That ε ≥ φ² is
`rigorous_finite`: checked by solving t² − Δu² = 4 for every non-square Δ < 5000,
minimum 2.618033989 at Δ = 5. **But the bound on the number of classes is not a
constant.** A parallel session located it in Dickson, *Introduction to the Theory
of Numbers* (1929), §46 pp. 73–75 and §71 p. 115: for
q = [b, 0, −a] of discriminant 4ab and m = a − b, with gcd(a,b) = 1 forcing
gcd(ab, a−b) = 1, the class count is bounded by

> 2^r (4 ∤ M), 2^{r+1} (4 | M, 8 ∤ M), 2^{r+2} (8 | M), r = #odd primes | M,

i.e. **2^{ω(|a−b|)+O(1)} = O_ε(|a−b|^ε)** — unbounded. *(Read by that session,
not here; second-hand until this repo opens Dickson.)* So Proposition L.1 yields

> G′(n₁, n₂) on a dyadic window ≪_ε |n₁ − n₂|^ε,

**and not the 2 that both of us measured.** The measurement stands; the proof no
longer reaches it, and saying so is the point of writing the status separately
from the statement.

**What the measurement actually says, searched exhaustively.** Bucketing every
reduced ratio (y²+1)/(x²+1) for x < y ≤ 3000 finds each pair (a, b) together
with *all* its shared moduli — 2014 pairs with ≥ 2, the largest with **8**. Yet:

| (a, b) | shared moduli | max in one dyadic window |
|---|---|---:|
| (1, 5) | 2, 10, 65, 442, 3026, 20737, … (8) | **1** |
| (1, 13) | 2, 5, 170, 530, 20165, 63002 (6) | **1** |
| (1, 10) | 5, 17, 325, 6401, 23717, 467857 (6) | **1** |
| (1, 85) | 2, 17, 26, 290, 10001 (5) | **2** |
| (1, 65) | 5, 50, 82, 901, 16385 (5) | **2** |
| (5, 481) | 2, 97, 146, 7450 (4) | **2** |

So the classes are real and there are many of them — but **the classes are
themselves spread across windows**. Over *every* ratio class, not a sample:

| X | classes with ≥ 2 shared moduli | window max = 1 | = 2 | **= 3** |
|---:|---:|---:|---:|---:|
| 3 000 | 2 014 | 1 636 | 378 | **0** |
| 6 000 | 3 916 | 3 167 | 749 | **0** |

**Never three.** A parallel session reached the same wall from the other side —
580 pairs achieving Gram 2 for X ≤ 8000, with Dickson class bounds of 2, 4, 8,
16 and 32, and every one of them giving exactly 2.

**A tempting reformulation, and it is false.** It is natural to argue: members
of one class are ε² ≥ φ⁴ ≈ 6.85 apart while a window has ratio 2, so two moduli
in one window must come from two different classes. Both sessions reached that
statement. It does not survive an exact orbit computation.

> **Counterexample.** (n₁, n₂) = (2, 85), conic 85x² − 2y² = −83.
> (x, y) = (11, 72) and (15, 98) both solve it, giving
> m = (11²+1)/2 = (72²+1)/85 = **61** and m = (15²+1)/2 = (98²+1)/85 = **113**,
> with 113/61 = 1.85 < 2 — one window. The fundamental unit is
> (t, u) = (339, 26), ε² = 678, and
>
>     A(11, 72) = (7473, 48718),  A⁻¹(11, 72) = (**−15**, 98).
>
> So (15, 98) is A⁻¹(11, 72) *with the sign of x flipped*. x ↦ −x is the
> **improper** automorph: it is not in {±Aᵏ}, so the two solutions lie in a
> proper class and its **opposite** — and m depends on x², which cannot see the
> difference.

So a single class-up-to-conjugation can put two moduli in one window, and the
ε² spacing bound simply does not apply across the improper pairing. Exact orbit
grouping (union–find under A, A⁻¹ and x ↦ −x) at X = 3000 confirms the scale of
it: of the classes attaining window maximum 2, **202 have only one such orbit
populated** — those are all improper pairs — against 159 with two and 14 with
three or more.

**What is actually measured**, then, is weaker and stranger than the
reformulation claimed:

> **no ratio class ever puts three moduli in one dyadic window**, whether they
> come from one orbit, two, or five — and 32 have three or more orbits populated.

The proper-class spacing explains at most one modulus per proper class; the
improper pairing explains a second; **nothing explains the absence of a third.**

### The absence of a third is a gap, not a scarcity

Three moduli in one window is exactly m_{i+2}/m_i < 2, so the statistic to look
at is the *two-step* ratio. Over every ratio class:

| X | classes with ≥2 m | with ≥3 m | min m_{i+1}/m_i | min m_{i+2}/m_i |
|---:|---:|---:|---:|---:|
| 1 500 | 1 025 | 55 | 1.0783 | **13.0000** |
| 3 000 | 2 014 | 74 | 1.0547 | **13.0000** |
| 5 000 | 3 319 | 109 | 1.0412 | **13.0000** |

Consecutive ratios get arbitrarily tight — 1.041 at X = 5000, and falling — while
the two-step minimum sits at **exactly 13** and does not move as the triple count
doubles. The threshold for a violation is 2. That is a margin of 6.5, stable.

**And the lower tail is a cluster, not an approach.** The nine smallest two-step
ratios at X = 5000 are

> 13.00, 14.50, 14.80, 14.90, 15.16, 16.40, 17.06, 17.55, 18.02

and then the next is **32.5**. Nothing in (18.02, 32.5); nothing below 13; median
819. So there is a floor with a cluster resting on it, which is the shape a
theorem makes, not the shape chance makes. Both sessions independently reached a
probability model predicting that three-in-a-window should be merely improbable;
a gap pinned at 13.0000 across a doubling of the triple count is not improbability.

**Every one of the twenty smallest two-step ratios has a = 1.** That is
n₁ = d and n₂ = db — *one cofactor divides the other*. The b values are 85, 533,
901, 65, 5, 325, 365, 1450, 2465: all products of primes ≡ 1 (mod 4), as
admissibility forces. So whatever bounds the two-step ratio from below is a
statement about the conic **y² − b x² = b − 1**, and the extremal case is
(a, b) = (1, 85) with x = 1, 4, 5 — which is not three near-coincident solutions
at all, but a tight pair (m = 17, 26, ratio 1.53) plus a distant third (m = 2).

That is the reduction worth attacking: a **gap principle** separating distinct
proper classes of a fixed binary quadratic form. Neither session has the
citation, and the measurement stands on its own until one turns up.

**Dickson's side condition does not recover it.** The condition that would force
the class bound to 2 is |a−b| odd with at most one odd prime factor. Of the
classes attaining a window maximum of 2, only **19%** satisfy it at X = 3000 and
**15%** at X = 6000 — and the other 85% attain exactly 2 as well. The constant is
not coming from a small class count.

**Does N^ε still suffice for the conclusion?** Probably, and it is worth being
explicit that this is reasoning: dispersion needs *count = main term + error*,
and O_ε(N^ε) with no structure supplies no main term any more than 2 does. So
the conclusion should survive with a weaker constant. That step is `inferred`,
and it is exactly the shape of claim this repo has had to withdraw before.

The window sweep extends the table above to X = 32 000, still 2 everywhere:

| M | 128 | 256 | 512 | 1024 | 2048 | 4096 | 8192 |
|---|---|---|---|---|---|---|---|
| max Gram | 2 | 2 | 2 | 2 | 2 | 2 | 2 |

## So Note F's conclusion transfers, and here is exactly how much is proved

- **Proved, Z[i]:** G(n₁,n₂) ≤ 1, at every split and on the full graph
  ([Note F](note-F-failure-localisation.md)).
- **Measured, Z:** G′(n₁,n₂) ≤ 2 on every dyadic window tested, uniformly for
  X ≤ 8000; the full graph reaches 9 at X = 8000 and grows like log X, driven by
  Pell families at n₁ = 1.
- **Inferred:** that boundedness persists for all X. A Gram entry of 2 has no
  more of a main term than one of 1 — dispersion needs *count = main term +
  error*, and a uniformly bounded count supplies no main term at any constant.
  So the conclusion is unchanged and the constant is all that moves.

What would close the gap is a uniform bound on integer points of the conic
n₂x² − n₁y² = n₁ − n₂ in a box — classical Pell theory, but **this repo has not
read a source for it**, and per the repo's own rule the exponent is not being
asserted from memory. Until then the Z[i] → Z step is `inferred`, and
`selberg-nu-zero-binds` rests on it.

## The larger result: it was never about x² + 1

The same harness answers a question the repo had not asked. For
A = {f(x) : x ≤ X} with deg f = d, the norm bound is Q ≍ X^d and |A| = X, so

> **α = 1/d**  and  **κ = |A|²/Q = X^{2−d}**

with no dependence on f beyond its degree. Then κ > 1 only at d = 1, κ = 1
exactly at d = 2, and κ < 1 for every higher degree. Measured over Z, sweeping
dyadic windows to √Q at X = 4000 ([`exp09`](../experiments/exp09_degree_ladder.py)):

| f | d | α | κ | max Gram | at M |
|---|---:|---:|---:|---:|---:|
| 2x + 1 | 1 | 1.000 | 2000 | **32** | 64 |
| x² + 1 | 2 | 0.500 | 1 | 2 | 8 |
| x² + x + 1 | 2 | 0.500 | 0.9998 | 2 | 16 |
| x³ + 2 | 3 | 0.333 | 0.00025 | 1 | 2 |
| x⁴ + 1 | 4 | 0.250 | 6.25 × 10⁻⁸ | 1 | 2 |

The Gram is bounded for every d ≥ 2 and grows with the window at d = 1.

**The ladder recovers the known case at its top end**, which is the check that
matters: d = 1 is primes in arithmetic progressions, κ = X, and the bilinear
form has everything to work with — Dirichlet. A classification that did not
return the solved case there would be evidence against itself.

And Ford–Maynard's placement generalises the same way. For A = {f(x)},
|J| = Q^{1/d}, so c = 1 − 1/d ≥ 1/2 for every d ≥ 2, which collides with
(1.1)'s θ < 1/2 exactly as it does at d = 2 ([Note C](note-C-requirements.md)).
Computed by `x2plus1.exponents.ford_maynard_theta`, which returns a range at
d = 1 and raises for every d ≥ 2.

> **No single-variable polynomial sequence of degree ≥ 2 has an admissible
> Ford–Maynard triple; κ ≤ 1 for all of them; and d = 1 is the only
> single-variable degree with anything for a bilinear form to cancel.**
> x² + 1 is the *least degenerate member of a degenerate class*, not a special
> case.

That is a uniform account of why every single-variable Landau-type question is
stuck, and it makes Note F an instance of something general rather than a fact
about one polynomial. It is also, deliberately, not a claim about truth — it is
a claim about what the Type I/II framework can express, and the standing warning
on C⁻ = 0 applies here verbatim.

### Li names the mechanism from the other side

Xiannan Li, [arXiv:2111.05403](https://arxiv.org/abs/2111.05403), p. 2, on what
makes a bilinear estimate tractable:

> "With current methods, in order to understand such bilinear sums, it is
> crucial that these sequences are all **special values of norm forms** of some
> number field. Given this, there are two main factors which affect the
> difficulty of the problem. The first … is that the problem tends to be more
> difficult the sparser the sequence. The second is that for certain homogeneous
> polynomials, such as a³ + 2b³, estimating the bilinear sum involves **a
> restriction of a variable to a one dimensional lattice**, and this makes the
> problem more tractable."

x² + 1 = N(x+i) satisfies the norm-form condition — that is
[Note A](note-A-dictionary.md) — and fails the second, because a restriction of
*a variable* needs a variable to restrict. That is this note's ladder, named
from inside the technique rather than from the exponents. He also states the
boundary: both the asymptotic sieve and Harman's "fail to prove asymptotic
estimates for sequences with exponential density strictly lower than 2/3."

### What is already in print, and what is not

*Rewritten after a folklore sweep found the prior art. The first version of this
section claimed the Type I/II admissibility statement was "not found in the
literature by two independent sweeps". That was true of the sweeps and false of
the literature.*

**Maynard states the density form of this barrier, twice.**

[arXiv:1507.05080v2](https://arxiv.org/abs/1507.05080), p. 1:

> "A non-linear polynomial f represents O(x^{1/2}) integers less than x, and
> **there are essentially no examples of sets containing O(x^{1/2}) integers
> less than x which contain infinitely many primes** (beyond artificial
> examples). Thus the sparsity of the set of values of f presents a major
> obstacle."

and the ICM survey *Counting primes*, §7:

> "all approaches seem to break down completely when considering sets containing
> fewer than x^{1/2} elements in [x, 2x].
>
> **Question 21.** Is there a plausible way to adapt Type I/II machinery to
> apply to very sparse sets with x^{1/2−ε} elements in [x, 2x]?"

So this repo did not find an unrecorded barrier. **It re-derived Maynard's
density heuristic and pushed it one step.** Three things survive as genuinely
this repo's, and they are narrower:

1. **Indexing the barrier by degree.** α = 1/d, hence c = 1 − 1/d ≥ 1/2 for
   every d ≥ 2, hence no admissible Ford–Maynard triple — that chain appears in
   no source either sweep found. Maynard's O(x^{1/2}) is the d = 2 bound used as
   a uniform *upper* bound; the per-degree statement is not drawn.
2. **Locating Landau's problem at the boundary rather than inside it.** Maynard
   attaches Question 21 to **Legendre's conjecture** — "thereby addressing
   Legendre's conjecture on the existence of a prime between consecutive
   squares" — not to n² + 1. And the two sit differently:
   #{n : n²+1 ∈ (x, 2x]} = (√2 − 1)√x + O(1) ≍ **x^{1/2}**, which is *not*
   x^{1/2−ε} for any ε > 0. **x² + 1 is exactly on Question 21's boundary, not
   inside it.**
3. **Evaluating Ford–Maynard's triple framework against a one-variable
   polynomial.** Their paper does not, and no other source found does.

That is a smaller claim than the first draft made, and the right one: *indexing
a known density barrier by polynomial degree, and locating Landau's fourth
problem exactly at its boundary* — not discovering an unrecorded barrier.

And it leaves the three d-uniform statements properly separated:

| statement, for every degree | status |
|---|---|
| **almost-primes**: p(f) ≤ deg f + 1 | known and old — Bukhstab 1967, Pintz §19 |
| **primes**, degree ≥ 2 | unknown, and Pintz and Maynard both say so |
| **Type I/II admissibility**, degree ≥ 2 | not found in print; this repo's, narrowly |

## Adversarial review

- *Two-parameter freedom smuggled in?* No — the point runs the other way. The
  degree ladder is the statement that one parameter is never enough, and d = 1
  is the exception that proves it: there κ = X because Q = X, not because a
  second variable appeared.
- *Where is parity broken?* Nowhere, at any degree ≥ 2. At d = 1 it is broken by
  Dirichlet, which is not a sieve result.
- *Is the Z-vs-Z[i] gap fatal to Note F?* No, and the note should not be read as
  suggesting it. Note F proves what it says. What was missing is that its
  statement is Gaussian while the hypotheses it is used against are rational,
  and the bridge is a boundedness fact that is measured rather than proved.
- *Is "bounded by 2" really as good as "bounded by 1"?* For this argument, yes:
  the argument uses only that there is no main term to extract. It would not be
  as good for an argument that needed the sharp constant, and no argument here
  does. Anyone tempted to use the sharp constant over Z should read this note
  first.
- *Could the rational 4-cycles be a resource rather than an obstacle?* They are
  the "congruence to detect" the plan (§2.2.4–5) anticipated, so the question is
  fair. Against it: there are ≍ X of them among ≍ X² pairs, and a dispersion
  main term needs ≍ X²/M. Three orders of magnitude short at any useful M, and
  the discrepancy grows with X.
- *Does the degree ladder rest on a fit?* No. α = 1/d and κ = X^{2−d} are
  arithmetic; only the Gram column is measured, and it is measured at fixed X
  across degrees rather than extrapolated in X.
