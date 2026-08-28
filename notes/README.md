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
| [G](note-G-spectral.md) | Spectral attempt | §2.4.3 | skeleton — see below |
| [H](note-H-numerical-pilot.md) | Numerical pilot | §2.4.4 | draft |
| [I](note-I-a2b4-replay.md) | a²+b⁴ replay | §2.4.5 | draft — harness calibrated |
| [J](note-J-mobius-in-progressions.md) | Möbius in progressions | *added* | draft — names the missing input, and localises the difficulty to the absolute values |
| [K](note-K-merikoski.md) | Merikoski's a²+(b²+1)² | *added* | draft — the fourth published sequence; κ is necessary, not sufficient |
| [L](note-L-over-Z.md) | The same question over Z, and over every degree | *added* | draft — Note F's scope, and the degree ladder |

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
Gaussian one — it has 4-cycles, with max Gram 2 rather than 1. Bounded is all
the argument uses, so nothing downstream changes; but the transfer is
`inferred`, not proved, and it is now a registry entry
(`gaussian-to-rational-bridge`) rather than an invisible step.

**And it was never about x² + 1.** For A = {f(x)} with deg f = d, α = 1/d and
κ = X^{2−d}, so κ > 1 only at d = 1. No single-variable polynomial of degree ≥ 2
has an admissible Ford–Maynard triple, and d = 1 — Dirichlet — is the only
single-variable degree with anything for a bilinear form to cancel. x² + 1 is
the least degenerate member of a degenerate class. [Note L](note-L-over-Z.md).

**Checkpoints.** Step 1 closes when Note C states a precise bilinear inequality
whose proof implies the theorem (plan §1.5). Step 2 closes when Notes F and G
together give a clean conjectural inequality over Z[i] plus a quantitative
statement of how far current bounds fall short (plan §2.5).

Every note carries an **Adversarial review** section, per plan §Cross-cutting.
Do not mark a note `draft` without filling it in.

Normalisation, once, for all notes: **Q** is the norm bound (the sieve's `n ≤ Q`),
**X = √Q**, and |A| = X for the x²+1 sequence.
