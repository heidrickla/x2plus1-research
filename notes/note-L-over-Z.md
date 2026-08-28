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

That is a uniform explanation of why every single-variable Landau-type question
is stuck, and it makes Note F an instance of something general rather than a
fact about one polynomial. It is also, deliberately, not a claim about
truth — it is a claim about what the Type I/II framework can express, and the
standing warning on C⁻ = 0 applies here verbatim.

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
