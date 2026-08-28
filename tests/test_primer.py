"""CLAUDE.md must stay readable, and the primer must stay deliverable.

Both have failed in the same direction, twice.

CLAUDE.md grew to 1,601 lines / 18,657 words of narrative prose. A file that long
is not read at session start -- it is skimmed, and the compensating move is to add
indexes and pointers into it, which is the same failure one step removed. It is now
a rules-and-facts document; these tests keep it one.

tools/session_primer.py returns its text from a SessionStart hook. A hook that
returns too much is not delivered: the host truncates it to a ~2 kB preview and
spills the rest to a file nothing reads. That happened -- measured at this repo's
own session start, "Output too large (51.3KB)" -- because the primer reproduced
CLAUDE.md's state section verbatim while CLAUDE.md was already in context.

Both failures were silent: the hook exited 0 with valid JSON, and the long file
was still "loaded". Nothing reported anything.
"""

import json
import re
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
PRIMER = REPO / "tools" / "session_primer.py"
CLAUDE = REPO / "CLAUDE.md"

#: CLAUDE.md is read in full at the start of every session. Prose is what made it
#: unreadable, so the budget is in WORDS. It was 18,657; it is now ~1,400.
CLAUDE_WORD_BUDGET = 3_000

#: Comfortably under the size at which hook delivery was observed to fail (51.3 kB).
PRIMER_BUDGET = 20_000


def _context() -> str:
    r = subprocess.run([sys.executable, str(PRIMER)], cwd=REPO,
                       capture_output=True, text=True, encoding="utf-8", timeout=120)
    assert r.returncode == 0, r.stderr[:2000]
    return json.loads(r.stdout)["hookSpecificOutput"]["additionalContext"]


# --------------------------------------------------------------- CLAUDE.md

def test_claude_md_stays_short_enough_to_actually_read():
    words = len(CLAUDE.read_text(encoding="utf-8").split())
    assert words <= CLAUDE_WORD_BUDGET, (
        f"CLAUDE.md is {words:,} words, over the {CLAUDE_WORD_BUDGET:,} budget. It is "
        "read in full at every session start. It reached 18,657 words once, at which "
        "point it stopped being read and started being indexed. Cut it -- do not raise "
        "the budget."
    )


def test_claude_md_is_rules_and_facts_not_prose():
    """Narrative paragraphs are what made it unreadable. Bullets and tables are not."""
    text = CLAUDE.read_text(encoding="utf-8")
    body = [p.strip() for p in re.split(r"\n\s*\n", text) if p.strip()]
    prose = []
    for p in body:
        if p.startswith(("#", "-", "|", " ", "\t", ">")):
            continue
        if len(p.split()) > 60:          # a long free-standing paragraph
            prose.append(p[:80])
    assert not prose, (
        "CLAUDE.md has grown narrative paragraphs again: " + "; ".join(prose)
    )


# ------------------------------------------------------------------ primer

def test_primer_runs_and_emits_valid_hook_json():
    ctx = _context()
    assert ctx.strip() and "x2plus1-research" in ctx


def test_primer_is_small_enough_to_be_delivered():
    n = len(_context())
    assert n <= PRIMER_BUDGET, (
        f"primer context is {n:,} chars, over {PRIMER_BUDGET:,}. A SessionStart hook "
        "this large is truncated to a preview and spilled to a file, so it delivers "
        "nothing. Shrink it -- do not raise the budget without checking the host "
        "actually delivers the larger payload."
    )


def test_primer_does_not_reproduce_claude_md():
    """CLAUDE.md is already injected as project instructions; copying it is waste."""
    ctx, text = _context(), CLAUDE.read_text(encoding="utf-8")
    flat_ctx = re.sub(r"\s+", " ", ctx)
    body = re.sub(r"\s+", " ", text)
    probe = body[len(body) // 2: len(body) // 2 + 160]
    assert probe and probe not in flat_ctx, (
        "the primer is reproducing CLAUDE.md. That text is already in context; this is "
        "the defect that made the hook undeliverable."
    )


def test_primer_carries_the_live_material_claude_md_cannot():
    ctx = _context()
    for marker in ("CLAIM REGISTRY", "RECENT COMMITS", "UNCOMMITTED", "OPEN [VERIFY] MARKERS"):
        assert marker in ctx, f"primer lost its live section: {marker}"


def test_both_guards_can_actually_fail():
    """Injected violation: a guard is not verified until it has failed on one."""
    text = CLAUDE.read_text(encoding="utf-8")
    # the old file's word count must breach the CLAUDE.md budget
    assert 18_657 > CLAUDE_WORD_BUDGET, "the word budget no longer detects the old file"
    # the old primer behaviour -- primer plus a verbatim copy -- must breach its budget
    assert len(_context()) + len(text) * 6 > PRIMER_BUDGET, (
        "the primer budget no longer detects a verbatim copy of the state"
    )
