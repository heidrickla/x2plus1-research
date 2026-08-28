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
| [notes/](notes/) | Notes A–I, the deliverables named in the plan. |
| [x2plus1/](x2plus1/) | the library: Z[i] arithmetic, sieving, Type I and Type II harnesses. |
| [experiments/](experiments/) | runnable scripts; each names the note it supports. |
| [tests/](tests/) | unit tests, plus `test_arithmetic_facts.py` — machine-checked statements of the lemmas the notes rely on. |
| [refs/](refs/) | bibliography and a literature-scan log. |
| [research_state/claims.json](research_state/claims.json) | every claim with an enforced epistemic status — `proved` / `quoted` / `measured` / `inferred` / `refuted` — checked by `tests/test_claims.py`. |

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

No installation needed — the scripts put the repo root on `sys.path`. Requires
Python ≥ 3.11 with `sympy` and `numpy`.

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

**Read that correctly.** C⁻ = 0 says *these axioms cannot prove primality* —
there exists an admissible sequence with no primes. It says nothing about
whether x² + 1 is prime infinitely often.

### What survives, and it is narrow

- **DFI's Lemma 2 is scale-free, and the re-normalisation is now written down**
  ([Note C](notes/note-C-requirements.md)). At X = |A| = Q^{1/2} it holds with
  γ(d) = 2ρ(d)/d, c = 4, G(z) ≍ log z, and an error that is o(|A|/log Q) once D
  exceeds z by exp(C(log log Q)²) — quasi-polynomial in log, not a power. So the
  machinery genuinely reaches a sequence of mass Q^{1/2}. But Lemma 2 requires
  **D > z**, and Note B caps D at o(Q^{1/2}), so z = o(Q^{1/2}) — so at no
  admissible parameter choice can it distinguish a prime from a product of two
  primes. **Its ceiling is P₂**, which is where the subject stands, and what
  puts it there is the hypothesis ordering, not anything bilinear. Lemma 2 is an
  identity, not a lower bound, so this is a *coinciding ceiling* and not a
  re-derivation of Iwaniec 1978.
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

### Three things that came out right without being aimed at

A repo that only produces obstructions is hard to trust. These are the checks
that the apparatus returns known answers where it should, and none was
engineered:

1. **The degree ladder recovers Dirichlet.** α = 1/d and κ = X^{2−d} give κ > 1
   only at d = 1, which is primes in arithmetic progressions — solved, and the
   only single-variable degree with bilinear structure. A classification that
   did not return the solved case there would be evidence against itself.
   [Note L](notes/note-L-over-Z.md).
2. **DFI's Lemma 2 is capped exactly at the known record.** Instantiated at
   X = |A| it applies cleanly, and its own hypothesis ordering D > z against
   Note B's ceiling forces z = o(Q^{1/2}) — so at no admissible parameter choice
   can it distinguish a prime from a product of two primes. Its ceiling is P₂,
   and P₂ is where the subject stands (Iwaniec 1978). Lemma 2 is an identity,
   not a lower bound, so this is a coinciding ceiling and **not** a re-derivation
   — worth exactly that much. [Note C](notes/note-C-requirements.md).
3. **Lemma 2's two output objects are the repo's two notes.** Its special
   bilinear forms (32) are [Note J](notes/note-J-mobius-in-progressions.md)'s
   object and its general forms (33) are
   [Note F](notes/note-F-failure-localisation.md)'s. The DFI apparatus
   decomposes along the seam the repo had already found.

A fourth, from the other direction: Ford–Maynard's footnote 2 (p. 7) names
Note F's counting function as the barrier, in their own words, having been
derived here from the Gaussian structure rather than read out of a paper.

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

| sequence | A(x) | κ > 1? (Type II non-degenerate) | ν (Ford–Maynard Table 1) | A(x) > x^{2/3}? (ASP applies) |
|---|---|---|---|---|
| a² + b⁴ (FI 1998) | x^{3/4} | ✅ | 1/2 | ✅ — D = x^{3/4−5ε} achieved |
| a² + (b²+1)² (Merikoski 2022) | x^{3/4} | ✅ (same κ) | **1/12** | ✅ but unused — Harman, lower bound only |
| x³ + 2y³ (Heath-Brown 2001) | x^{2/3} | ✅ | 1/3 | at the boundary **[VERIFY]** |
| x² + 1 | **x^{1/2}** | ❌ (κ = 1) | **0** | ❌ |

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
  absolute. [Note M](notes/note-M-where-mu-lives.md).
- **An absolute-value analogue of DFI's Proposition 1.** Prop 1 bounds a
  *signed* sum over this repo's residues; [exp07](experiments/exp07_absolute_values.py)
  shows the difficulty is entirely in the absolute values, so what is needed is
  Σ_d |Σ_m ρ_h(dm)| — precisely the shape Note F obstructs. Whether a
  well-factorable decomposition can reach it is the live question.
- Iwaniec 1978's **statement** is now sourced from Pintz's survey (§19); its
  **method** is still second-hand. Lemke Oliver, *Acta Arith.* **151** (2012),
  241–261 is the refereed generalisation and is unread. BFI I–III and *Opera de
  Cribro* Ch. 24–25 unobtained.
- [Note G](notes/note-G-spectral.md) is still marked a skeleton, though its
  premise has been corrected: DFI's method *is* spectral and does reach these
  residues without dispersion — it just lands on Proposition 1, i.e. the signed
  norm again.
- **Green–Sawhney** ([arXiv:2410.04189](https://arxiv.org/abs/2410.04189)) is
  still unread, and still the highest-value unread item. The plan's Green–Tao
  exclusion is `green-tao-excluded` in the registry, deliberately non-fatal, and
  must be re-argued rather than obeyed.
- The 2026 bilinear-sums-with-modular-square-roots cluster is logged in
  [refs/literature-log.md](refs/literature-log.md) from abstracts only. It
  bilinearises over the radicand, not the modulus, so it is filed as adjacent —
  but that judgement rests on abstracts, not readings.

## Conventions

Fix one normalisation and keep it. Throughout:

- **Q** (or **N**) is the *norm* bound — the sieve's own variable, `n ≤ Q`.
- **X** = √Q is the range of x, so |A| = X for the x² + 1 sequence.
- "Level N^{1/2}" and "level X" are the same statement. Confusing the two is
  the easiest available mistake; the plan's §1.3.2 parenthetical is in the
  norm normalisation.
- Gaussian integers are `(a, b)` int pairs meaning a + bi. Ideals are named by
  their unit-normalised generator (Re > 0, Im ≥ 0).
