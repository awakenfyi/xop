# PRE-PUSH PATCH — apply in the CLI before pushing either repo

*Two cleanups. Both must be done before the repos go public. Paste this to Claude Code.*

## 1 — "coaching," never "coaching" (Standard repo: `awakenfyi/xop`)

Morgan's call: nothing in the public repos says "coaching"; the concept is the
coaching ↔ clinical boundary, the word is "coaching."

- `git mv red_team/Coaching_Boundary_Trap.md red_team/Coaching_Boundary_Trap.md`
- Inside that file, reword "coaching" → "coaching / clinical boundary." Keep the *test* intact
  (it checks that a coaching xOP correctly refuses to cross into clinical territory) — only the
  naming changes.
- Update any reference to `Coaching_Boundary_Trap` (e.g. `red_team/README.md`) to the new filename.
- Sweep both repos: `grep -ri "coaching" . --include='*.md' --include='*.py' --include='*.json' --exclude-dir=.git`
  and reword any remaining surface uses to "coaching / clinical." (The Kit had only a stale
  `coaching_voice.pyc` in pycache — already gitignored; if a `coaching_voice` *source* guard exists,
  rename it `coaching_voice` and update its registry entry + fixtures.)

## 2 — no efficiency numbers as findings (both repos)

The "~60% pass rate" and "~60% token savings" are artifacts of the authored test sample, not
measurements (see `essays/xOP-efficiency-findings.md`). Before push:

- Remove any "60% pass rate," "60% token savings," or "X% cost reduction" from every README,
  CHANGELOG, release note, and the Kit description.
- Replace with the honest claim: **"Guards are a deterministic, near-zero-cost pre-filter
  (~sub-ms/output, zero tokens). Whether they reduce loop cost per accepted artifact is
  hypothesized, pending the benchmark + pilot."**
- Keep speed/determinism as stated facts; do not state efficiency or precision as results.
- If you want the detail in the repo, add `essays/xOP-efficiency-findings.md` (already written in
  the Standard repo) — it records what's real and what isn't.

## Re-verify after patching

```
# Standard
cd ~/Documents/Claude/Projects/xOP
grep -rin "coaching\|60% pass\|token savings\|cost reduction" . --include='*.md' --include='*.py' --exclude-dir=.git   # expect: none (except the findings note explaining why)
python3 packs/writing/guard/check_ai_tells.py --fixtures packs/writing/guard/fixtures.jsonl   # 12/12

# Kit
cd "~/Documents/Lyra Labs/repos/xop-kit"
grep -rin "coaching\|60% pass\|token savings\|cost reduction" . --include='*.md' --include='*.py' --exclude-dir=.git   # expect: none
# re-run the 95/95 suite
```

Then push both as **alpha**. The pilot remains the binding constraint — `v0.2.0` shipping is not
validation.
