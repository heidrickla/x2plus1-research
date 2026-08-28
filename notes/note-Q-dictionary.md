# Note Q — the dictionary: Note O ⇄ bipartite Diophantine tuples

Charter §3.3(2). Translating the O-thread into the language of the area it turns
out to belong to, because that is the precondition both for the novelty audit
(Note R) and for anything being written up.

## The sets coincide — this is not a specialisation

A cofactor of x²+1 is an integer a dividing some x²+1, i.e. with `a·m = x²+1`
for some m — equivalently **a·m − 1 is a perfect square**.

Conversely, if `a·z − 1 = P²` then `a·z = P²+1`, so a is a cofactor of P²+1.

> **The set of BD₂(−1)-admissible integers and the set of cofactors of x²+1 are
> the same set.** Note O has been studying BD₂(−1) in full generality, not a
> property of one sequence.

That matters for how its results should be stated: they are theorems about
BD₂(−1), and the x²+1 framing is presentation, not hypothesis.

## Vocabulary

| Note O | bipartite Diophantine tuples |
|---|---|
| cofactor a, modulus m, with a·m ∈ {x²+1} | elements a ∈ A, m ∈ B with a·m − 1 a square |
| cofactor pair sharing s moduli | K_{2,s} in the BD₂(−1) incidence |
| "no window holds three" (Conj. O.2) | a K_{2,3} with the B-side inside one dyadic interval |
| the conic aY² − bX² = M·D | the Pellian system after eliminating the shared element |
| solution classes; Prop L.1 orbits | Nagell Thm 108a classes; the Pell recursion |
| automorph ε (within a class) | the recursion v_{n+2} = 2s·v_{n+1} − v_n |
| multiplier τ_V (between classes) | *no clean counterpart located* — see Note R |
| unit cofactor a = 1 | the element 1, which the literature also treats separately |

## The elimination is theirs

Given x < y in A and z < w in B with all four products squares: `xz − 1 = P²`
and `yz − 1 = Q²` give `y(P²+1) = x(Q²+1)`, i.e.

> **xQ² − yP² = y − x.**

That is Note O's conic. Dujella performs the same elimination — *"Eliminating d
… we obtain the following system of Pellian equations az² − cx² = a − c"* — so
the starting point is standard and Note O reached it independently.

## What the O-thread says, in their variables

**The standard gap principle is vacuous here.** Tsang–Yip Lemma 2.1: for
x < y, z < w with all four products k-th powers and xz ≥ 2|n|,

  yw ≥ k^k (xz)^{k−1} / (4^{k−1}|n|^k).

At **k = 2, n = −1** this is `yw ≥ xz`, which holds for free. The lemma is stated
for k ≥ 3 because it degenerates, and that is why the k = 2 bound is open.

**What Note O gives instead is a joint constraint on the two ratios.**

> **Proposition (O.12 + O.13, restated).** *Let (A, B) have property BD₂(−1),
> with x < y in A and z < w in B. If **w/z < 2** then **y/x > (1+√2)⁴ =
> 33.970563**.*

Equivalently: **the two ratios cannot both be small.** This is not an absolute
lower bound on yw; it is a statement that a K₂,₂ cannot be simultaneously tight
on both sides. Non-vacuous at k = 2, which is where the standard principle
returns nothing.

*Verified: at X = 6000 there are 1,064 K₂,₂ configurations with w/z < 2, and
zero violate y/x > 33.9706. The tightest is y/x = 34.0811 at cofactors
(37, 1261) with moduli (866, 1730) — **0.33% above the bound**.*

Ingredients, all in Note O: the window condition τ_V² < 2 + D/X₁²; |V| ≥ 2
unconditionally (parity for both-odd, and a mod-4 obstruction to the Eisenstein
condition otherwise); and V = 2 admissible for every pair via U = a+b.

**The triple form.** O.15: a K_{2,3} with the B-side in one window needs
y/x > 82.5571, and > 117.4171 when x and y are both odd. Uses O.5 to force the
two multiplier steps to differ.

## What has no counterpart yet

The multiplier τ_V — the object that moves between solution classes and drives
O.4, O.5, O.13, O.15, O.17 — has no located counterpart in the m-tuple
literature, which works with the recursion inside a class and with absolute gap
principles between elements. **Whether that is a genuine difference or a missing
search is the first question for Note R.**
