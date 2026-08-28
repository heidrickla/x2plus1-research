# Note P — how this repo has gone wrong, in detail

CLAUDE.md carries these as one-line rules, because it is read in full at every
session start and prose there is not read. This note is the evidence behind them:
what actually happened, what the numbers were, and what did and did not catch it.

Read it when a rule in CLAUDE.md looks arbitrary, when you are about to argue with
one, or when you want the failure mode rather than the instruction. Every entry
below was written at the time by the session that made the error.

Provenance: this was CLAUDE.md's "Non-negotiables" section (8,929 words) until
CLAUDE.md was cut to rules and facts. Nothing here is new; nothing was lost.

---

## The rules, with their evidence

- **Normalisation.** Q (or N) = norm bound; X = √Q = range of x; |A| = X.
  State which one every exponent is relative to. "Level N^{1/2}" = "level X".
- **A result much better than the problem is hard should be attacked before it
  is used.** A three-hour-old lemma gave `3ab < b − a`, impossible for a ≥ 1, so
  Conjecture O.2 was closed in one line. It was not: the lemma's conclusion holds
  *per prime*, the ordering that selects the pair depends on the prime, and only
  the three-term product is uniform. **5 of 216 realised triples witness the
  failure** — but 211 do not, so the pattern was 97.7% supportive and no number
  came out wrong. It was caught by asking what the quantifier ranges over, before
  running anything.
  This is the same detector as the vacuous denominator, one level up: *99.26%
  coverage of an open problem*, and *a one-line proof of the open conjecture*,
  are both implausible on their face, and implausible-on-its-face is checkable
  without knowing any of the mathematics. **When a step is suddenly much stronger
  than the difficulty of the thing it settles, that is the moment to look for the
  quantifier, not the moment to write it up.** Arithmetic will not catch this
  class: every number involved can be correct.
  **But be honest about how narrow that detector is.** It did not fire because
  anyone was careful. It fired because `3ab < b − a` is *impossible*, visible by
  inspection at a = 1. Had the same bad reduction yielded `3ab < M^{2/3}` —
  still far stronger than the real bound, still wrong — nothing would have fired
  and it would have shipped. So the rule is **"the conclusion is too strong to be
  true"**, not "check the quantifiers", and it only works when the over-reach
  breaks something obvious. Between *suspiciously good* and *correct* there is a
  band where no self-check fires at all, and that band is where the Plücker
  constant lived for hours. **In that band a second independent derivation is the
  only detector there is** — which is the argument for overlapping the notes at
  the load-bearing identities rather than partitioning them cleanly. A percentage
  also has to carry its **direction of travel**: a proved bound whose measured
  reach is *falling* with X (O.11: 97.7% → 88.1%, admissible count doubling per
  doubling of X) is a different object from one that is flat (O.10: ~35%), and
  "6.85× better" alone tells a reader the opposite of what the data says.

- **Before believing a sweep's headline, ask what its output would look like if
  the finding were absent. If that looks the same, the sweep measured nothing.**
  (The parallel session's formulation.) This is *one* rule and it arrived wearing
  a different statistic each time — percentage, population, extremum, axis — which
  is why restating it more clearly never helped and why it fired repeatedly after
  being written down. **The operational form is a question, not a principle:
  *which set does the claim range over, and is that the set I computed?*** — asked
  out loud, before the number is read. Every instance below produced a correct
  number and an unlicensed inference:

  - *Vacuous denominator.* "95.68% of classes excluded" and "99.2% excluded" read
    the same whether a theorem is strong or **1,815,094 of 1,815,154 classes have
    fewer than three moduli and cannot host the configuration**. On the 60 that
    can, the figures are 15% and 54.5%.
  - *Consistency vs silence.* A grep for contradictions returns nothing whether
    both notes agree or only one speaks — so agreement was read as neither having
    said it, when Note L had.
  - *Absent base rate.* 27-of-28 uncited claims reads the same whether the notes
    are negligent or id-citation is simply not the convention (it is not — 20%).
  - *Missing direction of travel.* A bound at ~35% that is **flat** in X and one
    at 97.7% → 88.1% that is **falling** are different objects; "6.85× better"
    tells a reader the opposite of what the data says about the limit.
  - *A column of zeros.* Empty at a ≥ 2 looks the same whether it is a law or a
    range the sweep cannot reach — largest available b was 8321 against a 7×10⁴
    crossover.
  - *Fixed windows across sequences.* x²+c² on [64,256) gives max Gram
    2,3,3,3,4,5,6 across c — "the gap widens with c" — and normalised to each
    sequence's own √Q it is **2 throughout**: the window was varying, not the
    sequence.
  - *Extremum where the worst case was needed.* max ε was exactly c² and would
    have restored a threshold; **min ε was 10⁻⁸** and restores nothing.
  - *The loop's natural population.* An X-loop counts moduli, so it reports the
    mean over all bands when the informative statistic lives in one band; the
    informative subset is never the one the loop naturally counts.
  - *The unextended axis.* A sweep stopping at c = 5 or D = 10 looks identical
    whether the property is universal or holds on a short initial segment. Both
    were checked at five or six values and read as general; both failed at the
    next one.
- **A comparison feels like a finding; a property feels like a restatement — and
  the property is usually the stronger result.** "The mean drops below the
  barrier's line" reads as a discovery. "The count is a 0/1 indicator, so an
  error term better than O(1) means knowing it exactly" reads as a restatement,
  because Note F had said it for Z[i] already. The second is strictly stronger —
  pointwise rather than on average, and immune to the objection that sinks the
  first ("your band holds two cofactors"). **The stronger result looked like the
  smaller one**, and the weaker one was nearly published instead. Same asymmetry
  that let the Plücker constant survive: a right-*shaped* sentence beats a right
  statement. When a comparison and a property are both available, suspect the
  comparison. **And note where each comes from: a sweep emits comparisons, a
  derivation emits properties.** The tooling biases toward the weaker form, which
  is an argument for deriving before measuring — the reverse of the order most of
  this repo's findings were produced in. It also explains the other survivors:
  "the mean is U-shaped", "κ crosses 1 where C₄-freeness does", and the Plücker
  constant are each a *relation between two numbers* standing in for a
  *statement about one object*, and each time the relation was the weaker claim.
  **And a derivation that predicts falsely still establishes something a sweep
  cannot.** Generalising O.12 to x²+c² gives V·W = c²·M·(m_i − m_j), hence a
  bound weaker by c², hence a threshold below what a dyadic band supplies at
  c ≥ 2 — predicting O.12 fails there. It does not: banded cofactors still share
  at most one in-window modulus at c = 2, 3. The prediction was wrong and the
  derivation was not wasted, because what it established is **which step uses
  c = 1 essentially**: the *argument* is special to x²+1, the *fact* is not known
  to be. A sweep would have shown max Gram 1 for every c and read as "O.12
  generalises", which is exactly what is not established. Measurement offers the
  comparison; derivation supplies the property; **and here the measurement was
  the misleading one.**

- **The anchored-window defect was systematic across this repo's sweeps and
  changed no conclusion — and fixing it made one conclusion stronger.** Found in
  three independent places: `exp09`'s degree ladder, Note O's extremal-ratio
  measurement (where it corrupted a *value*, 43.79 for the true 34.0811), and
  `exp20`'s mean-G decay — the measurement the entire Type II argument rests on.
  In every case the conclusion survived. In the last it **improved**: every
  anchored mean is *higher* than the ratio mean, over roughly a third of the
  population, so `the-main-term-is-smaller-than-the-granularity` is better
  supported by the faithful quantification (0.0213 at N = 2048) than by the
  figures the repo had recorded (0.0243). **A defect whose repair strengthens the
  result is the rarest kind here** — every other one tonight cost something — and
  it is evidence the conclusions were not resting on the anchoring. **The
  systematic-ness is the finding**: one wording defect, reproduced independently
  in three sweeps years apart in style, because "dyadic band" reads as an
  interval when it means a ratio. And note where the repair had to land: putting
  the faithful numbers in a claim's `notes` while its `statement` still led with
  the anchored ones is the same half-correction this file already warns about.

- **Two sessions on one machine collide below every guard you build.** All three
  hazards found tonight sit *underneath* the pathspec, the claims gate and the
  prose gate, because each happens before or outside git.

  - ***Shared temp.*** `/tmp`, `$TMP` and `%TEMP%` all resolve to the same user
    directory here. A commit message written to `$TMP/msg.txt` by one session was
    picked up by the other's `git commit -F`, filing **59 lines of Note O under an
    unrelated title**; six files from three *further* sessions were sitting in the
    same directory. Use the session scratchpad named in the system prompt — for
    message files, for background-job output, for everything. The countermeasure
    at this layer is **content addressing, not path trust: a hash survives a
    shared path, a filename does not.**
  - ***Shared files.*** `git commit -- <path>` scopes what git commits but cannot
    separate two authors inside one file. Five times a paragraph from one session
    landed in the other's commit; `4f3e99a` is titled "two rules" and adds
    **three** bullets. `tools/check_claims_diff.py` fixes this where there are
    ids; `tools/check_prose_diff.py` covers `- **…**` headings; **neither sees an
    edit that extends an existing paragraph**, which is the case that still gets
    through.
  - ***Your own stale copy.*** A read-modify-write race: a script read
    CLAUDE.md, a 55-second test run followed, the other session committed a
    rewrite of that region inside the window, and the write put the stale copy
    back — dropping ~50 lines. **No staging discipline can see this**, because
    `git diff --cached` shows exactly what you meant to write. The only signal was
    **91 deletions against a 20-line addition**, printed in output nobody reads.
    **Re-read immediately before writing, and read the diff's deletion count.**
  - ***The message channel.*** Nothing checks it, and twice a message carried a
    **stronger claim than the artefact it described** — both times the committed
    artefact was correct. Do not gate it: the exchange *is* the
    duplicated-computation detector, and four errors tonight were caught because
    a claim was stated and then independently computed. **State the claim id and
    let the reader check the artefact**, and remember that *a claim existing only
    in a message has been checked by nothing.*

  **Three mechanisms on one file, each invisible to the guard built for the
  previous one**: a pathspec cannot separate two authors, a diff-check cannot see
  a stale read, and a gate could be invoked in a mode with no verdict. All three
  are fixed and **none of the fixes would have caught the other two** — which is
  the argument for treating a shared file as hostile rather than for adding a
  fourth guard.

- **How a check fails, and every way found here was silent.** A guard that
  reports nothing is the default failure; not one of the six below produced a
  false alarm on its own defect.

  - ***It cannot fail.*** The baseline: **a guard is not verified until it has
    failed on an injected violation.** A note-citation regex here skipped 26 of
    103 ids — including the refuted claim it was being tested with — and passed.
  - ***It checks a weaker proposition than its name.*** `exp09` sweeps windows
    **anchored at powers of two** while its claim says *every* dyadic window;
    [8,16) and [16,32) between them miss (9,17), which is how a line-family sweep
    reported the property *holding* at c = 6 on the witness that refutes it.
    Neither injected violation nor an enumeration floor reaches this — the sweep
    can fail, and covers a large population. **The countermeasure is a wording
    check: does the experiment quantify over the same set the statement does?**
    Found in three sweeps, and **every conclusion survived** — at `exp20` the
    faithful reading is *lower* at every scale (1.7500, 0.6562, 0.2429, 0.0799,
    0.0213 against 2.0000, 0.6667, 0.2536, 0.0865, 0.0243) over three times the
    population, so fixing it **strengthened** the result.
  - ***It skips.*** `tools/smoke_experiments.py` printed `SKIP -- no size
    recorded`, counted it, and **returned success**, so `exp25` was not run at all
    while the run reported fine. **Any check with a "not applicable" branch has a
    silent-success path by construction.**
  - ***Its pattern is too permissive.*** `re.search("M*D", …)` means *zero-or-more
    M then D* and matches every `D` in the file; a floor detector could not see
    `assert len(x) > N`, the idiomatic form of the thing it hunted. **A pattern
    too permissive matches more and reports less**, so its failures fall on the
    silent side — which is why all four audit-hunting-its-own-defect instances
    gave a clean bill and none gave an alarm. **A false alarm is self-limiting**
    (investigating costs you and you stop); **a false clean bill is
    self-reinforcing** — it retires the question and the next reader inherits
    "already checked". *(Too **specific** fails the other way and is the safe
    direction: a detector keyed to one phrasing produced 11-of-34 and 27-of-28
    alarms, all investigated, all wrong.)*
  - ***It has a mode with no verdict.*** `check_prose_diff.py CLAUDE.md` with no
    phrases was a reporting convenience: it printed the added bullet by name,
    said "bullets added: 1", and **exited 0**. Invoked that way it let a
    collision through while displaying it on screen. **A gate with a mode that
    cannot refuse is a gate you disarm by accident** — this is "a guard not on
    the path" with the guard *on* the path and called in the wrong mode. Now the
    bare call **refuses** when anything was added; reporting needs an explicit
    `--list`. Verified in all four modes before use.
  - ***It compares floats at an exact boundary.*** Whether a band's u < 2 attains
    (u−1)/√u = 1/√2 decides which D are covered. It does not — u < 2 is
    **strict** — so D = 8, where the threshold is exactly 1/√2, is the last
    *covered* value. But `u0(8)` evaluates to **1.9999999998**, so a bare `< 2`
    check calls it uncovered: printed number right, comparison right, answer off
    by one value. **At a boundary reason from the identity, not the float.**
- **Duplicated computation is the only safeguard here that works while nobody is
  paying attention.** Every other countermeasure in this file requires someone to
  remember to apply it, and the record shows all of them being written down and
  then broken by their own authors within the hour — the `&&` that could not gate
  because of a pipe, the enumeration floor missing from a test written after the
  floor rule, the vacuous denominator, the quantifier question, the informative
  subset three times on one claim. **What actually caught the two largest errors
  was two sessions computing the same thing on different axes and getting
  different answers.** Neither was reviewing the other. Nobody had to be
  vigilant: the disagreement did the work by existing. That is a property of the
  arrangement rather than a practice, and it is the argument for **overlapping
  the computations, not the reviews** — redundancy at the identities *and* at the
  sweeps, on different axes, with disagreement as the alarm. Three of tonight's
  findings arrived this way, including both that reframed the O-thread.
  **And the reason is a mechanism, not a preference.** A checklist item costs
  attention *every* time and pays only when it fires, so its expected value falls
  as vigilance decays — which is why every rule in this file was broken by its own
  author within an hour of being written. An axis extension costs attention once
  and **raises the probability of the next one**, because the payoff is itself the
  motivation. **The countermeasure that works unattended is the one whose success
  makes it more likely to be repeated.** Nobody had to be reminded to extend the D
  axis a second and third time; the second happened because the first had paid.

- **Two negatives from two restricted views are not two pieces of evidence if
  they share the restriction.** The D axis was nearly retired as an artefact on
  the strength of two independent-looking measurements: the singly-windowed
  cofactor Gram is **flat in D**, and the canonical incidence with its default
  cofactor floor gives **max G = 1 for every D**. Both correct, both computed
  separately, and both agreeing — and neither is the Type II shape, because each
  restricts a different *single* variable while the hypothesis bands **both**.
  Requiring cofactors ≥ 200 **and** moduli ≥ 200 finds four D that still fail, at
  cofactor ratios 1.27–1.71 and modulus ratios 1.28–1.92. **Agreement between two
  restricted views is evidence about the restriction, not about the question.**
  **And this is the one failure mode neither of the two working detectors
  reaches.** Duplicated computation does not help when both computations inherit
  the same restriction — they agree, correctly, about the wrong thing. A wording
  check does not fire either, because *both descriptions were accurate*: the
  singly-windowed Gram **is** flat in D, and the default cofactor floor **does**
  give max G = 1. Nothing was misstated and nothing disagreed. **The only thing
  that settled it was asking what configuration the claim is about** — cofactors
  and moduli *both* large — and measuring that, which found four D still
  failing.
  The check is not "did another measurement agree" but "does any of them range
  over what the claim ranges over".

- **A bounded search that finds a clean pattern is the most persuasive way to
  talk yourself out of a caution you had already got right.** The other session
  searched cofactors ≤ 300 and found every failure witness below cofactor 9 —
  D = 11 at (3,4), D = 14 at (3,5), D = 19 at (4,5), D = 39 at (5,8) — concluded
  that failures announce themselves at tiny cofactors, and on that basis
  **downgraded its own earlier warning** that the surviving D might simply be
  under-swept. The warning was correct: D = 35's witness is at **(2249, 3756)**,
  three orders of magnitude outside the search that "established" the pattern.
  **A bound's silence is not evidence about what lies outside it** — and the
  damage was not the wrong pattern but the retracted caution, which had been
  right before the evidence arrived. When a bounded search produces a clean law,
  the first question is what the bound excludes, and the second is whether the
  law is being used to retire a doubt that the search could not have addressed.

- **A wrong identification between two notes' machinery costs more than a wrong
  answer, because it manufactures an apparent contradiction.** Note L's ε and
  Note O's τ act on the same solution set of aY² − bX² = M. Identifying them —
  *"the fundamental multiplier is the fundamental automorph"*, which sounds like
  a definition — produced "two moduli of **one orbit** inside a window", which
  **contradicts Prop L.1** and reads as a defect in it. The natural next move is
  to go looking for the error in Note L, and there is none: ε² = 1.679×10⁷ and
  τ₁² = 1.877, two different objects differing by a factor of 8.95×10⁶. **Every
  other trap here produces a wrong answer; this one produces a wrong
  *retraction*, of something correct, in someone else's work.** What separated
  them was computing *both* quantities on *one* example — the same instrument as
  asking why two derivations of a constant agree, aimed at two pieces of
  machinery instead of two derivations. **When two notes' objects look like the
  same object, evaluate both on one instance before believing it.**

- **A citation to the nearest script you own is invisible to every check but
  running it.** The prose-citation defect (`experiment` naming a sentence) is
  visible in the string and a guard catches it. Its successor is not: **eleven
  claims here cited `exp23` — a real, running, correct experiment — which
  computed none of their numbers.** Every one named it because it was the nearest
  file the author owned, not because it contained anything. **A valid-looking
  citation to a working file passes the guard, passes the eye, and fails only on
  `python experiments/… | grep <the number>`.** Committed eleven times in one
  night against the very file written to fix the earlier version of the same
  defect. When adding a claim, run its cited experiment and find its number in
  the output, or extend the experiment until you can.

- **Put finished results next to each other on purpose.** Four findings tonight
  came from adjacency alone — the τ/ε split, the three-scale gap, |V| ≥ 2
  appearing in both the D family and the line family, and the pair/chain
  thresholds turning out to be one formula. In **every** case both results were
  already correct and already recorded; nothing was discovered by computing
  anything new. That makes it a different and cheaper operation than the
  duplicated computation that catches errors: this one needs a second
  **placement**, not a second run, and the material already exists. It has paid
  four times by accident and three times on demand. **And the productive pairs
  are across halves, not within them**: τ/ε bridged Notes L and O, D against κ
  bridged structure and density, μ against D bridged structure and cancellation.
  The within-half pairs tried — the 43 classes against mean G, θ against D — went
  nowhere. **Place results that were recorded by different arguments, not results
  that are about the same object.**

- **An invariant stated once and used implicitly everywhere gets substituted
  wrongly by everyone.** Both sessions made the *same* M·D error within an hour,
  each after reading the section that states it: the invariant for x²+D is
  aY² − bX² = **M·D**, but every downstream formula in the note is written in its
  D = 1 form, so the surrounding text *looks* like the general case. Theirs was
  in a τ₁² comparison; mine was in the window condition, where the modulus ratio
  (X_j²+D)/(X_i²+D) < 2 gives **R² < 2 + D/X₁²** and I used 2 + 1/X₁². Neither
  was a careless reading — the D = 1 form is what the page trains you on.
  **Where an invariant is defined, say which downstream formulas carry the
  parameter and which are already specialised.** And note the failure signature:
  both errors produced *apparent violations of a correct bound*, which is what
  sent each of us back to the derivation. A wrong invariant that happened to
  produce no violation would still be there.

- **And when a retraction dies in transit it leaves a FALSE sentence standing,
  which a correctly-applied hedge then disguises.** The other session found that
  a *caveat* survives at the site that derives a number and is dropped by every
  site that quotes it — quoting compresses, and the conditional clause is the
  compressible part. The same happens to *retractions*, and there it is worse. The
  D = 4 converse was withdrawn in Note O and in its claim, and CLAUDE.md went on
  asserting *"D = 4's two sub-threshold cycles are non-τ₁, so above ⟺ τ₁
  separates"* for hours — because after that correction the grep run was for the
  **number** (`43.79`) and never for the **claim**. A shed caveat leaves a true
  statement over-claimed; a shed retraction leaves a false one.
  **And the hedge made it harder to see.** That sentence had already been softened
  to "an observation, not a theorem", which is correct about evidence — but the
  thing hedged had *no* evidence, so the hedge was protecting a claim with none
  rather than one with little. **A correctly-applied hedge on a withdrawn premise
  reads as due caution and is its opposite.** The two failures compose: the hedge
  makes the sentence look already handled.
  Removing D = 4 also left *above ⟺ τ₁* with no confirming instance at all — at
  D = 1 and 2 every realised cycle is above threshold, so there is nothing to test
  the converse on. **Untested, not merely unproved**, and the third empty
  antecedent of the night wearing a populated-looking sentence.
  **The operation is: grep for the retracted CLAIM after retracting it, not only
  for the corrected number.** Both sessions ran the number version and missed the
  claim version, on different retractions, the same night.

- **When you correct a recorded value, grep the registry for the old one.** The
  43.79 → 34.0811 correction landed in the claim that made it and not in the
  `proved` claim it corrects, so two live claims asserted different minima for
  the same quantity. `grep -c "43.79" research_state/claims.json` returns **2**
  and would have said so in one line. **The consistency test cannot catch this**:
  it enforces the status ordering on `depends_on` edges and has no way to see two
  claims disagreeing about a number, because nothing links them — `superseded_by`
  is for whole claims and fires only on `refuted`, and there is no vocabulary for
  *a claim that corrects one figure inside another that otherwise stands*. Do not
  add a field for it; grep. Same instrument as **grep for the number before
  deriving it**, aimed at the other end of the operation. **And never grep for your own paraphrase of a field when you
  can read the field.** A check for `'passes unseen'` in a claim's notes reported
  the notes lost; they were present and said `'would pass unseen'`. That produced
  a false loss report sent to the other session and retracted a minute later —
  the grep-for-the-negation error at the smallest possible scale, against text
  written by the same hand ten minutes earlier. **And grep
  *everywhere*, not only where you were working**: running this over the registry
  and this session's own notes found nothing further, and extending it to the
  other session's note found their `τ_V² < 3` premise carrying the same D = 1
  specialisation my window condition had — the third instance of that family in
  an hour, and the one nobody was looking for.

- **Extend the axis nobody extended.** Two results in one night came from the
  same move, and both overturned a conclusion that had been checked at five or
  six values and read as general. The doubly-dyadic C₄-free property was verified
  for x²+c² at c = 1…5 by one session and c = 1,2,3,5,7 by the other; **neither
  ran c = 6**, where it fails. Extending the *next* axis — D in x²+D — produced
  the mechanism: four consecutive arguments give a 4-cycle exactly when
  D = k²+3k+1, x²+1 is the k = 0 member, and its instance is degenerate because
  one of its four values is the unit. **A sweep that stops at c = 5 or D = 10
  looks identical whether the property is universal or holds on a short initial
  segment** — the sweep-headline question applied to the axis rather than to the
  population. Ask which parameter was held fixed because it was never varied, as
  opposed to because varying it was considered and rejected.

- **Before asking whether a gap is real, ask what depends on it.** A hedge was
  found in Ford–Maynard's footnote 2 — "closely related to", not *equivalent to*
  — and read as the residual inference under `gaussian-to-rational-bridge`.
  Settling whether the paper makes the relation precise elsewhere would need a
  re-read the repo cannot do from what it holds. **One registry query settled it
  instead**: `fm-footnote2-is-note-F-G` has exactly one dependent, and
  `selberg-nu-zero-binds` is `quoted` with an empty `depends_on` — ν = 0 comes
  from Selberg via p.2 and Theorem 2.1, so the inference the hedge would block is
  one this repo never makes. The hedge is real, is the source's, and is **off the
  path**. This is what the dependency graph is *for*, and it had not been used
  this way before: **the question "is this gap real?" is often harder than "does
  anything stand on it?", and the second question answers the first whenever the
  answer is nothing.**

- **A summary rounds a nearly-zero quantity to zero, because that is the shape
  the sentence wants.** The three-scale gap has its narrowest instance on the D
  axis — proved reach ends at 4.899, smallest failure at 11, so **D = 5…10 is a
  six-value strip that is permitted to fail and has not**. Summarising, the other
  session wrote the D axis as *"the one place proof and data agree exactly"*: two
  true constituent facts (no failure inside the reach, every failure outside it)
  compressed into a claim that contradicts the very table it was contrasting
  against. **Small became none because "gaps everywhere, except here" is a better
  sentence than "gaps everywhere, smallest here."** Not carelessness — a summary
  is a compression, and a quantity close to a clean value is what compression
  destroys first. *(Recorded as **one** instance. I first wrote it as three,
  reaching for the density table and the vacuous denominator — but those were a
  documented sieve truncation and a wrong denominator respectively, neither of
  them rounding. Three is a better sentence than one, which is the same
  operation.)*

- **A strict comparison at an exact boundary is decided by which algebraically
  equivalent expression you evaluate.** O.12's D-reach turns on whether
  u₀ = 2 at D = 4V. It is exactly 2 (sympy: (u−1)²/u = 1/2 has roots 1/2 and 2),
  but `v = (t+√(t²+4))/2; u = v²` returns **1.9999999999999996** while
  `u = (2+t²+t√(t²+4))/2` returns **2.0** — so a bare `u < 2` reports D = 8 as
  uncovered from one and covered from the other, and the reach is off by one
  value of D. **The trap is not that floats are inexact**; it is that equivalent
  forms diverge *exactly where the comparison is strict*, which is precisely
  where the answer changes. One session read the float and got it wrong; the
  other got it right **by luck**, having picked the exact expression without
  reasoning about it. Decide boundary cases symbolically.

- **Paraphrases of a source drift toward whatever makes the local argument
  work, and only re-reading the sentence catches it.** `fm-barrier-range-is-
  small-moduli` was read — by the other session, quoting it back — as recording
  "mean G ≥ 1" as Ford–Maynard's threshold. Footnote 2, p. 7 asks for *"an error
  term better than O(1) on average over m₁, m₂"*: a condition on the **error
  term**, with no threshold on any mean. The measurement was right, its
  description was right, and the sentence between them had acquired a
  significance the source does not give it. Note F had the correct reading all
  along — the count is 0 or 1, so the error term **is** O(1) and no averaging can
  improve it, which is *pointwise* and strictly stronger than any statement about
  a mean. **Re-read the quoted sentence, not the claim about it**; and note this
  was found by asking *is the number in our claim the number in their paper* —
  the same question that caught the Plücker constant, aimed at a citation.

- **Consistency and silence look identical from a grep.** Notes L and O were
  cross-checked for contradictions about how many moduli a dyadic window can
  hold. They agree — identically so — and that agreement was read as *neither
  note having drawn the connection*, which became a claim, a commit message
  saying "neither note said so", and a message to the other session announcing
  it as new. Note L states it outright, in a section written here, **and states
  it more carefully**: that proving it upgrades one claim's status and changes no
  conclusion. The re-derivation was correct; the novelty and the added
  significance were not. **A search for contradictions cannot find that one side
  already said the thing** — it returns nothing in both cases. Before calling a
  cross-note observation new, grep for the *claim*, not for its negation. This
  hazard is specific to auditing notes at volume, which is exactly when it is
  most likely to fire.

- **When a recorded number does not reproduce, read the paragraph it sits in
  before looking for a bug.** Note M's squarefree densities did not match a fresh
  exact sieve. I proposed inconsistent rounding (a story fitted to two rows that
  happened to land near a rounding of the exact value, and true of neither),
  tested a p ≤ √X cutoff in code, and then — correctly refusing to fit a cause —
  recorded the last row as *unexplained*. It was explained: **"a sieve truncated
  at P = 20 000", three lines above the table**, in the file the claim cites. The
  truncated column reproduces every digit to six places and its stated error bound
  holds, so the numbers were never wrong; my correction was. Refusing to invent a
  cause is the right instinct and is not a substitute for reading. This repo
  already says *pull the paragraph, not the clause* about the literature; it
  applies with more force to its own notes, where the paragraph is three lines
  away. **The failure mode is searching the code for what the prose already says.**
  And note the shape: an approximation with a documented error bound reads exactly
  like an error once the sentence documenting it is out of view — which is the
  same thing `inferred` exists to stop, one level down.

- **And gate prose the same way: `tools/check_prose_diff.py CLAUDE.md "<phrase>"
  ... && git commit`.** The claims gate works because claims have ids; CLAUDE.md
  and the notes have none, so on a file two sessions both edit, a commit message
  can silently under-describe its own diff. That happened three times in one
  session — `4f3e99a` is titled "two rules" and adds **three** bullets, the third
  written by the other session. Nothing was lost either time and the messages
  were wrong. The tool lists every `- **…**` heading the working tree adds and
  refuses if one matches none of the phrases you name. **A pathspec cannot
  separate two authors inside one file; only reading the diff can, and on prose
  neither of us did that reliably.**

- **Gate the claims diff with `tools/check_claims_diff.py <id> ...`, chained.**
  It parses `HEAD` and the working tree, compares claim dicts by id, and exits
  non-zero on anything unnamed. `python tools/check_claims_diff.py <ids> && git
  commit ...` — the `&&` is the whole point; see the shared-file entry below.

- **Never assert a literature exponent from memory.** The hypotheses of the
  Friedlander–Iwaniec asymptotic sieve (Annals 1998; *Opera de Cribro* Ch. 25)
  must be quoted from the source with a page reference. Unverified slots in the
  notes are marked `**[VERIFY]**` and must stay marked until checked against
  the paper. This matters more here than anywhere else in the repo: the whole
  point of Note C is that the *exact* hypothesis is what decides the problem.
- **Distinguish adversarial β from β = μ.** The sieve's Type II hypothesis has
  an absolute value outside the m-sum (so α is effectively arbitrary) but
  supplies β = μ, not an adversary. Conflating them makes the problem look
  impossible when it is merely hard. `typeII.worst_case_signs` is the former,
  `typeII.mobius_bilinear` the latter.
- **Adversarial review of every note** (plan §Cross-cutting): where is
  two-parameter freedom being smuggled in, and where is parity actually broken?
- **Pull the paragraph, not the clause.** When quoting a source, read the whole
  paragraph into the claim's notes, not the sentence you came for. Three findings
  in one session sat one sentence past text this repo had already quoted,
  verified and cited correctly — C⁻ being the *lower-bound* constant (FM p. 2),
  C_bd being a class of *dense* sequences (FM pp. 1, 7, 13, 14), and FM's
  "natural barrier" being *unconditional* at c = 1/2 (footnote 2, p. 7). No guard
  can catch these: the locator is right, the quote is verbatim, the status is
  right. Only reading past the clause finds them. The normalisation convention
  behind the second was inside the very sentence `fm-no-admissible-theta-at-
  density-half` is built on.
- **A claim's `experiment` must name something that reproduces its numbers.**
  Nine of roughly forty claims with an experiment field named a file that
  computed something *adjacent* — seven pointed at `exp13`, which does two-step
  ratios and no mean, diagonal, argmin or cross-sequence table; two pointed at
  `exp16`, which did neither the signed sum nor the Cauchy–Schwarz bound. The
  numbers had come from scratchpad scripts run once and discarded. `tests/
  test_claims.py::test_support_paths_exist` checks the file *exists*, which is
  not the same question. **And writing the experiment is not bookkeeping: both
  times, the rerun at a second size produced something the one-shot script could
  not** — the mean-G classifier's threshold turned out to move with Q, and the
  Cauchy–Schwarz chain turned out to predict at every band rather than one. If a
  number is worth a claim it is worth a script that can be run again at a
  different size.
- **Three readings of "mean G" gave three different orderings of the same five
  sequences.** On x²+D for D = 1, 2, 6, 11, 39: the other session's band-1 figure
  orders them 1 < 2 < 6 < 39 < 11; the canonical **off-diagonal** mean orders
  them 6 < 11 < 2 < 39 < 1; the **diagonal** orders them 1 < 6 < 2 < 11 < 39.
  Each reproduces well on its own terms — the first to under 1% across a band
  change — and they disagree completely. **Reproducibility is not aboutness.**
  A statistic that reproduces is measuring *something* stably; whether it is
  measuring the thing in the claim is a separate question that stability cannot
  answer. This repo already refuted mean G as a captured/uncaptured classifier
  once; the same statistic was available for the same misreading on a new axis,
  and the temptation was **stronger** because it reproduced better.

- **A control is not a classifier.** A control shows an argument does not prove
  too much and needs exactly two points: a²+b⁴ has mean G 3.59 where x²+1 has
  0.022, so the mean-o(1) objection does not rule out dispersion for the sequence
  it demonstrably works on. That is sound. Reading it as *mean G > 1 separates
  captured from uncaptured* is a different claim about a whole population, and it
  was false — x³+2y³ is captured and sits at 0.1888, below the sequence with no
  known outcome. The tell was in the construction: the "law" was built from two
  points and confirmed on two more, one of which had no known outcome, so the real
  confirmation set was **one sequence**. And it generated its own supporting
  evidence — a literature quotation was gathered for a statement already false.
  When testing a proposed classifier, pick the case the incumbent invariant
  *cannot* see (here κ is equal for x³+2y³ and a²+b⁶), not the next case to hand.
- **If the values reproduce but no law does, record the values.** One quantity —
  the mean of G over cofactor bands — took four corrections in one session
  because three different laws were fitted to it and all three failed: 1/N, then
  (log X)/N, then N/X for the left arm of its U. Every time, the *values*
  reproduced exactly between two independent constructions and the *law* did not.
  Some measured quantities here are reproducible and unparameterised, and naming
  a shape for them is a reflex worth suppressing. The tell is that the
  disconfirming number was already in hand each time and got closer each time:
  first a second X was never taken, then a drift was recorded at 5.6 and the law
  quoted anyway, then the counterexample sat two rows apart in the same printed
  table. `rigorous_finite` is the status for values; `extrapolated` is for a
  fitted law and demands the fit be shown to hold.
- **Every string edit asserts its anchor.** A `replace` whose anchor text has
  moved writes back identical content and reports success; `git commit` then says
  "nothing to commit, working tree clean", which is easy to misread as a
  collision with the other session when one has genuinely happened that day. A
  silent no-op is a green result with no work behind it. Same shape as the rule
  below, one level down — and the aggravating factor is that *a plausible
  explanation for the anomaly is what stops you checking the implausible one*.
  Verify by grepping HEAD for the new text, not by trusting the script or the
  git output. **And run `git diff --cached` before every commit.** Explicit-path
  staging was the fix for `git add -A` collisions and is **not sufficient when
  two sessions edit the same file**: `git add CLAUDE.md` sweeps the other
  session's uncommitted CLAUDE.md work exactly as `-A` did. It happened here —
  one session's CLAUDE.md edit failed its anchor assert, the script died, the
  `git add` ran anyway, and the commit carried the *other* session's paragraph
  under a message that did not describe it. Nothing was lost and the content was
  correct; the attribution and the message were not. **Look at what is staged,
  not at what you meant to stage.** But a check cannot close a race — the same
  collision happened *while* that check was being run, the other session
  committing in the window between the check and the commit. **So commit with a
  pathspec: `git commit -F - -- <paths>`** (with one gap: it cannot commit an
  *untracked* file, which needs `git add` first) takes the working-tree content of
  exactly those paths and ignores the index for everything else, so it cannot
  sweep the other session's staged work even if you forget to look. (Options
  before the `--`; `git commit -- <paths> -F -` parses `-F` as a pathspec and
  fails.) The check is then a backstop rather than the only defence.
  **But the pathspec isolates files, not authors, and that is a much weaker
  guarantee than it sounds.** It was used, correctly, on commit `87a42a8` — whose
  message describes exactly one thing, making an O.4 citation precise — and that
  commit carried **nine** claim ids, eight of them the other session's O.3/O.3'
  repoints and corrected counts, entirely undescribed. The pathspec did its job:
  it committed the working-tree content of `research_state/claims.json`. Both
  sessions *edit that file*, so scoping to it excludes nothing. A pathspec
  protects you only where the sessions touch disjoint paths, which is precisely
  the case that was never the problem. On a genuinely shared file the only
  defence is to look at what the diff *contains* — and to do it by **parsing both
  versions and comparing**, not by grepping the diff. The grep form was tried
  here first and is wrong: a claim's `"id"` line is *context*, not a changed
  line, so it reports every id whose neighbour moved. On the very next commit it
  named seven ids where four had changed, and three of the phantoms belonged to
  the other session — the check was one step from producing a false accusation
  of exactly the collision it was written to detect. The correct form loads
  `git show HEAD:<path>` and the working file, keys both by id, and diffs the
  dicts; it reported four, which was right. **A check that over-reports on a
  shared file is not the safe direction: it manufactures collisions.**
  **And the check has to gate the commit, or it is decoration.** The parsed
  version was written, run, and it worked — it reported seventeen changed claims
  where four were mine — and the commit went through in the same breath, because
  the check was a separate `python -` process and its `AssertionError` did not
  stop the shell from reaching `git commit` on the next line. Third crossed
  attribution of the night, this one committed *over* a correct warning I had
  just read. The repo's governing rule is that a guard not on the path is not a
  guard, and **the path here is the shell**: put the comparison and the commit in
  one process, or chain them with `&&` so a non-zero exit actually stops it. A
  check whose failure the next command ignores is worse than none, because it
  produces the feeling of having checked.
  **And the `&&` is not enough if the check is piped.** `python -m pytest -q |
  tail -1 && git commit` **always commits**: a pipeline's exit status is the last
  command's, and `tail` always succeeds. That pattern ran here for most of a
  session beside an unpiped `tools/check_claims_diff.py … && git commit` that
  gated correctly — so the claims gate worked, the test gate never did, and one
  commit went out red. Both sessions hit this independently in mirrored forms: a
  check whose correct output reached a reader who overrode it, and a check whose
  output could not reach the gate at all. **Use `set -o pipefail`, or do not pipe
  the checker**, and verify the gate against a deliberate failure —
  `false | tail -1 && echo ran` prints `ran`, which is the whole bug in one line. Verified from `git show`, not from the report — the other
  session flagged it, and the flag was right, but a collision report is a claim
  like any other.
  **And one edit per block**: a script with two `replace` calls
  whose first raises dies before the second, prints only the second's success
  line, and reads as a full success. That happened here — the anchor an earlier
  commit of mine had moved — and the resulting commit message described a
  correction that never applied, while the registry recorded it as done. (A related near-miss: a two-branch `replace` here would have
  written a literal `PLACEHOLDER` into `claims.json` had its first branch
  matched. It did not, so the result was correct by luck. `tools/` has no guard
  for this; the sweep for `PLACEHOLDER`, duplicated sentences and unbalanced
  `~~` across the registry and every note comes back clean as of this writing.)
- **On a shared file the danger is your own stale copy — a read-modify-write
  race that no staging discipline can see.** Every rule in this file about
  `git add -A`, pathspecs and `git diff --cached` assumes the hazard is
  *committing someone else's work*. The opposite happened: a script here read
  CLAUDE.md, a 55-second test run went by, the other session committed a rewrite
  of that region inside the window, and the write put back the **stale copy**,
  dropping ~50 lines of theirs. **The pathspec worked perfectly** — it committed
  the working-tree content of exactly that file, and that content was already
  wrong before git was involved; `git diff --cached` would have shown precisely
  what was intended. Restored by **merging forward from HEAD~1**, not reverting,
  since HEAD~1 held both their rewrite and (swept) the new paragraph.
  **The signal was in the commit output and went unread: 91 deletions against a
  20-line addition.** On a shared file the check is *deletions*, not staging, and
  the practice is to **re-read immediately before writing** — leave no gap in
  which the other session can commit.
  **And the gate was disarmed by being called in its reporting mode.**
  `check_prose_diff.py CLAUDE.md` with **no phrases** lists and cannot refuse: it
  printed the other session's bullet *by name*, said "bullets added: 1", and
  exited 0. A guard that is on the path can still be invoked in the mode that has
  no verdict, and then it reads as having passed. **Always pass the phrases.**

- **Tests protect the computation; nothing protects the paraphrase.** The
  registry's status field grades how a claim was *established* and says nothing
  about whether its *statement* still means what the computation showed. One
  session produced four variants, and **every one survived a green suite, because
  the tests were testing the correct object while the prose described a different
  one**:
  - *convention distance* — a symbol declared correctly 448 lines from its use
    (Note O's r_k), and DFI's determinant vs discriminant 200 lines apart;
  - *paraphrase drift* — a section heading outliving its own corrected body, and
    a correction reaching a claim's `notes` while its `statement` kept the old
    wording;
  - *an unattached axis* — "no log-power correction" and a measured (log M)^{1/4}
    reading as contradictory until each carried its axis and its grouping;
  - *a hypothesis dropped from a statement while remaining in its proof* — Note O's
    Prop O.1 stated without the window, with a counterexample inside the same note
    ((1,5) at m = 2, where a g² = 4 = M exactly, so the *strict* inequality the
    proof turns on fails by nothing at all);
  - *a correct result cited across a scope boundary the citing note never mentions*
    — Note F's **Z[i]** lemma equated to ν = 0 in [FM]'s **rational** axioms, in
    Notes G, J and M, none of which named the transfer. Nothing in those sentences
    is false; the error is entirely in which object a reader takes them to be
    about. The transfer is `gaussian-to-rational-bridge`, `inferred`.
  - *a silent no-op edit* — a scripted `replace` whose anchor had changed wrote
    back identical content and printed success; `git commit` then said "nothing
    to commit", which was misread as a collision with the parallel session
    because that had genuinely happened twice the same night. **Every string edit
    must assert its anchor**, and a *plausible* explanation for an anomaly is
    what stops you checking the implausible one.
  - *a claim stated to an order, read as an equality* — a distinct failure, and
    the hardest, because **both halves are true**. `sqrt-MX-law`'s one sentence
    contains two: "saturating at ~|A| for M ≥ X" is right about the order and
    wrong by **4×** literally (the ceiling is DIAG ≈ 0.253·X, since above the
    boundary each modulus carries one x and |Σ| counts squarefree incidences);
    and "the saving is exactly zero at θ = 1/2" is right about the *exponent*,
    Q^{(1/2−θ)/2} = Q⁰, and wrong by **2.41** read as S = T. Neither is a false
    statement and neither would fail any guard. **Write the constant, or write
    "to within a constant" — never a bare ≍ that a reader will use numerically.**
    A third instance sat in a `proved` claim: `type-I-level` gave Σ_{N(d)≤D}|r_d|
    ≍ D while `admissible-density` gave (3/2π)·D admissible ideals — **the two
    could not both carry constant 1**, and neither noticed. The constant is
    forced and exact: r_d is triangular on (−1,1), so E|r_d| = 1/3 and the sum is
    **D/(2π) = 0.159155·D** (measured 0.15895 at D = 5×10⁵, 0.13%).
    **These are errors that *sit*, not errors that propagate.** A false conclusion
    is caught by the next thing that uses it; a wrong constant inside a true
    order-statement is used by nothing, so nothing objects — which is why all
    three survived a green suite, two prose sweeps *and* a citation audit. The
    conclusions were untouched in all three, at 2.4×, 4× and 6.3× off.
    **Checkable form: wherever a note states an order for a quantity some
    experiment computes, put the computed constant in.**
  - *a count of chances mistaken for a count of **informative** chances* — three
    times in one night, and the informative subset is **never** the one a loop
    naturally counts. `triples-cannot-be-settled-by-measurement` says an absence
    over a vacuous population is not evidence; the trap is that the population
    looks populated. O.2's class count was 31 informative of **278 939** above
    threshold; exp17's solution count was **9** informative of **2 093** carrying
    an in-window multiplier, because a solution whose (a,b) has only one such
    multiplier has nothing to pair with. Both were quoted at the inflated figure,
    the second by the session that had just written the first correction into the
    README. **Before quoting N, ask what the N−k silent ones were silent about.**
  - *a statement about **proofs** read as a statement about the **object*** — a
    new pair of registers, and it had Note G's Step 2 checkpoint (a plan
    deliverable) asserting the opposite of the truth. "The trivial bound has
    never been beaten by any amount" is true of the *literature*; the checkpoint
    then said a reader "would conclude it is **untouched**". Measured,
    |Σ_{x≤X} μ(x²+1)|/√X sits between 0.21 and 1.34 over two decades, |S|/X down
    to 1.7×10⁻⁴ — **square-root cancellation, unmistakably.** The estimate at
    θ = 0 is *visibly true and unprovable by current methods*, a different
    position entirely from a sequence that misbehaves. Nobody had measured a sum
    everyone assumed was hopeless. **Say "no proof is known", never "it is not
    known to hold" — and measure before writing either.** (Nothing is fitted;
    `chowla-for-x2plus1-is-open` is untouched.)
  Nothing checks a proposition's statement against its own proof, because the
  **And watch the trajectory, not just the instances.** Three laws were fitted to
  one decay in one night, and the *disconfirming evidence got closer to hand each
  time*: with 1/N there was only one X and nothing to contradict it; with
  (log X)/N a drift was noticed, written down at 5.6, and the law quoted anyway;
  with N/X the counterexample sat **two rows apart in the same printed table**.
  Availability of the refutation went up while use of it went down — which is the
  opposite of what learning looks like, and is what confidence in a framework
  does when it outruns the evidence for it. If a third instance of one error
  class is easier to catch than the first and was still missed, the problem is
  not attention; it is that the framework has started supplying the answer before
  the data does.

  tests test the proof. The one checkable habit: **a correction that reaches only
  a claim's `notes` has not landed** — notes are where history goes, the statement
  is what gets quoted. `test_retracted_wording_is_not_still_in_the_statement`
  enforces the mechanical half (a note quoting the wording it retracts must not
  leave that wording in the statement); the paraphrased half stays discipline.

## From the state section

One rule's evidence lived in CLAUDE.md's state section rather than its rules, and
would otherwise have been the single rule in CLAUDE.md with no evidence here.

- **Reading sources: rasterise, do not extract.** Exactly one source here is a
scan — Duke–Friedlander–Iwaniec — and its OCR renders prose correctly while
mangling displayed mathematics, which is the worst failure mode because it looks
readable. Two claims were committed and refuted in one day from it. Run
`python tools/check_sources.py`, then read the page images:
`pymupdf.open(pdf)[idx].get_pixmap(dpi=300).save(...)`, where for DFI page index
n renders article page n + 422. There is a non-fatal no-go rule,
`quoting-a-scanned-text-layer`.

  Its no-go rule is `quoting-a-scanned-text-layer`; the sources that depend on it
  are cited in `note-C-requirements.md`, `note-G-spectral.md` and
  `note-J-mobius-in-progressions.md`.
