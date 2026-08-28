"""Which top-level bullets a prose diff adds, and whose they are.

`git commit -- <path>` scopes what git commits but cannot separate two authors
editing the same file, and `check_claims_diff.py` only works where there are ids.
On CLAUDE.md and the notes there are none, so a commit message can under-describe
its own diff -- which happened three times in one session, each time a paragraph
from the other session landing inside a commit titled for this one's work.

Usage, chained ahead of the commit exactly like the claims gate:

    python tools/check_prose_diff.py CLAUDE.md "phrase in my bullet" ... && git commit ...

It lists every `- **...**` heading the working tree adds over HEAD and exits
non-zero if any of them matches none of the phrases given. With no phrases it
just lists, so it can be run to see what is there before naming anything.
"""

import re
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent


def added_bullets(path: str) -> list[str]:
    diff = subprocess.run(["git", "diff", "--", path], cwd=REPO,
                          capture_output=True, text=True, encoding="utf-8").stdout
    out = []
    for line in diff.splitlines():
        if line.startswith("+- **"):
            m = re.match(r"\+- \*\*(.+?)(\*\*|$)", line)
            out.append((m.group(1) if m else line[3:]).strip())
    return out


def main() -> int:
    if len(sys.argv) < 2:
        print("usage: check_prose_diff.py <path> [phrase ...]")
        return 2
    args = sys.argv[1:]
    listing = "--list" in args
    args = [a for a in args if a != "--list"]
    path, phrases = args[0], args[1:]
    bullets = added_bullets(path)
    print(f"bullets added to {path}: {len(bullets)}")
    for b in bullets:
        print(f"  - {b[:88]}")
    if listing:
        return 0
    if not phrases:
        # No phrases and no --list: the gate has nothing to check against, so it
        # refuses rather than reporting. A mode with no verdict is a mode that
        # disarms the gate by accident -- which is how a collision got past it.
        if bullets:
            print("REFUSING -- no phrases given; name each bullet, or pass --list to report only")
            return 1
        return 0
    unclaimed = [b for b in bullets if not any(p.lower() in b.lower() for p in phrases)]
    if unclaimed:
        print("REFUSING -- bullets matching none of the phrases given:")
        for b in unclaimed:
            print(f"  ! {b[:88]}")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
