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

**Status, and it has been wrong three times; this version is deliberately
weaker than the last two.**

The proved bound on the dyadic-window Gram entry is **O_ε(N^ε)**, and the
measured constant 2 is `rigorous_finite` with no proof attached. An earlier
draft of this section claimed the constant outright; a later one claimed
[Note O](note-O-tau-multiplier.md) had made it **O(1) unconditionally**. Both
are withdrawn.

What Note O does establish, and it is real, is
**Proposition O.1: Q̄² ∤ (ξ₁), so τ²ξ₁ is never integral** — no window holds
three moduli in geometric progression under a *single* multiplier. Its four
links are verified here independently
(`tests/test_polyseq.py::test_prop_O1_chain_holds_on_real_pairs`, zero
violations over 379 close pairs): N(ξ) = aM, |V| < M/√D, g = gcd(U,V) divides M,
and a g² < M with 8× to spare.

What it does **not** establish is the general statement. A third modulus from a
*different* multiplier gives ξ₃ = ±(Q″/Q̄″)ξ₁, so (ξ₁) must be divisible by both
Q̄ and Q̄″; if those are coprime the contradiction lands, and whether they can
share a prime ideal is open (Note O's Conjecture O.2). **That question cannot be
settled by measurement**: it concerns a configuration that never occurs, so every
sweep either of us has run contains zero instances of it. The absence of triples
is the thing to be explained, not evidence about the mechanism proposed to
explain it.

So the honest position is: the *pair* structure is explained, and the *triple*
question splits. **Triples involving the fundamental multiplier are now closed
unconditionally** — Theorem O.3 below, for M squarefree and odd, verified here
independently. Triples with both multipliers non-fundamental (shape
(ξ, τ_pξ, τ_qξ), p, q ≥ 2) remain reduced to the one ideal-theoretic statement,
Conjecture O.2. The bound is still not improved, and the only unconditional
constraint covering *every* shape is the Plücker one below, which has no ideal
theory in it.

**Earlier status, kept: the class count is unbounded, so the proposition does not
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

### The absence of a third has a mechanism, and the "floors" are not floors

Three moduli in one window is exactly m_{i+2}/m_i < 2, so the two-step ratio is
what decides it. Measured over every ratio class, the minimum two-step ratio is
**13.0000**, attained at (a, b) = (1, 85) with m = 2, 17, 26, and pinned across
X = 1500, 2500, 3500, 5000 while the triple count doubles. Restricted to pairs a
Type II split can meet (both cofactors ≥ 2, since a = 1 at d = 1 is the unit
cofactor) it is **73.0000** at (5, 481) for three sizes and **66.4923** at
(5, 4033) at X = 5000.

**And the minimiser was never a triple candidate — the two statistics are about
different populations.** A class can hold three moduli in a window only if it
clears M/√D ≥ 11.484 (the Plücker bound below). The global minimiser
(a, b) = (1, 85) has M/√D = 84/√85 = **9.111**, so it could never have held a
triple. Nor could (1, 5) at 1.789, (1, 65) at 7.938, or (5, 481) at 9.706.
Restricted to triple-capable classes, the minimum two-step ratio at X = 3000 is
**14.50** at (1, 533) with m = 10, 122, 145 — 23 such classes, against 13.0000
over all classes.

So the empty bin below 13 that prompted this section was partly evidence about
classes that were never candidates. It does not change any conclusion, and the
margin in the population that matters is 14.50 against a violation threshold of
2, but the two numbers should not be quoted as if they were one.

**Neither is a floor, and an earlier draft of this section said they were.**
[Note O](note-O-tau-multiplier.md) supplies the mechanism, and it gives a
different and better constant: the two-step ratio is ≥ 2 outright. So 13 and 66.5
are wherever the finite search has reached, and the restricted one *should* keep
drifting down — 73 → 66.5 is the beginning of that, not an anomaly. Note O even
predicts where the step falls: (5, 4033) first becomes visible at X = 4175, which
is between the 3500 and 5000 sweeps where it appeared. Predicted, not fitted.

**The multiplier, verified here independently.** For coprime a < b the close-pair
ratio is τ² with τ = (√b + √a)/(√b − √a). Over all 304 close pairs at X = 2500:

| m_i | m_j | observed | τ² | rel. err |
|---:|---:|---:|---:|---:|
| 24 650 | 42 850 | 1.73834 | 1.73835 | 8.8 × 10⁻⁶ |
| 13 925 | 20 450 | 1.46858 | 1.46860 | 1.2 × 10⁻⁵ |
| 10 405 | 12 545 | 1.20567 | 1.20568 | 8.2 × 10⁻⁶ |
| 6 605 | 12 745 | 1.92960 | 1.92961 | 3.7 × 10⁻⁶ |

median relative error 2.4 × 10⁻⁵, and only 2 of 304 above 1% (the error is
O(1/m), so the outliers are the smallest moduli). **And the threshold is sharp:**
τ² < 2 requires b/a > 33.97, and the minimum b/a over the 304 close pairs is
**34.1** — attained, never violated.

**τ alone does not forbid a third, and one class shows the multiplier acting
twice.** A third needs τ⁴ < 2, i.e. b/a > 134.3, and the median b/a over close
pairs is 148.2 — most of them clear it. So the work is done by Note O's
"τ cannot act twice", not by the threshold. But that phrase needs care: the
multiplier *can* act twice in one class. At X = 2500, of the 303 classes with a
close pair, 302 have exactly one and **(a, b) = (1, 53) has two** —
m = 10, 17, 24650, 42850, with close pairs (10, 17) at ratio 1.700 and
(24650, 42850) at ratio 1.7383 = τ². What never happens is two acting at
*consecutive* positions, which is what "three in one window" would require. The
statement is about consecutive triples, not about classes.

### |V| ≥ 2 is parity; |V| = 2 is not a lemma

[Note O](note-O-tau-multiplier.md)'s invariant V = X_iY_j − X_jY_i satisfies
U² − DV² = M², and the case |V| = 2 forces U² = M² + 4ab = (a+b)². Two facts
about it, and only one is a theorem.

> **Lemma.** For a, b both odd, V is always even, so |V| ≥ 2.
>
> *Proof.* X² = am − 1 and Y² = bm − 1. If m is odd then am and bm are odd, so
> X² and Y² are even and X, Y are both even; if m is even then both are odd.
> Either way X ≡ Y (mod 2), so V = X_iY_j − X_jY_i ≡ X_iX_j − X_jX_i ≡ 0 (mod 2). ∎

Machine-checked (`tests/test_polyseq.py::test_V_is_always_even_so_never_one`).
So "never |V| = 1" needs no hypothesis.

**"Always |V| = 2" does, and it is false.** At X = 4000 the histogram over 498
close pairs is {2: 495, 24: 1, 66: 1, 182: 1}, and the three are not anomalies —
they are the asymptotic |V| ≈ (M/2√D)(√r − 1/√r) working:

| M/√D | \|V\| | predicted | rel. err | (a, b) |
|---:|---:|---:|---:|---|
| 89.3 | 24 | 24.0 | 0.001 | (53, 423125) |
| 227.4 | 66 | 65.7 | 0.005 | (1, 51701) |
| 650.5 | 182 | 174.6 | 0.041 | (1, 423125) |

Their M/√D is 89, 227, 650 against a median of 11.96, and the |V| = 2 population
itself runs from 5.6666 to 87.0. So |V| = 2 is not a lemma with three exceptions:
**|V| is whatever the asymptotic gives**, and it equals 2 for pairs near the
minimal-separation configuration — which is most of them, because the close-pair
condition r < 2 already forces M/√D > 5.657.

### A three-term identity, offered as a tool

V is a 2 × 2 determinant, so three solutions of one conic satisfy the Plücker
relation obtained by expanding a 3 × 3 determinant with a repeated row:

> **V_ij X_k − V_ik X_j + V_jk X_i = 0**,  and the same with Y.

Exact; zero violations over 65 consecutive triples at X = 1500
(`tests/test_polyseq.py::test_three_term_determinant_identity`). For the
(1, 5) family it reads V_ij = V_jk = −2, V_ik = −6 at every step.

It constrains a would-be triple. With X_i < X_j < X_k inside one dyadic window,
so X_k/X_i < √2,

> |V_ik| = (|V_ij| X_k + |V_jk| X_i) / X_j > 2 + 2/√2 = 3.41,

hence **|V_ik| ≥ 4** by the parity lemma — which needs
**M/√D ≥ 4/(2^{1/4} − 2^{−1/4}) = 11.484**, minimised at r_ij = r_jk = √2,
against the 5.657 a mere close pair needs. That is a *necessary* condition and not a
sufficient one: the median M/√D over close pairs is 11.96, so about half clear
it. **It is, however, now the only unconditional constraint on a triple that
anyone has** — [Note O](note-O-tau-multiplier.md)'s ideal route is closed, and
this one contains no ideal theory, so it cannot share that route's failure mode.

**How thin the evidence for the absence really is.** At X = 4000 there are
278,939 ratio classes above the threshold M/√D ≥ 11.484; only **509** have two or
more shared moduli, and only **31** have three or more anywhere. So the whole
question rests on 31 informative classes, and 278,908 of the rest could not have
contradicted anything. "Verified over hundreds of thousands of ratio classes"
would have been true and thoroughly misleading.

### Theorem O.3 closes the natural case, and the walk is not needed for it

[Note O](note-O-tau-multiplier.md) now proves the k = 1 case outright, and the
proof removes the need for the orbit walk rather than extending it. **Mod M, in
the coordinates S = X+Y, T = X−Y, the class automorph diagonalises with both
eigenvalues units**, so integrality holds for a whole orbit or for none of it —
a single representative decides each class, and walking 44 of them was answering
a question one computation settles.

The statement: **for M = b−a squarefree and odd, no dyadic window holds three
shared moduli of the form (ξ, τ₁ξ, τ_kξ) with k ≥ 2.** The two requirements are
incompatible — divisibility forces M = 8ka(2k−j)/(j²−4) with j = 2B_k/M an
integer, while the geometry of a dyadic window forces M > 2√2·k√(ab), and the
two conditions have no common solution.

**Verified here independently**, by regenerating every multiplier in a ≤ 50,
b ≤ 60 000 from the Pell condition rather than from Note O's code — 224 670
multipliers, of which 220 077 have k = 1:

| checked | result |
|---|---|
| k = 1 ⟹ j = 2 exactly | 220 077 cases, **0 violations** |
| identity M = 8ka(2k−j)/(j²−4) on integer-j cases | holds exactly |
| k ≥ 2 satisfying the divisibility | 609 |
| k ≥ 2 satisfying the window geometry | 477 |
| k ≥ 2 satisfying **both** | **0** |

The k = 1 ⟹ j = 2 step is an identity, not a coincidence: U₁ = √(M² + 4ab) =
√((b−a)² + 4ab) = a+b, so B₁ = (a+b) − 2a = b−a = M and j = 2M/M = 2. The
disjointness is what the theorem asserts, and the two populations are both large
and cleanly separated — this is not a vacuous "no instances" check of the kind
`triples-cannot-be-settled-by-measurement` warns about, because both sides are
populated and it is their intersection that is empty.

**What stays open is O.2**, triples of shape (ξ, τ_pξ, τ_qξ) with p, q ≥ 2 —
neither multiplier the fundamental one. The coverage critique below applies to
exactly that remainder and to nothing else.

### How much of the candidate space is left, and what the walk covered

Note O's decidable criterion — (a, b) admissible, some k ≥ 2 with
a² + (4k²−2)ab + b² a perfect square, and r₁·r_k < 2 — was reconstructed here
independently. In the box a ≤ 60, b ≤ 300 000 it gives **534 candidates** under
the corrected admissibility (4 ∤ n; an earlier count of 322 used a test that
let 4 | n through). Note O's stated tightest, (1, 115921) at k = 22, is
reproduced; **(1, 226801) at k = 26 is tighter.**

Then the criterion was tested against the thing it is supposed to predict, and
it does not predict it.

### The candidate criterion counts configurations that are not there, and misdescribes the ones that are

**Two different equations.** They are easy to conflate because both are Pell
equations in D = ab and M = b−a, and neither name advertises the difference:

| | equation | what it is |
|---|---|---|
| multiplier at index k | U² − D V² = M², V = 2k | a ratio **between solution classes** |
| shared modulus | Y² − D X² = aM | an actual m with am, bm ∈ A |

The second is Prop L.1's conic in disguise: b(x²+1) = a(y²+1) with
m = (x²+1)/a, so (a,b) is occupied **exactly when the Gram entry G(a,b) ≥ 1** —
the same object [Note F](note-F-failure-localisation.md) bounds. A multiplier is
well defined whether or not any class of the second equation is occupied. So a
candidate list built from multipliers may be counting empty configurations.

**It is.** Occupancy tested directly, by QR-sieving x in 22 residue filters
before any exact isqrt, so the bound is large enough to mean something
(x ≤ 4×10⁷):

| a | b | occupied? | smallest x | smallest m | |
|---:|---:|---|---:|---:|---|
| 1 | 5 | yes | 1 | 2 | calibration |
| 1 | 115921 | **yes** | 387 | 149 770 | tightest of the parallel session's 95 |
| 1 | 226801 | **yes** | 185 | 34 226 | tightest of the 534 |
| 1 | 1761985 | yes | 296 | 87 617 | |
| 5 | 1265009 | yes | 357 407 | 2.55×10¹⁰ | |
| 2 | 2813785 | no | — | — | |
| 1 | 360361 | no | — | — | ω(M) = 6 near-miss |
| 37 | 158377 | no | — | — | ω(M) = 6 near-miss |
| 1 | 12352 | no | — | — | smallest D of the 534 |

Occupancy is **selective, not rare** — and the parallel session's independent
count agrees, 42 of its 95 occupied. The first row of (1, 115921) is checked by
hand outside any script: 387² + 1 = 149 770 and 115 921 × 149 770 = 131 763² + 1.

**And on the live pairs the criterion's r is not the modulus ratio.** Every
shared modulus of the tightest candidate, to x ≤ 2×10⁸:

    x =       387   m =           149,770
    x =     2,249   m =         5,058,002
    x =   147,709   m =    21,817,948,682
    x = 2,054,872   m = 4,222,498,936,385

    consecutive ratios:  33.77,  4313.55,  193.53
    max moduli in one dyadic window:  1

The criterion put this pair at the top of both lists with an r-product near 1.3;
τ₁² is 1.0118; the smallest ratio between two of its actual moduli is **33.77**.
Same on the others — (1, 226801) has one shared modulus below 2×10⁸, and
(1, 1761985) has two, spaced by 1.2 million. Window multiplicity 1 in all three.

**The framework is not wrong; it is being asked the wrong question.** On the 379
classes that genuinely put two moduli in one window at X = 3000, the observed
ratio is τ₁² to within 10⁻³ in **359 of 379 (94.7%)**, median relative error
**1.7×10⁻⁵** — exactly as `close_pairs` documents. So τ predicts a realised
close pair's ratio essentially perfectly, and nothing in that derivation needs
revisiting. What it does not do is tell you whether the class it points at is
occupied, and on the tightest candidates it is not: the near neighbour is the
empty class, and the occupied moduli sit ε² apart instead.

> **A candidate list built from multipliers selects pairs where two classes
> *could* be close. Whether the close pair is the *occupied* pair is a different
> question, and on every tightest candidate found here the answer is no.**

That retires the geometric attack on Conjecture O.2 from both directions. The
drift measurement that prompted this — minimum diagnostic ratio falling 20.2 →
0.95 across six decades of b, crossing 1 at (2, 2813785) — is **withdrawn**: that
pair is unoccupied, and the quantity was the wrong one regardless. The parallel
session's factor of four is withdrawn on the same grounds, by them.

### Generate from the realised side: the residuals are the live configurations

The failure above is a search direction, and reversing it fixes it. Generating
candidates from multipliers and testing occupancy afterwards searches a mostly
empty parameter space. The other order cannot:

> **Enumerate realised ratio classes, keep those with two moduli in one dyadic
> window, and read off which multiplier index explains the ratio.** Live by
> construction — occupancy is the input, not a filter applied later, and the
> multiplier structure is the output.

The 20 outliers of the positive control are exactly this method's first run.
Most are small-m cases where the documented O(1/m) correction dominates. One is
not, and it is the sharpest single object this repo has for the open question:

> **(1, 423125).** Shared moduli **m = 10 and m = 17**, ratio **1.70** — inside
> a dyadic window. τ₁² = 1.00617, so the fundamental multiplier does *not*
> explain it; **k = 91 does**, with r₉₁² = 1.73765. The pair has exactly two
> multipliers, k = 1 and k = 91.

Verified independently of any parameterisation: 10 − 1 = 3², 423125·10 − 1 =
2057², 17 − 1 = 4², 423125·17 − 1 = 2682². And enumerated exhaustively —
**x ≤ 3×10⁸ yields those two moduli and nothing else**, from x = 3 and x = 4.

Three things make it the right test case:

1. **The close pair is realised at a non-fundamental multiplier.** Every other
   live close pair examined here sits at k = 1. This is the shape Conjecture O.2
   is about, occurring.
2. **M = 423124 = 2²·13·79·103 is even, so Theorem O.3 is mute on it** — it is
   in precisely the regime the parity extension would bring inside.
3. **There is no third, and the reason is visible.** A third modulus at the
   fundamental step would sit at 10 × 1.00617 = 10.06 or 17 × 1.00617 = 17.10;
   neither is an integer. τ₁ does not act on either occupied modulus, which is
   Prop O.1's conclusion appearing on a live configuration rather than a
   hypothetical one.

Any extension of O.3 to even M must permit exactly two in a window here. That is
a concrete falsifier, and this repo did not previously have one.

### Theorem O.3 survives this, and its hypothesis is narrower than it reads

O.3 is **conditional** — if ξ exists and both τ₁ and τ_k act on it, contradiction
— so an empty configuration cannot produce a counterexample to it either.
Vacuity is safe for a negative result. Nothing above touches it, and it is
verified here independently (see above).

What is worth recording next to it is the reach of its hypothesis, *M = b−a
squarefree and odd*. For a = 1: b admissible and odd forces b ≡ 1 (mod 4), hence
M ≡ 0 (mod 4). So

> **O.3 is mute on every a = 1 pair with b odd — including both live candidates
> above, M = 115 920 and M = 226 800.**

Of the 534 candidates, **104 (19.5%)** have M odd and squarefree. Of admissible
b < 400 000 at a = 1, 33.9% give M odd. That is not a defect in a theorem that
is true as stated; it is the observation that "no dyadic window holds three"
reads considerably broader than a statement mute on four fifths of the
candidates and on the a = 1 family this note identifies as driving the full
graph's growth.

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
| **root equidistribution** — a power saving in the Weyl sum over roots of G(Ω) ≡ 0 | **unconditional at d = 2, conditional at d = 3** (Lemke Oliver, *Acta Arith.* **151**, Remark 3) |

That last row degrades one degree above where this repo sits, and for a reason
with nothing to do with density. The input Iwaniec's P₂ needs is a power saving
over the trivial O_q(M) in

> Σ_{M<m<M₁} Σ_{G(Ω)≡0 (mq)} e(hΩ/mq)

— the Weyl sum over roots of the quadratic congruence, which is DFI's ρ_h(n) and
this repo's r_d. Lemke Oliver establishes it unconditionally for irreducible
quadratics; at degree 3 the analogue is Hooley's, "conditional upon his
Hypothesis R* on the size of short Kloosterman sums". So the arithmetic input
*every* route needs is already conditional at d = 3, independently of κ or of
admissible triples.

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
- *The candidate-criterion section refutes work done in this repo — is it
  over-corrected?* It is scoped deliberately. What is refuted is that r₁·r_k
  predicts window multiplicity, and with it every count of "candidates where a
  triple could occur". What stands: the recount to 534, the tightest-candidate
  correction, the τ² law (positive control, 94.7% within 10⁻³), and Theorem O.3,
  which is conditional and so cannot be damaged by a configuration being empty.
- *Is the drift measurement withdrawn for the right reason?* Two independent
  ones, either sufficient. Its crossing point (2, 2813785) is unoccupied, and
  the quantity it measured does not predict window behaviour even on occupied
  pairs. It was recorded here for less than an hour and never left the repo.
- *Does one live pair carry too much weight?* (1, 423125) is one object, and the
  note claims exactly one thing from it: that the non-fundamental shape occurs,
  in the even-M regime O.3 cannot reach. It bounds nothing — how many such
  configurations exist is open, and `generate-candidates-from-the-realised-side`
  is `inferred` precisely because it is a claim about search, not about counts.
- *Was the population defect avoidable?* It was recorded in this repo already,
  as `triples-cannot-be-settled-by-measurement`, and both sessions walked into
  it anyway — one of them (this one) while citing it. The registry entry names
  the trap for configurations that never occur; what it did not say is that a
  *parameter* can be well defined on an empty configuration, which is how the
  trap was re-entered one level down.
