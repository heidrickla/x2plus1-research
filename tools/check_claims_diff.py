"""Which claims differ between HEAD and the working tree, by id.

Written after three crossed attributions in one night.  Grepping the diff for
'"id"' does NOT work: an id line is context, not a changed line, so it reports
every id whose neighbour moved -- it once named seven where four had changed,
three of the phantoms belonging to the other session.  Parse both sides.

Exits non-zero when the working tree carries claims the caller did not name, so
it can gate a commit:

    python tools/check_claims_diff.py <id> [<id> ...] && git commit ...

The gate only counts if it is chained.  A check in one process followed by a
commit in the next is not on the path.
"""

import io
import json
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
PATH = "research_state/claims.json"


def _by_id(doc):
    claims = doc["claims"] if isinstance(doc, dict) else doc
    return {c["id"]: c for c in claims}


def main() -> int:
    head = subprocess.run(["git", "show", f"HEAD:{PATH}"], cwd=REPO,
                          capture_output=True, text=True, encoding="utf-8")
    h = _by_id(json.loads(head.stdout))
    w = _by_id(json.load(io.open(REPO / PATH, encoding="utf-8")))
    changed = sorted(k for k in w if k not in h or w[k] != h[k])
    removed = sorted(set(h) - set(w))
    print("changed:", changed or "(none)")
    if removed:
        print("REMOVED:", removed)
    expected = sorted(sys.argv[1:])
    if not expected:
        return 0
    unexpected = sorted((set(changed) | set(removed)) - set(expected))
    if unexpected:
        print("REFUSING -- not named on the command line:", unexpected)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
