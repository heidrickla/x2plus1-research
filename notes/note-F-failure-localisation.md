# Note F — Failure localisation

*Plan §2.4.2. Status: draft — the strongest result in the repo and the leading
candidate for "the exact lemma that fails". Supported by
[`exp02`](../experiments/exp02_bilinear_pilot.py),
[`exp03`](../experiments/exp03_density_ledger.py), and
`tests/test_bilinear.py::test_incidence_graph_of_the_line_is_c4_free`.*

## The single off-diagonal sum

Dispersion (plan §2.2) Cauchy–Schwarzes in m and opens the square, leaving

> Σ_{n₁ ≠ n₂} β_{n₁} β̄_{n₂} · **G(n₁, n₂)**,  G(n₁, n₂) := #{m : mn₁ ∈ A and mn₂ ∈ A}.

Everything in Step 2 comes down to G. The plan (§2.2.4–5) anticipates that G
becomes a congruence/lattice count, to be detected by additive characters and
bounded by Weil. **That is not what happens.**

## Lemma (the line admits no multiplicative coincidence)

> Let A = {x + i : x ≥ 1}. If m₁ ≁ m₂ and n₁ ≁ n₂ and all four of m₁n₁, m₁n₂,
> m₂n₁, m₂n₂ are associates of elements of A, then contradiction.
> **Hence G(n₁, n₂) ≤ 1 for all n₁ ≠ n₂.**

*Proof.* Write m_j n_k = u_{jk} a_{jk} with a_{jk} = x_{jk} + i ∈ A and u_{jk} a
unit. From m₁n₁ · m₂n₂ = m₁n₂ · m₂n₁ we get a₁a₄ = u·a₂a₃ for some unit u,
where a₁ = x₁+i, … , a₄ = x₄+i and x_j ≥ 1.

Now (x+i)(y+i) = (xy − 1) + i(x + y) has Re ≥ 0 and Im ≥ 2 for x, y ≥ 1, so
both a₁a₄ and a₂a₃ lie in the closed first quadrant with imaginary part ≥ 2.
Multiplication by i, −1, or −i moves that region to Re < 0, Im < 0, Im ≤ 0
respectively, so **u = 1**. Comparing parts,

> x₁ + x₄ = x₂ + x₃  and  x₁x₄ = x₂x₃,

so {x₁, x₄} and {x₂, x₃} are the roots of one quadratic and agree as multisets.
If x₁ = x₂ then m₁n₁ ∼ m₁n₂, so n₁ ∼ n₂; if x₁ = x₃ then m₁n₁ ∼ m₂n₁, so
m₁ ∼ m₂. Both contradict the hypothesis. ∎

Machine-checked two ways: exhaustively on a box
(`test_line_admits_no_multiplicative_coincidence`) and on the actual incidence
matrices at four dyadic splits (`test_incidence_graph_of_the_line_is_c4_free`).

## Why this is the failure

The dispersion method exists to evaluate G(n₁, n₂) as *main term + error* and
to beat the trivial bound by controlling the error. Here **G is identically 0
or 1.** There is no main term, no congruence to detect, no exponential sum to
introduce, and therefore no Weil bound to apply. Cauchy–Schwarz has thrown away
the entire saving and handed back a set of 0/1s, and the only remaining source
of cancellation is the sign pattern β_{n₁}β̄_{n₂} — which is what we were trying
to establish in the first place.

Concretely, measured at X = 2×10⁴ (`exp02`): the naïve dispersion bound comes
out at **θ = 1.00–1.03 at every split** — worse than the trivial bound. Not
"insufficient by a small exponent": it never had a saving to lose.

## The same fact from the density side

For any A ⊂ Z[i] of size |A| with norms ≍ Q, splitting a = mn with N(m) ≍ M
gives mean degrees D_m ≍ |A|/M and d_n ≍ |A|M/Q, hence

> D_m · d_n ≍ |A|²/Q =: κ,  independent of M, and max_M min(D_m, d_n) ≍ √κ.

| sequence | \|A\| | κ | √κ | predicted / measured max min-degree |
|---|---|---|---|---|
| x² + 1 | Q^{1/2} | **1** | 1 | 1 / **1.26** |
| x³ + 2y³ | Q^{2/3} | Q^{1/3} | Q^{1/6} | — |
| a² + b⁴ | Q^{3/4} | Q^{1/2} | Q^{1/4} | 48.7 / **41.2** (Q = 10⁷) |

Density Q^{1/2} is exactly the value at which κ = 1. The plan's "thinner than
anything yet handled" is not a matter of degree: **Q^{1/2} is the critical
density at which the Type II incidence matrix degenerates to a forest.**

Checked beyond the mean, since a skewed degree distribution could still hide a
thick sub-rectangle: the **(2,2)-core is empty at every split** — no subgraph
in which every row and every column has degree ≥ 2. For a² + b⁴ at the same
norm bound the maximum off-diagonal Gram entry is **667**.

> **This is the line in the ledger where the two-parameter freedom of (a, b) is
> used.** Not in Type I, not in the local densities, not in the choice of
> sieve — here, to make G(n₁, n₂) large enough to have a main term.

## The important caveat

The sieve does **not** require cancellation for adversarial β. Its Type II
hypothesis has the absolute value outside the m-sum (so α is effectively
arbitrary) but supplies **β = μ**. With β = μ the form does cancel: [Note
H](note-H-numerical-pilot.md) measures Σ_m |Σ_n μ(n)·1[mn ∈ A]| ≍ √(MX), which
is o(X) for M = o(X). So the lemma above proves:

- ✅ **dispersion cannot work here**, at any split, for a structural reason;
- ❌ **not** that the Type II hypothesis is false.

Every drop of the required saving must come from the arithmetic of μ along the
fibres, with no help whatever from the incidence geometry. That is precisely
the regime the parity barrier governs.

## Candidate problem statement

> **Question F.** Let A = {x + i : x ≤ X} and M = X^u with 0 < u < 1. Does
>
>     Σ_{N(m) ≍ M} | Σ_{n} μ(n) · 1[mn ∈ A] |  ≪_A  X (log X)^{−A}
>
> hold? Numerically the left side is ≍ √(MX) = X^{(1+u)/2}, comfortably o(X)
> for every u < 1. The content is whether this survives as a theorem given
> that G(n₁, n₂) ≤ 1, so that no bilinear/dispersion argument can reach it.

This is the inequality Step 2's checkpoint (plan §2.5) asks for, in its
cleanest form. What it still needs is the second half of the checkpoint: a
quantitative statement of how far current bounds fall short — which is
[Note G](note-G-spectral.md), and is not yet done.

## Adversarial review

- *Two-parameter freedom smuggled in?* No. The lemma uses only that elements of
  A have imaginary part exactly 1; κ uses only |A| and Q.
- *Where is parity broken?* Nowhere. This note is a negative result: it shows
  the standard parity-breaking mechanism is structurally unavailable, and does
  not supply a replacement. Do not read it as an impossibility proof.
- *Does the lemma generalise the wrong way?* It uses Im = 1 only through
  "Im(a) is the same for all a ∈ A". The same proof kills 4-cycles for
  {x + ci} for any fixed c. It fails as soon as Im varies — which is exactly
  a² + b⁴. Worth stating in that generality in the write-up.
- *Is C₄-freeness really fatal, or just fatal to* this *dispersion arrangement?*
  Open. Cauchy–Schwarz in **n** instead of m, or an unbalanced/well-factorable
  split, gives a different Gram matrix. **[VERIFY]** — the current claim is
  about the arrangement in plan §2.2, and should not be over-read.
