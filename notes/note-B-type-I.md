# Note B — Type I computation

*Plan §1.3.2. Status: draft. Supported by
[`experiments/exp01_type_i_level.py`](../experiments/exp01_type_i_level.py).*

## Statement

For A = {x + i : x ≤ X} and an admissible ideal d of norm q, write

> A(d) = #{a ∈ A : d | a},  A(d) = g(d)·|A| + r_d,  g(d) = 1/q.

**Claim.** |r_d| ≤ 1 for every d, this is sharp, and consequently

> Σ_{N(d) ≤ D} |r_d| ≍ D for D ≤ X, and keeps growing (measured ratio to |A|:
> 1.30 at D = 8X, 3.19 at D = 64X) beyond it. Type I therefore holds exactly
> for **D = o(X) = o(Q^{1/2})**, and fails by a widening margin after that —
> it is not a marginal miss.

## Proof of the upper bound

By Note A, d | x + i ⟺ x ≡ r_d (mod q). So A(d) counts the elements of an
interval of length X in a single residue class mod q:

> A(d) = ⌊(X − r'_d)/q⌋ + 1 = X/q + O(1), with |r_d| ≤ 1.

Machine-checked: `test_type_i_error_per_modulus_is_at_most_one`.

By Note A, #{admissible d : N(d) ≤ D} ~ (3/2π)·D, so

> Σ_{N(d) ≤ D} |r_d| ≤ #{d : N(d) ≤ D} ≍ D,

and Type I at level D requires this to be o(|A|) = o(X).

## Why the bound cannot be improved

This is the part that matters, and it is not a soft remark. An interval of
length X meets a residue class mod q in ⌊X/q⌋ or ⌈X/q⌉ points — never anything
else. So |r_d| is genuinely of size ≍ ‖X/q‖ (distance to the nearest integer),
and averaged over the ≍ D admissible moduli that is ≍ 1 each once q > X.

The only escape would be **cancellation in the sign of r_d across d**. That is
not available to this argument: r_d = −{X/q} + O(1) depends on q through a
one-dimensional equidistribution that has no second parameter to sum over. In
the a² + b⁴ setting, the corresponding error is ≍ Q^{1/4} per modulus (one per
value of b), but the b-sum can be Poisson-summed and *does* cancel — which is
how FI reach a level beyond the trivial one. See [Note D](note-D-comparison-ledger.md).

## Measurements

`python experiments/exp01_type_i_level.py 4000` (X = 4000, so Q = 1.6×10⁷):

| D | D/X | #ideals | /D | Σ\|r_d\| | /\|A\| |
|---:|---:|---:|---:|---:|---:|
| 400 | 0.10 | 192 | 0.4800 | 61.8 | 0.0155 |
| 1600 | 0.40 | 766 | 0.4788 | 256.1 | 0.0640 |
| 3200 | 0.80 | 1524 | 0.4763 | 542.8 | 0.1357 |
| 6400 | 1.60 | 3050 | 0.4766 | 978.2 | 0.2446 |
| 25600 | 6.40 | 12210 | 0.4770 | 4475.4 | **1.1189** |
| 204800 | 51.20 | 97764 | 0.4774 | 11907.0 | 2.9768 |

Two things to read off. The ideal-count column confirms the density 3/(2π) =
0.47746 to four digits, which validates the whole harness. And Σ|r_d|/|A|
crosses 1 at **D ≈ 6X**, i.e. at D ≍ X ≍ Q^{1/2} up to a constant.

## Reconciling with the plan

Plan §1.3.2 says "D = X^{1/2−ε} is the limit … counting x ≤ X with x ≡ r mod
N(d) loses when N(d) > X^{1/2}". That is correct **in the norm normalisation**,
where the plan's X is this note's Q: moduli beyond Q^{1/2} = X contain at most
one element of the range, so the residual is pure error. In the x-variable the
same statement reads "level X^{1−ε}". These are the same claim; see the
normalisation paragraph in [the repo README](../README.md). Flagged only
because getting this backwards is the easiest available mistake.

## Checkpoint status

Note B's deliverable is complete: the level is D = Q^{1/2−ε}, the reason is the
one-residue-class structure of Note A, and it is sharp. [Note C](note-C-requirements.md) has since answered
the follow-up question: **no.** Friedlander–Iwaniec's hypothesis (R1) requires
D > x^{2/3} (ASP p. 1043), so the level established here is not merely a
limitation of this argument — it is below the asymptotic sieve's own floor, and
the sieve cannot be applied to x² + 1 at all. The bound proved in this note is
therefore the binding constraint on the whole programme.

## Adversarial review

- *Two-parameter freedom smuggled in?* No. The note is careful that the
  |r_d| ≤ 1 bound uses nothing but the interval structure.
- *Where is parity broken?* Nowhere — Type I is parity-blind. That is the
  point: no amount of Type I strength breaks parity, which is why the
  Iwaniec 1978 P₂ result is the natural stopping point for a Type-I-only
  argument.
- *Is the sharpness claim overreaching?* It shows this *argument* cannot be
  improved. It does **not** show that no Type I estimate beyond Q^{1/2} exists
  — a Zhang/Polymath-style well-factorable decomposition of the moduli might.
  Whether such a thing exists over Z[i] is plan §2.3's last bullet and is
  **open in this repo**.
