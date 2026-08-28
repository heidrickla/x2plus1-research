"""Run every experiment at a small size and report which ones still work.

The test suite covers `x2plus1/` thoroughly and the experiments not at all, so a
change to a library module can break a script silently. That risk is not
hypothetical: `polyseq` gained `ratio_classes`/`close_pairs`, `factorization`
gained the bulk root table, and `exp13` was refactored onto the library, all in
one session, and a separate experiment was found crashing on small inputs only
because someone ran it by hand.

Not part of pytest -- these take seconds to minutes each even at reduced sizes,
and the suite should stay fast enough to run on every edit. Run it after
changing anything in `x2plus1/`:

    python tools/smoke_experiments.py

Sizes here are deliberately far below what the notes quote. A green run means
"still executes and prints its table", not "reproduces the recorded numbers" --
several experiments need X in the thousands before their statistics mean
anything, and exp12 in particular has no data below X ~ 1000.
"""

from __future__ import annotations

import subprocess
import sys
import time
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
EXPERIMENTS = REPO / "experiments"

#: Arguments small enough to finish quickly, large enough to exercise the code.
#: Where an experiment needs a floor to produce any rows at all, the size is set
#: above it and the reason noted.
SIZES: dict[str, list[str]] = {
    "exp01_type_i_level.py": ["300"],
    "exp02_bilinear_pilot.py": ["2000"],
    "exp03_density_ledger.py": ["100000"],
    "exp04_kappa_family.py": ["100000", "3"],
    "exp05_mobius_progressions.py": ["10000"],
    "exp06_fit_robustness.py": ["10000"],
    "exp07_absolute_values.py": ["20000"],
    "exp08_merikoski_ledger.py": ["100000"],
    "exp09_degree_ladder.py": ["800", "64"],
    "exp10_second_variable.py": ["1200"],
    "exp12_tau_multiplier.py": ["1500"],   # no pairs with m >= 1000 below ~1000
    "exp13_window_gap.py": ["400"],
    "exp14_live_configurations.py": ["600"],  # ratio_classes is O(X^2)
    "exp15_cauchy_schwarz_reduction.py": ["40000"],
    "exp16_m_exponent.py": ["60000"],  # needs bands above M = 512 to fit
    "exp20_gram_mean.py": ["40000"],  # O(Q) divisor build; keep small
    "exp17_sharp_form.py": ["1200"],
    "exp18_ck_region.py": ["900"],
    "exp19_composition_bound.py": ["1200"],
    "exp21_note_O_verifications.py": ["900"],
    "exp22_sign_alternation.py": ["900"],
    "exp23_prose_claims_made_runnable.py": ["900"],
    "exp24_doubly_dyadic.py": ["600"],
}

TIMEOUT = 300


def main() -> int:
    scripts = sorted(p for p in EXPERIMENTS.glob("exp*.py"))
    if not scripts:
        print(f"no experiments found in {EXPERIMENTS}")
        return 1
    failures, skipped = [], 0
    for script in scripts:
        args = SIZES.get(script.name)
        if args is None:
            print(f"  {script.name:<34} SKIP -- no size recorded; add one to SIZES")
            skipped += 1
            continue
        t0 = time.time()
        try:
            proc = subprocess.run(
                [sys.executable, str(script), *args],
                cwd=REPO, capture_output=True, text=True, timeout=TIMEOUT,
            )
        except subprocess.TimeoutExpired:
            print(f"  {script.name:<34} TIMEOUT after {TIMEOUT}s at {' '.join(args)}")
            failures.append(script.name)
            continue
        dt = time.time() - t0
        if proc.returncode == 0:
            print(f"  {script.name:<34} ok    {dt:5.1f}s  ({' '.join(args)})")
        else:
            last = (proc.stderr.strip().splitlines() or ["(no stderr)"])[-1]
            print(f"  {script.name:<34} FAIL  {dt:5.1f}s  {last[:70]}")
            failures.append(script.name)

    print()
    if failures:
        print(f"{len(failures)} failing: {', '.join(failures)}")
        return 1
    ran = len(scripts) - skipped
    if skipped:
        print(f"{ran} of {len(scripts)} experiments run; {skipped} skipped for want of a size")
        return 1
    print(f"all {ran} experiments run")
    return 0


if __name__ == "__main__":
    sys.exit(main())
