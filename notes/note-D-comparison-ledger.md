# Note D — Comparison ledger

*Plan §1.3.4. Status: draft. Supported by
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
| Type I actually achieved | **cannot exceed Q^{1/2}** — no second variable to sum | **beyond** the trivial level, by summing over b | **←** |
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

1. **In Type I**, to sum over the second variable and beat the trivial level.
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

**[VERIFY]** — κ for Heath-Brown's set is computed from |A| ≍ Q^{2/3} and not
checked against the paper; and the claim that FI's Type I gain comes from
summing over b needs a page reference. That is the single most load-bearing
unverified line in the ledger.

## Adversarial review

- *Two-parameter freedom smuggled in?* This note is the audit for exactly that,
  so the risk runs the other way: attributing too much to the freedom. The
  lines marked "same" are the control, and they are genuinely the same.
- *Where is parity broken?* In the a² + b⁴ column, at the bilinear form. The
  ledger's value is that it localises the difference to two lines of the same
  nature.
- *Is κ a real invariant or a coincidence of three data points?* Three
  sequences is not evidence. What makes κ more than numerology is the degree
  computation in Note F, which derives it rather than fitting it. Still worth
  testing against a fourth sequence with a known outcome — e.g. all of Z[i]
  (κ = Q), or a thin set of density strictly between 1/2 and 3/4. **[VERIFY]**
