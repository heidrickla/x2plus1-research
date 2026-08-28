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


def test_registry_is_internally_consistent():
    problems = check(CLAIMS)
    assert problems == [], "\n".join(problems)


def test_every_claim_has_the_support_its_status_requires():
    for c in CLAIMS:
        if c.status in {Status.PROVED, Status.QUOTED, Status.MEASURED}:
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
