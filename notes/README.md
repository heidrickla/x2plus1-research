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

Note C is filled in from the sources and sets the frame for everything else.

**The asymptotic sieve for primes, as stated, does not apply to x² + 1**:
hypothesis (R1) needs a level of distribution D > x^{2/3}, and Note B proves
this sequence caps at x^{1/2}. **But (R1) is the negotiable hypothesis** —
Heath-Brown hit it at α = 2/3, judged it likely relaxable, and wrote his own
sieve instead (HB p. 3). What survives any change of sieve is Note F's
C₄-free lemma, a theorem about the sequence itself.

So the Step 2 notes (E, F, G, H) are **not** downstream of a dead end. An
earlier revision of Note C said they were; that was corrected once Heath-Brown
was read. The distinction to keep hold of:

| | binds for | hardness |
|---|---|---|
| (R1): D > x^{2/3} | [ASP] specifically | soft — precedent for relaxing it |
| κ = \|A\|²/x > 1 | the problem | hard — Note F is a theorem |

**Checkpoints.** Step 1 closes when Note C states a precise bilinear inequality
whose proof implies the theorem (plan §1.5). Step 2 closes when Notes F and G
together give a clean conjectural inequality over Z[i] plus a quantitative
statement of how far current bounds fall short (plan §2.5).

Every note carries an **Adversarial review** section, per plan §Cross-cutting.
Do not mark a note `draft` without filling it in.

Normalisation, once, for all notes: **Q** is the norm bound (the sieve's `n ≤ Q`),
**X = √Q**, and |A| = X for the x²+1 sequence.
