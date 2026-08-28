"""Enforcement for the claim registry.

Adapted from rh-research-engine's rule that a guard not on the path is not a
guard. These tests are the path: they check that every claim's declared status
is actually backed by the thing that status requires, and that the files and
tests named in support fields exist.
"""

import re
from pathlib import Path

import pytest

from x2plus1.claims import (
    DEFAULT_NOGO_RULES, REGISTRY_PATH, Status, check, load, screen,
)

REPO = Path(__file__).resolve().parent.parent
CLAIMS = load()
NOTE_FILES = sorted((REPO / "notes").glob("*.md"))

# ENUMERATION FLOORS.  Every check below iterates CLAIMS or NOTE_FILES, and an
# enumerating guard can succeed at covering nothing and report PASS -- a wrong
# path, a parse that yields [], a glob that matches no files.  A one-file check
# cannot scan nothing; an enumerating one can.  So the enumeration needs a floor
# that would be absurd at zero.
#
# Deliberately well below the true counts, so they bound the failure mode without
# needing maintenance on every addition.  Both were verified to FIRE by setting
# them above the true count once, before being trusted.
assert len(CLAIMS) >= 100, f"only {len(CLAIMS)} claims loaded -- the registry did not load"
assert len(NOTE_FILES) >= 12, f"only {len(NOTE_FILES)} notes found -- wrong path?"


def test_registry_is_internally_consistent():
    problems = check(CLAIMS)
    assert problems == [], "\n".join(problems)


def test_every_claim_has_the_support_its_status_requires():
    for c in CLAIMS:
        if c.status in {Status.PROVED, Status.QUOTED, Status.RIGOROUS_FINITE,
                        Status.EXTRAPOLATED}:
            assert c.support(), f"{c.id} claims {c.status} with no support field"


@pytest.mark.parametrize("claim", [c for c in CLAIMS if c.proof_site or c.experiment],
                         ids=lambda c: c.id)
def test_support_paths_exist(claim):
    """A proof_site or experiment naming a file must name a file that exists."""
    for token in re.split(r"[;,]\s*", claim.proof_site or claim.experiment):
        token = token.strip()
        if not token:
            continue
        path = token.split("::")[0].strip()
        if "/" in path:
            assert (REPO / path).exists(), f"{claim.id}: missing {path}"


@pytest.mark.parametrize("claim", [c for c in CLAIMS if "::" in c.proof_site],
                         ids=lambda c: c.id)
def test_named_tests_exist(claim):
    """A proof_site citing a test must cite a test that is really defined."""
    for token in re.split(r"[;,]\s*", claim.proof_site):
        if "::" not in token:
            continue
        path, name = token.strip().split("::", 1)
        source = (REPO / path).read_text(encoding="utf-8")
        assert f"def {name}(" in source, f"{claim.id}: {path} has no {name}"


@pytest.mark.parametrize("claim", [c for c in CLAIMS if c.status is Status.QUOTED],
                         ids=lambda c: c.id)
def test_quoted_claims_carry_a_locator(claim):
    """A citation without a page or result number is not a citation."""
    assert re.search(r"\bp\.?\s?\d|\bpp\.|Prop|Lemma|Theorem|§|arXiv",
                     claim.citation), f"{claim.id}: citation lacks a locator"


@pytest.mark.parametrize("claim", [c for c in CLAIMS if c.status is Status.REFUTED],
                         ids=lambda c: c.id)
def test_refuted_claims_name_what_replaced_them(claim):
    ids = {c.id for c in CLAIMS}
    assert claim.superseded_by in ids, f"{claim.id}: superseded_by is not a known claim"


def test_inferred_claims_say_they_are_inferred():
    """The hazard class must announce itself in the note field."""
    for c in CLAIMS:
        if c.status is Status.INFERRED:
            assert c.notes, f"{c.id}: inferred claims must record what is missing"


def test_extrapolated_claims_admit_the_extrapolation():
    """A fitted law must say so; that is the step nobody decides to take."""
    for c in CLAIMS:
        if c.status is Status.EXTRAPOLATED:
            assert c.notes, f"{c.id}: extrapolated claims must record what is fitted"


def test_no_claim_still_uses_the_retired_measured_status():
    """`measured` conflated exact-finite with fitted-asymptotic; it is retired."""
    raw = REGISTRY_PATH.read_text(encoding="utf-8")
    assert '"status": "measured"' not in raw


def test_nogo_rules_screen_the_routes_this_repo_ruled_out():
    assert "dispersion-at-alpha-half" in {
        r.id for r in screen("open the square and bound the Kloosterman sums over Z[i]")
    }
    assert "grh-substitute-for-type-ii" in {r.id for r in screen("assume GRH")}
    assert "level-beyond-sequence-size" in {
        r.id for r in screen("use well-factorable weights to raise the level past x^{1/2}")
    }


def test_nogo_rules_match_on_wording_not_only_tags():
    """Renaming a tag must not resurrect a refuted route."""
    hits = screen("a fresh dispersion method run, no tags attached")
    assert "dispersion-at-alpha-half" in {r.id for r in hits}


def test_contested_rules_warn_rather_than_block():
    """green-tao-excluded is contested by Green-Sawhney; it must not be fatal."""
    rule = next(r for r in DEFAULT_NOGO_RULES if r.id == "green-tao-excluded")
    assert rule.fatal is False
    assert "arXiv:2410.04189" in rule.message


def test_every_nogo_rule_cites_its_basis():
    for rule in DEFAULT_NOGO_RULES:
        assert rule.basis, f"{rule.id}: a no-go rule must say what establishes it"


def test_registry_is_stably_serialised():
    """Byte-stable, so a content hash over claims.json means something."""
    import json
    raw = REGISTRY_PATH.read_text(encoding="utf-8")
    assert json.dumps(json.loads(raw), indent=2) + "\n" == raw


@pytest.mark.parametrize("claim", [c for c in CLAIMS if c.status is Status.QUOTED],
                         ids=lambda c: c.id)
def test_quoted_claims_name_a_locator(claim):
    """A `quoted` claim must cite a page, section or numbered result.

    `REQUIRES_CITATION` only checks the field is non-empty, which let through
    "Li, as reported with Maynard ICM survey Question 21" -- a report, not a
    quotation, and the one entry in 36 that had no locator. The registry's whole
    point is that a citation and an inference read alike in prose; a citation
    without a locator is an inference wearing a citation's clothes.
    """
    pattern = (r"\bp{1,2}\.\s*\d|\bpage\b|sec(tion)?\.?\s*\d|Thm|Theorem|Lemma|"
               r"Prop|Def|Remark|Table|\(\d|footnote|abstract")
    assert re.search(pattern, claim.citation, re.I), (
        f"{claim.id}: citation names no page or result -- {claim.citation!r}"
    )


#: Backticked hyphenated tokens that are deliberately not registry ids.
_NOT_AN_ID = {"rh-research-engine"}


def _cited_ids():
    """(file, token, line) for every backticked token shaped like a claim id."""
    import re
    # Ids are not all lowercase (sqrt-MX-law, obstruction-is-type-I, asp-R1)
    # and not all have two hyphens. A lowercase-only pattern silently skipped 26
    # of 103 ids, including the most-cited one, and the guard passed vacuously
    # on an injected refuted citation until that was found.
    pattern = re.compile(r"`([A-Za-z0-9]+(?:-[A-Za-z0-9]+)+)`")
    out = []
    files = NOTE_FILES
    for extra in ("CLAUDE.md", "README.md"):
        path = REPO / extra
        if path.exists():
            files.append(path)
    for path in files:
        for i, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            for match in pattern.finditer(line):
                token = match.group(1)
                if token not in _NOT_AN_ID:
                    out.append((path, token, i))
    return out


def test_notes_cite_ids_that_exist():
    """A note citing `some-claim-id` must cite one the registry still has.

    Renaming or removing a claim leaves every note that cited it pointing at
    nothing, silently. Nothing else in the suite reads the notes, so this is the
    only link between the prose and the registry it quotes.
    """
    known = {c.id for c in CLAIMS} | {r.id for r in DEFAULT_NOGO_RULES}
    missing = [(p.name, t, n) for p, t, n in _cited_ids() if t not in known]
    assert not missing, "notes cite ids not in the registry: " + "; ".join(
        f"{f}:{n} `{t}`" for f, t, n in missing)


def test_notes_do_not_cite_refuted_claims_as_live():
    """A refuted claim may be named in a note, but not without saying so.

    The registry keeps refuted claims precisely so they cannot be silently
    re-asserted, and that guarantee stops at the registry's edge: prose citing
    `some-refuted-claim` in passing reads exactly like prose citing a live one.
    Four corrections in a single session came from a description drifting away
    from a computation that was right, so the paraphrase is where the risk is.

    A marker within two lines either side is enough -- the point is that a
    reader meets the status where they meet the claim.
    """
    refuted = {c.id for c in CLAIMS if c.status is Status.REFUTED}
    markers = ("refut", "withdraw", "supersed", "no longer", "was wrong",
               "retract", "abandon", "struck", "corrected")
    offenders = []
    for path, token, line_no in _cited_ids():
        if token not in refuted:
            continue
        lines = path.read_text(encoding="utf-8").splitlines()
        window = " ".join(lines[max(0, line_no - 3):line_no + 2]).lower()
        if not any(m in window for m in markers):
            offenders.append(f"{path.name}:{line_no} `{token}`")
    assert not offenders, (
        "refuted claims cited without a status marker nearby: " + "; ".join(offenders))


def test_retracted_wording_is_not_still_in_the_statement():
    """A note saying "an earlier version said 'X'" must not leave X in the statement.

    Notes are where a claim's history goes; the statement is what gets quoted.
    A correction that reaches only the notes has not landed -- and that happened
    twice in one session, once inside the very claim built to record the pattern.

    This checks the one part of it that is mechanical: when a note quotes the
    wording it is retracting, that wording must be gone from the statement. It
    does not catch a correction paraphrased rather than quoted, which is the
    larger half and stays a matter of discipline.
    """
    import re
    pattern = re.compile(
        r"(?:earlier version|previously|first|originally|an earlier draft)[^.]{0,80}?"
        r"(?:said|added|stated|read|claimed|carried)\s+['\"]([^'\"]{12,200})['\"]",
        re.I)
    offenders = []
    for claim in CLAIMS:
        notes = claim.notes or ""
        for retracted in pattern.findall(notes):
            needle = " ".join(retracted.split()).lower()
            haystack = " ".join(claim.statement.split()).lower()
            if needle in haystack:
                offenders.append(f"{claim.id}: statement still contains {retracted[:60]!r}")
    assert not offenders, "retracted wording left in the statement: " + "; ".join(offenders)


# Claims whose `experiment` field is prose rather than a runnable path. The
# registry says `rigorous_finite` requires "`experiment` naming the script", and
# prose names nothing runnable -- so these numbers cannot be reproduced, let
# alone at a second size, which is the whole purpose of the convention. Six
# others in the Note O area were repointed to exp21; two of those had counts that
# did NOT reproduce, precisely because no range had been stated.
#
# THIS LIST MUST ONLY SHRINK. Do not add to it: write the experiment instead.
PROSE_EXPERIMENT_FIELDS = {
    # Four came off this list when exp23 was written; the guard fired on all
    # four, which is what it is for.  What remains is refuted -- a refuted claim
    # is kept so it cannot be silently re-asserted, and reproducing numbers that
    # were wrong buys nothing.  That is a decision, not a backlog.
    "orbit-walk-covers-a-small-part-of-the-candidates",   # refuted; kept as-is
}


def _resolve_experiment(field):
    """The file an `experiment` field names, or None if it names prose."""
    head = field.split("::")[0].split(";")[0].strip()
    if " " in head:          # a sentence, not a path
        return None
    for base in ("", "tests", "experiments"):
        p = REPO / base / head if base else REPO / head
        if p.exists():
            return p
    return None


@pytest.mark.parametrize("claim", CLAIMS, ids=lambda c: c.id)
def test_experiment_field_names_a_runnable_artefact(claim):
    """A `rigorous_finite` claim must name a script, not describe one.

    'verified in-session via x2plus1.typeII.incidence' satisfies the letter of
    the status rule and none of its purpose: nothing can be rerun. This guard is
    what makes the `experiment` field mean what the registry says it means.
    """
    if not claim.experiment:
        return
    if claim.id in PROSE_EXPERIMENT_FIELDS:
        assert _resolve_experiment(claim.experiment) is None, (
            f"{claim.id} now names a runnable artefact -- remove it from "
            "PROSE_EXPERIMENT_FIELDS; that list must only shrink"
        )
        return
    assert _resolve_experiment(claim.experiment) is not None, (
        f"{claim.id}: experiment field {claim.experiment!r} names no runnable "
        "file. Write the experiment rather than describing the computation."
    )
