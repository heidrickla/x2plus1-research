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

**Checkpoints.** Step 1 closes when Note C states a precise bilinear inequality
whose proof implies the theorem (plan §1.5). Step 2 closes when Notes F and G
together give a clean conjectural inequality over Z[i] plus a quantitative
statement of how far current bounds fall short (plan §2.5).

Every note carries an **Adversarial review** section, per plan §Cross-cutting.
Do not mark a note `draft` without filling it in.

Normalisation, once, for all notes: **Q** is the norm bound (the sieve's `n ≤ Q`),
**X = √Q**, and |A| = X for the x²+1 sequence.
