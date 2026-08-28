# x² + 1 — research repo

Working repo for the programme in [x2plus1-research-plan.md](x2plus1-research-plan.md):
attack Landau's fourth problem via the Friedlander–Iwaniec asymptotic sieve,
reformulated over **Z[i]**.

The plan's working principle governs this repo too: **do not try to prove the
theorem — locate the exact lemma in the a² + b⁴ argument that fails at density
x^{1/2}.** Everything here is instrumentation for that search.

## Layout

| path | what it is |
|---|---|
| [x2plus1-research-plan.md](x2plus1-research-plan.md) | the charter. Not edited by work; amended only deliberately. |
| [notes/](notes/) | Notes A–O. A–I are the deliverables named in the plan; J–O were added by the work. |
| [x2plus1/](x2plus1/) | the library: Z[i] arithmetic, sieving, Type I and Type II harnesses. |
| [experiments/](experiments/) | runnable scripts; each names the note it supports. |
| [tests/](tests/) | unit tests, plus `test_arithmetic_facts.py` — machine-checked statements of the lemmas the notes rely on. |
| [refs/](refs/) | bibliography and a literature-scan log. |
| [research_state/claims.json](research_state/claims.json) | every claim with an enforced epistemic status — `proved` / `quoted` / `rigorous_finite` / `extrapolated` / `inferred` / `refuted` — checked by `tests/test_claims.py`. |

## Quick start

```bash
python -m pytest -q
```

```bash
python experiments/exp01_type_i_level.py 4000
```

```bash
python experiments/exp02_bilinear_pilot.py 20000
```

```bash
python experiments/exp03_density_ledger.py 10000000
```

```bash
python experiments/exp04_kappa_family.py 10000000 6
```

```bash
python experiments/exp08_merikoski_ledger.py 10000000
```

```bash
python experiments/exp09_degree_ladder.py 4000
```

```bash
python experiments/exp13_window_gap.py 2500
```

```bash
python tools/smoke_experiments.py
```

No installation needed — the scripts put the repo root on `sys.path`. Requires
Python ≥ 3.11 with `sympy` and `numpy` (and `pymupdf` for
`tools/check_sources.py`).

## State of play

**The obstruction is Type II, and it is [Note F](notes/note-F-failure-localisation.md)'s
C₄-free lemma.** That took three revisions to get right; the earlier framings
are kept as `refuted` entries in
[`research_state/claims.json`](research_state/claims.json).

Friedlander–Iwaniec's asymptotic sieve requires Type I to level **D > x^{2/3}**
((R1), ASP p. 1043), which x² + 1 cannot reach — [Note B](notes/note-B-type-I.md)
caps it at x^{1/2}. And ASP p. 1045 shows x^{2/3} is precisely where the
bilinear coefficient γ(n,C) is annihilated, so within ASP the two hypotheses are
one. **But x^{2/3} is ASP's threshold, not prime detection's** — Heath-Brown hit the
same wall at α = 2/3, judged it likely relaxable, and wrote his own sieve
instead (HB p. 3). What the obstruction actually is took three sources read
directly to pin down, and the answer is not the one this repo held for most of
its life.

### The obstruction, as the sources actually state it

**Duke-Friedlander-Iwaniec** ([Duke's own scan](https://www.math.ucla.edu/~wdduke/preprints/equidistribution.pdf))
— the sieve Green–Sawhney use. Its §6 is *Combinatorial identities*, not a
sieve; its Theorem S needs Type I at x^{1/2−ε} and concludes only o(π(x)); and
its Type II coefficients are **not arbitrary** — "β_n will be supported on
primes" (p. 437). The arbitrary-coefficient version is Green–Sawhney's
strengthening. And DFI's sequence has α = 1, so applied verbatim to A = {x+i}
the whole apparatus is **vacuous**: the hypotheses hold trivially and the
conclusion is weaker than the trivial bound. An earlier version of this README
said x² + 1 *meets* DFI's Type I hypothesis. It does not; that claim is now
`refuted` in the registry.

**Ford–Maynard** (arXiv:2407.14368) map the parameter space, and the parameter
that places x² + 1 is **ν**, not γ. By [Note F](notes/note-F-failure-localisation.md)
there is no arbitrary-coefficient Type II range at all, i.e. **ν = 0**, and then
C⁻ = 0 follows from **Selberg's example** (their p. 2) — the oldest result in the
paper, with no ε-loss — and from their Theorem 2.1 (p. 3). Every one of the eight
entries in their Table 1 (p. 3) has ν > 0; the smallest is Merikoski's 1/12. The
divisor-bounded escape is closed for the same reason: their Theorem 2.7(c) gives
C⁻_bd(1/2, 0, ν) = 0 for small ν, whatever the density. And their footnote 2
(p. 7) names Note F's counting function #{n : nm₁, nm₂ ∈ J} as the barrier to
extending θ+ν, calling it "typically very difficult"; here it is provably ≤ 1.

Cleanest placement, computed rather than argued
(`x2plus1.exponents.ford_maynard_theta`): for J of size x^{1−c} they say "one
can only hope for (I) to hold for γ < 1 − c and (II) for θ > c" (p. 7), while
(1.1) requires θ < 1/2. At density x^{1/2}, c = 1/2, and **there is no
admissible triple at all.** Two earlier readings of this paper are `refuted` in
the registry; the γ = 1/2 − ε argument was the second of them.

**And C⁻ is the lower-bound constant, so this closes infinitude, not just the
asymptotic.** Ford–Maynard define it on p. 2: "We have an asymptotic formula for
Σ_p a_p whenever C⁻ = C⁺ = 1 and **a non-trivial lower bound for primes whenever
C⁻ > 0**." Landau's problem asks only for infinitude, so a reader can fairly ask
whether a lower-bound method survives where an asymptotic one fails — Li's
density-2/3 statement is explicitly about *asymptotic* estimates. C⁻ = 0 answers
it: no non-trivial lower bound follows either. The same page subsumes the obvious
candidate, since they argue "in contrast with … especially those relying on the
iterative techniques of the Harman sieve … demonstrating general limitations of
the Type I/Type II setup" — which is why Merikoski's Harman-sieve lower bound is
a Table 1 *entry* rather than an exception to it.

**Read that correctly, and read both halves.** C⁻ = 0 says *these axioms cannot
prove infinitude* — there exists an admissible sequence with no primes. It says
nothing about whether x² + 1 is prime infinitely often. Stating only the first
half overclaims; stating only the second understates what is closed. Both are
true and they sit uncomfortably close together.

### What survives, and it is narrow

- **DFI's Lemma 2 is scale-free, and the re-normalisation is now written down**
  ([Note C](notes/note-C-requirements.md)). At X = |A| = Q^{1/2} it holds with
  γ(d) = 2ρ(d)/d, c = 4, G(z) ≍ log z, and an error that is o(|A|/log Q) once D
  exceeds z by exp(C(log log Q)²) — quasi-polynomial in log, not a power. So the
  machinery genuinely reaches a sequence of mass Q^{1/2}. **But the
  scale-freeness stops at Lemma 2**: Lemma 3 and Theorem S fix c_n ≤ τ(n) and
  X ≪ x log x, i.e. density one, so there is no re-normalisation of Theorem S —
  only a thin-sequence analogue that would have to be re-proved. Restating its
  hypotheses relative to |A|: Type I at Q^{1/2−ε} is **available** (Note B
  permits D ≪ Q^{1/2}(log Q)^{−222}); Type II with the short variable up to
  Q^{1/3−ε} and β supported on primes is **not**. The level is not the
  obstruction.
- **DFI's equidistribution theorem is about this repo's residues.** It covers
  aX²+2bX+c with ac−b² > 0, so ν²+1 ≡ 0 (mod p) is literally the case, and
  their Weyl sum ρ_h(n) is the sum over the r_d of [Note A](notes/note-A-dictionary.md).
  Their Proposition 1 bounds those residues **in arithmetic progressions** —
  exactly the shape [Note J](notes/note-J-mobius-in-progressions.md) reduces the
  Type II input to. Whether it transfers is the sharpest open question here.
- **The β = μ cancellation is outside their axioms**, but only in one precise
  form. A μ-restricted Type II is *weaker* than the arbitrary-coefficient one at
  the same range, so restricting coefficients is not per se an escape. It is new
  information only because it holds on ranges where the arbitrary-coefficient
  hypothesis fails outright — which, by Note F, is every range. Ford–Maynard
  expect such specialised results to upgrade to full ones (footnote 1, p. 3);
  Note F is a proof that here they cannot, which makes this sequence a
  counterexample to that expectation.

### The two supporting results

**Type I stops at Q^{1/2}, sharply.** Divisibility by a Gaussian ideal is
exactly one residue class mod N(d), so |r_d| ≤ 1 — and that is best possible,
since an interval of length X meets a class in ⌊X/q⌋ or ⌈X/q⌉ points. The
admissible ideals of norm ≤ D number ~(3/2π)·D — the residue of
ζ(s)L(s,χ₄)/ζ(2s), measured at 0.4771 against a predicted 0.47746, which
validates the harness. So Σ|r_d| ≍ D must be o(|A|) = o(Q^{1/2}).
[Note B](notes/note-B-type-I.md).

**The Type II incidence matrix is a forest, provably.** Writing
G(n₁, n₂) = #{m : mn₁ ∈ A and mn₂ ∈ A} — the sum every dispersion argument must
evaluate:

> **Lemma.** For A = {x + i}, G(n₁, n₂) ≤ 1 whenever n₁ ≠ n₂.
>
> *Proof.* A 4-cycle gives a₁a₄ = u·a₂a₃ for a unit u. Since (x+i)(y+i) =
> (xy−1) + i(x+y) has Re ≥ 0 and Im ≥ 2 for x, y ≥ 1, both sides lie in the
> first quadrant, forcing u = 1; then x₁+x₄ = x₂+x₃ and x₁x₄ = x₂x₃, so
> {x₁,x₄} = {x₂,x₃}, which collapses the cycle. ∎

So there is no congruence to detect, no exponential sum, no Weil bound — the
count is already 0 or 1. **That lemma is about Z[i].** Over Z, where the
literature's Type II hypotheses actually live, the same graph is *not* C₄-free —
one rational modulus merges several Gaussian ideals — and the Gram entries are 2
rather than 1 on every dyadic window. Bounded either way, so the conclusion is
unchanged and only the constant moves, but the transfer is `inferred`.
[Note L](notes/note-L-over-Z.md). Measured dispersion exponent: **θ = 1.00–1.03 at every
split, worse than trivial.** From the density side, mean degrees satisfy
D_m·d_n ≍ |A|²/Q =: κ independent of the split, so max over splits of
min(D_m, d_n) ≍ √κ = |A|/Q^{1/2} — **exactly 1** for x² + 1 and ≍ Q^{1/4} for
a² + b⁴ (predicted 48.7, measured 41.2 at Q = 10⁷; maximum off-diagonal Gram
entry 1 versus **667**). [Note F](notes/note-F-failure-localisation.md).

κ turns out to be exactly the condition for FI's required bilinear range (B1)
to be non-degenerate: (B1) forces M ≥ √x, cancellation forces M ≤ A(x), and
both hold iff κ > 1. That was not built in — it is a consistency check between
the repo's derived invariant and the paper's stated hypothesis. In the window
(B1) actually requires, the measured bilinear sum shows **no saving at all**
(S_μ/A(x) = 0.93, 1.00, 1.01), which corrects the earlier reading in
[Note H](notes/note-H-numerical-pilot.md).

### The one thing that moved, and exactly how far

[Note O](notes/note-O-tau-multiplier.md) identifies the multiplier behind the
close-pair structure: for coprime a < b the ratio of two shared moduli inside one
dyadic window is **τ² with τ = (√b + √a)/(√b − √a)**, verified to a median
relative error of 2.4 × 10⁻⁵, with a threshold (b/a > 33.97) attained at 34.1 and
never violated. **A multiplier at index k exists iff a² + (4k²−2)ab + b² is a
perfect square** — at k = 1 that is (a+b)², a square *identically*, which is why
the trivial multiplier always exists and why a triple needs a second one.

Two theorems follow. **O.3**: for M = b − a odd squarefree, no window holds
(ξ, τ₁ξ, τ_kξ). **O.3′**, superseding it: the same whenever
**gcd(M, 2X) ≤ 16**, with no hypothesis on M — reaching the even and
non-squarefree cases O.3 was mute on, including all four known live
non-fundamental close pairs. The proof turns on ρ = B_k/M, where the identity
M(ρ² − 1) = 4ka(k − ρ) and the window force ρ < 1.06066, while integrality makes
c·ρ an integer — and an integer in (c, 1.06066c) needs c ≥ 17.

**The general statement — no window holds three, full stop — is not proved.** It
was claimed unconditionally for about an hour and retracted. Its sharp form is
measurable and measured: *on any solution ξ, at most one acting multiplier has
modulus ratio < 2* — 13 840 solutions with an acting multiplier, 327 with exactly
one inside a window, **zero with two**, smallest competing ratio 14.91 against
the 2 required. The bound on the window Gram entry stays **O_ε(N^ε)** with the
measured 2 unproved.

Extended by [`exp17`](experiments/exp17_sharp_form.py), which restricts to the
slice y/x ≥ 3+2√2 where a second in-window multiplier is geometrically possible
at all: at X = 40000, over 55.5M ratio classes, **6 019 solutions carry exactly
one in-window multiplier and zero carry two**. **But most of those are vacuous** —
a solution whose (a,b) has only *one* in-window multiplier could never have
carried two. Counting only the informative ones, whose (a,b) has ≥ 2 in-window
multipliers: **3 at X = 3000 and 9 at X = 14000**. That is the evidence base, and
this README quoted the larger number until the check was run. Those are not a sample — acting is
orbit-invariant, so one solution settles its whole infinite class, and each of the
informative solution is **decided completely** — acting is orbit-invariant, so
one solution settles its whole infinite class. What the run misses is classes
whose least solution exceeds X, and nothing bounds how many of those there are.
The margin has stopped moving — smallest competing ratio 14.15 at both X = 14000 and
X = 40000, at the same witness (1, 16133) — a factor 7.1 above the 2 a window
needs.

**The one unconditional constraint on a triple** is Plücker plus parity. V is a
2×2 determinant, so three solutions satisfy V_ij X_k − V_ik X_j + V_jk X_i = 0;
with X_k/X_i < √2 that forces |V_ik| > 2 + 2/√2, hence ≥ 4 by parity, hence
**M/√D ≥ 11.484** — against the 5.657 a mere pair needs. It contains no ideal
theory, so it does not share the failure mode of the arguments above.

**Eight routes are closed with reasons** ([Note O](notes/note-O-tau-multiplier.md)),
and the two most likely to look worth retrying are not. The ideal-theoretic one
needs two ideals to be coprime, and coprimality holds in **5 of 65** observable
cases — the exception, not the rule. And there is **no residue obstruction at
all**: the exact linear conditions plus the conic are simultaneously solvable for
every one of the 21 pairs that survive the cheap filter, so O.2 is not a
congruence statement and **any proof must be about occupancy**.

**And the evidence is thinner than the sweeps suggest, which is worth stating
plainly.** A class can exhibit a triple only if it clears M/√D ≥ 11.484 *and* has
three shared moduli at all. At X = 4000 that is **31 classes**, not the 278 939
above the threshold — the rest are silent. "Verified over hundreds of thousands
of ratio classes" would be true and thoroughly misleading.

**The methodological finding cost a day and is the most transferable thing here.**
Generating candidates from *multipliers* and testing occupancy afterwards searches
a mostly-empty space — and worse, **the multiplier ratio does not predict the
spacing of the occupied moduli**: on (1, 115921) it predicts 1.31 and the observed
minimum ratio is 33.77, because the near-neighbour class the multiplier points at
is the empty one. Every r-product statistic either session produced is withdrawn.
The correct direction is inverted: enumerate *realised* classes and read off which
multiplier index explains the ratio, checking the residual rather than eyeballing
it. Occupancy as input cannot produce a dead configuration.

**And the θ axis turns out to be the same object.** Writing S_μ(M)² ≤ #{m∼M}·Q₂,
the second moment splits exactly as Q₂ = DIAG + OFF with
OFF = Σ_{x≠y} μ(x²+1)μ(y²+1)·**G_M(x,y)** — literally the Gram entries Prop L.1
bounds. Cauchy–Schwarz is tight (0.75) and DIAG ≍ X, so the upper bound Note M
needs follows from OFF = o(DIAG). **But that is a restatement, not a reduction**:
discarding the signs is 11×–1988× too weak, and regrouping by shift gives
OFF = Σ_m Σ_h Σ_x μ(x²+1)μ((x+h)²+1) — a two-point correlation, i.e. **Chowla for
x²+1**, which is open. So the route closes on the blocker the repo already names.
What survives is that a result on either axis is no longer irrelevant to the
other.

### Three things that came out right without being aimed at

A repo that only produces obstructions is hard to trust. These are the checks
that the apparatus returns known answers where it should, and none was
engineered:

1. **The degree ladder recovers Dirichlet.** α = 1/d and κ = X^{2−d} give κ > 1
   only at d = 1, which is primes in arithmetic progressions — solved, and the
   only single-variable degree with bilinear structure. A classification that
   did not return the solved case there would be evidence against itself.
   [Note L](notes/note-L-over-Z.md).
2. **Two independent readings land on the same triple.** Instantiating DFI's
   Theorem S relative to |A| gives Type I at Q^{1/2−ε} and Type II with the short
   variable up to Q^{1/3−ε} — and Ford–Maynard's Table 1 places DFI at
   (γ, θ, ν) = (1/2, 0, **1/3**). Two papers read separately, same numbers.
   [Note C](notes/note-C-requirements.md).
3. **Lemma 2's two output objects are the repo's two notes.** Its special
   bilinear forms (32) are [Note J](notes/note-J-mobius-in-progressions.md)'s
   object and its general forms (33) are
   [Note F](notes/note-F-failure-localisation.md)'s. The DFI apparatus
   decomposes along the seam the repo had already found.

A fourth, from the other direction: Ford–Maynard's footnote 2 (p. 7) names
Note F's counting function as the barrier, in their own words, having been
derived here from the Gaussian structure rather than read out of a paper.

**And evaluating that footnote's own hypothesis at this density sharpens the
placement.** It applies when θ + ν ≥ 1 − 2c, and |J| = x^{1/2} gives c = 1/2, so
**1 − 2c = 0 and θ + ν ≥ 0 holds for every admissible pair.** So this is not a
barrier x² + 1 runs into while reaching for a wide Type II range — **every Type
II range it could have is already on the far side of it**, the θ = ν = 0 boundary
where the sequence actually sits included. The footnote's averaging range is
m₁, m₂ ∼ x^{1−2c+ε} = x^ε, and Note F's bound holds at every split, that one
among them. The two statements compose exactly:

> Ford–Maynard: the obstruction to any Type II estimate here is bilinear
> cancellation in the error term for G.
> Note F: G is identically 0 or 1 — no main term, hence no error term.

What they call "typically very difficult outside of special situations" is, for
this sequence, **not difficult but empty**. (`inferred`: they state the
condition, the evaluation at c = 1/2 is ours.)

### What the Z[i] → Z transfer actually costs

Note F forbids **K₂,₂** over Z[i] — that is C₄-freeness. Over Z, one rational
modulus carries several primitive Gaussian ideals, and merging those rows breaks
it. Measured, the breakage is one-sided:

- **K_{2,s} is unbounded** — largest observed s = 9, at cofactors (1, 5) with
  moduli 2, 10, 65, 442, 3026, 20737, …
- **K_{s,2} is unbounded too** — six cofactors 1, 53, 423125, 24326641, … all
  share the moduli {10, 17}, and the family is infinite, being a Prop L.1 orbit
  read on the dual side.
- **K₃,₃ does not occur.** Zero instances, exhaustively over the X = 6000
  incidence structure.

So the merging **thickens each side separately and neither jointly** — a sharper
statement of the gap than "max Gram 2 instead of 1", because it says which
completeness survives. It buys nothing quantitatively: Kővári–Sós–Turán on a
K₃,₃-free graph gives a bound 2–4 orders above the true edge count here, and
Note F does not use C₄-freeness via edge counting either — it uses it to make the
Gram matrix diagonal, which is a statement about *cancellation*.

**And the window statement is self-dual.** A cofactor pair sharing a modulus
satisfies b x² − a y² = a − b; a *modulus* pair shared by a cofactor satisfies
m₂x² − m₁y² = m₁ − m₂ — the same conic with the roles swapped. So "at most two
moduli per window for a fixed cofactor pair" and "at most two cofactors per
window for a fixed modulus pair" are one theorem, and both measure 2. That also
dissolves the apparent tension above: the six cofactors sharing {10, 17} have
consecutive ratios 53 and 7983, so **no window holds two of them**. Unbounded
totals and a bounded window count are one structure read at two scales.

### It was never about x² + 1

For A = {f(x) : x ≤ X} with deg f = d, the norm bound is Q ≍ X^d and |A| = X, so

> **α = 1/d**  and  **κ = |A|²/Q = X^{2−d}**,

with no dependence on f beyond its degree. κ > 1 only at d = 1, κ = 1 exactly at
d = 2, κ < 1 above. And Ford–Maynard's c = 1 − 1/d is ≥ 1/2 for every d ≥ 2,
colliding with their (1.1)'s θ < 1/2. Measured over Z at X = 4000, sweeping
dyadic windows ([exp09](experiments/exp09_degree_ladder.py)):

| f | d | α | κ | max Gram |
|---|---:|---:|---:|---:|
| 2x + 1 | 1 | 1.000 | 2000 | **32** |
| x² + 1 | 2 | 0.500 | 1 | 2 |
| x² + x + 1 | 2 | 0.500 | 0.9998 | 2 |
| x³ + 2 | 3 | 0.333 | 0.00025 | 1 |
| x⁴ + 1 | 4 | 0.250 | 6.25 × 10⁻⁸ | 1 |

> **No single-variable polynomial sequence of degree ≥ 2 has an admissible
> Ford–Maynard triple, and d = 1 — Dirichlet — is the only single-variable
> degree with anything for a bilinear form to cancel.**

x² + 1 is the *least degenerate member of a degenerate class*, not a special
case. The ladder recovers the solved case at d = 1, which is the check that
matters. [Note L](notes/note-L-over-Z.md).

### The density ledger

| sequence | A(x) | free variables | κ > 1? | ν (FM Table 1) | ASP applies? |
|---|---|---:|---|---|---|
| a² + b⁴ (FI 1998) | x^{3/4} | 2 | ✅ | 1/2 | ✅ — D = x^{3/4−5ε} achieved |
| a² + p⁴ (Heath-Brown–Li) | x^{3/4} | 2 | ✅ | — | ✅ |
| a² + (b²+1)² (Merikoski 2022) | x^{3/4} | 2 | ✅ (same κ) | **1/12** | ✅ but unused — Harman, lower bound only |
| f(a, b²), *every* binary quadratic f (Xiao 2021) | x^{3/4} | 2 | ✅ | — | ✅ |
| x³ + 2y³ (Heath-Brown 2001) | x^{2/3} | 2 | ✅ | 1/3 | at the boundary — "not quite met", short by ε |
| x² + 1 | **x^{1/2}** | **1** | ❌ (κ = 1) | **0** | ❌ |

**Five published sequences, every one at α ≥ 2/3, every one with two free
variables.** Xiao's row is the sharpest form of the pattern: he varies the
*shape* over all irreducible primitive binary quadratics at once, and the
density does not move. What the technology generalises is the form; what it has
never generalised is the density.

The second row is the control: same density, same κ to 0.04%, and a Type II
range a sixth of an exponent shorter. **κ is necessary, not sufficient** —
[Note K](notes/note-K-merikoski.md), [`exp08`](experiments/exp08_merikoski_ledger.py).
The column that separates every solved case from this one is ν.

### Not yet done

- **The μ-Type II as a theorem rather than a measurement.** Its θ → 0 endpoint
  is |Σ_{x≤X} μ(x²+1)| ≪ X(log X)^{−A}, and even the o(X) version is Chowla for
  x²+1, which Teräväinen calls "wide open for any polynomials with nonlinear
  irreducible factors" (arXiv:2010.07924v4, pp. 1–2). For this sequence the
  trivial bound has never been beaten by any amount, at any level, signed or
  absolute — **in the literature.** The sum itself cancels: measured,
  |Σ_{x≤X} μ(x²+1)|/√X stays between 0.21 and 1.34 across more than two decades,
  reaching |S|/X = 1.7×10⁻⁴ at X = 4×10⁶. So the estimate needed at θ = 0 is
  **visibly true and unprovable by current methods**, which is a different
  position from a sequence that misbehaves. No law is fitted: two decades is not
  an asymptotic, and Chowla for x²+1 remains open.
  [Note M](notes/note-M-where-mu-lives.md), [Note G](notes/note-G-spectral.md).
- **An absolute-value analogue of DFI's Proposition 1.** Prop 1 bounds a
  *signed* sum over this repo's residues; [exp07](experiments/exp07_absolute_values.py)
  shows the difficulty is entirely in the absolute values, so what is needed is
  Σ_d |Σ_m ρ_h(dm)| — precisely the shape Note F obstructs. ~~Whether a
  well-factorable decomposition can reach it is the live question.~~ **Closed,
  negatively** — see the BFI bullet below.
- Iwaniec 1978's **statement** is sourced from Pintz's survey (§19), and its
  **method** is now sourced too: ~~Lemke Oliver unread~~ — **read**, and it
  records that Iwaniec "obtained a new form of the error in the linear sieve"
  plus an equidistribution result for the roots of x²+1 ≡ 0 (mod m), so
  Iwaniec's P₂, DFI's theorem and Note A are one object rather than three
  resembling ones. Its Remark 3 adds a third degree-uniform statement: at degree
  3 the analogue of its condition (IV) is Hooley's and is **conditional on
  Hypothesis R\*** on short Kloosterman sums — so the arithmetic input every
  route needs is already conditional one degree above us, independently of κ.
  *Opera de Cribro* Ch. 24–25 unobtained; BFI I–III no longer wanted (below).
- [Note G](notes/note-G-spectral.md) now carries the **Step 2 checkpoint**
  (plan §2.5): the shortfall comes out as *two incommensurable units*, not one
  number — the **norm** (Prop 1's signed 1/20 saving against an absolute-value
  requirement) and the **kind** (Chowla for x²+1, wide open). A third unit, the
  level, was proposed and refuted the same day.
- ~~Green–Sawhney unread~~ — **read**, and the plan's Green–Tao exclusion is
  re-argued from the paper in [Note N](notes/note-N-green-tao-exclusion.md). It
  survives, but the plan's stated reason ("single-variable polynomials are
  outside their scope") is not why: their weight has both coordinates free, our
  f′ = δ₁ imposes two independent linear conditions, and at their k ≈ 2^347 the
  normalised Gowers norm of a delta is 1 − o(1), so the conclusion is not merely
  inapplicable but *information-free*. They name x² + 4 with x prime — our
  y = 1 — as what they cannot reach. `green-tao-excluded` stays non-fatal: the
  rule exists so a reader has to read the argument, not obey the rule.
- The 2026 bilinear-sums-with-modular-square-roots cluster is logged in
  [refs/literature-log.md](refs/literature-log.md) from abstracts only. It
  bilinearises over the radicand, not the modulus, so it is filed as adjacent —
  but that judgement rests on abstracts, not readings.
- **Conjecture O.2 — no dyadic window holds three shared moduli — is the one
  open question the repo is not merely blocked on.** Its sharp form is
  measurable: *on any solution ξ, at most one acting multiplier has modulus
  ratio < 2*. Theorem O.3′ proves the case where one of the two is the trivial
  multiplier τ₁; the gap is p, q ≥ 2, which is realised — (53, 423125) has its
  close pair at k = 12 with τ₁ excluded — but only once in 379 close pairs at
  X = 3000. Proving it upgrades `rational-gram-bounded-on-windows` from
  `rigorous_finite` to `proved`. **It changes no conclusion**: a bounded count
  supplies no main term at 1, 2 or 3 alike, so a counterexample would not weaken
  the obstruction either. Worth doing for the status; worth knowing that is all
  it is. [Note O](notes/note-O-tau-multiplier.md).
- **The well-factorable question is closed, negatively.** BFI I–III remain
  unobtained in the original and are no longer wanted for it: read at source in Maynard's
  arXiv:2006.07088, every theorem in that line buys its level by giving up the
  absolute value — BV has sup_a |·| at level 1/2, BFI reaches x^{4/7−ε} and
  Maynard x^{3/5−ε} with a well-factorable weight and a *fixed* residue class.
  Beyond 1/2 there is no absolute-value statement to appeal to.
  [Note J](notes/note-J-mobius-in-progressions.md).

## Conventions

Fix one normalisation and keep it. Throughout:

- **Q** (or **N**) is the *norm* bound — the sieve's own variable, `n ≤ Q`.
- **X** = √Q is the range of x, so |A| = X for the x² + 1 sequence.
- "Level N^{1/2}" and "level X" are the same statement. Confusing the two is
  the easiest available mistake; the plan's §1.3.2 parenthetical is in the
  norm normalisation.
- Gaussian integers are `(a, b)` int pairs meaning a + bi. Ideals are named by
  their unit-normalised generator (Re > 0, Im ≥ 0).
