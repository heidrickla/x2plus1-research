# Notes

The deliverables named in the plan. Status is honest: `draft` means the
mathematics is written and machine-checked where checkable; `skeleton` means
the structure is in place and the content is not.

| note | title | plan ref | status |
|---|---|---|---|
| [A](note-A-dictionary.md) | Dictionary — x²+1 over Z[i] | §1.3.1 | draft |
| [B](note-B-type-I.md) | Type I computation | §1.3.2 | draft — **the binding constraint** |
| [C](note-C-requirements.md) | Requirements table | §1.3.3 | **filled and answered** |
| [D](note-D-comparison-ledger.md) | Comparison ledger vs a²+b⁴ | §1.3.4 | draft |
| [E](note-E-naive-dispersion.md) | Naïve dispersion run | §2.4.1 | partial — downstream of C |
| [F](note-F-failure-localisation.md) | Failure localisation | §2.4.2 | draft — downstream of C |
| [G](note-G-spectral.md) | Spectral attempt | §2.4.3 | skeleton — **deprioritised by C** |
| [H](note-H-numerical-pilot.md) | Numerical pilot | §2.4.4 | draft — conclusion corrected by C |
| [I](note-I-a2b4-replay.md) | a²+b⁴ replay | §2.4.5 | partial |

## Read Note C first

Note C is now answered, and it reorders everything else. Friedlander–Iwaniec's
hypothesis (R1) requires a level of distribution D > x^{2/3}; Note B proves this
sequence caps at D ≤ x^{1/2}. **The asymptotic sieve for primes does not apply
to x² + 1, and the obstruction is Type I, not Type II.**

So the Step 2 notes (E, F, G, H) analyse a hypothesis that is not the binding
one. Their content stands — Note F's C₄-free lemma is correct and is still the
right localisation of the *bilinear* failure — but the programme's live question
has moved to:

> **Is there a version of the asymptotic sieve for primes valid for sequences
> with A(x) ≍ x^{1/2}?** Equivalently: where in [ASP] §§3–8 is x^{2/3} spent?

**Checkpoints.** Step 1 closes when Note C states a precise bilinear inequality
whose proof implies the theorem (plan §1.5). Step 2 closes when Notes F and G
together give a clean conjectural inequality over Z[i] plus a quantitative
statement of how far current bounds fall short (plan §2.5).

Every note carries an **Adversarial review** section, per plan §Cross-cutting.
Do not mark a note `draft` without filling it in.

Normalisation, once, for all notes: **Q** is the norm bound (the sieve's `n ≤ Q`),
**X = √Q**, and |A| = X for the x²+1 sequence.
