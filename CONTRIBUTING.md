# Contributing

This is a research repository, so the unusual part is not the code — it is that
**every claim carries an enforced epistemic status**, and the test suite checks
it. Read this before opening a pull request; it is short.

## Run it first

```bash
python -m pip install -e ".[dev]"
python -m pytest -q                 # before trusting any measurement
python tools/smoke_experiments.py   # after changing x2plus1/
```

CI runs both on Python 3.11, 3.12 and 3.13.

## The claim registry

`research_state/claims.json` is the state of the research. Each entry has a
status, and `tests/test_claims.py` enforces what each status requires:

| status | requires |
|---|---|
| `proved` | a `proof_site` naming **both** a note and a test |
| `quoted` | a `citation` with a page or result locator |
| `rigorous_finite` | an `experiment` naming a script that reproduces the numbers |
| `extrapolated` | an experiment **and** notes |
| `inferred` | notes saying what is missing |
| `refuted` | a `superseded_by` — refuted claims are kept, not deleted |

**A finding that is not in the registry has not been made.** If your change
produces a number, add or amend a claim; the tests will tell you what the status
you chose demands.

## What a good change looks like

- **Numbers come with the script that produces them.** "Verified in-session" is
  not a citation — the `experiment` field must name something runnable, and a
  reviewer should be able to run it and find the number in the output.
- **State the population before the percentage.** Coverage over a set that cannot
  host the configuration is vacuous.
- **A bounded search proves nothing outside its bound**, and never licenses
  removing a caution.
- **Corrections reach the statement, not just the notes.** After correcting a
  value, grep for the old one *and* for the retracted claim.
- **Quote sources with a locator.** Never assert a literature exponent from
  memory; mark it `inferred` and say what is missing instead.

`CLAUDE.md` carries the full rule set, including a catalogue of how checks in
this repository have silently failed. It is written as operating instructions
rather than prose, and it is the fastest way to see what the project considers a
mistake.

## How pull requests land

`master` carries a ruleset, so a PR merges only when all four CI checks are
green: `tests (py3.11)`, `tests (py3.12)`, `tests (py3.13)`, and
`experiments run`. Force-pushes and branch deletion are blocked.

Merges are **squash-only** and the branch is deleted afterwards. The history here
is written to be read — each commit message says what changed and, where it
matters, what was wrong before — so one commit per change keeps that legible.

## Scope

The charter is `x2plus1-research-plan.md`. Steps 1 and 2 are complete — the Type
I/II obstruction is located and structural. **Step 3 is the live work**, and it
is a question in Diophantine approximation rather than sieve theory: the
incidence here is a bipartite Diophantine tuple with property BD₂(−1). See
[`notes/note-Q-dictionary.md`](notes/note-Q-dictionary.md) for the translation,
and [`notes/note-R-literature-audit.md`](notes/note-R-literature-audit.md) for
what is and is not known — **no result here has been established as new**, and
that audit gates any writing up.

Corrections to the mathematics, the literature audit especially, are welcome.

## Licence

Code is MIT, written material is CC BY 4.0. By contributing you agree your
contribution is offered under the same terms. See [`LICENSE`](LICENSE) and
[`LICENSE-notes.md`](LICENSE-notes.md).
