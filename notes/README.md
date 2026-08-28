# Notes

The deliverables named in the plan. Status is honest: `draft` means the
mathematics is written and machine-checked where checkable; `skeleton` means
the structure is in place and the content is not.

| note | title | plan ref | status |
|---|---|---|---|
| [A](note-A-dictionary.md) | Dictionary — x²+1 over Z[i] | §1.3.1 | draft |
| [B](note-B-type-I.md) | Type I computation | §1.3.2 | draft |
| [C](note-C-requirements.md) | Requirements table | §1.3.3 | **answered** |
| [D](note-D-comparison-ledger.md) | Comparison ledger vs a²+b⁴ | §1.3.4 | draft |
| [E](note-E-naive-dispersion.md) | Naïve dispersion run | §2.4.1 | draft |
| [F](note-F-failure-localisation.md) | Failure localisation | §2.4.2 | draft |
| [G](note-G-spectral.md) | Spectral attempt | §2.4.3 | draft — premise corrected; Step 2 checkpoint written |
| [H](note-H-numerical-pilot.md) | Numerical pilot | §2.4.4 | draft |
| [I](note-I-a2b4-replay.md) | a²+b⁴ replay | §2.4.5 | draft — harness calibrated |
| [J](note-J-mobius-in-progressions.md) | Möbius in progressions | *added* | draft — names the missing input, and localises the difficulty to the absolute values |
| [K](note-K-merikoski.md) | Merikoski's a²+(b²+1)² | *added* | draft — the fourth published sequence; κ is necessary, not sufficient |
| [L](note-L-over-Z.md) | The same question over Z, and over every degree | *added* | draft — Note F's scope, the degree ladder, and K_{s,2} for every s |
| [M](note-M-where-mu-lives.md) | Where the μ-cancellation lives | *added* | draft — the two windows are complements; the easiest case is Chowla, and so is the upper bound |
| [N](note-N-green-tao-exclusion.md) | The Green–Tao exclusion, re-argued | *added* | draft — exclusion survives, quantitatively, and for a different reason than the plan gives |
| [O](note-O-tau-multiplier.md) | The τ multiplier | *added* | draft — τ cannot act twice **inside a window** (the bare form is false); Theorems O.3 and O.3′; the general "no window holds three" is **open** |

## Read Note C first

Note C is filled in from the sources and sets the frame for everything else.

**The asymptotic sieve for primes, as stated, does not apply to x² + 1**:
hypothesis (R1) needs D > x^{2/3}, and Note B proves this sequence caps at
x^{1/2}.

**"Type I or Type II?" is a false dichotomy.** [ASP] p. 1045 shows x^{2/3} is
exactly the threshold below which the coefficient γ(n, C) in the bilinear
hypothesis (B) is annihilated — C = xD^{−1} must stay below N ≈ √D, or
Σ_{d|n, d≤C} μ(d) collapses to Σ_{d|n} μ(d) = 0. So (R1) *is* the condition
that (B) has content, and the single underlying fact is that at A(x) = x^{1/2}
there is no room for the parity-breaking mechanism. It surfaces three ways:

| symptom | note |
|---|---|
| (R1) unsatisfiable — D ≤ A(x) = x^{1/2} | [B](note-B-type-I.md) |
| (B) vacuous — C/N ≈ x^{1/4}, so γ(n,C) ≡ 0 | [C](note-C-requirements.md) |
| incidence matrix is a forest — κ = 1 | [F](note-F-failure-localisation.md) |

Note F's C₄-free lemma is the sharpest **sequence-intrinsic** form, and the one
that survives changing sieve. Heath-Brown's precedent for relaxing (R1) is real
but reaches an ε, not the x^{1/6} needed here.

**Notes F and J describe one obstruction from two sides.** Note J reduces the
Type II input to Σ_q |Σ_{x ≡ r_q (q)} μ(x²+1)|, and the absolute value per
modulus *is* the arbitrary outer coefficient. Measured: the signed sum is under
2% of the absolute-value sum, so the whole difficulty is in the |·|, which is
exactly what C₄-freeness kills.

**And DFI say the arbitrary-coefficient bilinear form *is* the parity-breaking
input** (p. 425). So Note F is not an obstacle standing beside the parity
barrier — it is the statement that their parity-breaking input does not exist
for this sequence. Sharpest placement the repo has, and it comes from the
source.

**Both remaining routes are closed, negatively.** The well-factorable route:
every theorem in the BFI line buys its level by giving up the absolute value, so
beyond level 1/2 there is no absolute-value statement to appeal to
([Note J](note-J-mobius-in-progressions.md)). And the μ-Type II as a theorem:
its θ → 0 endpoint is Chowla for x²+1, which Teräväinen calls wide open
([Note M](note-M-where-mu-lives.md)). For this sequence the trivial bound has
never been beaten by any amount, at any level, signed or absolute.

After reading Duke–Friedlander–Iwaniec and Ford–Maynard at source, the position
is worse than earlier drafts recorded. With ν = 0 (Note F) C⁻ = 0 already
follows from Selberg; the divisor-bounded escape is closed by their Thm 2.7(c);
and the claim that x² + 1 *meets* DFI's Type I hypothesis is **refuted** — DFI's
Theorem S is normalised to x and is vacuous on a sequence of mass x^{1/2}.

**The Ford–Maynard placement is stated by ν, not by γ.** A third reading (see
Note C, *The Ford–Maynard placement, corrected again*) withdrew two things: the
attribution to their Theorem 2.4, whose hypothesis P ∈ A\*₂ requires ν ≥ 1/3 and
so never applied here, and the weight put on γ = 1/2 − ε versus 1/2, a
distinction their own Table 1 caption discards. What binds is ν = 0, by Selberg
and by their Theorem 2.1; every entry in their Table 1 has ν > 0, and their
footnote 2 p. 7 names Note F's G(n₁,n₂) as the barrier.

**Note F's lemma is Z[i]-scoped, and [Note L](note-L-over-Z.md) says so.** The
Type II hypotheses of [ASP], [DFI] and [FM] quantify over *rational* m and n,
and the rational incidence graph of the same sequence is a coarsening of the
Gaussian one. The gap is larger than "2 rather than 1": six cofactors share the
moduli 10 and 17, in an infinite Pell orbit, so over Z the graph contains
**K_{s,2} for every s** where Note F forbids K_{2,2}. The *unwindowed* rational
bound does not exist. What supplies the constant 2 is the window — orbit members
are ~4.6×10⁵ apart, so a dyadic window admits one from each of two orbits.
**But (II) bands the cofactors too**, and there the coarsening
does not survive: [FM]'s (II) is bilinear over m ∼ M *and* n ∼ N, and **Theorem
O.12** proves that cofactors within a factor (5+√21)/2 = 4.7913 — a dyadic band
is a factor 2 — share at most one modulus per dyadic window. So over Z, on the
configuration the hypotheses actually quantify over, **G′ ≤ 1 is proved for all
X**, matching the Gaussian bound exactly. The K_{s,2} orbits and the free-cofactor
Gram 2 are real and are simply out of range: the witness 4-cycle needs
n₂/n₁ = 60.5. Bounded is all the argument uses, so nothing downstream changes;
what remains `inferred` in `gaussian-to-rational-bridge` is the reading of their
quantifier, and no longer a discrepancy between the two rings or a floor from a
finite sweep.

**And it was never about x² + 1.** For A = {f(x)} with deg f = d, α = 1/d and
κ = X^{2−d}, so κ > 1 only at d = 1. No single-variable polynomial of degree ≥ 2
has an admissible Ford–Maynard triple, and d = 1 — Dirichlet — is the only
single-variable degree with anything for a bilinear form to cancel. x² + 1 is
the least degenerate member of a degenerate class. [Note L](note-L-over-Z.md).

## The plan's checkpoints cannot close as worded, and that is a finding

*The charter is not edited by work (CLAUDE.md), so this is recorded here rather
than there. Both checkpoints name a vehicle the work has since shown is
unavailable.*

**§1.5** asks for "a precise bilinear inequality … whose proof would imply the
theorem **via the asymptotic sieve**." The inequality exists — it is
[Note F](note-F-failure-localisation.md)'s Question F, with ranges and a target
saving. But [ASP] does not apply to this sequence: (R1) needs D > x^{2/3} and
Note B caps the level at x^{1/2}, so the admissible range for D is empty
(`asp-inapplicable`, proved, and computed by
`x2plus1.exponents.asp_applies`, which raises). The clause "via the asymptotic
sieve" cannot be satisfied by anything.

**§2.5** asks for "a clean conjectural inequality over Z[i] (**an estimate for a
specific sum of Kloosterman sums or spectral coefficients**) that implies the
theorem, together with a quantitative statement of how far current bounds fall
short." The second half is delivered — [Note G](note-G-spectral.md) has it, as
two incommensurable units. The first half names Kloosterman sums, and Note F
proves there are none to estimate: G(n₁,n₂) is identically 0 or 1, so dispersion
produces no exponential sum at all. Note G's own premise had to be corrected
once for the same reason.

**So the honest status is: the deliverables exist and the success criteria do
not fit them.** Both criteria presuppose machinery this repo has since shown
does not reach x² + 1 — which is, in a sense, the project's result, arriving in
the form of its own checkpoints becoming unmeetable. Amending the plan is the
user's call, not the work's.

Every note carries an **Adversarial review** section, per plan §Cross-cutting.
Do not mark a note `draft` without filling it in.

Normalisation, once, for all notes: **Q** is the norm bound (the sieve's `n ≤ Q`),
**X = √Q**, and |A| = X for the x²+1 sequence.
