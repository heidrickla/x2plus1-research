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

**And the obvious escape from that is closed too, which is worth writing down
because it is the first thing a reader will try.** The objection runs: μ *is*
multiplicative on the integers, so do not index by n — index by the integer
N = x²+1 itself and apply Granville–Shao to the multiplicative function μ. The
reindexing is legitimate; the theorem still does not apply, for a second and
independent reason. Their statement is a **density-1** one: the inner sum runs
over *all* n ≤ x in a progression. Ours runs over

> {x² + 1 : x ≤ X}, which has X elements inside [1, X²+1] — **density X^{−1}**,

so what is needed is a Bombieri–Vinogradov theorem for μ **on a sparse set**,
which is a different and harder statement, not an instance of theirs. This is
the same α = 1/2 sparsity that blocks [ASP] and [DFI], arriving here in
multiplicative-function clothing.

So the direction is closed twice over: reindex by n and μ stops being
multiplicative; reindex by N and the sequence stops being density 1. Neither
horn is a strength-of-result issue.

## The law's upper bound is a Cauchy–Schwarz reduction, not a fit

*`sqrt-MX-law` is `extrapolated`, and §1's whole θ-axis argument rests on it.
What §1 actually needs is only the **upper** bound S_μ(M) ≪ √(MX). That half is
not a fit: it follows from Cauchy–Schwarz plus a second-moment statement about
the same Gram structure [Note F](note-F-failure-localisation.md) and
[Note L](note-L-over-Z.md) study.*

Write T_m = Σ_{x ≤ X, m | x²+1} μ(x²+1), so S_μ(M) = Σ_{m ∼ M} |T_m|. Then

> **S_μ(M)² ≤ #{m ∼ M} · Q₂**,  Q₂ := Σ_{m ∼ M} T_m²,

and expanding the square gives the **exact** decomposition

> **Q₂ = DIAG + OFF**, DIAG = #{(m,x) : m ∼ M, m | x²+1, x²+1 squarefree},
> OFF = Σ_{x≠y} μ(x²+1)μ(y²+1) · G_M(x,y),  G_M(x,y) = #{m ∼ M : m | gcd(x²+1, y²+1)}.

**OFF is built from exactly the Gram entries of the rational incidence graph** —
the object Prop L.1 bounds and Theorem O.3′ constrains. Measured at X = 2×10⁵:

| M | #m | Q₂ | DIAG | OFF/DIAG | S_μ | √(#m·Q₂) | S_μ/CS |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 200 | 38 | 73 835 | 48 859 | 0.511 | 1 291 | 1 675 | 0.771 |
| 800 | 137 | 55 298 | 49 902 | 0.108 | 2 166 | 2 752 | 0.787 |
| 3 200 | 513 | 56 505 | 50 981 | 0.108 | 4 011 | 5 384 | 0.745 |
| 12 800 | 1 917 | 53 912 | 50 714 | 0.063 | 7 566 | 10 166 | 0.744 |
| 51 200 | 7 227 | 52 527 | 50 581 | **0.038** | 14 537 | 19 484 | 0.746 |

Three things to read off. **DIAG is flat in M** — ≈ 5.05×10⁴ across a 256-fold
range — because each x has O(1) divisors in a dyadic band, so DIAG ≍ X.
**OFF is small relative to DIAG**, |OFF|/DIAG ≤ 0.51 and mostly under 0.11. And
**Cauchy–Schwarz is tight**, S_μ/CS ≈ 0.75 at every M, so the |T_m| are
equidistributed and no single modulus carries the sum.

*Not monotone, and the first draft of this paragraph said it was.* OFF is a
**signed** sum and changes sign with X and M: at X = 10⁵ the same three bands
give −0.166, −0.126, +0.095. The reduction needs |OFF| ≪ DIAG, which is what is
observed; reading one run's monotone column as a trend was an over-read, and
[`exp15`](../experiments/exp15_cauchy_schwarz_reduction.py) now reports the
worst |OFF|/DIAG rather than the endpoints.

So the upper bound reduces to one input:

> **If OFF = o(DIAG), then Q₂ ∼ DIAG ≍ X and S_μ(M) ≪ √(#{m ∼ M} · X).**

And #{m ∼ M : −1 is a QR mod m} ≍ M/√(log M) by Landau–Ramanujan, giving the
slightly sharper **S_μ(M) ≪ √(MX/√(log M))**.

**Status, precisely.** Cauchy–Schwarz and the decomposition are exact. DIAG ≍ X
is a standard divisor count. #m ≍ M/√(log M) is Landau–Ramanujan. **Only
OFF = o(DIAG) is measured rather than proved** — so this does not promote
`sqrt-MX-law`, and the note should not claim it does. What it changes is *what
would have to be proved*: not an asymptotic law fitted over four decades, but a
cancellation statement for Σ_{x≠y} μμ·G_M(x,y), where the G_M are bounded and
are the repo's own object. That is a reduction of the θ-axis to the Gram axis,
and it is the first connection between the two halves of this repo.

**How much easier the new statement is, honestly: possibly not at all.** The
counting bound on OFF — bound every G_M(x,y) and discard the signs — gives
|OFF| ≤ Σ_{m∼M}(|S_m|² − |S_m|), and that is **11× to 1988× too weak** across
the same bands:

| M | DIAG | trivial \|OFF\| bound | bound/DIAG | measured \|OFF\|/DIAG |
|---:|---:|---:|---:|---:|
| 200 | 64 515 | 1.28×10⁸ | 1988 | 0.511 |
| 3 200 | 66 242 | 1.05×10⁷ | 159 | 0.108 |
| 51 200 | 66 190 | 7.36×10⁵ | 11.1 | 0.038 |

So **OFF = o(DIAG) is itself a μ-cancellation statement, not a divisor count**.
The reduction converts one cancellation problem into another. What it buys is
shape, not difficulty: the new statement is a bilinear sum in μ(x²+1)μ(y²+1)
with **bounded, explicitly-studied weights** G_M(x,y), rather than an asymptotic
law fitted over four decades. Whether that is a route or a restatement is not
something this note can settle, and it should not be quoted as progress on the
θ axis.

**And it explains the root-grouping gap.** The measurement above is the
*per-modulus* normalisation — every root of −1 mod m sits inside one absolute
value. Run the same Cauchy–Schwarz per *progression* and the diagonal is
unchanged (it counts incidences either way), so the only thing that moves is the
outer count:

> S_mod ≪ √(#modules · X),  S_prog ≪ √(#progressions · X),
> hence **S_prog/S_mod ≍ √(#prog/#mod) = √(mean roots per modulus)**.

That is precisely the ratio the parallel session measured empirically — tracking
√(#prog/#mod) to within 2% across ten doublings, with the mean root count
climbing 2.652 → 3.694. So the root cancellation is not an extra phenomenon on
top of the law; it is the same Cauchy–Schwarz bound read with a different outer
index, and Cauchy–Schwarz being tight to 25% in both is why the ratio is sharp.
It also accounts for the sign of their exponent gap: per-modulus 0.4803 against
per-progression 0.5046, i.e. **below** √(MX), matching √(#m·X) with
#m ≍ M/√(log M).

*(The lower bound S_μ(M) ≫ √(MX) is untouched by this and remains fitted. §1
does not use it.)*

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

    S_μ(M) = Σ_m |Σ_{x ≡ ±r (mod m), r over ALL roots} μ(x²+1)|.

Machine-checked in
`tests/test_arithmetic_facts.py::test_mobius_of_the_cofactor_factors_when_the_value_is_squarefree`.

**But that is not quite exp05's quantity, and an earlier version of this section
said it was.** S_μ puts **one absolute value per modulus**, spanning every root
of −1 mod m at once; exp05 computes ρ **per (q, root) progression**. When a
modulus carries several roots they cancel against each other inside S_μ's
absolute value, and exp05 never sees that. Measured at X = 10⁶ over ten
doublings of M:

| | M-exponent | S/√(MX) drift |
|---|---:|---:|
| per progression (exp05's grouping) | **0.5046** | ×1.032 |
| per modulus (S_μ's own definition) | **0.4803** | ×0.873 |

The gap is entirely the root cancellation, and it is square-root exact:
S_prog/S_mod tracks √(#prog/#mod) to within 2% across the range, while the mean
root count per modulus climbs from 2.652 to 3.694. So

> **S_μ(M) ≍ √(MX) / √(mean roots per modulus)** — very slightly *below* √(MX),
> i.e. slightly *more* cancellation than the law claims, which makes Note M's
> saving a conservative estimate rather than an optimistic one.

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
> the exponent of the *per-progression* law directly, and the range behind §1 is
> four decades rather than one — with the root-grouping caveat above, which
> shifts the aggregate exponent by −0.02 in the conservative direction.

What is *not* improved: the law is still `extrapolated`. Extrapolating a fitted
exponent from 10⁷ to all X is the unsupported step, and it is unchanged. What
changes is that the fit is no longer resting on a single decade.

## The grouping is the Z-vs-Z[i] distinction, and the merging cuts both ways

The two groupings of the previous section are not an implementation detail.
**A (modulus, root) pair *is* a primitive Gaussian ideal of that norm** — an
ideal coprime to its conjugate. Checked over all 3145 admissible m < 20 000,
zero mismatches. (Primitivity is the whole content: (5) has norm 25 but 5 ∤ x²+1
ever, while 𝔭² and 𝔭̄² do correspond to the two roots mod 25. A first version of
this check counted all ideals of norm m and disagreed on 54 of 687 moduli,
correctly.) The counts match because both are 2^{#odd primes}: by CRT and Hensel
on the root side, by choosing 𝔭^e or 𝔭̄^e at each odd prime on the ideal side.

So:

| grouping | absolute value per | this is |
|---|---|---|
| per progression | primitive Gaussian ideal | the **Z[i]** sum |
| per modulus | rational m | the **Z** sum |

And **[ASP]'s (B) asks for the second.** Its display, quoted in
[Note C](note-C-requirements.md) from p. 1043, is
Σ_m | Σ_{N<n≤2N, mn≤x} γ(n)μ(mn)a_{mn} | with m rational and the inner sum over
every n with mn ∈ A — hence over every root at once. **The sieve-relevant law is
the per-modulus one**, exponent 0.480, not the per-progression 0.505.

> **The same row-merging that breaks C₄-freeness over Z supplies the extra
> cancellation in the μ-sum.** Several primitive Gaussian ideals share one
> rational modulus. In the incidence graph that merging creates 4-cycles, so the
> rational Gram entry is 2 where the Gaussian one is 1 ([Note L](note-L-over-Z.md),
> `rational-graph-not-c4-free`). In the μ-sum the same merging puts several ideal
> sums inside one absolute value, where they cancel at the square-root rate.
> **One mechanism, opposite signs: it costs the Gram bound and it pays the
> Type II sum.**

## The law has an identified log correction, and two routes predict it

Putting the mean root count into the law: the number of primitive ideals per
admissible modulus grows like √(log M), so

    S_μ(M) = S_prog / √(mean roots per modulus) ≍ √(MX) / (log M)^{1/4}.

The parallel session reaches the same form from the other side — Cauchy–Schwarz
gives S_μ(M)² ≤ #{m ∼ M}·Q₂, and with #{m ∼ M} ≍ M/√(log M) by Landau–Ramanujan
that is S_μ ≪ √(MX/√(log M)), the identical exponent. Measured at X = 10⁶ across
ten doublings:

| normalisation | drift over M = 512 … 524288 |
|---|---:|
| S_μ / √(MX) | ×0.873 |
| S_μ·(log M)^{1/4} / √(MX) | **×1.052** |

So the (log M)^{1/4} accounts for essentially all of the residual drift, and the
refined law fits to 5% where the plain one fits to 13%.

**This does not promote anything.** The upper-bound half now has a proof shape —
Cauchy–Schwarz is exact, the diagonal is a divisor count, the modulus count is
Landau–Ramanujan, and only the off-diagonal cancellation is measured — but
`sqrt-MX-law` stays `extrapolated` because that last input is the whole
difficulty. What changes is its *shape*: the missing step is cancellation in
Σ_{x≠y} μ(x²+1)μ(y²+1)·G_M(x,y), where G_M is this repo's own Gram entry, rather
than an exponent fitted over four decades. That is the first place the θ-axis and
the Gram axis meet.

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
