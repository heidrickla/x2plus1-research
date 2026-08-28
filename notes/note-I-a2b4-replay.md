# Note I — a² + b⁴ replay

*Plan §2.4.5. Status: partial — the harness runs on both sequences and the
structural diff is recorded; reproduction of FI's actual Type II bound is not
done.*

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

## What is not done

The plan asks specifically to **"run the same dispersion on the a² + b⁴ set and
confirm reproduction of the Friedlander–Iwaniec Type II bound."** That is the
validation step: if the harness cannot reproduce a known result, its verdict on
x² + 1 is worth nothing. It requires:

- [ ] FI's Type II statement quoted exactly, with its M-range and its saving.
      **[VERIFY]** — the same blocking dependency as
      [Note C](note-C-requirements.md).
- [ ] The harness run at a norm bound large enough for the claimed exponent to
      show above log-factor noise. Q = 10⁷ gives |A| ≈ 1.5×10⁵, almost
      certainly too small.
- [ ] A decision on whether the harness should measure FI's *proved* saving or
      the *true* size of the sum. These differ, and only the second is
      measurable numerically.

Until that is done, treat the diff above as descriptive. It shows the two
incidence structures differ enormously, which was never in doubt; it has not
been calibrated against a known theorem.

## Performance note

`a2b4_sequence` factors each element individually and is the bottleneck
(≈7 s at Q = 10⁷ for ≈150 000 elements). Reaching Q = 10⁹ needs the per-b
progression sieve extended to produce Gaussian factorisations directly, the way
`gauss_factor_x_plus_i` does for the line.

## Adversarial review

- *Two-parameter freedom smuggled in?* Not applicable — this note exists to
  measure it.
- *Where is parity broken?* In FI's argument, at the Type II bound this note
  has not yet reproduced. Until it does, the repo has no independent check that
  its harness can see parity being broken at all — which is the main reason
  this note matters.
