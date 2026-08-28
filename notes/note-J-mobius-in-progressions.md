# Note J — The Type II sum is Möbius in arithmetic progressions

*Not in the plan's original deliverable list. Added because Notes C and F
between them left one well-posed question — what exactly is the missing
arithmetic input? — and it turns out to have a recognisable answer.*

*Status: draft. The reduction is machine-checked in
[`tests/test_note_j.py`](../tests/test_note_j.py); the measurements are
[`exp05`](../experiments/exp05_mobius_progressions.py).*

## Where this note sits

[Note F](note-F-failure-localisation.md) proves the incidence graph of
A = {x + i} is C₄-free, so a bilinear form over it with **arbitrary** bounded
coefficients has no cancellation at any split. [Note C](note-C-requirements.md)
shows that is fatal wherever an arbitrary-coefficient Type II hypothesis is
asked for — which is Green–Sawhney's form of the Duke–Friedlander–Iwaniec
sieve, and, in Ford–Maynard's axioms, is the statement that ν = 0.

> **Scope, and this sentence crosses a boundary.** Note F's lemma is about
> **ideals of Z[i]**; [ASP], [DFI] and [FM] quantify their Type II hypotheses
> over **rational** m and n. The step between them is
> `gaussian-to-rational-bridge`, `inferred` — over Z the graph is *not* C₄-free
> (max windowed Gram 2, not 1, and the unwindowed count is unbounded: see
> [Note L](note-L-over-Z.md)). Bounded is all the argument uses, so the
> conclusion does not move; but "ν = 0" is reached through the bridge and not
> directly from Note F. The rest of this note names A = {x + i} where it means
> the Gaussian object, and says so where it does not.

But the sieve's own coefficient is **μ**, and with β = μ the same sum does
cancel. So the live question is not "does the bilinear form cancel" — it does —
but "what is the statement that would have to be proved, and is it recognisable?"

This note answers that. It is a reformulation, not a proof strategy, and
probably routine to a specialist; its value is that it names the target.

## The reduction

**Step 1 — the fibres are lines.** Fix m = a + bi and let n = c + di. Then

> mn = (ac − bd) + (ad + bc)i,

so the condition mn ∈ A — that is, Im(mn) = 1 — is the **line** ad + bc = 1 in
(c, d). Its homogeneous solutions are (c, d) = t(a, −b), i.e. n = t·m̄. Hence

> **{n : mn ∈ A} = n₀ + ℤ·m̄**, an arithmetic progression in Z[i] of common
> difference m̄, with ≍ X/N(m) terms.

Checked at every m occurring for X = 2000, with the fibre length independently
matched against #{x ≤ X : x ≡ r_m (mod N(m))}
(`test_fibres_are_arithmetic_progressions_with_difference_conj_m`,
`test_fibre_length_matches_the_residue_class_count`).

**Step 2 — μ of the ideal is μ of the norm.** Each rational prime p | x²+1
contributes exactly one prime ideal to (x+i) with the same exponent, so (x+i)
is squarefree as an ideal iff x²+1 is squarefree as an integer, and the two ω
agree:

> **μ_{Z[i]}((x+i)) = μ(x² + 1).**

(`test_mobius_of_the_ideal_equals_mobius_of_the_norm`.)

**Step 3 — combine.** Writing x + i = m·n, μ(x+i) = μ(m)μ(n) whenever x+i is
squarefree, so

> Σ_{N(m)≍M} | Σ_n μ(n)·1[mn ∈ A] |
>  =  Σ_{q ≍ M} | Σ_{x ≤ X, x ≡ r_q (mod q)} μ(x² + 1) |  + (non-squarefree),

with q = N(m) and r_q the root of r² + 1 ≡ 0 (mod q) — the admissible ideals of
[Note A](note-A-dictionary.md). Verified directly, with every disagreement
confirmed to come from a non-squarefree fibre
(`test_mobius_over_a_fibre_equals_the_progression_sum`).

## What that makes the missing input

> **The Type II hypothesis for x² + 1 is a Bombieri–Vinogradov theorem for
> μ(x² + 1) in arithmetic progressions.**

**The range this note used to assert here was wrong and is withdrawn.** It said
"moduli up to X^{3/4} … beyond BV's level 1/2, below Elliott–Halberstam", and
derived that from "DFI's Type II window N(b) ∈ [(log X)^C, Q^{3/8}]". Reading
DFI's page images rather than the scan's OCR shows the 3/8 is an **exponent
inside a bound** — Proposition 2, p. 426, gives
B(M,N) ≪ ‖αρ‖‖β‖(M^{1/2} + N^{3/4}M^{3/8+ε}) — and not a window at all.

DFI's actual Type II window is fixed by Theorem S (p. 437), which needs the
general bilinear form R(w,y) = Σ_{w≤n<y} β_n Σ_{(m,n)=1} α_m c_{mn} over

> **n ∈ [x^{o(1)}, x^{1/3−ε}]**, i.e. the short variable up to Q^{1/3−ε},

with β_n supported on primes. Confirmed from outside: Ford–Maynard's Table 1
places DFI at (γ, θ, ν) = (1/2, 0, **1/3**), and θ+ν = 1/3 is exactly Theorem S's
y. So the level to quote is **Q^{1/3−ε} in the short variable**, and whether that
is "beyond BV's level 1/2" depends on a conversion this note has not carried out
— the honest statement is that it is DFI's range, and DFI's range is not
available here.

Two things this buys. It removes the Gaussian divisor enumeration entirely —
the object needs only μ(x²+1), which sieves in linear time
([`x2plus1/mobius.py`](../x2plus1/mobius.py), 47 s at X = 10⁷ against minutes
for the incidence route) — and it makes the target recognisable, connecting to
the BFI/Zhang/Maynard literature on moduli beyond 1/2.

## Measurement: the law has no log-power correction

The reformulation makes the question directly measurable. The right statistic is
the **per-progression saving**

> ρ = S / (pairs · √(X/M)),

the mean |Σ μ| over one progression divided by the square root of its length.
Square-root cancellation makes ρ constant in both M and X; a log-power loss
shows as ρ drifting with log X. Note H could not resolve this over one decade.

Swept over prime moduli from X = 10⁴ to 10⁷ (`exp05`), fitting ρ ~ (log X)^c:

| M band | pairs in band | fitted c |
|---|---:|---:|
| [10, 10²) | 20 | +0.126 |
| [10², 10³) | 138 | −0.356 |
| [10³, 10⁴) | 1 058 | −0.101 |
| [10⁴, 10⁵) | 8 348 | **−0.026** |
| [10⁵, 10⁶) | 68 784 | **+0.039** |

**c → 0 as the statistics improve.** The scatter in the small bands is
sample-size noise — 20 pairs cannot fit an exponent — and the two well-sampled
bands both give |c| < 0.04 — but see the error bar below, which is four times
larger. At fixed M the drift is flat to within 1%:
ρ = 0.7221 → 0.7158 across X = 3×10⁵ → 10⁷.

The fit is taken at **fixed M band**, not at fixed u = log M/log X. That matters:
ρ carries a finite-n dependence (short progressions sit above the Gaussian
limit), and at fixed u the progression length varies with the band, confounding
the finite-n effect with the log-power being measured. At fixed band, n scales
cleanly with X and the two separate. Fitting at fixed u instead gives scatter
from −0.31 to +0.13, which is the confounding, not a signal.

### The error bar, and why the first one was wrong

The ±0.04 above is the scatter of one draw across bands. It is **not an error
bar**, and reporting it as one repeated a mistake the `rh-research-engine`
session had just found in its own exponent fit: shifting the sample grid inside
the same range moved its fitted exponent from 0.214 to 1.061, with the recorded
value being a single draw. Their general move — *vary the thing nobody chose and
see if the answer moves* — applies here, because nobody chose the decade band
boundaries.

[`exp06`](../experiments/exp06_fit_robustness.py) varies the band phase and
takes the spread as the error bar, with two injected-signal controls. Over
X = 10⁴…10⁷ (7 ladder points), 12 phases:

| signal | mean c | spread | range |
|---|---:|---:|---:|
| **actual** | **−0.057** | 0.186 | [−0.150, +0.036] |
| iid null (no log-power by construction) | −0.002 | 0.102 | [−0.066, +0.035] |
| injected damping (log X)^{−1/2} | **−0.482** | 0.176 | [−0.579, −0.403] |

The injected control is what licenses the reading: the estimator **recovers a
genuine −0.5 as −0.48**, so it has real power to see a log-power of that size.
Without it, "c ≈ 0" would be indistinguishable from an estimator that cannot see
anything at all. The null comes back unbiased at −0.002, and the actual signal
sits 0.055 from it — a tenth of the spread.

> **Conclusion: the law is √(MX) with no log-power correction, to a resolution
> of |c| ≲ 0.2.** Per-progression cancellation is clean square-root. This
> discharges the caveat Note H has carried since it was first measured — but at
> a quarter of the precision first claimed. The honest figure is ±0.19, not
> ±0.04, and the difference is entirely that the first number was one draw
> rather than an error bar.

### The constant, and a control that matters more than it

An earlier run reported ρ ≈ 0.655 against a predicted √(2/π)·√0.8948 = 0.755 and
flagged the gap as unexplained. It was an artefact: the statistic normalised by
the *nominal* band length X/√(lo·hi) rather than the actual mean progression
length, understating it by ~9%. Corrected, ρ ≈ 0.72, and the residual gap is the
finite-n approach to the Gaussian limit. **The fitted c is unaffected** — the
correction is a constant factor per band, which cancels in the drift — so the
headline survived the bug, which is the only reason it is worth reporting rather
than quietly fixing.

The control is the more interesting part. Recomputing ρ against two nulls at
X = 10⁶ — the same μ values randomly **shuffled** (destroying all arithmetic
structure), and a synthetic **iid** ±1/0 sequence at the same density:

| M band | mean length n | ρ actual | ρ shuffled | ρ iid |
|---|---:|---:|---:|---:|
| [10³, 10⁴) | 268.9 | 0.7255 | 0.7185 | 0.7311 |
| [10⁴, 10⁵) | 26.5 | 0.7157 | 0.7114 | 0.7163 |
| [10⁵, 10⁶) | 2.6 | 0.7326 | 0.7283 | 0.7278 |

> **μ(x²+1) along these progressions is statistically indistinguishable from
> random**, by this statistic, at this scale — actual, shuffled and iid agree to
> within 1–2% in every band.

That is a negative result and should be read as one: it says no *obstruction* is
visible in the correlation structure, not that μ is random. It is the outcome
one wants — the required cancellation appears to hold for the reason one would
hope — and it is exactly as far from a proof as it was before, since the parity
barrier is a statement about provability, not about truth.

## The difficulty is entirely in the absolute values

The Type II object carries |·| per modulus. Taking |·| is taking the supremum
over signs ε_q, i.e.

> S_abs = sup over ε ∈ {±1} of Σ_q ε_q Σ_{x ≡ r_q (q)} μ(x²+1),

which is **exactly an arbitrary outer coefficient** — the thing
[Note F](note-F-failure-localisation.md) proves this sequence cannot support.
*(The q here are **rational** moduli, while Note F's lemma is about ideals of
Z[i]; over Z the **windowed** Gram entry is 2 rather than 1, and the
unwindowed one is unbounded ([Note L](note-L-over-Z.md), K_{s,2} for every s). The transfer is
`gaussian-to-rational-bridge`, `inferred`; the conclusion survives because
bounded is bounded, and [Note G](note-G-spectral.md) states it in full.)*
So it is worth measuring what the absolute values cost. Against the signed sum
(same arithmetic, sup removed), at X = 3×10⁶ (`exp07`):

| M band | pairs | S_abs | S_signed | ratio | √(terms) |
|---|---:|---:|---:|---:|---:|
| [10³, 10⁴) | 1 058 | 21 319 | −397 | **0.019** | 924 |
| [10⁴, 10⁵) | 8 348 | 53 408 | −460 | **0.009** | 815 |
| [10⁵, 10⁶) | 68 784 | 138 889 | +525 | **0.004** | 738 |

**Measured across M as well as at one band, which is what the claim needs.** The
table above fixes X and varies the band; the ratio it reports is one number.
Sweeping M over a factor of 1024 at X = 10⁶:

| M | signed | S_abs | signed/S_abs | \|signed\|/√T |
|---:|---:|---:|---:|---:|
| 512 | −337 | 3 505 | 0.096 | 0.59 |
| 2 048 | 588 | 6 942 | 0.085 | 1.02 |
| 8 192 | −22 | 13 308 | 0.002 | 0.04 |
| 32 768 | −750 | 26 438 | 0.028 | 1.30 |
| 131 072 | 127 | 50 915 | 0.002 | 0.22 |
| 524 288 | −497 | 97 875 | 0.005 | 0.86 |

with T flat at 3.3×10⁵ = 0.33·X throughout. **The signed sum has full
square-root cancellation relative to the incidence count, uniformly in M** —
|signed|/√T is O(1) at every band, and its fluctuation between 0.04 and 1.30 is
what a random-sign sum of that size does. Meanwhile S_abs grows 28-fold.

So the ratio is not a constant 2%: it **decays as M grows**, 0.096 → 0.005. The
absolute value costs more the further into the Type II range one goes — which is
the direction that matters, since [ASP]'s (B1) wants M large.

> **The signed sum is under 2% of the absolute-value sum, and is itself below
> √(terms).** So the signed side already cancels better than square-root, while
> the absolute-value side does not cancel at all beyond the per-progression
> saving.

This is not a restatement of Note F — it is a *measurement* of it. The whole
Type II difficulty for x² + 1 sits in the absolute values, which are the
arbitrary coefficient, which is what C₄-freeness kills. The two notes are
describing one thing from two sides.

### And it answers the Proposition 1 question

[Note C](note-C-requirements.md) flagged DFI's Proposition 1 (p. 425) as the
sharpest open lead, because it bounds

> L_d(M) = Σ_{M<m≤2M} ρ_h(dm) ≪ (h,d)^{1/20}(d/M)^{1/20}M^{1+ε}

over exactly these residues, in exactly these progressions. But that is a bound
on a **signed** sum over m — the side this experiment shows is not where the
difficulty lives.

> **Proposition 1 is the right object in the wrong norm.** It would need an
> absolute-value analogue, Σ_d |Σ_m ρ_h(dm)|, and that is precisely the shape
> Note F obstructs.

That downgrades the lead, honestly. It does not close it — a signed bound can
still be an ingredient in an argument that handles the absolute values by other
means (Cauchy–Schwarz with a well-factorable decomposition, say) — but it is not
the missing input by itself, and Note C should not have called it the sharpest
question without checking the norm.

## Honest assessment as a pathway

**This is a target, not a route.** Three reasons to keep expectations low:

1. Any such theorem **breaks parity**, so it cannot follow from sieve axioms —
   it needs genuine arithmetic input, which is what nobody has at this density.
2. A BV theorem for μ along a thin polynomial sequence is open **at every
   level**. Its θ → 0 endpoint is |Σ_{x≤X} μ(x²+1)| ≪ X(log X)^{−A}, and even
   the o(X) version is Chowla for x²+1, which Teräväinen calls "wide open for
   any polynomials with nonlinear irreducible factors"
   ([Note M](note-M-where-mu-lives.md)). For this sequence the trivial bound has
   never been beaten by any amount, at any level, signed or absolute.
3. Ford–Maynard are worse than that, though **not for the reason this note gave
   until it was corrected**. The γ = 1/2 − ε argument and the appeal to their
   Theorem 2.4 are both `refuted` — 2.4's hypothesis needs ν ≥ 1/3, which this
   sequence does not have, and their Table 1 caption discards the ε. What binds
   is **ν = 0**, by Selberg and their Theorem 2.1, and there is no admissible
   (γ, θ, ν) triple at density x^{1/2} at all. See
   [Note C](note-C-requirements.md).

What it does change: it makes the required input a **statement about μ in
progressions** rather than about Gaussian bilinear forms, and that is a
literature with real machinery in it.

## This reopens something the repo had closed

[refs/bibliography.md](../refs/bibliography.md) argues that BFI, Zhang,
Polymath 8 and Maynard cannot help, because they raise the level for *primes in
APs* while our cap is a counting bound on the sequence. That argument is sound
for **Type I**. It does **not** transfer to the Type II input identified here:
that is a μ-weighted sum over x ≤ X to moduli well below X, where the counting
bound does not bite. So well-factorable weights and the dispersion machinery may
be relevant after all — applied to μ(x²+1), not to primes.

The registry claim `large-moduli-cannot-help` is scoped to Type I accordingly.

## The well-factorable route does not deliver absolute values

*The repo has carried "whether a well-factorable decomposition can reach
Σ_d |Σ_m ρ_h(dm)| is the live question" since the first draft of this note. Read
at source, the answer is no, and the reason is structural rather than
quantitative.*

Every theorem in the BFI line trades the absolute value away to buy the level.
From Maynard, [arXiv:2006.07088](https://arxiv.org/abs/2006.07088):

- **Bombieri–Vinogradov** (his (1.1)): Σ_{q ≤ x^{1/2}/(log x)^B}
  **sup_{(a,q)=1} |π(x;q,a) − π(x)/φ(q)|** ≪ x/(log x)^A. Absolute value, and a
  maximum over residue classes — at level **1/2**.
- **BFI Theorem 10**, quoted there as Theorem A: λ_q **well-factorable** of
  level Q ≤ x^{4/7−ε} ⟹ Σ_{q≤Q} λ_q(π(x;q,a) − π(x)/φ(q)) ≪ x/(log x)^A. No
  absolute value; a **fixed** residue class a.
- **Maynard Theorem 1.1**: the same with *triply* well-factorable at
  Q ≤ x^{3/5−ε}. **Theorem 1.2**: linear-sieve weights λ⁺ at D ≤ x^{7/12−ε}.

> **Beyond level 1/2 the literature has no absolute-value statement at all.**
> Every gain above x^{1/2} is bought by replacing |·| with a well-factorable
> weight and fixing the residue class.

**That was the repo's synthesis from the theorem statements. Maynard says it
himself, on p. 1, immediately before Definition 1** — read on a later sweep of
the same source:

> "In many applications, particularly those coming from sieve methods, one does
> not quite need to have the full strength of an estimate of the type (1.1). It
> is often sufficient to measure the difference between π(x; q, a) and π(x)/φ(q)
> only for a **fixed bounded integer a** (such as a = 1 or a = 2) **rather than
> taking the worst residue class** in each arithmetic progression. Moreover, it
> is also often sufficient to measure the difference … with 'well-factorable'
> weights (which naturally appear in sieve problems) **rather than absolute
> values**. **With these technical weakenings** we can produce estimates
> analogous to (1.1) which involve **moduli larger than x^{1/2}**."

Both weakenings named, and named as *what buys the level*. And the other half,
same page:

> "we do not know how to establish (1.1) with the summation extended to
> q ≤ x^{1/2+δ} for any fixed δ > 0."

So the full statement — sup over residue classes, absolute values — **is not
known beyond x^{1/2} at all**, by the author of the strongest result in the line.
The closure is now quoted rather than assembled.

Well-factorable is not a device for converting a signed bound into an
absolute-value one — it is the *structure a sieve's weights happen to have*,
and Iwaniec's theorem is that the linear sieve's upper-bound weights are a
linear combination of well-factorable sequences. An arbitrary sign pattern,
which is what |·| per modulus amounts to, is not well-factorable and there is no
result saying it can be made so.

**What that means here.** This note's object needs moduli to Q^{1/3−ε}, which
against a sequence of X = Q^{1/2} terms is level **2/3** — beyond BV. So it needs
an absolute-value statement in exactly the range where the literature offers only
well-factorable ones. The route is closed, and closed for a reason that no
improvement in the exponent would reopen.

That also connects to [Note F](note-F-failure-localisation.md) from the other
side: the absolute value per modulus *is* the arbitrary outer coefficient, and
Note F proves that coefficient admits no cancellation here. Two different
literatures decline the same object.

## Adversarial review

- *Two-parameter freedom smuggled in?* No. The reduction uses only that
  elements of A have imaginary part exactly 1 — the same hypothesis as Note F's
  lemma, and it is what makes the fibre a line.
- *Where is parity broken?* Nowhere. This note relocates the parity-breaking
  requirement into a recognisable statement; it does not supply it, and the
  measurement that the statement is *true* is not evidence that it is provable.
- *Is the reduction novel?* Almost certainly not — the link between Type II sums
  and Möbius in progressions is routine. Do not present it as new. Its value
  here is naming the target and making it cheap to compute.
- *Is c = 0 over-read?* It was: ±0.04 was one draw, not an error bar. The
  phase-varied figure is c = −0.057 ± 0.19, i.e. c = 0 to a resolution of
  |c| ≲ 0.2, over three decades of X.
- *Is the prime-moduli restriction distorting the object?* **Cross-checked at
  scale — [VERIFY] discharged.** The cap was never mathematical: it was sympy's
  `factorint` being called once per modulus. `factorization.admissible_roots_upto`
  builds the whole root table in bulk — an SPF sieve, one square root of −1 per
  prime p ≡ 1 (4) lifted by Hensel, CRT along each q — which reaches Q = 10⁶ in
  0.9 s where the per-modulus route capped the run at X ≤ 10⁵. It agrees with
  `roots_of_minus_one` exactly on q ≤ 3000, and reproduces
  Σ_q ρ(q)/Q → 3/(2π) = 0.47746 as **0.47744** at Q = 10⁶ — the same constant
  [Note B](note-B-type-I.md) measures by enumerating Gaussian ideals, from an
  unrelated code path.

  Over all admissible moduli, X = 10⁴ … 10⁷ — **four decades**, ending with a
  band of 4.3 million (q, root) pairs — ρ per band, averaged over the X ladder:

  | band | (q, root) pairs | mean ρ | sd across X |
  |---|---:|---:|---:|
  | [10, 10²) | 44 | 0.605 | 0.0900 |
  | [10², 10³) | 430 | 0.640 | 0.0411 |
  | [10³, 10⁴) | 4 294 | 0.635 | 0.0120 |
  | [10⁴, 10⁵) | 42 988 | 0.630 | 0.0018 |
  | [10⁵, 10⁶) | 429 684 | 0.632 | 0.0004 |

  **ρ ≈ 0.632 in every well-populated band, flat in M across four orders of
  magnitude and flat in X** — against 0.64–0.73 for prime moduli. So the prime
  restriction is not distorting the object.

  The fitted log-power depends on how many moduli a lane has, and that is
  diagnosable rather than mysterious. With no cut, the lanes give −0.342, 0.351,
  −0.213, −0.080, −0.031, −0.049; restricted to bands with ≥ 10⁴ pairs they give
  **c = −0.032 and +0.016**. The drift at small u is sampling noise, and the
  scatter behaves exactly as sampling noise must:

  > sd(ρ)·√pairs = 0.60, 0.85, 0.79 for the three bands with eight X-values
  > each — constant to 20% while the pair count varies by a factor of 100.

  (The two largest bands give 0.37 and 0.23, but they have only 5 and 3
  X-values, so their sd is itself badly estimated; they are shown, not used.)

  **So c = 0 to a resolution of about ±0.05 in the lanes that can resolve
  anything**, which is tighter than the prime-moduli figure of −0.057 ± 0.19 and
  independent of it. Still finite data, and still evidence about the **truth**,
  not about provability.
- *Is the X^{3/4} range right?* **No — [VERIFY] discharged, against this note.**
  DFI's page images render cleanly at 300 dpi even though the scan's OCR layer
  does not, and the range as stated here does not survive reading them.

  The X^{3/4} was derived from "DFI's Type II window N(b) ∈ [(log X)^C, Q^{3/8}]",
  and the 3/8 came from Proposition 2 (p. 426):

  > **PROPOSITION 2.** Suppose β_n are supported on primes. For h ≪ MN we have
  > (10) B(M,N) ≪ ‖αρ‖‖β‖(M^{1/2} + N^{3/4}M^{3/8+ε}).

  But 3/8 there is an **exponent inside a bound**, not a range for the modulus.
  DFI's actual Type II window is fixed by Theorem S (p. 437), which requires
  (35) with **y = x^{1/3−ε}** and w = x^{(log log x)^{−3}} — i.e. the general
  bilinear form R(w,y) = Σ_{w<n<y} β_n Σ_{(m,n)=1} α_m c_{mn} over
  **n ∈ [x^{o(1)}, x^{1/3−ε}]**. In the norm normalisation that is n up to
  Q^{1/3−ε}, not Q^{3/8}.

  This is confirmed from outside: Ford–Maynard's Table 1 places DFI at
  (γ, θ, ν) = (1/2, 0, **1/3**), and θ + ν = 1/3 is exactly Theorem S's y.

  So the level this note should quote for the missing input is **Q^{1/3−ε} in
  the short variable**, and the claim "beyond BV's level 1/2" needs re-deriving
  from that rather than from 3/8. Note also, since it cuts the other way: it is
  only β_n that DFI restrict to primes, not α_m — an earlier draft of this
  bullet said both, which was read off the broken OCR and is wrong.
