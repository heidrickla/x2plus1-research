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
theorem about the sequence and survives any change of sieve.

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

**Theorem O.3 is the real result there.** A multiplier with |V| = 2k exists iff
a² + (4k²−2)ab + b² is a perfect square — at k = 1 that is (a+b)², a square
*identically*, which is why the trivial multiplier always exists and why |V| = 2
dominates. A triple needs a **second** multiplier, since V = ±2 forces
U = ±(a+b) uniquely. Mod M we have b ≡ a, so in S = X+Y, T = X−Y the automorph
diagonalises with **unit** eigenvalues — hence each integrality condition holds
for a whole orbit or none. τ₁ acting is exactly M | S; then τ_k forces
M | 2B_k with B_k = U_k − 2ka, so M = 8ka(2k−j)/(j²−4) for j = 2B_k/M ≥ 3, and
the geometry needs M > 2√2·k√(ab). Together those give
e² + 4jwe + 2w²(2e−1) < 0 with every term positive. **So for M odd squarefree no
window holds (ξ, τ₁ξ, τ_kξ)** — and **Theorem O.3′ supersedes that**: with
ρ = B_k/M the identity M(ρ²−1) = 4ka(k−ρ) plus the geometry force ρ < 1.06066,
while integrality makes c·ρ an integer for c = gcd(M, 2X); an integer in
(c, 1.06066c) needs c ≥ 17. **So the conclusion holds whenever gcd(M, 2X) ≤ 16,
with no hypothesis on M at all** — reaching the even, non-squarefree cases O.3
was mute on. **And O.3″ sharpens O.3′ into a joint (c,k) region**: the
chain discards a term at ρ² < 9/8 − ρ/(8k), and ρ > 1 is free (U_k > 2k√(ab) >
2ka; Λ > 0 with ρ² < 1 forces ρ > k ≥ 1). Keeping it, with g = cρ ∈ ℤ the
identity reads M(g−c)(g+c) = 4kac(kc−g) and a triple needs
**(4k+√(16k²+2))(2c+1) < c(kc−c−1)**. k → ∞ gives back c ≥ 17, so **O.3′ is the
k-free shadow of O.3″**, while **k = 2 is excluded for every c ≤ 33**. k = 1 is
the boundary that hid it — U₁ = a+b, ρ = 1 exactly, Λ = 0/0. Reading "cρ ∈ ℤ
needs 1/(ρ−1)" off the ρ bound gives 33 not 34 at k = 2; **that route spends
ρ > 1 on the −ρ term while the region form substitutes ρ ≥ (c+1)/c in both**, so
the region form is the parent and the ρ bound its weaker corollary. O.3″ leaves
O.2's p,q ≥ 2 gap untouched and is far from binding: every realised acting
in-window multiplier with k ≥ 2 has c ∈ {2,4} against a threshold of 17.

**Theorem O.4 is the first that assumes nothing about which multiplier acts**, so
it is the one reaching the p,q ≥ 2 gap. Three moduli are two steps, so the window
must fit τ_min²; the automorph X_j = (UX_i + VaY_i)/M with aY_i > X_i√D gives the
**exact** X_j > τ_V X_i, and m = (X²+1)/a turns it into
m₃/m₁ > (τ_min⁴X₁²+1)/(X₁²+1). **A window holds three only if τ_min⁴ < 2 + 1/X₁²**
— b/a > 53.69 at X₁ = 1, rising to **b/a > [(1+√2)(1+√2+2^{5/4})]² = 133.875**,
against the pair threshold (1+√2)⁴ = 33.971. **The finite term is load-bearing**:
the clean form m_{i+2}/m_i ≥ τ₁⁴ is FALSE (9 of 110 gaps; at (1,5), m = 2 → 65
gives 32.50 against 46.98) because the modulus ratio is τ² only asymptotically.
**Step 2 must go through the map** — bounding
|V| = M(X_j²−X_i²)/(X_jY_i + X_iY_j) instead gives τ at V/a, true but not sharp
for a > 1. Still only necessary, and not binding: the nearest realised
configuration clearing the threshold is a factor 7.25 from a window.

**Conjecture O.2 moved three of its four cases tonight.** τ₁-assuming triples go
to **O.3″**; the equal-multiplier case (ξ, τ_pξ, τ_p²ξ) goes to **O.5** — τ_p² ∈ T
forces M | 8p², and the window forces D < M against M < D always; the general
threshold is **O.4**. What is left is **two distinct multipliers** — and
**Proposition O.6 proves that case is unreachable by congruences.** For M an odd
prime exactly one of M | S, M | T holds and it forces the sign of U_p ≡ ±2pa; the
exact identity **M·S′ = A_pS + V_p·M·X** (*not* S′ = A_pS/M, which fails on 246 of
246 pairs — the first version of the argument was built on it) together with
β ≡ p (mod M) makes **the subcase alternate at every step**, 246 times with 0
exceptions. So ε_p = +1 forces ε_q = −1, and both composite integrality
conditions become **automatic**: 0 failures over 493 opposite-sign (p,q) pairs,
against **40 of 246 same-sign pairs failing both** — the conditions have content
and the alternation is what removes it. so the composite's integrality
conditions carry no information.

**But the alternation is a CONSISTENCY constraint, and Theorem O.7 closes the
case with it.** A triple makes ξ₁ → ξ₂ → ξ₃ flip **twice** (ξ₃ back in subcase A)
while ξ₁ → ξ₃ is itself a single step and flips **once** (ξ₃ in B) — and the
dichotomy says exactly one. **So for M = b−a an odd prime, no dyadic window holds
three shared moduli: Conjecture O.2 on 14% of realised close pairs, assuming
nothing about which multipliers act.** Its only hypothesis is M ∤ V, supplied by
the window through the exact **a·|V|(X_jY_i + X_iY_j) = M(X_j²−X_i²)** — *the
factor a is load-bearing, and dropping it fails 3389 of 4033 pairs* — giving
|V| < 0.57735·M/√D < M. The hypothesis is sharp: every realised M-odd-prime class
with three moduli has M | V on its two-step, at ratios of 10⁴ and up. **M
composite remains open**, for the same reason O.3 had a 2-adic gap.

**I first wrote O.6 up as "the integrality route cannot close O.2" and that was
too strong** — the evidence showed only that those two *composite* conditions are
vacuous. Generalising "sub-route X′ is dead" to "route X is dead" is this repo's
most repeated error, and here the very proposition I declared insufficient is
what closes the case an hour later. **The geometry there is r_k² < 2, equivalently M > 4√2·k√(ab), and
the distinction decides the theorem**: the modulus ratio is τ², not τ, so r_k² < 2
is what "both fit one dyadic window" means. Under the weaker r_k < 2 (which is
M > (8/3)·k√(ab)) the ρ bound is **false** — 193 violations in 277, ρ reaching
1.2375. Verified with the identity exact in rationals over 1455 multipliers; the
correct hypothesis leaves 73 of them, so O.3′ reaches less than the loose form
suggests. Machine-checked in `tests/test_arithmetic_facts.py`. A corollary for
any surviving text: a window holding three needs **r₁·r_k < √2**, not < 2.

**O.2 — no window holds three, at all — is still open**, and the gap is p, q ≥ 2:
a close pair can be realised at a **non-fundamental** multiplier. `exp14` finds
**four** at X = 9000 (1332 of 1336 explained close pairs sit at k = 1):
(17, 593393) k=20; (53, 423125) k=12; (37, 26245) k=4; (37, 1635517) k=35.
**All four have M even, so O.3 is mute on all four, and O.3′ permits both moduli
and forbids a third in all four** — c = gcd(M,2X) is 2, 4 or 12 throughout.
Rare, not absent, and they are the falsifiers any extension must survive.

**The sharp form of O.2, and the identity behind the 17.** Asking which
multipliers *act* on a realised ξ (occupancy as input) shows they act freely —
18,116 solutions admit one, 215 admit two, some six, and the acting set can be a
cyclic semigroup: (1,5) at m = 2 admits k = 1, 3, 8, 21, 55, 144, i.e. τ₁, τ₁²,
τ₁³. **So "τ² is never integral" is false in general**; O.3′ forbids it only in
the window regime. But **never two inside a window**: 13,840 ξ with an acting
multiplier, 327 with exactly one at r < 2, **zero with two**, and the smallest
second ratio over 53 cases is 14.91 against the 2 a window needs. That is O.2 in
measurable form — *on any ξ, at most one acting multiplier has r < 2* — and
acting is orbit-invariant because the automorph diagonalises S = X+Y, T = X−Y
with **unit** eigenvalues mod M. Behind it: with B_p = M + δ_p,
**δ_p(2M + δ_p + 4pa) = 4paM(p−1)** exactly (0 violations in 1,002,709), so
δ_p = 0 **iff** p = 1 — the same fact as j = 2 ⟺ k = 1 and M₂ = 1 — and
δ_p < 2ap(p−1); with δ_p < 0.06066M from the geometry, gcd(δ_p,M) ≤ δ_p gives
M/d_p ≥ 17, recovering O.3′'s constant by a second route.

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

Read [README.md](README.md) and [notes/README.md](notes/README.md) first. Run
`python -m pytest -q` before trusting any measurement.

## Non-negotiables

- **Normalisation.** Q (or N) = norm bound; X = √Q = range of x; |A| = X.
  State which one every exponent is relative to. "Level N^{1/2}" = "level X".
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
- **The informative subset is never the one the loop naturally counts.** An
  absence is evidence only in proportion to the configurations that *could* have
  contradicted it, and the natural loop counts everything it visited. Three times
  in one session: 278 939 ratio classes above threshold of which **31** could
  hold a triple; 379 "candidates where a triple could occur" of which most were
  unoccupied; 2 093 solutions carrying one in-window multiplier of which **9**
  had a second to pair with. Each time the loop was correct and its total was
  the wrong number, and the third happened *after* the rule was written into the
  README by the session that then broke it. Report the informative count, and
  refuse to conclude when it is zero.
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
  produces the feeling of having checked. Verified from `git show`, not from the report — the other
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
