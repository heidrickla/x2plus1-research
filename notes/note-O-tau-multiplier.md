# Note O — The multiplier τ, and the three-in-a-window question

*Not in the plan's deliverable list. Written because
[Note L](note-L-rational-graph.md)'s Proposition L.1 proves a bound of
O_ε(N^ε) on the dyadic-window Gram entry while the measured value is 2, and
because both sessions independently proposed — and both had refuted — a
probability model for the gap. This note supplies the mechanism for the **pairs**
and proves it; it reduces the **triple** question to a statement it does not
settle, and closes the one route it proposed for settling it.*

*Status: **Proposition O.1 proved (τ² ξ is not integral **when τξ stays inside the
window** — the hypothesis is essential, see (1,5) below). Conjecture O.2 — the
statement the measurements actually make — is OPEN.** A draft of this note
claimed O.2 as proved; the composition step does not hold and the retraction is
recorded below rather than edited away. Machine check:
[`exp12`](../experiments/exp12_tau_multiplier.py).*

## The statement being explained

For coprime a < b, call m a **shared modulus** when

> a·m = x² + 1  and  b·m = y² + 1,

equivalently a solution of the conic b x² − a y² = a − b. Note L measures, over
every ratio class up to X = 8000:

- pairs of shared moduli inside one dyadic window get **arbitrarily tight** —
  smallest ratio 1.0783 → 1.0547 → 1.0412 as X grows, and 1.0036 at D = 2×10⁸;
- **no window is ever observed to hold three**, and the two-step ratio
  m_{i+2}/m_i has a search minimum pinned at 13.0 across X = 1500, 3000, 5000
  with the bin [6.85, 13) empty — populated on one side, empty on the other.
  *Search minimum, not floor:* Prop O.1 bounds the two-step ratio below only by
  2, so 13.0 and the restricted 66.49 are where finite search has reached and
  should be expected to drift down.

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

**The gap principle.** Throughout, **r = m_j/m_i** is the *modulus* ratio, so a
pair inside one window has r < 2. Then

> |V| ≈ (M / 2√D) · (√r − 1/√r),

and |V| ≥ 1 forces M ≥ 2.83 √D, since √r − 1/√r < √2 − 1/√2 = 0.7071. The minimum of |V| over every class attaining a
pair is **2**, never 1, so the operative threshold is 5.657 — against an
**observed minimum M/√D of 5.667**. Agreement to 0.2%.

**Why |V| = 2 is common, and why that is not the same as forced.** U² − 4D = M²
gives U² = (a−b)² + 4ab = (a+b)², so (U, V) = (a+b, 2) is the *trivial* solution
of U² − DV² = M², always available; and |V| ≥ 2 is parity (see the proof
section). So 2 is the smallest value the invariant can take, and it is what
pairs near the minimal-separation configuration realise — 495 of 498 at
X = 4000.

**It is not, however, a law, and an earlier draft of this note treated it as
one.** |V| is whatever the asymptotic |V| ≈ (M/2√D)(√r − 1/√r) gives. The three
pairs with |V| ∈ {24, 66, 182} are that formula working correctly at
M/√D = 89, 227, 650 against a median of 11.96 — not anomalies. The proof below
therefore assumes nothing about V.

## The multiplier

In the common case |V| = 2, U = ±(a+b) and the ratio of the two solutions is

> **τ = (U + V√D)/M = (√b + √a)/(√b − √a).**

The modulus ratio of such a pair is **τ²**. Measured: for m ≥ 1000 the relative
deviation of m_j/m_i from τ² is at most 1.3×10⁻⁴ over 284 pairs; the error is
O(1/m), so the law is exact in the limit. Three independent confirmations at the
extremes of the data:

| (a, b) | τ² | measured ratio |
|---|---|---|
| (2, 85) | 1.8556 | 1.8525 |
| (13, 449) | 1.9880 | 1.9880 |
| (1, 9805) | 1.04119 | 1.04119 |

The last is the smallest consecutive ratio in the entire X = 5000 sweep.

## Proposition O.1 — τ² ξ is not integral *when τξ stays in the window*

> **The window hypothesis is not optional, and an earlier statement of this
> proposition omitted it and was therefore false.** The counterexample is
> (a, b) = (1, 5) at m = 2: coprime, m_i ≥ 2, and yet τ₁² = τ₃ **does** act —
> the acting set there is the whole tower k = 1, 3, 8, 21, 55, 144. It escapes
> because a·g² = 4 = M, failing the *strict* inequality a g² < M that the proof
> turns on, and it fails it precisely because r₁ = 6.854 puts τ₁ξ nowhere near
> the window. The chain a g² < M is derived **from** the window via
> |V| < M/√D; without it there is no proposition. Corrected in place rather
> than quietly, since "τ acts at most once" was the note's own headline and is
> false as a general statement.

**Read the qualifier.** τ acting "at most once" is a statement about one solution
ξ *whose τ-image stays inside the window*, not about a ratio class. A class contains many solutions at widely separated
positions, and **each of them carries its own τ-pair**. At X = 2500 the class
(a,b) = (1,53) has shared moduli 10, 17, 24650, 42850 — two close pairs,
(10, 17) at ratio 1.700 and (24650, 42850) at ratio 1.73832, both matching
τ² = 1.73835. So τ acts twice in that class. What the proposition forbids is τ
acting twice **from the same ξ while both images stay inside the window** —
which is what a third modulus in one window requires. Without the window clause
it is false: (1,5) at m = 2 has τ₁ and τ₁² = τ₃ both acting. The per-class count
is unbounded and so, outside a window, is the per-solution count.

> **Proposition O.1.** Let a < b be coprime, M = b − a, D = ab, and let ξ₁ be a
> solution with m_i ≥ 2 **such that τξ₁ lies in the same dyadic window as ξ₁**
> (equivalently, the modulus ratio r₁ < 2). Then **τ² ξ₁ is not integral**: no
> window contains three shared moduli in geometric progression under a single
> multiplier.

> **Conjecture O.2 (open).** No dyadic window contains three shared moduli at
> all — the statement every measurement in this repo and Note L supports, and
> which O.1 does **not** imply. See "Where the proof stops" below.

*Proof.* Since gcd(a,b) = 1 we have gcd(M, a) = gcd(b−a, a) = gcd(b, a) = 1 and
likewise gcd(M, b) = 1, so **M is coprime to D**.

A shared modulus corresponds to an element of K = Q(√D). **The norm is aM, not
M** — an earlier draft of this note wrote ±M and the difference is load-bearing,
so it is derived here. Put

> **ξ_k = a Y_k + X_k √D**,  N(ξ_k) = a²Y_k² − D X_k² = a(a Y_k² − b X_k²) = **aM**,

using aY² − bX² = b − a = M. Two shared moduli in one window then give

> ξ₂ ξ̄₁ = −a(U + V√D) = −a·P,  so  ξ₂/ξ₁ = −P/(M),  N(P) = U² − DV² = M².

Both identities verified exactly, 379/379 close pairs at X = 3000.

Put **g = gcd(U, V)**. Since g² | M² we have g | M; write **M′ = M/g**. Then
P = g·P′ with P′ = (U/g) + (V/g)√D of norm M′², and P′ is divisible by no
rational prime, since a rational p | P′ would need p | U/g and p | V/g, which
are coprime by construction. Every prime p | M′ is therefore split (an inert p
would contribute p^{2e} to the norm only via 𝔭^e = (p)^e, a rational factor),
and the p-part of P′ is 𝔭^{2e} or 𝔭̄^{2e} — never mixed, again because a mixed
part is rational. Hence

> **P′ = Q² with N(Q) = M′, and τ = P/(M) = P′/(M′) = Q²/(Q Q̄) = Q/Q̄.**

The ideal (ξ₁) has norm aM. Integrality of ξ₂ = ±τ ξ₁ requires Q̄ | (ξ₁), which
is possible since N(Q̄) = M′ ≤ aM.

Now suppose τ²ξ₁ were also a solution. That requires Q̄² | (ξ₁), of norm M′², so

> M′² ≤ aM,  i.e.  **M ≤ a g².**

**It remains to show M > a g², which is where the window hypothesis enters.**
Write u = m_i, v = m_j, A = (au−1)(bv−1), B = (av−1)(bu−1). Then

> A − B = (abuv − au − bv + 1) − (abuv − av − bu + 1) = (v−u)(a−b) = −(v−u)M,

an identity. Since V = √A − √B,

> |V| = (v−u)M / (√A + √B) ≤ u M / (2√((au−1)(bu−1))),   [v, u are m_j, m_i]

using v − u < u — *this is the window hypothesis, and the only place it is
used* — and √A, √B ≥ √((au−1)(bu−1)). For u ≥ 2 we have au − 1 ≥ au/2 and
bu − 1 ≥ bu/2, so the root is at least u√D/2 and

> **|V| < M/√D.**

Finally g | V gives g ≤ |V| < M/√D = M/√(ab), so g² < M²/(ab) and hence

> **a g² < M²/b < M**,

the last step because M = b − a < b. This contradicts M ≤ a g². ∎

## Where the proof stops, and why O.2 is still open

> **⚠ READ THIS SECTION AS HISTORY.** It records the retraction of an early
> unconditional claim and the state of the argument at that point. **Theorems
> O.7–O.11 below supersede it**: O.2 is now proved for M an odd prime, and for
> every M the inequality 3ab < (b−a)^{4/3} — sharpened to 0.048628·(b−a)^{4/3} —
> is a proved necessary condition. What remains is quantitative, not structural.

**This is a retraction.** A draft of this note, and a message to the parallel
session, claimed O.2 as an unconditional theorem. It is not, and the error was
in the composition step, which read:

> "ξ₃/ξ₂ = Q′/Q̄′ by the same argument, so ξ₃ = (Q′/Q̄′)(Q/Q̄)ξ₁, requiring
> Q̄′Q̄ | (ξ₁) of norm M′²."

That does not follow. ξ₃ = τ′ξ₂ requires Q̄′ | (ξ₂), and **(ξ₂) has norm aM in
its own right** — the two divisibilities are conditions on different elements and
do not stack. Composing them is only legitimate when the numerator and
denominator do not share prime ideals, and I asserted that after checking only
the case of total cancellation (Q′ = Q̄, which returns ξ₃ = ξ₁).

What a correct argument needs. A third modulus gives ξ₃ = ±(Q″/Q̄″)ξ₁ with
Q̄″ ≠ Q̄ (equality forces ξ₃ = ξ₂). Then (ξ₁) is divisible by **both** Q̄ and
Q̄″, so N(lcm(Q̄, Q̄″)) ≤ aM. **If Q̄ and Q̄″ are coprime** this gives
M′M″ ≤ aM, hence M ≤ a·g·g″ < M by the bound above — the contradiction. So O.2
reduces exactly to:

> **Can two distinct multipliers for the same ξ₁ have Q̄, Q̄″ sharing a prime
> ideal?** If not, O.2 follows.

**And this cannot be settled by measurement inside a window**, because no
triples occur there. But it *can* be probed in wider windows, where consecutive
triples do exist (the two-step ratio floor is 13), and the answer closes this
route rather than opening it.

Composing the three multipliers gives Q″/Q̄″ = Q′Q/(Q̄′Q̄); cancelling by
c = gcd(Q′Q, Q̄′Q̄) and *assuming* c is self-conjugate hence c = (n) yields

> g₁₂ · g₂₃ · n² = M · g₁₃,   with coprimality of Q̄, Q̄″ the case n = 1.

Over the 110 consecutive triples at X = 4000:

| | count |
|---|---|
| relation g₁₂g₂₃n² = M g₁₃ holds | 65 of 110 |
| of those, n = 1 (the coprime case) | **5 of 65** |

**Both halves are bad news for the route.** The relation fails outright in 45 of
110 cases, so the derivation above over-assumes — c need not be self-conjugate,
and the primitivity that would force it does not hold in general. And where the
relation does hold, coprimality is the **exception**: n = 3, 8, 27, 38, 69 are
typical, so Q̄ and Q̄″ routinely share prime ideals. The branch of the argument
that would give the contradiction covers a small minority of the only regime
where the question can be observed at all.

> **So the ideal-theoretic route to O.2 is closed, not merely incomplete.** The
> reduction "O.2 follows if Q̄ and Q̄″ are coprime" is true but its hypothesis is
> usually false, and no repair is offered here.

### How much evidence O.2 actually has

Worth stating, because the sweeps are large and the *informative* part of them
is not. A class can exhibit a triple only if it clears the Plücker–parity
threshold **M/√D ≥ 11.484** (below) *and* has at least three shared moduli at
all. At X = 4000:

| | count |
|---|---|
| ratio classes above the triple threshold | 278,939 |
| of those, with ≥ 2 shared moduli | 509 |
| **of those, with ≥ 3 shared moduli anywhere** | **31** |
| max moduli in one window among them | 2 |

**So O.2 rests on 31 informative classes, not on 278,939.** The other quarter of
a million are silent: they have too few moduli for the question to arise. Any
statement of the form "verified over hundreds of thousands of classes" would be
true and misleading, and this note should not make it.

The threshold itself is the parallel session's, and at the time it was written it
was the **only unconditional constraint on a triple** anyone had. *(It is no
longer: Theorems O.4 and O.9–O.11 give stronger ones, and the constant recorded
here does not follow from the derivation stated — see the correction below.)* V is a 2×2
determinant, so three solutions satisfy the Plücker relation
V_ij X_k − V_ik X_j + V_jk X_i = 0 (machine-checked in Note L as
`test_three_term_determinant_identity`). With X_k/X_i < √2 that forces
|V_ik| > 2 + 2/√2 = 3.41, hence |V_ik| ≥ 4 by the parity lemma.
**It contains no ideal theory**, so it does not share the failure mode of the
composition step above.

> **⚠ CORRECTED — the constant this section recorded, M/√D ≥ 11.484, does not
> follow from the derivation it states.** The exact bound is
> **|V| < (M/2√D)(R − 1/R)** with R = X_k/X_i (proved in Theorem O.8's lemma,
> from a|V|(X_jY_i + X_iY_j) = M(X_j² − X_i²)). With R < √2 that is
> |V| < 0.35355·M/√D, so **|V| ≥ 4 gives M/√D > 11.3137 = 8√2**, not 11.484.
>
> **And it is not unconditional.** R < √2 is the *asymptotic* window condition;
> exactly, R² < 2 + 1/X_i². At X_i = 1 that gives only **M/√D > 6.93**, rising to
> 11.3137 as X_i → ∞ (9.60, 10.46, 10.99, 11.23 at X_i = 2, 3, 5, 10).
>
> **11.484 is nevertheless correct**, and Theorem O.4 proves it by a different
> route — composition rather than the determinant. The two constants are
> *algebraically identical*, since
> 1/(2^{1/4} − 2^{−1/4}) = 2^{1/4}(√2+1) = 2^{1/4} + 2^{3/4}, so
> 4/(2^{1/4} − 2^{−1/4}) = 4(2^{1/4} + 2^{3/4}) = 11.48400. The value was right
> and the route to it was not.

### A constructive attack, and what it found

Searching is the wrong instrument once you know what a triple needs, so this is
the aimed version. A multiplier with |V| = 2k exists exactly when

> **a² + (4k²−2)ab + b² is a perfect square** — U² = M² + 4k²D.

At k = 1 that is (a+b)², a **square identically**, which is why the trivial
multiplier τ always exists. For k ≥ 2 it is a real Diophantine condition, and it
holds for roughly 0.1% of coprime pairs. Verified 498/498 on the close pairs: the
three with |V| ∈ {24, 66, 182} are k = 12, 33, 91 and each satisfies it.

**A triple needs a second multiplier**, because V = ±2 forces U = ±(a+b)
uniquely — there is exactly one multiplier at k = 1. So one can *construct* the
candidates instead of sweeping for them: admissible (a,b) with b/a ≥ 134, a k ≥ 2
multiplier, and geometry permitting r₁·r_k < 2. **There are 95** in the box
a < 200, b < 200000, the tightest being (1, 115921) at k = 22 with
r₁r_k = 1.309. *(The parallel session's census over a ≤ 60, b ≤ 300000 finds
322, with (1, 226801) at k = 26 tighter still at 1.2540 — the population grows
with the box, so quote the box.)*

> ### The candidate lists do not predict window behaviour at all
>
> **This is the correction that retires the whole constructive line above, and
> it subsumes the occupancy problem stated below.** The parallel session
> enumerated every shared modulus of (1, 115921) — the tightest candidate on
> either list, r₁r_k ≈ 1.31 — out to x ≤ 2×10⁸:
>
> | x | m |
> |---|---|
> | 387 | 149,770 |
> | 2,249 | 5,058,002 |
> | 147,709 | 21,817,948,682 |
> | 2,054,872 | 4,222,498,936,385 |
>
> Consecutive ratios **33.77, 4313.55, 193.53**. Maximum dyadic-window
> multiplicity **1**. The criterion predicted ~1.31 and reality gives 33.77 — a
> factor of 26. Same on the other live pairs: (1, 226801) has one modulus to
> x ≤ 2×10⁸, (1, 1761985) has two at ratio 1,223,596.
>
> **The reason.** r₁·r_k is a ratio between *solution classes*. A pair can be
> perfectly occupied and still have every observed modulus spaced by ε², because
> the near-neighbour class the multiplier points at is the empty one. **The
> criterion selects pairs where two classes could be close; it says nothing
> about whether the close pair is the occupied pair.**
>
> So everything in this section built on r-products — the 95, the 322, the
> τ⁴ < 2 chances, the factor of 3.91, the parallel session's decade drift and
> its sub-1 crossing — counts parameter configurations whose r-values do not
> predict the window behaviour of the occupied ones. **All of it is withdrawn as
> evidence about triples.** What survives is stated at the end of this note.
>
> ### A structural fact about the rational graph: K_{s,2} but no K_{3,3}

Over Z[i], [Note F](note-F-failure-localisation.md) forbids **K₂,₂** outright —
that is C₄-freeness. Over Z the merging of several primitive Gaussian ideals into
one rational modulus breaks that, and the parallel session's K₆,₂ shows it breaks
it unboundedly. Measured at X = 6000 over the full incidence graph:

| | |
|---|---|
| largest K_{2,s} (two cofactors, s shared moduli) | **s = 9**, at cofactors (1, 5), moduli 2, 10, 65, 442, 3026, 20737, … |
| **K₃,₃ instances** (three cofactors sharing three moduli) | **0** |

So the row-merging **thickens one side of the bipartite graph and not both**: the
rational graph is K₂,₂-rich and, in this range, K₃,₃-free. That is a sharper
statement of the Z-vs-Z[i] gap than "max Gram 2 instead of 1", because it says
*which* completeness survives the transfer and which does not.

**O.2 is self-dual, which doubles what proving it would give.** A cofactor pair
(a, b) sharing a modulus satisfies b x² − a y² = a − b; a *modulus* pair (m₁, m₂)
shared by a cofactor satisfies m₂ x² − m₁ y² = m₁ − m₂ — **the same equation with
the roles swapped**. So "at most two moduli per window for a fixed cofactor pair"
and "at most two cofactors per window for a fixed modulus pair" are one theorem.
Measured at X = 5000, and the constant agrees:

| | max in one window | attained at |
|---|---|---|
| moduli, for a fixed **cofactor** pair | **2** | (2, 82) → moduli 365, 685 |
| cofactors, for a fixed **modulus** pair | **2** | (1, 41) → cofactors 730, 1370 |

This also explains why the K_{s,2} families are spread across decades rather than
bunched: the parallel session's six cofactors sharing {10, 17} are 1, 53, 423125,
24326641, … with consecutive ratios 53 and 7983, so **no window holds two of
them** — the dual statement, satisfied with room to spare.

**And it buys nothing quantitatively, which must be said or someone will reach
for Kővári–Sós–Turán.** A K₃,₃-free bipartite graph on (M, N) vertices has
O(M·N^{2/3} + N) edges. In a dyadic window there are ~M moduli, ~X²/M cofactors,
and the *actual* edge count is **0.331·X** — measured flat to 0.1% across a
factor 256 in M, not the bare "~X" an earlier version of this sentence gave,
which invites the constant 1 and is 3× wrong. The KST bound exceeds
that by **2–4 orders of magnitude** in every regime (e.g. X = 10⁶, M = 10⁶:
10¹⁰ against 10⁶). The same is true of C₄-freeness over Z[i], and it is worth
being explicit that **Note F does not use C₄-freeness via edge counting at all**
— it uses it to make the Gram matrix diagonal, which is a statement about
*cancellation*. Freeness from a complete bipartite subgraph is informative here
only through the Gram structure, never through KST.

*(A first version of this search reported 19 K₃,₃ instances. All were spurious —
the third cofactor equalled the first, because the loop guarded n₃ > n₂ while
n₁, n₂ came from `combinations` over a set in hash order rather than sorted
order. With strictly increasing indices the count is 0.)*

**Theorem O.3 is untouched**, because it is conditional: *if* ξ exists and both
> multipliers act on it, contradiction. Nothing here weakens a conditional
> negative result; it says only that the candidate lists were never the right
> place to hunt for its counterexamples.
>
> **MULTIPLIER EXISTENCE IS NOT MODULUS EXISTENCE, and this list conflates
> them.** A multiplier at index k is solvability of **U² − DV² = M²**; a shared
> modulus is solvability of **Y² − DX² = aM**. Different equations. A multiplier
> is the *ratio between two solution classes* and is well defined whether or not
> any class is occupied. Measured: **42 of the 95 are occupied** (some shared
> modulus with x ≤ 1.5×10⁶); the rest are configurations with no shared moduli
> at all, for which "a triple could occur here" is meaningless.

The point was made by the parallel session against its own drift measurement,
and it applies to this list equally. Two pairs found here by a heuristic
targeting ω(M) ≥ 6 — (1, 360361) and (37, 158377), each with two multipliers at
r < 2 and r-product 1.83 — are **both unoccupied**, which is exactly the failure
mode: they look like near-counterexamples and are not configurations at all.

**Theorem O.3 is unaffected**, because it is conditional: *if* ξ exists and both
multipliers act, contradiction. Vacuity is safe for a negative result. What needs
the caveat is any statement of the form "there are N candidates where a triple
could occur" — that N is a count of parameter configurations, not of live ones.

The multiplier acts explicitly. From ξ = aY + X√D,

> X′ = (U_k X + 2k a Y)/M,  Y′ = (U_k Y + 2k b X)/M,

integral iff M divides both. Since U₁ = a+b ≡ 2a and b ≡ a (mod M), this
collapses to two linear congruences:

> **τ₁: 2a(X+Y) ≡ 0 (mod M)   τ_k: U_k X + 2ka Y ≡ 0 (mod M)**

*(Checked against known cases: (2,85) with m = 61 maps to (15,98) = m = 113, and
(53,423125) with m = 10 maps to m = 17.)*

**There is no local obstruction.** All 95 candidates admit a solution of both
congruences together with the conic mod M. So O.2, if true, is not a congruence
statement — that explanation is eliminated.

**But the residues a conic solution can actually occupy are restricted.** The
class automorph is X′ = tX + uaY, Y′ = tY + ubX with (t,u) the fundamental
solution of t² − Du² = 1, and its orbit mod M is finite. Walking **44 orbits to
cycle closure** (longest 6000 states) over the candidates with a reachable seed:

> **in every orbit, the two conditions are never simultaneously satisfied.**

So the obstruction is global rather than local, and it is finitely checkable per
class: the target residue set is non-empty but the conic's orbit misses it.

### Theorem O.3 — the two conditions are incompatible

The orbit walk turns out to have been unnecessary, and seeing why gives a proof.
Mod M we have b ≡ a, so in the coordinates **S = X+Y, T = X−Y** the class
automorph **diagonalises**:

> S → (t + ua)S,  T → (t − ua)T,  with (t+ua)(t−ua) ≡ t² − Du² = 1 (mod M).

Both eigenvalues are **units**, so each condition holds for an entire orbit or
for none of it — which is exactly what the 44 walks observed, and why walking
was pointless.

> **Theorem O.3.** Let M = b − a be squarefree and odd. Then no dyadic window
> contains three shared moduli of the form (ξ, τ₁ξ, τ_kξ) with k ≥ 2.

*Proof.* τ₁ integral means M | 2a(X+Y), so M | S. Writing
A_k = U_k + 2ka, B_k = U_k − 2ka, the τ_k condition is A_kS + B_kT ≡ 0 (mod 2M),
which given M | S reduces to M | B_kT. If p | X and p | M then bX² − aY² = −M
forces p | Y and hence p² | M, so squarefreeness gives gcd(X, M) = 1; with S ≡ 0
we have T ≡ 2X, so gcd(T, M) = 1 and

> **M | 2B_k.**  Put j = 2B_k/M ∈ ℤ_{>0}.

Now j = 2 ⟺ k = 1: U_k = M + 2ka squares to M² + 4kaM + 4k²a², equal to
M² + 4k²ab exactly when M = k(b−a), i.e. k = 1. And j > 2 for k ≥ 2, since
U_k > M + 2ka ⟺ kM > M. **So j ≥ 3.** *(Checked on 14,923 multipliers, zero
violations.)* Squaring 2U_k = jM + 4ka against U_k² = M² + 4k²D gives

> **M = 8ka(2k − j)/(j² − 4)**,  so with w = 2k − j > 0 and e = j² − 4 ≥ 5,
> M = 8kaw/e and b = a + M.

Meanwhile r_k < 2 requires 2k = (M/2√D)(√r_k − 1/√r_k) < M/(2√2·√D), i.e.
**M > 4√2·k√(ab)** — recall r_k is the *modulus* ratio, so the window is
r_k < 2, not τ_k < 2. Substituting M = 8kaw/e and b = a + 8kaw/e, and using
k = (j+w)/2, this becomes

> e² + 4jwe + 2w²(2e − 1) < 0.

For j ≥ 3 we have e ≥ 5, so every term is positive. Contradiction. ∎

**The reduction is verified symbolically, not just numerically.** Substituting
M = 8kaw/e, b = a + M and k = (j+w)/2 into the geometry M² − 32k²ab and clearing
by e²/a², `sympy` returns

> M² − 32k²ab  ≡  **−8(j+w)²·(e² + 4ejw + 2w²(2e−1))**  (up to the positive factor e²/a²),

so the ratio to the displayed quantity is exactly **8(j+w)²** — positive for
j, w > 0. The equivalence is therefore an algebraic identity rather than a
numerical coincidence, and the contradiction is exact.

**Robust to the constant.** An earlier draft printed the weaker M > 2√2·k√(ab)
at this step. Carrying that through instead gives

> e² + 4jwe + 4w²(e − 2) < 0,

also a sum of strictly positive terms for e ≥ 5. Expanded in j and w, both
reductions have negative part −8(j+w)² and −16(j+w)² respectively, dominated by
the 48ej²-type terms since e ≥ 5. So the theorem does not turn on which constant
is used — and the weaker one defines a *larger* geometry set, making the
measured disjointness a stronger statement rather than a weaker one.

**How much of the problem O.3 reaches — and it is a minority.** The hypothesis
"M odd and squarefree" is not cosmetic. For a = 1 with b admissible and odd,
b ≡ 1 (mod 4) forces **4 | M**, so O.3 is mute on the entire a = 1 family — which
is the family [Note L](note-L-rational-graph.md) identifies as driving the full
graph's growth, and which contains both of the tightest *occupied* candidates,
(1, 115921) and (1, 226801), at M = 115920 and 226800. Over the 95:

| | count |
|---|---|
| M odd | 35 |
| M squarefree | 17 |
| **both — O.3 applies** | **17** |
| a = 1 (all with M even, all outside O.3) | 15 |

The parallel session's larger census agrees: over a ≤ 60, b ≤ 300000, **104 of
534 (19.5%)** of the pairs admitting a k ≥ 2 with r₁r_k < 2 have M odd and
squarefree. "No window holds three" reads broader than a statement mute on four
fifths of them and on the whole a = 1 family.

### Theorem O.3′ — squarefreeness replaced by a checkable gcd

> **Convention, stated because it caused a collision.** Throughout this note
> **r_k denotes the MODULUS ratio** m_j/m_i, not the X-ratio. The two differ by a
> square: the X-ratio is τ_k and the modulus ratio is τ_k². So "both moduli in
> one dyadic window" is **r_k < 2**, equivalently τ_k < √2, equivalently
> **M > 4√2·k√(ab)**. Reading r_k as the X-ratio instead gives the weaker
> M > (8/3)k√(ab) and the ρ bound below is then false — 344 violations in a box
> where the correct condition has 0. Checked on the realised pair
> (53, 423125): observed modulus ratio 1.70000, r₁₂ = 1.70066, τ₁₂ = 1.30409.

The squarefree hypothesis can be dropped for a much weaker one, and the proof
gets shorter rather than longer. Put **ρ = B_k/M**. Then B_k = ρM gives
U_k = ρM + 2ka, and U_k² = M² + 4k²ab with b = a + M yields the identity

> **M(ρ² − 1) = 4ka(k − ρ)**,  i.e.  M = 4ka·Λ with Λ = (k−ρ)/(ρ²−1).

*(Verified, 0 violations over all 95 geometry-passing candidates.)* The geometry
r_k < 2 needs M > 4√2·k√(ab); substituting M = 4kaΛ and ab = a² + aM reduces it
to Λ² − 8kΛ − 2 > 0, so Λ > 4k + √(16k²+2). Feeding that back,

> 9k − ρ > 8kρ²,  so  ρ² < 9/8 − ρ/(8k) < 1.125,  hence **ρ < 1.06066**.

*(Measured over every multiplier with modulus ratio < 2: ρ_max = 1.058207,
**0 violations** of ρ² < 9/8. The parallel session's independent run in exact
`Fraction` arithmetic gives ρ_max = 1.057143, also 0.)*

Now integrality. With M | S, τ_k gives M | B_kT and T ≡ 2X, so
**M | c·B_k where c = gcd(M, 2X)** — and hence **cρ ∈ ℤ**. But cρ lies in
(c, 1.06066c), which contains an integer only when 1.06066c ≥ c+1, i.e.

> **c ≥ 17.**

> **Theorem O.3′.** If gcd(M, 2X) ≤ 16, no dyadic window contains
> (ξ, τ₁ξ, τ_kξ) with k ≥ 2 — no hypothesis on M at all.

For M squarefree, gcd(X,M) = 1 forces c | 2, recovering Theorem O.3. But O.3′
applies to **4 | M** as well whenever the gcd stays small, which is the family
O.3 was mute on. Consistency check on the live non-fundamental pair below:
(1, 423125) has moduli m = 10 and 17, so X = 3 and 4 and c = gcd(423124, 6) = 2,
c = gcd(423124, 8) = 4 — both ≤ 16, and O.3′ correctly **permits** those two,
forbidding only a third.

*(ρ_max = 1.0582 needs c ≥ 18 to admit an integer in (c, 1.06066c), against the
17 the bound allows — the margin is real but thin, one unit.)*

### Theorem O.3″ — the discarded term, and why c ≤ 33 at k = 2

O.3′ throws information away at one step and it is recoverable. The chain reaches
ρ² < 9/8 − ρ/(8k) and then drops the second term using ρ > 0. But **ρ > 1 is
free**, and the proof of it needs nothing already derived:

> U_k = √(M² + 4k²ab) > 2k√(ab) > 2ka since b > a, so **ρ = (U_k − 2ka)/M > 0**.
> And Λ = (k−ρ)/(ρ²−1) > 0. If ρ² < 1 then k − ρ < 0, i.e. ρ > k ≥ 1, which
> contradicts ρ < 1. Hence ρ² > 1, i.e. **ρ > 1**. ∎

**k = 1 is the boundary and must be excluded, which is why this was invisible.**
There U₁ = a + b, so B₁ = b − a = M and **ρ = 1 exactly** — the identity reads
M·0 = 4a·0 and Λ = 0/0 is undefined. *(Verified: ρ = 1 identically on all 553,959
in-window k = 1 multipliers at X = 4000.)* For k ≥ 2, ρ = 1 would force
M·0 = 4ka(k−1) ≠ 0, so ρ > 1 is **strict**. O.3 already assumed k ≥ 2; the
sharpening costs no hypothesis.

Keeping the term, and using the exact Λ > A_k := 4k + √(16k²+2) rather than
Λ > 8k, the geometry gives

> **ρ² < 1 + (k − ρ)/A_k**,  hence with ρ > 1  **ρ² < 1 + (k−1)/A_k**.

At k = 2 that is ρ < 1.030543 against O.3′'s 1.060207 — the excess over 1 is
**halved**. *(0 violations over the 55 in-window k ≥ 2 multipliers at X = 4000,
and the tightest — (a,b) = (13, 26765) at k = 8, ρ = 1.052632 — sits at 0.9994 of
the bound. The bound is essentially saturated, so little more is available by
this route.)*

Now integrality, in the sharp form. Write **g = cρ ∈ ℤ**, so g > c. Substituting
ρ = g/c into M(ρ²−1) = 4ka(k−ρ) and clearing gives the exact Diophantine relation

> **M(g − c)(g + c) = 4kac(kc − g)**,

and M > 4ka·A_k turns it into **A_k(g−c)(g+c) < c(kc − g)**. With g = c + t,
t ≥ 1 an integer, this is A_k·t·(2c+t) < c(kc − c − t); the left side increases
in t and the right side decreases, so **t = 1 is the only case to check**:

> **Theorem O.3″.** A dyadic window contains (ξ, τ₁ξ, τ_kξ) with k ≥ 2 only if
>
> **(4k + √(16k²+2))·(2c+1) < c·(kc − c − 1)**,  where c = gcd(M, 2X).

Taking k → ∞ recovers c > 8 + √72 = 16.485, i.e. **c ≥ 17 — Theorem O.3′ is the
k-free shadow of this**. But the condition binds hard at small k:

| c | 17 | 18 | 19 | 20 | 21–22 | 23–25 | 26–33 | ≥ 34 |
|---|---|---|---|---|---|---|---|---|
| survives only for k ≥ | 35 | 13 | 8 | 6 | 5 | 4 | 3 | 2 |

> **In particular k = 2 needs c ≥ 34**, roughly doubling O.3′'s reach at the
> smallest index a triple can use, and c = 17 — the case O.3′ stops one unit
> short of — needs k ≥ 35.

**The ρ-bound and the region inequality differ by one at k = 2, 3, 4, and the
region form is the right one.** Reading off "cρ ∈ ℤ needs 1/(ρ−1)" from
ρ < √(1 + (k−1)/A_k) gives c ≥ 33 at k = 2, not 34. Neither is wrong: the ρ-bound
already spent ρ > 1 on the −ρ term, whereas the region inequality substitutes
ρ ≥ (c+1)/c into **both** places it appears. So the region form is strictly
sharper and the ρ-bound is its weaker corollary; they differ by exactly 1 at
k = 2, 3, 4 and agree from k = 5 on, where ρ ≈ 1 makes the two substitutions
indistinguishable.

| k | 2 | 3 | 4 | 5 | 10 | ≥ 35 |
|---|---|---|---|---|---|---|
| c from the ρ bound | 33 | 25 | 22 | 21 | 19 | 17 |
| c from the region inequality | **34** | **26** | **23** | 21 | 19 | 17 |

*(Caught by the parallel session verifying the claim text against its own
implementation — the note stated both forms and gave only the region numbers.)*

**What this does not do.** It still assumes τ₁ acts, so the p, q ≥ 2 gap that
keeps O.2 open is untouched; the live witness (53, 423125) at k = 12 excludes τ₁
and is not addressed. It shrinks the surviving region of an already-covered
family rather than reaching a new one.

**And measured against realised configurations it is far from binding.** At
X = 4000 every acting in-window multiplier with k ≥ 2 has **c ∈ {2, 4}** —
(c,k) = (2,12), (2,33), (2,91), (4,4) — against a threshold of 17. The theorem
holds with two orders of magnitude to spare on everything that occurs, which
says the constraint doing the real work in nature is not this one. Note that
measuring c here is legitimate where measuring the conclusion is not: c is read
off configurations that **do** occur, so this is not
`triples-cannot-be-settled-by-measurement`.

### Theorem O.4 — a bound that assumes nothing about which multiplier acts

O.3, O.3′ and O.3″ all assume τ₁ acts. **O.4 does not**, and that is the whole
point of it: it is the first statement here that reaches the p, q ≥ 2 gap where
O.2 is actually open.

The idea is composition. If m₁ < m₂ < m₃ are three shared moduli of one class,
the two steps have multipliers τ₁₂, τ₂₃ — whatever they happen to be — and the
composite τ₁₃ = τ₁₂τ₂₃ is what the window has to accommodate. Since **every**
multiplier is at least the smallest one, the window must fit τ_min².

Write T = {(U + V√D)/M : U² − DV² = M², U, V ∈ ℤ} and τ_min = min{τ ∈ T : τ > 1}.

> **Step 1 (the map).** Any two solutions give U = bX_iX_j − aY_iY_j and
> V = X_iY_j − X_jY_i with U² − DV² = M², and **X_j = (UX_i + VaY_i)/M**,
> Y_j = (UY_i + VbX_i)/M. *(0 failures over all 1950 consecutive pairs at
> X = 3000, trying all four sign conventions — and it holds across orbits, not
> only within one.)*
>
> **Step 2 (the exact inequality).** aY_i² = bX_i² + M > bX_i² gives
> aY_i > X_i√(ab) = X_i√D, so
>
> **X_j > ((U + V√D)/M)·X_i = τ_V·X_i.**
>
> *This is where the factor a cancels, and it is the step to get right.* Bounding
> the symmetric form |V| = M(X_j²−X_i²)/(X_jY_i + X_iY_j) instead loses a factor
> of a and yields τ evaluated at V/a — correct but weaker, and wrong at a > 1.
> Going through the map is what makes it sharp.
>
> **Step 3.** τ_V ≥ τ_min at each step, so X₃ > τ_min²X₁, and m = (X²+1)/a gives
>
> **m₃/m₁ = (X₃² + 1)/(X₁² + 1) > (τ_min⁴X₁² + 1)/(X₁² + 1).**
>
> **Step 4.** A dyadic window needs m₃/m₁ < 2, i.e. τ_min⁴X₁² < 2X₁² + 1. ∎

> **Theorem O.4.** Three shared moduli of the class (a, b) lie in one dyadic
> window only if **τ_min⁴ < 2 + 1/X₁²**, where X₁ = √(am₁ − 1) is the smallest.

**The finite term is not decoration — it is why the clean form is false.** The
modulus ratio equals τ² only asymptotically; exactly, m = (X²+1)/a. Dropping the
+1 gives "m_{i+2}/m_i ≥ τ₁⁴", which **fails 9 times in 110 gaps at X = 4000** —
tightest at (a,b) = (1,5), m = 2 → 65, where the observed 32.50 is well under
τ₁⁴ = 46.98. With the correction there are **0 violations in 110**, and it is
sharp: at (1,5), m = 20737 → 974170 the bound is 46.9765 against an observed
46.9774.

Since |V| ≥ 2 unless a² − ab + b² is a perfect square, **τ_min = τ₁** and the
theorem is a threshold on b/a that tightens as m₁ grows:

| X₁ | 1 | 2 | 3 | 5 | 10 | → ∞ |
|---|---|---|---|---|---|---|
| needs τ₁⁴ < | 3 | 2.25 | 2.111 | 2.04 | 2.01 | 2 |
| needs b/a > | 53.69 | 97.99 | 115.29 | 126.58 | 131.98 | **133.87** |

In closed form, against the **pair** threshold b/a > (1+√2)⁴ = 33.9706:

> **triple:  b/a > [(1+√2)(1 + √2 + 2^{5/4})]² = 133.8748…**,  equivalently
> **M > 4(2^{1/4} + 2^{3/4})√(ab) = 11.4840·√(ab)**,
> and the two thresholds are t_pair = (1+√2)² and
> t_triple = t_pair + 2^{5/4}(1+√2).

**It is slightly stronger than the determinant route, and it repairs that
route's recorded constant.** From `three-term-determinant-identity`, |V₁₃| ≥ 4
with the exact |V| < (M/2√D)(R − 1/R) gives **M > 8√2·√(ab) = 11.3137√(ab)**
asymptotically — and only 6.93√(ab) at X₁ = 1. This note had recorded that route
as yielding 11.484 unconditionally; it does not, and the section above is
corrected. O.4 reaches **11.4840** because 2^{1/4} enters from the *composite*
τ₁² < √2 rather than from |V| ≥ 4, and the two expressions coincide exactly:
4/(2^{1/4} − 2^{−1/4}) = 4(2^{1/4} + 2^{3/4}). **The value in the note was right;
the derivation attached to it was not.**

**What O.4 does not do.** It is a necessary condition, not a contradiction, so
O.2 stays open; it quadruples the threshold (33.97 → 133.87) without closing
anything. And it is not binding in practice either: among the 31 classes at
X = 4000 that clear b/a > 133.87 *and* hold three moduli, the smallest two-step
ratio is **14.50** at (a, b) = (1, 533) — a factor 7.25 from the 2 a window
needs. The live witness (53, 423125) has b/a = 7983.5 and is permitted, correctly,
since it carries a pair and not a triple.

### Theorem O.5 — the p = q case, closed outright

O.4 bounds the composite from below by τ_min². When the **two steps carry the
same multiplier** the composite is τ_p², and then the integrality of τ_p² is a
divisibility on M alone — which closes that case completely.

> τ_p² = (U_p + 2p√D)²/M² = (U' + V'√D)/M with
> **U' = (M² + 8p²D)/M = M + 8p²D/M** and **V' = 4pU_p/M**.

So τ_p² ∈ T requires M | 8p²D. Now D = ab = a(a + M) ≡ a² (mod M), and
gcd(a, M) = gcd(a, b − a) = gcd(a, b) = 1 because the class is reduced. Hence

> **τ_p² ∈ T  ⟹  M | 8p².**

*(0 failures over the 555 occurrences of τ_p² ∈ T with a ≤ 60, b ≤ 4000,
p ≤ 30. At p = 1 it reads M | 8, verified separately as an equivalence over
133,670 coprime pairs.)*

The window then contradicts it with no room at all. O.4 with X₁ ≥ 1 gives
τ_p⁴ < 3, so τ_p < 3^{1/4}; τ_V < c forces Vs < (c²−1)/(2c) with s = √D/M, so
with V = 2p

> p < 0.139060·M/√D,  hence  **8p² < 0.154701·M²/D**.

But M | 8p² gives M ≤ 8p², so D < 0.154701·M < M. And **M < D always** —
M = b − a < b ≤ ab = D for a ≥ 1. Contradiction.

> **Theorem O.5.** No dyadic window contains (ξ, τ_pξ, τ_p²ξ), for any p ≥ 1,
> provided X₁ ≥ 1. No hypothesis on M, on a, or on which multipliers act.

**State the X₁ ≥ 1, do not leave it implicit.** It is inherited from O.4 and it
excludes exactly one configuration: X₁ = 0 means am₁ = 1, i.e. a = 1 and m₁ = 1.
That case is **vacuous rather than open** — the window [1, 2) contains the single
modulus 1 — but Proposition O.1 was stated without its window hypothesis and was
false as written, so an unstated hypothesis is the specific way results in this
note have gone wrong before.

**This supersedes Proposition O.1**, which is the p = 1 case and needed the
auxiliary a·g² < M with g = gcd(U,V), a window hypothesis, and an escape clause.
O.5 explains the escape rather than tolerating it: at (a,b) = (1,5) we have
M = 4 | 8, so τ₁² genuinely **is** in T — O.1's inequality failing there by
nothing (a·g² = 4 = M exactly) was the symptom, and the cause is that the
integrality is fine and it is the *window* that fails. The two realised classes
where τ₁² acts at X = 3000 are (1,5) with M = 4 and (1,2) with M = 1, both
dividing 8.

**What it does not reach is p ≠ q.** The two steps of a triple may carry
different multipliers, and then the composite's integrality is
M | U_pU_q + 4pqD, which does not collapse: multiplying by the conjugate returns
M | M²(M² + 4(p²+q²)D), true for free. So **O.2's surviving case is exactly two
*distinct* multipliers**, and that is now the whole of it — the equal case is
closed and the τ₁-assuming cases were closed by O.3″. The live witness
(53, 423125) at k = 12 is a pair, so it does not exhibit the surviving case
either; nothing realised does.

### Proposition O.6 — the sign alternates at every step

With O.3″ covering the τ₁-assuming cases and O.5 the equal-multiplier case, what
survived of O.2 was two **distinct** multipliers. This is the attempt to close
that for M = b − a an odd prime, and the outcome is that **it cannot be closed
this way** — with a mechanism, which is worth more than another threshold.

Mod M we have b ≡ a, so τ_p acting on ξ = (X, Y) gives **M | A_pS and M | B_pT**
with A_p = U_p + 2pa, B_p = U_p − 2pa, S = X+Y, T = X−Y. For M an odd prime
U_p² ≡ (2pa)² makes the **sign ε_p well defined**: M | B_p or M | A_p, never both
(both give M | 4pa, hence M | p, impossible for an in-window p < M).

> **The dichotomy.** M | S and M | T cannot both hold — they give M | X and
> M | Y for M odd, so M² | aY² − bX² = M, i.e. M = 1. And for an in-window
> multiplier neither can fail. So **exactly one holds, and it forces the sign**:
> M | S ⟹ M | B_p (ε_p = +1); M | T ⟹ M | A_p (ε_p = −1).

**The exact identities matter, and the natural guess is wrong.**

> **M·S′ = A_pS + V_p·M·X**  and  **M·T′ = B_pT − V_p·M·X.**

Not S′ = A_pS/M — that is what a first pass gives from the mod-M relation, and it
**fails on every single pair, 246 of 246**. The necessary conditions M | A_pS and
M | B_pT survive it; the orbit bookkeeping does not.

> **Proposition O.6 (alternation).** In subcase A (M | S) write B_p = Mβ. Then
> A_pβ = M + 4p²a with A_p ≡ 4pa forces **β ≡ p (mod M)**, and T ≡ 2X gives
> T′ ≡ 2X(β − p) ≡ 0. So ξ′ is in subcase B; symmetrically B → A. **The subcase
> alternates at every step.**

*(246 steps at X = 3000: alternates **246 times, stays the same 0 times**, with
ε forced by the subcase and β ≡ p — resp. α ≡ −p — with 0 failures throughout.)*

**And that is exactly what kills the route.** A triple ξ₁ → ξ₂ → ξ₃ therefore has
ε_p = +1 and ε_q = −1, and then both of the composite's integrality conditions
are **automatic**:

> qU_p + pU_q ≡ 2pqa − 2pqa ≡ 0  and  U_pU_q + 4pqD ≡ −4pqa² + 4pqa² ≡ 0 (mod M).

*(0 failures over 493 opposite-sign (p,q) pairs. By contrast **40 of 246
same-sign pairs fail both** — so the conditions genuinely have content, and the
alternation is precisely what removes it.)*

> **So the composite's integrality conditions carry no information.** The
> structure that lets τ_p act on ξ₁ is the same structure that makes τ_q's action
> on ξ₂ integrality-free.

> ### ⚠ CORRECTED — this section first concluded "the integrality route cannot
> close O.2", and that is **too strong**. What is dead is the *composite's
> integrality conditions*, which is what the numbers above measure. The
> **alternation itself** is a different constraint — a consistency condition, not
> a divisibility — and **Theorem O.7 below closes the M odd prime case with it**.
> The correct statement is the narrow one: those two conditions are vacuous.
> Recorded rather than rewritten, because "route X is dead" was asserted here on
> evidence that only showed "sub-route X′ is dead", which is the single most
> repeated error in this repo.

**This is the mechanism behind an observation already in the repo.** "There is no
local obstruction — all 95 candidates are satisfiable mod M" was an empirical
remark about 95 cases. For M an odd prime the *pointwise* satisfiability is now
explained: the signs alternate, so each composite condition holds for free. What
does **not** follow — and what this note wrongly inferred for an hour — is that
no congruence-flavoured argument can work. The alternation is itself such an
argument, and it closes the case.

**And the case was worth closing, which is why the failure is informative.**
M odd prime is **54 of the 379 realised close pairs (14%)**, not a corner. What
fails is the method, not the coverage.

### Theorem O.7 — Conjecture O.2, proved for M an odd prime

The alternation is not just a description; it is a **consistency** constraint,
and three moduli in one window violate it. The whole proof is that a two-step
chain and the one-step composite disagree about where ξ₃ sits.

> **The exact identity.** For any two solutions,
> **a·|V|·(X_jY_i + X_iY_j) = M(X_j² − X_i²)**.
> *(0 failures over 4033 pairs at X = 6000. The factor a is easy to drop — my
> first version did — and it is what makes the next line come out clean.)*
>
> **The in-window bound.** aY² = bX² + M > bX² gives Y > X√(b/a), so
> X_jY_i + X_iY_j > 2X_iX_j√(b/a) and
>
> **|V| < (M/2√D)(R − 1/R)**,  R = X_j/X_i.
>
> A window with X_i ≥ 1 gives R² = X_j²/X_i² < 2 + 1/X_i² ≤ 3, so R − 1/R < 2/√3
> and **|V| < 0.57735·M/√D ≤ 0.40825·M < M**. Since V ≠ 0, **M ∤ V for every
> in-window pair.** *(0 failures over 751 in-window pairs, max |V|√D/M = 0.3529
> against the bound 0.57735; and M | V occurs 0 times.)*
>
> **The dichotomy needs exactly that.** Both M | S and M | T give M | X and M | Y,
> so M² | aY² − bX² = M, i.e. M = 1. Neither gives M | A_V and M | B_V, hence
> M | A_V − B_V = 2Va, hence M | V — excluded. So **exactly one holds**.
>
> **The contradiction.** Let ξ₁, ξ₂, ξ₃ lie in one dyadic window. All three
> pairwise ratios are < 2, so M ∤ V for all three steps and Proposition O.6
> applies to each. Say ξ₁ is in subcase A. Then ξ₂ is in B, so ξ₃ is in A. But
> **ξ₁ → ξ₃ is itself a single step**, so ξ₃ is in B. By the dichotomy ξ₃ cannot
> be both. ∎

> **Theorem O.7.** For M = b − a an odd prime, no dyadic window contains three
> shared moduli of the class (a, b). This is **Conjecture O.2 for M odd prime**,
> and it assumes nothing about which multipliers act — it covers p ≠ q.

**The realised triples escape exactly where the proof says they must.** M ∤ V is
the only hypothesis, and every realised M-odd-prime class holding three moduli
has **M | V on its two-step**:

| (a,b) | M | two-step | V₁₃ | V₁₃/M |
|---|---|---|---|---|
| (2, 13) | 11 | 5 → 48985 | 110 | 10 |
| (2, 5) | 3 | 13 → 18241 | 18 | 6 |
| (2, 25) | 23 | 13 → 499001 | 322 | 14 |

Those triples are real and far outside any window — ratios of 10⁴ and up — which
is precisely how |V| gets past 0.577·M/√D. *(Over all pairs with M odd prime at
X = 6000: 454 of 459 flip the subcase, and **all 5 that do not have M | V**.)*

### Theorem O.8 — the same argument for M odd squarefree, on one hypothesis

The dichotomy generalises, and it comes from an identity that is worth having on
its own.

> **Lemma O.8.1.** For any shared modulus m of the class (a, b), with S = X + Y
> and T = X − Y: **S·T = −M·m**.
>
> *Proof.* aY² − bX² = M with b = a + M gives a(Y² − X²) = M(X² + 1) = M·am, so
> Y² − X² = Mm. ∎  *(0 failures over 822,349 solutions at X = 4000.)*

> **Lemma O.8.2.** For M odd, **gcd(M, S)·gcd(M, T) = M**.
>
> *Proof.* Let p^e ‖ M. By O.8.1, v_p(S) + v_p(T) = e + v_p(m). If p ∤ S then
> v_p(T) = e + v_p(m) ≥ e, so the two contributions are 0 and e; symmetrically for
> p ∤ T. If p divides **both** then p | 2X and p | 2Y, so p | X, so
> am = X² + 1 ≡ 1 (mod p) and **p ∤ m** — whence v_p(S) + v_p(T) = e with both
> terms ≤ e, and the min-sum is again e. ∎  *(0 failures over the same 822,349;
> and the p | S, p | T ⟹ p | X ⟹ p ∤ m step checked on all 141,277 instances.)*

So the dichotomy of O.7 is really a **factorisation** M = M⁺·M⁻ with M⁺ | S and
M⁻ | T. For M **squarefree** each e = 1, so the split is exact prime by prime —
exactly one of p | S, p | T — and O.6's alternation localises.

> **Theorem O.8.** For M odd and squarefree, if **gcd(V, M) = 1** on each of the
> three pairwise steps, no dyadic window contains three shared moduli.
>
> *Proof.* gcd(V,M) = 1 makes the local sign defined at every p | M, so the local
> subcase flips at each prime, i.e. the pair (gcd(M,S), gcd(M,T)) **swaps**. Two
> steps restore it, one step swaps it, and M⁺ = M⁻ is impossible for M squarefree
> > 1. ∎

*(The local flip holds at every p | M on all 710 qualifying pairs at X = 4000,
0 failures; and the swap holds on **1333 of 1333** pairs with gcd(V,M) = 1 over
all odd M — 1089 of 1089 restricted to squarefree.)*

**The coprimality hypothesis is observed, not proved, and that is the honest
gap.** Every in-window pair at X = 6000 has gcd(V, M) = 1 — **295 of 295, no
exceptions** — but the window bound |V| < 0.57735·M/√D bounds V without making it
coprime to M. Note gcd(V,M) = 1 is **equivalent to g = gcd(U,V) = 1**: g | M and
g | V give g | gcd(V,M), and conversely p | gcd(V,M) forces p | U since
U² = M² + DV². So this is the same quantity Proposition O.1's chain already
tracks, where all that is known in-window is a·g² < M — which permits g > 1.

**Two separate things are being asked of M, and it is worth not conflating
them.** *Coprimality* is what separates swap from non-swap: **every** observed
non-swap has gcd(V, M) > 1, and there are none among the 1333 pairs with
gcd(V, M) = 1. *Squarefreeness* is needed for a different reason — it makes
O.8.2 a **dichotomy** per prime rather than a partial split. At M = 9 the pair is
(3, 3): neither p^e | S nor p^e | T, so there is no local subcase to flip.

*(A first pass here recorded the non-swaps as "all at M = 9", from an example
list that happened to show only those. Printing the distribution gives
M = 3, 9, 11, 15, 21, 23 — most of them squarefree. The right invariant is
gcd(V,M), not squarefreeness, and reading six examples instead of the counts is
how the two got conflated.)*

### Theorem O.9 — the same conclusion with no hypothesis, by pigeonhole

O.8's coprimality assumption turns out to be unnecessary, and dropping it makes
the argument shorter. The mechanism is a **sign**, and the contradiction is that
three signs cannot be pairwise distinct.

> **The sign.** For p | M odd, aY² = bX² + M gives **Y² ≡ X² (mod p)**, and
> p ∤ X: otherwise p | Y, so p | S and p | T, while S·T = −M·m with v_p(M) = 1
> forces v_p(S) + v_p(T) = 1. So each solution carries
> **σ_i = ±1 with Y_i ≡ σ_i X_i (mod p)**.
>
> **The equivalence.** V_ij = X_iY_j − X_jY_i ≡ X_iX_j(σ_j − σ_i) (mod p), and p
> is odd with p ∤ X_iX_j, so
>
> **p | V_ij ⟺ σ_i = σ_j.**
>
> *(0 failures over 1,588,226 (p, solution) sign determinations and 1317
> (p, pair) equivalence checks at X = 4000.)*
>
> **The pigeonhole.** Three values in {±1} cannot be pairwise distinct, so **at
> every p | M some pair has σ_i = σ_j**, hence p divides one of V₁₂, V₂₃, V₁₃.
> For M squarefree that is **M | V₁₂·V₂₃·V₁₃** — *unconditionally*.
> *(0 failures over the realised triples.)*
>
> **The size.** In a window R² = X_j²/X_i² < 2 + 1/X₁² ≤ 3, so R − 1/R < 2/√3 and
> **|V| < (M/2√D)(R − 1/R) < M/√(3D)**. With V ≠ 0,
> M ≤ |V₁₂V₂₃V₁₃| < M³/(3D)^{3/2}. ∎

> **Theorem O.9.** For M = b − a odd and squarefree, a dyadic window contains
> three shared moduli (with X₁ ≥ 1) only if
>
> **3ab < (b − a)^{4/3}**,  equivalently  **a < (t−1)²/(3t)^{3/2}** for t = b/a,
>
> so asymptotically **b > 27a³**.

**This supersedes Theorem O.8**, whose gcd(V, M) = 1 was not needed, and it
recovers **O.7** as the case M prime: there step 3 gives M | V_ij for some pair,
against 0 < |V_ij| < M/√(3D) < M. So O.7 holds with **no hypothesis at all**, not
merely with one that happens to be observed.

**How strong is it? — read the denominator, and see the correction under O.10.**
Over *all* M-odd-squarefree classes, 499,188 of 503,054 (99.2%) fail
3ab < M^{4/3} — but a class with fewer than three shared moduli cannot host a
triple whatever any theorem says, so that figure measures vacuity. On the
**informative** population it is **~35%**, flat in X. Combined with O.4's
t > 133.875 the admissible a is small: **a ≤ 2** at the minimum admissible t,
6 at t = 10³, 19 at t = 10⁴.

*(The parity input |V| even whenever M is odd is `V-is-even-whenever-M-is-odd`
in the registry, proved there rather than restated here.)*

**And the pair-level identity is cleaner without the cofactor** — the parallel
session's, and distinct from Lemma O.8.1 (S·T = −M·m is about a single modulus,
V·W about a pair). It is mine divided by a:

> **V·W = M·(m_i − m_j)**,  W = X_jY_i + X_iY_j.

*(0 failures over 2747 pairs.)* Since Y² = X² + Mm, VW = X_i²Y_j² − X_j²Y_i² =
M(X_i²m_j − X_j²m_i) = M(m_i − m_j) using X² = am − 1. **The a cancels
entirely**: the relation is between V, W, M and the modulus gap alone. It also
gives the dual reading — for M odd squarefree, exactly one of V, W is divisible
by each p | M, so **gcd(V,M) = 1 ⟺ M | W**.

### Theorem O.10 — no hypothesis on M at all: the sign becomes a valuation

O.9 needs M odd squarefree because it needs a two-valued **sign**. The p-adic
version needs nothing: replace the sign by a **valuation split**, and the
pigeonhole by an ordering.

> Fix p^e ‖ M. Since gcd(a, b) = 1 and M = b − a, **gcd(a, M) = 1**. Then
> b ≡ a (mod p^e) and aY² = bX² + M give **Y² ≡ X² (mod p^e)**, i.e. p^e | S·T
> — which is Lemma O.8.1 again, S·T = −M·m.
>
> Put **s_i = min(e, v_p(S_i))** and **t_i = min(e, v_p(T_i))**. Then
> **s_i + t_i ≥ e**: if v_p(S) ≥ e then s = e; otherwise
> v_p(T) ≥ e − v_p(S) gives t ≥ e − s.
>
> p^{s_i} | S_i means Y_i ≡ −X_i (mod p^{s_i}), and p^{t_i} | T_i means
> Y_i ≡ X_i (mod p^{t_i}). Either congruence kills V_ij = X_iY_j − X_jY_i, so
>
> **v_p(V_ij) ≥ max( min(s_i,s_j), min(t_i,t_j) ).**
>
> **Order s₁ ≤ s₂ ≤ s₃.** Then v_p(V₂₃) ≥ min(s₂,s₃) = s₂ and
> v_p(V₁₂) ≥ min(t₁,t₂) ≥ e − s₂, so **v_p(V₁₂) + v_p(V₂₃) ≥ e**. ∎

> **Theorem O.10.** For **any** M = b − a — odd or even, squarefree or not —
> **M | V₁₂·V₂₃·V₁₃**; and since a window gives 0 < |V| < M/√(3D),
>
> **3ab < (b − a)^{4/3}.**

*(0 failures at X = 4000 over 12,447,219 checks of s + t ≥ e, 6266 of the
v_p(V) lower bound, and 224 of the ordered two-term sum; and M | V₁₂V₂₃V₁₃ holds
on every realised triple in all four categories — odd squarefree 23,
odd non-squarefree 39, even non-squarefree 216.)*

> ### ⚠ DO NOT reduce the two-term sum to a fixed pair
>
> The step above gives **v_p(V₁₂) + v_p(V₂₃) ≥ e**, two terms rather than three,
> and the obvious next move is to conclude **M | V_a·V_b for some fixed pair** —
> which with |V| < M/√(3D) would give M ≤ |V_aV_b| < M²/(3D), i.e.
> **3ab < b − a**, impossible for a ≥ 1. That closes Conjecture O.2 in one line,
> and it is **wrong**.
>
> **The ordering that selects the pair is computed per prime**, so different
> primes select different pairs, and only the *three*-term product is uniform
> across all of them. **5 of 216 realised triples admit no single pair whose
> product M divides**: (1,481) M = 480; (1,925) M = 924; (1,106) M = 105;
> (1,2465) M = 2464; (1,1450) M = 1449 — every one with M carrying ≥ 3 distinct
> primes, which is exactly the room the orderings need to disagree.
>
> *(The parallel session made this move an hour after establishing the two-term
> form, and caught it only because the conclusion 3ab < b − a is false by
> inspection. A slightly weaker over-reach would have shipped. Recorded here, and in
> `note-P-method.md`; CLAUDE.md now carries only the one-line rule.)*


**The sign was the e = 1 shadow of this.** At v_p(M) = 1, s and t lie in {0,1}
and S·T = −M·m forces s + t = 1 exactly, so (s,t) is (1,0) or (0,1) — precisely
σ = ∓1. "Three signs in {±1} collide" becomes "order by s and take the middle
two", and that is the only step that changes.

**So there is no remaining case.** The parallel session's intermediate form
restricted to M₁ = ∏{odd p ‖ M} and left classes with M₁ = 1 silent — M a power
of two times a powerful odd part. The valuation form covers those too.

> ### ⚠ THE DENOMINATOR — and both of us got this wrong
>
> A first version of this section reported **99.26% of classes excluded**. That
> figure is over *every* ratio class, and **a class with fewer than three shared
> moduli cannot host a triple whatever any theorem says**. At X = 3000 only
> **60 of 1,815,154 classes have three shared moduli at all** — so the theorem is
> vacuous on 99.997% of what was being counted, and the percentage measured the
> vacuity, not the reach.
>
> **On the informative population — classes with ≥ 3 shared moduli — it is ~35%,
> and stable:**
>
> | X | informative classes | excluded by 3ab < M^{4/3} |
> |---:|---:|---:|
> | 2000 | 48 | 17 (**35.4%**) |
> | 3000 | 60 | 21 (**35.0%**) |
> | 4000 | 70 | 24 (**34.3%**) |
> | 6000 | 96 | 34 (**35.4%**) |
>
> The comparison with the M₁ form survives and is the honest gain: on the same
> 60 classes at X = 3000 the M₁ form excludes **9 (15.0%) and is silent on 21
> (35.0%)**, while the valuation form excludes **21 (35.0%) and is silent on
> none**. More than double the reach, and no silent class — but **35%, not 99%**.
>
> This is the repo's own rule — *the informative subset is never the one the loop
> naturally counts* — arriving in a new place, and it caught both sessions within
> the hour for the same mechanical reason: `ratio_classes` returns every class,
> so sweeping every class is what one writes. **A percentage here must carry its
> population in the same sentence.**

### Theorem O.11 — the three ratios are not independent, and that is worth 6.85×

O.10 bounds all three |V| by the same extreme, as if R₁₂, R₂₃ and R₁₃ could each
sit at the window's edge. They cannot: **R₁₂·R₂₃ = R₁₃**, so pushing two of them
out pushes the third past the window.

Write R = e^u, so the exact per-pair bound |V_ij| < (M/2√D)(R_ij − 1/R_ij) reads
**|V_ij| < (M/√D)·sinh(u_ij)**, with u₁₂ + u₂₃ = u₁₃ ≤ ln ρ, ρ = √(2 + 1/X₁²).

> For fixed u₁₃, **sinh(u₁₂)·sinh(u₂₃) is maximised at u₁₂ = u₂₃ = u₁₃/2** — the
> derivative is sinh(u₁₃ − 2u₁₂), and the second derivative is negative there.
> *(Confirmed numerically: the maximum of sinh(u)sinh(w−u) over a 2000-point grid
> sits at u = w/2 to eight digits.)* So, all three factors increasing in u₁₃,
>
> f(R₁₂)f(R₂₃)f(R₁₃) ≤ 16 sinh³(u₁₃/2)cosh(u₁₃/2) = **(√ρ − 1/√ρ)³(√ρ + 1/√ρ)**
>
> — call it C(X₁). Then M ≤ |V₁₂V₂₃V₁₃| < (M/2√D)³·C gives (2√D)³ < C·M².

> **Theorem O.11.** A dyadic window contains three shared moduli only if
> **ab < (C(X₁)/8)^{2/3}·(b − a)^{4/3}**, C(X₁) = (√ρ − 1/√ρ)³(√ρ + 1/√ρ),
> ρ = √(2 + 1/X₁²). Asymptotically **ab < 0.048628·(b−a)^{4/3}**, against O.10's
> 0.333 — **6.85× stronger**.

| X₁ | 1 | 2 | 3 | 5 | 10 | → ∞ |
|---|---|---|---|---|---|---|
| ab < c·M^{4/3}, c = | 0.1259 | 0.0670 | 0.0567 | 0.0515 | 0.0493 | **0.04863** |

**Coverage, over the informative population — and the trend is the point.**

| X | informative classes | O.10 excludes | O.11 excludes |
|---:|---:|---:|---:|
| 1500 | 43 | 14 (32.6%) | 42 (**97.7%**) |
| 2000 | 48 | 17 (35.4%) | 46 (95.8%) |
| 3000 | 60 | 21 (35.0%) | 57 (95.0%) |
| 4000 | 70 | 24 (34.3%) | 65 (92.9%) |
| 6000 | 96 | 34 (35.4%) | 88 (91.7%) |
| 8000 | 109 | 37 (33.9%) | 96 (**88.1%**) |

> **⚠ Do not read 88–98% as an asymptotic.** O.10's ~35% is flat in X; **O.11's
> is falling monotonically** — 97.7, 95.8, 95.0, 92.9, 91.7, 88.1 — and the
> admissible count is roughly doubling as X doubles (1, 2, 3, 5, 8, 13) while the
> informative population grows only 2.5× over the same range. So the reach may
> well tend to 0, and **no claim is made about its limit.** What is proved is the
> inequality; the percentages are a finite observation over a stated population,
> which is the distinction the denominator correction above was about.

**And every class O.11 admits has a = 1**, which is the cofactor the Type II
question cannot see.

| X | informative | a = 1 | a ≥ 2 | admitted, a = 1 | admitted, a ≥ 2 |
|---:|---:|---:|---:|---:|---:|
| 1500 | 43 | 34 | 9 | 1 | **0** |
| 2000 | 48 | 36 | 12 | 2 | **0** |
| 3000 | 60 | 44 | 16 | 3 | **0** |
| 4000 | 70 | 51 | 19 | 5 | **0** |
| 6000 | 96 | 66 | 30 | 8 | **0** |
| 8000 | 109 | 76 | 33 | 13 | **0** |

**119 informative classes with a ≥ 2 across the six sizes, and O.11 excludes
every one** — and **that fact carries no information.**

> **⚠ The a ≥ 2 column cannot test the question.** The largest b among informative
> classes with a ≥ 2 is **925 at X = 3000 and 8321 at X = 6000**, against an
> a = 2 crossover of **7×10⁴**. Nothing with a ≥ 2 is within an order of magnitude
> of being admitted, so "O.11 excludes every one" is a statement about the sweep's
> reach and not about a ≥ 2.
>
> **The headline this nearly produced was false.** Since `full-graph-growth-is-pell`
> records that n₁ = 1 cannot occur in a Type II hypothesis, *"O.11 is exhaustive
> on exactly the classes the Type II question ranges over"* was true of every
> number in the sweep, connected two notes — and is **wrong**, for range reasons
> alone. Same shape as the Plücker constant: correct arithmetic, correct-sounding
> synthesis, no causal content. Caught by the parallel session asking not where
> the crossover is but **how far the data is from it**.

> **⚠ This is a range effect, not a law, and the law is easy to write down.**
> O.11 admits (a, b) as soon as ab < c·(b−a)^{4/3}, and for **fixed a** the right
> side wins as b → ∞. The crossover is b ≳ 9.0×10³ at a = 1, 7.0×10⁴ at a = 2,
> 2.4×10⁵ at a = 3, 1.1×10⁶ at a = 5. So the a ≥ 2 column is empty because the
> sweep does not reach far enough in b, and it **will** fill in at larger X. The
> honest statement is the finite one: *no informative class with a ≥ 2 is admitted
> for X ≤ 8000*, and the a = 1 column is already filling (1, 2, 3, 5, 8, 13).

### Theorem O.12 — C₄-freeness over Z, on the configuration Type II uses

Everything above windows the **moduli** and lets the cofactors range freely. But
Ford–Maynard's (II) is a bilinear form over **m ~ M and n ~ N**: *both* variables
sit in ranges, and `fm-barrier-range-is-small-moduli` records that footnote 2
averages over m₁, m₂ ~ x^{1−2c+ε} — the cofactors are banded too. On that
configuration the question is not O.2 at all, and it is already settled.

> **Two cofactors in one dyadic band are within a factor 2 of each other**, so
> u = n₂/n₁ < 2 and, with d = gcd(n₁,n₂), **b/a = n₂/n₁ < 2**.

Run the pair bound at the weakest multiplier the lattice permits. A pair of
shared moduli m_i < m_j < 2m_i with X_i ≥ 1 needs X_j > τ_V X_i, so
m_j/m_i > (τ_V²X_i² + 1)/(X_i² + 1) and **τ_V² < 2 + 1/X_i² ≤ 3**. τ is
increasing in |V| and |V| ≥ 1, so τ_V ≥ τ(1) = √(1+s²) + s with s = √D/M; and
τ(1)² < 3 forces s < 1/√3, i.e. **M/√D > √3**. Finally M/√D = (u−1)/√u, and

> (u−1)/√u > √3  ⟺  u² − 5u + 1 > 0  ⟺  **u > (5+√21)/2 = 4.7913**.

> **Theorem O.12.** If n₂/n₁ < (5+√21)/2 = 4.7913 — in particular if n₁ and n₂
> lie in **one dyadic band** — then they share **at most one modulus in any
> dyadic window**. The rational incidence graph restricted to the doubly-dyadic
> configuration is **C₄-free**.

*(Margin 2.4×, and it uses |V| ≥ 1 rather than the parity lemma's |V| ≥ 2, so it
does not depend on a, b's parity. Asymptotically, τ_V² < 2 gives M/√D > 2√2 and
u > 5 + 2√6 = 9.899; with |V| ≥ 2 it is the familiar 33.97.)*

**Measured, and the contrast is exactly the theorem.** At every dyadic modulus
window from [8,16) to [2^23, 2^24) at X = 3000 and 6000:

| cofactors | max Gram entry |
|---|---|
| both in one dyadic band | **1** |
| free | **2** |

**O.12 is not knife-edge, which matters if "range" is read loosely.** The proved
threshold is 4.7913 using only |V| ≥ 1; with |V| ≥ 2 — which the parity lemma
gives whenever M is odd — it rises to **13.9282** at X₁ = 1 and **33.9706**
asymptotically. And empirically nothing happens far above even that: the
**minimum n₂/n₁ observed is 34.0811**, at (37, 1261) with moduli 866 and 1730 —
**7.11× the |V| ≥ 1 bound**, and only **0.33% above** the 33.9706 that |V| ≥ 2
gives asymptotically. **That 0.33% carries a condition, stated in full in
O.13 some 1400 lines below and repeated here because this is where a reader
meets the number first: it is sharpness against the |V| ≥ 2 threshold, and
|V| ≥ 2 binds because every realised extremum measured is a τ₁ step — measured
absence over a finite range, not a theorem.** **⚠ This line previously recorded 43.79 at (34, 1489),
moduli 1073 and 1973, "9.1×". That pair is genuine but is not the minimum, and
the reason it looked like one is the anchored-window defect**: 866 and 1730 have
ratio 1.9977 so they lie in one dyadic window, but a sweep stepping
M = 2, 4, 8, … puts 866 in [512, 1024) and 1730 in [1024, 2048) and never
compares them, while 1073 and 1973 both sit inside [1024, 2048) and are found.
**Third recorded instance of that defect** (after `exp09` and the line-family
c = 6 sweep), and the first to corrupt a number rather than a coverage
statement. So the theorem covers any reasonable reading of "both variables
in ranges", not just the dyadic one, and a range as wide as a factor 4.79 is
already inside it unconditionally.

**And the sweep carries its own positive control**, which is the check that
distinguishes a real result from a vacuous one. At X = 3000 over 300,026 banded
cofactor pairs: **57,132 share exactly one modulus, 0 share two or more** — while
**127 *free* pairs share two**. So the forbidden configuration genuinely occurs
the moment the banding is dropped, and the banded population is large enough to
have shown it. *(A "max of 1" over pairs that share nothing would look
identical and mean nothing.)*

**Why this matters outside Note O.** `gaussian-to-rational-bridge` is `inferred`,
and its stated gap is: *"What is proved over Z[i] is G ≤ 1; what is measured over
Z is G′ ≤ 2 on every dyadic window for X ≤ 8000."* O.12 closes that sentence's
second half — over Z, on the configuration (II) quantifies over, **G′ ≤ 1 is
proved, for all X, and it matches the Z[i] bound exactly** rather than being a
measured constant one larger.

**And it caps Ford–Maynard's footnote-2 quantity.** `fm-barrier-range-is-small-moduli`
records mean G = 2.000, 1.333, 0.810, 0.577 over N = 8, 16, 32, 64 at X = 12000
and concludes the mean is ≥ 1 for ε ≲ 0.18. Those are the **moduli-unrestricted**
figures — reproduced exactly here. But (II) bands n as well as m, so the
footnote's quantity is doubly dyadic, and there O.12 forces max G ≤ 1:

| N band | #cofactors | mean G, moduli free | max | mean G, doubly banded | max |
|---|---:|---:|---:|---:|---:|
| [8,16) | 2 | 2.0000 | 2 | **1.0000** | 1 |
| [16,32) | 4 | 1.3333 | 3 | **0.6667** | 1 |
| [32,64) | 7 | 0.8095 | 2 | **0.4762** | 1 |
| [64,128) | 13 | 0.5769 | 2 | **0.4103** | 1 |
| [128,256) | 24 | 0.3152 | 2 | **0.2319** | 1 |

> **On the configuration (II) quantifies over the mean never exceeds 1**, and the
> only band reaching 1 contains **two cofactors, i.e. a single pair** — which is
> the informative-subset caveat that claim already carries, now binding on the
> one value that mattered.

> ### ⚠ The "mean ≥ 1" line is this repo's paraphrase, not Ford–Maynard's
>
> Checked at source (arXiv:2407.14368v1, footnote 2, p. 7): the footnote asks for
> **"an error term better than O(1)"** on #{n : nm₁, nm₂ ∈ J}, averaged over
> m₁, m₂ ∼ x^{1−2c+ε}. It says nothing about a mean exceeding one. So the table
> above is evidence about *how often the count is 1*, **not** about a threshold
> being crossed, and it should not be read as defeating the barrier.
>
> **And the real requirement makes the result stronger, not weaker.** Note F has
> had the correct reading since it was written: the count is 0 or 1, so the error
> term **is** O(1) and no averaging can improve it. That is pointwise, and it is
> immune to the objection that would sink a mean argument ("your band holds two
> cofactors"). **Theorem O.12 is that statement, now proved over Z**: on the
> doubly-dyadic configuration the footnote's counting function is a **0/1
> indicator**, over Z as well as over Z[i] — and "better than O(1)" for a 0/1
> integer means knowing it exactly.
>
> *(Found by asking whether the number in our claim is the number in their paper —
> the same "why do these two agree" question that caught the Plücker constant,
> aimed at a citation rather than a derivation. Paraphrases drift in the direction
> that makes the local argument work.)*

**Positive control: the 0/1 property is not generic.** Running the same
doubly-dyadic sweep at Q = 10⁵ on four comparison sequences:

| sequence | status | max Gram, banded | banded pairs with ≥ 2 |
|---|---|---:|---:|
| **x² + 1** | open | **1** (proved) | **0** |
| a² + b⁶ | not known captured | 11 | 1,752 |
| x³ + 2y³ | **captured** (Heath–Brown) | 15 | 511 |
| a² + b⁴ | **captured** (Friedlander–Iwaniec) | 66 | 33,411 |
| a² + (b²+1)² | **captured** (Merikoski) | 67 | 27,890 |

x²+1 sits alone at 1 while everything else is ≥ 11, and for x²+1 the value is a
theorem rather than a measurement. **This explains the footnote's own hedge**: for
a sequence whose count ranges over 0…66 there is something to average and an
error term better than O(1) is a meaningful ask; for a 0/1 indicator there is
nothing to average.

> **⚠ It is NOT a classifier, and the ordering is not even stable.** Across
> Q = 2.5×10⁴, 5×10⁴, 10⁵ the two smallest entries **swap**: a²+b⁶ (not known
> captured) reads 6, 7, 11 against x³+2y³ (captured) at 5, 9, 15 — above at the
> first size, below at the other two. A statistic whose ordering moves with Q
> cannot separate captured from open, and reading this table as "low ⟹ hard"
> would be the mean-G classifier again. **x³+2y³ is here precisely because it is
> what killed that classifier, and it was run before any of this was written.**
>
> **What is claimed is only this**: x²+1 reads **exactly 1 at every Q**, where
> the value is a theorem; every other sequence reads ≥ 5 and **grows with Q**. So
> the property is not generic and x²+1 is qualitatively alone in having it — a
> difference in kind, not a position in an ordering.

**O.12's *argument* is special to c = 1; the *fact* is not known to be.** Along
the line family x² + c², the parallel session derived that the identity carries a
factor c²:

> V·W = (am_i − c²)(bm_j − c²) − (am_j − c²)(bm_i − c²) = **c²·M·(m_i − m_j)**,

and Y > X√(b/a) still holds exactly when b > a. So the bound becomes
|V| < c²·(M/2√D)(R − 1/R) — a factor **c² weaker** — and O.12's threshold scales
as **1/c²**, falling below what a dyadic band supplies as soon as c ≥ 2. **The
prediction is that O.12 fails for c ≥ 2. It does not**: banded cofactors still
share at most one in-window modulus at c = 2 and c = 3, over 530,973 and 617,940
banded pairs.

*(Verified independently here: the identity holds with 0 failures over 1089,
1582, 2406 pairs at c = 1, 2, 3.)*

**Where the argument stops, exactly.** O.12 uses only |V| ≥ 1. Upgrading that to
**|V| ≥ 2** raises the threshold to M/√D > 2√3/c², against the 1/√2 = 0.7071 a
dyadic band supplies:

| c | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| threshold, \|V\| ≥ 1 | 1.7321 | 0.4330 | 0.1925 | 0.1083 | 0.0693 |
| threshold, \|V\| ≥ 2 | 3.4641 | **0.8660** | 0.3849 | 0.2165 | 0.1386 |

So **|V| ≥ 2 extends O.12 to c = 2 and no further** — 0.8660 clears 0.7071, and
c = 3 does not. And **every |V| observed is even**, at every c from 1 to 5
(smallest values 2,4,…; 4,6,…; 6,8,…; 4,8,…; 6,10,…), so |V| ≥ 2 looks
structural — but `V-is-even-whenever-M-is-odd` is proved for c = 1 only, and the
general-c parity argument is not done here. **The honest boundary: O.12 covers
c = 1 outright and c = 2 modulo that parity lemma; c ≥ 3 is measured only.**

> **Three repairs, all closed.** (i) The bound is **saturated** — max |V| over it
> is 1.0000, 3.9999, 8.9998 at c = 1, 2, 3, exactly c² — so it cannot be
> tightened. (ii) min |V| is **2, 4, 6, 4, 6** at c = 1…5, i.e. not c², so no
> lower bound of that shape restores the threshold. (iii) The crude step
> Y > X√(b/a) is lossy and **the loss grows as c²** — exactly,
> (Y/X)²/(b/a) − 1 = **ε = c²M/(abm)**, with max ε = 1.0000, 4.0000, 8.9999,
> 15.9997 at c = 1…4 — which looks as though c²/(1+ε) < 1 would restore the
> threshold for every c. **It does not: the bound needs the worst case, which is
> min ε**, and ε ∝ 1/m so min ε is 10⁻⁹–10⁻⁸ and c²/(1+min ε) = c² to four
> places. *(That is the informative-subset error in a third costume — max where
> min was needed — on the same claim within an hour.)*
>
> Anyone generalising O.12 along the line family should know those are the three
> doors and all are shut.

**And that turns the line family into a test bed for the bridge.** Over Z[i],
`kappa-counts-lines-and-c4-freeness-permits-one` proves A_c is C₄-free for
**every** c, by Note F's argument with c in place of 1. Over Z, O.12 proves the
doubly-dyadic G′ ≤ 1 **only at c = 1**. So c ≥ 2 is exactly the situation the
bridge describes — Z[i] side proved, Z side not — and it can be checked:

| c | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| banded max Gram | 1 | 1 | 1 | 1 | 1 |
| free max Gram | 2 | 2 | 2 | 2 | 2 |
| banded pairs | 158,708 | 496,495 | 392,970 | 648,160 | 146,128 |
| banded pairs sharing ≥ 2 | 0 | 0 | 0 | 0 | 0 |

> ### ⚠ CORRECTED — the family **bounds** the transfer, it does not support it
>
> This table stopped at c = 5 and read as four supporting instances. **Extend the
> axis by one and it fails**: at **c = 6**, cofactors **(5, 8)** — ratio 1.6 — share
> moduli **9 and 17** — ratio 1.889 — both doubly dyadic, since 5·9 = 3²+6²,
> 8·9 = 6²+6², 5·17 = 7²+6², 8·17 = 10²+6². Over c ≤ 8 the property **holds at
> 1, 2, 3, 4, 5, 7 and fails at 6 and 8**.
>
> **The mechanism is the Z[i]→Z coarsening in its purest form**:
> (3+6i)(10+6i) = **−6+78i** and (6+6i)(7+6i) = **6+78i** are **conjugate, not
> associate** — so A₆ *is* C₄-free over Z[i], as the line argument requires, while
> the norms agree at 6120 and the rational 4-cycle is real.
>
> **And my sweep would have missed it even at c = 6.** It tested windows
> **anchored at powers of two**, which is strictly weaker than "any dyadic
> window": [8,16) and [16,32) between them miss the pair (9,17). Corrected to test
> by **ratio** on both axes. *An anchored sweep would have passed on a
> counterexample, and did.*
>
> **It does not refute the bridge for x²+1**, where the Z side is *proved* by O.12
> rather than transferred. What it removes is any reading of the c-family as
> evidence that the transfer is reliable.

**And there is a mechanism underneath, on the next axis out — D itself.** In
x² + D, four consecutive arguments k…k+3 give a 4-cycle exactly when

> (k²+D)((k+3)²+D) − ((k+1)²+D)((k+2)²+D) = **4(D − k² − 3k − 1)**

*(identity verified symbolically)* — because k(k+3) and (k+1)(k+2) differ by 2
while the D-linear parts differ by 4. So the cycle exists precisely for
**D = k² + 3k + 1**: D = 1, 5, 11, 19, 29, 41, 55, …

| k | D | the four values | product | cofactors | moduli | |
|---|---|---|---|---|---|---|
| 0 | **1** | 1, 2, 5, 10 | 10 | {1, 5} | {1, 2} | **the unit, twice** |
| 1 | 5 | 6, 9, 14, 21 | 126 | {3, 7} — ratio 2.33 | {2, 3} | one ratio ≥ 2 |
| 2 | 11 | 15, 20, 27, 36 | 540 | {3, 4} | {5, 9} | **genuine** |
| 3 | 19 | 28, 35, 44, 55 | 1540 | — | — | genuine |
| 4 | 29 | 45, 54, 65, 78 | 3510 | — | — | genuine |

> **x²+1 IS the k = 0 member.** It does not avoid the family — its instance is
> **degenerate**, because one of the four values is 0²+1 = **1**, the unit modulus
> that no Type II hypothesis admits and that this repo excludes everywhere else
> for exactly that reason. D = 5 escapes for a *second and unrelated* reason,
> which is why the first genuine counterexample is D = 11 and not D = 5. Both
> ratios fall toward 1 as k grows, so the later members are not marginal cases
> scraping under the threshold — they are deeply doubly dyadic, and there are
> infinitely many.

### The one mechanism underneath all of it: the invariant is M·D, not M

Every D-coincidence recorded above is one statement. From a·m = X² + D and
b·m = Y² + D we get b(X²+D) = abm = a(Y²+D), hence

> **aY² − bX² = (b − a)·D = M·D.**

*(0 failures over 2268 solutions across D = 1, 2, 5, 11, 29, 39, 52 here, and
over 5354 pairs in the parallel session — together with **V·W = D·M·(m_i − m_j)**,
the pair identity with D in place of the c² found earlier along the line family.)*

> ### ⚠ WHICH FORMULAS IN THIS NOTE CARRY THE D — read before reusing any of them
>
> The invariant is stated once, here, and used **implicitly** everywhere else, so
> every formula elsewhere in this note looks like its D = 1 form. **Three separate
> errors in about one hour came from reading one of them as general**, across both
> sessions, each after having read this section:
>
> | formula, as written elsewhere | D = 1 form of | correct for general D |
> |---|---|---|
> | aY² − bX² = M | the conic | **M·D** |
> | U² − DV² = M² | the multiplier | U² − abV² = **(M·D)²** |
> | window premise τ_V² < 3 at X₁ = 1 | R² < 2 + 1/X₁² | τ_V² < **2 + D** |
> | τ₁ = (√b+√a)/(√b−√a) | the fundamental multiplier | **not** τ₁ for D ≠ 1 |
> | V = 1 ⟺ a² − ab + b² square | U² = M² + ab | U² = **(M·D)² + ab** |
> | reach D ≤ V√6 (all X) | from τ_V² < 3 | **D·g(D) ≤ 2√2·V**, g = √(2+D) − 1/√(2+D) |
>
> The **asymptotic** statements (τ_V² < 2, reach D ≤ 4V) are the exception: both
> window forms tend to 2 as X₁ grows, so those transfer unchanged.
>
> **Worked example — one pair, three roles, three formulas, one of them right.**
> The cofactor pair **(25, 481)** appeared three times in one night:
>
> 1. as a *"non-τ₁ converse"* at D = 4, because a² − ab + b² = 219961 = 469² —
>    which is the **D = 1** test for V = 1. **Withdrawn.** The correct test is
>    whether (M·D)² + ab is square, and 3339001 is not.
> 2. as an inhabitant of O.13′'s exceptional branch — correct, because there the
>    ambient D **is** 1 and the Eisenstein condition is the right one.
> 3. as D = 4's extremal pair in O.13‴, minimal V = 4, threshold 9.5150 against a
>    realised 19.2400 — correct, because every formula was taken in its M·D form.
>
> Same pair, same arithmetic, three readings; only the one that carried the D is
> right. If a formula here is being applied at D ≠ 1, find it in the table above
> before using it.
>
> **The failure mode is not carelessness.** Each of the three was found by
> checking a derivation against *this* section, never by a test failing and never
> by re-reading the formula itself — because the D = 1 form is what the
> surrounding text looks like, and a correct-looking formula surrounded by
> correct-looking formulas raises nothing.

**So the quantity Note O calls M is really M·D**, and every bound built on it
weakens by a factor of D. O.9 becomes **3ab < (M·D)^{4/3}**, and that separates
the cases exactly. At the cofactor pair (5, 8), where M = 3:

| D | 3ab | (M·D)^{4/3} | |
|---|---:|---:|---|
| 39 | 120 | **572.24** | permitted — **and the triple occurs** |
| 1 | 120 | **4.33** | forbidden — and none occurs |

**Same bound, same cofactors. D is the whole difference.**

It subsumes every coincidence on this axis: the line-family break at **c = 6**
(there D = c², and the |V| bound weakens by exactly c² — measured before the
reason was known); the 4-cycle family **D = k² + 3k + 1**; and the seven
unit-free triples at D ≤ 60. **And the density confirms the mechanism rather than
merely agreeing with it**: over D ≤ 160 at X = 900, **51 of 160 (31.9%) admit a
unit-free triple, none with D ≤ 25**, and D = 1 does not. A bound loosening like
D^{4/3} predicts exactly that shape — nothing until D is large enough, then a
positive density. A sporadic set would look completely different.

> **So the honest headline is better than "x²+1 is special".** It is the **D = 1
> end of a one-parameter family — the point at which every bound in this
> apparatus is at its tightest** — which is why the Note O conclusions hold there
> and essentially nowhere else. The twelve theorems are not weakened by this.
> They are **located**.

**The right axis is the discriminant, which unifies all of these.** Completing the
square gives **4(x² + bx + c) = (2x+b)² + |Δ|** with Δ = b² − 4c, so a general
quadratic is x² + D on the arguments of one parity, up to a factor 4. The
property is therefore a function of **Δ alone**, and it is — checked at X = 900
over 0 ≤ b ≤ 3, 1 ≤ c ≤ 7, every discriminant class agreeing internally:

| Δ | −3 | −4 | −7 | −8 | −11 | −12 | −15 | −19 |
|---|---|---|---|---|---|---|---|---|
| polynomials | x²+x+1, x²+3x+3 | **x²+1**, x²+2x+2 | x²+x+2, x²+3x+4 | x²+2, x²+2x+3 | x²+x+3, x²+3x+5 | x²+3, x²+2x+4 | x²+x+4, x²+3x+6 | x²+x+5, x²+3x+7 |
| banded max | 1 | **1** | 1 | 1 | **2** | 1 | 1 | **2** |

*(x²+2x+1 = (x+1)² has Δ = 0 and reads 66 — a perfect square is degenerate and
not a member of the family.)*

So the line family x² + c² (Δ = −4c²), the D family x² + D (Δ = −4D) and the
general quadratics are **one axis indexed by Δ**, and x²+1 is Δ = −4. At X = 1500
the property *appears to hold* for D = 1…10, 12, 13, 15, 16, 17, 18, 20, 22, 25,
28, 30, 33, 35 and fails for D = 11, 14, 19, 21, 23, 24, 26, 27, 29, 31, 32, 34, 36, …
— **the consecutive-argument family k²+3k+1 is a proper subset of the failures**,
so it is one mechanism among several.

> **⚠ "Survives at X" is not evidence of surviving, and D = 35 demonstrates it.**
> D = 35 holds at X = 1500 and **fails at X = 2500**, with cofactors
> **(2249, 3756)** — ratio 1.6701 — sharing moduli **459 and 879** — ratio 1.9150:
> 2249·459 = 1016²+35, 3756·459 = 1313²+35, 2249·879 = 1406²+35,
> 3756·879 = 1817²+35. A genuine banded doubly-dyadic 4-cycle that a sweep to
> 1500 cannot see. **So every entry in the holding list is a survivor of a finite
> sweep and nothing more — D = 1 is the only value proved to hold, by O.12.**
>
> *And it also refutes a pattern I drew from the same data.* Searching cofactors
> ≤ 300 finds every failure witness below cofactor 9 — D = 11 at (3,4), D = 14 at
> (3,5), D = 19 at (4,5), D = 39 at (5,8) — from which I concluded that failures
> announce themselves at tiny cofactors and a small-cofactor search is an
> effective detector. **D = 35's witness is at (2249, 3756)**, three orders of
> magnitude above that bound. The tiny-cofactor pattern is a property of the D
> values that happened to be found, not of failure, and the bounded search could
> not have seen the case refuting it.

**And M·D gives O.12's exact reach on this axis.** The pair condition
τ(V)² < 3 becomes V·s < 1/√3 with s = √(ab)/(M·D) = √u/((u−1)D), i.e.

> **(u − 1)·D/√u > V·√3**,

while a dyadic band supplies only (u−1)/√u < 1/√2. So O.12 covers D exactly when
**D ≤ V·√6**:

| input | bound | covers |
|---|---|---|
| \|V\| ≥ 1 (unconditional) | D·g(D) ≤ 2√2 | **D = 1** |
| \|V\| ≥ 2 (the parity lemma) | D·g(D) ≤ 4√2 | **D = 1, 2, 3** |

*with g(D) = √(2+D) − 1/√(2+D). **⚠ These rows previously read D ≤ √6 (D ≤ 2)
and D ≤ 2√6 (D ≤ 4), from the premise τ_V² < 3.** That premise is the D = 1
case: the window condition is m_j/m_i = (X_j²+D)/(X_i²+D) < 2, so at X₁ = 1 it
is **τ_V² < 2 + D**, not 3. Sanity check on the correction — under the
asymptotic premise c = 2 the same formula gives g = 1/√2 and D ≤ 4V exactly,
which is the row below. **D = 2 survives empirically at every X either session
has run; what it loses is its proof at X₁ = 1.***

**So O.12 proves the same statement for x²+2 asymptotically, and for x²+1 at
every X.** ⚠ *The unconditional-at-X₁ = 1 claim for x²+2 is withdrawn: it rested
on τ_V² < 3, which is the D = 1 premise.* And
stops there unconditionally. *(Thresholds: u must exceed 4.7913 at D = 1 and
2.3187 at D = 2, both above the 2 a band supplies; at D = 3 it is 1.7676, below
it, and the argument fails.)*

**There are two forms of the reach, and they answer different questions.** The
window condition is R² < 2 + 1/X₁², so:

| | condition | \|V\| ≥ 1 | \|V\| ≥ 2 |
|---|---|---|---|
| **all X** (X₁ ≥ 1) | τ_V² < **2 + D** | D·g(D) ≤ 2√2, i.e. **D = 1** | D·g(D) ≤ 4√2, i.e. **D ≤ 3** |
| **asymptotic** (X₁ → ∞) | τ_V² < 2 | D ≤ 4V, i.e. **D ≤ 4** | D ≤ 4V, i.e. **D ≤ 8** |

The asymptotic row is the M·D invariant applied to the threshold family: the
condition M/√(ab) > 2√2·V becomes **(u−1)/√u > 2√2·V/D** — *the threshold divided
by D* — and a band supplies (u−1)/√u < 1/√2, so a banded pair needs **D > 4V**.

> ### ⚠ The boundary is decided by an identity, not by a float comparison
>
> At D = 4V the requirement is *exactly* 1/√2 and u₀ is *exactly* 2 — sympy
> returns {1/2, 2} for (u−1)²/u = 1/2. But **two algebraically identical
> expressions disagree there in floating point**, on the wrong side of a strict
> test:
>
> | route | value | `u₀ < 2` ? |
> |---|---|---|
> | v = (t + √(t²+4))/2, u = v² | **1.9999999999999996** | **True** — reports D = 8 *uncovered* |
> | u = (2 + t² + t√(t²+4))/2 | **2.0** | False — correct |
>
> The trap is not "floats are inexact" — it is that **equivalent expressions
> diverge exactly where the comparison is strict**, so the number looks right, the
> comparison looks right, and the answer is off by one value of D. *(I reached the
> correct endpoint only because I happened to use the second expression; I did not
> reason about it. The parallel session used the first and read its output.)*
> **Decide such boundaries symbolically.**
>
> **D = 4V is COVERED, not the crossover.** A band gives u < 2 **strictly**, so
> (u−1)/√u approaches 1/√2 without attaining it; at D = 4V the requirement is
> exactly 1/√2 and no banded u reaches it. The first *uncovered* values are
> **D = 5** at |V| ≥ 1 and **D = 9** at |V| ≥ 2. *(At D = 9, u = 1.9 gives 0.6529
> against a threshold of 0.6285 — permitted.)*

**And this explains measurements neither form could explain alone.** **D = 5, 6,
7, 8** are *asymptotically* protected but **not** protected at small X₁ — which
is exactly why they hold to X = 8000 without being proved, since a failure there
would have to come from X₁ small. **D = 9, 10** are permitted by *both* forms and
still unfallen: the necessary-not-sufficient gap, now with an exact left
endpoint. **D = 11** is the first observed failure, at u₀ = 1.6632, well inside a
band.

**It also turns the x²+39 banded triple from a discovery into a prediction.** At
D = 39 a banded pair needs only u > 1.1559, and the witness (5, 8) has u = 1.6
with (u−1)/√u = 0.4743 against a threshold of 0.1450. **Banded pairs become
possible from D = 9 on**, so the triple was not an accident of search.

**|V| is even on this axis too**, so the second row is available: over D = 1…6,
minimum |V| is 2, 4, 6, 4, 2, 4 and **no odd value occurs in 1,238 pairs**. Since
V ≠ 0, evenness gives |V| ≥ 2 directly. *(`V-is-even-whenever-M-is-odd` is proved
for D = 1; the general-D statement is observed here, not proved.)*

> **So O.12 covers D = 1, 2 unconditionally and D = 3, 4 given evenness — and
> x²+2 in particular can never fail.**
>
> **And the two sides are consistent with nothing to spare.** Every failure
> observed on this axis — D = 11, 14, 19, 20, 21, 23, 24, 26, 27, 29, 31, 32, 34,
> 35, 36, 37, 38, 39, 40 — lies **outside** the reach, and **no D inside it has
> ever failed**. The smallest observed failure is **11**, against a boundary of
> 4.899. What is unexplained is the strip **D = 5…10** (plus scattered larger
> survivors): outside the proof, not yet fallen. **D = 5 sits 0.101 past the boundary.**
>
> ### ⚠ CORRECTED — "so D = 5 should fall first" inverts the mechanism
>
> A first version of this passage predicted that D = 5, being the smallest
> unprotected value, would be the first survivor to fall. **That is backwards**:
> a larger D gives a **looser** bound, so if looseness drove the timing D = 10
> would fall *before* D = 5. And the timing is not monotone in D at all — it is
> arithmetic, governed by whether a witness exists at accessible cofactors:
>
> | D | first falls at | cofactors |
> |---|---|---|
> | 11, 14, 19 | X ≤ 1200 | below 6 |
> | 35 | X = 2500 | (2249, 3756) |
> | 20 | X = 4000 | (47, 63) |
> | 5–10 | **not by X = 8000** (all six, verified) | — |
>
> **D = 11 falls far earlier than D = 20 despite having the tighter bound**,
> because 11 and 19 lie in the k²+3k+1 family, which hands over a witness at four
> *consecutive* arguments. The tiny-cofactor witnesses are **the family's, not
> failure's** — which is the same phenomenon that produced the retracted caution
> above, seen a second time.
>
> **So the honest answer is neither.** The argument's boundary (D ≤ 4) is *not*
> the empirical boundary — that is at least 10 — but it is *not* an artefact of
> the technique either: it is the only **proved** boundary, and 5…10 is
> **unfallen rather than protected**. That gap is the same
> necessary-but-not-sufficient gap as the 39 of 60 admissible classes that hold no
> triple, one level down: the bound permits failure and no failure is found. That bears directly on the conjecture that
> D = 1 is the unique survivor: at small D the bound is not merely tight but
> **unsatisfiable**, so no number of candidate classes at larger X can produce a
> configuration. The attrition argument reaches D > 3 on the all-X
> reading (D > 4 asymptotically), not D > 1.

**And this reconciles exactly with the line-family analysis above.** There D = c²,
so |V| ≥ 2 covering D ≤ 3 admits only c = 1, while the asymptotic D ≤ 8 gives
c ≤ 2 — the earlier finding that |V| ≥ 2 extends O.12 to c = 2 and no further is
therefore the **asymptotic** statement, not the all-X one. Two routes to the same boundary, computed
independently before the M·D invariant was known.

**And the same axis refutes the O.2 analogue outright, at D = 39.**

> **cofactors (5, 8)** — ratio 1.6, one dyadic **band**
> **moduli 8, 11, 15** — all in [8,16), one dyadic **window**
>
> 5·8 = 40 = 1²+39  8·8 = 64 = 5²+39
> 5·11 = 55 = 4²+39  8·11 = 88 = 7²+39
> 5·15 = 75 = 6²+39  8·15 = 120 = 9²+39

*(All six verified independently.)* **Three shared moduli in one window with both
cofactors inside one band** — so for D = 39 the analogue of Conjecture **O.2**
*and* the analogue of Theorem **O.12** are both false, in a single configuration,
with cofactors as small as 5 and 8. Over D ≤ 60 there are **seven** unit-free
triples — D = 29, 39, 42, 44, 52, 53, 59 — and **D = 1 is not among them**.

> **The unit-free restriction is what makes that mean anything**: 35 of 60 admit a
> triple if the unit cofactor is allowed, and the unit is exactly what no Type II
> hypothesis admits — the same distinction that improved the free-cofactor witness
> above.

**None of this weakens O.2 or O.12 for x²+1.** O.12 is proved; O.2 has no
counterexample to X = 8000, with the two-step floor unmoved at exactly 13.0000
across five sizes and 110 informative classes. What it removes is the reading of
either as an instance of something general — **twelve theorems establish a fact
about x²+1, not about degree-2 sequences**, and that is now demonstrated rather
than assumed. At the 4-cycle level x²+1 is the *degenerate member of a failing
family*; at the triple level it is simply *not in the failing set*.

**This does not touch O.12, which is about x²+1.** What it removes is any reading
of O.12 as an instance of something general: **its conclusion fails for an
explicit infinite family of degree-2 sequences**, and x²+1's escape has a *cause*
rather than being a brute fact. Three results now bound it from three sides — the
genericity control shows the property failing off the line family, c = 6 shows it
failing within the line family, and this shows **why the survivor survives**.

**And it is the same methodological error twice.** c = 6 came from extending an
axis neither session extended; D = 11 came from extending the next one. Both
times the property had been checked at five or six values and read as general.
**"What would the sweep look like if the finding were absent" applies to the axis
as much as to the population**: a sweep stopping at c = 5, or D = 10, looks
identical whether the property is universal or holds on a short initial segment.

> **What that is and is not.** It is evidence for the **transfer** — "C₄-free
> over Z[i] ⟹ G′ ≤ 1 over Z on the banded configuration" — at cases it was not
> built on. It is **not** evidence for the bridge's other half, the inference from
> *no main term either way* to *ν = 0 in Ford–Maynard's sense*, which is about
> what their (II) quantifies over and is untouched by any amount of c.

**This is the complement of the genericity control above, from the inside.** That
control shows the 0/1 property failing badly *off* the line family — ≥ 11 for
a²+b⁴ and the rest. This shows the *proof* failing *within* it while the property
survives. Together: **the property is not generic, the proof is not general, and
x²+1 is the only place both hold.** A sweep alone would have shown max Gram 1 for
every c and read as "O.12 generalises" — which is exactly what is not
established, and the distinction is invisible without the derivation.

> **What it does not close.** The bridge's remaining content is the *inference*
> "both give no main term, so the conclusion is unchanged". That step is
> untouched; O.12 removes the quantitative discrepancy and the finite floor, not
> the reasoning. And it says nothing about O.2, which is the free-cofactor
> question. The cleanest witness is **cofactors (2, 82) sharing moduli 365 and
> 685** — ratio 1.877, one window — since 2·365 = 27²+1, 82·365 = 173²+1,
> 2·685 = 37²+1, 82·685 = 237²+1. **No unit anywhere**, and its cofactor ratio of
> 41 sits far above O.12's 4.7913, so it is *consistent with* the theorem. *(The
> same 4-cycle is usually written (1, 41) with moduli 730 and 1370, which a reader
> can dismiss in a line since no Type II hypothesis admits the unit cofactor;
> unit-allowed and unit-excluded maxima are both 2 at X = 2000 and 4000, so the
> unit was never doing the work.)* It is a genuine G′ = 2 and
> is simply not a Type II configuration.

**What was M even and M non-squarefree** is now covered; the sign argument's
apparent need for them was an artefact of working at e = 1: U² ≡ (Va)² only gives M | A_VB_V in general, and the signs can differ
across the prime factorisation of M — which is exactly the 2-adic gap O.3 already
had. **M odd prime is 54 of the 379 realised close pairs (14%)**, so this is a
real slice rather than a corner, and the surviving case is the composite one.

**And the candidate criterion in the withdrawn section was the wrong shape**,
which matters only for reading that section's numbers. For three moduli
m, r₁m, r_km all inside [m, 2m) the requirement is **r_k < 2** alone; the product
r₁·r_k is not the window condition. The 95 were selected with r₁·r_k < 2, which
since r₁ > 1 is *stricter* — a conservative subset, so nothing built on it was
inflated, but the criterion as stated does not mean what it says.

**The parity hypothesis is redundant, and that is not good news.** Since a and b
are admissible and coprime, either both are ≡ 1 (mod 4) — forcing **4 | M** — or
one is ≡ 2 (mod 4), forcing **M odd**. So **M ≡ 2 (mod 4) never occurs**
(verified: 0 of 59,811 admissible coprime pairs). Hence "M squarefree" already
implies "M odd", O.3's hypothesis simplifies to squarefreeness alone — and
dropping "odd" gains nothing, because the family O.3 misses is exactly
**4 | M**, i.e. a and b both odd, which for a = 1 is every odd b. Reaching it
needs a **2-adic** argument, not a parity one.

**But the gap is exactly one step, not the whole proof.** The condition is
2M | A_kS + B_kT. τ₁ gives M | 2S; for M *odd* that is M | S, whence M | B_kT
and gcd(T,M) = 1 gives M | B_k. For M *even*, M | 2S only gives S ≡ 0 (mod M/2)
and the reduction stalls. Everything after M | 2B_k — that j ≥ 3, that
M = 8ka(2k−j)/(j²−4), and that e² + 4jwe + 2w²(2e−1) > 0 — is **parity-free
algebra**. Extending O.3 to even M is a single lemma, not a new argument, and
the disjointness table below was computed with no parity restriction at all.

**The two requirements pull opposite ways**: the divisibility forces M *small*
relative to a, and the geometry forces M *large* relative to √(ab). Machine
check of the disjointness, over admissible (a,b) with a ≤ 400:

| | count |
|---|---|
| configurations satisfying the divisibility M \| 2B_k | 199 |
| …of those, also satisfying r₁r_k < 2 | **0** |
| configurations satisfying r₁r_k < 2 (the 95 candidates) | 95 |
| …of those, also satisfying the divisibility | **0** |

The two sets are disjoint, from both directions. The nearest miss is
a = 1, b = 481, k = 20, j = 4, where the divisibility holds and r₁r_k = 18.36
against the 2 it needs.

*Scope, precisely.* This rules out triples of the shape (ξ, τ₁ξ, τ_kξ) for the
smallest available k, over 44 complete orbits. It does not rule out triples built
from other multiplier combinations, and it does not cover classes whose least
solution exceeds the search. **It is not a proof of O.2.** A triple's two multipliers need not include τ₁:
the general shape is (ξ, τ_pξ, τ_qξ) with p, q ≥ 1, whose compatibility
determinant is A_pB_q − A_qB_p = 4a(pU_q − qU_p), and Theorem O.3 handles only
p = 1. It also assumes M squarefree and odd, which holds for 17 of the 95
candidates. **What is proved is a theorem about the natural case, not the
general one** — and after two retractions today the difference is worth
labouring.

### The general case, measured but not proved

For M odd squarefree, put M₁ = gcd(S, M) and M₂ = M/M₁; the conic forces
M₂ | T, and each condition splits as **M₁ | B_k and M₂ | A_k**. This also
explains why τ₁ is special: B₁ = U₁ − 2a = a+b−2a = **M exactly** and
A₁ = M + 4a, so M₂ | M and M₂ | M+4a force M₂ | 4a, and with M odd coprime to a
that gives **M₂ = 1**. τ₁ acting *is* the statement M | S — the same fact as
j = 2 ⟺ k = 1, seen from the other side.

For p, q ≥ 2 the factorisation is not forced and Theorem O.3 does not apply.
Measured over admissible (a,b) with a < 120, b < 300000:

| | count |
|---|---|
| (p,q) pairs with two multipliers, both k ≥ 2 | 274 |
| …of which the larger still fits a window (r_q < 2) | **0** |

The geometry alone kills them, and with a wide margin. Since r_q < 2 requires
q < √(b/a)/(4√2), the test is the ratio q/(√(b/a)/4√2), which must be below 1:

> **minimum observed 3.91**, over 171 pairs.

So a second multiplier at k ≥ 2 forces k up faster than √(b/a) grows, and the
smallest available one is never small enough. That is the same tension
Theorem O.3 proves for p = 1 — divisibility wanting M small, geometry wanting it
large — showing up as a factor of four rather than as a contradiction. **It is a
measurement, not a proof, and the general case of O.2 is open.**

### Where a proof of the general case would live

The multiplier equation U_k² − D(2k)² = M² says multipliers **are** solutions of
U² − DV² = M² with V even. Within one class the automorph sends
(U,V) → (tU + DuV, tV + uU), so V is multiplied by roughly ε ≥ √D at each step.
Checked:

| (a,b) | the k ≥ 2 multiplier's V | next V in the trivial class |
|---|---|---|
| (1, 1105) | 28 | 57,250,510,370 |
| (1, 2465) | 36 | 120,924,595,842 |
| (1, 5986) | 54 | 15,354,174,254 |

The class of the trivial solution (a+b, 2) jumps straight past every small V. So

> **every k ≥ 2 multiplier is the fundamental solution of its own class**,

and the general case of O.2 reduces to a bound on how small the fundamental
solutions of U² − DV² = M² can be.

**And that is the wrong way round from the standard theory, which is worth
saying plainly because the first version of this paragraph got it backwards.**
Nagell's bound is an *upper* bound: a class representative can be normalised to
√N ≤ ξ ≤ √(Nε₁), whence with N = M²

> V = (ξ − N/ξ)/(2√D) ≤ M(√ε₁ − 1/√ε₁)/(2√D).

That says a fundamental solution's V cannot be *large*. The general case of O.2
needs the opposite — that V cannot be *small* for any class other than the
trivial one — and no such bound is standard, because in general it is false:
distinct classes can have small fundamental solutions, which is exactly what the
k = 12, 33, 91 multipliers are.

So the reduction is real but it does **not** land in a solved area. The honest
statement is that the general case turns on a lower bound for non-trivial
fundamental solutions of U² − DV² = M², that no such bound is available off the
shelf, and that the measured factor of 3.91 is currently the only evidence it
holds at all. Whether that factor is stable or decaying with the box is the
question that decides whether a theorem is there to find, and it is being
measured rather than assumed.

*Caveat, stated because it is the only thing keeping this from being a flat
refutation:* the 110 triples live in wide windows (ratio ≥ 13), not dyadic ones.
Nothing proves the dyadic regime behaves the same way. What the data removes is
any **reason to believe** coprimality holds — it does not establish that it
fails where it would be needed. O.2 is open with no mechanism proposed for it.

The factor a that the corrected norm introduces is absorbed exactly because the
bound on g carries **both** a and b in its denominator. Had N(ξ) been ±M the
same chain would have read g² < M with room to spare; had the bound been
M/√b alone it would have failed. Verified 379/379 at X = 3000.

**No hypothesis on V is used.** An earlier draft of this note derived
P = Q² from |V| = 2 and carried "|V| = 2" and "M odd" as two named gaps. Both
are gone: the argument above runs for arbitrary V and arbitrary parity, with
g = gcd(U,V) absorbing exactly what the |V| = 2 special case made invisible
(g = 1 when M is odd, g = 2 when M is even). The only hypothesis is m_i ≥ 2.

**Two corrections owed to the parallel session**, each of which killed a claim
of mine:

- *The three "exceptional" |V| ∈ {24, 66, 182} are not exceptional.* They are
  the asymptotic |V| ≈ (M/2√D)(√r − 1/√r) working correctly at
  M/√D = 89, 227, 650 against a median of 11.96. |V| is whatever that formula
  gives; it comes out 2 for pairs near the minimal-separation configuration,
  which is merely most of them. So "|V| = 2 with three anomalies" was the wrong
  picture, and a proof resting on it would have rested on nothing.
- *The norm of ξ is aM, not ±M.* Caught while checking the bookkeeping before
  reporting the proposition as unconditional. The conclusion survives, but only
  because a g² < M²/b < M uses M < b; with the wrong norm the final inequality
  was being read off the wrong quantity.
- *|V| ≥ 2 is parity, in two lines.* For a, b both odd: m odd makes am, bm odd,
  so X², Y² are even and X, Y both even; m even makes both odd. Either way
  X_k ≡ Y_k (mod 2), so V = X_i Y_j − X_j Y_i ≡ 0 (mod 2). Verified over 825
  pairs with a, b odd at X = 2000. Not needed above, but it explains g = 2.

## The falsifiable test — evidence for O.2, not proof of it

τ⁴ < 2 means a third modulus **would fit inside the window**, so every such pair
is a chance to observe three. At X = 4000 there are **258 such chances**, and a
third occurs in **none** of them. Read this as evidence for **Conjecture O.2**,
which is open — not as support for Proposition O.1, which is proved by the
inequality chain and needs none.

| population | chances (τ⁴ < 2) | thirds found |
|---|---|---|
| a = 1 (unit cofactor) | 106 | 0 |
| **a ≥ 2 (Type II-admissible)** | **152** | **0** |

The split matters. Note L records that the twenty smallest two-step ratios all
have a = 1 — the unit-cofactor configuration that no Type II split admits — and
raises the worry that the phenomenon might be confined to the family the
application never sees. **It is not**: 152 of the 258 chances have both
cofactors non-trivial, and the mechanism above is uniform in a.

Note the calibration above, though: 258 *chances* is not 258 *informative*
classes. The count that matters is 31.

## Consequence for Proposition L.1

Prop L.1 proves the spacing half (one modulus per class) and cites Dickson for a
count of 2^{ω(M)+O(1)}, giving G′ ≪_ε N^ε, with the measured 2 recorded as
`rigorous_finite`.

**Nothing here improves that bound.** Prop L.1's O_ε(N^ε) stands, and the
measured 2 stays `rigorous_finite`. O.1 rules out one shape of triple — three
moduli in geometric progression under a single τ — which is not the general
statement.

What has changed is narrower and worth stating exactly:

- the **pair** structure is explained, by τ and the exact chain ending a g² < M;
- the **triple** question has a proved constraint M/√D ≥ 11.484 — but from
  **Theorem O.4**, not from the Plücker–parity argument this note first
  attributed it to, which yields 11.3137 asymptotically and 6.93 at X₁ = 1; and
  it is unconditional only in the limit, the exact form being
  τ_min⁴ < 2 + 1/X₁²;
- the one ideal-theoretic route proposed for closing it is **closed**, because
  its coprimality hypothesis is the exception rather than the rule;
- and the empirical support is **31 classes**, not the sweep size.

That is a better-understood 2 than yesterday's, and it is still a measurement.

**What it does not do.** It bounds the *dyadic-window* entry. Note L's full
rational graph still grows (6 → 9 as X goes 500 → 8000) because it sums over all
windows, and [Note F](note-F-failure-localisation.md)'s C₄-freeness over Z[i] is
untouched and remains the obstruction that matters for Type II. A window Gram of
2 rather than N^ε does not create the cancellation Note F shows is absent.

### Two group actions, and why Notes L and O never collided

Both notes act on the solutions of aY² − bX² = M, and they act with **different
groups** — which neither note says, and which is why they have coexisted for so
long without either appearing to contradict the other.

> **Note L's ε** — the fundamental automorph, u² − Dv² = 1 — moves **within** an
> orbit. Prop L.1's spacing m′/m → ε² ≥ φ⁴ = 6.854 is why a dyadic window holds
> **at most one member of each orbit**.
>
> **Note O's τ_k** — the multiplier, U² = M² + 4k²D — moves **between** orbits,
> and τ₁² can sit well below 2. **That is how two moduli land in one window at
> all.**

At (1, 41) — Note L's own windowed witness — the two are seven orders of
magnitude apart:

| | |
|---|---|
| ε = 2049 + 320√41 = 4098 (u² − Dv² = 1 exactly) | within-orbit ratio ε² = **1.679×10⁷** |
| τ₁ = (√41+1)/(√41−1) = 1.370156 | τ₁² = **1.877328** |
| observed 1370/730 | **1.876712** |

*(Verified independently: τ₁² matches the observed ratio to four places, and the
residual is exactly the finite +1 correction that Theorem O.4 found load-bearing.
The two mechanisms differ by a factor of 8.95×10⁶.)*

**And the unit-free witness carries the *identical* τ, not an analogue.**
τ₁ = (√u + 1)/(√u − 1) depends only on **u = b/a**, so it is scale-invariant:
(2, 82) = 2·(1, 41) has u = 41 in both cases and therefore
**τ₁ = 1.370156212 to nine places in both**, with U² = M² + 4D a perfect square
either way (42² at M = 40, 84² at M = 80). So the unit-free pair is a **drop-in
replacement** for the orbit story, not a parallel example — a reader meeting the
structure there never has to dispose of the objection that the witness leans on a
cofactor the Type II hypothesis excludes.

**So the two moduli in that window are in different orbits, brought together by
τ and not by ε** — and the whole structure becomes legible:

> the windowed Gram entry counts **the orbits τ reaches inside one window**;
> ε guarantees **at most one member per orbit**;
> and **Conjecture O.2 is the statement that τ never reaches three.**

Note O's twelve theorems and Note L's Prop L.1 are the two halves of that
sentence, and **neither note contained it**.

> **⚠ The plausible identification is exactly backwards.** Assigning moduli to
> orbits by |V| = 2 — on the reasoning that the fundamental *multiplier* is the
> fundamental *automorph* — produces "two moduli of one orbit inside a window",
> which would **contradict Prop L.1** and read as a defect in Note L. What
> separates them is doing the arithmetic on one example: 1.877 against 1.679×10⁷
> is not a near miss, it is two different objects. *(Prop L.1's own hedge stands:
> its spacing is asymptotic, x′/x → ε, and Note L already records the proved bound
> as O_ε(N^ε) with the constant 2 as `rigorous_finite`.)*

### Where O.2's content actually lives: 43 classes

The τ/ε structure makes the right population computable. A triple needs a class
admitting **two in-window multipliers** — indices k with M² + 4k²D a perfect
square and τ_k² < 2. At X = 3000, over **1,815,155** reduced ratio classes:

| in-window multipliers | classes |
|---:|---:|
| 0 | 1,503,796 |
| 1 | 311,316 |
| **2** | **43** |
| 3+ | **0** |

**Of those 43: forty realise exactly one modulus, three realise two, none three.**
So no chain is realised anywhere, and **O.2's entire content at this X lives on 43
classes** — of which 40 lack the moduli to use the multipliers they admit.

**It scales, and the fraction halves per doubling** *(all three rows reproduced
independently)*:

| X | classes | 0 mult. | 1 | **2** | 3+ | fraction with 2 | moduli realised |
|---:|---:|---:|---:|---:|---:|---:|---|
| 1500 | 453,111 | 375,381 | 77,707 | **23** | 0 | 5.1×10⁻⁵ | {1: 23} |
| 3000 | 1,815,155 | 1,503,796 | 311,316 | **43** | 0 | 2.4×10⁻⁵ | {1: 40, 2: 3} |
| 6000 | 7,267,040 | 6,020,269 | 1,246,693 | **78** | 0 | 1.07×10⁻⁵ | {1: 73, 2: 5} |

The count grows 23 → 43 → 78 while the class population grows fourfold per
doubling, so **the set where a triple is structurally possible grows far more
slowly than the classes do**. *(No law is fitted to 23 → 43 → 78; the values are
the statement. What is claimed is the direction, which is the same at all three
sizes.)* And **the maximum moduli realised is two at every size**, against the
three a triple needs.

**Three thresholds, one constant.** All of them are conditions on M/√D, and
M/√D = (u−1)/√u with u = b/a, so each converts to a cofactor ratio:

| configuration | needs M/√D > | i.e. u > | closed form |
|---|---:|---:|---|
| a **pair** in one window | 4√2 = 5.6569 | **33.9706** | (1+√2)⁴ |
| a **chain** (a second in-window multiplier, k ≥ 2) | 8√2 = 11.3137 | **129.9923** | (4√2 + √33)² |
| a **triple** (Theorem O.4) | 4(2^{1/4}+2^{3/4}) = 11.4840 | **133.8748** | [(1+√2)(1+√2+2^{5/4})]² |

*(All three verified to six places.)* The chain sits **3.8825 below** the triple —
exactly as it must, since a triple needs a chain **and something more**. The
8√2 is the determinant route's constant, |V| ≥ 4 read as k ≥ 2.

**Two of the three are the same formula.** Since |V| ≥ V₀ requires
M/√D > 2√2·V₀, and M/√D = (u−1)/√u, the threshold is

> **u > (√2·V₀ + √(2V₀² + 1))²**

| V₀ | M/√D > | u > | 8V₀²+2 | gap |
|---:|---:|---:|---:|---:|
| **2** | 5.656854 | **33.970563** | 34 | 0.0294 |
| **4** | 11.313708 | **129.992307** | 130 | 0.0077 |
| 6 | 16.970563 | 289.996552 | 290 | 0.0034 |
| 8 | 22.627417 | 513.998054 | 514 | 0.0019 |

**And it closes exactly at the seam**: √2·2 + √9 = 2√2 + 3 = **(1+√2)²**
*(verified symbolically)*, so V₀ = 2 gives u > (1+√2)⁴ — the pair threshold, on the
nose. **So the doubling 4√2 → 8√2 is precisely |V| ≥ 2 → |V| ≥ 4**: not a
coincidence between two derivations made at different times, but **one input read
twice**. The family runs to 8V₀² + 2 from below.

> **⚠ And the triple threshold is genuinely NOT in the family**, which is what
> keeps this honest rather than merely tidy. 133.8748 falls **strictly between
> V₀ = 4 (129.992) and V₀ = 5 (201.995)** — it comes from O.4's *composite*
> τ₁² < √2, not from any |V| bound. Two of the three rows are one mechanism; the
> third is a different one, and their interleaving (chain below triple) is a
> **consistency check, not a pattern**.

**And that is why the 43 are empty: the two requirements pull opposite ways.**

| u = b/a | classes | max shared moduli |
|---|---:|---:|
| < 2 | 530,837 | 2 |
| 2 – 10 | 710,187 | **8** |
| 10 – 100 | 392,697 | 6 |
| 100 – 10³ | 124,151 | 4 |
| > 10³ | 57,283 | 3 |

*(Reproduced independently.)* **A chain needs u > 129.99; the maximum modulus
count falls with u.** So the range where a chain is *possible* is precisely the
range where the moduli to use it are **scarcest** — which is why the 43
chain-admitting classes carry at most two moduli against the three a triple
needs.

> **⚠ Not established as structural.** Three moduli **do** occur above u = 10³,
> so modulus count alone does not forbid a triple. What is established is that
> the two conditions are **in tension**, and that the tension is quantified — not
> that it is decisive.

> **⚠ "realises two moduli" and "realises two moduli IN ONE WINDOW" are different
> counts, and they first diverge at X = 6000.** Of the five classes realising two
> moduli there, **four** have them inside one window — (1,423125) at 10, 17;
> (1,51701) at 82, 145; (53,423125) at 10, 17; (37,26245) at 545, 986 — while
> **(13, 27145) has moduli 2 and 530, a ratio of 265**. At X = 3000 all three
> coincided, so the distinction was invisible there and the smaller table cannot
> show it. **And (37, 26245) at 545, 986 is a fourth live close pair**, not among
> `exp14`'s three — so the smaller table was hiding a witness as well as a
> distinction.

**And the three that realise a k ≥ 2 step are exactly `exp14`'s live
non-fundamental close pairs:**

| (a, b) | k | moduli |
|---|---|---|
| (1, 423125) | 1, 91 | 10, 17 |
| (1, 51701) | 1, 33 | 82, 145 |
| (53, 423125) | 1, 12 | 10, 17 |

**Three independent constructions, same three configurations**: `exp14` streaming
the *realised* side, a count of multiplier indices satisfying a Pell condition,
and an independent re-derivation here reproducing 1,503,796 / 311,316 / 43 and
the same k values exactly.

> **So the supply is not generous where it matters.** Dickson gives
> 2^{ω(M)+O(1)} orbits, but **τ reaches two of them inside one window in only 43
> of 1.8 million classes** — and in 40 of those the moduli do not exist to use it.

**This is the fourth refinement of O.2's denominator**, and each was correct
against its predecessor: 278,939 above threshold → 31 informative classes → 60
with three shared moduli → **43 admitting two in-window multipliers**. Each time
the population shrank because a *necessary condition* was noticed, not because
the data changed.

**⚠ The orbit-margin question this replaces could not be computed, and the reason
is worth recording.** Partitioning a class's moduli into automorph orbits has no
cheap criterion, and both obvious ones fail **in opposite directions**:

- **The order's fundamental unit is wrong.** At (1,5) the observed ratios run
  2, 5, 6.5, 6.8, 6.8462, 6.8529, 6.8539, **6.8541** → φ⁴, so the automorph is
  **φ² = 2.6180**, which lies in the maximal order **Z[φ]** and *not* in Z[√5],
  whose fundamental unit 9 + 4√5 = 17.9443 would predict a ratio of **322** and
  split that single orbit into many.
- **M | V is wrong the other way.** At (1,5) with m = 2, 10 we have V = −2 and
  M = 4, so M ∤ V — yet they are in the **same** orbit. And that is *forced*: the
  subcase alternates along an orbit and p | V holds exactly when subcases agree,
  so consecutive orbit members **necessarily** have M ∤ V.

A mis-partition yields a margin that measures nothing and **looks exactly like a
margin** — the same near-miss as the τ/ε conflation, in a form where it would
have been invisible.

### What the whole thread says about the method

Three **necessary-but-not-sufficient gaps**, at three different scales, all
pointing the same way:

| scale | the bound permits | what occurs |
|---|---|---|
| classes | 39 of 60 informative classes clear O.11 | **none** holds a triple |
| the D axis | D = 5…10 are outside every proved reach | **none** has fallen to X = 8000 |
| in X | O.11's proved reach *falls* with X, 97.7% → 88.1% | nothing realises the excess |

**The bounds permit far more than occurs, at every level.** And that is a
statement about the **method**, not about x²+1: every bound in this apparatus —
O.4's τ_min⁴ < 2 + 1/X₁², O.9's 3ab < M^{4/3}, O.11's constant, O.12's
(5+√21)/2 — comes from a **size** argument, and size arguments cannot see the
arithmetic that actually forbids the configurations. **The D axis is where the gap is narrowest, not where it is
absent.** Every observed failure lies outside the proved reach and nothing inside
it has ever failed — but that states the bound is **sound**, not that it is
**tight**. The reach ends at D ≤ 4.899 and the smallest observed failure is
D = 11, so **D = 5, 6, 7, 8, 9, 10 lie between them**: six values permitted to
fail, protected by no proof, and unfallen to X = 8000. That is row (2) of the
table above, not an exception to it — **six values wide, against 39 of 60 classes
and a reach that falls with X.**

**So the honest summary of the O-thread is not "these theorems nearly close
O.2".** It is: *the size arguments are now sharp enough to be worth stating and
are still nowhere near what is true, and the gap between them is arithmetic
nobody here has reached.*

## What survives

*Written last, after two retractions and one line of investigation withdrawn
wholesale. This is the list a reader should trust.*

**Proved.**

- The invariant U² − DV² = M² and the identity A − B = −(m_j − m_i)M.
- The gap principle |V| < M/√D for m_i ≥ 2, using the window exactly once.
- N(ξ) = aM for ξ = aY + X√D, and ξ₂ξ̄₁ = −a(U + V√D).
- g = gcd(U,V) divides M, and **a g² < M**.
- A multiplier at index k exists **iff a² + (4k²−2)ab + b² is a perfect square**;
  at k = 1 that is (a+b)², a square identically, so the trivial multiplier always
  exists and V = ±2 forces U = ±(a+b) uniquely.
- Mod M the automorph diagonalises in S, T with **unit** eigenvalues, so every
  integrality condition is orbit-invariant.
- τ₁ acting is exactly M | S; equivalently M₂ = 1 in the M = M₁M₂ splitting.
- The identity M(ρ² − 1) = 4ka(k − ρ) with ρ = B_k/M, and ρ < 1.06066 from the
  geometry.
- **S·T = −M·m** (Lemma O.8.1), and hence gcd(M,S)·gcd(M,T) = M for M odd.
- The exact **a·|V|·(X_jY_i + X_iY_j) = M(X_j² − X_i²)**, giving
  |V| < (M/2√D)(R − 1/R) with R = X_j/X_i — the sharp form of the |V| law, with
  no asymptotics. *The factor a is load-bearing.*

**Proved — the triple question, in the order they were found.**

- **O.3**, M odd squarefree: no window holds (ξ, τ₁ξ, τ_kξ), k ≥ 2.
- **O.3′**, superseding it: the same whenever **gcd(M, 2X) ≤ 16**, no hypothesis
  on M — reaching even and non-squarefree M, including (53, 423125).
- **O.3″**, superseding *that*: a triple needs
  (4k + √(16k²+2))(2c+1) < c(kc − c − 1). O.3′ is its k → ∞ shadow; **k = 2 is
  excluded for every c ≤ 33**.
- **O.4**, assuming nothing about which multiplier acts: a window holds three only
  if **τ_min⁴ < 2 + 1/X₁²** — asymptotically b/a > 133.875, i.e.
  M > 4(2^{1/4} + 2^{3/4})√(ab). Repairs the constant this note had attributed to
  the Plücker–parity route, which gives 11.3137 and not 11.484.
- **O.5**: τ_p² ∈ T forces M | 8p², so **no window holds (ξ, τ_pξ, τ_p²ξ)** for
  any p, given X₁ ≥ 1. Supersedes Proposition O.1 and explains its (1,5) escape
  (M = 4 | 8).
- **O.6**: for M an odd prime the subcase (M | S vs M | T) **alternates at every
  step** with M ∤ V. Its consequence for the composite's two integrality
  conditions is that they are vacuous — *not*, as first written, that the route
  is dead.
- **O.7**: hence **no window holds three when M is an odd prime** — Conjecture
  O.2 on 14% of realised close pairs, covering p ≠ q. Two steps flip twice, the
  one-step composite flips once, and the dichotomy forbids both.
- **O.8**: the same for **M odd squarefree**, on the hypothesis gcd(V,M) = 1 —
  which is *observed on every in-window pair* (295 of 295) and **not proved**. It
  is equivalent to g = gcd(U,V) = 1, the quantity Prop O.1 tracks.

- **O.9**: for M odd squarefree, no hypothesis — each solution carries a **sign**
  σ = ±1 with Y ≡ σX (mod p), p | V_ij ⟺ σ_i = σ_j, and three signs cannot be
  pairwise distinct. So **M | V₁₂V₂₃V₁₃** and **3ab < (b−a)^{4/3}**.
- **O.10**, dropping *every* hypothesis on M: the sign becomes a **valuation
  split** s_i + t_i ≥ e with s = min(e, v_p(S)), t = min(e, v_p(T)); ordering
  s₁ ≤ s₂ ≤ s₃ gives v_p(V₁₂) + v_p(V₂₃) ≥ e. The sign is its e = 1 shadow.
- **O.11**: R₁₂R₂₃ = R₁₃ couples the three bounds, and sinh(u₁₂)sinh(u₂₃) at
  fixed u₁₃ peaks at the **equal** split, so the constant improves **6.85×** to
  **ab < 0.048628·(b−a)^{4/3}**.

**What is left of O.2.** Nothing structural — no hypothesis on M survives. What
is left is **quantitative**: at X = 8000, 13 of 109 informative classes clear
O.11's inequality, all with a = 1, and none of them holds three moduli in a
window. **The bounds are not what forbids triples in nature** — the same verdict
as O.3″ and O.4, now reached from a proved inequality rather than a threshold.

**And O.11's reach is falling**, 97.7% → 88.1% over X = 1500–8000, with the
admissible count doubling per doubling of X. Whatever closes the remaining
classes is not a refinement of this constant.

**Measured, and trustworthy as measurements.**

- The τ² law for close pairs, relative error O(1/m), 1.3×10⁻⁴ for m ≥ 1000.
- |V| = 2 in 495 of 498 close pairs, with |V| ≥ 2 by parity for a, b both odd.
- No dyadic window with three shared moduli in any sweep: 208 informative
  classes at X = 60000, and 31 at X = 4000.

**Withdrawn.**

- Everything resting on r-products as a predictor of window behaviour: the 95
  candidates, the 322, the 258 τ⁴ < 2 "chances", the factor of 3.91, and the
  parallel session's decade drift and sub-1 crossing. The r-product is a ratio
  between solution *classes* and does not predict the spacing of the *occupied*
  moduli — demonstrated on (1, 115921), where it predicts 1.31 and the observed
  minimum ratio is 33.77.
- The claim that O.2 follows from Q̄, Q̄″ coprimality: true, but the hypothesis
  holds in 5 of 65 observable cases.
- Two earlier claims retracted in place above: "no window holds three" as proved,
  and N(ξ) = ±M.

### The sharp form of O.2, and the identity behind it

*Measured the right way round — occupancy as the input, per the inverted method.*

For each realised solution ξ, ask which multipliers actually **act** on it, i.e.
for which k is τ_kξ integral. Two facts, neither of which I expected.

**Multipliers act freely, and often several at once.** Over 1.8M solutions at
X = 3000, 18,116 admit one acting multiplier, 215 admit two, and some admit six.
The acting set can be a whole cyclic semigroup: (1,5) at m = 2 admits
k ∈ {1, 3, 8, 21, 55, 144}, which are exactly τ₁, τ₁², τ₁³, … — τ₃ = (7+3√5)/2
= φ⁴ = τ₁². So "τ² is never integral" is **false in general**, and O.3′ is not
saying otherwise: it forbids it only in the window regime, and (1,5) has
r₁ = 6.854.

**But never two inside a window.** Restricting to acting multipliers with
modulus ratio r < 2:

| | count |
|---|---|
| solutions ξ with at least one acting multiplier | 13,840 |
| with exactly one acting multiplier at r < 2 | 327 |
| **with two or more at r < 2** | **0** |

Extended by [`exp17`](../experiments/exp17_sharp_form.py), which restricts to the
slice y/x ≥ 3+2√2 where a second in-window multiplier is geometrically possible
at all, and bounds the k-loop by k < M/(4√2·√D) rather than by an arbitrary
ceiling:

| X | solutions with an acting multiplier | with exactly one at r < 2 | **with two** | smallest competing ratio |
|---:|---:|---:|---:|---:|
| 3 000 | 689 | 449 | **0** | 14.91 at (1, 901), m = 842 |
| 14 000 | 2 583 | **2 093** | **0** | 14.15 at (1, 16133), m = 3970 |
| 40 000 | 6 796 | **6 019** | **0** | 14.15 at (1, 16133), m = 3970 |

**Read those middle columns with care — most of them are vacuous.** A solution
whose (a,b) has only *one* in-window multiplier could never have carried two, so
it says nothing about O.2. Counting only the solutions whose (a,b) has **≥ 2**
in-window multipliers:

| X | carrying exactly one | **informative** | with two |
|---:|---:|---:|---:|
| 3 000 | 449 | **3** | 0 |
| 14 000 | 2 093 | **9** | 0 |

So the evidence base is **9 informative solutions at X = 14000**, not 2 093 —
and this note quoted the larger number until the check was run. That is
`triples-cannot-be-settled-by-measurement` one level down, after both sessions
had named it and after I had applied it to the *class* count (31 of 278 939)
without thinking to apply it here. The earlier sentence claimed 6 019 solutions
"could have carried a second" — not an
absence measured over a vacuous population, which is the distinction
`triples-cannot-be-settled-by-measurement` insists on. The margin drifts slowly
(14.91 → 14.15) and stays a factor of 7 above the 2 a window needs.

> **Sharp form of O.2.** On any ξ, at most one acting multiplier has r < 2.

This is equivalent to O.2 — a third modulus in the window is exactly a second
in-window multiplier — and it is the form that is directly measurable. The margin
is wide: when a second multiplier acts alongside an in-window one, its ratio is
at least **14.91** (over 53 such cases) against the 2 a window needs. Examples:
(1,901) at m = 842 acts at k = 1, 27, 465 with ratios 1.143, 14.91, …;
(1,85) at m = 17 acts at k = 1, 9, 56, 189.

**Why it is a statement about classes, not members.** The acting conditions are
M | A_kS and M | B_kT, and the automorph diagonalises S, T with **unit**
eigenvalues mod M — so acting is **orbit-invariant**. Either τ_k acts on every
member of a class or on none. That is the same fact the parallel session sees
from the dual side, where the cofactors sharing moduli {10, 17} form two
interleaved orbits of 17x² − 10y² = −7 with two-step ratio (ε²)² = 459,682, so a
dyadic window admits **one member from each of two orbits** — and that is the
measured constant 2, not a coincidence.

### An exact identity behind the constant 17

Writing **B_p = M + δ_p**, the relation A_pB_p = M(M + 4p²a) with A_p = B_p + 4pa
gives

> **δ_p(2M + δ_p + 4pa) = 4paM(p − 1)**

— exact, **0 violations over 1,002,709 multipliers**. Two consequences:

- **δ_p = 0 exactly when p = 1.** So B₁ = M identically. This is the cleanest
  statement of why τ₁ is special, and it is the same fact as j = 2 ⟺ k = 1 and
  as M₂ = 1, now visible as a single vanishing.
- Since 2M + δ_p + 4pa > 2M, the identity gives the exact bound
  **δ_p < 2ap(p−1)** for p ≥ 2.

**Two small lemmas the identity gives in the window regime**, both proved from it
and both verified over the 50 strictly in-window multipliers with k ≥ 2 in
a < 60, b < 80000:

- **Distinct in-window multipliers never share a δ.** If δ_p = δ_q, subtracting
  the two identities gives δ(p−q) = M(p−q)(p+q−1), so δ = M(p+q−1) ≥ 2M — against
  δ < 0.06066M. *(0 same-δ pairs observed.)*
- **δ_p is pinned to within 8% of 2ap(p−1).** The window gives
  4pa/M < (1/√2)√(a/b) ≤ 0.121 and δ_p/M < 0.06066, so the identity's denominator
  2M + δ_p + 4pa is under 2.182M and

  > **0.917 · 2ap(p−1) < δ_p < 2ap(p−1).**

  *(Measured 0.9655 … 0.9929; minimiser (29, 9605) at k = 3, where δ/M = 0.0351
  and 4ka/M = 0.0363 against the bounds 0.06066 and 0.121.)*

  A first check reported a minimum of 0.8000, apparently violating the bound. The
  filter was `k ≤ M/(4√2√D) + 2`, whose "+2" admits multipliers just *outside* the
  window, where the derivation does not apply. Same shape as everything else
  today — a correct computation over the wrong population — this time in a check
  written to test a bound derived minutes earlier.

And it recovers O.3′'s constant from an independent route: the geometry gives
ρ_p < 1.06066, i.e. δ_p < 0.06066M; then d_p = gcd(δ_p, M) ≤ δ_p < 0.06066M, so
**M/d_p > 16.48, i.e. ≥ 17** — the same 17 as the integer-in-(c, 1.06066c)
argument, reached without it.

### Routes tried on O.2's general case, and why each fails

*Recorded so they are not re-run. All concern the remaining case: two multipliers
τ_p, τ_q with p, q ≥ 2 both acting on one ξ with modulus ratio < 2.*

1. **Ideal coprimality.** O.2 follows if Q̄ and Q̄″ are coprime. True, but the
   hypothesis is usually false — coprimality holds in **5 of 65** cases where it
   can be observed. *Closed, not incomplete.*
2. **A local obstruction.** All 95 constructed candidates satisfy the acting
   congruences together with the conic **mod M**. O.2 is not a congruence
   statement.
3. **Walking the automorph orbit.** Superseded rather than failed: mod M the
   automorph diagonalises S, T with **unit** eigenvalues, so acting is
   orbit-invariant and every point of an orbit gives the same answer. Walking was
   never going to find anything.
4. **Nagell as a lower bound on fundamental solutions.** Wrong direction —
   Nagell bounds a class representative from **above** (V ≤ M(√ε−1/√ε)/2√D). The
   general case needs a *lower* bound on non-trivial fundamental solutions, and
   none is standard because in general it is false: k = 12, 33, 91 are exactly
   such small solutions.
5. **The exact divisibility with S·T = −Mm.** Acting gives (M/g_T) | T and
   (M/g_S) | S with g_T = gcd(δ_p, δ_q, M), g_S = gcd(δ_p+4pa, δ_q+4qa, M), so
   m ≥ M/(g_Tg_S). **No contradiction**, because O.2 puts no upper bound on m —
   the window constrains the *ratio*, not the height.
6. **(5) plus a Nagell upper bound on the smallest m.** Orbit-invariance means
   the two multipliers act on the smallest member too, and Nagell bounds it by
   ≈ εM/2D. A contradiction would need ε < 2D/(g_Tg_S) ≈ 543a/b. Measured:
   ε = 3.6×10³ against a bound of 0.60 for (1, 901); 4.4×10⁵⁵ against 0.005 for
   (1, 115921). **Fails by tens of orders.**
7. **Constructing candidates from multipliers.** Invalid in principle, not just
   in practice — see the withdrawal above: the r-product is a ratio between
   solution *classes* and does not predict the spacing of the *occupied* moduli.
8. **Deciding O.2 at the residue level, without finding solutions.** This looked
   the most promising, because acting is orbit-invariant and therefore a function
   of (S, T) mod M — so a class could in principle be decided with no search at
   all. Two things came out of it, one useful and one fatal.

   *Useful:* the relaxed conditions M | A_kS and M | B_kT **factorise** — the
   first constrains only S, the second only T — so two multipliers p, q can
   co-act only if **αβ | M** with α = gcd(A_p, A_q, M), β = gcd(B_p, B_q, M).
   Cheap, and it eliminates 19 of the 40 in-window pairs found with a < 80,
   b < 60000. It is also *only* necessary: sum-and-difference is weaker than the
   original pair whenever 2 is not invertible mod M, and our M is usually even.
   Validated against real solutions — 898 604 agreements, 2 794 disagreements,
   all in the permissive direction, so a zero here would still be conclusive.

   *Fatal:* it is not zero. Enumerating (X, Y) mod M against the **exact** four
   linear conditions plus the conic X² ≡ Y², all **21 of 21** surviving pairs
   have a simultaneous residue solution — (1, 16354) at p=1, q=15; (2, 5125) at
   p=1, q=8; (74, 21389) at p=1, q=2; and eighteen more.

   > **So there is no residue obstruction to O.2 whatsoever.** The configurations
   > exist mod M and are simply not occupied.

   **And that last clause is now witnessed rather than inferred.** Taking the
   pairs whose two-multiplier residue exists and enumerating their *actual*
   shared moduli to x ≤ 6×10⁶:

   | (a, b) | p, q | shared moduli | which of {p,q} acts on each |
   |---|---|---|---|
   | (2, 5125) | 1, 8 | 10211776961, 19026737665 | {8}, {} |
   | (2, 8321) | 1, 9 | 8065, 8581 | {1}, {} |
   | (5, 7922) | 1, 7 | 1, 925, 139413121 | {}, {}, {} |
   | (1, 16354) | 1, 15 | 785, 338486405, 349241345 | {}, {1}, {} |
   | (74, 21389) | 1, 2 | *none* | — |

   Every occupied class carries **at most one** of the two, and the residue class
   carrying both is occupied in none of them.

   ### The tightest near-counterexample, fully characterised

   **(a, b) = (2, 8321)**, M = 8319, D = 16642. Everything a counterexample needs
   is present except the last step:

   - it is **live**: shared moduli m = 8065 and 8581 (8065·2 − 1 = 127², etc.);
   - they are a **close pair**: ratio 1.06398, inside a window;
   - τ₁ **explains it exactly**: r₁ = 1.06398, agreeing to five decimals;
   - a **second in-window multiplier exists**: k = 9, U₉ = 8637, r₉ = 1.73542 < 2;

   *(r is the **modulus** ratio throughout, per the convention 400 lines above —
   the multipliers themselves are τ₁ = 1.03150 and τ₉ = 1.31735, and it is their
   squares that are listed. Restated here because a convention stated once at the
   top of a long note is the same trap as DFI's determinant, and the parallel
   session read these as τ.)*
   - the **residues permit both** — this pair is one of route 8's 21;
   - so a third modulus at 8065 × 1.73542 ≈ 13996 would sit inside the window.

   **13996 is not a shared modulus, and neither is anything within ±4 of it.**
   τ₉ simply does not act on this class. Every ingredient lines up and occupancy
   alone forbids the triple — which is the whole of Conjecture O.2 in a single
   configuration, and the object to hold in mind when reading the eight closed
   routes above. This is the sharpest statement of
   the evidence available: not "no triple was found", but *"for the pairs where a
   triple is residue-possible, the occupied classes systematically avoid the
   residue that would produce it."*

   That kills the route and sharpens the conjecture: **any proof of O.2 must
   involve occupancy** — which classes actually contain solutions — and not the
   congruence data. Occupancy is a class-group question about the form, so this
   is also why the "countable conjunction of finite checks" framing above, while
   correct, does not make O.2 mechanically decidable: each check needs a
   fundamental solution, not a residue.

The common shape of 5 and 6 is that every bound available constrains M, a, b and
the *ratio*, while a triple is unconstrained in **height**. Any proof will have
to use something that does not scale with m.

**And there is such a thing, which is why the measurement is stronger than it
looks.** Acting is orbit-invariant, so it is a property of the *class*, not of
the member — one solution per class settles it for the whole infinite orbit.
So O.2 is not a statement about arbitrarily large m at all: it is the statement
that **no occupied class carries two in-window multipliers**, and each class is
decided by a single finite check. What [`exp17`](../experiments/exp17_sharp_form.py)
covers is therefore *exactly* the classes possessing a solution below X — 2 093
of them at X = 14000, each settled completely rather than sampled. The classes it
misses are those whose least solution exceeds X, and nothing here bounds how many
of those there are.

**Open.** Conjecture O.2, with no mechanism. It does now have a
candidate-generation method that cannot produce a dead configuration, due to the
parallel session and recorded here because it inverts everything above:

> **Enumerate realised ratio classes, take those with two moduli in one window,
> and read off which multiplier index explains the ratio.** Occupancy is the
> *input*, not an afterthought; the multiplier structure is the output.

Generating candidates from multipliers and testing occupancy searches a mostly
empty parameter space — that is what went wrong with the 95 and the 322. Running
it the other way cannot. The method's first product is the sharpest object
either of us has:

> **(53, 423125)**, live, with shared moduli m = 10 and m = 17 at ratio 1.70000
> — inside a window — where τ₁² = 1.045787 and the realised close pair sits at
> **k = 12**, r₁₂² = 1.70066 (relative error 3.9×10⁻⁴). Its only multipliers
> below k = 4000 are k = 1 and k = 12. Verified with no parameterisation:
> 53·10−1 = 23², 423125·10−1 = 2057², 53·17−1 = 30², 423125·17−1 = 2682².

This is one of the three |V| ∉ {2} cases from the top of this note — |V| = 24 =
2·12 — seen from the other end. It shows the close pair of a live class can be
realised at a **non-fundamental** multiplier, so a triple's two multipliers need
not include τ₁, which is exactly the p, q ≥ 2 gap O.3 does not cover. And
M = 423072 = 2⁵·3²·13·113 is both even and non-squarefree, so O.3 is mute on it
— while **O.3′ reaches it**: c = gcd(M, 2X) is 2 at m = 10 and 12 at m = 17,
both ≤ 16, so O.3′ correctly permits those two and forbids only a third.

**The sibling is the caution, and it caught a misattribution.** (1, 423125) has
the *same* two modulus values, 10 and 17, reached from different x — and for it
**no** multiplier below k = 4000 explains the ratio: the nearest, k = 91, is
2.2% off. It is one of 12 unexplained close pairs at X = 3000, all small-m,
where the O(1/m) correction dominates. An earlier version of this paragraph
named (1, 423125) at k = 91 as the non-fundamental case; that was an index read
off a list without checking the residual, and it is wrong. The robust content is
the **exclusion of k = 1**, which holds either way.

Census from the inverted method at X = 3000: 379 close pairs, 367 explained by
some multiplier index — **366 at k = 1 and exactly one at k ≥ 2** — with 12
unexplained within k ≤ 4000. So the non-fundamental shape is realised, and
realised **once**. Rare, not absent.

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
- *Was O.2 claimed as proved?* Yes, in a draft of this note and in a message to
  the parallel session, and it was wrong. The composition step treated
  Q̄′ | (ξ₂) and Q̄ | (ξ₁) as conditions on one element. Retracted above, in
  place, with the reduction that survives stated exactly. The lesson is the one
  the session has hit twice already: the bound was correct and the inference
  from it was not, and no measurement could have caught it because the
  configuration it concerns does not occur.
- *Does this rescue the theorem?* No, and it should not be read that way. It
  sharpens one bookkeeping constant inside Note L. The parity barrier and Note F
  are where the problem lives, and neither moves.

---

## O.13 The true threshold is (1+√2)⁴, and O.12 is short only on non-τ₁ configurations

O.12 proves that two shared moduli of a banded cofactor pair cannot lie in one
window, via τ_V² < 3 with |V| ≥ 1, giving **u > (5+√21)/2 = 4.7913**. That is a
*bound*; it says nothing about how much room is left. The extremal realised
configuration says.

**Proposition O.13.** *A 4-cycle whose two shared moduli are related by the
fundamental multiplier τ₁ lies in one dyadic window only if*

  **u = b/a > (1+√2)⁴ = 17 + 12√2 = 33.970563…**

*Proof.* The modulus ratio is τ₁², and a window requires τ₁² < 2, i.e.
(√u+1)/(√u−1) < √2. Rearranging, √u (√2−1) > √2+1, so
√u > (√2+1)/(√2−1) = (√2+1)² = 3+2√2, and u > (3+2√2)² = 17+12√2. ∎

Elementary — but it is a statement about **τ₁ configurations only**, and O.12
must cover every V, which is exactly the factor it gives up.

**The realised extrema are all τ₁.** Enumerating realised windowed 4-cycles and
reading off which multiplier explains each ratio — the direction this note
insists on, occupancy as input — at X = 6000 for D = 1, the twelve smallest
unit-free cofactor ratios are:

| u | cofactors | moduli | m₂/m₁ | τ₁² | ratio | u/(1+√2)⁴ |
|---:|---|---|---:|---:|---:|---:|
| **34.0811** | (37, 1261) | (866, 1730) | 1.99769 | 1.99771 | 0.99999 | **1.00325** |
| 34.0984 | (193, 6581) | (1130, 2257) | 1.99735 | 1.99735 | 1.00000 | 1.00376 |
| 34.1882 | (85, 2906) | (1997, 3985) | 1.99549 | 1.99550 | 1.00000 | 1.00641 |
| 34.3400 | (50, 1717) | (1181, 2353) | 1.99238 | 1.99239 | 1.00000 | 1.01088 |
| 34.4340 | (53, 1825) | (314, 625) | 1.99045 | 1.99048 | 0.99998 | 1.01364 |
| 34.5385 | (13, 449) | (7730, 15370) | 1.98836 | 1.98836 | 1.00000 | 1.01672 |

**Twelve of twelve match τ₁² to five decimals**, and the minimum sits **0.325%
above** the Proposition's threshold. D = 2 behaves identically: minimum 34.0548
at (73, 2486), 0.248% above.

**And the converse separates cleanly, which is what makes this a mechanism
rather than a coincidence.** D = 4 has realised windowed 4-cycles *below* the
threshold — u = 19.2400 at (25, 481) and 19.7267 at (35113, 692665) — and both
have m₂/m₁ ÷ τ₁² = **0.632** and **0.640**, i.e. they are **not** τ₁. Both sit
on the same tiny modulus pair **(5, 8)**. Every configuration at or above the
threshold is τ₁; every one below it is not.

**So the 7× gap has a cause.** O.12 proves 4.7913 because it must cover non-τ₁
configurations. Those exist — D = 4 has two — but at D = 1 and D = 2 none is
realised, so the effective threshold is (1+√2)⁴ and the extremum attains it to a
third of a percent. **The theorem buys 2.40× of margin over a band's 2 where
17.04× is true, and the missing factor 7.09 is exactly the non-τ₁ allowance.**

⚠ This does **not** prove x²+1 admits no non-τ₁ windowed 4-cycle; that is the
cross-orbit case this note repeatedly records as the one multipliers do not
predict (on (1, 115921) the multiplier product predicts a modulus ratio 1.31
against an observed minimum 33.77). It is measured absence over a finite range,
and a bound's silence is not evidence about what lies outside it.

> **⚠ What in O.13 is new, and what was already here.** The values **13.9282**
> (X₁ = 1) and **33.9706** (asymptotic) were already recorded above, in the
> paragraph on O.12 not being knife-edge, reached via |V| ≥ 2 from the parity
> lemma. O.13 did not discover them and does not claim to. What is new is the
> **closed form** — 33.9706 = (1+√2)⁴ = 17 + 12√2, and the family
> u > (√2V + √(2V²+1))² it belongs to — the **characterisation of which V are
> admissible** (V = 2 always at D = 1 via U = a+b; V = 1 exactly on the
> Eisenstein condition), and the **extremal measurement** 34.0811, which corrects
> the 43.79 recorded above. *I wrote O.13 without grepping for its own numbers
> first; the note and the derivation agreeing is the good case, but the check
> costs one search and I did not run it.*

### O.13′ The threshold as a function of V, and what a sub-threshold cycle forces

**For D = 1 only.** The M·D section applies: for x²+D the conic is
aY² − bX² = M·D, so every formula below with M in it needs M → M·D. What
follows is derived and checked at D = 1 and is **not** transferred.

Write s = √(ab)/M. Then τ_V = √(1 + V²s²) + Vs, and τ_V² < 2 ⟺
√(1+V²s²) < √2 − Vs ⟺ **Vs < 1/(2√2)**, i.e. (u−1)/√u > 2√2·V, i.e.

  **u > (√2·V + √(2V² + 1))²**

| V | threshold | admissible when |
|---:|---|---|
| 1 | (√2+√3)² = **5 + 2√6 = 9.898979** | ~~a² − ab + b² a perfect square~~ — **never occurs**, see below |
| 2 | (2√2+3)² = **17 + 12√2 = 33.970563** | **always** |
| 3 | (3√2+√19)² = **73.986484** | — |

**V = 2 is always admissible**, since U = a+b gives U² − abV² = (a+b)² − 4ab = M²
identically — that is τ₁, and it is why O.13's threshold is the generic one.
**V = 1 requires U² = M² + ab = a² − ab + b² to be a perfect square**, the
Eisenstein norm form: (a, b) must be a *60-degree Pythagorean pair*. Thresholds
**increase** with V, so no V ≥ 3 can rescue a configuration that V = 2 rejects.

**Proposition O.13′ (D = 1).** *A windowed 4-cycle satisfies either
u > (1+√2)⁴ = 33.9706, or 5 + 2√6 = 9.8990 < u < 33.9706 with a² − ab + b² a
perfect square. Below 9.8990 no V is admissible at all.*

> **⚠ THE SECOND BRANCH IS EMPTY, so the proposition collapses to u > 33.9706.**
> V = 1 never occurs for x²+1 (`V-never-one-unconditionally`). If a, b are both
> odd this is Note L's parity lemma; if exactly one is even then, since a cofactor
> of x²+1 is never divisible by 4, it is ≡ 2 (mod 4) and
> a² − ab + b² ≡ 3 (mod 4), which is not a square — and V = 1 requires
> U² = M² + ab = a² − ab + b². So the Eisenstein condition and the parity lemma
> exclude V = 1 in complementary cases, and **the exceptional branch cannot be
> entered at all.** The enumeration in O.13″ below is therefore doubly empty: its
> candidates all have a, b both odd, so parity already forbade them.

**Measured, and the vacuity stated rather than hidden:** at X = 4000 there are
**576** realised unit-free windowed 4-cycles and **none** is below 33.9706, so
the exceptional branch is available and **never used** — which also means the
Diophantine condition is tested on **zero** cases here. *A conditional verified
over an empty antecedent is verified of nothing;* the content is the theorem,
not the check.

> **⚠ An earlier version of this section claimed D = 4 supplies the converse** —
> its two sub-threshold cycles, u = 19.2400 at (25,481) and 19.7267 at
> (35113,692665), do have a² − ab + b² a perfect square (219961 = 469²). **That
> reading is withdrawn.** At D = 4 the invariant is M·D, so the threshold is
> (u−1)·D/√u > 2√2·V, giving **u > 2 + √3 = 3.7321** at V = 2 — and 19.24 and
> 19.73 are *above* it. They are ordinary configurations, not exceptions, and the
> perfect-square coincidence is not evidence of V = 1: the correct V = 1 test at
> D = 4 is whether (M·D)² + ab is square, and for (25,481) it is **3339001,
> which is not**. Caught by checking my own derivation against the M·D section
> before committing, not by anything failing. **The D = 4 numbers are
> observations without an interpretation** *(the D-generalisation itself is now
> done — see O.13‴ below).*

⚠ The thresholds above are the **asymptotic** ones (τ_V² < 2). O.12 proves its
bound with τ_V² < 3, which is why 4.7913 is below even the V = 1 value of
9.8990: it is not merely covering V = 1, it is also carrying the finite
correction. The two allowances are separate and multiply.

### O.13″ The exceptional branch is inhabited, and what empties it is occupancy

Closing O.13′'s second branch would turn O.12's proved 4.7913 into **33.9706**,
a factor 7.09 — the single largest improvement available to the theorem. Two
filters apply before any occupancy question is asked:

- **Eisenstein.** a² − ab + b² must be a perfect square, for V = 1 to exist.
- **Gaussian.** n | x²+1 is solvable iff 4 ∤ n and n has no prime factor
  ≡ 3 (mod 4). **Both** cofactors must pass — a condition the Eisenstein one
  knows nothing about, so there was reason to hope the two are incompatible.

**They are not.** At a ≤ 1200 four primitive pairs pass both:

| pair | u | shared moduli (x ≤ 3×10⁶) | most in one window | spread |
|---|---:|---:|---:|---:|
| (25, 481) | 19.2400 | **2** — {2, 53546} | 1 | **26773×** |
| (505, 7897) | 15.6376 | 0 | 0 | — |
| (865, 22873) | 26.4428 | 1 — {74} | 1 | — |
| (985, 29593) | 30.0437 | 0 | 0 | — |

So the branch is **inhabited**, and neither congruence filter empties it.

**What empties it is occupancy.** (25, 481) *does* share two moduli — 2 and
53546, both verified (25·2 = 7²+1, 481·2 = 31²+1) — and they are a factor
**26773** apart. Nothing forbids the configuration; the moduli simply are not
near each other.

**Which is the wall this note already records for O.2**: *any proof must be
about occupancy, not congruences.* The gap between O.12 and O.13′ is therefore
not a gap that a sharper local argument can close — it is the same difficulty,
at a different scale, and that is the useful thing to know about it.

⚠ Bounded: a ≤ 1200 and x ≤ 3×10⁶. Larger a is untested, and a bound's silence
is not evidence about what lies outside it.


### O.13‴ The generalisation to arbitrary D

Every formula in its M·D form, per the invariant table:

  conic aY² − bX² = **M·D**;  multiplier U² − abV² = **(M·D)²**;
  window τ_V² < **2 + D/X₁²**.

With s = V√(ab)/(M·D) and c = 2 + D/X₁², a window needs s < (c−1)/(2√c), i.e.

  **√u − 1/√u > 2√c · V / ((c−1)·D)**

At D = 1, X₁ → ∞ this recovers u > (1+√2)⁴, so the general form is anchored to
the case that is checked.

**V = 2 is automatic for every pair only at D = 1**, where U = a+b gives
(a+b)² − 4ab = M². For D ≠ 1 it needs (M·D)² + 4ab to be a square — true for
(3,7) at D = 5 and (3,4) at D = 11, false for the rest below — so **the minimal
admissible V is pair-dependent**, which is what makes the general threshold
non-uniform and is the step O.13′ left open.

Checked at X = 1500 against the smallest realised unit-free windowed 4-cycle:

| D | min u realised | pair | min V | X₁ | threshold | slack | V=2 auto |
|---:|---:|---|---:|---:|---:|---:|---|
| 1 | 34.0811 | (37, 1261) | 2 | 179 | 33.9691 | **1.00×** | yes |
| 2 | 34.2121 | (33, 1129) | 4 | 80 | 33.9556 | **1.01×** | no |
| 3 | 24.0691 | (1057, 25441) | 4 | 65 | 16.1452 | 1.49× | no |
| 4 | 19.2400 | (25, 481) | 4 | 11 | 9.5150 | 2.02× | no |
| 5 | 2.3333 | (3, 7) | 2 | 1 | 1.4204 | 1.64× | yes |
| 6 | 15.7611 | (4081, 64321) | 4 | 169 | 5.3682 | 2.94× | no |
| 7 | 2.3125 | (16, 37) | 1 | 11 | 1.4697 | 1.57× | no |
| 8 | 3.6667 | (3, 11) | 4 | 1 | 1.4185 | 2.58× | no |
| 11 | 1.3333 | (3, 4) | 2 | 2 | 1.2348 | **1.08×** | yes |

**No violation at any D**, which is as much the point as the thresholds are:
three separate errors tonight came from using a D = 1 formula generally, and a
machinery that produces no violation across nine D is evidence the corrected
forms are right where re-reading them was not.

⚠ **Do not read the sharp cases as a pattern.** D = 1, 2 and 11 being near-tight
while 4 and 6 are loose is nine points with no proposed mechanism. That D = 11
is both the first failing D *and* near-tight is exactly the kind of near-miss
this note has had refuted before.

---

## O.14 Below u = 53.6942, Conjecture O.2 is an explicit finite list

O.13's V-family applies to the triple question, which is O.2 itself. A window
holding three shared moduli needs the composite of two multiplier steps to fit:
**τ_min⁴ < 2 + 1/X₁²**. With s = V√(ab)/M, the condition τ_V² < c is
√u − 1/√u > 2√c·V/(c−1), so with c = √(2 + 1/X₁²):

| X₁ | V = 1 (needs a²−ab+b² square) | V = 2 (always, U = a+b) |
|---:|---:|---:|
| 1 | ~~14.8609~~ (V = 1 never occurs) | **53.6942** |
| 10 | 34.4675 | 131.9783 |
| → ∞ | 34.9419 | 133.8748 |

**The V = 2 column is Theorem O.4, recovered independently** — this note records
O.4 as "b/a > 53.69 at X₁ = 1, rising to 133.875", and the family gives
133.874781 to six decimals from a different starting point.

**So unconditionally in X₁: a windowed triple needs u > 53.6942.** The V = 1
branch below it is *empty*, not merely sparse — `V-never-one-unconditionally`
shows V = 1 never occurs for x²+1 — so O.4's exception is closed and the
threshold is unconditional. *(The enumeration below was carried out before that
was known; it stands as an independent check, since every candidate it found is
unoccupied as well as excluded.)*

**That branch is finite and enumerable.** Both cofactors must also divide some
x²+1 — 4 ∤ n and no prime factor ≡ 3 (mod 4) — and at a ≤ 3000 exactly **five**
primitive pairs pass both filters:

| pair | u | shared moduli (x ≤ 2×10⁷) | most in one window | local obstruction |
|---|---:|---:|---:|---|
| (25, 481) | 19.2400 | 2 — {2, 53546}, ratio 26773 | 1 | none |
| (505, 7897) | 15.6376 | 1 | 1 | none |
| (865, 22873) | 26.4428 | 1 — {74} | 1 | none |
| (985, 29593) | 30.0437 | 0 | 0 | none |
| (1345, 54937) | 40.8454 | 0 | 0 | none |

**A triple needs three in one window; the maximum observed is one.** And every
candidate is locally solvable at every modulus checked, so what empties the
branch is **occupancy, not congruence** — the third independent confirmation of
this note's position that O.2 is not a congruence statement.

**What this does and does not do.** It is the first reduction of any part of O.2
to a finite explicit list. It does **not** close the conjecture: above 53.6942
the V = 2 branch is available to every pair, and that range is exactly what O.4
already covers as a necessary condition without settling it.

⚠ Bounded at a ≤ 3000 and x ≤ 2×10⁷; larger a may add candidates, and a bound's
silence is not evidence about what lies outside it. The counts are size-dependent
even where the conclusion is not — (505, 7897) shows 0 shared moduli at
x ≤ 5×10⁶ and 1 at x ≤ 2×10⁷.

---

## O.15 Combining O.5 with |V| ≥ 2: the triple threshold rises to 82.5571

O.14 puts the triple threshold at 53.6942 (X₁ = 1) by bounding the composite
below by τ_min², i.e. by taking **both steps at the minimum**. Theorem O.5
forbids exactly that: *"No dyadic window contains (ξ, τ_pξ, τ_p²ξ), for any
p ≥ 1, provided X₁ ≥ 1"*, and its own derivation states the case as "when the
two steps carry the same multiplier". Since U² = M² + DV² determines U from V up
to sign, **same V means the same multiplier**, so a triple forces V ≠ W.

Combining that with `V-never-one-unconditionally` (|V| ≥ 2, no hypothesis):

- if a, b are **both odd**, Note L's parity lemma makes every V even, so
  {V, W} ⊇ {2, 4};
- otherwise exactly one is even and odd V is permitted, but V = 1 is not, so
  {V, W} ⊇ {2, 3}.

The window needs (τ_V τ_W)² < 2 + 1/X₁², with τ_V = √(1 + V²s²) + Vs and
s = √(ab)/M = 1/(√u − 1/√u):

| (V, W) | X₁ = 1 | X₁ → ∞ | |
|---|---:|---:|---|
| (2, 2) | 53.6942 | 133.8748 | **excluded by O.5** |
| (2, 3) | **82.5571** | 207.8186 | one cofactor even |
| (2, 4) | **117.4171** | 297.7611 | a, b both odd |

> **Theorem O.15.** *A dyadic window contains three shared moduli of a coprime
> admissible pair only if u > 82.5571, and only if u > 117.4171 when a and b are
> both odd. Asymptotically the thresholds are 207.8186 and 297.7611.*

So the unconditional necessary condition improves on O.4's 53.6942 by a factor
**1.5375**, and by **2.1868** on the both-odd branch that covers every candidate
O.14 enumerated.

*(Values cross-checked by bisection and by an independent symbolic solve, both to
four decimals. The three columns of the first row reproduce O.4 and O.14, which
is the check that the composite formula is the same one those results use.)*

⚠ This is a **necessary** condition, not a proof of O.2. Nothing here forbids a
triple above 117.4171, and that is where the conjecture lives.

### O.16 The minimal distinct composite reduces to one congruence

O.15 leaves (V, W) = (2, 4) — the note's k = 1, 2 — as the binding configuration.
O.5 closes p = q because τ_p² ∈ T becomes a divisibility on M alone; this note
records that the composite for p ≠ q "does not collapse the same way". It does
not, but it reduces to a single congruence, which is worth having explicitly.

With τ_p = (U_p + 2p√D)/M and U_p² = M² + 4p²D,

> τ₁τ₂ = (U₁U₂ + 8D + (4U₁ + 2U₂)√D)/M²,

so τ₁τ₂ ∈ T requires **M | U₁U₂ + 8D** and **M | 4U₁ + 2U₂**. Reduce mod M using
b ≡ a, hence D = ab ≡ a² and U₁ = a + b ≡ 2a:

> U₁U₂ + 8D ≡ 2a(U₂ + 4a),  4U₁ + 2U₂ ≡ 2(U₂ + 4a).

Since gcd(a, M) = gcd(a, b − a) = 1, the two conditions are the same one:

> **Lemma O.16.** *τ₁τ₂ ∈ T ⟺ M | 2(U₂ + 4a), where U₂ = √(M² + 16D).*

**Machine-checked: 155 classes at a < 60, b < 4000 admit both k = 1 and k = 2
multipliers, and the criterion agrees with the full two-condition test on all
155, with zero disagreements.**

**It is restrictive but does not close the case.** Only **21 of the 155** satisfy
it — 14% — of which 17 have U₂ ≡ −4a (mod M) exactly and 4 rely on the factor 2,
which needs M even. So unlike O.5's p = q, there is a sign available and the case
survives; the note's assessment was right, and this is the number behind it.

⚠ Closing (1,2) alone would not close O.2: it would raise O.15's binding pair to
(1,3), not eliminate it. The value here is that the condition is now one
congruence rather than two, and its density is measured.

### O.17 The composite criterion in general: a per-prime sign

O.16 handled (p, s) = (1, 2). The general case reduces the same way, and the
reduction is the **sign mechanism of O.9** rather than a new device.

τ_p τ_s = (U_pU_s + 4psD + 2(sU_p + pU_s)√D)/M², so integrality needs

> **M | U_pU_s + 4psD** and **M | 2(sU_p + pU_s)**.

Since D = ab ≡ a² (mod M) and U_p² = M² + 4p²D ≡ (2pa)², we have U_p ≡ 2σ_p·pa
for a sign σ_p — but **only per prime**, because U_p² ≡ (2pa)² has 2^ω(M) roots
mod M. Working at a prime power r^e ‖ M and writing the local signs σ_p, σ_s:

> U_pU_s + 4psD ≡ 4psa²(σ_pσ_s + 1),  2(sU_p + pU_s) ≡ 4psa(σ_p + σ_s).

Both vanish exactly when σ_p ≠ σ_s; otherwise they are 8psa² and 8psa, and
gcd(a, M) = 1 leaves r^e | 8ps.

> **Lemma O.17.** *τ_pτ_s ∈ T ⟺ at every prime power r^e ‖ M, either
> r^e | 8ps, or the local signs of U_p and U_s differ.*

**The local sign always exists where it is needed.** If r^e does not escape then
r ∤ 8ps, so r is odd and r ∤ p; and r | M with gcd(a, M) = 1 gives r ∤ a. Hence
r ∤ 2pa and the square root of (2pa)² mod r^e is ±-unique.

**It recovers O.5.** For p = s the signs are identical at every prime, so the
condition is r^e | 8p² everywhere, i.e. **M | 8p²** — Theorem O.5's condition,
obtained here as the degenerate case rather than separately.

**Machine-checked over 68,820 (class, p, s) triples** with a < 45, b < 2500 and
p ≤ s ≤ 6 that admit both multipliers: the criterion agrees with the full
two-condition test **68,820 times, zero disagreements**. The per-prime decisions
are 117,795 "signs agree, not integral", 20,053 "r^e | 8ps", 911 "signs differ,
integral" — and **zero** cases where no local sign existed, as the argument above
predicts.

**Why this is the right form.** O.9 derives M | V₁₂V₂₃V₁₃ from exactly this sign,
and O.10 upgrades it to a valuation. The composite integrality turns out to be
governed by the same object, so O.5, O.16 and the sign arguments are three faces
of one mechanism rather than three techniques.

⚠ Still does not close O.2: the criterion is satisfiable — 911 of the observed
per-prime decisions go the integral way — so the configuration survives.

### O.18 The alternation does not extend to odd composite M — route nine, closed

O.17 shows the composite criterion is a **per-prime** sign, and O.6's alternation
forces opposite signs, which is exactly why the integrality conditions carry no
information. That suggests an extension: O.7 closes M an odd **prime** by parity
— two steps flip twice, the one-step composite flips once, and the dichotomy
forbids both. If the alternation held **per prime**, the same parity argument
would run at each prime of any odd M and close O.2 for all odd M.

**It does not.** At X = 3000, over classes with M odd composite, at least two
shared moduli, and **unit-free** (a ≥ 2, since a = 1 is inadmissible anyway):

| | count |
|---|---:|
| alternates at every step | 794 |
| **does NOT always alternate** | **20** |
| dichotomy fails at some solution | 18 |

Counterexamples: (2, 65) M = 63 at r = 7 with subcase codes [1, 1, −1];
(2, 925) M = 923 at r = 71 with [1, 1, −1]; (2, 5945) M = 5943 at r = 7 with
[−1, −1]; (10, 673) M = 663 at r = 3 with [−1, −1]; (2, 185) M = 183 at r = 3
with [1, 1].

**And the dichotomy itself fails 18 times** — at those solutions neither or both
of r | S, r | T hold, so the local sign is not even defined. O.6's proof that
exactly one holds uses M prime (both would give M | 4pa, hence M | p); at a
prime power dividing a composite M that step does not survive.

So the ninth route on O.2's general case is closed, and for a reason worth
keeping: **O.6's alternation is a statement about M prime, not a statement about
each prime of M.** The per-prime structure that O.17 exposes for the *composite
criterion* does not propagate to the *alternation*.

⚠ Recorded so it is not retried. It is the natural move once O.17 is in hand, and
it looks like it should work.

---

## O.19 This whole thread is the D(−1)-tuple extension problem

**The identification is exact and elementary.** m is a shared modulus of the
cofactor pair (a, b) iff am − 1 and bm − 1 are both perfect squares — because
am = X²+1 and bm = Y²+1. That is precisely the condition for m to be a common
**D(−1)-extension** of a and b, in the sense of Diophantine m-tuples: a
D(−1)-set is a set whose pairwise products are one more than a square.

**Verified on this note's own running examples.** The pair (1, 5) at m = 2 — the
counterexample that forced the window hypothesis into Proposition O.1 — is the
classical D(−1)-triple **{1, 2, 5}**: 1·2−1 = 1², 1·5−1 = 2², 2·5−1 = 3². And
the unit-free witness (2, 82) with moduli 365 and 685 has all four products
square, though 2·82−1 = 163 is not, so {2, 82} is not itself a D(−1)-pair. **The
configuration studied here requires two of the three products to be squares, not
all three**, so it is the *extension* equation rather than the triple condition.

**What the literature has that this note does not.**

- The D(−1)-quadruple conjecture is **resolved**: there is no Diophantine
  D(−1)-quadruple (Bonciocat–Cipu–Mignotte, arXiv:2010.09200).
- **Gap principles are standard equipment** in that field — Dujella's gap
  principle, `c > 4ab` for regular quadruples, and explicit extension counts of
  a triple by ranges (at most 3, 7, 6 or 0 depending on where c sits relative to
  b² and 200b⁴).
- The technique is **linear forms in logarithms** (MSC 11J68), Baker's method
  and Baker–Davenport reduction — not congruences, and not the size arguments
  this note has been building.
- The structural result that a D(−1)-quadruple {a,b,c,d} with a < b < c < d
  forces **a = 1** independently mirrors this repo's finding that *every class
  O.11 admits has a = 1*.

**What this means for O.2.** This note records eight closed routes and a ninth
(O.18), and concludes that "any proof must be about occupancy, not congruences"
and that size arguments cannot reach it. Both may be true and both may be beside
the point: **the field's answer to exactly this kind of question is linear forms
in logarithms**, which is neither a congruence nor a size argument, and which
this note has never attempted.

**⚠ And do not over-read the transfer.** Dujella's Lemmas 2–3 intersect **two**
Pellian equations, because he extends a *triple* {a,b,c} by d, giving his (4) and
(5). Note O's configuration is a cofactor **pair** with one equation and three
solutions in a window, so the two-recurrence intersection has no analogue here.
What would transfer is the **gap principle** — and this note already has one,
O.4's τ_min⁴. The literature's are absolute (c > 4ab); O.4's is a ratio, and O.2
is open precisely where a ratio bound goes weak, at large u where τ_min → 1. So
the transfer is genuinely uncertain, and this section must not be read as "the
tools exist, just apply them".

**What was confirmed by reading it** (22pp, via pymupdf — the fetcher could not
parse the PDF): the elimination gives a z² − c x² = a − c, the same shape as
A Y² − B X² = M; the solution classes come from **Nagell Theorem 108a**, the same
Nagell this note tried and recorded as "running the wrong way"; and Lemma 2 works
**modulo 2c**, twice the larger element, where this note tested congruences
modulo M = b − a and found none. Different moduli — **mod 2b was never tried
here.**

⚠ **STATUS.** The identification and the two worked examples are verified here.
The literature statements are from abstracts and search results, **not from the
papers read in full**, and must be treated as `inferred` until someone reads
them. In particular: whether the standard gap principles apply when {a,b} is not
itself a D(−1)-pair, and whether O.2 is already a corollary of known results, are
both **open questions about the literature**, not settled facts.
