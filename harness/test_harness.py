"""
test_harness.py -- the invariants the eval rail enforces on every PR.

This is not a unit test of arithmetic; it is a guard on the standard's mechanics. It asserts that:
  1. the GATE actually catches a gate-violating detector   (lexical_floor must have fp_warranted > 0)
  2. the COVERAGE FLOOR actually catches the empty detector (always_abstain must catch 0 inherited)
  3. the upper bound is clean                                (oracle scores perfectly)
  4. malformed detector output never becomes a commit       (it maps to undecidable, never w/i)
  5. OPTIONAL: a contributor's real judge (harness/judge_detector.py:judge) must NOT break the gate

If any of these fails, the scorer or the gate logic regressed -> the PR is blocked.

Run: python test_harness.py        (after building phase1/gold.json via the pipeline)
Exit code 0 = pass, 1 = fail. No pytest required.
"""
from __future__ import annotations
import json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import detectors as D            # noqa: E402
from run_harness import score    # noqa: E402

GOLD = os.path.join(HERE, "phase1", "gold.json")
FAILS = []


def check(name, cond):
    print(f"  [{'PASS' if cond else 'FAIL'}] {name}")
    if not cond:
        FAILS.append(name)


def main():
    if not os.path.exists(GOLD):
        sys.exit("no phase1/gold.json -- the eval rail must build it first "
                 "(generate_candidates -> label_cli --from demo_*.txt -> reconcile).")
    cases = json.load(open(GOLD))["cases"]

    aa = score(D.always_abstain, cases)
    lex = score(D.lexical_floor, cases)
    orc = score(D.oracle_upper_bound, cases)

    print("invariant checks:")
    # 1. the gate catches a gate-violating detector
    check("gate catches lexical_floor (fp_on_warranted > 0)", lex["fp_warranted"] > 0)
    # 2. the floor catches the empty detector
    check("floor catches always_abstain (inherited_caught == 0)", aa["inherited_caught"] == 0)
    check("always_abstain does NOT violate the gate (fp == 0)", aa["fp_warranted"] == 0)
    # 3. oracle is clean and complete
    check("oracle gate clean (fp == 0)", orc["fp_warranted"] == 0)
    check("oracle catches all inherited", orc["inherited_caught"] == orc["n_i"])
    # 4. malformed output never becomes a commit
    bad = score(lambda c: "garbage-not-a-class", cases)
    check("malformed detector output maps to undecidable, never a commit",
          bad["fp_warranted"] == 0 and bad["inherited_caught"] == 0)

    # 5. optional contributor judge -- the real enforcement for future PRs
    judge_path = os.path.join(HERE, "judge_detector.py")
    if os.path.exists(judge_path):
        import judge_detector  # noqa
        jm = score(judge_detector.judge, cases)
        print("\ncontributor judge (harness/judge_detector.py):")
        check("contributor judge does NOT break the gate (fp_on_warranted == 0)",
              jm["fp_warranted"] == 0)
    else:
        print("\n  (no harness/judge_detector.py -- skipping contributor-judge gate check)")

    print()
    if FAILS:
        print(f"FAILED {len(FAILS)} invariant(s): {FAILS}")
        sys.exit(1)
    print("all invariants hold.")


if __name__ == "__main__":
    main()
