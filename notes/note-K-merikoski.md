# Note K — Merikoski's a² + (b²+1)², and what κ cannot see

*Added. Status: draft. Supported by
[`exp08`](../experiments/exp08_merikoski_ledger.py) and
`tests/test_bilinear.py::test_merikoski_sequence_is_indistinguishable_from_a2b4_here`.
Source read directly: [MER] = Merikoski, [arXiv:2112.03617v2](https://arxiv.org/abs/2112.03617),
*The polynomials X²+(Y²+1)² and X²+(Y³+Z³)² also capture their primes*, 58 pp.*

This note exists because [Note D](note-D-comparison-ledger.md) carried a
standing request for **a fourth published sequence with a known outcome**, and
one turned up that is far better than the request: Merikoski's sequence differs
from Friedlander–Iwaniec's by a single `+1` inside the inner polynomial, and its
Type II counting problem is *literally this repo's own congruence*.

## Why this sequence and not another

> "the argument fails to capture primes of the form a² + f(b)² for
> non-homogeneous quadratic polynomials f(b)" — [MER] p. 2

That is the FI method meeting x² + 1's polynomial for the first time.
Merikoski's Theorem 1 (p. 2) fixes it:

> Σ_{p≤X} Σ_{p = a²+(b²+1)²} 1 ≍ X^{3/4} / log X.

Note the `≍`: **a lower bound of the right order, not an asymptotic.** And
[MER] p. 6 defines

> ρ₁(d) := |{ν (d) : ν² + 1 ≡ 0 (d)}|

which is [Note A](note-A-dictionary.md)'s ρ(d), unchanged.

Setting D = 0 in `a2_bsq_plus_D_sequence` recovers a² + b⁴ exactly, so the two
sequences can be compared with one variable changed and nothing else.

## The measurement: κ cannot tell them apart

`python experiments/exp08_merikoski_ledger.py 10000000`

| sequence | \|A\| | κ | √κ | max min-degree | ratio | C₄-free? | max Gram |
|---|---:|---:|---:|---:|---:|:--:|---:|
| a² + b⁴ | 153 890 | 2368.2 | 48.66 | 41.22 | 0.85 | no | 667 |
| a² + (b²+1)² | 153 856 | 2367.2 | 48.65 | 40.12 | 0.82 | no | 213 |
| x² + 1 | 3 162 | 1.0 | 1.00 | 1.26 | 1.26 | **yes** | 1 |

Rows 1 and 2 agree in |A| to 0.02%, in κ to 0.04%, and in max min-degree to
2.7%. The literature separates them by **a sixth in the Type II exponent**:

| | Type I | Type II range | conclusion |
|---|---|---|---|
| a² + b⁴ [FI] | D ≤ X^{3/4−5ε} | X^{1/4+η} ≪ N ≪ X^{1/2−η} | asymptotic |
| a² + (b²+1)² [MER] | D ≤ X^{3/4−η′} (Prop. 4, p. 7) | X^{1/4+η} ≪ N ≪ X^{1/3−η} (Prop. 12, p. 15) | lower bound only |

**So κ is a necessary condition and never a sufficient one.** This is the
sharpest available correction to how the ledger has been reading κ: κ = 1 for
x² + 1 says the bilinear structure is *absent*, which no method can repair; but
κ ≫ 1 says nothing about how much of that structure is *usable*.

## How insufficient is κ? A conjecture of mine, refuted

Since κ = |A|²/Q and |A| ≍ Q^{1/2}|B| for A_B = {a + b²i : b ∈ B}, we have
**κ = |B|² exactly**, so the κ criterion is met at |B| = 2 — two values of b.
Merikoski's sparse-set theorem needs |B| ≫ Y^{1−δ}. That gap suggested a
conjecture: *the incidence graph stays 4-cycle-free until |B| is a positive
power of Q, so κ is wrong by an exponent rather than a constant.*

**It is false.** 4-cycles appear at |B| = 2, and κ and C₄-freeness therefore
fail at the *same* threshold. Getting there needed two controls, because the
first two measurements were both artefacts:

- **The unit cofactor.** At B = {1,2} the max Gram hit the search cap
  immediately, with argmax column norms (1, 16) — n₁ a *unit*. This is the same
  artefact [Note L](note-L-over-Z.md) found driving the full rational graph's
  growth, in a new setting. Fix: a cofactor floor N(n) ≥ N(m).
- **Commensurable lines.** With 1 ∈ B, or more generally b₁ | b₂, the map
  z ↦ (b₂/b₁)² z carries the line Im = b₁² into Im = b₂², since (b₂/b₁)² is then
  a rational integer. G(1, 4) at B = {1,2} counts *every* a with (4a)²+16 ≤ Q —
  pure dilation, not bilinear structure. Fix: 1 ∉ B and no b dividing another.

With both applied — B = {2,3}, window [16, 64), no unit m or n — an explicit
4-cycle survives:

> n₁ = 4+2i (norm 20), n₂ = 19+7i (norm 410)
> m = 1+4i (norm 17): m n₁ ∼ 18+4i, m n₂ ∼ 83+9i
> m = 2+6i (norm 40): m n₁ ∼ 28+4i, m n₂ ∼ 128+4i

all four products associates of elements of A_{2,3}. A parallel session reached
the same conclusion independently and by a different route — solving the
collision condition algebraically and sweeping x₂, x₃ ≤ 2500 — finding ~300
collisions for each of B = {2,3}, {2,5}, {3,5}, {3,4} against ~600 for the
leaky B = {1,2}, {1,3}. So the dilation leak roughly doubles the count but does
not create the cycles.

**So κ is sharp at the threshold, and must not be demoted on these grounds.**
"Necessary, not sufficient" stands — it is the a²+(b²+1)² control above, and it
is a statement about how much κ buys *above* the threshold, not about where the
threshold is.

### Why they cross together, which is not a point in κ's favour

The sharpness is real, and its *cause* deflates the reading it invites. Take the
plain line

> A_c = {a + ci : a ≥ 1, a² + c² ≤ Q},  so |A_c| = ⌊√(Q − c²)⌋

and κ = |A|²/Q = 1 − c²/Q. **Exactly 1 in the limit, for every c.** A single line
cannot have κ > 1 — the geometry forbids it, since a line's count is its length
and its length is √Q. And A_c is C₄-free by Note F's argument verbatim with c in
place of 1: (a₁+ci)(a₄+ci) = (a₂+ci)(a₃+ci) forces a₁a₄ = a₂a₃ **and**
a₁+a₄ = a₂+a₃, hence {a₁,a₄} = {a₂,a₃}.

Two lines always admit a 4-cycle. At (c₁,c₂) = (2,3) — no c = 1, neither
dividing the other, so both of the artefacts above are excluded:

> **(1+2i)(6+2i) = 2 + 14i = (2+2i)(4+3i)**

and the same holds at (2,5), (3,5), (3,7), (5,7), (4,6). So in the A_B family
**κ = |B|² counts the lines and C₄-freeness permits one of them**. The two
conditions are functions of the same integer, which is why no measurement can
separate them there. The threshold coincidence is forced by the parameterisation;
it is not evidence that a density statistic detects 4-cycles, and κ should be
neither demoted nor credited on the strength of it.

**And it generalises Note F in the direction that matters.** The C₄-free lemma is
not a fact about x²+1. It is a fact about *a line*, of which x²+1 is the case
c = 1. *(Over Z[i]. Over Z it is not — see the next section, where the
same family refutes the transfer at c = 6.)* That sharpens the obstruction rather than softening it: x²+1 is not
unluckily C₄-free, **every line is**, and α = 1/2 is forced for all of them — so
there is no nearby line with more room, and the escape has to leave the family
entirely. Machine-checked in `test_every_single_line_is_c4_free_and_has_kappa_one`
and `test_two_lines_always_admit_a_four_cycle`.

### And two points are enough — so κ does not see it even at the threshold

The A_B family ties κ to the line count, so nothing measured *inside* it can
separate the two conditions. Step outside by two elements:

> A = {x+i : x ≤ X} ∪ {2+2i, 4+2i},  κ = (X+2)²/(X²+1)

κ = **1.000004** at X = 10⁶, against **0.999999** for the bare line — the same
number to five places — and

> **(1+i)(4+2i) = 2+6i = (2+i)(2+2i)**

so it is not C₄-free. **O(1) elements flip C₄-freeness at fixed κ.** The
threshold coincidence above is therefore a fact about the parameterisation, and
"κ is sharp at the threshold" should be read as *κ is not violated there*, never
as *κ locates it*.

**And the D axis is the strongest form of all three, because it needs no
perturbation.** For x² + D the sequence has |A| = X and Q = X² + D, so

> **κ = X²/(X² + D) → 1 for every fixed D**

At X = 10⁴ the whole family sits within 4×10⁻⁷ of 1 — κ = 0.999999990 at D = 1
against 0.999999610 at D = 39, **a spread in the ninth decimal**. Meanwhile D
decides the structure completely: D = 1, 2 hold unconditionally, D = 4 holds on
parity, and D = 6, 11, 19, 36, 39 fail with explicit witnesses, **D = 39 with a
banded triple**.

> **An entire one-parameter family has κ → 1 throughout and splits into
> proved-holds and proved-fails.**

The line-count argument explains the A_B coincidence away; the two-point argument
needs an O(1) perturbation a reader can call artificial. This needs neither —
x² + D are natural sequences, one per D, and **the parameter κ cannot resolve is
the parameter that decides the answer.**

**And along the one axis κ *can* see, it points the wrong way.** For k·x² + D,
κ = X²/(kX² + D) → **1/k**, so the leading coefficient does move it. Measured at
X = 1200:

| f | κ → | doubly-dyadic C₄-free? |
|---|---:|---|
| x²+1 | 1 | **holds** |
| x²+39 | 1 | **fails** |
| 2x²+1 | 1/2 | holds |
| 2x²+39 | 1/2 | **holds** |
| 3x²+39 | 1/3 | holds |

**Same κ = 1, opposite outcomes; and the smaller κ holds exactly where the larger
one fails.** No monotone relation in either direction.

The mechanism is known and it is why: **k imposes k | M·D**, thinning the class
population and *tightening* the structure, while κ = 1/k *falls* with k. Larger k
means smaller κ **and** a tighter sequence — density and structure moving in
opposite directions along the only axis κ resolves.

> **Through D, κ is blind. Through k, κ is inverted. That is everything κ can see
> of a degree-2 sequence, and neither component carries the property.**

**What this does not show.** It is about the binary property. One 4-cycle moves
max G from 1 to 2 and leaves mean G at O(1/X), and [this note's own refuted
classifier](#mean-g-separates-them-where-κ-does-not--refuted-by-the-test-built-to-confirm-it)
plus Note L's mean-G work both say the mean is the load-bearing statistic and the
max is not. So the Type II obstruction — a statement about the whole graph — is
untouched. The tempting stronger reading, "κ is blind to the obstruction", is the
same over-reach that already put two claims in the registry as `refuted`, and is
not made here.

### The conjecture was testing the wrong object, and the right one answers it

The question "how insufficient is κ?" has an answer, and it is a power of X —
just not on the axis the conjecture looked at. κ and C₄-freeness are properties
of the *graph*, and they fire at |B| = 2. What a *method* needs is a different
quantity entirely, and Merikoski's other paper states it. From
[arXiv:2302.11331v3](https://arxiv.org/abs/2302.11331) (Compositio Math. **161**
(2025), 181–243):

> **Theorem 1.2.** There is some (computable) δ > 0 such that the following
> holds for any small η > 0. For all sufficiently large X and for all
> B ⊆ [ηX^{1/2}, (1−η)X^{1/2}] ∩ ℤ with **|B| ≥ X^{1/2−δ}** we have for any
> ε > 0, Σ_{p = a²+b² ≤ X} 1_B(b) ≫_ε X^{1/2−ε}|B|.

So B must be within X^δ of the *entire* available range, and Merikoski notes
this is the first unconditional power saving in the density of B at all —
before it, Fouvry–Iwaniec needed density (log X)^{−C}. Putting the two axes
side by side, with κ = |B|²:

| | |B| | κ |
|---|---|---|
| κ > 1, and 4-cycles appear | **2** | 4 |
| best available method (Merikoski Thm 1.2) | **X^{1/2−δ}** | X^{1−2δ} |
| x² + 1 | 1 | 1 |

> **κ > 1 is satisfied a full power of X before any method applies.** That is
> the quantitative content of "necessary, not sufficient", and it is a statement
> about methods rather than about the incidence graph — which is exactly where
> the refuted conjecture went wrong: it tested the graph and the graph was
> innocent.

Merikoski also states the repo's own position in his first paragraph — "A key
motivating question is Landau's fourth problem, which asks if there are
infinitely many prime numbers of the form n²+1. **This is far beyond the current
methods as the set is very sparse** – the number of integers up to X of this
form is of order X^{1/2}" — and gives Li's record exactly: the sparsest
polynomial sequence with primes has size **X^{43/67+ε}** (43/67 = 0.641791…,
which is the 0.6418 this repo had been carrying).

**And C₄-freeness is arithmetic, not a density constraint.** For a C₄-free
bipartite graph, Σ_n C(d_n, 2) ≤ C(R, 2). Measured at Q = 10⁶:

| window | x²+1 (col-side ratio) | a²+b⁴ |
|---|---:|---:|
| [16, 64) | 0.048 | **29.0** |
| [64, 256) | 0.016 | **7.71** |
| [256, 1024) | 0.005 | **1.95** |

x²+1 sits 20× to 400× *below* the ceiling C₄-freeness imposes, so the lemma is
nowhere near binding as an edge count — the graph is far sparser than it would
have to be. a²+b⁴ exceeds 1, as it must, which is the control that the measure
detects the difference at all. The cycles that appear at |B| = 2 are created by
arithmetic, not by density, which is exactly why a density statistic like κ
cannot see where they start.

## The line family and the discriminant axis

*Four results that are not about κ at all. They belong here because they
grew out of the line result above, and they end by locating x²+1 inside a
one-parameter family rather than leaving it an isolated special case.*

### The family refutes the Z[i] → Z transfer, at c = 6

A_c is C₄-free over Z[i] for **every** c. Over **Z**, on the doubly-dyadic
configuration where Theorem O.12 proves C₄-freeness at c = 1, the property holds
only for

> **c ∈ {1, 2, 3, 4, 5, 7}**

and fails at the other fourteen values up to 20. Stable from X = 1500 to 3000 on
the survivors. The witness at c = 6 is doubly dyadic on both axes — cofactors
(5, 8) with u = 1.6, moduli 9 and 17 with ratio 1.889:

> 5·9 = 45 = 3²+6²  8·9 = 72 = 6²+6²
> 5·17 = 85 = 7²+6²  8·17 = 136 = 10²+6²

**And the mechanism is the Z[i]/Z gap in its purest form:**

> (3+6i)(10+6i) = **−6 + 78i**   (6+6i)(7+6i) = **6 + 78i**

**Conjugate, not associate.** No Gaussian 4-cycle — A₆ is C₄-free over Z[i], as
the line argument requires — while the norms coincide at 6120 and the rational
cycle is real. Two Gaussian elements with the same norm and different ideals are
invisible to Z, and that is the whole of the coarsening
[Note L](note-L-over-Z.md) describes, arriving on the *banded* configuration
where at c = 1 it cannot.

**So the c-family bounds the transfer rather than supporting it.** Four
supporting instances against fourteen refuting, over c ≤ 20. It does not touch
`gaussian-to-rational-bridge` for x²+1, where the Z-side statement is **proved**
by O.12 rather than transferred — but it removes any reading of the line family
as evidence that Z[i]-to-Z transfer is reliable, and it is the repo's first
concrete counterexample to that pattern.

**It also settles a question the derivation left open.** The generalised bound
V·W = c²·M·(m_i − m_j) says O.12's *argument* is special to c = 1; measurement to
c = 5 said the *fact* generalised. The fact is special too — nearly. The
derivation pointed at the right conclusion with the wrong threshold, while five
sizes of measurement at c ≤ 5 said "generalises" and would have gone on saying it.
Machine-checked in `test_doubly_dyadic_c4_freeness_fails_at_c_equals_six`.

### And there is a mechanism: x²+1 is the degenerate member of an explicit family

Extend the axis once more — to **D** itself, in x² + D. Four *consecutive*
arguments k, k+1, k+2, k+3 give a 4-cycle exactly when the outer product equals
the inner one, and

> **(k²+D)((k+3)²+D) − ((k+1)²+D)((k+2)²+D) = 4(D − k² − 3k − 1)**

since k(k+3) and (k+1)(k+2) differ by 2 while the D-linear parts differ by 4. So
the cycle exists precisely for

> **D = k² + 3k + 1:  D = 1, 5, 11, 19, 29, 41, 55, …**

and exactly two members fail to be *doubly dyadic* counterexamples:

| k | D | values | cofactor ratio | modulus ratio | |
|---:|---:|---|---:|---:|---|
| 0 | **1** | 1, 2, 5, 10 | 2.000 | 5.000 | **first value is the UNIT** |
| 1 | 5 | 6, 9, 14, 21 | 1.500 | **2.333** | modulus ratio ≥ 2 |
| 2 | 11 | 15, 20, 27, 36 | 1.333 | 1.800 | genuine |
| 3 | 19 | 28, 35, 44, 55 | 1.250 | 1.571 | genuine |
| 4 | 29 | 45, 54, 65, 78 | 1.200 | 1.444 | genuine |

**x²+1 is the k = 0 member.** It does not avoid the family — its instance is
**degenerate**, because one of the four values is 0²+1 = **1**, the unit modulus
that no Type II hypothesis admits and that this repo excludes everywhere else for
the same reason. D = 5 escapes for a *second, unrelated* reason, which is why the
first genuine counterexample is D = 11 and not D = 5. Both ratios fall toward 1
as k grows, so these are not marginal cases scraping under a threshold.

**This does not touch Theorem O.12**, which is about x²+1. What it removes is any
reading of O.12 as an instance of something general: its conclusion fails for an
infinite explicit family of degree-2 sequences, and **x²+1's escape has a cause**.
Machine-checked in
`test_four_consecutive_x_give_a_cycle_exactly_when_D_is_k2_plus_3k_plus_1`.

### The same move settles the triple question: x²+39 has a banded triple

Extending the D axis to *three* moduli rather than two:

> **x² + 39.  Cofactors (5, 8)** — ratio 1.6, one dyadic **band**.
> **Moduli 8, 11, 15** — 15 < 16, one dyadic **window**.
>
> 5·8 = 40 = 1²+39  8·8 = 64 = 5²+39
> 5·11 = 55 = 4²+39  8·11 = 88 = 7²+39
> 5·15 = 75 = 6²+39  8·15 = 120 = 9²+39

All six verified. Three shared moduli in one window with both cofactors inside
one band — which refutes the analogue of **Conjecture O.2** (no window holds
three) *and* of **Theorem O.12** (banded cofactors share at most one), in a
single configuration, with cofactors as small as 5 and 8.

Over D ≤ 60 there are **seven** unit-free triples — D = 29, 39, 42, 44, 52, 53,
59 — and **D = 1 is not among them**. The unit-free restriction carries the
weight: *35 of 60* admit a triple if the unit cofactor is allowed, and the unit
is exactly what no Type II hypothesis admits.

**This does not refute O.2 or O.12 for x²+1**, and neither is weakened by a
digit: O.12 is proved, and O.2 has no counterexample to X = 8000 with its
two-step floor unmoved at 13.0000 across five sizes. What it removes is any
reading of either as an instance of something general. **The Note O thread's
twelve theorems establish a fact about x²+1, not about degree-2 sequences** — the
same correction the D = k²+3k+1 family makes one level down, where x²+1 was the
degenerate member of a failing family and here is simply not in the failing set.
Machine-checked in
`test_x2_plus_39_has_a_banded_triple_so_O2_is_special_to_D_equals_one`.

### The mechanism: the invariant is M·D, and x²+1 is the tight end

All of the above is one statement. For f(x) = x² + D with a·m = X²+D and
b·m = Y²+D, b(X²+D) = abm = a(Y²+D) gives

> **aY² − bX² = (b−a)·D = M·D**

so **the invariant Note O calls M is really M·D**, and every bound built on it
weakens by a factor of D. Verified together with

> **V·W = D·M·(m_i − m_j)** — 0 failures over 5354 pairs, D = 1, 2, 5, 11, 29, 39, 52

which is the identity above with D in place of the c² found first. O.9's bound
becomes **3ab < (M·D)^{4/3}**, and at cofactors (5, 8) with M = 3:

| D | 3ab | (MD)^{4/3} | |
|---:|---:|---:|---|
| 39 | 120 | **572** | permitted — **and the triple occurs** |
| 1 | 120 | **4.33** | forbidden — and none occurs |

**Same bound; D is the whole difference.** This subsumes every D-result in this
note: the c-family break at c = 6 (there D = c², and the |V| bound weakens by
exactly c²), the 4-cycle family D = k²+3k+1, and the seven unit-free triples at
D ≤ 60.

**And the density confirms the mechanism rather than merely agreeing with it.**
Over D ≤ 160 at X = 900, **51 of 160 (31.9%) admit a unit-free triple, none with
D ≤ 25**, and D = 1 does not. A bound loosening like D^{4/3} predicts exactly
that shape — nothing until D is large enough, then a positive density. A sporadic
set would look completely different.

> **So x²+1 is not special in an arbitrary way. It is the D = 1 end of a
> one-parameter family — the point at which every bound in the Note O apparatus
> is at its tightest — which is why those conclusions hold there and essentially
> nowhere else.** The twelve theorems are not weakened by this. They are located.

**And the located version is sharper than "x²+1 is the tight end", because the
argument reaches further than one value.** Run O.12 with the M·D invariant:
s = √(ab)/(M·D) = √u/((u−1)D), so τ(V)² < 3 reads V·s < 1/√3 and **a banded pair
in one window requires (u−1)·D/√u > V·√3** — against a band's
(u−1)/√u < 1/√2. So **D ≤ V·√6 makes the condition unsatisfiable**:

| input | bound | covers |
|---|---|---|
| \|V\| ≥ 1, unconditional | D ≤ √6 = 2.4495 | **D = 1, 2** |
| \|V\| ≥ 2, from evenness | D ≤ 2√6 = 4.8990 | **D = 1, 2, 3, 4** |

At D = 2 the arithmetic is 1.41421 < 1.73205 — a 22% margin, not a near miss. V
is even for every D measured (0 odd out of 15,084 pairs across D = 1…6 at
X = 2500), though that is *proved* only for D = 1.

**The two regimes differ in kind, and that is the point.** For D ≥ 5 the bound is
merely *satisfiable* and larger X eventually supplies a class meeting it —
D = 35 fell at X = 2500, D = 20 at X = 4000. For D ≤ 4 no cofactor class can
satisfy it at all, so no amount of X helps. A conjecture that "every D > 1
eventually fails" was filed here and is **refuted at D = 2** for exactly that
reason: it rested on counting classes, which describes the first regime and has
no purchase on the second.

**Where the D thread ends, with each row's status attached.**

| D | status |
|---|---|
| ≤ 2 | **proved**, unconditional — (u−1)D/√u < 1.41421 < √3 |
| 3, 4 | **proved** on \|V\| ≥ 2, i.e. on evenness — observed for D ≤ 6, proved only at D = 1 |
| 5 … 10 | **unfallen** to X = 7000, unprotected, unexplained |
| 11, 14, 19, 20, 21, 23, … | **fallen**, with witnesses |

The 5…10 gap is the interesting one and it is not a gap in the sweep: the bound
permits failure there and no failure is found, which is the same
necessary-not-sufficient gap as [Note O](note-O-tau-multiplier.md)'s 39 of 60
admissible classes that hold no triple. **The argument's boundary is not the
empirical boundary — and it is not an artefact either**, since it is the only
proved one.

**And the timing of the failures is arithmetic, not monotone in D.** D = 11, 14,
19 fail by X = 1200 at cofactors below 6, while D = 20 needs X = 4000 at
(47, 63) and D = 35 needs X = 2500 at (2249, 3756) — so **D = 11 fails far
earlier than D = 20 despite having the tighter bound**. The early ones are the
k²+3k+1 family, which supplies a witness at four consecutive arguments and
therefore announces itself immediately. Small-cofactor witnesses are that
family's signature, not failure's.

Machine-checked in
`test_the_whole_note_O_apparatus_generalises_with_M_replaced_by_M_times_D`.


## ~~Mean G separates them where κ does not~~ — refuted by the test built to confirm it

*Written and refuted within the hour. Kept because the refutation is the useful
part and the shape of the error is worth the space.*

Note L's mean-G statistic looked like a candidate for the *sufficient* part of
this note's headline. At Q = 4×10⁶, band N ∈ [2048, 4096):

| sequence | κ | mean G | max G | status |
|---|---:|---:|---:|---|
| x² + 1 | 1.00 | 0.0219 | 2 | open |
| **x³ + 2y³** | **75.1** | **0.1888** | **79** | **captured — Heath-Brown** |
| a² + b⁶ | 115.4 | 0.5590 | 22 | not known captured |
| a² + b⁴ | 1297.5 | 3.592 | 107 | captured — Friedlander–Iwaniec |
| a² + (b²+1)² | 1269.3 | 12.809 | 97 | captured — Merikoski |

Without the second row it reads as a clean law: mean G > 1 for both captured
sequences, < 1 for x²+1, and κ separating none of it. **With it the law is dead.**
x³+2y³ is captured and sits at **0.1888** — below 1, and *below* the sequence with
no known outcome. Captured sequences land at 0.19, 3.59 and 12.81; non-captured at
0.02 and 0.56. **Interleaved.**

The second row was chosen because it was decisive rather than convenient:
x³+2y³ and a²+b⁶ both have |A| ≍ Q^{2/3}, hence κ ≍ Q^{1/3}, so **κ cannot
distinguish them and any real classifier had to.** Mean G does not.

**What survives is the narrow original**, which was never a classifier: the
argument that a bounded integer-valued count with mean o(1) leaves dispersion
nothing to decompose does not prove too much, because a²+b⁴ has mean 3.59 at the
band where x²+1 has 0.022. That is a *two-sequence control*. Generalising it into
a four-sequence law — built from two points and "confirmed" on two more, one of
which had no known outcome — is the error, and the FI quotation below was
gathered as support for something already false.

## What actually separates them: the curve desingularises

[MER] p. 4 gives the reduction. After Cauchy–Schwarz the task is a count over

> b₁² + 1 ≡ a(b₂² + 1) (mod Δ),  Δ = Im(z̄₁z₂),  B₁, B₂ ≪ X^{1/4},

against FI's b₁² ≡ a b₂² (mod Δ). Poisson summation in b₁, b₂ splits this into
a main term N₁(a;Δ) = |{x₁,x₂ (Δ) : x₁²+1 ≡ a(x₂²+1)}| and an error term of
exponential sums. Then the trade, both halves quoted:

- **Main term — the +1 helps.** For a ≠ 0, 1 the homogenisation
  (1−a)x₀² + x₁² − a x₂² = 0 is *non-singular* ([MER] p. 16), so Weil gives
  ε_p(a) ≪ p^{1/2} and the divisor sum truncates at d ≤ log^{2C}X. FI's curve
  x₁² ≡ a x₂² is singular, N_FI(a;p) = p + (a/p)p, and that Jacobi-symbol sum
  "cannot be truncated" — they must show cancellation in z₁, z₂ instead.
  > "for the main term having (b²+1)² rather than b⁴ turns out to be a friend
  > rather than an enemy" — [MER] p. 5
- **Error term — the +1 hurts, and this is what costs the sixth.** On the
  non-singular curve S(a,h₁,h₂;Δ) ≪ |Δ|^{1/2+ε} ≪ N^{1/2+ε}, "sufficient
  provided that N ≪ X^{1/3−η}". On FI's singular curve one "morally" gets
  S_FI ≪ N^ε, "which is why for a²+b⁴ one can handle the Type II sums up to
  N ≪ X^{1/2−η}" ([MER] p. 4).

**Both halves of the trade run through the b-sum.** There is no version of
either that survives B = 1.

## √κ is the length of the Poisson sum

For A = {a + f(b)i} with a ≪ Q^{1/2} and b ≪ B, we have |A| ≍ Q^{1/2}B, so

> κ = |A|²/Q = B²,  **√κ = B**

identically — not a fit. What Merikoski supplies is the *meaning* of B: it is
the range [MER] p. 4 names for the Poisson summation variables, B₁, B₂ ≪ X^{1/4}
at α = 3/4. So the repo's κ is not merely a degree heuristic that happens to
track α; **√κ is the length of the sum every Type II argument in this family
applies Poisson summation to.**

For x² + 1, B = 1. Poisson summation over a single point is the identity map;
there is no main term to evaluate, no exponential sum to bound, and no curve —
singular or not — to apply Weil to. [Note D](note-D-comparison-ledger.md)
already said "a large sieve over one point is the trivial bound"; this is the
same statement with a published mechanism attached to it.

The degree claim `kappa-invariant` — that max over splits of min(D_m, d_n) ≍ √κ
— remains `extrapolated`. The identity √κ = B is arithmetic and is not what that
claim is about.

## Ford–Maynard place this sequence too, and the placement is the useful part

[FM] Table 1, p. 3 ("Examples from the literature (**epsilons omitted**)")
lists eight rows. Three matter here:

| γ | θ | ν | reference | property |
|---|---|---|---|---|
| 3/4 | 1/4 | 1/2 | Friedlander–Iwaniec | p = x² + y⁴ |
| 3/4 | 1/4 | **1/12** | Merikoski, Thm. 1 | p = x² + (y²+1)² |
| 1/2 | 0 | 1/3 | Duke–Friedlander–Iwaniec | x² ≡ a (mod p), x/p in a short interval |

Two things follow, and both cut against how [Note C](note-C-requirements.md)
had been arguing.

1. **ν = 1/12 suffices.** Merikoski's Type II range is a twelfth of an exponent
   wide, and Harman's sieve converts it into a lower bound of the right order.
   The bar is not "a wide arbitrary-coefficient Type II range". It is ν > 0.
2. **γ = 1/2 is not itself fatal.** DFI sit at γ = 1/2 with ν = 1/3 and succeed,
   via exactly the divisor-bounded route ([FM] p. 6: "This was exploited in
   Duke–Friedlander–Iwaniec [7] in the case θ = 0, ν = 1/3").

So the discriminating parameter across the whole table is ν, and every entry has
ν > 0. [Note F](note-F-failure-localisation.md) proves ν = 0 here. See
[Note C](note-C-requirements.md) § *The Ford–Maynard placement, corrected
again* for what that does to the earlier γ = 1/2 − ε argument.

## The coefficient class is the honest one

[MER] Prop. 12, p. 15 takes α(m) and β(n) bounded, with β supported on
squarefree n coprime to P(W) and satisfying the Siegel–Walfisz property (4.1),
p. 14; Prop. 13, p. 16 reduces to β with Siegel–Walfisz main term 0 (4.2).

That is **α arbitrary, β Siegel–Walfisz** — not arbitrary on both sides. It is
the same class [CLAUDE.md](../CLAUDE.md) insists the repo keep separate from the
adversarial one, and it is exactly the class
[Note J](note-J-mobius-in-progressions.md) measures: an arbitrary bounded α is
worst-cased by α(m) = sign(Σ_n β(n)c_{mn}), which is the absolute value per
modulus. So Note J's object

> Σ_q | Σ_{x ≡ r_q (q)} μ(x²+1) |

is *the Merikoski-class Type II sum for this sequence*, not a weaker relative of
it. Note J's measurement — signed sum under 2% of the absolute-value sum — is
therefore a measurement of the quantity Prop. 12 would have to control.

## Adversarial review

- *Is this a fourth data point, or the same point twice?* It is genuinely new in
  the direction that matters: the density is deliberately **identical** to
  a² + b⁴, so the sequence tests whether anything other than density is being
  measured. It is not new evidence about density, and must not be counted as a
  fourth density.
- *Where is two-parameter freedom being smuggled in?* Nowhere new — but this
  note is the first place the repo can say what the second parameter *is used
  for*, rather than that it exists. It is the Poisson variable.
- *Does this open a route for x² + 1?* No, and the note should not be read that
  way. Every step of [MER] §4–5 needs B → ∞. The one transferable item is
  negative: the desingularisation trick that rescues the main term costs half an
  exponent in the error term, so even granting a b-sum, the +1 makes the range
  *narrower*, not wider.
- *The mean-G classifier was added to this note and refuted in the same hour —
  should it be here at all?* Yes, and struck rather than deleted, because the
  refutation is the transferable part. What it demonstrates is a failure mode the
  rest of this note is exposed to: κ is *also* a statistic fitted to a handful of
  sequences with known outcomes, and this note's whole method is to add data
  points to that handful. The classifier died because a fifth point was chosen
  for being decisive rather than available. **The same test has not been run
  against κ**, and κ's "necessary" half is safe only because it is a much weaker
  claim than the classifier attempted.
- *Does the FI quotation now stand on nothing?* It stands on itself — it is a
  verbatim quote with a page reference — but it was *gathered* as support for a
  statement that was already false, which is worth remembering when it is next
  cited. Evidence collected to support a conclusion is not evidence discovered
  while testing one.
- *Does κ survive?* As a necessary condition, yes, and strengthened — it is now
  identified with a quantity in the published arguments. As anything sufficient,
  no, and it was never claimed to be; this note is the falsification test that
  says so out loud.
- *Where is parity broken?* In [MER], by Harman's sieve fed with ν = 1/12 at
  γ = 3/4. Nothing here breaks parity at γ = 1/2 with ν = 0.
