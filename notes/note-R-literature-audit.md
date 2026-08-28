# Note R — literature audit of the O-thread

**Purpose.** Charter §3.3(3): for each result in Note O, is it known? This gates
any writing up. The O-thread was built for two months without the search terms
that identify its object, and when those were finally run they matched it
immediately — so the prior on "already known" is high and the burden is on us.

**Status of this note.** A first pass. Every row is marked with how it was
checked, and *"not checked"* is a legitimate and common entry. **Nothing here
should be read as establishing novelty**; the only claims it makes are about
what was searched and what was found.

**How rows are graded.**

| grade | meaning |
|---|---|
| **KNOWN** | found in the literature, with a reference |
| **LIKELY KNOWN** | the technique is standard in the area; specific statement not located |
| **OPEN (theirs)** | the literature poses it as open |
| **NOT CHECKED** | no search run, or searches inconclusive |

---

## The object

| item | grade | evidence |
|---|---|---|
| The incidence is BD₂(−1): a·m − 1 = x² | **KNOWN** | Tsang–Yip arXiv:2512.03441 p.1 define BD_k(n) exactly. Bugeaud–Dujella and Bugeaud–Gyarmati studied the same objects two decades earlier |
| (1,5) at m = 2 is the D(−1)-triple {1,2,5} | **KNOWN** | classical; verified here |
| min{\|A\|,\|B\|} bounded for BD₂(−1) | **OPEN (theirs)** | Tsang–Yip: *"it remains an open question…"*; Q1.3: *"when k = 2, we do not know any upper bound on ℓ"* |
| ℓ = 3 measured for x²+1 | **NOT CHECKED** | whether anyone has computed this for the D(−1) incidence specifically |

## The equation and its solution structure

| item | grade | evidence |
|---|---|---|
| Elimination gives aY² − bX² = M·D | **KNOWN** | Dujella, *An absolute bound…*, §2: "Eliminating d … we obtain the following system of Pellian equations" |
| Solutions fall into finitely many classes with bounded fundamental solutions | **KNOWN** | Nagell Thm 108a, cited by Dujella; Note O reached it independently as Prop L.1's orbits |
| Class count is O_ε(M^ε) via Dickson | **NOT CHECKED** | standard-looking; not located |
| ε² ≥ φ⁴ spacing within a class (Prop L.1) | **LIKELY KNOWN** | this is the Pell recursion; every gap-principle argument in the area uses it |

## The gap principles

| item | grade | evidence |
|---|---|---|
| Gap principles exist in the area generally | **KNOWN** | Dujella's gap principle; c > 4ab for regular quadruples; by-range extension counts |
| **The standard one is VACUOUS at k = 2** | **KNOWN, and it is the key fact** | see below |
| O.4: three moduli in a window need τ_min⁴ < 2 + 1/X₁² | **NOT SUPERSEDED** by the standard gap principle, which gives nothing here |
| O.13: pair threshold (1+√2)⁴ = 33.9706 | **NOT SUPERSEDED**, same reason |
| O.15: triple threshold 82.5571 / 117.4171 via O.5 forcing V ≠ W | **NOT SUPERSEDED**, same reason |

### The standard gap principle is vacuous at k = 2, and that is why this case is open

Tsang–Yip Lemma 2.1 (their [31, Lemma 3.6]) is **exactly the K₂,₂ configuration**:

> *Let k ≥ 3 and n ≠ 0. Let x < y, z < w with xz ≥ 2|n|, and suppose xz+n, yz+n,
> xw+n, yw+n are k-th powers. Then yw ≥ k^k (xz)^{k−1} / (4^{k−1}|n|^k).*

Evaluate the constant and the exponent at k = 2, n = −1:

| k | bound |
|---:|---|
| 2 | yw ≥ **1.0000 · (xz)¹** |
| 3 | yw ≥ 1.6875 · (xz)² |
| 4 | yw ≥ 4.0000 · (xz)³ |
| 5 | yw ≥ 12.207 · (xz)⁴ |

At k = 2 it says **yw ≥ xz**, which is true for free since y > x and w > z. The
lemma is stated for k ≥ 3 precisely because it degenerates. **This is why
min{|A|,|B|} is settled for k ≥ 3 and open for k = 2** — the standard tool
returns nothing.

**Consequence for this audit.** The O-thread's gap principles are *ratio* bounds
derived from the Pell/multiplier structure (τ_V, the automorph ε, the window
condition τ² < 2 + D/X₁²), not absolute bounds of the `c > 4ab` type. Since the
absolute one is vacuous at k = 2, **they are not superseded by it.** That is a
weaker statement than "new" — no search has been run for the specific thresholds
— but it removes the most obvious way they could already be known.

## The arithmetic lemmas

| item | grade | evidence |
|---|---|---|
| \|V\| ≥ 2 unconditionally (parity + the mod-4 obstruction) | **NOT CHECKED** | elementary enough that it is probably folklore |
| All even elements lie on one side of a BD₂(−1) configuration | **LIKELY KNOWN** | two lines from ab ≡ 1,2 mod 4; anyone in the area would see it |
| O.17: composite integrality ⟺ per-prime sign differs, or r^e \| 8ps | **NOT CHECKED** | the per-prime sign is the same device as O.9/O.10; whether the composite criterion is stated anywhere is unchecked |
| O.5: no window holds (ξ, τ_pξ, τ_p²ξ) | **NOT CHECKED** | |
| O.7: O.2 for M an odd prime | **NOT CHECKED** | |

## What is definitely *not* in the literature so far as searched

Nothing. **No row above has been established as new.** The honest summary of the
first pass is: the object is known and named, the equation and its solution
structure are standard, gap principles are standard equipment, and the specific
thresholds have not been checked either way.

---

## The k = 2 gap is a named bottleneck, not an obscure corner

Worth separating from "it is open", because it changes how much the question is
worth. Tsang–Yip's Theorem 1.9 covers k ≥ 2 for multiplicative Hilbert cubes,
and then:

> *"When k = 2, we are not able to prove a result similar to Corollary 1.7, where
> the upper bound on the dimension of multiplicative Hilbert cubes only depends
> on the shift. **This is mainly due to the fact, mentioned earlier, that it is an
> open problem to show that for each n ≠ 0, there is an absolute upper bound on
> min{|A|, |B|} for a bipartite Diophantine tuple**"*

So the k = 2 bipartite bound is what blocks their own downstream result. Two
places in one paper name it: once as an open question in its own right, once as
the reason a theorem stops short. Combined with the vacuity of the standard gap
principle at k = 2, the picture is consistent — **the case is open because the
standard tool returns nothing there, and its being open costs the area
something.**

## The one thing the literature says is open, and we have data on

Tsang–Yip Question 1.3 for k = 2. Measured here, exhaustively to X = 9000:
**ℓ = 3** — |A| = 2 leaves |B| unbounded, and no K₃,₃ occurs among the 218
cofactor pairs sharing three or more moduli. The cutoff is sharp rather than
gradual: 96 of 160 qualifying pairs at X = 5000 reach K₃,₂ and none reaches
K₃,₃.

That is **data on an open question**, not an answer to it, and it is *sharper*
than the conjectural bound ℓ ≤ 5 — which this repo's own rules say to distrust.

## What to do next

1. Read Dujella's book (Tsang–Yip ref. [17]) for the gap-principle chapter, and
   check O.4/O.13/O.15 against it. **This is the highest-value single action**:
   it decides whether the O-thread's thresholds are new.
2. Search specifically for the *windowed* question — solutions of a Pell equation
   in a dyadic interval. The general searches run so far returned the class
   structure and nothing on interval constraints, but a null search proves
   nothing.
3. Only then consider what, if anything, is writable.
