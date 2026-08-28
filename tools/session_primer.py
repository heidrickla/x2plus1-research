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
import re
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


def _state_index() -> str:
    """An INDEX of CLAUDE.md's state section, not a copy of it.

    This used to return the section verbatim, on the reasoning that the text
    should have exactly one home and so must be read rather than hardcoded.
    Reading rather than hardcoding is right; reproducing the result was not.

    CLAUDE.md is injected into every session as project instructions -- including
    after a compaction, which is the case this hook exists for -- so the verbatim
    copy put the same ~52 kB of text into one context twice. Worse, it took the
    primer to 66 kB, and a SessionStart hook that large is not delivered: the host
    truncates it to a ~2 kB preview and spills the rest to a file nothing reads.
    Measured at this session's own start: "Output too large (51.3KB)". So the
    primer was failing at its whole job, silently, which is the direction this
    repo calls a false clean bill.

    The state therefore lives in CLAUDE.md and is already in context. What the
    primer adds is what CLAUDE.md CANNOT carry: live git state, claim counts, the
    inferred and refuted lists, open markers. This emits only the bold lead-in of
    each paragraph, so a compacted session knows what the always-loaded section
    covers and can search it -- about 2.5 kB instead of 52 kB.
    """
    path = REPO / "CLAUDE.md"
    if not path.exists():
        return "    (CLAUDE.md missing -- its 'Where things stand' is the state)"
    text = path.read_text(encoding="utf-8")
    try:
        start = text.index("## Where things stand")
    except ValueError:
        return "    (CLAUDE.md has no 'Where things stand' section)"
    rest = text[start:]
    nxt = re.search(r"\n## ", rest[1:])
    section = rest[: nxt.start() + 1] if nxt else rest
    leads = []
    for para in re.split(r"\n\s*\n", section):
        para = para.strip()
        if not para.startswith("**"):
            continue
        flat = re.sub(r"\s+", " ", para.replace("**", "").replace("*", ""))
        leads.append(flat.strip())
    if not leads:
        return "    (no bold lead-ins found -- read the section directly)"
    out = [
        "    CLAUDE.md is already in your context as project instructions.",
        f"    Its '## Where things stand' section is {len(section):,} chars and IS the state.",
        f"    Do not re-read it from disk -- search it.  Its {len(leads)} paragraphs open:",
    ]
    for i, lead in enumerate(leads, 1):
        out.append(f"      {i:>2}. {lead[:110].rstrip()}")
    return "\n".join(out)


def _open_markers() -> str:
    out = []
    # CLAUDE.md is deliberately excluded: it DEFINES the [VERIFY] convention,
    # so its own description of the rule reads as an open marker.
    sources = (sorted((REPO / "notes").glob("*.md"))
               + sorted((REPO / "refs").glob("*.md"))
               + [REPO / "README.md"])
    for p in sources:
        if not p.exists():
            continue
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

WHERE THINGS STAND -- an INDEX, because the text itself is already in your
context. CLAUDE.md is loaded as project instructions on every request, so
reproducing it here would put the same 52 kB in twice and would push this hook
past the size the host will deliver.

{_state_index()}

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
