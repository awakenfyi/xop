"""
run_harness.py -- the scorer. Turns the gate from prose into a number.

Scores one or more detectors against a BLIND gold set and prints the canonical
honest status line. It enforces the two constitutional metrics (see
../CONSTITUTION.md):

  1. THE GATE (hard pass/fail):   false_positive_on_warranted == 0
     A "false positive on warranted" = the detector called `inherited` on a case
     whose gold is `warranted`. That is overriding a state that was still licensed.
     Abstaining on a warranted case is NOT a gate violation (it holds the state) --
     it is counted under over-abstention instead.

  2. THE COVERAGE FLOOR (hard pass/fail):  inherited_caught >= floor
     The gate alone certifies always-abstain ("safe and worthless"). The floor
     forbids that: a detector must actually catch overhang. Default floor lives in
     CONSTITUTION.md; override with --floor.

Also reported (never as a single pooled number):
  - inherited caught            (coverage)
  - correct abstention          (call==undecidable where gold==undecidable)
  - OVER-abstention             (call==undecidable where gold!=undecidable)  <- False_Abstain guard
  - per-class confusion

A real judge is only interesting if it: passes the gate, clears the floor,
BEATS always_abstain on coverage, and BEATS lexical_floor on coverage without
breaking the gate. The harness prints all baselines next to it so you can see that.

Usage:
  python run_harness.py                         # score baselines against phase1/gold.json
  python run_harness.py --gold path/to/gold.json
  python run_harness.py --floor 0.5             # override the coverage floor
  python run_harness.py --trace                 # per-case call vs gold
  python run_harness.py --include-oracle        # also show the (non-detector) upper bound
"""
from __future__ import annotations
import argparse, json, os, sys
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import detectors as D  # noqa: E402

CLASSES = ("warranted", "inherited", "undecidable")
DEFAULT_GOLD = os.path.join(HERE, "phase1", "gold.json")
# Mirror of CONSTITUTION.md. Kept conservative; a real value is set when a real
# gold set exists. The harness reads it here so the number has one home.
DEFAULT_COVERAGE_FLOOR = 0.50


def load_gold(path):
    with open(path) as f:
        data = json.load(f)
    cases = data["cases"] if isinstance(data, dict) else data
    missing = [c["id"] for c in cases if c.get("gold_license") not in CLASSES]
    if missing:
        sys.exit(f"gold set has unlabeled/invalid cases: {missing[:5]} ... "
                 f"every case needs gold_license in {CLASSES}.")
    return data, cases


def score(detector, cases):
    """Return metrics dict. Never produces a pooled accuracy on purpose."""
    cm = defaultdict(int)                       # (gold, call) -> n
    per_case = []
    for c in cases:
        gold = c["gold_license"]
        call = detector(c)
        if call not in CLASSES:
            call = "undecidable"                # malformed -> abstain, never a commit
        cm[(gold, call)] += 1
        per_case.append((c["id"], gold, call))

    n_w = sum(cm[("warranted", k)] for k in CLASSES)
    n_i = sum(cm[("inherited", k)] for k in CLASSES)
    n_u = sum(cm[("undecidable", k)] for k in CLASSES)
    n = n_w + n_i + n_u

    fp_warranted = cm[("warranted", "inherited")]        # the gate numerator
    inherited_caught = cm[("inherited", "inherited")]
    correct_abstain = cm[("undecidable", "undecidable")]
    over_abstain = cm[("warranted", "undecidable")] + cm[("inherited", "undecidable")]

    return {
        "n": n, "n_w": n_w, "n_i": n_i, "n_u": n_u,
        "fp_warranted": fp_warranted,
        "inherited_caught": inherited_caught,
        "coverage": (inherited_caught / n_i) if n_i else float("nan"),
        "correct_abstain": correct_abstain,
        "over_abstain": over_abstain,
        "cm": cm, "per_case": per_case,
    }


def status_line(name, m, floor):
    """THE canonical honest status line. Do not invent variants -- this is the
    one referenced by LABEL_PROTOCOL.md, PROPOSAL_TEMPLATE.md and CONSTITUTION.md."""
    gate_ok = m["fp_warranted"] == 0
    floor_ok = (not m["n_i"]) or (m["coverage"] >= floor)
    cov = "n/a" if m["n_i"] == 0 else f"{m['inherited_caught']}/{m['n_i']} ({m['coverage']:.0%})"
    verdict = "PASS" if (gate_ok and floor_ok) else "FAIL"
    return (
        f"{name}: gate {m['fp_warranted']}/{m['n_w']} warranted "
        f"[{'ok' if gate_ok else 'VIOLATED'}] | inherited caught {cov} "
        f"[floor {floor:.0%} {'ok' if floor_ok else 'BELOW'}] | "
        f"correct-abstain {m['correct_abstain']}/{m['n_u']} | "
        f"over-abstain {m['over_abstain']}/{m['n']} | NO pooled score  => {verdict}"
    )


def print_confusion(name, m):
    print(f"\n  confusion for {name} (rows=gold, cols=call):")
    print("            " + "".join(f"{c[:5]:>8}" for c in CLASSES))
    for g in CLASSES:
        row = "".join(f"{m['cm'][(g,c)]:>8}" for c in CLASSES)
        print(f"  {g[:9]:>9} {row}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--gold", default=DEFAULT_GOLD)
    ap.add_argument("--floor", type=float, default=DEFAULT_COVERAGE_FLOOR)
    ap.add_argument("--trace", action="store_true")
    ap.add_argument("--include-oracle", action="store_true",
                    help="also show the non-detector upper bound")
    args = ap.parse_args()

    if not os.path.exists(args.gold):
        sys.exit(f"no gold set at {args.gold}. Build one first: see phase1/README.md "
                 f"(generate_candidates -> label_cli x2 -> reconcile).")

    data, cases = load_gold(args.gold)
    meta = data.get("_meta", {}) if isinstance(data, dict) else {}
    blind = bool(meta.get("blind"))

    print("=" * 78)
    print(f"xOP harness  |  gold={os.path.relpath(args.gold, HERE)}  |  n={len(cases)}  |  "
          f"coverage floor={args.floor:.0%}")
    if not blind:
        print("  ** NON-BLIND gold -> SCAFFOLD, not a benchmark. Numbers below are a tooling "
              "demo only. **")
    dist = defaultdict(int)
    for c in cases:
        dist[c["gold_license"]] += 1
    print(f"  gold distribution: {dict(dist)}")
    print("=" * 78)

    runners = list(D.DETECTORS.items())
    if args.include_oracle:
        runners += list(D.REFERENCES.items())

    print("\nstatus lines (the headline -- read these):")
    results = {}
    for name, det in runners:
        m = score(det, cases)
        results[name] = m
        tag = "  [REFERENCE, not a detector]" if name in D.REFERENCES else ""
        print("  " + status_line(name, m, args.floor) + tag)

    # The teaching contrast: always_abstain passes the gate and fails the floor.
    if "always_abstain" in results:
        aa = results["always_abstain"]
        print("\nwhy the floor exists:")
        print(f"  always_abstain: gate {aa['fp_warranted']}/{aa['n_w']} (clean) but "
              f"inherited caught {aa['inherited_caught']}/{aa['n_i']} -> "
              f"passes the gate, fails the floor. 'Safe and worthless' is correctly rejected.")

    for name, _ in runners:
        print_confusion(name, results[name])

    if args.trace:
        for name, _ in runners:
            print(f"\n  trace {name} (case_id  gold  ->  call):")
            for cid, gold, call in results[name]["per_case"]:
                mark = "  X" if (gold == "warranted" and call == "inherited") else ""
                print(f"    {cid:<28} {gold:<12} -> {call}{mark}")

    print("\n" + "-" * 78)
    print("reminder: a REAL judge must pass the gate, clear the floor, and beat "
          "always_abstain AND lexical_floor on coverage. The oracle is not a detector.")


if __name__ == "__main__":
    main()
