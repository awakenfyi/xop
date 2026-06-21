#!/usr/bin/env bash
# verify.sh — the xOP pre-publish gate. Run before any release or PR; CI runs it too.
# Deterministic, honest checks. Each gate reports separately — there is NO pooled score.
set -uo pipefail
cd "$(dirname "$0")"
PY="${PYTHON:-python3}"
command -v "$PY" >/dev/null 2>&1 || { echo "FATAL: python3 not found"; exit 2; }
FAIL=0
say() { printf "\n========== %s ==========\n" "$1"; }

# Gate 1 — rebuild the gold scaffold and run the harness (the gate, as a number)
say "Gate 1 · harness rebuild + runs clean (gate/floor reported here; enforced by Gate 2 + future judge_detector.py)"
if ( cd harness/phase1 \
      && "$PY" generate_candidates.py >/dev/null \
      && "$PY" label_cli.py --labeler alice --from demo_a.txt >/dev/null \
      && "$PY" label_cli.py --labeler bob   --from demo_b.txt >/dev/null \
      && "$PY" reconcile.py labels_alice.json labels_bob.json >/dev/null ) \
   && ( cd harness && "$PY" run_harness.py ); then
  echo "ok · harness ran (scaffold gold; baselines FAIL by design)"
else
  echo "FAIL · harness did not run clean"; FAIL=1
fi

# Gate 2 — harness invariants
say "Gate 2 · harness invariants"
if ( cd harness && "$PY" test_harness.py ); then echo "ok"; else echo "FAIL · invariants"; FAIL=1; fi

# Gate 3 — honest-status: never claim the warrant judge is built.
# Strip markdown emphasis first so "does **not** claim ... is built" reads as the negation it is.
say "Gate 3 · honest-status (judge must read as unbuilt)"
if grep -rniE "(warrant|license) judge (is|has been|'s) (now )?(built|implemented|complete|validated)" \
      --include=*.md . 2>/dev/null \
   | grep -vE "v1\.1/|gem_gpt_test/" \
   | sed -E 's/[*_`]//g' \
   | grep -viE "\bnot\b|\bno\b|un(built|validated)|isn'?t|never|stands in|does not exist|claim|must|should" ; then
  echo "FAIL · a doc claims the judge is built"; FAIL=1
else
  echo "ok · judge consistently described as unbuilt"
fi

# Gate 4 — reference integrity: internal markdown links resolve
say "Gate 4 · reference integrity (internal links resolve)"
MISS="$("$PY" - <<'PYEOF'
import os, re, glob
root = os.getcwd()
miss = []
skip = ("v1.1/", "gem_gpt_test/", ".git/")
link = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
for md in glob.glob("**/*.md", recursive=True):
    if any(md.startswith(s) or ("/"+s) in ("/"+md) for s in skip):
        continue
    base = os.path.dirname(md)
    try:
        text = open(md, encoding="utf-8").read()
    except Exception:
        continue
    for tgt in link.findall(text):
        t = tgt.strip()
        if t.startswith(("http://", "https://", "mailto:", "#")):
            continue
        t = t.split("#")[0].strip()
        if not t:
            continue
        cand = os.path.normpath(os.path.join(base, t))
        if not os.path.exists(cand) and not os.path.exists(os.path.normpath(os.path.join(root, t))):
            miss.append(f"{md} -> {tgt}")
print("\n".join(miss))
PYEOF
)"
if [ -n "$MISS" ]; then echo "FAIL · dead internal links:"; echo "$MISS"; FAIL=1; else echo "ok · all internal markdown links resolve"; fi

# (No-pooled-score is enforced structurally by run_harness.py — it never computes a pooled
#  number — which is stronger than a markdown grep. So Gate 1 is the real enforcement; no lint here.)

say "RESULT"
if [ "$FAIL" -eq 0 ]; then echo "PASS · release gate green"; exit 0; else echo "FAIL · fix the gates above"; exit 1; fi
