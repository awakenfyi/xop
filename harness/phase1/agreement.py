"""
agreement.py -- inter-annotator agreement, reported PER CLASS, never pooled.

LABEL_PROTOCOL.md: report agreement separately for warranted / inherited / undecidable.
The headline number is warranted-vs-inherited: if humans can't agree there, no detector
should be trusted to. A single pooled accuracy number is forbidden -- it hides the class
that matters behind an average.

Reports, for the two labelers with the most overlap (pairwise):
  - the 3x3 confusion matrix
  - Cohen's kappa (chance-corrected overall agreement, one number, clearly labeled)
  - per-class agreement (of cases where either said class C, how often both did)
  - the specific warranted<->inherited confusion count (the dangerous one)

Usage:
  python agreement.py labels_alice.json labels_bob.json [...]
"""
from __future__ import annotations
import json, os, sys
from itertools import combinations
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
CLASSES = ["warranted", "inherited", "undecidable"]


def load(lf):
    with open(lf if os.path.isabs(lf) else os.path.join(HERE, lf)) as f:
        return json.load(f)


def kappa(pairs):
    """Cohen's kappa over (a,b) call pairs."""
    n = len(pairs)
    if n == 0:
        return float("nan")
    po = sum(1 for a, b in pairs if a == b) / n
    ca, cb = defaultdict(int), defaultdict(int)
    for a, b in pairs:
        ca[a] += 1; cb[b] += 1
    pe = sum((ca[c] / n) * (cb[c] / n) for c in CLASSES)
    return 1.0 if pe == 1 else (po - pe) / (1 - pe)


def report_pair(la, lb):
    na, na_l = la["labeler_id"], la["labels"]
    nb, nb_l = lb["labeler_id"], lb["labels"]
    common = sorted(set(na_l) & set(nb_l))
    if not common:
        print(f"\n{na} vs {nb}: no overlap."); return
    pairs = [(na_l[c]["call"], nb_l[c]["call"]) for c in common]

    print("\n" + "=" * 64)
    print(f"{na} vs {nb}   (n={len(common)} overlapping cases)")
    blind = bool(la.get("blind")) and bool(lb.get("blind"))
    if not blind or na.startswith("DEMO") or nb.startswith("DEMO"):
        print("  ** FIXTURE / NON-BLIND -- tooling demo, NOT a real result **")

    # confusion matrix
    cm = defaultdict(int)
    for a, b in pairs:
        cm[(a, b)] += 1
    print("\n  confusion (rows=%s, cols=%s):" % (na, nb))
    head = "           " + "".join(f"{c[:5]:>8}" for c in CLASSES)
    print(head)
    for a in CLASSES:
        row = "".join(f"{cm[(a,c)]:>8}" for c in CLASSES)
        print(f"  {a[:9]:>9}{row}")

    # overall (clearly labeled, secondary)
    po = sum(1 for a, b in pairs if a == b) / len(pairs)
    print(f"\n  raw overall agreement: {po:.0%}  (secondary -- do not lead with this)")
    print(f"  Cohen's kappa:         {kappa(pairs):.2f}")

    # per class (the real report)
    print("\n  per-class agreement (both said C / either said C):")
    for c in CLASSES:
        either = sum(1 for a, b in pairs if a == c or b == c)
        both = sum(1 for a, b in pairs if a == c and b == c)
        frac = f"{both}/{either}" if either else "0/0"
        pct = f"{(both/either):.0%}" if either else "--"
        print(f"    {c:<12} {frac:>7}  {pct}")

    # the dangerous confusion
    wi = cm[("warranted", "inherited")] + cm[("inherited", "warranted")]
    print(f"\n  >> warranted<->inherited disagreements: {wi}  "
          f"(the number that matters most; high = the surface didn't settle it)")
    print(f"  honest status: n={len(common)} | kappa={kappa(pairs):.2f} | "
          f"w<->i splits={wi} | per-class above | NO pooled score")


def main():
    if len(sys.argv) < 3:
        sys.exit("need >=2 label files.")
    files = [load(x) for x in sys.argv[1:]]
    # report every pair; usually 2 labelers => 1 pair
    for a, b in combinations(files, 2):
        report_pair(a, b)


if __name__ == "__main__":
    main()
