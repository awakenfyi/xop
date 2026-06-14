# REPO_STATE — what's real, what's scaffold, what's missing

*The honesty manifest. A reviewer should never have to guess which parts are built and which are
promised. This file is the map; it stays accurate or it gets deleted.*

## Built and runnable
- **Harness scorer** (`harness/run_harness.py`) — computes the gate, the coverage floor, abstain
  rates, per-class confusion, and the canonical status line. No pooled score. **Runs today.**
- **Baselines** (`harness/detectors.py`) — `always_abstain`, `lexical_floor`, and the
  `oracle_upper_bound` reference (not a detector).
- **Gold pipeline** (`harness/phase1/`) — generate → label (blind) → reconcile → agreement. Runs
  end to end on a 13-case scaffold.
- **Constitution, Governance, Plan, Spec, README** — consolidated and consistent.
- **AGENTS.md, CONCEPTS.md, SCORECARD.md, PIPELINE.md** — the agent-facing spine (Printing-Press
  style): operating guide, locked vocabulary, the two-tier xOP scorecard, and the build pipeline.
  `CONCEPTS.md` §2a records the canonical **`license → warrant`** ruling.
- **failures/** — three documented blind spots. **red_team/** — seven attacks as PENDING tests.
- **Flagship reference xOP** — `examples/refusal_license/` (procedure + illustrative examples +
  unlabeled gold candidates + failure pointers).

## Scaffold (honest, not yet real)
- **The gold set is 13 template cases, not a benchmark.** `gold_license` is produced by a *scripted*
  demo (`harness/phase1/demo_*.txt`), explicitly `blind: false`. Real gold needs ≥2 independent
  humans labeling blind (`--attest-blind`), N ≥ 60. See `PLAN.md`.
- **Coverage-floor value** is a placeholder (`0.50`) until a real gold set sets it.
- **The `license → warrant` migration is decided but not executed.** `CONCEPTS.md` §2a locks the
  word and scopes the mechanical rename (`gold_license`/`license_state` → warrant; harness-verified,
  example dir-slugs and the OSS `license:` field excluded). Until run, the two words are aliases.
- **Four of the launch-five reference xOPs** (Caution, Boundary, Feedback, Closure) are named in
  `examples/README.md` but not yet authored.

## Referenced but not built (named so reviewers don't rediscover them)
- **The license judge.** The whole critical path. A blind human label stands in for it today. Seam:
  `make_llm_judge` in `harness/detectors.py`.
- **`tools/xop_builder.md`** is a spec stub, not the full paste-into-a-thread prompt.
- **`tools/builder_failures.md`** (False xOP, Hidden SOP, License Collapse, Always-Abstain xOP,
  Circular License) — listed in the builder stub, not yet written.
- **A felt-domain residual** that doesn't reduce to self-report — unsolved (`concept/03` open problems).

## Decisions a reviewer should know I made
- **Lyra/COP precursor docs** were moved to `archive/` to keep the public spine clean. Nothing was
  deleted.
- **`PATTERNS.md` ships with a hard caveat**: candidate patterns, *not* labeling guidance — to avoid
  biasing blind labelers. (This diverges from a suggestion to publish canonical patterns; the
  divergence is deliberate and explained in the file.)
- **Reference-xOP gold folders ship UNLABELED.** An xOP does not label its own eval set.
- **`Graduated_Decomposition.md` was de-duplicated** (it had been uploaded twice).
- **`ci_mode_dropped`** was added to the candidate pool so `failures/Register_Overhang_Blindness.md`
  no longer references a case that wasn't there.

## The three things that move this from architecture to evidence
1. 100 blind-labeled cases. 2. Judge v1 that passes the gate and clears the floor. 3. One external
contributor who builds a compatible xOP. (`PLAN.md`.)
