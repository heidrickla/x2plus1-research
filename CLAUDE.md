# x2plus1-research

| | |
|---|---|
| Problem | Landau's fourth: infinitely many primes x²+1 |
| Method | Friedlander–Iwaniec asymptotic sieve, reformulated over Z[i] |
| Output | `notes/` — code exists to keep the notes honest |
| Charter | `x2plus1-research-plan.md` — **Steps 1–2 are done** (obstruction located, structural). **Step 3 is live**: the bipartite Diophantine problem |
| State | `research_state/claims.json` |

## Run

    python -m pytest -q                 # before trusting any measurement
    python tools/smoke_experiments.py   # after changing x2plus1/ — all experiments, small
    python tools/check_sources.py       # which source PDFs are scans
    python experiments/expNN_*.py [size]  # each takes a size, prints a table, gitignored

## State

Statuses enforced by `tests/test_claims.py`. Read the registry before writing a
finding; this table is a summary of it, not a second copy.

| | |
|---|---|
| Obstruction | Type II, not level. Note F: G(n₁,n₂) = #{m : mn₁,mn₂ ∈ A} ≤ 1 over Z[i] |
| Over Z | Thm O.12: G′ ≤ 1 for cofactor ratio < (5+√21)/2 = 4.7913, so on any dyadic band |
| — improved | \|V\| ≥ 2 is unconditional, so the same argument gives < 7+4√3 = 13.9282 at X₁ = 1 and < (1+√2)⁴ = 33.9706 asymptotically |
| Consequence | no bilinear cancellation at any split; C⁻ = 0 via Selberg ν = 0 ([FM] p.2, Thm 2.1) |
| Type I | available at D = x^{1/2−ε}; never the obstruction |
| Density | α = 1/2, κ = 1; no admissible [FM] (γ,θ,ν) triple |
| Degree | α = 1/d, κ = X^{2−d}: no single-variable polynomial of degree ≥ 2 has one |
| Sharpness | proved bound (1+√2)⁴ = 33.9706 vs realised extremum 34.0811 at (37,1261) — **attained to 0.33%** |
| Open | Conjecture O.2 — no window holds three shared moduli. No counterexample to X = 8000 |
| O.2 threshold | O.15: a windowed triple needs u > 82.5571 (117.4171 if a,b both odd), from O.5 forcing V ≠ W |
| Weakest link | `gaussian-to-rational-bridge` (inferred): the Z[i]→Z transfer |
| ⚠ Note O | is **BD₂(−1)**, bipartite Diophantine tuples (am−1, bm−1 squares). Tsang–Yip arXiv:2512.03441 Q1.3: *"when k = 2, we do not know any upper bound on ℓ"* — **open**, conjecturally ℓ ≤ 5 |
| — measured here | ℓ = 3, **exhaustively**: every K₃,₃ contains a pair sharing ≥3 moduli, and all 218 such pairs at X = 9000 fail to extend. \|A\|=2 is unbounded. Measured, not proved |
| — the citable form | O.12+O.13 in their variables: (A,B) with BD₂(−1), x<y, z<w — **if w/z < 2 then y/x > (1+√2)⁴ = 33.9706**. A *joint* ratio constraint; their Lemma 2.1 is **vacuous** at k = 2 (gives yw ≥ xz). See `note-Q-dictionary.md` |
| — and the sets coincide | a is BD₂(−1)-admissible ⟺ a is a cofactor of some x²+1, so the O-thread is about BD₂(−1) **generally** |
| — cutoff is sharp | 96 of 160 qualifying pairs reach K₃,₂, 64 reach K₃,₁, **none** reaches K₃,₃ — an obstruction, not sparsity. Unit-free K₃,₂ exists: {2,10,14365}×{5,1513} |
| — side constraint | all even elements lie on one side (ab−1 square ⟹ ab ≢ 0 mod 4), 0 violations in 35,350 incidences |

Ruled out by the plan: Green–Tao / nilsequences; GRH or zero-density substitutes for
Type II.

## Status vocabulary

| status | requires | means |
|---|---|---|
| `proved` | `proof_site`: a note **and** a test | proved here |
| `quoted` | `citation` with page/result locator | verbatim from a source |
| `rigorous_finite` | `experiment` naming the script | exact over a stated finite range |
| `extrapolated` | `experiment` + `notes` | a law fitted from finite data |
| `inferred` | `notes` saying what is missing | reasoning, not reading or proof |
| `hypothesis` | — | proposed; screen against no-go rules |
| `refuted` | `superseded_by` | kept so it cannot be re-asserted |

Screen a route before proposing it: `from x2plus1.claims import screen; screen("...")`.
No-go rules match wording as well as tags. `green-tao-excluded` is non-fatal: contested
by Green–Sawhney, so re-argue rather than obey.

## Rules

Evidence for each: `notes/note-P-method.md`.

### Inference

- A result much better than the problem is hard: attack it before using it.
- Before believing a sweep, ask what its output would look like if the finding were
  absent. If the same, it measured nothing.
- Name the population before reading the number. Coverage over classes that cannot host
  the configuration is vacuous; >90% coverage of an open problem means the denominator
  is wrong.
- Prefer the property to the comparison. A sweep emits comparisons, a derivation emits
  properties; the property is usually stronger and looks weaker.
- Quote a percentage with its direction of travel — flat and falling are different
  objects.
- A bounded search's clean pattern licenses nothing outside the bound, and never
  licenses retiring a caution.
- Two negatives from restricted views are one piece of evidence if they share the
  restriction. Ask whether any of them ranges over what the claim ranges over.
- Extend the axis nobody extended: a sweep stopping at c = 5 or D = 10 looks identical
  whether the property is universal or holds on an initial segment.
- If the values reproduce but no law does, record the values — `rigorous_finite`, not
  `extrapolated`.
- Reproducibility is not aboutness: a statistic can be stable and measure another object.
- A control is not a classifier. Two points show an argument does not prove too much;
  they do not define a population.
- Do not round a nearly-zero gap to zero because the sentence wants it.
- Before asking whether a gap is real, ask what depends on it — often nothing.

### Verification

- Duplicated computation on independent axes is the only safeguard that works
  unattended. Overlap the computations, not the reviews; disagreement is the alarm.
- A guard that is not on the path is not a guard — and it can be on the path and
  still be invoked in a mode that has no verdict.
- A guard is not verified until it has failed on an injected violation.
- Every way a check has failed here was silent: it could not fail; it checked a weaker
  proposition than its name; it skipped and returned success; its pattern was too
  permissive; it had a mode with no verdict; it compared floats at an exact boundary.
- A false alarm is self-limiting, a false clean bill self-reinforcing. Too permissive
  fails silently; too specific fails loudly, and on a shared file reads as an accusation.
- Decide boundary cases symbolically: equivalent expressions straddle a strict
  comparison exactly where the answer changes.
- A claim's `experiment` must name something that reproduces its numbers. Run it and
  find the number in the output.
- Tests protect the computation, not the paraphrase.
- Verify landed text with a token that cannot wrap — a number or identifier, never a
  sentence. Prose here is hard-wrapped at ~79 columns.

### Sources

- Never assert a literature exponent from memory. Quote with a page reference, or mark
  the claim `inferred` and say what is missing.
- Pull the paragraph, not the clause.
- Re-read the quoted sentence, not the claim about it: paraphrases drift toward whatever
  makes the local argument work.
- Rasterise scans, do not extract. `DFI-equidistribution.pdf` is the only scan; its OCR
  renders prose correctly and mangles displayed mathematics.
  `pymupdf.open(pdf)[idx].get_pixmap(dpi=300)`; DFI page index n is article page n+422.
- When a recorded number does not reproduce, read the paragraph it sits in before
  looking for a bug.
- Consistency and silence look identical from a grep. Before calling a cross-note
  observation new, grep for the claim, not its negation.
- After correcting a value, grep everywhere for the old one — and for the retracted
  *claim*, not only the number. A shed caveat over-claims; a shed retraction leaves a
  false sentence standing.
- A correctly-applied hedge on a withdrawn premise reads as due caution and is not.
- A correction that reaches only a claim's `notes` has not landed.

### Shared files and commits

- Gate the commit in one shell, chained:
  `python tools/check_claims_diff.py <ids> && python tools/check_prose_diff.py <file> "<phrase>" && git commit -F - -- <paths>`
- Always pass the phrases: a gate invoked in its reporting mode cannot refuse.
- Never pipe a check into the gate — a pipeline's status is the last command's. Use
  `RC=$?` or `set -o pipefail`.
- Every string edit asserts its anchor; a silent no-op reports success.
- One edit per script block: a later `replace` masks an earlier failure.
- Commit with a pathspec, options before `--`. It isolates files, not authors.
- On a file two sessions edit, the danger is your own stale copy. Re-read immediately
  before writing, and read the diff's **deletions**.
- Use the session scratchpad, never `$TMP` — it is shared between sessions.
- A claim that exists only in a cross-session message has been checked by nothing.

### Domain

- Normalisation: Q (or N) = norm bound; X = √Q = range of x; |A| = X. State which one
  every exponent is relative to. "Level N^{1/2}" = "level X".
- The invariant is **M·D**: a·m = X²+D and b·m = Y²+D give aY² − bX² = M·D. Every Note O
  formula written with M is its D = 1 form. `notes/note-O-tau-multiplier.md` carries a
  table of which downstream formulas take the D; check it before reusing one at D ≠ 1.
- Note L's ε (automorph) moves within an orbit; Note O's τ (multiplier) moves between
  orbits. At (1,41): ε² = 1.679×10⁷ against τ₁² = 1.877.
- The modulus ratio is τ², not τ. A window is **ratio < 2**, never a power-of-two-anchored
  interval — [8,16) and [16,32) between them miss (9,17).
- Distinguish adversarial β from β = μ: `typeII.worst_case_signs` vs
  `typeII.mobius_bilinear`.
- Generate candidates from the realised side: enumerate occupied configurations and read
  off which multiplier explains them, never the reverse.
- Place finished results recorded by *different arguments* side by side. Redundancy
  detects; adjacency generates.

## Code conventions

- Exact integer arithmetic in Z[i] — int pairs, never `complex`. Floats appear only in
  reported statistics.
- Ideals are named by their unit-normalised generator (`unit_normalize`: Re > 0, Im ≥ 0).
  Never key a dict on a non-normalised Gaussian integer.
- Bulk work goes through the progression sieve in `factorization.py`, not per-value
  `factorint`. Divisibility in this sequence *is* a congruence.
- New numerically-checkable claims get a test in `tests/test_arithmetic_facts.py`.
- No scipy. `typeII.Sparse` is a hand-rolled CSR; keep the dependencies at sympy + numpy.
- Write the convention where the symbol is defined.
