# Note O — The multiplier τ, and the three-in-a-window question

*Not in the plan's deliverable list. Written because
[Note L](note-L-rational-graph.md)'s Proposition L.1 proves a bound of
O_ε(N^ε) on the dyadic-window Gram entry while the measured value is 2, and
because both sessions independently proposed — and both had refuted — a
probability model for the gap. This note supplies the mechanism for the **pairs**
and proves it; it reduces the **triple** question to a statement it does not
settle, and closes the one route it proposed for settling it.*

*Status: **Proposition O.1 proved (τ² ξ is never integral). Conjecture O.2 — the
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

## Proposition O.1 — τ acts at most once *on a given solution*

**Read the qualifier.** τ acting "at most once" is a statement about one solution
ξ, not about a ratio class. A class contains many solutions at widely separated
positions, and **each of them carries its own τ-pair**. At X = 2500 the class
(a,b) = (1,53) has shared moduli 10, 17, 24650, 42850 — two close pairs,
(10, 17) at ratio 1.700 and (24650, 42850) at ratio 1.73832, both matching
τ² = 1.73835. So τ acts twice in that class. What never happens is τ acting
twice **from the same ξ**, which is what a third modulus in one window requires.
The proposition below is about that, and the per-class count is unbounded.

> **Proposition O.1.** Let a < b be coprime, M = b − a, D = ab, and let ξ₁ be a
> solution with m_i ≥ 2. Then **τ² ξ₁ is not integral**: no window contains
> three shared moduli lying in geometric progression under a single multiplier.

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
multiplier, and geometry permitting r₁·r_k < 2. **There are 95**, the tightest
being (1, 115921) at k = 22 with r₁r_k = 1.309 — comfortably inside a window.

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
M > 2√2·k√(ab). Substituting M = 8kaw/e and b = a + 8kaw/e, and using
k = (j+w)/2, this becomes

> e² + 4jwe + 2w²(2e − 1) < 0.

For j ≥ 3 we have e ≥ 5, so every term is positive. Contradiction. ∎

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
solutions of U² − DV² = M² can be — a Nagell-type question about a specific
Pell-with-square-right-hand-side, not about x²+1 at all. That is a well-posed
question in a studied area, which is a better place to leave it than the
factor of 3.91.

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
