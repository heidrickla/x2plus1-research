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

**Measured through the boundary, which had never been done.** Everything the repo
had was *below* θ = 1/2 — exp16 stops at M = X/2 — so the vanishing point itself
was an extrapolation from one side. Running M from X/32 to 8X at X = 4×10⁵, with
the trivial bound T(M) = Σ_{m∼M} #{x ≤ X : m | x²+1} computed alongside rather
than assumed:

| M | θ | T | S_μ | saving T/S | √(X/M) | ratio |
|---:|---:|---:|---:|---:|---:|---:|
| 12 500 | 0.366 | 132 428 | 10 700 | 12.38 | 5.66 | 2.19 |
| 50 000 | 0.419 | 132 428 | 20 150 | 6.57 | 2.83 | 2.32 |
| 200 000 | 0.473 | 132 343 | 38 638 | 3.43 | 1.41 | 2.42 |
| **400 000** | **0.500** | 132 339 | 54 955 | **2.41** | **1.00** | 2.41 |
| 1 600 000 | 0.554 | 132 296 | 85 506 | 1.55 | 0.50 | 3.09 |
| 3 200 000 | 0.581 | 132 399 | 93 446 | 1.42 | 0.35 | 4.01 |

Three things fall out. **T is flat at ≈ 132 400 = 0.331·X across a factor of 256
in M** — the "each x has O(1) divisors per dyadic band" fact, measured rather
than assumed, and constant to 0.1%. **Below the boundary the ratio observed/√(X/M)
is constant at 2.2–2.4**, so the law is not merely the right shape but
saving ≈ **2.3·√(X/M)**, with a constant the repo did not have. And **above the
boundary the ratio departs** — 2.53, 3.09, 4.01 — so √(X/M) genuinely stops
applying at θ = 1/2 rather than degrading through it.

**And [Note L](note-L-over-Z.md)'s Gram-mean minimum is at the same place, which
neither note observes.** Note L measures mean G over cofactor bands as U-shaped
with its minimum at **N = 1.37 X**, from a divisor-built incidence table — an
entirely different computation from the μ sums here. Converting to this note's
coordinate: with m·n = Q ≍ X², a cofactor N = 1.37X is a modulus m = Q/N, so

| X | 3000 | 6000 | 10⁵ | 10⁶ |
|---|---:|---:|---:|---:|
| θ at the Gram minimum | 0.48034 | 0.48191 | 0.48633 | 0.48861 |

rising to **1/2** — exactly where the saving Q^{(1/2−θ)/2} vanishes.

> **The scale where no cancellation is available is the scale where there are
> fewest edges to cancel over.**

The mechanism is not mysterious and should be stated: both are governed by the
balanced split m = n = √Q, where the saving exponent vanishes *by construction*
and the Gram U-shape bottoms for structural reasons. What is worth recording is
that the two were measured by completely different routes and land together. The
convergence is **from below** and still 0.4886 at X = 10⁶, so the coincidence is
asymptotic rather than exact at any measured size.

**One precision the numbers force.** "Exactly zero at θ = 1/2" is about the
*power*, and is correct: Q^{(1/2−θ)/2} = Q⁰. It does **not** mean S_μ reaches the
trivial bound there — at M = X the measured saving is **2.41**, a constant factor,
not 1. A reader could take "no saving" to mean "S = T", and that is false by a
factor of two and a half. What is zero is the exponent.

### The Cauchy–Schwarz chain predicts that 2.41, to 0.7%

The Cauchy–Schwarz reduction below (*The law's upper bound is a Cauchy–Schwarz
reduction, not a fit*) is exact algebra; whether it is *quantitatively* right had
not been tested. This section is out of order with it deliberately — the 2.41 is
measured here, so its explanation belongs here too. It is, and the test needs one correction first.

**T is not DIAG.** The trivial incidence count and the Cauchy–Schwarz diagonal
differ by a μ² weight, and the difference is not the obvious one:

    T    = Σ_{m∼M} #{x ≤ X : m | x²+1}            = 0.331·X
    DIAG = Σ_x μ²(x²+1)·#{m∼M : m | x²+1}         = 0.253·X

    DIAG/T at X = 2×10⁵, M = X/8 … 2X:  0.7658, 0.7649, 0.7651, 0.7681, 0.7658

Constant across a factor of 16 in M — and **not** the squarefree density 0.8948.
The 24% gap is a correlation: only 76.5% of the (m,x) incidences in a band have
x²+1 squarefree, against 89.5% of all x, because a value with more divisors in a
band has more prime factors at fixed size, hence smaller ones, which are likelier
to be repeated.

With the right weight, the chain lands on the measurement:

| input | value | measured by |
|---|---:|---|
| #m in [X, 2X) | 52 187 | the boundary run |
| T at M = X | 132 339 | the boundary run |
| DIAG/T | 0.7658 | the T-vs-DIAG run, X = 2×10⁵ |
| Cauchy–Schwarz tightness S/CS | 0.75 | the parallel session, X = 2×10⁵ |

√(#m·DIAG) = 72 725, and 0.75 × 72 725 = **54 544** against a measured
**54 955** — 0.7%. Predicted saving 2.426 against a measured 2.408. **Four runs,
two values of X, both sides of the collaboration, nothing fitted to the
comparison**, so the agreement is not self-consistency.

**And it measures OFF.** The prediction set Q₂ = DIAG, i.e. OFF = 0, so the 0.8%
residual bounds **OFF/DIAG ≈ 0.016** at this M — independently of the parallel
session's direct measurement, which has |OFF|/DIAG at 0.038 at its largest M.

None of this promotes anything: OFF = o(DIAG) is Chowla, and that is where the
θ axis stops. What changed is that the decomposition is now quantitatively
verified rather than only algebraically exact.

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
Table 1 — and DFI's row is a success.

~~Their Theorem 2.5 (p. 7) gives C⁻_bd(P_ε; ϱ) = 1 + O(ε) for P = (1/2, 0, ν)
with 1/3 ≤ ν < 1/2 and divisor-bounded weights, and this sequence's indicator
*is* divisor-bounded.~~ **Struck — the appeal to the divisor-bounded constants
is not available to this sequence.** [FM] p. 13, (4.1), restricts C±_bd to pairs
satisfying **two** conditions at once:

> |w_n| ≤ τ(n)^ϱ  (x/2 < n ≤ x),   and   Σ_p b_p ≥ x/(ϱ log x).

The second forces b to carry ≍ x/log x primes, hence mass ≍ x; then
a_n = b_n + w_n has mass ≍ x too, so **C±_bd is a class of dense sequences**. A
sparse sequence enters [FM]'s frame only after normalisation to mass ≍ x — which
is what (I) and (II) having right-hand side x/log^B x requires — and then
|w_n| ≍ x^{1/2} on A, violating the first condition. Unnormalised, |w_n| ≤ 1
satisfies the first and fails the second. **The two halves of (4.1) cannot both
hold for a sequence of density x^{1/2}**, so "the indicator is divisor-bounded"
was true in a sense (4.1) does not use.

**The normalisation is not an inference — [FM] state it, twice.** p. 1: "we
consider a sequence (a_n)_{x/2<n≤x} of non-negative weights, **normalized to have
average value about 1** … A typical example would be when a_n is the *normalized
indicator function* of a set of positive integers." And p. 7, in the sentence
this repo already quotes for a different purpose: "If a_n is the **normalized
indicator function of a set J ⊆ (x/2, x] containing x^{1−c} elements**, then one
can only hope for (I) to hold for γ < 1 − c and (II) for θ > c." At c = 1/2 the
normalised indicator is x^{1/2} on A, which is the rescaling that breaks the
first half of (4.1).

**And [FM] flag the consequence themselves**, p. 14:

> "our hypotheses for C± are **not** sensitive to logarithmic-sized rescalings of
> the sequences. **In contrast, the hypotheses for C±_bd are very sensitive to
> unbounded rescalings.**"

An x^{1/2} rescaling is exactly an unbounded one. So the error was appealing to
C_bd for a sequence that reaches [FM]'s frame only through the rescaling their
own remark warns about — and the same remark is why **C± is safe**: the main
position goes through Ψ and Theorem 2.1, which tolerate log-sized rescalings and
need no bound on |w_n| at all.

This removes a support, not the conditional. The parameters still land above
DFI's row, which is all §2 ever claimed.

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
   traffic to run the other way, and [Note F] proves that here it cannot. (Scope:
   Note F is a statement about **ideals of Z[i]** and [FM]'s (II) quantifies over
   **rational** m, n; the step is `gaussian-to-rational-bridge`, `inferred`.
   Bounded either way, so the conclusion holds, but it is reached through the
   bridge.)

## Condition 1 is not a technicality: its easiest case is a named open problem

Set θ = 0. Then the inequality of [Note F]'s Question F reads

> |Σ_{x ≤ X} μ(x²+1)| ≪_A X (log X)^{−A},

using `mobius-ideal-equals-mobius-norm`. Drop the log-power and it is Chowla's
assertion for x² + 1 — and **that is wide open**. One precision, because the
repo's own rule demands it: Teräväinen's (1.1) and his "wide open" remark are
stated for the **Liouville** function λ, and his paper never mentions μ. What
this repo needs is the μ statement. The two are universally taken as equivalent
in difficulty and are related by λ = 1_□ * μ, but **that transfer is not carried
out here**, and openness for λ does not logically imply openness for μ. So the
quotation below establishes the λ endpoint; that the μ endpoint is no easier is
this repo's own assertion. (His *positive* results, Thm 2.6 and Cor 2.7, are for
general bounded multiplicative g and do cover μ.) Teräväinen,
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

**That sentence is about what is *proved*, and it should not be read as a claim
about what is *true*.** Sieved to X = 4×10⁶:

| X | Σ_{x≤X} μ(x²+1) | \|S\|/√X | \|S\|/X |
|---:|---:|---:|---:|
| 10⁴ | 134 | 1.34 | 0.0134 |
| 1.6×10⁵ | −208 | 0.52 | 0.0013 |
| 6.4×10⁵ | −730 | 0.91 | 0.0011 |
| 2.56×10⁶ | 482 | 0.30 | 0.00019 |
| 4×10⁶ | 675 | 0.34 | 0.00017 |

**|S|/√X stays between 0.21 and 1.34 over more than two decades** — square-root
cancellation, unmistakably, with |S|/X down to 1.7×10⁻⁴. So the estimate the repo
needs at θ = 0 is not merely plausible: it is visibly true, and the difficulty is
entirely that nobody can prove it. "The trivial bound has never been beaten"
describes the state of the literature, not the state of the sum, and a reader who
takes it for the latter would conclude the sequence is badly behaved when it is
not.

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
law fitted over four decades. **And following it one step further says which**: it is a restatement, and of a
problem this repo has already named.

For fixed m the solutions of m | x²+1 form ρ(m) progressions mod m, so every
pair in OFF is y = x + h for an admissible shift h, and

> **OFF = Σ_{m∼M} Σ_{h adm. mod m} Σ_x μ(x²+1)·μ((x+h)²+1).**

The inner object is a **two-point correlation of μ(x²+1)**. So OFF = o(DIAG) is a
Chowla-type statement for μ(x²+1) — which is `chowla-for-x2plus1-is-open`, whose
easiest endpoint Teräväinen calls "wide open for any polynomials with nonlinear
irreducible factors". The reduction therefore lands exactly on the blocker this note's opening
section already identifies — *The two windows are complements* — having
travelled through the Gram axis to get there.

That is worth recording precisely because it is negative: the Cauchy–Schwarz
route is closed, and closed by the same obstruction as everything else here
rather than by a new one. Whether that is a route or a restatement is now
settled — restatement — and it should not be quoted as progress on the θ axis.

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

**And the bound predicts the saving at the boundary, which is not 1.** At M = X
the reduction gives S ≪ √(#m·Q₂) with Q₂ ≍ cX and #m ≍ X/√(log X), hence

> S ≪ X·√c / (log X)^{1/4},  so the saving T/S is ≈ **(log X)^{1/4}**.

At X = 4×10⁵ that is 1.90, against a measured saving of **2.41** — same shape,
constant ≈ 1.27.

**And the constant is not free: with the right weight the chain lands at 0.7%.**
A first version of this paragraph read the parallel session's flat
T = 0.331·X as the DIAG of the decomposition. **It is not.** They differ by a μ²
weight, and the ratio is *not* the plain squarefree density:

> T = Σ_{m∼M} #{x ≤ X : m | x²+1} = 0.331X,  **DIAG** = Σ_x μ²(x²+1)·#{m∼M : m | x²+1} = 0.253X,
> **DIAG/T = 0.7658**, constant across a factor 16 in M — against a squarefree density of 0.8948.

The 24% gap is a real correlation: values with more divisors in a band are *more*
likely non-squarefree, since more prime factors at fixed size means smaller
primes and small primes repeat. Equating T with DIAG would have put that 24% into
the bound. *(The measured DIAG agrees across sessions: 5.05×10⁴ and 5.07×10⁴ at
X = 2×10⁵.)* Assembling the chain with the right weight, at X = 4×10⁵ and M = X:

| | |
|---|---|
| #m | 52 187 |
| T | 132 339 |
| DIAG/T | 0.7658 |
| Cauchy–Schwarz tightness | 0.75 |
| **0.75·√(#m·DIAG)** | **54 544** |
| **measured S_μ** | **54 955** |

**0.7%**, from four separate runs at two values of X with nothing fitted to the
comparison. As a by-product it bounds the residual: the prediction assumed
Q₂ = DIAG, i.e. OFF = 0, so the 0.8% shortfall gives **OFF/DIAG ≈ 0.016** at this
M — independently consistent with the 0.038 measured at the largest M above.

**Nothing here is promoted.** OFF = o(DIAG) is still Chowla. What changed is that
the decomposition is **quantitatively verified** rather than only algebraically
exact, and the step this note had as "a standard divisor count" is now a measured
number carrying the correct weight. So the reduction and the direct boundary measurement agree, and
both say the same thing about §1's headline: **what vanishes at θ = 1/2 is the
exponent**, Q^{(1/2−θ)/2} = Q⁰. The saving itself is a log power and is
measurably above 1. Reading "the saving is exactly zero at θ = 1/2" as S = T is
wrong by a factor of two and a half.

*(The lower bound S_μ(M) ≫ √(MX) is untouched by this and remains fitted. §1
does not use it.)*

## Reducing S_μ to μ(x²+1), and the grouping that survives the reduction

§1 rests on S_μ(M) ≍ √(MX), which is `extrapolated`, and the honest worry has
been that its *direct* measurement (exp02) spans less than a decade,
X = 2×10⁴ … 10⁵, while carrying the whole θ-axis argument. The four-decade
support was recorded as holding "in the equivalent per-progression
normalisation" (exp05). Part of that gap closes and part of it does not, and the
two halves were run together in a first version of this section — whose heading
read "the two measurements are the same sum", which is not what the section
establishes.

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

| X | exact | truncated at P = 20 000 | change (exact) |
|---:|---:|---:|---:|
| 10⁴ | 0.895200 | 0.895200 | |
| 10⁵ | 0.894890 | 0.894900 | −3.1×10⁻⁴ |
| 10⁶ | 0.894856 | 0.894860 | −3.4×10⁻⁵ |
| 10⁷ | 0.894842 | 0.894847 | −1.4×10⁻⁵ |

Flat to four places. **Both columns are correct**; the second is what this note
originally recorded, and it is the truncated sieve described in the paragraph
directly above — its error is 1.0×10⁻⁵ at 10⁵ and 5×10⁻⁶ at 10⁷, so the "under
10⁻⁵" bound stated there holds. The exact column removes the truncation. They
are given side by side because a later pass read the single column as an error,
proposed a cause for it, and was wrong twice before noticing the cause was
already written three lines up. Both runs are in `exp23`. At X = 4000 over the band [300, 600) the aggregate ratio of
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
> rational **windowed** Gram entry is 2 where the Gaussian one is 1 ([Note L](note-L-over-Z.md),
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

**This does not contradict `no-log-power-correction`, and the two must be read
with their axes attached.** That claim measures the **X** direction in the
**per-progression** grouping and finds it flat. This one measures the **M**
direction, and the drift is entirely **per-modulus**. The coherent picture:

    S_prog(M)  ~  sqrt(MX)                     flat in X (exp05) and in M (exp16)
    S_mu(M)    ~  sqrt(MX) / (log M)^{1/4}     the per-modulus law

and since [ASP]'s (B) asks for one absolute value per rational modulus, **the
sieve-relevant law is the second**, so the log factor is not a curiosity about a
normalisation the sieve does not use.

**This does not promote anything, and §5 above settles how little it buys.**
The upper-bound half has a proof shape — Cauchy–Schwarz is exact, the diagonal is
a divisor count, the modulus count is Landau–Ramanujan, and only the off-diagonal
cancellation is measured — but that last input is **Chowla for this polynomial**:
for fixed m the solutions of m | x²+1 are progressions, so every pair in OFF is
y = x + h and the inner object is a two-point correlation of μ(x²+1). So

> **the reduction is a restatement, not a route.** It travels through the Gram
> axis and arrives at the same blocker as everything else here, and
> `sqrt-MX-law` stays `extrapolated`. Do not quote it as progress on the θ axis.

What survives is structural and is not diminished by that: **OFF is literally
built from the G_M(x,y) that Prop L.1 bounds and Theorem O.3′ constrains**, so
the θ axis and the Gram axis are the same object. That was not true before, and
it means a result on either side is no longer obviously irrelevant to the other.

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
- *The Chowla sum shows clean square-root cancellation — is the θ → 0 endpoint
  therefore nearly proved?* No, and the two facts should never be quoted
  together without this sentence. |S|/√X ∈ [0.21, 1.34] over two decades says
  the estimate is **true**; it says nothing about provability, and the gap
  between them is the whole subject. A reader who takes the measurement as
  progress toward the proof has the situation exactly backwards: it is *because*
  the truth is not in doubt that the difficulty is purely one of method.
- *Does the 0.7% agreement validate the Cauchy–Schwarz reduction?* It validates
  the **decomposition**, given four measured constants. It does not make the
  reduction a route — §5 settles that separately, and negatively, since
  OFF = o(DIAG) is Chowla. Quantitative accuracy in a chain whose last link is
  an open problem is not progress on the open problem, and the temptation to
  read it that way is exactly why §5 says "do not quote as progress" in as many
  words.
- *The saving at θ = 1/2 is 2.41, not 1 — does the axis still vanish there?* The
  **exponent** vanishes; that is what Q^{(1/2−θ)/2} = Q⁰ means and it is the only
  thing the argument uses. The constant 2.41 is not a saving in any sense a
  sieve can spend, and reading "no saving" as S = T is wrong by a factor of two
  and a half in the other direction. Both misreadings are available from one
  sentence, which is why the section states the exponent and the constant apart.
- *Which grouping does the sieve actually need, and does the note commit?* Per
  **modulus** — [ASP]'s (B) puts one absolute value per rational m, spanning
  every root. The note commits, and it matters: the two groupings have different
  exponents (0.4803 against 0.5046) and the per-progression one, which has four
  decades behind it, is **not** the quantity (B) asks for. Any future use of
  exp05's range must carry that.
- *Both new sources were located by a parallel session.* Both were then fetched
  and read here before being quoted; neither is recorded on the strength of the
  other session's report.

---

## M.9 The D-blindness is in the weights, not in the matrix

The parallel session placed the μ side next to the D axis and found both
analytic quantities blind to D: κ = X²/(kX² + D) → 1/k cannot resolve D at all
(an identity, not a measurement), and |Σ_{x≤X} μ(x²+D)|/√X is O(1) uniformly in
D with an ordering matching the structure at neither size. Their conclusion —
*the arithmetic parameter that decides the whole C₄ structure is invisible from
the analytic side* — is the sharpest form of this repo's position.

**OFF is the test that locates it.** OFF is not merely a third analytic
quantity; it *is* an incidence matrix, μ-weighted:

  Q₂ = DIAG + OFF,  OFF = Σ_{x≠y} μ(x²+D) μ(y²+D) · G_M(x, y).

**⚠ Which matrix — and it is not the C₄ one.** The kernel above is indexed by
**elements** x, y (it counts divisors of gcd(x²+D, y²+D) in the band), as the
expansion forces and as §M's own "every pair is y = x + h" already implies. Note
F's G and Prop L.1 are indexed by **cofactors**, #{m : mn₁, mn₂ ∈ A}. CLAUDE.md
called them the same object; they are not. On the same values, one window
[1000, 2000), X = 3000:

| D | cofactor max | mean/supp | mean/all | element max | mean/supp | mean/all |
|---:|---:|---:|---:|---:|---:|---:|
| 1 | **2** | 1.0245 | 0.0150 | 2 | 1.0043 | 0.00067 |
| 2 | **2** | 1.0222 | 0.0136 | 4 | 1.0427 | 0.00110 |
| 6 | **2** | 1.0220 | 0.0110 | 5 | 1.0521 | 0.00126 |
| 11 | **2** | 1.0188 | 0.0130 | 7 | 1.1944 | 0.00254 |
| 39 | **2** | 1.0149 | 0.0147 | 6 | 1.1656 | 0.00301 |

**The cofactor Gram is flat in D — max exactly 2 throughout, mean slightly
*falling*. The element matrix rises.** So the D-dependence reported below is a
statement about the Cauchy–Schwarz chain, **not** about C₄-freeness, and must
never be quoted as the latter. *(Note that the singly-windowed cofactor Gram is
blind to D even though the **doubly-banded** one is not — O.12 holds at D ≤ 4 and
fails at D = 11. The structural distinction lives in the doubly-banded
configuration specifically.)*

So the weighted and unweighted readings of **one incidence matrix** can be taken
in a single pass, at the same X, over the same band, on the same population —
no difference of size, window or denominator between them. At X = 20000
(`exp25_off_sees_D.py`):

| D | OFF/DIAG [1000,2000) | [2500,5000) | mean G b1 | b2 | drift | DIAG |
|---:|---:|---:|---:|---:|---:|---:|
| 1 | +0.2275 | +0.1441 | 1.0077 | 1.0075 | 0.02% | 5073 |
| 2 | +0.0906 | −0.0468 | 1.0482 | 1.0484 | 0.02% | 5188 |
| 6 | −0.1099 | −0.0912 | 1.0655 | 1.0581 | 0.69% | 7644 |
| 11 | −0.1604 | +0.0714 | 1.2127 | 1.2008 | 0.98% | 1908 |
| 39 | +0.1892 | +0.1257 | 1.1919 | 1.1859 | 0.50% | 2030 |

**OFF is blind, and more strongly than S_μ is.** It changes sign *within* each
band, and its sign pattern is not stable *between* them — (+,+,−,−,+) against
(+,−,−,+,+). A quantity that only fluctuated in magnitude could be concealing a
trend; one whose signs reshuffle under a change of band cannot be monotone in D.

**The matrix it is built from is not blind.** Mean G reproduces to under 1%
across that band change and separates the D values. Nor is DIAG, which swings by
a factor of 4.

So the conclusion moves one step in and one step sideways: not *the analytic
side cannot see D*, but **the D-dependence is present in the object the analytic
quantity is made of, and the μ signs annihilate it.** The dichotomy is
**weighted / unweighted**, not analytic / structural — DIAG sits on the analytic
side and sees D perfectly well. This is Note J's finding from a new angle: the
signs that make the sum hard to bound are the same signs that hide the
arithmetic, and it now has a measurement on both faces.

### ⚠ Two cautions about the unweighted statistic, one of them nearly shipped

**(i) Quote the mean, not the max.** From band 1 alone, max G is *monotone* in
D — 4, 7, 9, 10, 15 — and was written up here as "climbs monotonically". Band 2
gives 4, 8, 7, 9, 14: neither monotone nor band-stable. A bounded sweep produced
a clean law, exactly as this repo's own rule predicts.

**(ii) Mean G is not a structural classifier.** Its order is
1 < 2 < 6 < **39 < 11** — it puts D = 11 *above* D = 39, while structurally 39
is the more degenerate (a banded **triple**, against 11's banded 4-cycle). This
repo has already refuted mean G as a captured/uncaptured classifier, built from
two points and "confirmed" on two more. The same statistic is now available for
the same misreading on a new axis, and the temptation is **stronger** here
because it reproduces across bands to under 1%. **Reproducibility is not
aboutness**: that mean G is a stable function of D says nothing about whether it
is a function of the structure D controls.
