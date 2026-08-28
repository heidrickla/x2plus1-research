# Note D — Comparison ledger

*Plan §1.3.4. Status: draft; Type I lines and the density hierarchy checked
against [ASP], [X2Y4] and [HB] — see [Note C](note-C-requirements.md) for the
citations. Supported by
[`experiments/exp03_density_ledger.py`](../experiments/exp03_density_ledger.py).*

## The two sequences in one language

a² + b⁴ = a² + (b²)² = N(a + b²i). So both problems sift Gaussian integers:

| | x² + 1 | a² + b⁴ |
|---|---|---|
| set | {z ∈ Z[i] : **Im z = 1**} | {z ∈ Z[i] : **Im z is a perfect square**} |
| parameters | x | a, b |
| \|A\| at norm bound Q | Q^{1/2} | ≍ 0.874·Q^{3/4} |
| measured \|A\| at Q = 10⁷ | 3 162 | 153 890 |

FI sift a *parabola* of imaginary parts; this project sifts a single horizontal
line. Everything below is a consequence of that one difference.

## The ledger

Lines marked **←** are where the two-parameter freedom of (a, b) is used.

| line | x² + 1 | a² + b⁴ | |
|---|---|---|---|
| local densities g(d) | 1/N(d) on admissible d | 1/N(d) on admissible d | same |
| admissible ideals, norm ≤ D | ~(3/2π)D | same congruence condition | same |
| Type I error per modulus | ≤ **1**, sharp | ≍ Q^{1/4} trivially — one per value of b | |
| Type I error, summed | ≍ D | ≍ D·Q^{1/4} trivially | |
| Type I as a fraction of \|A\| | D/Q^{1/2} | D·Q^{1/4}/Q^{3/4} = D/Q^{1/2} | same trivially |
| Type I actually achieved | **cannot exceed Q^{1/2}** — no vector to average over | **beyond** the trivial level, by a Davenport–Halberstam large sieve over the roots ν of ν²+1 ≡ 0 (mod d) | **←** |
| rectangle density κ = \|A\|²/Q | **1** | Q^{1/2} | **←** |
| max_M min(D_m, d_n) = √κ | **1** (measured 1.26) | Q^{1/4} (predicted 48.7, measured 41.2) | **←** |
| max off-diagonal Gram entry | **1** (C₄-free — proved) | **667** at Q = 10⁶ | **←** |
| dispersion has a main term? | **no** | yes | **←** |
| measured θ(μ), N(m) ∈ [10³,10⁴), Q = 10⁷ | 0.966 | 0.803 | |
| parity broken by | — | the bilinear form, via the above | **←** |

## Reading the ledger

The two-parameter freedom is **not** used where one might first expect. The
local data is identical: same admissible ideals, same densities, same Euler
factors. The *trivial* Type I bookkeeping is also identical once normalised by
|A|. The freedom is used in exactly two places, and they are the same place
twice:

1. **In Type I**, to supply a vector of coefficients for a large sieve to
   average over, beating the trivial level.
2. **In Type II**, to make the incidence matrix thick, so that the Gram matrix
   G(n₁, n₂) has a main term for dispersion to work on.

Both are "there is a second variable to sum over". For x² + 1 there is not, and
[Note F](note-F-failure-localisation.md) shows the second failure is not a
matter of degree: G ≤ 1 identically, by a two-line proof.

## The density hierarchy, restated

The plan says the target set "has density x^{1/2}, thinner than anything yet
handled". The ledger sharpens *thinner* into a threshold:

| sequence | \|A\| | κ = \|A\|²/Q | status |
|---|---|---|---|
| a² + b⁴ (FI 1998) | Q^{3/4} | Q^{1/2} | done |
| x³ + 2y³ (Heath-Brown 2001) | Q^{2/3} | Q^{1/3} | done |
| x² + 1 | Q^{1/2} | **1** | open |

κ > 1 is exactly the condition for *some* dyadic split to give an incidence
matrix that is more than a matching. Q^{1/2} is not merely thinner — it is the
critical density, and it sits on the wrong side of the threshold by exactly Q⁰.

**There is a second, stronger threshold, and it comes from the literature
rather than from this repo.** [Note C](note-C-requirements.md) reads off from
Friedlander–Iwaniec that the asymptotic sieve for primes requires a level of
distribution D > Q^{2/3} (hypothesis (R1)), while for a thin sequence (R)
cannot hold beyond A = |A|. So [ASP] applies only when **|A| > Q^{2/3}**.

Heath-Brown ([HB] p. 2) uses exactly this exponent, calling it α(f), and places
the four problems on it himself: Dirichlet at α = 1, FI at α = 3/4, his own
theorem at α = 2/3, "while the conjecture that x² + 1 takes infinitely many
prime values has α = 1/2". So this ledger's frame is the literature's.

| sequence | α = \|A\| exponent | κ > 1? (Type II non-degenerate) | (R1): D > Q^{2/3}? | level achieved |
|---|---|---|---|---|
| a² + b⁴ | 3/4 | ✅ | ✅ met | Q^{3/4−5ε} ([X2Y4] Prop. 3.5) |
| x³ + 2y³ | 2/3 | ✅ | ❌ "not quite met" — short by Q^ε | Q^{2/3−ε} ([HB] Lem. 2.1–2.2) |
| x² + 1 | **1/2** | ❌ (κ = 1) | ❌ short by **Q^{1/6}** | Q^{1/2}(log Q)^{−222} |

**The two thresholds are not equally hard.** (R1)'s 2/3 is a hypothesis of one
theorem: Heath-Brown hit it, judged it "possible that [it] might be relaxed",
and wrote his own sieve instead ([HB] p. 3). κ > 1 is a property of the
sequence: Note F's C₄-free lemma is a theorem and survives any change of sieve.
So the Type I line is the one that binds *for [ASP] specifically*, and the
Type II line is the one that binds *for the problem*.

All three of this note's **[VERIFY]**s are now discharged, one by correcting an
error.

*Density.* Heath-Brown's α is the same exponent and he places all four problems
on it himself ([HB] p. 2), so the hierarchy is quoted, not inferred.

*Level achieved.* FI reach D = Q^{3/4−5ε} ([X2Y4] Prop. 3.5, p. 962), "apart
from the ε, the best that one can hope for"; Heath-Brown reaches Q^{2/3−ε}
([HB] Lem. 2.1–2.2, p. 5). So the D ≤ |A| ceiling is real and attained in both
solved cases.

*Mechanism — previously stated wrongly.* This note guessed the gain came from
Poisson summation in b. It does not. [X2Y4] §3 (p. 957) observes that for
moduli in a short interval 8D/9 < d ≤ D the points ν/d with ν² + 1 ≡ 0 (mod d)
are spaced by 1/4D rather than 1/D², and applies **the Davenport–Halberstam
large sieve** to them, giving Lemma 3.2:

> Σ_{D<d≤2D} Σ_{ν²+1≡0 (d)} |Σ_{n≤N} α_n e(νn/d)|² ≪ (D + N)‖α‖².

Note what those ν are: the roots of ν² + 1 ≡ 0, i.e. exactly this repo's
admissible ideals ([Note A](note-A-dictionary.md)). The structure FI exploit is
the *same* structure x² + 1 has. What differs is that they have a **vector α**
— supplied by the second variable — for the large sieve to average over. For
x² + 1 that vector has one entry, and a large sieve over one point is the
trivial bound. **That is the two-parameter freedom, stated exactly**, and it is
a sharper statement than the one this note originally guessed.

## Is κ a law, or three coincidences?

Three published sequences cannot distinguish the two. So the family

> A_k = { a + b^k i : a² + b^{2k} ≤ Q },  |A_k| ≍ Q^{1/2 + 1/(2k)}

was swept — it interpolates between α = 1 (k = 1, all of Z[i]), α = 3/4 (k = 2,
the FI set), α = 2/3 (k = 3, Heath-Brown's density) and, as k → ∞, α = 1/2,
which is the line Im z = 1. κ predicts max_M min(D_m, d_n) ≍ √κ = Q^{1/(2k)}.
Measured at Q = 10⁷ (`experiments/exp04_kappa_family.py`):

| sequence | α | \|A\| | √κ predicted | max min-degree | ratio | C₄-free? |
|---|---:|---:|---:|---:|---:|:--:|
| a² + b⁴ | 0.750 | 153 890 | 48.66 | 41.22 | **0.85** | no |
| a² + b⁶ | 0.667 | 40 661 | 12.86 | 11.45 | **0.89** | no |
| a² + b⁸ | 0.625 | 20 676 | 6.54 | 5.81 | **0.89** | no |
| a² + b¹⁰ | 0.600 | 12 951 | 4.10 | 3.78 | **0.92** | no |
| a² + b¹² | 0.583 | 9 400 | 2.97 | 2.72 | **0.91** | no |
| x² + 1 | 0.500 | 3 162 | 1.00 | 1.26 | 1.26 | **yes** |

The ratio is constant to within 8% across a factor of 16 in √κ. **κ is a law,
not a coincidence of the three published densities** — and the incidence graph
becomes a forest exactly at α = 1/2, the endpoint the family approaches but
never reaches.

## The fourth published sequence, and the limit of κ

The [VERIFY] asking for "a fourth sequence with a known outcome" is discharged,
and by a better sequence than the family above supplies: only
k = 2 in that family has a known outcome, so it tests the *law* but not the
*criterion*. Merikoski's a² + (b²+1)² (arXiv:2112.03617, 2022) has one, and its
density is deliberately identical to a² + b⁴. Measured by
[`exp08`](../experiments/exp08_merikoski_ledger.py) at Q = 10⁷:

| sequence | \|A\| | κ | √κ | max min-degree | ratio | C₄-free? | outcome |
|---|---:|---:|---:|---:|---:|:--:|---|
| a² + b⁴ | 153 890 | 2368.2 | 48.66 | 41.22 | 0.85 | no | asymptotic, Type II to X^{1/2−η} |
| a² + (b²+1)² | 153 856 | 2367.2 | 48.65 | 40.12 | 0.82 | no | lower bound, Type II to X^{1/3−η} |
| x² + 1 | 3 162 | 1.0 | 1.00 | 1.26 | 1.26 | **yes** | open |

The first two rows agree in every column to within 3%, and the literature
separates them by a sixth in the Type II exponent. **So κ is a necessary
condition and not a sufficient one**, and this ledger should not be read as
predicting outcomes. What κ measures is whether there is bilinear structure to
work with at all; how much of it is usable is decided by the singularity type
of the Type II curve, which no degree count sees. [Note K](note-K-merikoski.md)
has the mechanism.

The same note identifies √κ with the range B of the Poisson summation variable
in [MER] p. 4 — for A = {a + f(b)i} the identity κ = B² is immediate — which is
what the "one point" remark above amounts to in the published arguments.

Status: this is `measured`, not `proved` — the degree computation is a
heuristic. The proved statement in the neighbourhood is
[Note F](note-F-failure-localisation.md)'s C₄-free lemma. See
[`research_state/claims.json`](../research_state/claims.json).

## Adversarial review

- *Two-parameter freedom smuggled in?* This note is the audit for exactly that,
  so the risk runs the other way: attributing too much to the freedom. The
  lines marked "same" are the control, and they are genuinely the same.
- *Where is parity broken?* In the a² + b⁴ column, at the bilinear form. The
  ledger's value is that it localises the difference to two lines of the same
  nature.
- *Is κ a real invariant or a coincidence of three data points?* **Answered
  above**, and more strongly than the objection asked: swept across the family
  a² + b^{2k} for k = 2…6, the predicted ratio holds to within 8% over a factor
  of 16 in √κ. Still `measured`, not `proved`.
