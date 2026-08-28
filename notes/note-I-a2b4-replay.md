# Note I — a² + b⁴ replay

*Plan §2.4.5. Status: draft — the harness is calibrated against [X2Y4]
Prop. 4.1 and the structural diff is recorded.*

## What is done

`experiments/exp03_density_ledger.py` runs the identical Type II harness on
both sequences at a matched norm bound, which is the "diff against Note E line
by line" the plan asks for, at the level of incidence structure. At Q = 10⁷:

| sequence | N(m) range | rows | cols | T | D_m | d_n | min | θ(μ) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| x² + 1 | [10², 10³) | 430 | 3 251 | 3 474 | 8.08 | 1.07 | 1.07 | 0.840 |
| a² + b⁴ | [10², 10³) | 707 | 52 064 | 302 276 | 427.55 | 5.81 | 5.81 | 0.713 |
| x² + 1 | [10³, 10⁴) | 2 785 | 1 723 | 3 499 | 1.26 | 2.03 | 1.26 | 0.966 |
| a² + b⁴ | [10³, 10⁴) | 7 029 | 7 326 | 301 954 | 42.96 | 41.22 | 41.22 | 0.803 |
| x² + 1 | [10⁴, 10⁵) | 3 463 | 371 | 3 463 | 1.00 | 9.33 | 1.00 | 0.990 |
| a² + b⁴ | [10⁴, 10⁵) | 64 991 | 782 | 297 175 | 4.57 | 380.02 | 4.57 | 0.896 |

and the maximum off-diagonal Gram entry is **1** for x² + 1 against **667** for
a² + b⁴. See [Note D](note-D-comparison-ledger.md) for the ledger and
[Note F](note-F-failure-localisation.md) for the lemma behind the 1.

## Calibration against FI's proved bound — done

The plan's actual requirement was to "confirm reproduction of the
Friedlander–Iwaniec Type II bound", because a harness that cannot see a known
theorem is worthless as a verdict on x² + 1. [X2Y4] Prop. 4.1 (p. 963) proves

> B(x; N) ≪ A(x)(log x)^{4−A}  for  x^{1/4+η} < N < x^{1/2}(log x)^{−B},

with N the size of n. In this harness's variable that is N(m) ∈ (Q^{1/2},
Q^{3/4}). Measuring S_μ/|A| at Q = 10⁷, where that window is (3 162, 177 828):

| N(m) | in FI's range? | a² + b⁴ | x² + 1 |
|---:|---|---:|---:|
| ~3 162 | ✅ | **0.16** | 0.84 |
| ~31 623 | ✅ | **0.52** | 1.01 |
| ~316 228 | ✗ | 1.09 | 1.05 |
| ~3 162 278 | ✗ | 1.33 | 1.08 |

**The harness sees cancellation exactly where FI prove it, and only there.**
Inside the window a² + b⁴ drops to 0.16–0.52 while x² + 1 sits at 0.84–1.01;
outside it, both saturate. That is the calibration, and it is the reason to
take the x² + 1 column seriously.

**What it does not show.** FI prove a saving of (log x)^{4−A} for *every* A.
Measured ratios of 0.16 and 0.52 are nothing like that — at Q = 10⁷,
(log Q)^{-1} ≈ 0.06 already. So this confirms the harness resolves the
*direction* of the difference, not the magnitude of FI's bound, and it cannot:
a log-power saving is invisible over one decade. Treat the table as a sanity
check that the instrument is pointed the right way, not as numerical evidence
for Prop. 4.1.

## Still not done

- [ ] The same run at a norm bound large enough for exponents to separate from
      log-factor noise. Q = 10⁷ gives |A| ≈ 1.5×10⁵ for a² + b⁴; the
      bottleneck is below.
- [ ] A line-by-line diff of the *dispersion bookkeeping* (plan §2.4.5), as
      opposed to the incidence statistics compared here. [Note
      E](note-E-naive-dispersion.md) records that the x² + 1 run dies at step 1,
      so the diff is short on one side, but it should still be written out.

## Performance note

`a2b4_sequence` factors each element individually and is the bottleneck
(≈7 s at Q = 10⁷ for ≈150 000 elements). Reaching Q = 10⁹ needs the per-b
progression sieve extended to produce Gaussian factorisations directly, the way
`gauss_factor_x_plus_i` does for the line.

## Adversarial review

- *Two-parameter freedom smuggled in?* Not applicable — this note exists to
  measure it.
- *Where is parity broken?* In FI's argument, at the Type II bound. The
  calibration above is the repo's only independent check that its harness can
  see the difference parity-breaking makes — it can, in direction. That check
  is what licenses [Note F](note-F-failure-localisation.md)'s verdict on
  x² + 1; without it the C₄-free lemma would be a fact about a matrix nobody
  had shown was the right matrix.
