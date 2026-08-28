# Working notes for this repo

Research repo, not a product. The output is *notes* — code exists to keep the
notes honest.

## Non-negotiables

- **Normalisation.** Q (or N) = norm bound; X = √Q = range of x; |A| = X.
  State which one every exponent is relative to. "Level N^{1/2}" = "level X".
- **Never assert a literature exponent from memory.** The hypotheses of the
  Friedlander–Iwaniec asymptotic sieve (Annals 1998; *Opera de Cribro* Ch. 25)
  must be quoted from the source with a page reference. Unverified slots in the
  notes are marked `**[VERIFY]**` and must stay marked until checked against
  the paper. This matters more here than anywhere else in the repo: the whole
  point of Note C is that the *exact* hypothesis is what decides the problem.
- **Distinguish adversarial β from β = μ.** The sieve's Type II hypothesis has
  an absolute value outside the m-sum (so α is effectively arbitrary) but
  supplies β = μ, not an adversary. Conflating them makes the problem look
  impossible when it is merely hard. `typeII.worst_case_signs` is the former,
  `typeII.mobius_bilinear` the latter.
- **Adversarial review of every note** (plan §Cross-cutting): where is
  two-parameter freedom being smuggled in, and where is parity actually broken?

## Code conventions

- Exact integer arithmetic in Z[i] — int pairs, never `complex`. Floats appear
  only in reported statistics.
- Ideals are named by their unit-normalised generator (`unit_normalize`:
  Re > 0, Im ≥ 0). Never key a dict on a non-normalised Gaussian integer.
- Bulk work goes through the progression sieve in `factorization.py`, not
  per-value `factorint`. Divisibility in this sequence *is* a congruence; the
  code should look like the mathematics.
- New claims that can be checked numerically get a test in
  `tests/test_arithmetic_facts.py`. That file is the machine-checked version of
  Note A; if a test there fails, a note is wrong.
- No scipy. `typeII.Sparse` is a 40-line CSR; keep the dependency set at
  sympy + numpy.

## Running things

```bash
python -m pytest -q
```

Experiments take a size argument and print a table; they are meant to be read,
not imported. Each one names the note it feeds in its docstring. Results are
gitignored — rerun rather than commit output.

## Scope discipline

The plan rules these out; they stay ruled out unless the plan is amended:

- Green–Tao / nilsequence methods (single-variable polynomials are out of scope).
- GRH or zero-density substitutes for Type II (they control primes in
  progressions, not in a sparse sequence).
