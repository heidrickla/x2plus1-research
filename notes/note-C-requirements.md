# Note C — Requirements table

*Plan §1.3.3, the Step 1 checkpoint. Status: **filled and answered.***

Sources, both read directly (PDFs in `refs/pdf/`, gitignored — copyright):

- **[ASP]** Friedlander & Iwaniec, "Asymptotic sieve for primes", *Ann. of
  Math.* **148** (1998), 1041–1065. [arXiv:math/9811186](https://arxiv.org/abs/math/9811186).
- **[X2Y4]** Friedlander & Iwaniec, "The polynomial X² + Y⁴ captures its
  primes", *Ann. of Math.* **148** (1998), 945–1040.
  [arXiv:math/9811185](https://arxiv.org/abs/math/9811185).

Page references are to the Annals pagination printed in the arXiv preprints.

---

## The answer, first

> **The asymptotic sieve for primes cannot be applied to x² + 1, and the
> obstruction is Type I, not Type II.**
>
> [ASP] requires a level of distribution **D > x^{2/3}** — hypothesis (R1),
> p. 1043. [Note B](note-B-type-I.md) proves that for this sequence
> Σ_{d≤D}|r_d| ≍ D, so (R) forces D ≤ A(x) = x^{1/2}. Since
> x^{1/2} < x^{2/3}, **the admissible range for D is empty.**

Friedlander and Iwaniec state the general principle themselves, p. 1044:

> "for thin sequences A one cannot expect (R) to hold with D(x) > A(x) and for
> such sequences the classical sieve does correspondingly worse."

Combining that ceiling with (R1) gives the sieve's own **density threshold**:
it applies only to sequences with **A(x) > x^{2/3}**. This is stated outright
in [ASP] p. 1059, in the remark on hypothesis (9.2):

> "The condition (9.2) holds for sequences A = (aₙ) satisfying aₙ ≤ nᵋ and
> A(x) ≥ x^{2/3 + 2ε}."

| sequence | A(x) | vs. x^{2/3} | D achieved |
|---|---|---|---|
| a² + b⁴ | x^{3/4} | **above** | **x^{3/4−5ε}** ([X2Y4] Prop. 3.5, p. 962) |
| x³ + 2y³ | x^{2/3} | at the boundary | — **[VERIFY]** |
| x² + 1 | **x^{1/2}** | **below** | ≤ x^{1/2}, and no D is admissible |

So Step 2 as framed by the plan is attacking the wrong half. See
[§ Consequences](#consequences-for-the-plan) below.

---

## The hypotheses, quoted

Sequence A = (aₙ) of nonnegative reals, A(x) = Σ_{n≤x} aₙ,
A_d(x) = Σ_{n≤x, d|n} aₙ = g(d)A(x) + r_d(x). Goal: an asymptotic for
S(x) = Σ_{n≤x} aₙΛ(n).

### Standing conditions

| eq. | statement | p. | holds for x²+1? |
|---|---|---|---|
| (1.4) | A(x) ≫ A(√x)(log x)² | 1041 | ✅ x^{1/2} ≫ x^{1/4}(log x)² |
| (1.6) | A_d(x) ≪ d^{−1}τ(d)⁸A(x) uniformly in d ≤ x^{1/3} | 1042 | ✅ ρ(d) ≤ τ(d) |
| (1.8) | 0 ≤ g(p) < 1, g(p) ≪ p^{−1} | 1042 | ✅ g(p) = ρ(p)/p ∈ {0, 2/p} |
| (1.9) | Σ_{p≤y} g(p) = log log y + c + O((log y)^{−10}) | 1042 | ✅ PNT mod 4 |
| (1.16) | aₙ = 0 if μ(n) = 0 | 1044 | ❌ x²+1 is often non-squarefree (7²+1 = 2·5²) |

### Hypothesis (R) — Type I

> **(R)** Σ_{d≤D} μ²(d)|r_d(t)| ≤ A(x)(log x)^{−222} for all t ≤ x, with
> **(R1)** x^{2/3} < D(x) < x.  *(p. 1043)*

- **θ₁ = 2/3**, strictly. Not a convenience: (R1) is a lower bound on D.
- Log-saving exponent **E = 222**.
- Only squarefree moduli are summed.

### Hypothesis (B) — Type II

> **(B)** Σ_m | Σ_{N<n≤2N, mn≤x} γ(n)μ(mn)a_{mn} | ≤ A(x)(log x)^{−222}
>
> for every N with **(B1)** Δ^{−1}√D < N < δ^{−1}√x, some δ = δ(x) ≥ 2,
> Δ = Δ(x) ≥ 2, where **(B2)** γ(n) = γ(n,C) = Σ_{d|n, d≤C} μ(d), required for
> every C with **(B3)** 1 ≤ C ≤ xD^{−1}.  *(pp. 1043–1044)*

Answering the questions the skeleton left open:

- **Is α_m arbitrary?** Effectively yes — the absolute value sits outside the
  m-sum, which is the sup over |α_m| ≤ 1. The repo's `mobius_bilinear` is the
  right measurement and `worst_case_signs` is not. ✅ as built.
- **Is β = μ?** Essentially. The inner coefficient is γ(n)μ(mn), a
  Möbius-type weight with a short divisor truncation, not an adversary. ✅
- **Range of N:** √D up to √x, up to the Δ, δ factors.

### Conclusion delivered

> **Theorem 1** *(p. 1044)*. Σ_{p≤x} a_p log p = HA(x){1 + O(log δ / log Δ)},
> with H = Π_p (1 − g(p))(1 − 1/p)^{−1}.

An **asymptotic**, not a lower bound. "In practice (B) can be established … for
δ = (log x)^α and Δ = x^η", giving error O(log log x / log x).

### Theorem 2 — the non-squarefree version

Since x² + 1 violates (1.16), §9 is the relevant version. It replaces (1.16) by
(9.1) and adds *(p. 1059)*:

> **(9.2)** Σ_{n≤x} aₙ² ≤ x^{−2/3}A(x)², or the weaker sufficient
> **(9.3)** Σ_{n≤x} aₙ² ≤ x^{−1}A(x)²D(x)^{1/2};
> **(R3)** Σ³_{d<DL²} |r_d(t)| ≤ A(x)L^{−2}, L = (log x)^{224}, cubefree moduli.

> **Theorem 2** *(p. 1059)*. Assume (1.4), (1.6), (1.8), (1.9), (B), (B1),
> (B2), (B3), (9.1), (9.2), (R3), (R1). Then (1.17) holds.

**[X2Y4]** §2 (pp. 953–954) restates this applied form: (2.9) with
**(2.10) x^{2/3} < D < x**, and the bilinear hypothesis (2.11) over
**(2.14) Δ^{−1}√D < N < δ^{−1}√x**.

---

## Verification against A = {x² + 1}

Take aₙ = #{m ≥ 1 : m² + 1 = n}, so aₙ ∈ {0,1} and A(x) = ⌊√(x−1)⌋ ≍ x^{1/2}.
Note A's ρ(d) is exactly [X2Y4]'s ρ(d), and g(d) = ρ(d)/d.

**Three independent failures, all the same fact.**

1. **(R) + (R1).** Note B: Σ_{d≤D}|r_d| ≍ D, so (R) needs D ≪ x^{1/2}(log x)^{−222}.
   (R1) needs D > x^{2/3}. **Empty.**
2. **(9.2).** LHS = Σ aₙ² = A(x) = x^{1/2}. RHS = x^{−2/3}A(x)² = x^{1/3}.
   Needs x^{1/2} ≤ x^{1/3}. **False.**
3. **(9.3), the weaker fallback.** RHS = x^{−1}·x·D^{1/2} = D^{1/2}. Needs
   D ≥ x, contradicting (R1)'s D < x — and a fortiori D ≤ x^{1/2}. **False.**

Every one traces to A(x) = x^{1/2} < x^{2/3}. This is not a normalisation
artefact and not repairable by reformulating: the set of Gaussian integers on
Im z = 1 with norm ≤ x has x^{1/2} elements, and there is no denser
presentation of the same problem to sift instead.

## What this does to the Type II picture

Even waiving (R1) and taking the largest conceivable D = x^{1/2}, (B1) would
require N ∈ (x^{1/4}, x^{1/2}) up to δ, Δ, i.e. **M = x/N ∈ (x^{1/2}, x^{3/4})**.
In the repo's variables (X = √x = |A|) that is **M ∈ (X, X^{3/2})** — and
[Note H](note-H-numerical-pilot.md) measured, at X = 2×10⁴:

| M range | S_μ | A(x) = X | S_μ / A(x) |
|---:|---:|---:|---:|
| [10⁴, 10⁵) | 18 519 | 20 000 | 0.93 |
| [10⁵, 10⁶) | 20 058 | 20 000 | 1.00 |
| [10⁶, 10⁷) | 20 273 | 20 000 | 1.01 |

**No saving whatever, where (B) demands a factor (log x)^{−222}.** The
cancellation Note H found (≍ √(MX), θ < 1) lives at M < X — *outside* the
range the sieve needs. So Note H's earlier reading ("the obstruction looks
technical rather than structural") was measuring the wrong window and has been
corrected.

The reason is structural and is the same κ of [Note F](note-F-failure-localisation.md):
(B1) forces N ≤ √x, hence M ≥ √x; cancellation in the m-sum needs m to divide
more than one element of A, i.e. M ≤ A(x). Both hold at once **iff
A(x) > √x, i.e. iff κ = A(x)²/x > 1** — and for x²+1, κ = 1, so the two
constraints meet only at the single point M = A(x). The invariant derived in
Note F turns out to be exactly the condition for (B1)'s range to be
non-degenerate. That was not built in; it is a genuine consistency check.

## Consequences for the plan

The plan's §1.5 checkpoint asks Note C for "a precise bilinear inequality whose
proof would imply the theorem via the asymptotic sieve". **No such inequality
exists**, because no Type II input can rescue a sequence for which (R1) is
unsatisfiable. Concretely:

- **Step 2 as written is attacking the wrong half.** Notes E, F, G and H
  concern hypothesis (B). The binding constraint is (R1). Note F's C₄-free
  lemma remains true and remains the correct localisation *of the bilinear
  failure* — but the bilinear failure is downstream.
- **The plan's §1.3.2 prediction was right and its §1.5 target was not.** The
  Type I level really is x^{1/2−ε}; what the plan did not anticipate is that
  x^{1/2} is below the sieve's own floor.
- **The research problem is restated.** Not "prove a bilinear estimate for
  x²+1", but: **is there a version of the asymptotic sieve for primes valid for
  sequences with A(x) ≍ x^{1/2}?** Everything in [ASP] between (R1) and
  Theorem 1 is where the 2/3 is spent; identifying which step needs it is the
  next concrete task, and is a well-posed reading exercise on a 25-page paper.

## Open

- **[VERIFY]** Where in [ASP] §§3–8 is x^{2/3} actually used? Is it a genuine
  barrier of the method or an artefact of the chosen decomposition? This is now
  *the* question, and it replaces Step 2 as the priority.
- **[VERIFY]** Heath-Brown's x³ + 2y³ has A(x) ≍ x^{2/3}, exactly at the
  threshold. Does he use [ASP], or a separate argument? If separate, why —
  and does that argument have more room at x^{1/2}? Inferred from the density,
  not read from the paper.
- **[VERIFY]** [X2Y4] Prop. 3.5 gives D = x^{3/4−5ε} = A(x)^{1−ε}, called
  "apart from the ε, the best that one can hope for" (p. 962). Confirms the
  D ≤ A(x) ceiling is real and attained. Check whether any later work relaxes
  (R1) below 2/3.

## Adversarial review

- *Two-parameter freedom smuggled in?* No — this note only reads hypotheses.
- *Where is parity broken?* In [ASP] by hypothesis (B); §1 is explicit that (B)
  is the new axiom and (R) the classical one. The finding here is that x²+1
  fails the *classical* half, so it never reaches the parity-breaking machinery.
- *Is the failure really unfixable, or an artefact of choosing aₙ as an
  indicator?* Weighting cannot help: (9.2) compares Σaₙ² to A(x)², and any
  reweighting that inflates A(x) inflates Σaₙ² at least as fast by
  Cauchy–Schwarz. Worth writing out properly.
- *Could a different sieve apply?* Yes, and that is the honest next question —
  [ASP] is one theorem, not a proof of impossibility. Iwaniec 1978 (P₂) already
  works at this density with a classical sieve; what is unavailable at
  A(x) = x^{1/2} is the parity-breaking upgrade.
