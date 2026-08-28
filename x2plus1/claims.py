"""A claim registry with enforced epistemic status.

Adapted from the pattern in `rh-research-engine` (`core/models.py`,
`core/nogo.py`, `docs/EPISTEMIC_BOUNDARIES.md`), whose governing rule is worth
restating here:

    A guard that is not on the path is not a guard.

So every status below is checked by `tests/test_claims.py`, not merely
documented. This module exists because of a demonstrated failure mode in this
repo: twice, a conclusion was over-read from evidence that did not support it
(first "the obstruction is Type I, not Type II", then "(R1) is soft"). Both
came from the same slip -- not distinguishing what was *measured* from what was
*proved* from what was *quoted* from what was merely *reasoned*.

The vocabulary is deliberately not interchangeable:

    PROVED           proved in this repo, with a named note section AND a test
    QUOTED           quoted verbatim from a source, with a page reference
    RIGOROUS_FINITE  computed exactly over a stated finite range
    EXTRAPOLATED     an asymptotic law inferred from finite data
    INFERRED         reasoning not backed by reading, proof, or computation
    HYPOTHESIS       proposed, no support claimed
    REFUTED          shown false, kept so it cannot be silently resurrected

INFERRED is the class this repo needed and the RH engine did not have. Its
whole point is that an inferred claim looks exactly like a quoted one in prose,
which is how a plausible chain of reasoning gets promoted to a finding.

RIGOROUS_FINITE vs EXTRAPOLATED splits what was one MEASURED class, after the
rh-research-engine session pointed at its `rigorous_numerical` rung: *rigorous
about what it covers, and what it covers is always finite.* The two are not
comparable evidence. "The maximum off-diagonal Gram entry is 1 for every m at
X = 8000" is an exact integer computation -- it settles a finite question
completely. "rho ~ (log X)^c with c = 0.00 +- 0.04" is a fit, and fits are how
a finite observation becomes an asymptotic claim without anyone deciding to
promote it. Collapsing them is the same error as collapsing INFERRED into
QUOTED, one level down.
"""

from __future__ import annotations

import json
import re
from dataclasses import dataclass, field
from enum import StrEnum
from pathlib import Path

REGISTRY_PATH = Path(__file__).resolve().parent.parent / "research_state" / "claims.json"


class Status(StrEnum):
    PROVED = "proved"
    QUOTED = "quoted"
    #: Exact over a stated finite range. Settles a finite question completely;
    #: says nothing whatever about the asymptotic.
    RIGOROUS_FINITE = "rigorous_finite"
    #: An asymptotic law fitted from finite data. The class where a finite
    #: observation quietly becomes a claim about all X.
    EXTRAPOLATED = "extrapolated"
    INFERRED = "inferred"
    HYPOTHESIS = "hypothesis"
    REFUTED = "refuted"


#: Statuses that may not be asserted without the corresponding support field.
REQUIRES_CITATION = {Status.QUOTED}
REQUIRES_EXPERIMENT = {Status.RIGOROUS_FINITE, Status.EXTRAPOLATED}
REQUIRES_PROOF_SITE = {Status.PROVED}


@dataclass
class Claim:
    id: str
    statement: str
    status: Status
    #: For QUOTED: source with page/section. Empty otherwise.
    citation: str = ""
    #: For MEASURED: the experiment or test that produced the number.
    experiment: str = ""
    #: For PROVED: where the proof is written, and the test that checks it.
    proof_site: str = ""
    depends_on: list[str] = field(default_factory=list)
    tags: set[str] = field(default_factory=set)
    notes: str = ""
    #: Set when a claim was weakened or withdrawn; kept for the record.
    superseded_by: str = ""

    def support(self) -> str:
        return self.citation or self.experiment or self.proof_site


@dataclass
class NoGoRule:
    """A route this repo has established does not work.

    Carries trigger *phrases* as well as tags, following the rh-research-engine
    comment that tag-only matching lets a refuted route be resurrected verbatim
    just by renaming its tag.
    """

    id: str
    message: str
    trigger_tags: set[str] = field(default_factory=set)
    trigger_phrases: list[str] = field(default_factory=list)
    #: False for a rule that is contested rather than settled -- it warns
    #: instead of blocking. See `green-tao-excluded`.
    fatal: bool = True
    basis: str = ""


def _normalize(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", text.casefold()).strip()


DEFAULT_NOGO_RULES = [
    NoGoRule(
        id="dispersion-at-alpha-half",
        message=(
            "Dispersion cannot work for A = {x+i}: the incidence graph is C4-free, "
            "so the Gram matrix G(n1,n2) is identically 0 or 1 and Cauchy-Schwarz "
            "has no main term to act on. Verified from both sides (in m and in n)."
        ),
        trigger_tags={"dispersion", "bilinear_cancellation"},
        trigger_phrases=[
            "dispersion method",
            "open the square",
            "cauchy-schwarz in m",
            "kloosterman sums over z[i]",
            "weil bound",
        ],
        basis="notes/note-F-failure-localisation.md (proved); notes/note-E (run)",
    ),
    NoGoRule(
        id="level-beyond-sequence-size",
        message=(
            "No Type I level D > |A| = x^{1/2} is available. Once D exceeds the "
            "number of sequence elements the admissible moduli outnumber them and "
            "sum |r_d| cannot be small. FI state the same, ASP p.1044."
        ),
        trigger_tags={"level_of_distribution", "type_i"},
        trigger_phrases=[
            "well-factorable level",
            "well-factorable weights to raise the level",
            "level of distribution beyond",
            "bombieri-vinogradov for this sequence",
            "raise the level past",
        ],
        basis="notes/note-B-type-I.md (proved); ASP p.1044 (quoted)",
    ),
    NoGoRule(
        id="well-factorable-for-the-absolute-values",
        message=(
            "CLOSED, and the earlier wording of this rule had it backwards. "
            "Well-factorable weights are NOT a route from a signed bound to an "
            "absolute-value one: every theorem in the BFI line TRADES THE ABSOLUTE "
            "VALUE AWAY to buy the level. Bombieri-Vinogradov has sup_a |.| at level "
            "1/2; BFI Theorem 10 reaches x^{4/7-eps} and Maynard Theorem 1.1 reaches "
            "x^{3/5-eps}, both with a well-factorable weight and a FIXED residue "
            "class and no absolute value. Beyond level 1/2 the literature has no "
            "absolute-value statement at all. Note J's object needs moduli to "
            "Q^{1/3-eps}, which against X = Q^{1/2} terms is level 2/3 -- exactly "
            "where only well-factorable statements exist. No improvement in the "
            "exponent reopens this."
        ),
        trigger_tags={"well_factorable", "absolute_values"},
        trigger_phrases=[
            "well-factorable decomposition",
            "absolute values over moduli",
            "signed to absolute",
        ],
        fatal=False,
        basis="Maynard arXiv:2006.07088 Thm A, 1.1, 1.2 and (1.1), read at source; notes/note-J-mobius-in-progressions.md",
    ),
    NoGoRule(
        id="asp-below-two-thirds",
        message=(
            "The Friedlander-Iwaniec asymptotic sieve as stated does not apply "
            "below A(x) = x^{2/3}: (R1) requires D > x^{2/3}, and below it the "
            "coefficient gamma(n,C) is annihilated so hypothesis (B) is vacuous."
        ),
        trigger_tags={"asymptotic_sieve", "asp"},
        trigger_phrases=[
            "apply the asymptotic sieve",
            "invoke theorem 1 of",
            "verify (b) for x^2+1",
        ],
        basis="ASP pp.1043,1045 (quoted); notes/note-C-requirements.md",
    ),
    NoGoRule(
        id="sector-equidistribution",
        message=(
            "Sector equidistribution of Gaussian primes (Hecke, and narrow-sector "
            "refinements) says nothing about Im z = 1: sectors are two-dimensional "
            "regions, the line is a one-dimensional subvariety."
        ),
        trigger_tags={"hecke_sectors"},
        trigger_phrases=["equidistribution in sectors", "narrow sector", "hecke grossencharacter"],
        basis="notes/note-A-dictionary.md",
    ),
    NoGoRule(
        id="grh-substitute-for-type-ii",
        message=(
            "GRH and zero-density results control primes in progressions, not in a "
            "sparse sequence; they do not substitute for Type II. (Plan, Cross-cutting.)"
        ),
        trigger_tags={"grh"},
        trigger_phrases=["assume grh", "zero density", "generalized riemann hypothesis"],
        basis="x2plus1-research-plan.md, Cross-cutting",
    ),
    NoGoRule(
        id="quoting-a-scanned-text-layer",
        message=(
            "Do not record a claim as `quoted` from a scanned PDF's extracted text. "
            "Exactly one source here is a scan -- Duke-Friedlander-Iwaniec -- and its OCR "
            "renders prose correctly while mangling displayed mathematics, which is the "
            "worst possible failure mode: it looks readable. Two claims were committed and "
            "refuted in one day from it. Run `python tools/check_sources.py`, then read the "
            "page images (pymupdf, 300 dpi; DFI page index n renders article page n + 422)."
        ),
        trigger_tags={"scanned_source"},
        trigger_phrases=[
            "extract_text",
            "from the ocr",
            "the scan says",
            "pypdf reader",
        ],
        fatal=False,
        basis="tools/check_sources.py; refs/literature-log.md 2026-08-28",
    ),
    NoGoRule(
        id="green-tao-excluded",
        message=(
            "CONTESTED, not settled. The plan excludes Green-Tao / nilsequence "
            "methods as out of scope for single-variable polynomials. Green-Sawhney "
            "(arXiv:2410.04189) obtain a Type II estimate over Q(i) using exactly "
            "that toolkit. Their sequence is two-variable with alpha = 1, so the "
            "exclusion is still defensible -- but re-argue it before relying on it."
        ),
        trigger_tags={"green_tao", "nilsequence", "gowers_norm"},
        trigger_phrases=["gowers norm", "nilsequence", "inverse theorem", "concatenation theorem"],
        fatal=False,
        basis="x2plus1-research-plan.md vs arXiv:2410.04189",
    ),
]


def violations(claim: Claim, rules: list[NoGoRule] | None = None) -> list[NoGoRule]:
    """Rules this claim trips, by tag *or* by wording."""
    rules = DEFAULT_NOGO_RULES if rules is None else rules
    haystack = _normalize(" ".join([claim.statement, claim.notes]))
    hits = []
    for rule in rules:
        if rule.trigger_tags & claim.tags:
            hits.append(rule)
        elif any(_normalize(p) in haystack for p in rule.trigger_phrases):
            hits.append(rule)
    return hits


def load(path: Path | None = None) -> list[Claim]:
    raw = json.loads((path or REGISTRY_PATH).read_text(encoding="utf-8"))
    return [
        Claim(
            id=c["id"],
            statement=c["statement"],
            status=Status(c["status"]),
            citation=c.get("citation", ""),
            experiment=c.get("experiment", ""),
            proof_site=c.get("proof_site", ""),
            depends_on=c.get("depends_on", []),
            tags=set(c.get("tags", [])),
            notes=c.get("notes", ""),
            superseded_by=c.get("superseded_by", ""),
        )
        for c in raw["claims"]
    ]


def check(claims: list[Claim]) -> list[str]:
    """Every enforcement rule. Returns a list of violations; empty means clean."""
    problems: list[str] = []
    ids = {c.id for c in claims}
    for c in claims:
        if c.status in REQUIRES_CITATION and not c.citation:
            problems.append(f"{c.id}: status={c.status} requires a citation")
        if c.status in REQUIRES_EXPERIMENT and not c.experiment:
            problems.append(f"{c.id}: status={c.status} requires an experiment")
        if c.status in REQUIRES_PROOF_SITE and not c.proof_site:
            problems.append(f"{c.id}: status={c.status} requires a proof_site")
        for dep in c.depends_on:
            if dep not in ids:
                problems.append(f"{c.id}: depends_on unknown claim {dep!r}")
        # A claim may not rest on something weaker than itself.
        rank = {Status.HYPOTHESIS: 0, Status.INFERRED: 1, Status.EXTRAPOLATED: 1,
                Status.RIGOROUS_FINITE: 2, Status.QUOTED: 3, Status.PROVED: 3,
                Status.REFUTED: 0}
        for dep in c.depends_on:
            d = next(x for x in claims if x.id == dep)
            if rank[c.status] > rank[d.status] and not c.superseded_by:
                problems.append(
                    f"{c.id} ({c.status}) depends on {d.id} ({d.status}), which is weaker"
                )
        # No-go rules block *proposals*, not records of the finding. A claim
        # stating "dispersion cannot work here" is the no-go, not a breach of
        # it; only a HYPOTHESIS is proposing to go that way.
        if c.status is Status.HYPOTHESIS:
            for rule in violations(c):
                if rule.fatal:
                    problems.append(
                        f"{c.id}: proposes a route ruled out by {rule.id!r} -- {rule.message}"
                    )
    return problems


def screen(statement: str, tags: set[str] | None = None) -> list[NoGoRule]:
    """Screen a proposed route before writing it down.

    Intended use is at the point a new idea is being considered:

        >>> [r.id for r in screen("open the square and bound by the Weil bound")]
        ['dispersion-at-alpha-half']

    A non-fatal hit is a warning to re-argue, not a block.
    """
    return violations(Claim(id="<proposal>", statement=statement,
                            status=Status.HYPOTHESIS, tags=tags or set()))
