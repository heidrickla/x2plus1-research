# Working notes for this repo

Research repo, not a product. The output is *notes* — code exists to keep the
notes honest.

## Where things stand

*This section is the compaction fallback. `tools/session_primer.py` prints a
live version of it via a SessionStart/compact hook, but that hook only binds in
sessions that start with `.claude/settings.json` already present — **true of
`SessionStart` specifically, and not of hooks in general.** `SessionStart` cannot
fire for a session that has already begun: the event is past and adding the hook
later does not bring it back. `Stop` and `UserPromptSubmit` fire repeatedly for
the life of a session and settings are re-read each time, so those *do* bind
mid-session. (Reported by the supervisor session from its own case — it created
`.claude/settings.json` mid-session and its `Stop` hook fired on the next attempt
to end a turn. Not independently verified here, and not verifiable from inside a
running session.) So the primer genuinely does not protect a session that started
without it, and that limitation does not generalise — so this file,
which is always loaded, carries the same state by hand. Keep it current; a stale
version here is worse than none.*

**The obstruction is Type II, and it is Note F's C₄-free lemma**: for
A = {x+i}, G(n₁,n₂) = #{m : mn₁, mn₂ ∈ A} ≤ 1, so a bilinear form with
arbitrary bounded coefficients admits no cancellation at any split. That is a
theorem about the sequence and survives any change of sieve. **And it survives the
change of ring**: Theorem O.12 proves G′ ≤ 1 over **Z** for cofactors within a
factor (5+√21)/2 = 4.7913 — in particular within one dyadic band — on every
dyadic modulus window, and [FM]'s (II) is bilinear over m ∼ M *and* n ∼ N, so
banded pairs are all it sees. The C₄-free input therefore no longer arrives
through `gaussian-to-rational-bridge`; it is available on both sides. What is
still `inferred` is only the reading of their quantifier, which is the same
reading the bridge always rested on.

**And there is a stronger form that does not depend on the bound being 1.** At
X = 3000 the mean of G over pairs in a dyadic band [N,2N) is 2.000, 0.667, 0.254,
0.0865, **0.0243** at N = 8, 32, 128, 512, 2048 — but the first two are over **1 and 21 pairs**, so read them as barely defined rather than as data. So over the range the sieve uses
the expected Gram entry is far below 1 *while G is integer-valued*: at N ≈ 2048,
a mean of 0.024 against a granularity of 1, so **what dispersion would call the
error is tens of times what it would call the main term.**

*Do not attach a law to that decay, and do not quote "max 2".* Independently
re-measured on the cofactor side: the values reproduce exactly, but **1/N and
(log X)/N both fail** — the latter by 6–8× with a drifting ratio — and the fitted
exponent itself moves (0.80 to 0.88) with the range, so no clean power fits. The
mean is also **U-shaped**, bottoming near N ≈ X and climbing back to 0.51 by
N ≈ X²/4. And **max G is 3, not 2**: G(17, 26) = 3 with shared moduli 1, 85,
2 966 965, all verified as t²+1 — but one is the **unit modulus m = 1**, which no
Type II hypothesis admits, so **excluding units it is 2**. It is also consistent
with `rational-gram-bounded-on-windows`, since those span seven orders and no
*window* holds two. Max-2 is a statement about windows, not about G, and a
cofactor-band sweep reporting 2 has not gone to small enough N.
**None of it touches the argument**: (B1) forces M ≥ √x = X, hence cofactor
n ≤ X, which is exactly where the mean is small and falling. Any bounded integer-valued count with mean o(1) has no
decomposition into main term plus smaller error, so this survives a bound of 2 or
3 — which makes `gaussian-to-rational-bridge` even less load-bearing than the
C₄-free form needs it to be.

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
needs is a named open problem. **The law's range is four decades, not one.**
μ((x²+1)/m) = μ(m)·μ(x²+1) on squarefree values and μ(m) dies under the absolute
value, so S_μ reduces to sums of μ(x²+1), which sieve — reaching X = 10⁶,
an order past exp02's incidence route. The non-squarefree residue is flat at
0.8948 across 10⁴…10⁷, a constant factor. **But the grouping matters**: S_μ takes
one absolute value per *modulus* (all roots at once), exp05 one per *progression*,
and inter-root cancellation is square-root exact. Measured M-exponents at
X = 10⁶: **0.5046 per progression, 0.4803 per modulus**. So exp05's four decades
support the per-progression law, and the aggregate S_μ sits slightly *below*
√(MX) — more cancellation than claimed, i.e. the saving is conservative. Still
`extrapolated`: the step to all X is untouched.

**The boundary itself is now measured, not extrapolated to.** Everything prior
was below θ = 1/2. Running M from X/32 to 8X at X = 4×10⁵ with the trivial bound
T computed rather than assumed: T is **flat at 0.331·X across a factor of 256 in
M**; below the boundary the saving is **2.3·√(X/M)**; above it √(X/M) stops
applying (ratio 2.53, 3.09, 4.01). **At θ = 1/2 the saving is 2.41, not 1** —
"exactly zero" is true of the *exponent*, and reading it as S = T is wrong by a
factor of two and a half. And the Cauchy–Schwarz chain predicts that 2.41 **to
0.7%** from four independent runs, once T and DIAG are kept apart: they differ by
a μ² weight of **0.7658**, not the squarefree density 0.8948, because divisor
count in a band and squarefreeness are correlated.

**The θ-axis is now measured end to end, and the picture is sharper than
"the difficulty is the absolute values".** At θ = 0 the plain Chowla sum has
**square-root cancellation**: |Σ_{x≤X} μ(x²+1)|/√X stays in [0.21, 1.34] over
X = 10⁴…4×10⁶. With the divisor weight — the *signed* Type II sum — it is still
O(√T) uniformly across a factor of 1024 in M. **So the estimate this repo needs
at θ = 0 is visibly TRUE; the whole difficulty is that nobody can prove it**, and
"the trivial bound has never been beaten" describes the literature, not the sum.
What costs is the absolute value, and **the cost grows with M**: signed/absolute
decays 0.096 → 0.005 across that range, so the 2% figure is understated exactly
where (B1) needs it.

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
sufficient** — only the direction κ = 1 ⟹ forest is load-bearing. **And κ is a
reparameterisation of α, not an independent invariant**: |A| = Q^α gives
κ = Q^{2α−1} identically, so κ > 1 ⟺ α > 1/2 and "κ > 1 is necessary" *is*
"density above 1/2 is necessary" — the literature's own boundary, Li's record
being 0.6418. Never quote a κ observation as independent evidence for a density
conclusion, or the reverse. √κ is the
length of the Poisson sum in [MER] p. 4; for x²+1 it is 1. **And mean G is NOT the
sufficient part** — a classifier proposed and refuted within the hour by the test
built to check it. At Q = 4×10⁶, band N ∈ [2048, 4096):

| | κ | mean G | status |
|---|---:|---:|---|
| x²+1 | 1.00 | 0.0219 | open |
| **x³+2y³** | **75.1** | **0.1888** | **captured (Heath-Brown)** |
| a²+b⁶ | 115.4 | 0.5590 | not known captured |
| a²+b⁴ | 1297.5 | 3.592 | captured (FI) |
| a²+(b²+1)² | 1269.3 | 12.809 | captured (MER) |

Without x³+2y³ it reads as a law — mean G > 1 exactly for the captured ones. With
it: **captured sequences at 0.19, 3.59, 12.81 and non-captured at 0.02, 0.56,
interleaved.** The row was chosen because x³+2y³ and a²+b⁶ share κ ≍ Q^{1/3}, so κ
cannot distinguish them and a real classifier had to. **What survives is only the
two-sequence control** (`mean-G-separates-x2plus1-from-a2b4`): the mean-o(1)
argument does not prove too much, since a²+b⁴ has mean 3.59 where x²+1 has 0.022.
Generalising a control into a classifier — from two points, "confirmed" on two
more of which one had no known outcome — is the error.

**Position against the literature** (all read at source): ASP needs D > x^{2/3}
and this sequence caps at x^{1/2}; DFI's Theorem S is normalised to x and is
*vacuous* on a sequence of mass x^{1/2} — and restated relative to |A| its
Type I (D = x^{1/2−ε}) is **available** while its Type II (short variable to
x^{1/3−ε}, β on primes) is not, so the level is never the obstruction;
Ford–Maynard's binding parameter is **ν, not γ** — every entry in their Table 1 has ν > 0 (smallest: Merikoski's
1/12), and ν = 0 here gives C⁻ = 0 by Selberg and their Theorem 2.1. Their
footnote 2 p. 7 names Note F's G(n₁,n₂) as the barrier — **and at this density
that barrier is unconditional**: its hypothesis is θ + ν ≥ 1 − 2c, and |J| =
x^{1/2} gives c = 1/2, so 1 − 2c = 0 and θ + ν ≥ 0 holds for every admissible
pair. FM say the obstruction is bilinear cancellation in the error term for G;
Note F says G ∈ {0,1}, so there is no main term and no error term to cancel.
Their "typically very difficult" is, here, empty. **Do not evaluate the footnote's precision
requirement at its own range** — a claim doing so was refuted the same day. Its
range at c = 1/2 is m₁,m₂ ∼ x^ε, and **small ε means SMALL moduli** (x^{0.05} =
2.6 at x = 1.44×10⁸), which is the end where mean G is *large*: 2.000, 1.333,
0.810, 0.577 at N = 8, 16, 32, 64, over bands holding 2, 4, 7, 13 cofactors. What
is unaffected is what the sieve uses: (B1) forces M ≥ X, so the cofactor is at
most X, exactly where the mean is small and falling. The control is what keeps
the obstruction honest: at a²+b⁴'s density, mean **3.59** at the same band where
x²+1 has 0.022 — an ordinary estimation problem, and the one FI solved. Their Theorem 2.4 never
applied here, and the γ = 1/2 − ε argument is `refuted`; the clean placement is
that θ > c = 1/2 collides with (1.1)'s θ < 1/2, so there is no admissible triple
at all (`x2plus1.exponents.ford_maynard_theta`). **C⁻ is the LOWER-BOUND constant** — [FM] p. 2 at
source: "a non-trivial lower bound for primes whenever C⁻(γ, θ, ν) > 0". So
C⁻ = 0 closes **infinitude**, not merely the asymptotic, which matters because
infinitude is all Landau's problem needs. The same page covers the Harman sieve
explicitly ("especially those relying on the iterative techniques of the Harman
sieve … demonstrating general limitations of the Type I/Type II setup") —
stronger than Li's remark, which is about *asymptotic* estimates where the
objection was about lower bounds. And the standing warning now needs stating
more carefully rather than less: C⁻ = 0 is about **what these axioms can
prove**, never about whether x²+1 is prime infinitely often — do not conflate
them.

**Notes N and O** are the two additions the plan does not list. N re-argues the
Green–Tao exclusion from Green–Sawhney: it survives, but not for the plan's
stated reason — their weight has both coordinates free, δ₁ imposes two
independent linear conditions, and at their k ≈ 2^347 the normalised Gowers norm
of a delta is 1 − o(1), so the conclusion is *information-free*. O identifies the
multiplier τ = (√b+√a)/(√b−√a) behind the close-pair structure and proves it
cannot act twice on one element **while both images stay inside the window** —
the window clause is essential and its omission made an earlier statement of
Proposition O.1 false, with (1,5) at m = 2 the counterexample (τ₁ and τ₁² = τ₃
both act there; it escapes because a·g² = 4 = M, and it escapes *because*
r₁ = 6.854 is nowhere near a window). **The general "no window holds three" is NOT
proved** — it was claimed unconditionally and retracted; the window Gram bound
stays O_ε(N^ε).

**Note O's thread — twelve results, in order.** All concern *shared moduli*: for
a cofactor pair with d = gcd, a = n₁/d, b = n₂/d, the moduli both divide are
solutions of aY² − bX² = M, M = b − a, D = ab, and m = (X²+1)/a. Multipliers
τ_V = (U + V√D)/M with U² − DV² = M² move between solutions.

- **O.3 / O.3′ / O.3″** — triples of the form (ξ, τ₁ξ, τ_kξ), so they *assume τ₁
  acts*. O.3: M odd squarefree. O.3′: gcd(M,2X) ≤ 16, no hypothesis on M, from
  M(ρ²−1) = 4ka(k−ρ) with ρ = B_k/M and ρ < 1.06066. **O.3″** keeps a term O.3′
  discards (ρ > 1 is free) and gives the joint region
  **(4k+√(16k²+2))(2c+1) < c(kc−c−1)**; k → ∞ recovers c ≥ 17, and **k = 2 is
  excluded for every c ≤ 33**. Reading "cρ ∈ ℤ needs 1/(ρ−1)" off the ρ bound
  gives 33 not 34 at k = 2 — that route spends ρ > 1 on the −ρ term, the region
  form substitutes ρ ≥ (c+1)/c in both. Parent and corollary, not a conflict.
- **O.4** — first to assume *nothing* about which multiplier acts. The automorph
  X_j = (UX_i + VaY_i)/M with aY_i > X_i√D gives the exact X_j > τ_V X_i, and
  m = (X²+1)/a turns it into m₃/m₁ > (τ_min⁴X₁²+1)/(X₁²+1), so a window needs
  **τ_min⁴ < 2 + 1/X₁²** — b/a > 53.69 at X₁ = 1, rising to
  **133.875 = [(1+√2)(1+√2+2^{5/4})]²**. **The finite term is load-bearing**: the
  clean m_{i+2}/m_i ≥ τ₁⁴ is FALSE (9 of 110 gaps; (1,5) m 2→65 gives 32.50 vs
  46.98). **Step 2 must go through the map** — the symmetric route gives τ at V/a.
- **O.5** — τ_p² ∈ T forces **M | 8p²** (since D ≡ a² mod M, gcd(a,M) = 1), and
  the window forces D < M against M < D always. So **no window holds
  (ξ, τ_pξ, τ_p²ξ)** for any p, given X₁ ≥ 1. **Supersedes Prop O.1** and explains
  its (1,5) escape: M = 4 | 8, so τ₁² really is integral there and it is the
  *window* that fails.
- **O.6** — for M an odd prime the subcase (M | S vs M | T) **alternates at every
  step** when M ∤ V, via M·S′ = A_pS + V_p·M·X (*not* S′ = A_pS/M, which fails on
  246 of 246). I first wrote this up as "the integrality route cannot close O.2";
  **too strong** — it shows only that the composite's two integrality conditions
  are vacuous, and the alternation itself closes the case an hour later.
- **O.7** — hence **no window holds three when M is an odd prime**: two steps flip
  twice, the one-step composite flips once, and the dichotomy forbids both.
- **O.8** (superseded) — M odd squarefree on the hypothesis gcd(V,M) = 1, via
  **S·T = −M·m** ⟹ gcd(M,S)·gcd(M,T) = M.
- **O.9** — the mechanism is a **sign**: Y² ≡ X² (mod p) gives σ = ±1 with
  Y ≡ σX, and V_ij ≡ X_iX_j(σ_j − σ_i), so **p | V_ij ⟺ σ_i = σ_j**. Three signs
  in {±1} cannot be pairwise distinct, so **M | V₁₂V₂₃V₁₃** and, with
  |V| < M/√(3D), **3ab < (b−a)^{4/3}**.
- **O.10** — **no hypothesis on M at all.** The sign becomes a valuation split:
  s = min(e, v_p(S)), t = min(e, v_p(T)) satisfy s + t ≥ e; either p^s | S or
  p^t | T kills V, so v_p(V_ij) ≥ max(min(s_i,s_j), min(t_i,t_j)); ordering
  s₁ ≤ s₂ ≤ s₃ gives v_p(V₁₂) + v_p(V₂₃) ≥ e. **The sign is its e = 1 shadow.**
- **O.11** — R₁₂R₂₃ = R₁₃ couples the three bounds, and sinh(u₁₂)sinh(u₂₃) at
  fixed u₁₃ peaks at the **equal** split, so ab < (C(X₁)/8)^{2/3}(b−a)^{4/3} with
  C = (√ρ−1/√ρ)³(√ρ+1/√ρ) — **0.048628 vs O.10's 1/3, 6.85× stronger**.
- **O.12** — the one that touches the main line. See below.

**Read every coverage figure over the informative population.** A class with
fewer than three shared moduli cannot host a triple, and only **60 of 1,815,154**
classes at X = 3000 have three at all. O.10 excludes **~35%** of informative
classes (flat in X); O.11 **88–98%** — **but O.11's falls monotonically** (97.7 →
88.1 over X = 1500–8000) while the admissible count doubles per doubling of X, so
it may tend to 0 and no claim is made about its limit. Both sessions first
published the ~99%-of-all-classes figure. **A coverage figure above ~90% on an
open question is evidence the denominator is wrong.**

**⚠ Two hazards recorded because each nearly shipped.** (i) The per-prime form
v_p(V₁₂)+v_p(V₂₃) ≥ e does **not** give M | V_aV_b for a fixed pair — the ordering
is computed per prime, and 5 of 216 realised triples admit no uniform pair
((1,481) M=480, (1,925) M=924, (1,106) M=105, (1,2465) M=2464, (1,1450) M=1449,
all with ≥3 distinct primes). That reduction would prove O.2 in one line.
(ii) Every class O.11 admits has a = 1, and a = 1 is the unit cofactor no Type II
hypothesis admits — so *"O.11 is exhaustive on exactly the Type II classes"* is
true of every number in the sweep and **false**: the largest b among informative
a ≥ 2 classes is 8321 at X = 6000 against an a = 2 crossover of 7×10⁴, so the
data cannot test it.

**Theorem O.12 is the one that touches the main line.** The rest of Note O
windows the *moduli* and lets cofactors range free; **Ford–Maynard's (II) bands
both** (m ~ M, n ~ N; footnote 2 averages over m₁,m₂ ~ x^{1−2c+ε}). Banded
cofactors give u = n₂/n₁ < 2, while two shared moduli in one window need
τ_V² < 3, i.e. M/√D > √3, i.e. **u > (5+√21)/2 = 4.7913** — a factor 2.4 out of
reach, using |V| ≥ 1 so it does not depend on parity. **So the rational graph on
the doubly-dyadic configuration is C₄-free, proved, for all X.** Measured: banded
Gram 1, free Gram 2, at every window at X = 2000/3000/6000, with a positive
control — 57,132 of 300,026 banded pairs share exactly one modulus and 0 share
two, while 127 free pairs share two. **This closes the second half of
`gaussian-to-rational-bridge`'s stated gap** — "what is measured over Z is
G′ ≤ 2" becomes a proved G′ ≤ 1, matching Z[i] exactly. It does **not** close the
bridge's inference ("both give no main term, so the conclusion is unchanged"),
and says **nothing** about O.2. The cleanest witness is **unit-free**: cofactors
**(2, 82)** share moduli **365 and 685** (ratio 1.877, one window), since
2·365 = 27²+1, 82·365 = 173²+1, 2·685 = 37²+1, 82·685 = 237²+1 — cofactor ratio
41, far above O.12's 4.7913, so consistent with it. *(Usually written (1,41) with
730 and 1370, which a reader dismisses in a line because the unit cofactor is
inadmissible; the maxima are 2 with or without the unit.)* A genuine G′ = 2,
with 41/1 far outside any band.

**And O.12 makes Ford–Maynard's footnote-2 counting function a 0/1 indicator over
Z.** Their footnote (arXiv:2407.14368v1 p. 7) asks for #{n : nm₁, nm₂ ∈ J} with
**"an error term better than O(1)"** on average over m₁, m₂ ∼ x^{1−2c+ε} — it
bands both variables, so O.12 applies and the count is 0 or 1. For a 0/1 integer
"better than O(1)" means knowing it exactly. **Note F's reading — the count is 0
or 1, so the error term *is* O(1) and no averaging can improve it — is therefore
available over Z and not only over Z[i]**, and it is *pointwise*, hence immune to
the objection that would sink a mean argument.

> **⚠ The "mean ≥ 1" line in `fm-barrier-range-is-small-moduli` is this repo's
> paraphrase, not the footnote's**, which is a condition on the error term and
> says nothing about a mean. The measured means (2.000/1.333/0.810/0.577 free;
> **1.000/0.667/0.476/0.410 doubly banded, max 1**) are evidence about *how often
> the count is 1*, **not** about a threshold being crossed. Caught by asking
> whether the number in our claim is the number in their paper — the Plücker
> question aimed at a citation. **Paraphrases drift in the direction that makes
> the local argument work.**

**Where the residual inference lives, now that O.12 has closed the other half.**
Ford–Maynard's footnote 2 contains **two** steps and only the first is exact.
(1) Their #{n : nm₁, nm₂ ∈ J} **is** Note F's G with the variables named the
other way — an equality of definitions — and O.12 proves the 0/1 property over Z
on exactly the configuration their average runs over, so that step needs neither
an inference nor the transfer. (2) The implication from that object to (θ, ν) is
stated by them as **"closely related to"**, not as an equivalence. So
"count is 0/1, error O(1) unimprovable" ⟹ **ν = 0 in their sense** rests on a
four-word hedge *in the source*. **But the hedge is off the path**, which a dependency trace shows and re-reading
the paper cannot: `fm-footnote2-is-note-F-G` has exactly **one** dependent, and
ν = 0 comes from `selberg-nu-zero-binds` — `quoted`, empty `depends_on`, from
Selberg via [FM] p. 2 and Theorem 2.1. **This repo never derives ν = 0 from the
counting function.** Footnote 2 corroborates that we measure the object the
literature names as the barrier — *relevance*, not a derivation step. It binds
only `fm-barrier-is-unconditional-at-density-half`, where the footnote **is** the
source. What `gaussian-to-rational-bridge` actually carries is the reading of
what (II) quantifies over, a different sentence, which **could** be settled by
reading more carefully.

**Positive control — the 0/1 property is not generic.** Doubly-dyadic max Gram at
Q = 2.5×10⁴ / 5×10⁴ / 10⁵: **x²+1 = 1, 1, 1** (proved, 0 banded pairs sharing
two); a²+b⁶ = 6, 7, 11; x³+2y³ = 5, 9, 15; a²+b⁴ = 26, 60, 66; a²+(b²+1)² = 33,
67, 67. x²+1 is at 1 at every size where the value is a *theorem*; everything
else **grows with Q**. **Which explains the footnote's own hedge** — for a count
ranging over 0…67 there is something to average, for a 0/1 indicator there is
not. **⚠ NOT a classifier, and the ordering is not even stable**: a²+b⁶ (not
known captured) is *above* the captured x³+2y³ at Q = 2.5×10⁴ and below it at the
other two, so it cannot separate captured from open. x³+2y³ is in the table
because it is what killed the mean-G classifier, and it was run before the
framing was chosen. **The claim is a difference in kind, not a position in an
ordering.**

**O.12's *argument* is special to c = 1; the *fact* is not known to be.** Along
x²+c² the identity carries a factor c² — **V·W = c²·M(m_i − m_j)** — so the
threshold scales as **1/c²** and drops below what a dyadic band supplies at
c ≥ 2. The prediction is that O.12 fails there; **it does not** (banded max Gram
is 1 for c = 1…5, over 146k–648k banded pairs each, free 2 throughout). Both
repairs are shut: the bound is **saturated** (max |V|/bound = 1.0000, 3.9999,
8.9998 = exactly c²) and min |V| is 2, 4, 6 — i.e. 2c, not c². **And that makes
the line family a test bed for the bridge**: A_c is C₄-free over Z[i] for every c
(proved), while O.12 covers Z only at c = 1, so **And the family BOUNDS the transfer rather than
supporting it**: doubly-dyadic C₄-freeness over Z **fails at c = 6** — cofactors
(5,8), ratio 1.6, sharing moduli 9 and 17, ratio 1.889, since 5·9 = 3²+6²,
8·9 = 6²+6², 5·17 = 7²+6², 8·17 = 10²+6². Over c ≤ 8 it holds at 1,2,3,4,5,7 and
fails at 6,8. **The mechanism is the Z[i]→Z coarsening exactly**:
(3+6i)(10+6i) = −6+78i and (6+6i)(7+6i) = 6+78i are **conjugate, not associate**,
so A₆ *is* C₄-free over Z[i] while the norms agree at 6120 and the rational cycle
is real. ⚠ **"Any dyadic window" means any ratio < 2, NOT a window anchored at a
power of two** — [8,16) and [16,32) between them miss (9,17), so an anchored
sweep passes on the counterexample, and mine did. It does **not** refute the
bridge for x²+1, where the Z side is *proved* by O.12 rather than transferred.

**THE ONE MECHANISM UNDERNEATH ALL THE D-COINCIDENCES: the invariant is M·D.**
From a·m = X²+D and b·m = Y²+D, b(X²+D) = abm = a(Y²+D), so **aY² − bX² = M·D**
— what Note O calls M is really M·D, and **every bound built on it weakens by a
factor of D**. O.9 becomes 3ab < (M·D)^{4/3}, which separates the cases exactly:
at cofactors (5,8) with M = 3, that is 120 vs **4.33** at D = 1 (forbidden, none
occurs) and 120 vs **572.24** at D = 39 (permitted, and the triple occurs). Same
bound, same cofactors — **D is the whole difference**. It subsumes the c = 6
break (D = c², bound weakens by exactly c²), the family below, and the seven
unit-free triples at D ≤ 60; and the density is a prediction that could have
failed — 51 of 160 D ≤ 160 admit a unit-free triple, **none with D ≤ 25**, which
is the shape a D^{4/3} loosening predicts and not the shape of a sporadic set.
**So x²+1 is the D = 1 end of a one-parameter family — the point where every
bound in the apparatus is tightest.** **And M·D gives O.12's exact reach on that
axis**: the pair condition becomes (u−1)·D/√u > V·√3 against a band's
(u−1)/√u < 1/√2, so O.12 covers **D ≤ V√6** — **D = 1, 2** unconditionally and
**D ≤ 4** with the parity lemma's |V| ≥ 2. So the theorem also proves the
statement for **x²+2**, and stops there. *(This reconciles with the line-family
result computed before M·D was known: D = c², so D ≤ 4 is c ≤ 2.)* **|V| is even
on this axis too** — min |V| = 2, 4, 6, 4, 2, 4 over D = 1…6 with no odd value in
1,238 pairs — so the second row is available and **x²+2 in particular can never
fail**. ⚠ **That bounds the uniqueness conjecture**: the parallel session's
attrition argument (larger X gives more candidate cofactor classes at fixed D)
cannot reach small D, because there the condition **(u−1)D/√u > V√3** is not
merely tight against a band's 1/√2 but **unsatisfiable** — at D = 2 it is
1.41421 < 1.73205, a 22% margin. So the conjecture is **"every D > 4 fails"**,
not "every D > 1", and the two regimes differ in kind rather than in where a
sweep stopped. **D = 5 is the first value the argument does not reach**, so if
the attrition picture is right it should be the first survivor to fall. The twelve theorems are not weakened by
that; they are *located*. ⚠ And **the right axis is the discriminant**:
4(x²+bx+c) = (2x+b)² + |Δ|, so the line family (Δ = −4c²), the D family
(Δ = −4D) and general quadratics are one axis — 11 discriminant classes checked,
all agreeing internally, 0 disagreements.

**The next axis out — D itself.** In x²+D, four
consecutive arguments k…k+3 give a 4-cycle exactly when
**(k²+D)((k+3)²+D) − ((k+1)²+D)((k+2)²+D) = 4(D − k² − 3k − 1)** *(verified
symbolically)*, so precisely for **D = k²+3k+1 = 1, 5, 11, 19, 29, …**.
**x²+1 IS the k = 0 member — it does not avoid the family.** Its instance is
1·10 = 2·5, giving cofactors {1,5} and moduli {1,2}: **the unit in both**, and the
unit modulus is what no Type II hypothesis admits. D = 5 escapes for an unrelated
second reason, so the first genuine counterexample is **D = 11** (values 15, 20,
27, 36; cofactors {3,4}, moduli {5,9}, both ratios < 2). Both ratios → 1 as k
grows, so the family is deeply doubly dyadic and infinite. **O.12's conclusion
fails for an explicit infinite family of degree-2 sequences, and x²+1's escape
has a cause rather than being a brute fact.** ⚠ **The axis lesson**: c = 6 and
D = 11 were both found by extending an axis that had been checked at five or six
values and read as general — *"what would the sweep look like if the finding were
absent"* applies to the **axis** as much as to the population.

**Two group actions, and why Notes L and O never collided.** Both act on
aY² − bX² = M. **Note L's ε** (the automorph, u² − Dv² = 1) moves **within** an
orbit — Prop L.1's ε² ≥ φ⁴ = 6.854 is why a window holds at most one per orbit.
**Note O's τ_k** (the multiplier, U² = M² + 4k²D) moves **between** orbits, and
τ₁² can sit below 2 — which is how two moduli land in one window at all. At
(1,41) they are seven orders apart: ε² = **1.679×10⁷** against
τ₁² = **1.877328**, versus the observed 1370/730 = 1.876712 (matching to four
places, the residual being O.4's finite +1; **identically at the unit-free
(2,82) = 2·(1,41), which scales the conic and carries the same τ₁ to six
places — the witness Note L now leads with**). **So the windowed Gram entry counts
the orbits τ reaches inside one window, ε gives at most one member per orbit, and
O.2 is the statement that τ never reaches three** — the sentence neither note
contained. ⚠ **The plausible identification is backwards**: assigning orbits by
|V| = 2, on the reasoning that the fundamental multiplier is the fundamental
automorph, yields "two moduli of one orbit in a window" and reads as a defect in
Note L. 1.877 against 1.679×10⁷ is not a near miss but two different objects.

**What the whole thread says about the method.** Three
necessary-but-not-sufficient gaps at three scales, all the same direction: **39
of 60** informative classes clear O.11 and none holds a triple; **D = 5…10** are
outside every proved reach and none has fallen to X = 8000; and **O.11's reach
falls with X** (97.7% → 88.1%) while nothing realises the excess. **The bounds
permit far more than occurs, at every level** — which is a statement about the
*method*: every bound here (O.4's τ_min⁴ < 2 + 1/X₁², O.9's 3ab < M^{4/3},
O.11's constant, O.12's (5+√21)/2) is a **size** argument, and size arguments
cannot see the arithmetic that actually forbids the configurations. **The D axis is where the gap is
NARROWEST, not where it is absent** — every observed failure lies outside the
proved reach and nothing inside it has ever failed, but that is *soundness*, not
tightness: the reach ends at D ≤ 4.899 and the smallest failure is D = 11, so
D = 5…10 is six values permitted-and-unfallen, which is row (2) itself. **So the summary is not "these
theorems nearly close O.2" but "the size arguments are now sharp enough to state
and still nowhere near what is true".**

**What is left of O.2.** Nothing structural — no hypothesis on M survives. What
remains is quantitative: at X = 8000, 13 of 109 informative classes clear O.11,
all with a = 1, and none holds three moduli in a window. **The bounds are not
what forbids triples in nature.** And closing O.2 would move
`rational-gram-bounded-on-windows` from `rigorous_finite` to `proved` and change
no conclusion — Note L says so directly, and the volume of the O-thread should
not be read as stakes.

**The load-bearing identities**, all exact and machine-checked: **S·T = −M·m**;
**V·W = M(m_i − m_j)** with W = X_jY_i + X_iY_j (the parallel session's, with no
cofactor); **a·|V|(X_jY_i + X_iY_j) = M(X_j²−X_i²)**, giving
|V| < (M/2√D)(R − 1/R) with no asymptotics; **U² − DV² = M²**; and
**δ_p(2M + δ_p + 4pa) = 4paM(p−1)** (0 violations in 1,002,709), so δ_p = 0 iff
p = 1 — the same fact as j = 2 ⟺ k = 1 — and M/d_p ≥ 17, recovering O.3′'s
constant by a second route.

**The geometry is r_k² < 2, i.e. M > 4√2·k√(ab), and the distinction decides the
theorems**: the modulus ratio is τ², not τ. Under the weaker r_k < 2 the ρ bound
is **false** — 193 violations in 277, ρ reaching 1.2375.

**The four non-fundamental close pairs are the falsifiers any extension must
survive.** `exp14` at X = 9000 finds four (1332 of 1336 explained close pairs sit
at k = 1): (17, 593393) k=20; (53, 423125) k=12; (37, 26245) k=4;
(37, 1635517) k=35. **All four have M even**, so O.3 is mute on all four and O.3′
permits both moduli while forbidding a third — c = gcd(M,2X) is 2, 4 or 12
throughout. Multipliers **act freely**: (1,5) at m = 2 admits k = 1, 3, 8, 21,
55, 144, i.e. τ₁, τ₁², τ₁³ — so "τ² is never integral" is false in general and
the *window* is the content.

**The θ axis and the Gram axis are the same object.** S_μ(M)² ≤ #{m∼M}·Q₂ with
**Q₂ = DIAG + OFF** exactly, DIAG ≍ X the squarefree incidence count and
OFF = Σ_{x≠y} μ(x²+1)μ(y²+1)·**G_M(x,y)** — literally the Gram entries Prop L.1
bounds. Cauchy–Schwarz is tight (S/CS ≈ 0.75) and |OFF|/DIAG ≤ 0.5, so the
*upper* bound §1 needs follows from OFF = o(DIAG), giving
S_μ(M) ≪ √(MX/√(log M)) = √(MX)/(log M)^{1/4}. **But temper it**: bounding G_M
and discarding signs is 11×–1988× too weak, so OFF = o(DIAG) is itself a
μ-cancellation claim. **And it closes on Chowla.** For fixed m the solutions form
ρ(m) progressions mod m, so every pair in OFF is y = x + h and
**OFF = Σ_m Σ_h Σ_x μ(x²+1)μ((x+h)²+1)** — a two-point correlation of μ(x²+1),
i.e. `chowla-for-x2plus1-is-open`. So the route is a **restatement**, landing on
the same blocker as everything else here rather than a new one, and must not be
quoted as progress. `sqrt-MX-law` stays
`extrapolated`. The unifying fact: a (modulus, root) pair **is** a primitive
Gaussian ideal, so per-progression = ℤ[i] and per-modulus = ℤ; the merging of
several primitive ideals into one rational modulus **creates the 4-cycles that
cost the Gram bound and produces the root cancellation that pays the Type II
sum**. One mechanism, opposite signs. ASP's (B) is indexed by rational m, so the
sieve-relevant exponent is the per-modulus 0.480, not 0.505.

**Conventions kill, and only recomputation catches them.** Three separate times
in one day a quantity was computed correctly and *described* in a way that
silently changed it: r_k as modulus-ratio vs X-ratio (τ² vs τ); DFI's
"determinant" D = ac − b² vs the discriminant −4, which decides whether their
theorem covers ν²+1 at all and had its resolution 200 lines from the quote; and
S_μ grouped per modulus vs per progression, differing by √(root count). Each was
found by *recomputing*, never by rereading, and each sat next to a correct
machine check — one O.1 test's docstring carried the window qualifier its own
note had dropped. **Tests protect the computation; nothing protects the
paraphrase.** Write the convention where the symbol is defined.

**Measurement cannot settle the triple question but it can kill a proposed
theorem.** `triples-cannot-be-settled-by-measurement` still holds for the triple
itself — the configuration never occurs, so every sweep is vacuous. Live
*close pairs* are a different matter: they exist, they are enumerable, and a
proposed extension that forbade one would be refuted on the spot. That is the
only measurement-shaped leverage on O.2 and it is worth using.

**K_{6,2}, and infinite.** Six cofactors — 1, 53, 423125, 24326641,
194502909745, 11182518951605 — each have both 10n and 17n of the form t²+1, and
the family is a Prop L.1 orbit on the dual side (D = 170, ε² = 678, two-step
ratios → 459682). So the Z-vs-Z[i] gap is **not** "2 instead of 1": Note F
forbids K_{2,2} over Z[i], while over Z the *unwindowed* bound does not exist.
The window is what supplies the constant — orbit members are ~4.6×10⁵ apart, so
a dyadic window admits one from each of the two orbits, which is the measured 2.

**O.2 in one configuration, and the place to start if anyone reopens it:
(a,b) = (2, 8321)**, M = 8319. Live (shared moduli 8065, 8581); a close pair
(ratio 1.06398); τ₁ explains it to five decimals; a **second** in-window
multiplier exists (k = 9, r₉ = 1.73542 < 2); and the residues permit both. So a
third modulus at ≈ 13996 would fit the window — **and it is not there**. Every
ingredient lines up and **occupancy alone forbids the triple**. That is why all
eight recorded routes fail: each tries to rule out something the residues, the
geometry and the multiplier existence all permit. Pinned by a test.

**O.2 is self-dual.** A cofactor pair sharing a modulus and a modulus pair shared
by a cofactor satisfy *the same conic with the roles swapped*, so "at most two
moduli per window for a fixed cofactor pair" and "at most two cofactors per
window for a fixed modulus pair" are one theorem — measured max 2 both ways at
X = 5000. That also dissolves an apparent tension: K_{s,2} is unbounded (six
cofactors share {10, 17}, infinitely many do) precisely because those cofactors
are 1, 53, 423125, … with ratios 53 and 7983, so **no window holds two of them**.
Unbounded totals and a bounded window count are one structure at two scales.
Structurally the rational graph is unbounded in K_{2,s} *and* in K_{s,2} but has
**no K₃,₃** — the row-merging thickens each side separately and neither jointly.
That buys nothing via Kővári–Sós–Turán (the bound is 2–4 orders loose here);
freeness matters only through the Gram structure, never through edge counts.

**The literature side is closed.** Every load-bearing quotation has been read in
its paragraph, not just its clause — DFI (300 dpi) and Li on one side,
Ford–Maynard, Merikoski, Teräväinen, Maynard's well-factorable, ASP and
Granville–Shao on the other. Eight findings, of which **three strengthened a
claim rather than correcting one**. The remaining risk is not in the citations.

**Eight routes on O.2's general case are closed with reasons** (Note O). The two
that most look worth retrying and are not: **there is no residue obstruction at
all** — the exact four linear conditions plus the conic are simultaneously
solvable for all 21 pairs that survive the cheap αβ | M filter — and **Nagell
runs the wrong way**, bounding fundamental solutions from above when a lower
bound is what is needed. Any proof must be about **occupancy**, not congruences.

**The big methodological finding, which cost both sessions a day of work.**
Generating candidates from *multipliers* and testing occupancy afterwards
searches a mostly-empty parameter space, and worse, **r₁·r_k is a ratio between
solution classes and does not predict the spacing of the occupied moduli** — on
(1, 115921) it predicts 1.31 and the observed minimum ratio is 33.77. Every
r-product statistic either session produced is withdrawn. The correct direction
is inverted: **enumerate realised ratio classes, take those with two moduli in a
window, and read off which multiplier index explains the ratio** — occupancy is
the input, so it cannot produce a dead configuration. Check the residual on the
index; eyeballing it produced a misattribution that `exp14` caught.

Two dead ends worth not repeating. The ideal route (Q̄, Q̄″ coprime) is **closed**:
coprimality holds in 5 of 65 cases where it can be observed. And there is **no
local obstruction** — all 95 candidates are satisfiable mod M — so O.2 is not a
congruence statement. Finally, the empirical support for O.2 is **31 informative
classes** at X = 4000 (208 at X = 60000), not the 278,939 above threshold: a
class is silent unless it has three shared moduli at all, so "verified over
hundreds of thousands" would be true and misleading.

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

**Citation audit, 2026-08-28.** The load-bearing `quoted` claims were re-checked
against the sources rather than the notes — DFI pp. 423–425 from 300 dpi images,
ASP (B)/(B1)/(B2)/(B3) p. 1043, Ford–Maynard (1.1) and (II) pp. 1–2, Li pp. 1–2
and 6. **Every quote is verbatim correct and no claim needed retracting.** Two
things came out of it and both are about *placement*, not accuracy:

- **The determinant trap.** DFI p. 425 says it "would be interesting to extend
  the arguments herein to deal with … negative determinant". Their determinant is
  **D = ac − b²**, so ν²+1 has D = 1 > 0 and *is* covered (Theorem, p. 424); its
  **discriminant** is −4, so a reader who checks that concludes the opposite and
  takes out three claims at once. The resolution was 200 lines from the quote in
  Note C and is now beside it.
- **An understatement.** Ford–Maynard's (II) quantifies over |ξ_m| ⩽ τ^B(m),
  |κ_n| ⩽ τ^B(n) — *divisor*-bounded, not the 1-bounded the requirements table
  says. That is a strictly stronger hypothesis, so Note F applies a fortiori;
  the table is safe but now labelled.

So: re-verify by **reading the source, not the note** — the notes were right, and
the two findings were both invisible from inside them.

**Note F's C₄-free lemma is not about x²+1 — it is about a line.** Every
A_c = {a+ci : a²+c² ≤ Q} is C₄-free by the same argument (the product *and* the
sum of the two a's are determined, so the pair is), and every one has
|A_c| = ⌊√(Q−c²)⌋, hence **κ = 1 − c²/Q → 1 exactly**. A single line cannot have
κ > 1: its count is its length and its length is √Q. Two lines always admit a
cycle — (1+2i)(6+2i) = 2+14i = (2+2i)(4+3i) at (c₁,c₂) = (2,3). This *sharpens*
the obstruction: x²+1 is not unluckily C₄-free, every line is, and α = 1/2 is
forced for all of them, so there is no nearby line with more room and an escape
must leave the family. **And x²+1's escape from the doubly-dyadic 4-cycle has a cause**: for
x²+D, four consecutive arguments give a cycle exactly when **D = k²+3k+1**
(identity: the difference of the two products is 4(D − k² − 3k − 1)), so
D = 1, 5, 11, 19, 29, … all carry one. x²+1 is the **k = 0** member and its
instance is degenerate — one of its four values is 0²+1 = **1**, the unit
modulus. D = 5 escapes separately, on the modulus ratio 2.333. Every k ≥ 2 is a
genuine counterexample with both ratios falling toward 1. So O.12's conclusion is
not general, and the survivor survives for the same reason the unit cofactor is
excluded everywhere else here. **And the same holds one level up: x²+39 has
cofactors (5,8) — one band — sharing three moduli 8, 11, 15 — one window**, so
the analogues of Conjecture O.2 *and* O.12 both fail there; seven unit-free
triples over D ≤ 60, and D = 1 in none of them. Neither result touches x²+1,
where O.12 is proved and O.2 has no counterexample to X = 8000; what they remove
is any reading of the Note O theorems as general facts about degree-2 sequences. **And there is one mechanism under all of it**: a·m = X²+D and
b·m = Y²+D give **aY² − bX² = M·D**, so the invariant Note O calls M is really
M·D and every bound weakens by a factor D — O.9 becomes 3ab < (M·D)^{4/3}, which
at cofactors (5,8) reads 120 < 572 at D = 39 (permitted, and the triple occurs)
against 120 vs 4.33 at D = 1 (forbidden, and none occurs). **x²+1 is the D = 1
end where every bound is tightest**, which locates the Note O theorems rather
than weakening them.
It also explains Note K's κ threshold as a coincidence of
parameterisation — κ = |B|² counts lines, C₄-freeness permits one, so both are
functions of the same integer. **Two points settle that κ is not doing the work**:
A = {x+i} ∪ {2+2i, 4+2i} has κ = 1.000004 at X = 10⁶ against the bare line's
0.999999, and is not C₄-free.

**The Note O thread (Z-side triple question) is the parallel session's and is
close to closed.** Its live form is the p-adic valuation argument: with p^e ‖ M,
s_i = min(e, v_p(S_i)) and t_i = min(e, v_p(T_i)) satisfy s_i + t_i ≥ e, giving
v_p(V_ij) ≥ max(min(s_i,s_j), min(t_i,t_j)); ordering by s yields
**M | V₁₂V₁₃V₂₃**, hence **3ab < M^{4/3}** with no hypothesis on M at all.
Supporting identities: **S·T = −M·m** (theirs) and **V·W = M·(m_i − m_j)** with
W = X_jY_i + X_iY_j (mine — the cofactor cancels), from which
gcd(V,M) = 1 ⟺ M | W. **Two traps are recorded there, both live**: the coverage
figure is over classes with ≥3 moduli (60 of 1,815,154 at X = 3000 — anything
quoted over all classes is ~30,000× inflated), and the **two-term** strengthening
v_p(V₁₂)+v_p(V₂₃) ≥ e does *not* give M | V_aV_b for a fixed pair — the ordering
is per-prime, 5 of 216 triples witness it, and the fixed-pair version would
close the conjecture in one line via 3ab < b−a. Recorded as
`the-two-term-strengthening-of-the-valuation-argument-is-blocked`
(`rigorous_finite`, with all five witnesses) so it cannot be quietly retried.

Read [README.md](README.md) and [notes/README.md](notes/README.md) first. Run
`python -m pytest -q` before trusting any measurement.

## Non-negotiables

- **Normalisation.** Q (or N) = norm bound; X = √Q = range of x; |A| = X.
  State which one every exponent is relative to. "Level N^{1/2}" = "level X".
- **A result much better than the problem is hard should be attacked before it
  is used.** A three-hour-old lemma gave `3ab < b − a`, impossible for a ≥ 1, so
  Conjecture O.2 was closed in one line. It was not: the lemma's conclusion holds
  *per prime*, the ordering that selects the pair depends on the prime, and only
  the three-term product is uniform. **5 of 216 realised triples witness the
  failure** — but 211 do not, so the pattern was 97.7% supportive and no number
  came out wrong. It was caught by asking what the quantifier ranges over, before
  running anything.
  This is the same detector as the vacuous denominator, one level up: *99.26%
  coverage of an open problem*, and *a one-line proof of the open conjecture*,
  are both implausible on their face, and implausible-on-its-face is checkable
  without knowing any of the mathematics. **When a step is suddenly much stronger
  than the difficulty of the thing it settles, that is the moment to look for the
  quantifier, not the moment to write it up.** Arithmetic will not catch this
  class: every number involved can be correct.
  **But be honest about how narrow that detector is.** It did not fire because
  anyone was careful. It fired because `3ab < b − a` is *impossible*, visible by
  inspection at a = 1. Had the same bad reduction yielded `3ab < M^{2/3}` —
  still far stronger than the real bound, still wrong — nothing would have fired
  and it would have shipped. So the rule is **"the conclusion is too strong to be
  true"**, not "check the quantifiers", and it only works when the over-reach
  breaks something obvious. Between *suspiciously good* and *correct* there is a
  band where no self-check fires at all, and that band is where the Plücker
  constant lived for hours. **In that band a second independent derivation is the
  only detector there is** — which is the argument for overlapping the notes at
  the load-bearing identities rather than partitioning them cleanly. A percentage
  also has to carry its **direction of travel**: a proved bound whose measured
  reach is *falling* with X (O.11: 97.7% → 88.1%, admissible count doubling per
  doubling of X) is a different object from one that is flat (O.10: ~35%), and
  "6.85× better" alone tells a reader the opposite of what the data says.

- **Before believing a sweep's headline, ask what its output would look like if
  the finding were absent. If that looks the same, the sweep measured nothing.**
  (The parallel session's formulation.) This is *one* rule and it arrived wearing
  a different statistic each time — percentage, population, extremum, axis — which
  is why restating it more clearly never helped and why it fired repeatedly after
  being written down. **The operational form is a question, not a principle:
  *which set does the claim range over, and is that the set I computed?*** — asked
  out loud, before the number is read. Every instance below produced a correct
  number and an unlicensed inference:

  - *Vacuous denominator.* "95.68% of classes excluded" and "99.2% excluded" read
    the same whether a theorem is strong or **1,815,094 of 1,815,154 classes have
    fewer than three moduli and cannot host the configuration**. On the 60 that
    can, the figures are 15% and 54.5%.
  - *Consistency vs silence.* A grep for contradictions returns nothing whether
    both notes agree or only one speaks — so agreement was read as neither having
    said it, when Note L had.
  - *Absent base rate.* 27-of-28 uncited claims reads the same whether the notes
    are negligent or id-citation is simply not the convention (it is not — 20%).
  - *Missing direction of travel.* A bound at ~35% that is **flat** in X and one
    at 97.7% → 88.1% that is **falling** are different objects; "6.85× better"
    tells a reader the opposite of what the data says about the limit.
  - *A column of zeros.* Empty at a ≥ 2 looks the same whether it is a law or a
    range the sweep cannot reach — largest available b was 8321 against a 7×10⁴
    crossover.
  - *Fixed windows across sequences.* x²+c² on [64,256) gives max Gram
    2,3,3,3,4,5,6 across c — "the gap widens with c" — and normalised to each
    sequence's own √Q it is **2 throughout**: the window was varying, not the
    sequence.
  - *Extremum where the worst case was needed.* max ε was exactly c² and would
    have restored a threshold; **min ε was 10⁻⁸** and restores nothing.
  - *The loop's natural population.* An X-loop counts moduli, so it reports the
    mean over all bands when the informative statistic lives in one band; the
    informative subset is never the one the loop naturally counts.
  - *The unextended axis.* A sweep stopping at c = 5 or D = 10 looks identical
    whether the property is universal or holds on a short initial segment. Both
    were checked at five or six values and read as general; both failed at the
    next one.
- **A comparison feels like a finding; a property feels like a restatement — and
  the property is usually the stronger result.** "The mean drops below the
  barrier's line" reads as a discovery. "The count is a 0/1 indicator, so an
  error term better than O(1) means knowing it exactly" reads as a restatement,
  because Note F had said it for Z[i] already. The second is strictly stronger —
  pointwise rather than on average, and immune to the objection that sinks the
  first ("your band holds two cofactors"). **The stronger result looked like the
  smaller one**, and the weaker one was nearly published instead. Same asymmetry
  that let the Plücker constant survive: a right-*shaped* sentence beats a right
  statement. When a comparison and a property are both available, suspect the
  comparison. **And note where each comes from: a sweep emits comparisons, a
  derivation emits properties.** The tooling biases toward the weaker form, which
  is an argument for deriving before measuring — the reverse of the order most of
  this repo's findings were produced in. It also explains the other survivors:
  "the mean is U-shaped", "κ crosses 1 where C₄-freeness does", and the Plücker
  constant are each a *relation between two numbers* standing in for a
  *statement about one object*, and each time the relation was the weaker claim.
  **And a derivation that predicts falsely still establishes something a sweep
  cannot.** Generalising O.12 to x²+c² gives V·W = c²·M·(m_i − m_j), hence a
  bound weaker by c², hence a threshold below what a dyadic band supplies at
  c ≥ 2 — predicting O.12 fails there. It does not: banded cofactors still share
  at most one in-window modulus at c = 2, 3. The prediction was wrong and the
  derivation was not wasted, because what it established is **which step uses
  c = 1 essentially**: the *argument* is special to x²+1, the *fact* is not known
  to be. A sweep would have shown max Gram 1 for every c and read as "O.12
  generalises", which is exactly what is not established. Measurement offers the
  comparison; derivation supplies the property; **and here the measurement was
  the misleading one.**

- **A guard can check a strictly weaker proposition than the one it is named
  for, and neither of the other two countermeasures reaches it.** `exp09` sweeps
  `M = 2; while M <= cap: …; M *= 2` — windows **anchored at powers of two** —
  while `rational-gram-bounded-on-windows` says *"every dyadic window [M,2M)"*.
  [8,16) and [16,32) between them **miss (9,17)**, which is precisely how the
  other session's line-family sweep reported the property *holding* at c = 6 on
  the very witness that refutes it. Injected-violation testing does not catch
  this (the sweep can fail, and does), nor do enumeration floors (it covers a
  large population). It reports on a real property — just not the one in the
  claim. Re-measured by ratio: the conclusion survives at X = 2000 and 4000, so
  only the evidence was narrower than the wording.
  **The countermeasure is a wording check, not a code check: for each claim, does
  the experiment quantify over the same set the statement does?** "Every dyadic
  window" versus "every power-of-two window" is a difference visible in the
  sentence and invisible in the output — the same instrument as the source-
  paraphrase check, turned inward, where the drift is between claim and code
  rather than between paper and claim. What actually caught it was **two
  computations disagreeing**, which is the redundancy argument in its most direct
  form: not a second reading, a second *computation* whose disagreement was
  itself the signal.

- **Duplicated computation is the only safeguard here that works while nobody is
  paying attention.** Every other countermeasure in this file requires someone to
  remember to apply it, and the record shows all of them being written down and
  then broken by their own authors within the hour — the `&&` that could not gate
  because of a pipe, the enumeration floor missing from a test written after the
  floor rule, the vacuous denominator, the quantifier question, the informative
  subset three times on one claim. **What actually caught the two largest errors
  was two sessions computing the same thing on different axes and getting
  different answers.** Neither was reviewing the other. Nobody had to be
  vigilant: the disagreement did the work by existing. That is a property of the
  arrangement rather than a practice, and it is the argument for **overlapping
  the computations, not the reviews** — redundancy at the identities *and* at the
  sweeps, on different axes, with disagreement as the alarm. Three of tonight's
  findings arrived this way, including both that reframed the O-thread.
  **And the reason is a mechanism, not a preference.** A checklist item costs
  attention *every* time and pays only when it fires, so its expected value falls
  as vigilance decays — which is why every rule in this file was broken by its own
  author within an hour of being written. An axis extension costs attention once
  and **raises the probability of the next one**, because the payoff is itself the
  motivation. **The countermeasure that works unattended is the one whose success
  makes it more likely to be repeated.** Nobody had to be reminded to extend the D
  axis a second and third time; the second happened because the first had paid.

- **A bounded search that finds a clean pattern is the most persuasive way to
  talk yourself out of a caution you had already got right.** The other session
  searched cofactors ≤ 300 and found every failure witness below cofactor 9 —
  D = 11 at (3,4), D = 14 at (3,5), D = 19 at (4,5), D = 39 at (5,8) — concluded
  that failures announce themselves at tiny cofactors, and on that basis
  **downgraded its own earlier warning** that the surviving D might simply be
  under-swept. The warning was correct: D = 35's witness is at **(2249, 3756)**,
  three orders of magnitude outside the search that "established" the pattern.
  **A bound's silence is not evidence about what lies outside it** — and the
  damage was not the wrong pattern but the retracted caution, which had been
  right before the evidence arrived. When a bounded search produces a clean law,
  the first question is what the bound excludes, and the second is whether the
  law is being used to retire a doubt that the search could not have addressed.

- **A wrong identification between two notes' machinery costs more than a wrong
  answer, because it manufactures an apparent contradiction.** Note L's ε and
  Note O's τ act on the same solution set of aY² − bX² = M. Identifying them —
  *"the fundamental multiplier is the fundamental automorph"*, which sounds like
  a definition — produced "two moduli of **one orbit** inside a window", which
  **contradicts Prop L.1** and reads as a defect in it. The natural next move is
  to go looking for the error in Note L, and there is none: ε² = 1.679×10⁷ and
  τ₁² = 1.877, two different objects differing by a factor of 8.95×10⁶. **Every
  other trap here produces a wrong answer; this one produces a wrong
  *retraction*, of something correct, in someone else's work.** What separated
  them was computing *both* quantities on *one* example — the same instrument as
  asking why two derivations of a constant agree, aimed at two pieces of
  machinery instead of two derivations. **When two notes' objects look like the
  same object, evaluate both on one instance before believing it.**

- **Two sessions on one machine share `/tmp`, and a commit message written there
  will be committed by the other session.** Commit `a142e23` adds 59 lines to
  Note O under the message *"My own five prose citations; four now run, and one
  of them was wrong"* — a message written four hours earlier, by the other
  session, for an unrelated commit. Cause: `/tmp/msg.txt`, written during a
  `git commit --amend -F /tmp/msg.txt` and still holding that text when the
  second session used the same path. **Nothing was lost and the log is wrong**:
  a reader following it finds 59 lines of Note O filed as claim-citation work.
  Use the session scratchpad — the path is in the system prompt and is
  session-specific — never `/tmp`, for message files, for background-job output,
  for anything. This is the collision hazard that `git commit -- <paths>` cannot
  see, because it happens **before git is involved** — below every guard here:
  the pathspec scopes what git commits, floors bound what a check sees, and
  `check_claims_diff` compares content, and none of them touches a file read
  earlier. **The countermeasure at that layer is content addressing rather than
  path trust: a hash survives a shared path, a filename does not.** Verified on
  this side afterwards — no repo tooling writes to shared temp (nothing in
  `tools/`, `experiments/`, `x2plus1/`, `tests/`), and the one commit whose
  message came from a temp read matches its diff exactly, so the leak went
  outward only. `$TMP` and `%TEMP%` resolve to the same shared directory as
  `/tmp` here; six files from three *other* sessions were sitting in it.

- **A citation to the nearest script you own is invisible to every check but
  running it.** The prose-citation defect (`experiment` naming a sentence) is
  visible in the string and a guard catches it. Its successor is not: **eleven
  claims here cited `exp23` — a real, running, correct experiment — which
  computed none of their numbers.** Every one named it because it was the nearest
  file the author owned, not because it contained anything. **A valid-looking
  citation to a working file passes the guard, passes the eye, and fails only on
  `python experiments/… | grep <the number>`.** Committed eleven times in one
  night against the very file written to fix the earlier version of the same
  defect. When adding a claim, run its cited experiment and find its number in
  the output, or extend the experiment until you can.

- **Put finished results next to each other on purpose.** Four findings tonight
  came from adjacency alone — the τ/ε split, the three-scale gap, |V| ≥ 2
  appearing in both the D family and the line family, and the pair/chain
  thresholds turning out to be one formula. In **every** case both results were
  already correct and already recorded; nothing was discovered by computing
  anything new. That makes it a different and cheaper operation than the
  duplicated computation that catches errors: this one needs a second
  **placement**, not a second run, and the material already exists. It has paid
  four times by accident and three times on demand. **And the productive pairs
  are across halves, not within them**: τ/ε bridged Notes L and O, D against κ
  bridged structure and density, μ against D bridged structure and cancellation.
  The within-half pairs tried — the 43 classes against mean G, θ against D — went
  nowhere. **Place results that were recorded by different arguments, not results
  that are about the same object.**

- **A float landing on a strict/non-strict boundary is invisible to the eye and
  to the test.** The asymptotic D-reach turns on whether a band's u < 2 attains
  (u−1)/√u = 1/√2. It does not — u < 2 is **strict** — so D = 8, where the
  threshold is exactly 1/√2, is the last **covered** value. But `u0(8)` evaluates
  to **1.9999999998**, so a bare `< 2` check reports D = 8 as *uncovered*, and
  the printed number looks right, the comparison looks right, and the answer is
  off by one value. **At a boundary, reason from the identity** — (2−1)/√2 = 1/√2
  exactly — **not from the float.**

- **A false alarm is self-limiting; a false clean bill is self-reinforcing.**
  Investigating an alarm costs you and you stop; a clean bill *retires the
  question*, and the next reader inherits "already checked". All four
  audit-hunting-its-own-defect instances here produced a **clean bill** and none
  produced an alarm — which is not chance: `M*D` as a regex means *zero-or-more M
  then D*, and a floor pattern that cannot see `assert len(x) > N` misses the
  common form. **A pattern too permissive matches more and reports less**, so
  every failure of a checker written this way falls on the silent side. Assume a
  clean audit is broken until it has failed on an injected violation.

- **And the same defect produces a false ALARM when the pattern is too specific
  — which is how it lands as an accusation against the other session.** Checking
  whether my own CLAUDE.md edit had survived, I grepped the sentence I had
  written. It returned **0 in the working tree and 0 in HEAD**, and the peer had
  just committed that file — so the reading was *their write clobbered mine*.
  It had not: the phrase is **hard-wrapped**, "algebraically" ends line 946 and
  "equivalent expression" begins 947, and the text was there all along, already
  committed. `1.9999999999999996` — a fragment that cannot wrap — finds it at
  once. **Every note and CLAUDE.md here is wrapped at ~79 columns, so any
  verification grep of more than about forty characters of prose is at risk**,
  and the failure is silent in the direction that matters: it says *absent* when
  the truth is *present*. **Verify landed text with a token that cannot wrap — a
  number, an identifier, a symbol — never a sentence.**
  The pair is the whole rule: *too permissive ⇒ false clean bill, self-
  reinforcing; too specific ⇒ false alarm, self-limiting*, one defect with two
  signs. The asymmetry above held exactly — the alarm cost two tool calls and
  stopped. But note where a false alarm is **not** cheap: on a shared file it
  reads as the other session having destroyed your work, and this is the
  **second** time an instrument here came one step from that accusation (the
  over-reporting claims-diff grep was the first). Against a peer, self-limiting
  is not the same as harmless.

- **Extend the axis nobody extended.** Two results in one night came from the
  same move, and both overturned a conclusion that had been checked at five or
  six values and read as general. The doubly-dyadic C₄-free property was verified
  for x²+c² at c = 1…5 by one session and c = 1,2,3,5,7 by the other; **neither
  ran c = 6**, where it fails. Extending the *next* axis — D in x²+D — produced
  the mechanism: four consecutive arguments give a 4-cycle exactly when
  D = k²+3k+1, x²+1 is the k = 0 member, and its instance is degenerate because
  one of its four values is the unit. **A sweep that stops at c = 5 or D = 10
  looks identical whether the property is universal or holds on a short initial
  segment** — the sweep-headline question applied to the axis rather than to the
  population. Ask which parameter was held fixed because it was never varied, as
  opposed to because varying it was considered and rejected.

- **Before asking whether a gap is real, ask what depends on it.** A hedge was
  found in Ford–Maynard's footnote 2 — "closely related to", not *equivalent to*
  — and read as the residual inference under `gaussian-to-rational-bridge`.
  Settling whether the paper makes the relation precise elsewhere would need a
  re-read the repo cannot do from what it holds. **One registry query settled it
  instead**: `fm-footnote2-is-note-F-G` has exactly one dependent, and
  `selberg-nu-zero-binds` is `quoted` with an empty `depends_on` — ν = 0 comes
  from Selberg via p.2 and Theorem 2.1, so the inference the hedge would block is
  one this repo never makes. The hedge is real, is the source's, and is **off the
  path**. This is what the dependency graph is *for*, and it had not been used
  this way before: **the question "is this gap real?" is often harder than "does
  anything stand on it?", and the second question answers the first whenever the
  answer is nothing.**

- **A summary rounds a nearly-zero quantity to zero, because that is the shape
  the sentence wants.** The three-scale gap has its narrowest instance on the D
  axis — proved reach ends at 4.899, smallest failure at 11, so **D = 5…10 is a
  six-value strip that is permitted to fail and has not**. Summarising, the other
  session wrote the D axis as *"the one place proof and data agree exactly"*: two
  true constituent facts (no failure inside the reach, every failure outside it)
  compressed into a claim that contradicts the very table it was contrasting
  against. **Small became none because "gaps everywhere, except here" is a better
  sentence than "gaps everywhere, smallest here."** Not carelessness — a summary
  is a compression, and a quantity close to a clean value is what compression
  destroys first. *(Recorded as **one** instance. I first wrote it as three,
  reaching for the density table and the vacuous denominator — but those were a
  documented sieve truncation and a wrong denominator respectively, neither of
  them rounding. Three is a better sentence than one, which is the same
  operation.)*

- **A strict comparison at an exact boundary is decided by which algebraically
  equivalent expression you evaluate.** O.12's D-reach turns on whether
  u₀ = 2 at D = 4V. It is exactly 2 (sympy: (u−1)²/u = 1/2 has roots 1/2 and 2),
  but `v = (t+√(t²+4))/2; u = v²` returns **1.9999999999999996** while
  `u = (2+t²+t√(t²+4))/2` returns **2.0** — so a bare `u < 2` reports D = 8 as
  uncovered from one and covered from the other, and the reach is off by one
  value of D. **The trap is not that floats are inexact**; it is that equivalent
  forms diverge *exactly where the comparison is strict*, which is precisely
  where the answer changes. One session read the float and got it wrong; the
  other got it right **by luck**, having picked the exact expression without
  reasoning about it. Decide boundary cases symbolically.

- **Paraphrases of a source drift toward whatever makes the local argument
  work, and only re-reading the sentence catches it.** `fm-barrier-range-is-
  small-moduli` was read — by the other session, quoting it back — as recording
  "mean G ≥ 1" as Ford–Maynard's threshold. Footnote 2, p. 7 asks for *"an error
  term better than O(1) on average over m₁, m₂"*: a condition on the **error
  term**, with no threshold on any mean. The measurement was right, its
  description was right, and the sentence between them had acquired a
  significance the source does not give it. Note F had the correct reading all
  along — the count is 0 or 1, so the error term **is** O(1) and no averaging can
  improve it, which is *pointwise* and strictly stronger than any statement about
  a mean. **Re-read the quoted sentence, not the claim about it**; and note this
  was found by asking *is the number in our claim the number in their paper* —
  the same question that caught the Plücker constant, aimed at a citation.

- **Consistency and silence look identical from a grep.** Notes L and O were
  cross-checked for contradictions about how many moduli a dyadic window can
  hold. They agree — identically so — and that agreement was read as *neither
  note having drawn the connection*, which became a claim, a commit message
  saying "neither note said so", and a message to the other session announcing
  it as new. Note L states it outright, in a section written here, **and states
  it more carefully**: that proving it upgrades one claim's status and changes no
  conclusion. The re-derivation was correct; the novelty and the added
  significance were not. **A search for contradictions cannot find that one side
  already said the thing** — it returns nothing in both cases. Before calling a
  cross-note observation new, grep for the *claim*, not for its negation. This
  hazard is specific to auditing notes at volume, which is exactly when it is
  most likely to fire.

- **When a recorded number does not reproduce, read the paragraph it sits in
  before looking for a bug.** Note M's squarefree densities did not match a fresh
  exact sieve. I proposed inconsistent rounding (a story fitted to two rows that
  happened to land near a rounding of the exact value, and true of neither),
  tested a p ≤ √X cutoff in code, and then — correctly refusing to fit a cause —
  recorded the last row as *unexplained*. It was explained: **"a sieve truncated
  at P = 20 000", three lines above the table**, in the file the claim cites. The
  truncated column reproduces every digit to six places and its stated error bound
  holds, so the numbers were never wrong; my correction was. Refusing to invent a
  cause is the right instinct and is not a substitute for reading. This repo
  already says *pull the paragraph, not the clause* about the literature; it
  applies with more force to its own notes, where the paragraph is three lines
  away. **The failure mode is searching the code for what the prose already says.**
  And note the shape: an approximation with a documented error bound reads exactly
  like an error once the sentence documenting it is out of view — which is the
  same thing `inferred` exists to stop, one level down.

- **Gate the claims diff with `tools/check_claims_diff.py <id> ...`, chained.**
  It parses `HEAD` and the working tree, compares claim dicts by id, and exits
  non-zero on anything unnamed. `python tools/check_claims_diff.py <ids> && git
  commit ...` — the `&&` is the whole point; see the shared-file entry below.

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
- **Pull the paragraph, not the clause.** When quoting a source, read the whole
  paragraph into the claim's notes, not the sentence you came for. Three findings
  in one session sat one sentence past text this repo had already quoted,
  verified and cited correctly — C⁻ being the *lower-bound* constant (FM p. 2),
  C_bd being a class of *dense* sequences (FM pp. 1, 7, 13, 14), and FM's
  "natural barrier" being *unconditional* at c = 1/2 (footnote 2, p. 7). No guard
  can catch these: the locator is right, the quote is verbatim, the status is
  right. Only reading past the clause finds them. The normalisation convention
  behind the second was inside the very sentence `fm-no-admissible-theta-at-
  density-half` is built on.
- **A claim's `experiment` must name something that reproduces its numbers.**
  Nine of roughly forty claims with an experiment field named a file that
  computed something *adjacent* — seven pointed at `exp13`, which does two-step
  ratios and no mean, diagonal, argmin or cross-sequence table; two pointed at
  `exp16`, which did neither the signed sum nor the Cauchy–Schwarz bound. The
  numbers had come from scratchpad scripts run once and discarded. `tests/
  test_claims.py::test_support_paths_exist` checks the file *exists*, which is
  not the same question. **And writing the experiment is not bookkeeping: both
  times, the rerun at a second size produced something the one-shot script could
  not** — the mean-G classifier's threshold turned out to move with Q, and the
  Cauchy–Schwarz chain turned out to predict at every band rather than one. If a
  number is worth a claim it is worth a script that can be run again at a
  different size.
- **A control is not a classifier.** A control shows an argument does not prove
  too much and needs exactly two points: a²+b⁴ has mean G 3.59 where x²+1 has
  0.022, so the mean-o(1) objection does not rule out dispersion for the sequence
  it demonstrably works on. That is sound. Reading it as *mean G > 1 separates
  captured from uncaptured* is a different claim about a whole population, and it
  was false — x³+2y³ is captured and sits at 0.1888, below the sequence with no
  known outcome. The tell was in the construction: the "law" was built from two
  points and confirmed on two more, one of which had no known outcome, so the real
  confirmation set was **one sequence**. And it generated its own supporting
  evidence — a literature quotation was gathered for a statement already false.
  When testing a proposed classifier, pick the case the incumbent invariant
  *cannot* see (here κ is equal for x³+2y³ and a²+b⁶), not the next case to hand.
- **If the values reproduce but no law does, record the values.** One quantity —
  the mean of G over cofactor bands — took four corrections in one session
  because three different laws were fitted to it and all three failed: 1/N, then
  (log X)/N, then N/X for the left arm of its U. Every time, the *values*
  reproduced exactly between two independent constructions and the *law* did not.
  Some measured quantities here are reproducible and unparameterised, and naming
  a shape for them is a reflex worth suppressing. The tell is that the
  disconfirming number was already in hand each time and got closer each time:
  first a second X was never taken, then a drift was recorded at 5.6 and the law
  quoted anyway, then the counterexample sat two rows apart in the same printed
  table. `rigorous_finite` is the status for values; `extrapolated` is for a
  fitted law and demands the fit be shown to hold.
- **Every string edit asserts its anchor.** A `replace` whose anchor text has
  moved writes back identical content and reports success; `git commit` then says
  "nothing to commit, working tree clean", which is easy to misread as a
  collision with the other session when one has genuinely happened that day. A
  silent no-op is a green result with no work behind it. Same shape as the rule
  below, one level down — and the aggravating factor is that *a plausible
  explanation for the anomaly is what stops you checking the implausible one*.
  Verify by grepping HEAD for the new text, not by trusting the script or the
  git output. **And run `git diff --cached` before every commit.** Explicit-path
  staging was the fix for `git add -A` collisions and is **not sufficient when
  two sessions edit the same file**: `git add CLAUDE.md` sweeps the other
  session's uncommitted CLAUDE.md work exactly as `-A` did. It happened here —
  one session's CLAUDE.md edit failed its anchor assert, the script died, the
  `git add` ran anyway, and the commit carried the *other* session's paragraph
  under a message that did not describe it. Nothing was lost and the content was
  correct; the attribution and the message were not. **Look at what is staged,
  not at what you meant to stage.** But a check cannot close a race — the same
  collision happened *while* that check was being run, the other session
  committing in the window between the check and the commit. **So commit with a
  pathspec: `git commit -F - -- <paths>`** (with one gap: it cannot commit an
  *untracked* file, which needs `git add` first) takes the working-tree content of
  exactly those paths and ignores the index for everything else, so it cannot
  sweep the other session's staged work even if you forget to look. (Options
  before the `--`; `git commit -- <paths> -F -` parses `-F` as a pathspec and
  fails.) The check is then a backstop rather than the only defence.
  **But the pathspec isolates files, not authors, and that is a much weaker
  guarantee than it sounds.** It was used, correctly, on commit `87a42a8` — whose
  message describes exactly one thing, making an O.4 citation precise — and that
  commit carried **nine** claim ids, eight of them the other session's O.3/O.3'
  repoints and corrected counts, entirely undescribed. The pathspec did its job:
  it committed the working-tree content of `research_state/claims.json`. Both
  sessions *edit that file*, so scoping to it excludes nothing. A pathspec
  protects you only where the sessions touch disjoint paths, which is precisely
  the case that was never the problem. On a genuinely shared file the only
  defence is to look at what the diff *contains* — and to do it by **parsing both
  versions and comparing**, not by grepping the diff. The grep form was tried
  here first and is wrong: a claim's `"id"` line is *context*, not a changed
  line, so it reports every id whose neighbour moved. On the very next commit it
  named seven ids where four had changed, and three of the phantoms belonged to
  the other session — the check was one step from producing a false accusation
  of exactly the collision it was written to detect. The correct form loads
  `git show HEAD:<path>` and the working file, keys both by id, and diffs the
  dicts; it reported four, which was right. **A check that over-reports on a
  shared file is not the safe direction: it manufactures collisions.**
  **And the check has to gate the commit, or it is decoration.** The parsed
  version was written, run, and it worked — it reported seventeen changed claims
  where four were mine — and the commit went through in the same breath, because
  the check was a separate `python -` process and its `AssertionError` did not
  stop the shell from reaching `git commit` on the next line. Third crossed
  attribution of the night, this one committed *over* a correct warning I had
  just read. The repo's governing rule is that a guard not on the path is not a
  guard, and **the path here is the shell**: put the comparison and the commit in
  one process, or chain them with `&&` so a non-zero exit actually stops it. A
  check whose failure the next command ignores is worse than none, because it
  produces the feeling of having checked.
  **And the `&&` is not enough if the check is piped.** `python -m pytest -q |
  tail -1 && git commit` **always commits**: a pipeline's exit status is the last
  command's, and `tail` always succeeds. That pattern ran here for most of a
  session beside an unpiped `tools/check_claims_diff.py … && git commit` that
  gated correctly — so the claims gate worked, the test gate never did, and one
  commit went out red. Both sessions hit this independently in mirrored forms: a
  check whose correct output reached a reader who overrode it, and a check whose
  output could not reach the gate at all. **Use `set -o pipefail`, or do not pipe
  the checker**, and verify the gate against a deliberate failure —
  `false | tail -1 && echo ran` prints `ran`, which is the whole bug in one line. Verified from `git show`, not from the report — the other
  session flagged it, and the flag was right, but a collision report is a claim
  like any other.
  **And one edit per block**: a script with two `replace` calls
  whose first raises dies before the second, prints only the second's success
  line, and reads as a full success. That happened here — the anchor an earlier
  commit of mine had moved — and the resulting commit message described a
  correction that never applied, while the registry recorded it as done. (A related near-miss: a two-branch `replace` here would have
  written a literal `PLACEHOLDER` into `claims.json` had its first branch
  matched. It did not, so the result was correct by luck. `tools/` has no guard
  for this; the sweep for `PLACEHOLDER`, duplicated sentences and unbalanced
  `~~` across the registry and every note comes back clean as of this writing.)
- **A guard is not verified until it has failed on an injected violation.** The
  same session's note-to-registry guard passed vacuously: a lowercase-only
  pattern skipped 26 of 103 claim ids, including `sqrt-MX-law` and the refuted
  claim it was being tested with. It reported green while seeing nothing. This is
  the repo's "a guard that is not on the path is not a guard", one level up — that
  guard *was* on the path.
- **Tests protect the computation; nothing protects the paraphrase.** The
  registry's status field grades how a claim was *established* and says nothing
  about whether its *statement* still means what the computation showed. One
  session produced four variants, and **every one survived a green suite, because
  the tests were testing the correct object while the prose described a different
  one**:
  - *convention distance* — a symbol declared correctly 448 lines from its use
    (Note O's r_k), and DFI's determinant vs discriminant 200 lines apart;
  - *paraphrase drift* — a section heading outliving its own corrected body, and
    a correction reaching a claim's `notes` while its `statement` kept the old
    wording;
  - *an unattached axis* — "no log-power correction" and a measured (log M)^{1/4}
    reading as contradictory until each carried its axis and its grouping;
  - *a hypothesis dropped from a statement while remaining in its proof* — Note O's
    Prop O.1 stated without the window, with a counterexample inside the same note
    ((1,5) at m = 2, where a g² = 4 = M exactly, so the *strict* inequality the
    proof turns on fails by nothing at all);
  - *a correct result cited across a scope boundary the citing note never mentions*
    — Note F's **Z[i]** lemma equated to ν = 0 in [FM]'s **rational** axioms, in
    Notes G, J and M, none of which named the transfer. Nothing in those sentences
    is false; the error is entirely in which object a reader takes them to be
    about. The transfer is `gaussian-to-rational-bridge`, `inferred`.
  - *a silent no-op edit* — a scripted `replace` whose anchor had changed wrote
    back identical content and printed success; `git commit` then said "nothing
    to commit", which was misread as a collision with the parallel session
    because that had genuinely happened twice the same night. **Every string edit
    must assert its anchor**, and a *plausible* explanation for an anomaly is
    what stops you checking the implausible one.
  - *a claim stated to an order, read as an equality* — a distinct failure, and
    the hardest, because **both halves are true**. `sqrt-MX-law`'s one sentence
    contains two: "saturating at ~|A| for M ≥ X" is right about the order and
    wrong by **4×** literally (the ceiling is DIAG ≈ 0.253·X, since above the
    boundary each modulus carries one x and |Σ| counts squarefree incidences);
    and "the saving is exactly zero at θ = 1/2" is right about the *exponent*,
    Q^{(1/2−θ)/2} = Q⁰, and wrong by **2.41** read as S = T. Neither is a false
    statement and neither would fail any guard. **Write the constant, or write
    "to within a constant" — never a bare ≍ that a reader will use numerically.**
    A third instance sat in a `proved` claim: `type-I-level` gave Σ_{N(d)≤D}|r_d|
    ≍ D while `admissible-density` gave (3/2π)·D admissible ideals — **the two
    could not both carry constant 1**, and neither noticed. The constant is
    forced and exact: r_d is triangular on (−1,1), so E|r_d| = 1/3 and the sum is
    **D/(2π) = 0.159155·D** (measured 0.15895 at D = 5×10⁵, 0.13%).
    **These are errors that *sit*, not errors that propagate.** A false conclusion
    is caught by the next thing that uses it; a wrong constant inside a true
    order-statement is used by nothing, so nothing objects — which is why all
    three survived a green suite, two prose sweeps *and* a citation audit. The
    conclusions were untouched in all three, at 2.4×, 4× and 6.3× off.
    **Checkable form: wherever a note states an order for a quantity some
    experiment computes, put the computed constant in.**
  - *a count of chances mistaken for a count of **informative** chances* — three
    times in one night, and the informative subset is **never** the one a loop
    naturally counts. `triples-cannot-be-settled-by-measurement` says an absence
    over a vacuous population is not evidence; the trap is that the population
    looks populated. O.2's class count was 31 informative of **278 939** above
    threshold; exp17's solution count was **9** informative of **2 093** carrying
    an in-window multiplier, because a solution whose (a,b) has only one such
    multiplier has nothing to pair with. Both were quoted at the inflated figure,
    the second by the session that had just written the first correction into the
    README. **Before quoting N, ask what the N−k silent ones were silent about.**
  - *a statement about **proofs** read as a statement about the **object*** — a
    new pair of registers, and it had Note G's Step 2 checkpoint (a plan
    deliverable) asserting the opposite of the truth. "The trivial bound has
    never been beaten by any amount" is true of the *literature*; the checkpoint
    then said a reader "would conclude it is **untouched**". Measured,
    |Σ_{x≤X} μ(x²+1)|/√X sits between 0.21 and 1.34 over two decades, |S|/X down
    to 1.7×10⁻⁴ — **square-root cancellation, unmistakably.** The estimate at
    θ = 0 is *visibly true and unprovable by current methods*, a different
    position entirely from a sequence that misbehaves. Nobody had measured a sum
    everyone assumed was hopeless. **Say "no proof is known", never "it is not
    known to hold" — and measure before writing either.** (Nothing is fitted;
    `chowla-for-x2plus1-is-open` is untouched.)
  Nothing checks a proposition's statement against its own proof, because the
  **And watch the trajectory, not just the instances.** Three laws were fitted to
  one decay in one night, and the *disconfirming evidence got closer to hand each
  time*: with 1/N there was only one X and nothing to contradict it; with
  (log X)/N a drift was noticed, written down at 5.6, and the law quoted anyway;
  with N/X the counterexample sat **two rows apart in the same printed table**.
  Availability of the refutation went up while use of it went down — which is the
  opposite of what learning looks like, and is what confidence in a framework
  does when it outruns the evidence for it. If a third instance of one error
  class is easier to catch than the first and was still missed, the problem is
  not attention; it is that the framework has started supplying the answer before
  the data does.

  tests test the proof. The one checkable habit: **a correction that reaches only
  a claim's `notes` has not landed** — notes are where history goes, the statement
  is what gets quoted. `test_retracted_wording_is_not_still_in_the_statement`
  enforces the mechanical half (a note quoting the wording it retracts must not
  leave that wording in the statement); the paraphrased half stays discipline.

## The claim registry — read before writing a finding

`research_state/claims.json` records every established claim with an **enforced
epistemic status**, checked by `tests/test_claims.py`. The pattern is adapted
from the sibling repo `rh-research-engine` (`core/models.py`, `core/nogo.py`,
`docs/EPISTEMIC_BOUNDARIES.md`), whose governing rule applies here too:

> A guard that is not on the path is not a guard.

**And a corollary this repo earned the hard way:** *a guard is not verified until
it has failed on an injected violation.* A claim-id guard written specifically to
catch vacuous passes was itself passing vacuously — its identifier pattern
silently skipped 26 of 103 ids, including `sqrt-MX-law` and the very `refuted`
claim used to test it. It did not fail to catch a violation; it failed to see the
input, and reported green. Inject a known-bad case before trusting any guard.

**The status vocabulary does not protect the statement.** Five times in one day a
quantity was computed correctly and *described* in a way that silently changed
what it was — r_k as modulus-ratio vs X-ratio, DFI's "determinant" ac − b² vs the
discriminant, S_μ grouped per modulus vs per progression, a signed OFF read as
monotone, a tolerance quoted without its X. Every one was caught by
**recomputing**, never by rereading, and three sat next to a correct machine
check whose docstring carried the qualifier the prose had dropped. Tests protect
the computation. Nothing protects the paraphrase, and the paraphrase is what gets
written into `claims.json` and quoted. Write the convention where the symbol is
defined.

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

The suite covers `x2plus1/` and not the experiments, so after changing a library
module run

```bash
python tools/smoke_experiments.py
```

which executes all twelve at reduced sizes in about 20 seconds. Green means
"still runs", not "reproduces the recorded numbers". And
`python tools/check_sources.py` flags which source PDFs are scans whose text
layer must not be quoted.

## Scope discipline

The plan rules these out; they stay ruled out unless the plan is amended:

- Green–Tao / nilsequence methods (single-variable polynomials are out of scope).
- GRH or zero-density substitutes for Type II (they control primes in
  progressions, not in a sparse sequence).
