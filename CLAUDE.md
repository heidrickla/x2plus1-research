# Working notes for this repo

Research repo, not a product. The output is *notes* — code exists to keep the
notes honest.

## Where things stand

*This section is the compaction fallback. `tools/session_primer.py` prints a
live version of it via a SessionStart/compact hook, but that hook only binds in
sessions that start with `.claude/settings.json` already present — so this file,
which is always loaded, carries the same state by hand. Keep it current; a stale
version here is worse than none.*

**The obstruction is Type II, and it is Note F's C₄-free lemma**: for
A = {x+i}, G(n₁,n₂) = #{m : mn₁, mn₂ ∈ A} ≤ 1, so a bilinear form with
arbitrary bounded coefficients admits no cancellation at any split. That is a
theorem about the sequence and survives any change of sieve.

**And DFI say, on p. 425, that the arbitrary-coefficient bilinear form *is* the
parity-breaking input** — "this problem has been partially surmounted by adding
new information about general bilinear forms of the type (8) … here α_m and β_n
are arbitrary but bounded complex numbers". So **Note F is not an obstacle
beside the parity barrier; it is the statement that DFI's parity-breaking input
does not exist for this sequence.** Sharpest placement the repo has, and it
comes from the source.

**Note M** puts Notes H and F on one axis. With M = Q^θ, S_μ(M) ≍ √(MX) gives a
saving Q^{(1/2−θ)/2}: a power for every θ < 1/2, exactly zero at θ = 1/2. ASP's
(B1) needs θ ≥ 1/2; Ford–Maynard's (1.1) needs θ < 1/2. **The μ-cancellation
holds on precisely the range FM admits and dies precisely where ASP begins**,
and θ = 1/2 is where M = |A| and κ = 1. Its θ → 0 endpoint is Chowla for x²+1,
which Teräväinen calls wide open — so the easiest case of the input this repo
needs is a named open problem.

**Note J** reduces the Type II input to a Bombieri–Vinogradov statement for
μ(x²+1) in arithmetic progressions, and then measures that **the whole
difficulty is in the absolute values** — the signed sum is under 2% of the
absolute-value sum, and |·| per modulus *is* the arbitrary coefficient. Notes F
and J describe one obstruction from two sides.

**Note L** does two things. It scopes Note F: that lemma is about **Z[i]**, and
the rational graph — where [ASP]/[DFI]/[FM]'s Type II hypotheses actually live —
is *not* C₄-free (max Gram 2, not 1, because one rational modulus merges several
Gaussian ideals). Bounded either way, so nothing downstream changes, but the
transfer is now the registry entry `gaussian-to-rational-bridge`, `inferred`.
And it generalises everything: for A = {f(x)} with deg f = d, **α = 1/d and
κ = X^{2−d}**, so κ > 1 only at d = 1. **No single-variable polynomial of degree
≥ 2 has an admissible Ford–Maynard triple**; x²+1 is the least degenerate member
of a degenerate class, and d = 1 (Dirichlet) is the only degree with bilinear
structure. The ladder recovering Dirichlet at d = 1 is the check that it means
something.

**Note K** adds the fourth published sequence with a known outcome: Merikoski's
a²+(b²+1)², which has the *same density and the same κ* as a²+b⁴ and a Type II
range a sixth of an exponent shorter. **So κ > 1 is necessary and not
sufficient** — only the direction κ = 1 ⟹ forest is load-bearing. √κ is the
length of the Poisson sum in [MER] p. 4; for x²+1 it is 1.

**Position against the literature** (all read at source): ASP needs D > x^{2/3}
and this sequence caps at x^{1/2}; DFI's Theorem S is normalised to x and is
*vacuous* on a sequence of mass x^{1/2} — and restated relative to |A| its
Type I (D = x^{1/2−ε}) is **available** while its Type II (short variable to
x^{1/3−ε}, β on primes) is not, so the level is never the obstruction;
Ford–Maynard's binding parameter is **ν, not γ** — every entry in their Table 1 has ν > 0 (smallest: Merikoski's
1/12), and ν = 0 here gives C⁻ = 0 by Selberg and their Theorem 2.1. Their
footnote 2 p. 7 names Note F's G(n₁,n₂) as the barrier. Their Theorem 2.4 never
applied here, and the γ = 1/2 − ε argument is `refuted`; the clean placement is
that θ > c = 1/2 collides with (1.1)'s θ < 1/2, so there is no admissible triple
at all (`x2plus1.exponents.ford_maynard_theta`). C⁻ = 0 is about **what these
axioms can prove**, never about whether x²+1 is prime infinitely often — do not
conflate them.

**Notes N and O** are the two additions the plan does not list. N re-argues the
Green–Tao exclusion from Green–Sawhney: it survives, but not for the plan's
stated reason — their weight has both coordinates free, δ₁ imposes two
independent linear conditions, and at their k ≈ 2^347 the normalised Gowers norm
of a delta is 1 − o(1), so the conclusion is *information-free*. O identifies the
multiplier τ = (√b+√a)/(√b−√a) behind the close-pair structure and proves it
cannot act twice on one element. **The general "no window holds three" is NOT
proved** — it was claimed unconditionally and retracted; the window Gram bound
stays O_ε(N^ε). Three things to know before reopening it. The ideal-theoretic
route is **closed, not merely incomplete**: it needs Q̄ and Q̄″ coprime, and over
the only regime where that is observable (triples in *wide* windows) coprimality
holds in 5 of 65 cases — it is the exception. The only unconditional constraint
on a triple is the Plücker–parity one, **M/√D ≥ 11.484** against 5.657 for a
pair, and its virtue is that it contains no ideal theory. And the empirical
support is **31 informative classes**, not the 278,939 above threshold — a class
is silent unless it has three shared moduli at all, so "verified over hundreds of
thousands" would be true and misleading.

**Two closures, both negative and both durable.** The well-factorable route is
dead: every theorem in the BFI line buys its level by giving up the absolute
value (BV has sup_a |·| at level 1/2; BFI x^{4/7−ε} and Maynard x^{3/5−ε} with a
well-factorable weight and a *fixed* residue class), so beyond level 1/2 there is
no absolute-value statement to appeal to. And the remaining triple question
**cannot be settled by measurement** — it concerns a configuration that never
occurs, so every sweep contains zero instances, and the absence is the thing to
be explained rather than evidence about a proposed explanation. That trap
produced two adopted-then-retracted claims in one day.

**Reading sources: rasterise, do not extract.** Exactly one source here is a
scan — Duke–Friedlander–Iwaniec — and its OCR renders prose correctly while
mangling displayed mathematics, which is the worst failure mode because it looks
readable. Two claims were committed and refuted in one day from it. Run
`python tools/check_sources.py`, then read the page images:
`pymupdf.open(pdf)[idx].get_pixmap(dpi=300).save(...)`, where for DFI page index
n renders article page n + 422. There is a non-fatal no-go rule,
`quoting-a-scanned-text-layer`.

Read [README.md](README.md) and [notes/README.md](notes/README.md) first. Run
`python -m pytest -q` before trusting any measurement.

## Non-negotiables

- **Normalisation.** Q (or N) = norm bound; X = √Q = range of x; |A| = X.
  State which one every exponent is relative to. "Level N^{1/2}" = "level X".
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

## The claim registry — read before writing a finding

`research_state/claims.json` records every established claim with an **enforced
epistemic status**, checked by `tests/test_claims.py`. The pattern is adapted
from the sibling repo `rh-research-engine` (`core/models.py`, `core/nogo.py`,
`docs/EPISTEMIC_BOUNDARIES.md`), whose governing rule applies here too:

> A guard that is not on the path is not a guard.

The vocabulary is deliberately not interchangeable:

| status | requires | meaning |
|---|---|---|
| `proved` | `proof_site` naming a note **and** a test | proved in this repo |
| `quoted` | `citation` with a page/result locator | verbatim from a source |
| `rigorous_finite` | `experiment` naming the script | exact over a stated finite range |
| `extrapolated` | `experiment` + `notes` | an asymptotic law fitted from finite data |
| `inferred` | `notes` saying what is missing | reasoning, not reading or proof |
| `hypothesis` | — | proposed; screened against no-go rules |
| `refuted` | `superseded_by` | kept so it cannot be silently re-asserted |

**`inferred` is the class this repo needed.** Twice a conclusion was over-read
from evidence that did not support it — "the obstruction is Type I, not Type II",
then "(R1) is soft". Both are in the registry as `refuted`, with what replaced
them. An inferred claim reads exactly like a quoted one in prose; the status is
the only thing that keeps them apart.

**`rigorous_finite` vs `extrapolated`** is the same distinction one level down,
added after the `rh-research-engine` session pointed at its `rigorous_numerical`
rung: *rigorous about what it covers, and what it covers is always finite.*
"max off-diagonal Gram entry is 1 at X = 8000" settles a finite question
completely; "ρ ~ (log X)^c with c = 0.00 ± 0.04" is a fit. Fits are how a finite
observation becomes a claim about all X without anyone deciding to promote it.
The dependency guard enforces the ordering — it has already rejected a
`rigorous_finite` claim that rested on an `extrapolated` one.

Before proposing a route, screen it:

```python
from x2plus1.claims import screen
screen("open the square and bound by Weil")   # -> ['dispersion-at-alpha-half']
```

No-go rules match on **wording as well as tags**, so a ruled-out route cannot be
resurrected by renaming its tag. `green-tao-excluded` is deliberately non-fatal:
it is contested by Green–Sawhney and must be re-argued, not obeyed.

## Code conventions

- Exact integer arithmetic in Z[i] — int pairs, never `complex`. Floats appear
  only in reported statistics.
- Ideals are named by their unit-normalised generator (`unit_normalize`:
  Re > 0, Im ≥ 0). Never key a dict on a non-normalised Gaussian integer.
- Bulk work goes through the progression sieve in `factorization.py`, not
  per-value `factorint`. Divisibility in this sequence *is* a congruence; the
  code should look like the mathematics.
- New claims that can be checked numerically get a test in
  `tests/test_arithmetic_facts.py`. That file is the machine-checked version of
  Note A; if a test there fails, a note is wrong.
- No scipy. `typeII.Sparse` is a 40-line CSR; keep the dependency set at
  sympy + numpy.

## Running things

```bash
python -m pytest -q
```

Experiments take a size argument and print a table; they are meant to be read,
not imported. Each one names the note it feeds in its docstring. Results are
gitignored — rerun rather than commit output.

## Scope discipline

The plan rules these out; they stay ruled out unless the plan is amended:

- Green–Tao / nilsequence methods (single-variable polynomials are out of scope).
- GRH or zero-density substitutes for Type II (they control primes in
  progressions, not in a sparse sequence).
