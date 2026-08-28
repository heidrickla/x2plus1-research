"""Print priming context for a session resumed after compaction.

Wired to a SessionStart hook with a "compact" matcher in .claude/settings.json.
Emits JSON with hookSpecificOutput.additionalContext, which Claude Code injects
back into the model's context, so a compacted session recovers the state that
matters instead of the state that happened to survive summarisation.

Everything printed is derived from files on disk, never hardcoded prose, so it
cannot drift from the repo.
"""

from __future__ import annotations

import json
import subprocess
import sys
from collections import Counter
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent


def _git(*args: str) -> str:
    try:
        return subprocess.run(
            ["git", *args], cwd=REPO, capture_output=True, text=True, timeout=10
        ).stdout.strip()
    except Exception:
        return ""


def _claims_summary() -> str:
    path = REPO / "research_state" / "claims.json"
    if not path.exists():
        return "claims.json missing"
    claims = json.loads(path.read_text(encoding="utf-8"))["claims"]
    counts = Counter(c["status"] for c in claims)
    lines = [f"{len(claims)} claims: " + ", ".join(f"{v} {k}" for k, v in sorted(counts.items()))]
    weak = [c for c in claims if c["status"] == "inferred"]
    if weak:
        lines.append("  INFERRED (load-bearing but unverified) -- treat with suspicion:")
        for c in weak:
            lines.append(f"    - {c['id']}: {c['statement'][:150]}")
    dead = [c for c in claims if c["status"] == "refuted"]
    if dead:
        lines.append("  REFUTED (do not re-assert):")
        for c in dead:
            lines.append(f"    - {c['id']} -> superseded by {c.get('superseded_by', '?')}")
    return "\n".join(lines)


def _where_things_stand() -> str:
    """The state section of CLAUDE.md, read rather than duplicated.

    This used to be hardcoded prose, and it drifted: it asserted that x^2+1
    meets DFI's Type I hypothesis for several commits after that claim became
    `refuted` in the registry. A primer that re-injects a refuted claim into
    every future session is worse than no primer, so the text now has exactly
    one home.
    """
    path = REPO / "CLAUDE.md"
    if not path.exists():
        return "(CLAUDE.md missing)"
    lines = path.read_text(encoding="utf-8").splitlines()
    try:
        start = lines.index("## Where things stand")
    except ValueError:
        return "(CLAUDE.md has no 'Where things stand' section)"
    body = []
    for line in lines[start + 1:]:
        if line.startswith("## "):
            break
        body.append(line)
    return "\n".join(body).strip()


def _open_markers() -> str:
    out = []
    for p in sorted((REPO / "notes").glob("*.md")) + sorted((REPO / "refs").glob("*.md")):
        for i, line in enumerate(p.read_text(encoding="utf-8").splitlines(), 1):
            if "[VERIFY]" in line and "discharged" not in line and "is answered" not in line:
                rel = p.relative_to(REPO).as_posix()
                out.append(f"    {rel}:{i}  {line.strip()[:130]}")
    return "\n".join(out) if out else "    (none)"


def main() -> None:
    ctx = f"""=== x2plus1-research: primed after compaction ===

PROJECT. Landau's fourth problem (infinitely many primes x^2+1), attacked via
the Friedlander-Iwaniec asymptotic sieve reformulated over Z[i]. Read README.md
and notes/README.md first; the charter is x2plus1-research-plan.md (do not edit
it without deliberate reason).

WHERE THINGS STAND (verbatim from CLAUDE.md, which is the one hand-maintained
copy -- this script does not carry its own version of it)

{_where_things_stand()}

DISCIPLINE, and this repo has burned itself twice by ignoring it:
  - research_state/claims.json records every claim with an ENFORCED status
    (proved / quoted / measured / inferred / refuted), checked by
    tests/test_claims.py. Read x2plus1/claims.py before writing a finding.
  - NEVER assert a literature exponent from memory. Quote with a page number,
    or mark the claim `inferred` and say what is missing.
  - Distinguish a hypothesis of one theorem from a property of the sequence.
  - Before proposing a route, screen it: x2plus1.claims.screen("...").

CLAIM REGISTRY
{_claims_summary()}

OPEN [VERIFY] MARKERS
{_open_markers()}

RECENT COMMITS
{_git("log", "--oneline", "-8") or "    (git unavailable)"}

UNCOMMITTED
{_git("status", "--short") or "    (clean)"}

RUN `python -m pytest -q` to confirm the harness is intact before trusting any
measurement. Experiments live in experiments/ and each names the note it feeds.
"""
    json.dump(
        {
            "hookSpecificOutput": {
                "hookEventName": "SessionStart",
                "additionalContext": ctx,
            },
            "suppressOutput": True,
        },
        sys.stdout,
    )


if __name__ == "__main__":
    main()
