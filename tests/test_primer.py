"""The primer must be small enough to be DELIVERED, and must not duplicate CLAUDE.md.

`tools/session_primer.py` runs as a SessionStart hook and returns its text in
hookSpecificOutput.additionalContext.  A hook that returns too much is not
delivered: the host truncates it to a ~2 kB preview and writes the rest to a file
that nothing reads.  That happened -- measured at 51.3 kB, and by the time it was
noticed the primer had grown to 66 kB -- because the primer reproduced CLAUDE.md's
"Where things stand" section verbatim, and CLAUDE.md is already injected into
every session as project instructions.

The failure was silent in the worst direction: the hook exited 0, printed valid
JSON, and delivered almost nothing.  These tests are the guard, and the last one
verifies the guard can actually fail rather than passing vacuously.
"""

import json
import re
import subprocess
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parent.parent
PRIMER = REPO / "tools" / "session_primer.py"

#: Comfortably under the size at which delivery was observed to fail (51.3 kB),
#: and large enough for the live material to grow.  Lower is better: every byte
#: is spent before any work starts.
BUDGET = 20_000


def _context() -> str:
    r = subprocess.run([sys.executable, str(PRIMER)], cwd=REPO,
                       capture_output=True, text=True, encoding="utf-8", timeout=120)
    assert r.returncode == 0, r.stderr[:2000]
    return json.loads(r.stdout)["hookSpecificOutput"]["additionalContext"]


def _state_section() -> str:
    text = (REPO / "CLAUDE.md").read_text(encoding="utf-8")
    start = text.index("## Where things stand")
    rest = text[start:]
    nxt = re.search(r"\n## ", rest[1:])
    return rest[: nxt.start() + 1] if nxt else rest


def test_primer_runs_and_emits_valid_hook_json():
    ctx = _context()
    assert ctx.strip(), "primer produced empty context"
    assert "x2plus1-research" in ctx


def test_primer_is_small_enough_to_be_delivered():
    n = len(_context())
    assert n <= BUDGET, (
        f"primer context is {n:,} chars, over the {BUDGET:,} budget. A SessionStart "
        "hook this large is truncated to a preview and spilled to a file, so it "
        "delivers nothing. Shrink it -- do not raise the budget without checking "
        "the host actually delivers the larger payload."
    )


def test_primer_indexes_the_state_section_rather_than_copying_it():
    """CLAUDE.md is already in context; reproducing it is pure waste."""
    ctx = _context()
    section = _state_section()
    # a distinctive run of prose from the middle of the section
    middle = re.sub(r"\s+", " ", section[len(section) // 2: len(section) // 2 + 300]).strip()
    probe = middle[50:200]
    assert probe, "could not build a probe from the state section"
    flat_ctx = re.sub(r"\s+", " ", ctx)
    assert probe not in flat_ctx, (
        "the primer is reproducing CLAUDE.md's state section verbatim. That text is "
        "already injected as project instructions, so this is the same content twice "
        "in one context -- and it is what pushed the hook past the delivery limit."
    )


def test_primer_index_is_derived_from_claude_md_not_hardcoded():
    """It must read the file, so it cannot drift -- that part of the design was right."""
    ctx = _context()
    section = _state_section()
    paras = [p.strip() for p in re.split(r"\n\s*\n", section) if p.strip().startswith("**")]
    assert paras, "no bold-led paragraphs in the state section"
    first = re.sub(r"\s+", " ", paras[0].replace("**", "").replace("*", "")).strip()[:60]
    assert first in re.sub(r"\s+", " ", ctx), (
        "the primer's index does not match CLAUDE.md's first state paragraph, so it is "
        "not being read from the file"
    )
    assert f"{len(paras)} paragraphs" in ctx or str(len(paras)) in ctx


def test_primer_carries_the_live_material_claude_md_cannot():
    """The primer's whole value-add is what a static file cannot hold."""
    ctx = _context()
    for marker in ("CLAIM REGISTRY", "RECENT COMMITS", "UNCOMMITTED", "OPEN [VERIFY] MARKERS"):
        assert marker in ctx, f"primer lost its live section: {marker}"
    assert "REFUTED (do not re-assert)" in ctx or "refuted" in ctx


def test_the_size_guard_can_actually_fail():
    """Injected violation: the guard is not verified until it has failed on one.

    Reconstructs what the primer used to emit -- its live material plus the state
    section verbatim -- and asserts THAT would breach the budget. If this ever
    passes, the budget has been raised to the point of being decorative.
    """
    would_be = len(_context()) + len(_state_section())
    assert would_be > BUDGET, (
        "the old verbatim-copy behaviour would NOT breach the budget, so the budget "
        "no longer detects the defect it exists for"
    )
