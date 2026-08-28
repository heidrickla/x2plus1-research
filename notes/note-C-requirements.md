# Note C — Requirements table

*Plan §1.3.3, the Step 1 checkpoint. Status: **filled and answered.***

Sources, both read directly (PDFs in `refs/pdf/`, gitignored — copyright):

- **[ASP]** Friedlander & Iwaniec, "Asymptotic sieve for primes", *Ann. of
  Math.* **148** (1998), 1041–1065. [arXiv:math/9811186](https://arxiv.org/abs/math/9811186).
- **[X2Y4]** Friedlander & Iwaniec, "The polynomial X² + Y⁴ captures its
  primes", *Ann. of Math.* **148** (1998), 945–1040.
  [arXiv:math/9811185](https://arxiv.org/abs/math/9811185).
- **[HB]** Heath-Brown, "Primes represented by x³ + 2y³", *Acta Math.* **186**
  (2001), 1–84. Read from the
  [Oxford ORA copy](https://ora.ox.ac.uk/objects/uuid:ebb25eb4-a19e-4049-8117-3269e140b0fe);
  page numbers below are that preprint's.

Page references are to the Annals pagination printed in the arXiv preprints.

---

## The answer, first

> **The asymptotic sieve for primes, as stated, cannot be applied to x² + 1.
> The hypothesis that fails is the Type I one, (R1).**
>
> [ASP] requires a level of distribution **D > x^{2/3}** — hypothesis (R1),
> p. 1043. [Note B](note-B-type-I.md) proves that for this sequence
> Σ_{d≤D}|r_d| ≍ D, so (R) forces D ≤ A(x) = x^{1/2}. Since
> x^{1/2} < x^{2/3}, **the admissible range for D is empty.**
>
> **(R1) is not a separate hypothesis from the bilinear one.** [ASP] p. 1045
> shows x^{2/3} is exactly the threshold below which the coefficient γ(n,C) in
> (B) is annihilated, so within [ASP] the two hypotheses are one.
>
> **But x^{2/3} is [ASP]'s threshold, not prime detection's.** A level-1/2
> prime-detecting sieve exists — Duke–Friedlander–Iwaniec, used by
> Green–Sawhney — and x² + 1 *meets* its Type I hypothesis while failing its
> Type II one outright. So the obstruction is Type II, and
> [Note F](note-F-failure-localisation.md)'s C₄-free lemma is the whole of it.
> See [§ The x^{2/3} is ASP's threshold](#the-x23-is-asps-threshold-not-prime-detections).

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
| x³ + 2y³ | x^{2/3} | at the boundary | **x^{2/3−ε}** ([HB] Lem. 2.1–2.2, p. 5) |
| x² + 1 | **x^{1/2}** | **below** | ≤ x^{1/2}, and no D is admissible |

x³ + 2y³ sits exactly on the boundary and misses (R1) by ε; x² + 1 misses by
x^{1/6}. See [§ Consequences](#consequences-for-the-plan) below.

---

## Heath-Brown's precedent

(R1) is genuinely unsatisfiable for x² + 1. [HB] shows that (R1) failing is not
*by itself* fatal — it has happened before and was worked around. The section
after this one bounds how far that precedent reaches.

### Heath-Brown uses the same density exponent

[HB] p. 2 defines α(f) as the infimum of α with
#{(x₁,…,xₙ) ∈ ℕⁿ : |f|(x₁,…,xₙ) ≤ X} ≪ X^α, and remarks:

> "Thus the smaller the value of α, the harder it will be to prove that f
> represents primes. The two classical theorems of Dirichlet both correspond to
> α = 1. … Before the present work there was only one theorem proved in which
> α < 1, namely the result of Friedlander and Iwaniec that there are infinitely
> many primes of the form x² + y⁴, for which α = 3/4. Our theorem corresponds
> to the still smaller value α = 2/3, **while the conjecture that x² + 1 takes
> infinitely many prime values has α = 1/2.**"

So the 1 / ¾ / ⅔ / ½ hierarchy this repo has been using is the literature's own
frame, and x² + 1 is named in it. α(f) is A(x)'s exponent — the same quantity.

### He did not use the asymptotic sieve, and said why

[HB] p. 3:

> "We should mention at the outset that our approach to the sieve procedure has
> much in common with that given by Friedlander and Iwaniec [3]. … **Unfortunately
> their condition (R1) is not quite met in our case, so that their work cannot be
> used as it stands. Although it seems possible that Friedlander and Iwaniec's
> hypothesis (R1) might be relaxed sufficiently for our application, we have
> chosen instead to present our own version of the sieve argument.** In the light
> of these remarks, it should be stressed that it is the 'Type II' bound … which
> is the most novel part of our proof, and not the sieve procedure."

Two things follow.

1. **The mechanism this note identified is confirmed from outside.** [HB]
   Lemmas 2.1–2.2 give A the level of distribution **X^{2−ε}** (p. 5) for a
   sequence whose values are ≍ X³. In the sieve's variable that is
   D = x^{2/3−ε}, against (R1)'s requirement D > x^{2/3}. **Missed by ε** —
   exactly "not quite met", and exactly the D ≤ A(x) ceiling biting at α = 2/3
   where A(x) = x^{2/3}. Note C's prediction that x³+2y³ sits "at the boundary"
   was right, and the [VERIFY] on it is discharged.
2. **(R1) is a soft barrier.** A leading practitioner, facing it, judged it
   probably relaxable and routed around it in a page. It is a feature of FI's
   particular formulation, not a law.

### But x² + 1 misses by a power, not an epsilon

| sequence | α | A(x) | level achieved | (R1) needs D > x^{2/3} | shortfall |
|---|---|---|---|---|---|
| a² + b⁴ | 3/4 | x^{3/4} | x^{3/4−5ε} | ✅ met | — |
| x³ + 2y³ | 2/3 | x^{2/3} | x^{2/3−ε} | ❌ "not quite met" | **x^ε** |
| x² + 1 | **1/2** | x^{1/2} | x^{1/2}(log x)^{−222} | ❌ | **x^{1/6}** |

Heath-Brown's workaround closed a gap of ε. For x² + 1 the gap is a sixth of an
exponent. Nothing in [HB] suggests a bespoke sieve could absorb that, and his
own remark is scoped to "our application".

### How far the precedent reaches

Heath-Brown stresses that the Type II bound, not the sieve procedure, is "the
most novel part" of his proof — so the difficulty at α = 2/3 was bilinear, and
the sieve was bookkeeping he preferred to redo himself. That is a real
precedent for replacing (R1). The next section bounds it: his gap was ε, and
the quantity (R1) protects degrades by a *power* at α = 1/2.

### What is available at α = 1/2

Iwaniec, *Invent. Math.* **47** (1978), 171–188, remains the record: for
irreducible g(n) = an² + bn + c with a > 0 and c odd (so x² + 1 qualifies),
g(n) = P₂ infinitely often, with |{n ≤ x : g(n) = P₂}| ≫ Γ_g x/log x. That is a
**lower-bound weighted sieve** (Richert's weighted sum), not an asymptotic —
i.e. exactly the parity-limited conclusion. The gap between that and the
theorem is precisely the parity barrier, and ASP is the only machine built to
cross it. *(Read via an exposition, not the original — see
[refs/bibliography.md](../refs/bibliography.md).)*

---

## Where the x^{2/3} is spent — answered

*This was the note's live question. It is answered on [ASP] p. 1045, in the
discussion of (B), not anywhere in §§3–8.*

The literal string x^{2/3} occurs three times in [ASP]: the statement of (R1)
(p. 1043), Theorem 2's hypothesis list (p. 1059), and one estimate in §9
(p. 1062, bounding E21 — and there it is paired with (9.2), so it belongs to
the non-squarefree machinery). **In the main proof of Theorem 1, §§3–8, (R1) is
never invoked.** That looked at first like evidence the exponent is an
artefact. It is not. FI explain it directly:

> "There is also the Möbius function μ(d) in the coefficient γ(n, C). Here d
> must be quite a bit smaller than N to ensure that **μ(d) does not completely
> neutralize μ(n)**. By (B1–B3) we know that d < C < (x/Δ)·N·D^{−3/2}, so **our
> hypothesis (B) can be realistic only if D is somewhat larger than
> x^{2/3+ε}**." — [ASP] p. 1045

So (R1) is not a technical constraint sitting beside (B). **It is the condition
under which (B) is not vacuous.** The mechanism:

- (B3) sets the divisor truncation at C = xD^{−1}; (B1) puts n in a range with
  N ≳ √D.
- γ(n, C) = Σ_{d|n, d≤C} μ(d). If C exceeds n, this is Σ_{d|n} μ(d) = **0** for
  every n > 1.
- So C ≲ N is needed for the coefficient to be anything at all, and
  xD^{−1} ≲ √D ⟺ **D ≳ x^{2/3}**.

FI are explicit on the same page that this is where parity-breaking lives:

> "our stipulation of the lower bound restriction N > Δ^{−1}√D in (B1) is
> essential; indeed by narrowing this slightly to N > √D we would not be able
> to break the parity problem. … the source of cancellation in the bilinear
> form in (B) comes from the sign changes of the Möbius function μ(mn)."

### What that does to the "Type I or Type II?" question

**It dissolves it.** (R1) and (B) are not two independent hypotheses to be
failed separately — (R1) is the statement that (B) has content. Asking which
half obstructs x² + 1 was malformed. The single fact is that at A(x) = x^{1/2}
there is no room for ASP's parity-breaking mechanism, and it shows up three
ways:

| symptom | where |
|---|---|
| (R1) unsatisfiable: D ≤ A(x) = x^{1/2} < x^{2/3} | [Note B](note-B-type-I.md) |
| (B) vacuous: C = xD^{−1} = x^{1/2} against N ≈ x^{1/4}, so C/N ≈ x^{1/4} and γ(n,C) ≡ 0 | this note |
| incidence matrix is a forest: κ = 1 | [Note F](note-F-failure-localisation.md) |

Note that C ≲ √D together with D ≤ A(x) gives x/A(x) ≲ √A(x), i.e.
**A(x) ≳ x^{2/3}** — the sieve's density threshold, re-derived from the
mechanism rather than read off (9.2).

### And it re-scopes Heath-Brown's remark

At D = x^{2/3−ε}: C = x^{1/3+ε} against √D = x^{1/3−ε/2}, so C/√D = x^{1.5ε}.
The neutralisation is *marginal* — which is exactly the situation in which "it
seems possible that (R1) might be relaxed sufficiently for our application"
([HB] p. 3) is a reasonable thing to write. At D = x^{1/2}, C/N ≈ x^{1/4}: the
coefficient does not weaken, it vanishes.

**So the previous revision of this note over-corrected.** "(R1) is soft" is true
by an ε and false by a power. The accurate statement:

> (R1)'s x^{2/3} encodes the condition for ASP's parity-breaking to exist at
> all. It is negotiable at the margin — Heath-Brown negotiated it — and it is
> not negotiable by a sixth of an exponent.

This does not resurrect the claim that Step 2 is the wrong half. It says the
halves are the same half. [Note F](note-F-failure-localisation.md)'s C₄-free
lemma remains the sharpest *sequence-intrinsic* statement of the obstruction,
and it is the one that survives changing sieve.

## The x^{2/3} is ASP's threshold, not prime detection's

*Established by verifying the Open items below. This is the most consequential
correction in the note, and it finally settles the "which half" question.*

**A prime-detecting sieve that runs at Type I level x^{1/2} exists, and it is in
current use.** Green–Sawhney do not use [ASP]; they use the
**Duke–Friedlander–Iwaniec** sieve (*Ann. of Math.* **141** (1995), §6),
transplanted to ideals of O_K. Their Lemma 3.2 (p. 9) needs

- **Type I at X^{1/2}(log X)^{−C}** — note: not x^{2/3}; and
- **Type II with arbitrary 1-bounded α_a, β_b for N(b) ∈ [(log X)^C, X^{3/8}]**.

They call their own Type I range "just barely enough" and record that
"obtaining Type I information at level X^{1/2} in our setting remains an
interesting open question" (p. 4).

### What that does to x² + 1

| DFI hypothesis | x² + 1 | why |
|---|---|---|
| Type I at X^{1/2}(log X)^{−C} | ✅ **met** | [Note B](note-B-type-I.md) gives Σ_{d≤D}\|r_d\| ≍ D, so at D = X(log X)^{−C} the error is A(x)(log X)^{−C} |
| Type II, **arbitrary** 1-bounded coefficients | ❌ **fails outright** | [Note F](note-F-failure-localisation.md): the incidence graph is C₄-free, so the worst case has no cancellation at any split |

Measured across DFI's stated range at X = 2×10⁴ (X^{3/8} ≈ 1682):

| N(m) | T | worst-case \|S\| | θ | (θ if β = μ) |
|---:|---:|---:|---:|---:|
| [10, 10²) | 24 691 | 24 671 | **1.000** | 0.627 |
| [10², 10³) | 22 011 | 21 843 | **0.999** | 0.775 |
| [10³, 1682) | 7 319 | 7 249 | **0.999** | 0.825 |

The last column is the point. With β = μ there *is* cancellation. It is
specifically the **arbitrary-coefficient** requirement that fails — which is
exactly what C₄-freeness predicts, and it is a theorem about the sequence, not
a hypothesis of a sieve.

> **So the obstruction for x² + 1 is Type II, unambiguously.** Changing from
> ASP to a level-1/2 sieve removes the x^{2/3} artefact entirely and leaves
> Note F's lemma standing alone as the blocker. Everything earlier in this note
> about (R1) remains true *of [ASP]*, and is no longer the operative constraint.

### DFI read directly — four corrections to the above

*The paper is paywalled at the Annals, but Duke posts a scan himself at
[math.ucla.edu/~wdduke/preprints/equidistribution.pdf](https://www.math.ucla.edu/~wdduke/preprints/equidistribution.pdf)
(byte-identical copy independently re-fetched by a second reader). The
table above was built from a report of Green–Sawhney's Lemma 3.2 quoting DFI,
and three of its four entries turn out to describe **Green–Sawhney's
strengthening, not DFI**.*

1. **§6 is not a sieve.** It is titled *Combinatorial identities* — a Buchstab/
   Legendre identity whose outputs are Lemma 3 and **Theorem S** (p. 437).
2. **DFI's Type II coefficients are *not* arbitrary.** The class is stated
   exactly at p. 437: "|α_m| ≤ ω(m), |β_n| ≤ 1, |λ_d| ≤ 1 … and, in our case,
   **β_n will be supported on primes**", and Proposition 2 (p. 426) is proved
   only under that restriction, with the remark that "the restriction to n₁, n₂
   primes simplifies much of the argument, yet it is just this type that is
   needed for our application." Green–Sawhney **drop** it and demand "any
   1-bounded sequences α_a, β_b" — so the arbitrary-coefficient hypothesis this
   note attributed to DFI is Green–Sawhney's.
3. **DFI's own Type I level is x^{1/2−ε}**, not X^{1/2}(log X)^{−C}; and
   Theorem S concludes only **Σ_{p≤x} c_p ≪ ε·π(x)** — o(π(x)), not a log-power
   saving. Green–Sawhney strengthen every axis.
4. **DFI's sequence is not thin: α = 1.** Applied verbatim to A = {x+i}, whose
   mass is X^{1/2} inside norm bound X, Theorem S and Green–Sawhney's Lemma 3.2
   are **vacuous** — the hypotheses hold trivially and the conclusion is weaker
   than the trivial bound.

### But DFI's engine is scale-free, and that is the constructive part

Theorem S is normalised to x. **Lemma 2 (p. 436) is not.** It assumes only

> (27) Σ_{n ≡ 0 (d)} |c_n| ≤ γ(d)·X with γ submultiplicative, and (29) γ(p) ≤ c/p,

which A = {x+i} satisfies with γ(d) = ρ(d)/d and X ≍ x^{1/2} — exactly [Note
A](note-A-dictionary.md)'s local densities. So the machinery **does** apply to a
thin sequence; what changes is that the Type I and Type II hypotheses must then
be re-normalised to X = |A|, demanding cancellation of size |A|(log)^{−B} rather
than x(log)^{−B}.

> **It is at that re-normalised level that [Note F](note-F-failure-localisation.md)'s
> C₄-free obstruction bites.** Neither DFI nor Green–Sawhney ever writes the
> thin-sequence version down, so this is the first place the repo's obstruction
> and the literature's machinery are stated in the same normalisation.

### The equidistribution theorem is about this repo's residues

DFI's actual theorem (p. 424) is for f(X) = aX² + 2bX + c with D = ac − b² > 0.
**Taking a = 1, b = 0, c = 1 gives D = 1, so ν² + 1 ≡ 0 (mod p) is literally the
case covered**, and their ρ_h(n) = Σ_{f(ν)≡0 (n)} e(hν/n) is exactly the Weyl
sum over this repo's residues r_d. Two directly reusable inputs:

- **Proposition 1** (p. 425): L_d(M) = Σ_{M<m≤2M} ρ_h(dm) ≪
  (h,d)^{1/20}(d/M)^{1/20}M^{1+ε} — a nontrivial bound on r_d **in arithmetic
  progressions**, uniform in d up to d ≍ M.
- **Proposition 2** (p. 426): a genuine Type II bound with M^{3/8}, for β
  supported on primes.

Proposition 1 is the more interesting of the two here, because [Note
J](note-J-mobius-in-progressions.md) reduces the Type II input to a statement
about exactly these residues in progressions. **[VERIFY]** whether Proposition 1
transfers, and at what level.

### How far below 2/3 the literature actually reaches

Two sieves break parity below x^{2/3}, and neither reaches x^{1/2}:

- **Xiannan Li** — unconditional, exponential density 2/3 − γ/3 for γ < 5/67,
  i.e. down to ≈ x^{0.6418}. Li states outright that both [ASP] and Harman's
  sieve "fail to prove asymptotic estimates for sequences with exponential
  density strictly lower than 2/3".
- **Merikoski** — conditional on exceptional characters, exponent of
  distribution 5/8, with a general floor of 0.61634….

And **Ford–Maynard** (arXiv:2407.14368) map the parameter space directly. Their
Theorem 4.16: C⁻(γ, θ, ν) = 0 whenever γ < 1/2 and γ ∉ [θ, θ+ν]. Their
Theorem 2.4 is the one that bites here, because **x² + 1 sits at γ = 1/2
exactly**: with ε losses, C⁻(P_ε) = 0, and they comment that "one cannot hope to
obtain non-trivial lower bounds on primes without some additional assumptions".
The escape they name is divisor-bounded weights — which is precisely the
Duke–Friedlander–Iwaniec setting. Maynard's ICM survey states that all current
approaches break down below x^{1/2} and asks (Question 21) whether adapting
them is even plausible.

### Ford–Maynard read directly — and it is worse than the knife-edge

*Read in full (arXiv:2407.14368v1, 107 pp.), then adversarially re-extracted
page by page by a second reader who verified every quotation and overturned the
first reading's conclusion. Three corrections, and they all cut against the
repo.*

**1. x² + 1 is not at γ = 1/2. It is at γ = 1/2 − ε, which is the killed
regime.** Ford–Maynard's (I) demands a log-power saving at level *exactly* x^γ.
[Note B](note-B-type-I.md) gives Σ_{d≤D}|r_d| ≍ D against A(x) = x^{1/2}, so
Type I holds for D = o(x^{1/2}) and **fails at x^{1/2}**. In their convention
that is γ = 1/2 − ε for every ε and never γ = 1/2 — i.e. exactly P_ε, exactly
what Theorem 2.4 and Theorem 4.16 kill. The consolation that "at γ = 1/2 exactly
they assert C^{±} = 1" is void, because γ = 1/2 exactly is the one case this
sequence does not have.

**2. The binding result is not Theorem 2.4 at all — it is Selberg.** By [Note
F](note-F-failure-localisation.md) the sequence has **no arbitrary-coefficient
Type II range**, i.e. ν = 0 in their sense. Ford–Maynard, p. 2:

> "Selberg [28] showed that whenever ν = 0, there are examples of a_n with
> b_n = 1 for all n which satisfy (I) for arbitrary γ < 1 but with Σ_p a_p = 0,
> so non-trivial Type II information is necessary to detect primes."

Their Theorem 2.1 is the quantitative version. So the Type I/II framework
returns C⁻ = 0 for this repo's parameters by the **oldest result in the paper**,
with no ε-loss and no A*₂ membership question. Theorem 2.4 is a refinement of a
conclusion already reached.

**3. The divisor-bounded escape is unavailable, and by a shorter route than the
density argument.** Theorem 2.7(c), p. 8: C⁻(1/2, 0, ν) = 0 = C⁻_bd(1/2, 0, ν)
at ν = 0.1616, and C⁻_bd(1/2, 0, 3/19) = 0. **Divisor-boundedness buys nothing
once ν is small, whatever the density.** The [VERIFY] this note carried — is
x²+1's indicator weight divisor-bounded, and does that exempt it? — is answered:
it is, and it does not.

### What survives, stated narrowly

C⁻ = 0 is a statement about **what these axioms can prove**, not about x² + 1.
It means there exists an admissible sequence with no primes; it says nothing
about whether x² + 1 is prime infinitely often. Do not conflate the two.

The one direction Ford–Maynard leave open is arithmetic information **not
expressible as (I)/(II) with arbitrary coefficients** (p. 18):

> "It would be naturally be desirable to have a theory which can incorporate
> such additional arithmetic information, or to generate new means to
> distinguish sets which contain primes from the examples produced here which do
> not."

The repo's β = μ cancellation ([Note J](note-J-mobius-in-progressions.md)) is a
candidate — **but only in one precise form**. A μ-restricted Type II is *weaker*
than the arbitrary-coefficient one at the same range, so every Ford–Maynard
counterexample satisfies it a fortiori; restricting coefficients cannot per se
be an escape. It is new information **only because it holds on ranges where the
arbitrary-coefficient hypothesis fails outright** — which, by Note F, is every
range. That is the narrow statement, and it is the only one the sources support.

Against it, Ford–Maynard's own expectation (footnote 1, p. 3):

> "A mild generalization of the underlying methods should allow one to establish
> (I) and (II) in full."

i.e. they expect specialised-coefficient results to upgrade to full ones, which
would collapse the distinction the repo is relying on. Here it demonstrably does
not upgrade — Note F is a proof that it cannot — so this sequence is a genuine
counterexample to their expectation. That is the sharpest thing the repo has.

**γ = 1/2 is a knife-edge in the literature's own map, and x² + 1 sits just
below it.**

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
proof would imply the theorem via the asymptotic sieve". Strictly, **no such
inequality exists for [ASP] as written** — (R1) is unsatisfiable, so no Type II
input can invoke Theorem 1 or Theorem 2. But that is a statement about one
theorem's hypotheses, and [HB] is the precedent for replacing them.

- **Step 2 stands.** [Note F](note-F-failure-localisation.md)'s Question F is
  still the right target: it is a statement about the sequence, and it does not
  depend on which sieve consumes it. Notes E, F, G, H are not downstream of a
  dead end.
- **What Step 1 delivers is a constraint, not a checkpoint.** Any sieve applied
  to x² + 1 must run on a Type I level of x^{1/2}, which is a sixth of an
  exponent below what [ASP] asks. Note C's deliverable is therefore that
  constraint plus the evidence that (R1) is soft — not the bilinear inequality
  the plan expected.
- **The plan's §1.3.2 prediction was right.** The Type I level really is
  x^{1/2−ε}, by the sharp argument of Note B.

## Open

The three literature markers are resolved; what replaced them is sharper.

**Resolved.**

- *Green–Sawhney* (arXiv:2410.04189, accepted Acta Math.). Theorem 1.1 for
  n ≡ 0, 4 (mod 6), both coordinates prime; at n = 4 it settles FI's Gaussian
  Primes Conjecture ([FI, arXiv:1811.05507, Conj. 1.1], of which FI wrote that
  it "requires breaking the parity barrier"). **α = 1**, sharing Dirichlet's
  rung — one above a² + b⁴, not two, and not thin at all by FI's own criterion.
  Their Type II input is Gowers U^k norms *of functions on Z at scale X^{1/2}*;
  the number field carries the sieve, not the norms. **The plan's
  §Cross-cutting exclusion of Green–Tao methods survives**, on its stated
  grounds. The method is vacuous rather than false on a mass-X^{1/2} weight:
  every hypothesis is normalised against the full norm range, and
  re-normalising would demand power-of-X Gowers savings where their Prop. 4.4
  supplies (log X)^{−A}.
- *Merikoski, "On Gaussian primes in sparse sets"* (arXiv:2302.11331,
  Compositio Math. **161** (2025), 181–243). Infinitude for
  \|B ∩ [0,Y]\| ≫ Y^{1−δ} (Thm 1.1); δ never made explicit, guessed in
  (1/20, 1/10), with δ = 1/6 a hard barrier where the Type II range empties.
  **Does not use [ASP].** Decisively, his A(X) ≍ X^{1/2}\|B\| = X^{1−δ}, so
  α ≈ 1 − δ — essentially dense, not our regime; and his large-sieve step needs
  N ≪ X^{−η}\|B\|, so \|B\| = 1 empties the Type II range at any δ. Every b
  must sit near X^{1/2}, so **b = 1 is off the chart, not a limit of it**.
- *Ford–Maynard* (arXiv:2407.14368). **Refuted as a source of a relaxed (R1)**:
  it never cites [ASP], never states (R1) or (B1)–(B3), and never mentions
  γ(n,C). Its value is the opposite of what was hoped — Theorems 2.4 and 4.16
  map exactly where γ = 1/2 fails.
- *arXiv:2112.03617*: α = 3/4 for X²+(Y²+1)², α = 5/6 for X²+(Y³+Z³)². The
  inner Y²+1 makes the Type II congruence curve non-singular, which helps the
  main term but *costs* Type II range (N ≪ X^{1/3−η} against FI's X^{1/2−η}).
  No transfer to one variable.

**Now open, in priority order.**

- **Read Duke–Friedlander–Iwaniec §6 directly** (*Ann. of Math.* **141** (1995),
  423–441). Everything in this note about DFI is at two removes. The claim that
  x² + 1 *meets* DFI's Type I hypothesis is `inferred` and load-bearing.
- **[VERIFY]** Ford–Maynard Theorem 2.4's escape clause is divisor-bounded
  weights, and DFI is the divisor-bounded setting. Is x² + 1's weight
  divisor-bounded in their sense, and does Theorem 2.4 therefore apply to it or
  exempt it? This is the sharpest live question in the repo.
- **[VERIFY]** Xiannan Li's sieve reaches ≈ x^{0.6418} unconditionally. What in
  it is density-limited, and does the limit come from Type I or Type II?

## Adversarial review

- *Two-parameter freedom smuggled in?* No — this note only reads hypotheses.
- *Where is parity broken?* In [ASP] by hypothesis (B); §1 is explicit that (B)
  is the new axiom and (R) the classical one. The finding here is that x²+1
  fails the *classical* half, so it never reaches the parity-breaking machinery.
- *Is the failure really unfixable, or an artefact of choosing aₙ as an
  indicator?* Weighting cannot help: (9.2) compares Σaₙ² to A(x)², and any
  reweighting that inflates A(x) inflates Σaₙ² at least as fast by
  Cauchy–Schwarz. Worth writing out properly.
- *Could a different sieve apply?* Yes — [ASP] is one theorem, not a proof of
  impossibility, and [HB] is the worked precedent for writing a replacement when
  (R1) fails. Iwaniec 1978 (P₂) already works at this density with a classical
  weighted sieve; what is unavailable at A(x) = x^{1/2} is the parity-breaking
  upgrade.
- *Did this note over-read its own finding once already?* Yes. The first version
  concluded "the obstruction is Type I, not Type II" and deprioritised Step 2.
  Heath-Brown's p. 3 remark shows (R1) is the negotiable hypothesis. The lesson
  is to distinguish **a hypothesis of one theorem** from **a property of the
  sequence**: Note B's x^{1/2} cap and Note F's C₄-free lemma are the latter and
  survive any change of sieve; (R1) is the former.
