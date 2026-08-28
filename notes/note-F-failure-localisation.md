# Note F — Failure localisation

*Plan §2.4.2. Status: draft — the strongest result in the repo and the leading
candidate for "the exact lemma that fails". Supported by
[`exp02`](../experiments/exp02_bilinear_pilot.py),
[`exp03`](../experiments/exp03_density_ledger.py), and
`tests/test_bilinear.py::test_incidence_graph_of_the_line_is_c4_free`.*

## The single off-diagonal sum

Dispersion (plan §2.2) Cauchy–Schwarzes in m and opens the square, leaving

> Σ_{n₁ ≠ n₂} β_{n₁} β̄_{n₂} · **G(n₁, n₂)**,  G(n₁, n₂) := #{m : mn₁ ∈ A and mn₂ ∈ A}.

Everything in Step 2 comes down to G. The plan (§2.2.4–5) anticipates that G
becomes a congruence/lattice count, to be detected by additive characters and
bounded by Weil. **That is not what happens.**

## Lemma (the line admits no multiplicative coincidence)

> Let A = {x + i : x ≥ 1}. If m₁ ≁ m₂ and n₁ ≁ n₂ and all four of m₁n₁, m₁n₂,
> m₂n₁, m₂n₂ are associates of elements of A, then contradiction.
> **Hence G(n₁, n₂) ≤ 1 for all n₁ ≠ n₂.**

*Proof.* Write m_j n_k = u_{jk} a_{jk} with a_{jk} = x_{jk} + i ∈ A and u_{jk} a
unit. From m₁n₁ · m₂n₂ = m₁n₂ · m₂n₁ we get a₁a₄ = u·a₂a₃ for some unit u,
where a₁ = x₁+i, … , a₄ = x₄+i and x_j ≥ 1.

Now (x+i)(y+i) = (xy − 1) + i(x + y) has Re ≥ 0 and Im ≥ 2 for x, y ≥ 1, so
both a₁a₄ and a₂a₃ lie in the closed first quadrant with imaginary part ≥ 2.
Multiplication by i, −1, or −i moves that region to Re < 0, Im < 0, Im ≤ 0
respectively, so **u = 1**. Comparing parts,

> x₁ + x₄ = x₂ + x₃  and  x₁x₄ = x₂x₃,

so {x₁, x₄} and {x₂, x₃} are the roots of one quadratic and agree as multisets.
If x₁ = x₂ then m₁n₁ ∼ m₁n₂, so n₁ ∼ n₂; if x₁ = x₃ then m₁n₁ ∼ m₂n₁, so
m₁ ∼ m₂. Both contradict the hypothesis. ∎

Machine-checked three ways: exhaustively on a box
(`test_line_admits_no_multiplicative_coincidence`), on the actual incidence
matrices at four dyadic splits (`test_incidence_graph_of_the_line_is_c4_free`),
and on the full unrestricted divisor graph (`test_c4_freeness_does_not_depend_on_the_split`).

**The lemma does not mention the split.** Its proof uses no norm range, so it
applies to the incidence graph of *every* multiplicative decomposition of A at
once. Verified: with all divisors admitted and no range restriction, the graph
is 37 975 × 37 975 with 75 948 edges at X = 8000, and the maximum off-diagonal
Gram entry is still **1**. So there is no balanced, unbalanced, or
well-factorable choice of split that escapes it — a well-factorable weight
λ(m) = Σ_{m=m₁m₂} λ₁(m₁)λ₂(m₂) produces a trilinear form whose every
Cauchy–Schwarz still lands on a bipartite Gram matrix of exactly this kind.

## Why this is the failure

The dispersion method exists to evaluate G(n₁, n₂) as *main term + error* and
to beat the trivial bound by controlling the error. Here **G is identically 0
or 1.** There is no main term, no congruence to detect, no exponential sum to
introduce, and therefore no Weil bound to apply. Cauchy–Schwarz has thrown away
the entire saving and handed back a set of 0/1s, and the only remaining source
of cancellation is the sign pattern β_{n₁}β̄_{n₂} — which is what we were trying
to establish in the first place.

Concretely, measured at X = 2×10⁴ (`exp02`): the naïve dispersion bound comes
out at **θ = 1.00–1.03 at every split** — worse than the trivial bound. Not
"insufficient by a small exponent": it never had a saving to lose.

## The same fact from the density side

For any A ⊂ Z[i] of size |A| with norms ≍ Q, splitting a = mn with N(m) ≍ M
gives mean degrees D_m ≍ |A|/M and d_n ≍ |A|M/Q, hence

> D_m · d_n ≍ |A|²/Q =: κ,  independent of M, and max_M min(D_m, d_n) ≍ √κ.

| sequence | \|A\| | κ | √κ | predicted / measured max min-degree |
|---|---|---|---|---|
| x² + 1 | Q^{1/2} | **1** | 1 | 1 / **1.26** |
| x³ + 2y³ | Q^{2/3} | Q^{1/3} | Q^{1/6} | — |
| a² + b⁴ | Q^{3/4} | Q^{1/2} | Q^{1/4} | 48.7 / **41.2** (Q = 10⁷) |

Density Q^{1/2} is exactly the value at which κ = 1. The plan's "thinner than
anything yet handled" is not a matter of degree: **Q^{1/2} is the critical
density at which the Type II incidence matrix degenerates to a forest.**

Checked beyond the mean, since a skewed degree distribution could still hide a
thick sub-rectangle: the **(2,2)-core is empty at every split** — no subgraph
in which every row and every column has degree ≥ 2. For a² + b⁴ at the same
norm bound the maximum off-diagonal Gram entry is **667**.

> **This is the line in the ledger where the two-parameter freedom of (a, b) is
> used.** Not in Type I, not in the local densities, not in the choice of
> sieve — here, to make G(n₁, n₂) large enough to have a main term.

**How much weight κ can carry, corrected.** κ = 1 ⟹ forest ⟹ no main term is
a real implication and it is what this note rests on. The converse is not
available and this note should not be read as suggesting it: a² + (b²+1)² has
the *same* density, the same κ to 0.04%, and the same max min-degree to 3% as
a² + b⁴, yet its provable Type II range is a sixth of an exponent shorter and
it yields a lower bound where a² + b⁴ yields an asymptotic
([Note K](note-K-merikoski.md), [`exp08`](../experiments/exp08_merikoski_ledger.py)).
That is the first control the repo has that varies structure while holding
density fixed, and it says κ is **necessary and not sufficient**. Nothing above
depends on sufficiency — the argument here runs entirely through κ = 1.

## Under a level-1/2 sieve, this lemma is the whole obstruction

[Note C](note-C-requirements.md) establishes that a prime-detecting sieve
running at Type I level x^{1/2} exists — Duke–Friedlander–Iwaniec, as used by
Green–Sawhney — and that x² + 1 **meets** its Type I hypothesis. Its Type II
hypothesis asks for cancellation with **arbitrary 1-bounded coefficients** over
N(b) ∈ [(log X)^C, X^{3/8}]. Measured there:

| N(m) | worst-case θ | θ with β = μ |
|---:|---:|---:|
| [10, 10²) | **1.000** | 0.627 |
| [10², 10³) | **0.999** | 0.775 |
| [10³, 1682) | **0.999** | 0.825 |

With β = μ there is cancellation; with arbitrary β there is none. That gap is
exactly C₄-freeness. **So once the x^{2/3} artefact of [ASP] is removed, this
lemma stands alone as the obstruction** — and unlike (R1) it is a theorem about
the sequence, not a hypothesis of a sieve.

## The important caveat

[ASP] does **not** require cancellation for adversarial β; DFI does. Its Type II
hypothesis has the absolute value outside the m-sum (so α is effectively
arbitrary) but supplies **β = μ**. With β = μ the form does cancel: [Note
H](note-H-numerical-pilot.md) measures Σ_m |Σ_n μ(n)·1[mn ∈ A]| ≍ √(MX), which
is o(X) for M = o(X). So the lemma above proves:

- ✅ **dispersion cannot work here**, at any split, for a structural reason;
- ✅ **DFI's arbitrary-coefficient Type II hypothesis is false** for this
  sequence — measured θ ≈ 1 across its whole stated range;
- ❌ **not** that [ASP]'s μ-coefficient Type II hypothesis is false.

Every drop of the required saving must come from the arithmetic of μ along the
fibres, with no help whatever from the incidence geometry. That is precisely
the regime the parity barrier governs.

## DFI say the parity-breaking input *is* the arbitrary-coefficient form

Read from the page images of the Duke scan, p. 425, immediately above
Proposition 1:

> "It is now well-understood that information about L_d(M) is **not sufficient**
> to demonstrate asymptotic formulae for primes (or even their existence) due to
> a 'parity problem' [B]. In recent years this problem has been partially
> surmounted by adding new information about general bilinear forms of the type
>
>     (8)  B(M, N) = ΣΣ_{(m,n)=1} α_m β_n ρ_h(mn).
>
> **Here α_m and β_n are arbitrary but bounded complex numbers** with support
> M < m ≤ 2M and N < n ≤ 2N. In this paper we are able to obtain just barely
> enough information about the sums L_d(M) and B(M,N) to wipe out the parity
> problem in its entirety."

So the thing that breaks parity, in the words of the people who broke it, is the
bilinear form **with arbitrary bounded coefficients on both sides**. That is
precisely the object this note's lemma is about.

> **Note F is therefore not an obstacle standing beside the parity barrier. It
> is the statement that DFI's parity-breaking input does not exist for
> A = {x+i}.**

That is a sharper placement than "dispersion has no main term", and it comes
from the source rather than from this repo. Two consequences worth separating:

- **What they need versus what they prove.** They need (8) with arbitrary
  coefficients; what Proposition 2 (p. 426) delivers is the case "β_n are
  supported on primes". The gap between those two is exactly where this sequence
  dies, and it is the same gap [FM]'s footnote 1 expects to close in general.
- **Their own plausible bounds are out of reach here for a different reason.**
  p. 425 offers L_d(M) ≪ M^{1/2}(hdM)^ε and B(M,N) ≪ ‖α‖‖β‖(M+N)^{1/2}(hMN)^ε
  as "plausible"; Proposition 1 achieves only
  L_d(M) ≪ (h,d)^{1/20}(d/M)^{1/20}M^{1+ε}. A factor of ten in the exponent —
  but both are *signed*, and [Note J](note-J-mobius-in-progressions.md) measures
  that the difficulty here is entirely in the absolute values.

## Ford–Maynard name this exact counting function

Found on a third pass through arXiv:2407.14368v1, footnote 2, p. 7. Explaining
why a set J ⊆ (x/2, x] with x^{1−c} elements resists Type II estimates beyond
θ + ν = 1 − 2c:

> "Showing one can take θ + ν ⩾ 1 − 2c is closely related to estimating
> **#{n : nm₁, nm₂ ∈ J}** with an error term better than O(1) on average over
> m₁, m₂ ∼ x^{1−2c+ϵ} (i.e. to show bilinear cancellation in the error term),
> which is typically very difficult outside of special situations."

That is G, with the roles of the two variables named the other way round. So
the object this note is built on is the object the literature's own survey of
the method identifies as the barrier — and where they say "typically very
difficult", the lemma above says, for this sequence, **impossible**: the count
is 0 or 1, so the error term *is* O(1) and no averaging can improve it.

**Where the residual inference actually lives, and it is not ours.** Two distinct
steps sit in that quotation and only the first is exact:

1. **The identification of the object.** Their #{n : nm₁, nm₂ ∈ J} *is* G, with
   the variables named the other way round. That is an equality of definitions,
   not an inference, and Theorem O.12 now proves the 0/1 property over **Z** on
   exactly the configuration their average runs over — m₁, m₂ banded and n
   banded — so it no longer needs the Gaussian-to-rational transfer either.
2. **The implication from that object to the (θ, ν) parameters.** Ford–Maynard
   write that θ + ν ⩾ 1 − 2c is **"closely related to"** estimating it. They do
   not write *equivalent to*, and the hedge is theirs, not a looseness in this
   note's reading of them.

> So the step from "the count is 0 or 1, so the error term is O(1) and
> unimprovable" to "**ν = 0 in Ford–Maynard's sense**" rests on a four-word phrase
> in the source. That is why `gaussian-to-rational-bridge` and
> `fm-barrier-is-unconditional-at-density-half` are `inferred` and why **no amount
> of further computation here can promote them** — the missing link is a precise
> statement of the relation, which would have to come from the literature or from
> a direct argument, not from measuring this sequence more carefully.

*Naming it matters because the two steps had been read as one.* The first is now
proved on both sides; the second was never ours to close.

Two consequences worth stating separately:

- It is external evidence that the repo is measuring the right thing. Note F was
  derived here from the Gaussian-integer structure, not read out of a paper.
- It sharpens what "special situation" means. a² + b⁴ is one: its incidence
  graph has 4-cycles in abundance (max off-diagonal Gram entry **667** at
  Q = 10⁷, against **1** here). So is a² + (b²+1)², measurably to within a few
  percent of it — see [Note K](note-K-merikoski.md), which is the reminder that
  having 4-cycles is necessary and not sufficient.

## Candidate problem statement

> **Question F.** Let A = {x + i : x ≤ X} and M = X^u with 0 < u < 1. Does
>
>     Σ_{N(m) ≍ M} | Σ_{n} μ(n) · 1[mn ∈ A] |  ≪_A  X (log X)^{−A}
>
> hold? Numerically the left side is ≍ √(MX) = X^{(1+u)/2}, comfortably o(X)
> for every u < 1. The content is whether this survives as a theorem given
> that G(n₁, n₂) ≤ 1, so that no bilinear/dispersion argument can reach it.

This is the inequality Step 2's checkpoint (plan §2.5) asks for, in its
cleanest form. What it still needs is the second half of the checkpoint: a
quantitative statement of how far current bounds fall short — which is
[Note G](note-G-spectral.md), and is not yet done.

## Adversarial review

- *Two-parameter freedom smuggled in?* No. The lemma uses only that elements of
  A have imaginary part exactly 1; κ uses only |A| and Q.
- *Where is parity broken?* Nowhere. This note is a negative result: it shows
  the standard parity-breaking mechanism is structurally unavailable, and does
  not supply a replacement. Do not read it as an impossibility proof.
- *Does the lemma generalise the wrong way?* It uses Im = 1 only through
  "Im(a) is the same for all a ∈ A". The same proof kills 4-cycles for
  {x + ci} for any fixed c. It fails as soon as Im varies — which is exactly
  a² + b⁴. Worth stating in that generality in the write-up.
- *Is C₄-freeness really fatal, or just fatal to* this *dispersion arrangement?*
  Cauchy–Schwarz in **n** has now been run: the maximum off-diagonal entry of
  C·Cᵀ is also 1, at every split. That is forced — a 4-cycle is a 4-cycle
  whichever side is squared — so no rearrangement of the *square* helps.
  A well-factorable or unbalanced decomposition does not help either: the
  lemma holds on the *full* divisor graph, so there is no split to choose. What
  survives is only the question of whether a method that never squares at all
  could work — which is a question about methods, not about this lemma.
