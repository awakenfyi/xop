"""
reconcile.py -- merge >=2 blind label files into a gold set.

Gold rule (LABEL_PROTOCOL.md rule 3): if labelers AGREE, gold = that call. If they DISAGREE
at all, gold = 'undecidable' -- disagreement means the surface didn't settle it, which is
exactly the case the format is built to abstain on. (We treat any non-identical pair as a
split, including warranted-vs-undecidable: the conservative gold is undecidable.)

Writes gold.json (the validated set the harness scores against) and prints the split rate.

Usage:
  python reconcile.py labels_alice.json labels_bob.json [labels_carol.json ...]
"""
from __future__ import annotations
import json, os, sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
POOL = os.path.join(HERE, "candidates_pool.json")
GOLD = os.path.join(HERE, "gold.json")

LIC2TP = {"warranted": True, "inherited": False, "undecidable": "undecidable"}


def main():
    if len(sys.argv) < 3:
        sys.exit("need >=2 label files: python reconcile.py labels_a.json labels_b.json ...")
    label_files = sys.argv[1:]

    with open(POOL) as f:
        pool = {c["id"]: c for c in json.load(f)["cases"]}

    sets, ids, blind_all = [], set(), True
    for lf in label_files:
        with open(lf if os.path.isabs(lf) else os.path.join(HERE, lf)) as f:
            d = json.load(f)
        blind_all = blind_all and bool(d.get("blind"))
        sets.append((d["labeler_id"], d["labels"]))
        ids.add(d["labeler_id"])

    common = set(pool)
    for _, labels in sets:
        common &= set(labels)
    if not common:
        sys.exit("no cases labeled by all provided labelers.")

    gold_cases, split = [], 0
    for cid in sorted(common):
        calls = [labels[cid]["call"] for _, labels in sets]
        if len(set(calls)) == 1:
            gold = calls[0]
        else:
            gold = "undecidable"
            split += 1
        c = dict(pool[cid])
        c["gold_license"] = gold
        c["trigger_present_at_final"] = LIC2TP[gold]
        c["labeler_id"] = sorted(ids)
        c["blind"] = blind_all
        c["reconciled_from"] = {lid: labels[cid]["call"] for lid, labels in sets}
        gold_cases.append(c)

    out = {
        "_meta": {
            "what": "Reconciled gold set from blind labels.",
            "labelers": sorted(ids),
            "blind": blind_all,
            "n": len(gold_cases),
            "split_to_undecidable": split,
            "gold_rule": "agree -> that call; any disagreement -> undecidable.",
        },
        "cases": gold_cases,
    }
    with open(GOLD, "w") as f:
        json.dump(out, f, indent=2)

    dist = Counter(c["gold_license"] for c in gold_cases)
    print(f"reconciled {len(gold_cases)} cases from {sorted(ids)}  (blind={blind_all})")
    print(f"  gold distribution: {dict(dist)}")
    print(f"  split-to-undecidable: {split}/{len(gold_cases)}")
    if not blind_all:
        print("  WARNING: not all labelers blind -> this is a SCAFFOLD, not a benchmark.")
    print(f"  wrote {GOLD}")
    print("  next: python agreement.py " + " ".join(os.path.basename(x) for x in label_files))


if __name__ == "__main__":
    main()
