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

The threshold itself is the parallel session's, and with O.2 open it is now the
**only unconditional constraint on a triple** anyone has. V is a 2×2
determinant, so three solutions satisfy the Plücker relation
V_ij X_k − V_ik X_j + V_jk X_i = 0 (machine-checked in Note L as
`test_three_term_determinant_identity`). With X_k/X_i < √2 that forces
|V_ik| > 2 + 2/√2 = 3.41, hence |V_ik| ≥ 4 by the parity lemma, hence
M/√D ≥ 4/(2^{1/4} − 2^{−1/4}) = 11.484 — against the 5.657 a mere pair needs.
**It contains no ideal theory**, so it does not share the failure mode of the
composition step above.

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
- the **triple** question has a proved unconditional constraint, M/√D ≥ 11.484,
  which is the parallel session's Plücker–parity argument and contains no ideal
  theory;
- the one ideal-theoretic route proposed for closing it is **closed**, because
  its coprimality hypothesis is the exception rather than the rule;
- and the empirical support is **31 classes**, not the sweep size.

That is a better-understood 2 than yesterday's, and it is still a measurement.

**What it does not do.** It bounds the *dyadic-window* entry. Note L's full
rational graph still grows (6 → 9 as X goes 500 → 8000) because it sums over all
windows, and [Note F](note-F-failure-localisation.md)'s C₄-freeness over Z[i] is
untouched and remains the obstruction that matters for Type II. A window Gram of
2 rather than N^ε does not create the cancellation Note F shows is absent.

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
- **Theorem O.3**, for M odd squarefree: no window holds (ξ, τ₁ξ, τ_kξ), k ≥ 2.
- **Theorem O.3′**, superseding it: the same conclusion whenever
  **gcd(M, 2X) ≤ 16**, with no hypothesis on M. Squarefreeness forces
  gcd(X,M) = 1 hence c | 2, so O.3 is the special case. O.3′ reaches even and
  non-squarefree M — including (53, 423125), where c = 2 and 12.

**Measured, and trustworthy as measurements.**

- The τ² law for close pairs, relative error O(1/m), 1.3×10⁻⁴ for m ≥ 1000.
- |V| = 2 in 495 of 498 close pairs, with |V| ≥ 2 by parity for a, b both odd.
- The Plücker–parity constraint M/√D ≥ 11.484 for any triple.
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
