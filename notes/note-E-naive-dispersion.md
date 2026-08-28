# Note E — Naïve dispersion run

*Plan §2.4.1. Status: partial — executed and the outcome recorded; the
line-by-line bookkeeping against FI is not yet written.*

## Execution of plan §2.2, steps 1–3

**Step 1, Cauchy–Schwarz in m.** |S|² ≤ ‖α‖²·Σ_m |Σ_n β_n 1[mn ∈ A]|².

**Step 2, open the square.** Σ_{n₁,n₂} β_{n₁}β̄_{n₂}·G(n₁,n₂), with
G(n₁,n₂) = #{m : mn₁ ∈ A, mn₂ ∈ A}.

**Step 3, split diagonal from off-diagonal.** Measured at X = 2×10⁴:

| N(m) range | T (= diagonal) | off-diagonal | off/diag | dispersion bound | θ |
|---:|---:|---:|---:|---:|---:|
| [10, 10²) | 24 691 | 2.29×10⁷ | 927.6 | 31 763 | 1.025 |
| [10², 10³) | 22 011 | 1.70×10⁶ | 77.19 | 27 204 | 1.021 |
| [10³, 10⁴) | 21 983 | 1.51×10⁵ | 6.854 | 27 228 | 1.021 |
| [10⁴, 10⁵) | 22 017 | 3 726 | 0.169 | 22 778 | 1.003 |

**The dispersion bound exceeds the trivial bound T at every split** (θ > 1).

## Steps 4–6 are not reached

The plan expects (§2.2.4) that "mn₁, mn₂ ∈ A becomes a congruence / lattice-point
condition on m", to be detected by additive characters and bounded by Weil
(§2.2.5), with the losses totalled against Note C (§2.2.6). None of that
happens, because by [Note F](note-F-failure-localisation.md)

> **G(n₁, n₂) ≤ 1 for every n₁ ≠ n₂** (the incidence graph is C₄-free).

There is no congruence condition to detect: the count is already 0 or 1. So
there is no exponential sum, no Weil bound, and nothing to total. **The final
exponent of the naïve run is θ ≈ 1.02 — worse than trivial — and the prediction
in the plan ("fails; determine by how much") has the answer "by everything: the
method never acquires a saving to lose."**

## Where exactly the argument dies

Step 1. Cauchy–Schwarz in m is already fatal. It discards the sign information
in α, and the resulting Gram matrix has no main term to compensate. Every later
step in §2.2 presupposes a main-term/error split of G that does not exist here.

## To do

- The line-by-line diff against the a² + b⁴ run required by plan §2.4.5 —
  that is [Note I](note-I-a2b4-replay.md).
- Try Cauchy–Schwarz in **n** instead of m, and unbalanced splits. The Gram
  matrix is then #{n : mn₁ ∈ A, mn₂ ∈ A}; by the same lemma (which is symmetric
  in m and n) it is also ≤ 1, so this is expected to fail identically — but it
  should be *run*, not assumed. **[VERIFY]**
- Well-factorable / Zhang-style splittings of m (plan §2.3, last bullet): does
  any decomposition produce a Gram matrix with a main term? The C₄-free lemma
  suggests no, since it is a statement about A itself and not about the split.

## Adversarial review

- *Two-parameter freedom smuggled in?* No — the run is honest and that is why
  it fails.
- *Where is parity broken?* Nowhere; the run never gets far enough to engage
  parity. Note that a dispersion argument that *did* work here would have had
  to break parity, so its failure is not evidence of a bug.
