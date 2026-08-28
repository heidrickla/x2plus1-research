# Note O — The multiplier τ, and why no window holds three

*Not in the plan's deliverable list. Written because
[Note L](note-L-rational-graph.md)'s Proposition L.1 proves a bound of
O_ε(N^ε) on the dyadic-window Gram entry while the measured value is 2, and
because both sessions independently proposed — and both had refuted — a
probability model for the gap. This note supplies a mechanism and a proof.*

*Status: **Proposition O.1 proved; hypotheses (i)–(ii) verified exhaustively at
X = 4000 but not proved in general.** Machine check:
[`exp12`](../experiments/exp12_tau_multiplier.py).*

## The statement being explained

For coprime a < b, call m a **shared modulus** when

> a·m = x² + 1  and  b·m = y² + 1,

equivalently a solution of the conic b x² − a y² = a − b. Note L measures, over
every ratio class up to X = 8000:

- pairs of shared moduli inside one dyadic window get **arbitrarily tight** —
  smallest ratio 1.0783 → 1.0547 → 1.0412 as X grows, and 1.0036 at D = 2×10⁸;
- **no window ever holds three**, and the two-step ratio m_{i+2}/m_i has a
  *floor* at 13.0 with an empty bin below it, not a tail approaching 2.

Dickson bounds the number of classes by 2^{ω(|a−b|)+O(1)}, which is 32 or more
for many pairs and 128 for the pair below, so the class count does not explain
the 2. Two probability models were proposed, one per session, and the floor
refutes both: improbability does not produce an empty bin.

## The invariant

Write **M = b − a**, **D = ab**. Two shared moduli m_i < m_j give solutions
(X, Y) = (√(am−1), √(bm−1)). Set

> U = b X_i X_j − a Y_i Y_j  V = X_i Y_j − X_j Y_i.

Then **U² − D V² = M²** identically, and V = 0 exactly when the two solutions
are proportional.

**The gap principle.** For a pair inside one window, r = X_j/X_i ≤ √2 and

> |V| ≈ (M / 2√D) · (r − 1/r),

so |V| ≥ 1 forces M ≥ 2.83 √D. Measured, over every class attaining a pair:
the minimum of |V| is **2**, never 1, so the true threshold is 5.657 — against
an **observed minimum M/√D of 5.667**. Agreement to 0.2%.

**|V| = 2 is forced, not lucky.** U² − 4D = M² gives U² = (a−b)² + 4ab =
(a+b)², so (U, V) = (a+b, 2) is the *trivial* solution of U² − DV² = M², always
available. |V| = 1 would need a² − ab + b² to be a perfect square; among coprime
(a,b) with a < 400 that happens 325 times, but for only **2** of those are a and
b both admissible in the sense of [Note L](note-L-rational-graph.md) (every odd
prime ≡ 1 mod 4), and neither yields a window pair. Measured: 495 of 498 close
pairs have |V| = 2 exactly.

## The multiplier

|V| = 2 pins the ratio of the two solutions to

> **τ = (U + V√D)/M = (√b + √a)/(√b − √a).**

The modulus ratio of a close pair is **τ²**. Measured: for m ≥ 1000 the relative
deviation of m_j/m_i from τ² is at most 1.3×10⁻⁴ over 284 pairs; the error is
O(1/m), so the law is exact in the limit. Three independent confirmations at the
extremes of the data:

| (a, b) | τ² | measured ratio |
|---|---|---|
| (2, 85) | 1.8556 | 1.8525 |
| (13, 449) | 1.9880 | 1.9880 |
| (1, 9805) | 1.04119 | 1.04119 |

The last is the smallest consecutive ratio in the entire X = 5000 sweep.

## Proposition O.1 — τ acts at most once *on a given solution*

**Read the qualifier.** τ acting "at most once" is a statement about one solution
ξ, not about a ratio class. A class contains many solutions at widely separated
positions, and **each of them carries its own τ-pair**. At X = 2500 the class
(a,b) = (1,53) has shared moduli 10, 17, 24650, 42850 — two close pairs,
(10, 17) at ratio 1.700 and (24650, 42850) at ratio 1.73832, both matching
τ² = 1.73835. So τ acts twice in that class. What never happens is τ acting
twice **from the same ξ**, which is what a third modulus in one window requires.
The proposition below is about that, and the per-class count is unbounded.

> **Let a < b be coprime with gcd(a,b) = 1, M = b − a, D = ab. Then no dyadic
> window contains three shared moduli for (a, b).**

*Proof.* Since gcd(a,b) = 1 we have gcd(M, a) = gcd(b−a, a) = gcd(b, a) = 1 and
likewise gcd(M, b) = 1, so **M is coprime to D**.

A shared modulus corresponds to an element ξ of the order of K = Q(√D) with
N(ξ) = ±M. Two shared moduli in one window give ξ₁, ξ₂ with

> ξ₂/ξ₁ = (U + V√D)/M =: P/(M),  N(P) = U² − DV² = M² = N((M)).

Let (i) P = Q² with Q an ideal of norm M — which holds because M is coprime to
D, every prime of M splits in K, and P is divisible by no rational prime (with
V = 2 and M odd, a rational p | P would need p | U and p | 2). Then (M) = Q Q̄
and

> **τ = P/(M) = Q²/(Q Q̄) = Q/Q̄.**

Now N(ξ₁) = ±M, so the ideal (ξ₁) has norm M — it is *exactly* Q or Q̄, with no
room to spare. Integrality of ξ₂ = τ ξ₁ requires Q̄ | (ξ₁), forcing (ξ₁) = Q̄,
and then (ξ₂) = Q. **All of ξ₁'s norm is consumed.**

Suppose a third shared modulus ξ₃ lay in the same window. Then ξ₃/ξ₂ = Q'/Q̄'
by the same argument, so

> ξ₃ = (Q'/Q̄')(Q/Q̄) ξ₁,

whose integrality requires Q̄' Q̄ | (ξ₁), an ideal of norm M² dividing one of
norm M. Impossible unless the factors cancel, i.e. Q' = Q̄ — but that is
τ' = τ^{-1}, giving ξ₃ = ξ₁, not a third modulus. ∎

**Hypotheses used, and their status.**

- (i) *P = Q² with N(Q) = M.* Argued above for V = 2 and M odd; **not proved for
  even M or for the exceptional |V| ∈ {24, 66, 182}** seen 3 times in 498.
- (ii) *|V| = 2.* Verified for 495 of 498 close pairs. The 3 exceptions have
  larger |V| and correspondingly wider ratios; the proof shape is unchanged
  (N(P) = M² regardless) but step (i) needs re-checking for them.

## The falsifiable prediction, and its test

The proposition is not vacuous: τ⁴ < 2 means a third modulus **would fit inside
the window**, so every such pair is a chance to observe three. At X = 4000 there
are **258 such chances**, and a third occurs in **none** of them.

| population | chances (τ⁴ < 2) | thirds found |
|---|---|---|
| a = 1 (unit cofactor) | 106 | 0 |
| **a ≥ 2 (Type II-admissible)** | **152** | **0** |

The split matters. Note L records that the twenty smallest two-step ratios all
have a = 1 — the unit-cofactor configuration that no Type II split admits — and
raises the worry that the phenomenon might be confined to the family the
application never sees. **It is not**: 152 of the 258 chances have both
cofactors non-trivial, and the mechanism above is uniform in a.

## Consequence for Proposition L.1

Prop L.1 proves the spacing half (one modulus per class) and cites Dickson for a
count of 2^{ω(M)+O(1)}, giving G′ ≪_ε N^ε, with the measured 2 recorded as
`rigorous_finite`. Proposition O.1 replaces the count entirely: the bound is not
"few classes exist" but "**τ has no room to act twice on one solution**", and it gives **2**
directly, with no ε.

If (i) and (ii) are discharged in general, the dyadic-window Gram entry for the
rational graph is **O(1), unconditionally** — the first quantity in this repo to
move from measurement to theorem this week.

**What it does not do.** It bounds the *dyadic-window* entry. Note L's full
rational graph still grows (6 → 9 as X goes 500 → 8000) because it sums over all
windows, and [Note F](note-F-failure-localisation.md)'s C₄-freeness over Z[i] is
untouched and remains the obstruction that matters for Type II. A window Gram of
2 rather than N^ε does not create the cancellation Note F shows is absent.

## Adversarial review

- *Two-parameter freedom smuggled in?* No. Everything is about pairs of divisors
  of x²+1 with x ≤ X.
- *Is the empty bin small-sample?* The floor sits at 13.0 at X = 1500, 3000 and
  5000 while the triple count doubles (65 → 91 → 129), and the bin [6.85, 13) is
  empty at all three. The parallel session's independent sweep reproduces the
  same floor and the same minimiser, (1, 85) with m = 2, 17, 26.
- *Was the τ² law over-read?* It was, once. A first run reported the law as exact
  and the run's own worst deviation was 0.737, at m = 82. The law is asymptotic;
  the honest statement is error O(1/m), and the note now carries both figures.
- *Were the "thirds found" real?* A first pass reported 3 of 258 hits. All three
  were the tolerance window re-detecting m₁ itself. Excluding m₁ and m₂ gives 0.
  The number in this note is from the corrected test.
- *Is "acts at most once" being stated per class?* It was, in a first draft, and
  the parallel session found the counterexample: (1,53) carries two close pairs.
  The qualifier "on a given solution" is load-bearing and is now in the heading.
- *Does this rescue the theorem?* No, and it should not be read that way. It
  sharpens one bookkeeping constant inside Note L. The parity barrier and Note F
  are where the problem lives, and neither moves.
