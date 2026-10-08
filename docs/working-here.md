# Working in this repository

Every claim carries an enforced epistemic status, and the test suite checks it. The method rules, each with the evidence behind it, are in [`notes/note-P-method.md`](../notes/note-P-method.md).

## Run

```bash
python -m pip install -e ".[dev]"
python -m pytest -q                   # before trusting any measurement
python tools/smoke_experiments.py     # after changing x2plus1/: all experiments, small
python tools/check_sources.py         # which source PDFs are scans
python experiments/expNN_*.py [size]  # each takes a size and prints a table (output gitignored)
```

CI runs the tests on Python 3.11, 3.12 and 3.13, and the experiments once.

## The claim registry

`research_state/claims.json` is the state of the research, and `tests/test_claims.py` enforces what each status requires. A finding that is not in the registry has not been made; a change that produces a number adds or amends a claim.

| status | requires | means |
|---|---|---|
| `proved` | `proof_site`: a note and a test | proved here |
| `quoted` | `citation` with a page or result locator | verbatim from a source |
| `rigorous_finite` | `experiment` naming the script | exact over a stated finite range |
| `extrapolated` | `experiment` and `notes` | a law fitted from finite data |
| `inferred` | `notes` saying what is missing | reasoning, not reading or proof |
| `hypothesis` | | proposed; screen it against the no-go rules |
| `refuted` | `superseded_by` | kept so it cannot be re-asserted |

Screen a route before proposing it: `from x2plus1.claims import screen; screen("...")`. No-go rules match wording as well as tags. `green-tao-excluded` is non-fatal: contested by Green–Sawhney, so re-argue it.

## What a good change looks like

- Numbers come with the script that produces them: the `experiment` field names something runnable, and running it shows the number.
- State the population before the percentage. Coverage over a set that cannot host the configuration is vacuous.
- A bounded search proves nothing outside its bound, and never licenses removing a caution.
- Corrections reach the statement, not only the notes. After correcting a value, grep for the old one and for the retracted claim.
- Quote sources with a locator. A literature exponent is never asserted from memory: mark it `inferred` and say what is missing.
- `DFI-equidistribution.pdf` is the only scanned source: rasterise its pages (`pymupdf.open(pdf)[idx].get_pixmap(dpi=300)`; page index n is article page n+422), since its OCR mangles displayed mathematics.

## How changes land

`master` carries a ruleset: a pull request merges only when all four CI checks are green (`tests (py3.11)`, `tests (py3.12)`, `tests (py3.13)`, `experiments run`). Force-pushes and branch deletion are blocked. Merges are squash-only and the branch is deleted afterwards; each commit message says what changed and, where it matters, what was wrong before.

## Code conventions

- Exact integer arithmetic in Z[i]: int pairs, never `complex`. Floats appear only in reported statistics.
- Ideals are named by their unit-normalised generator (`unit_normalize`: Re > 0, Im ≥ 0). Never key a dict on a non-normalised Gaussian integer.
- Bulk work goes through the progression sieve in `factorization.py`, not per-value `factorint`: divisibility in this sequence is a congruence.
- A new numerically checkable claim gets a test in `tests/test_arithmetic_facts.py`.
- No scipy: `typeII.Sparse` is a hand-rolled CSR, and the dependencies stay at sympy and numpy.
- Write the convention where the symbol is defined.

## Domain notes

- The invariant is M·D: a·m = X²+D and b·m = Y²+D give aY² − bX² = M·D. Every Note O formula written with M is its D = 1 form; `notes/note-O-tau-multiplier.md` tables which downstream formulas take the D.
- Note L's ε (automorph) moves within an orbit; Note O's τ (multiplier) moves between orbits. At (1,41): ε² = 1.679×10⁷ against τ₁² = 1.877.
- The modulus ratio is τ², not τ. A window is ratio < 2, never a power-of-two-anchored interval: [8,16) and [16,32) between them miss (9,17).
- Adversarial β and β = μ are different computations: `typeII.worst_case_signs` and `typeII.mobius_bilinear`.
- Generate candidates from the realised side: enumerate occupied configurations and read off which multiplier explains them.

## Licence of contributions

Code is MIT, written material is CC BY 4.0, and a contribution is offered under the same terms. See [`LICENSE`](../LICENSE) and [`LICENSE-notes.md`](../LICENSE-notes.md).
