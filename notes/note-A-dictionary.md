# Note A — Dictionary

*Plan §1.3.1. Status: draft. Every statement here is machine-checked in
[`tests/test_arithmetic_facts.py`](../tests/test_arithmetic_facts.py) unless
marked otherwise.*

## The translation

x² + 1 = N(x + i), where N(a + bi) = a² + b². So the sifted set is

> **A = { x + i : 1 ≤ x ≤ X } ⊂ Z[i]**, with X = √Q for norm bound Q.

Landau's fourth problem asks whether A contains infinitely many Gaussian
integers of prime norm — i.e. whether the horizontal line Im z = 1 carries
infinitely many Gaussian primes.

|A| = X = Q^{1/2}. This is the density figure in the plan's status paragraph:
counted by norm, A is a Q^{1/2}-dense subset of Z[i].

## Arithmetic of Z[i]

- Units: {±1, ±i}. Z[i] is Euclidean, hence a PID and a UFD.
- **p = 2 ramifies**: 2 = −i(1+i)², N(1+i) = 2.
- **p ≡ 1 (mod 4) splits**: (p) = (π)(π̄), N(π) = p.
- **p ≡ 3 (mod 4) is inert**: (p) is prime, N(p) = p².

Ideals are named by their unit-normalised generator (Re > 0, Im ≥ 0).

## Which ideals can divide an element of A

Call d **admissible** if d | x + i for some x.

1. **No p ≡ 3 (mod 4) divides x² + 1**, since −1 is a non-residue mod such p.
   So no inert prime, and no rational prime at all, divides any x + i: if
   p | x + i then p | (x+i) − (x−i) = 2i, forcing p = 2 — and 2 = −i(1+i)²
   with (1+i)² ∤ x+i by the next item.
2. **v₂(x² + 1) = 1 for odd x, 0 for even x** (x odd ⇒ x² ≡ 1 mod 8). Hence
   v_{(1+i)}(x + i) ≤ 1.
3. **Exactly one of π, π̄ divides x + i** when p ≡ 1 (mod 4) divides x² + 1,
   and its exponent is v_p(x² + 1) — because N(π) = p, so the π-valuation of
   x+i equals the p-valuation of its norm.

So d is admissible ⟺ N(d) = q is divisible by neither 4 nor any prime
≡ 3 (mod 4) ⟺ r² + 1 ≡ 0 (mod q) is soluble.

## The key structural fact

> **d | x + i ⟺ x ≡ r_d (mod N(d))** for a single residue r_d, namely the root
> of r² + 1 ≡ 0 mod N(d) corresponding to d.

Admissible ideals of norm q are in bijection with the roots of r² + 1 mod q.
Write ρ(q) for their number: ρ is multiplicative, ρ(2) = 1, ρ(4) = 0,
ρ(p^k) = 2 for p ≡ 1 (mod 4), ρ(p^k) = 0 for p ≡ 3 (mod 4).

**Divisibility in A is a congruence, in one class.** This one line drives
everything downstream: it makes Type I trivial *and* caps it (Note B), and it is
what makes the Type II incidence matrix a matching (Note F).

## Local densities

g(d) = 1/N(d) on admissible d, 0 otherwise. The generating Dirichlet series is

> Σ_{d admissible} N(d)^{−s} = ζ(s)·L(s, χ₄)/ζ(2s)

*(derivation: the Euler factor is (1+p^{−s})/(1−p^{−s}) at p ≡ 1 (mod 4),
1 + 2^{−s} at p = 2, and 1 at p ≡ 3 (mod 4); matching these against
ζ(s)L(s,χ₄)/ζ(2s) factor by factor.)* Residue at s = 1:

> L(1, χ₄)/ζ(2) = (π/4)/(π²/6) = **3/(2π) = 0.477465…**

so #{admissible d : N(d) ≤ D} ~ (3/2π)·D. Measured: 0.4771 at D = 64 000
(`experiments/exp01_type_i_level.py`).

## What A is *not*

A is the set of Gaussian integers on the line Im z = 1. Hecke's theorem gives
angular equidistribution of Gaussian primes, and equidistribution in sectors;
neither says anything here, because a horizontal line is not a sector.

Hecke proved, via Grössencharacters λ_k and their L-functions, that the angles
of Gaussian primes equidistribute in [0, π/2). The narrow-sector refinements
are the closest available: unconditionally Ricci reaches sectors of width
X^{−3/10+ε}, and even under GRH the limit is X^{−1/2+ε}. All of these are
statements about **sectors** — two-dimensional regions of positive measure. The
line Im z = 1 is a one-dimensional subvariety carrying ~Q^{1/2} of the ~Q
lattice points of norm ≤ Q, and no sector result, however narrow, specialises
to it. So the degeneracy is not that the region is small; it is that it is not
a region.

## Adversarial review

- *Two-parameter freedom smuggled in?* None here — A is one-parameter by
  construction, and the note never varies anything but x.
- *Where is parity broken?* Nowhere in this note. Note A is pre-sieve
  bookkeeping; it establishes that the local data is as favourable as it could
  be (g(d) = 1/N(d) exactly, no ramification pathology), which is precisely why
  the obstruction cannot be local.

## Open

- **[VERIFY]** The narrow-sector figures (Ricci's X^{−3/10+ε}; X^{−1/2+ε} under
  GRH) are from a literature search, not from reading the sources. They are
  context, not load-bearing — no line of this repo's argument rests on them.
- The nearest genuinely relevant result is *On Gaussian primes in sparse sets*
  ([arXiv:2302.11331](https://arxiv.org/abs/2302.11331)): primes a² + b² with
  b confined to a set of size X^{1/2−δ}. Our problem is that set having **one**
  element. Unread — see [Note C](note-C-requirements.md)'s Open list.
