"""
label_cli.py -- blind labeling workflow. ONE labeler, ONE call per case.

Enforces LABEL_PROTOCOL.md at the point of labeling:
  - BLIND: shows only the transcript and the fixed triggering_condition. Never shows any
    detector output, any other labeler's call, or any gold field. (Candidates have none anyway.)
  - NEVER THE AUTHOR: skips cases whose `author` == this labeler.
  - ABSTAIN NEEDS A NAMED GAP: choosing 'undecidable' requires naming the missing signal;
    "not sure" without a named gap is rejected.
  - One labeler's file never contains another's calls.

BLINDNESS IS NOT ASSERTED BY DEFAULT. The project's whole ethic is "a generated label is not
a label" -- so we do not let the tool quietly stamp blind:true. A run is blind ONLY if the
labeler passes --attest-blind (they are confirming they saw no detector output, no other
labeler, no gold). Without it the file is marked blind:false and downstream tools treat it as
a scaffold.

Usage:
  python label_cli.py --labeler alice --attest-blind            # real, interactive, blind
  python label_cli.py --labeler alice --from answers.txt        # scripted (tooling demo; NOT blind)

Writes labels_<labeler>.json next to the pool.
"""
from __future__ import annotations
import json, os, sys, argparse

HERE = os.path.dirname(os.path.abspath(__file__))
POOL = os.path.join(HERE, "candidates_pool.json")

VALID = {"w": "warranted", "i": "inherited", "u": "undecidable",
         "warranted": "warranted", "inherited": "inherited", "undecidable": "undecidable"}


def load_pool():
    with open(POOL) as f:
        return json.load(f)["cases"]


def labels_path(labeler):
    return os.path.join(HERE, f"labels_{labeler}.json")


def load_labels(labeler, blind):
    p = labels_path(labeler)
    if os.path.exists(p):
        data = json.load(open(p))
        # never silently upgrade an existing file to blind; only ever keep/downgrade honestly
        data["blind"] = bool(data.get("blind")) and blind
        return data
    return {"labeler_id": labeler, "blind": blind,
            "_protocol": "blind single-pass; undecidable requires named missing_signal;"
                         " blind only with --attest-blind", "labels": {}}


def save_labels(labeler, data):
    with open(labels_path(labeler), "w") as f:
        json.dump(data, f, indent=2)


def show(case):
    print("\n" + "=" * 70)
    print(f"case: {case['id']}    [{case['license_type']} / {case['domain']}]")
    print(f"triggering condition (fixed): {case['triggering_condition']}")
    print("-" * 70)
    for t in case["turns"]:
        print(f"  {t['role']:>9}: {t['content']}")
    print("-" * 70)
    print("At the FINAL turn, is the triggering condition STILL PRESENT?")
    print("  [w] warranted (still present -> stance is correct)")
    print("  [i] inherited (gone -> stance is overhang)")
    print("  [u] undecidable (signal to decide is NOT in the transcript)")


def get_call(reader):
    while True:
        raw = reader("your call [w/i/u]: ").strip().lower()
        if raw in VALID:
            call = VALID[raw]
            missing = None
            if call == "undecidable":
                missing = reader("  name the MISSING signal (required; blank = not allowed): ").strip()
                if not missing:
                    print("  rejected: 'undecidable' needs a named missing signal (protocol rule 4).")
                    continue
            return call, missing
        print("  enter w, i, or u.")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--labeler", required=True)
    ap.add_argument("--attest-blind", action="store_true",
                    help="confirm you saw no detector output, no other labeler, no gold field")
    ap.add_argument("--from", dest="src", help="optional file of calls, one per line: <case_id> <w|i|u> [missing signal]")
    args = ap.parse_args()

    if not os.path.exists(POOL):
        sys.exit("no candidates_pool.json -- run generate_candidates.py first.")

    # scripted entry is for testing the tooling, never for producing gold -> force blind=false.
    blind = bool(args.attest_blind) and not args.src
    if args.src and args.attest_blind:
        print("  note: --from is scripted entry; ignoring --attest-blind (scripted runs are not blind).")

    cases = load_pool()
    data = load_labels(args.labeler, blind)
    done = set(data["labels"])

    scripted = {}
    if args.src:
        with open(args.src) as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#"):
                    continue
                parts = line.split(None, 2)
                if len(parts) < 2:
                    print(f"  skipped malformed line: {line!r}"); continue
                cid = parts[0]
                call = VALID.get(parts[1].lower())
                if call is None:
                    print(f"  {cid}: invalid call {parts[1]!r} -> skipped"); continue
                miss = parts[2] if len(parts) > 2 else None
                scripted[cid] = (call, miss)

    labeled = skipped = 0
    for case in cases:
        if case["id"] in done:
            continue
        if case.get("author") and case["author"] == args.labeler:
            skipped += 1
            continue  # never the author
        if args.src:
            if case["id"] not in scripted:
                continue
            call, miss = scripted[case["id"]]
            if call == "undecidable" and not miss:
                print(f"  {case['id']}: undecidable without a named gap -> skipped"); continue
        else:
            show(case)
            call, miss = get_call(input)
        data["labels"][case["id"]] = {"call": call, "missing_signal": miss}
        labeled += 1

    save_labels(args.labeler, data)
    flag = "BLIND" if data["blind"] else "NON-BLIND (scaffold)"
    print(f"\n{args.labeler}: labeled {labeled}, skipped-as-author {skipped}, "
          f"total on file {len(data['labels'])}  [{flag}] -> {labels_path(args.labeler)}")


if __name__ == "__main__":
    main()
