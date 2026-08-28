# Note M — Where the μ-cancellation lives, and what its easiest case already is

*Added. Status: draft. Rests on [Note H](note-H-numerical-pilot.md)'s √(MX) law,
[Note J](note-J-mobius-in-progressions.md)'s reduction, and two sources located
by a parallel session and then **read at source here** before being recorded.*

The repo has carried, in different notes, two facts that were never put next to
each other:

- **[Note H]**: S_μ(M) := Σ_{N(m)≍M} |Σ_n μ(n)·1[mn ∈ A]| ≍ √(MX).
- **[Note F]**: in the window [ASP]'s (B1) requires, there is *no saving at all*
  — measured S_μ/A(x) = 0.93, 1.00, 1.01.

Written as exponents, in the repo's normalisation (Q the norm bound,
X = Q^{1/2} = |A|, M = Q^θ), those are the same statement, and it is sharper
than either.

## The two windows are complements

The trivial bound for S_μ(M) is the edge count, ≍ X up to logs. So

> **saving = X / √(MX) = √(X/M) = Q^{(1/2 − θ)/2}.**

A power saving for every θ < 1/2, degrading continuously, and **exactly zero at
θ = 1/2**.

Now place the two frameworks on the same axis:

| | requires | in θ |
|---|---|---|
| [ASP] (B1) | M ≥ √x = Q^{1/2} = X | **θ ≥ 1/2** |
| [FM] (1.1) | 0 ≤ θ < 1/2 | **θ < 1/2** |
| μ-cancellation (measured) | saving Q^{(1/2−θ)/2} | **θ < 1/2** |

> **The μ-cancellation holds on precisely the range Ford–Maynard's framework
> admits, and vanishes at precisely the point where the asymptotic sieve's
> bilinear hypothesis begins.**

That is why the repo kept getting two different answers about whether the μ-sum
"has a saving". It does, everywhere [FM] can use one; it does not, anywhere
[ASP] asks for one. `no-saving-in-required-window` and `sqrt-MX-law` are the
same law read at the two ends of the same interval.

The mechanism is the one [Note L](note-L-over-Z.md) makes general: at θ = 1/2
the modulus is M ≍ X = |A|, so the mean degree is 1 and the incidence graph is
the forest. θ = 1/2 is where κ = 1 bites, on the nose.

## What that would buy, stated as a conditional and not more

Suppose — this is the conditional — that [FM]'s (II) could be weakened from
*arbitrary bounded* ξ_m, κ_n to *arbitrary ξ_m with κ_n = μ(n)*. Then the
measured law supplies a Type II range on any [θ, θ+ν] ⊂ [0, 1/2), so x² + 1
would sit at

> (γ, θ, ν) = (1/2, 0, ν) for any ν < 1/2,

which is **above** Duke–Friedlander–Iwaniec's (1/2, 0, 1/3) in [FM]'s own
Table 1 — and DFI's row is a success. Their Theorem 2.5 (p. 7) gives
C⁻_bd(P_ε; ϱ) = 1 + O(ε) for P = (1/2, 0, ν) with 1/3 ≤ ν < 1/2 and
divisor-bounded weights, and this sequence's indicator *is* divisor-bounded
(registry: `divisor-bounded-escape-unavailable`, where that fact is recorded
while being useless for the arbitrary-coefficient version).

**Read this correctly.** Substituting a weaker hypothesis into a theorem is not
valid reasoning, and no claim is being made that Theorem 2.5 applies. The
content is only that *the parameters land in the region their machinery already
handles*, so the entire distance between "x² + 1 is open" and "x² + 1 is inside
a solved parameter regime" is the difference between arbitrary κ_n and κ_n = μ.
That is exactly the gap [FM] p. 18 names as missing from the theory:

> "It would be naturally be desirable to have a theory which can incorporate
> such additional arithmetic information…"

Two things are needed to make it unconditional, and both are hard:

1. **the μ-Type II as a theorem**, not a measurement; and
2. **a sieve that needs only μ-coefficients** — [FM]'s footnote 1 expects the
   traffic to run the other way, and [Note F] proves that here it cannot.

## Condition 1 is not a technicality: its easiest case is a named open problem

Set θ = 0. Then the inequality of [Note F]'s Question F reads

> |Σ_{x ≤ X} μ(x²+1)| ≪_A X (log X)^{−A},

using `mobius-ideal-equals-mobius-norm`. Drop the log-power and it is Chowla's
assertion for x² + 1 — and **that is wide open**. Teräväinen,
[arXiv:2010.07924v4](https://arxiv.org/abs/2010.07924), pp. 1–2, on
Σ_{n≤x} λ(P(n)) = o(x):

> "Since (1.1) contains Chowla's famous conjecture on k-point correlations and
> is **wide open for any polynomials with nonlinear irreducible factors**, it
> makes sense to study Conjecture 1.2 as a stepping stone in its direction."

So the Type II input this repo needs is not an unproven estimate of the usual
kind. **Its θ → 0 endpoint is an open problem of independent standing, and for
this sequence the trivial bound has never been beaten by any amount, at any
level, signed or absolute.** What is known is qualitative: λ(P(n)) takes each
sign infinitely often for some classes of P, with no rate.

That is the most honest single sentence about the project's position, and it
should be read alongside the standing warning: it says nothing about whether
x² + 1 is prime infinitely often.

## Scope correction: "the difficulty is the absolute values" was too broad

[Note J] and `difficulty-is-the-absolute-values` say the signed sum is under 2%
of the absolute-value sum, and conclude that the |·| is the whole difficulty.
True here — but the *reason* is not that absolute values are intrinsically
hopeless. Bombieri–Vinogradov in exactly that norm is known for μ on the
density-1 sequence. Granville–Shao,
[arXiv:1703.06865v2](https://arxiv.org/abs/1703.06865), p. 2, having displayed

> Σ_{q∼Q} max_{a:(a,q)=1} |Δ(f,x;q,a)| ≪ x/(log x)^A for Q ≤ x^{1/2}/(log x)^B,

write: **"The analogous result is known to hold when f = μ, the Möbius
function"**.

So the correct statement is: *the absolute values are the difficulty **for this
sequence***, and what makes them so is the composition with a quadratic. The
structural reason is worth recording because it closes a whole direction:
**μ(n²+1) is not a multiplicative function of n**, so Granville–Shao's theory,
and multiplicative-function machinery generally, does not apply *as stated* —
not "applies but is too weak".

## The two measurements of the law are the same sum, not two normalisations

§1 rests on S_μ(M) ≍ √(MX), which is `extrapolated`, and the honest worry has
been that its *direct* measurement (exp02) spans less than a decade,
X = 2×10⁴ … 10⁵, while carrying the whole θ-axis argument. The four-decade
support was recorded as holding "in the equivalent per-progression
normalisation" (exp05). That understates it. **The two are the same sum.**

> If N = x²+1 is squarefree and m | N, then gcd(m, N/m) = 1, so
> μ(N) = μ(m)·μ(N/m), and μ(m)² = 1 gives
>
>     μ((x²+1)/m) = μ(m)·μ(x²+1).

Inside S_μ(M) = Σ_m |Σ_x μ((x²+1)/m)| the factor μ(m) is a constant of modulus 1
on the inner sum, so it **drops out under the absolute value**, leaving

    S_μ(M) = Σ_m |Σ_{x ≡ ±r (mod m)} μ(x²+1)|,

which is exactly what exp05 measures per progression. Machine-checked in
`tests/test_arithmetic_facts.py::test_mobius_of_the_cofactor_factors_when_the_value_is_squarefree`.

**The two differ only on the non-squarefree x, and that correction is an
asymptotic constant.** Only p = 2 and p ≡ 1 (mod 4) admit p² | x²+1, each
costing density 2/p², so a sieve truncated at P = 20 000 has error under 10⁻⁵.
Measured:

| X | density of squarefree x²+1 | change |
|---:|---:|---:|
| 10⁴ | 0.895200 | |
| 10⁵ | 0.894900 | −3.0×10⁻⁴ |
| 10⁶ | 0.894860 | −4.0×10⁻⁵ |
| 10⁷ | 0.894847 | −1.3×10⁻⁵ |

Flat to four places. At X = 4000 over the band [300, 600) the aggregate ratio of
the two sums is 0.884 — a constant-order correction, as the density predicts.

> **A constant factor cannot move an exponent.** So exp05's four decades bear on
> the exponent in S_μ(M) ≍ √(MX) directly, and the range behind §1 is four
> decades rather than one.

What is *not* improved: the law is still `extrapolated`. Extrapolating a fitted
exponent from 10⁷ to all X is the unsupported step, and it is unchanged. What
changes is that the fit is no longer resting on a single decade.

## Adversarial review

- *Where is two-parameter freedom smuggled in?* Nowhere, and the θ-axis makes
  its absence quantitative: the saving dies exactly at θ = 1/2, which is where
  the mean degree reaches 1.
- *Is the conditional in §2 doing illegitimate work?* It would be if it claimed
  Theorem 2.5 applies. It claims only where the parameters land. The section
  says so twice because this is the repo's characteristic failure mode.
- *Does §1 double-count?* No — `sqrt-MX-law` is `extrapolated` and
  `no-saving-in-required-window` is `rigorous_finite`, and this note derives no
  new number from them, only the observation that their windows are
  complements.
- *How much does §1 rest on a fit?* All of it, and the fit's range matters. The
  saving Q^{(1/2−θ)/2} is read straight off S_μ(M) ≍ √(MX), which is
  `extrapolated`. Its direct measurement (exp02) spans **less than one decade**,
  X = 2×10⁴ … 10⁵. The section above closes that gap properly: exp05's four
  decades are not an analogue but the *same sum*, since μ((x²+1)/m) =
  μ(m)·μ(x²+1) on squarefree values and the μ(m) dies under the absolute value.
  The residue is the non-squarefree x, whose density is flat at 0.8948 to four
  places over 10⁴…10⁷, hence a constant factor, hence unable to move an
  exponent. The extrapolation to all X remains the unsupported step.
- *Is the Chowla remark a counsel of despair?* It is a scoping fact. It rules
  out reading Question F as "an estimate someone could plausibly supply", which
  earlier drafts came close to doing, and it says where the difficulty sits
  relative to the rest of the subject.
- *Both new sources were located by a parallel session.* Both were then fetched
  and read here before being quoted; neither is recorded on the strength of the
  other session's report.
