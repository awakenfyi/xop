# HANDOFF — get the xOP repo push-ready

*Build brief for Claude Code. Written from a Cowork session that did the safe prep.
Execute the tasks below in order. The one thing no agent can resolve — TASK 0 — needs Morgan.*

---

## How to use this brief

This repo is **content-complete but not push-ready**. The substance is here; what's left is
one open decision, a structure ratification, and hygiene. Do TASK 0 first — it gates whether
several docs are honest. Don't skip to the platform; the binding constraint (TASK 5, the pilot)
hasn't moved in seven iterations and no amount of code substitutes for it.

**The prime directive of this project, applied to you:** runnability is the warrant; no author
grades its own homework; well-formed ≠ valid. A doc that *claims* more than the repo *contains*
is the exact failure this whole standard exists to catch. Keep the docs sized to what's built.

---

## TASK 0 — RESOLVE THIS FIRST (needs Morgan, gates doc honesty)

**Does the `xOP Framework v0.2.0` — "seven Guards, 95/95 fixtures, `base.py`, `guard.run()` API,
`xop` CLI" — actually exist anywhere?**

It does **not** exist in this repo. A full-filesystem search found: **one** rule-tested Guard
(`packs/writing/guard/`, `no-ai-tells`, 12/12), the 13-case license-judge harness scaffold
(judge unbuilt), and the stance-calibration scorers. No `base.py`, no seven Guards, no CLI.

- **If it exists in another environment (gem/gpt sandbox, a separate dev repo):** bring it in,
  or point the benchmark doc at *that* repo. Then flip the "what exists" labels back.
- **If it's aspirational (most likely):** every doc must say "one Guard built, the rest
  designed." `essays/xOPs-Make-Loops-Efficient.md` is already corrected to this. Audit the rest
  (README badges, any STANDARD/benchmark prose) for the same honesty.

Until this is answered, do not publish any doc that states the v0.2.0 framework as existing.

---

## LOCKED VOCABULARY (do not drift — from `site/awaken_content_map.md`)

| Use | Locked term | Never say |
|---|---|---|
| The family | the OP family — SOP · AOP · **xOP** | "framework," "prompt library" |
| The standard | **xOP** | "xOP tool/app" |
| The concept | **warrant** — "is this stance still *warranted*?" | "license" (collides with LICENSE) |
| The three states | **warranted · inherited · undecidable** | "pass/fail," "good/bad" |
| The one rule | **the gate** — `never override a state that's still warranted` | "guardrail," "filter" |
| Credibility line | **"No model grades model. Receipts, not vibes."** | "AI-powered," "magic" |
| Lyra | "the version that doesn't perform" | — |
| xOP | "the version that doesn't resolve" | — |

Metaphysics ("witness," consciousness, residual-as-soul) stays OUT of the public spine. The
construct file has been quarantined to `_private/` (gitignored). Do not reintroduce it.

---

## CLEANUP ALREADY DONE (don't redo)

- `_private/LYRA_PERSONAL_IMPERSONAL_MODE.md` — the consciousness construct, moved out of the
  public spine (was tracked at `archive/`), now untracked + gitignored.
- `XOP WEIGHTS 3.2/` — session scratch (6 zips, the TRIBE PDF, working drafts) — gitignored so
  `git add -A` can't sweep it in. **Salvage keepers before deleting** (see below).
- `meta/APPROACH.md` — promoted from scratch; it's the decision note.
- `essays/xOPs-Make-Loops-Efficient.md` — the benchmark doc, rewritten honest (one Guard, not
  seven) with verified citations + live URLs.
- `.gitignore` already excludes `v1.1/`, `gem_gpt_test/`, `.DS_Store`, `__pycache__`.
- **Root reorg DONE (grouped folders):** spec docs → `standard/`; the two loose xOPs →
  `catalog/` (renamed `AOP-01-refusal-warrant.md`, `COP-01-coaching-warrant.md`); the writing
  Work Pack → `packs/writing/`; working docs → `meta/`; `pause.py` → `harness/`. Root now holds
  only README + community/convention files + AGENTS.md. README repo-map updated to match. Guard
  (12/12) and harness both re-verified running from new locations.

**Keepers still inside `XOP WEIGHTS 3.2/` to salvage into the spine:** `_TEMPLATE.md`,
`SKILL.md`, `STANCE_CALIBRATION_EVAL.md`, `stance_scorers.py`, `stance_report.py`,
`AOP-02-evidence-caution.SCORED.md`, `keyword_flag_demo.py`. The `lyra *.zip` archives and the
TRIBE PDF are scratch — leave gitignored or delete.

---

## TASK 1 — Make all docs consistent with TASK 0's answer

Audit README.md, STANDARD/SPECIFICATION, and any benchmark/standard prose. Every "what exists"
statement must match the repo. The honest baseline today: *contract specified · one Guard
built and RULE-TESTED · adjudication + remaining Guards designed, not implemented · gate not yet
validated (pilot unrun).*

## TASK 2 — Finish the structure (the Work-Pack model is now applied)

The decision (see `meta/APPROACH.md`): **areas are navigation, roles are bundles, the modular
xOP / Guard / Skill stays the build unit. Four products: xOP Standard · xOP Kit · xOP
Conformance · Lyra (Lyra is one of four).** The repo now uses **Work-Pack folders** —
`packs/writing/` is a self-contained `Skill + xOP + Guard + Tests` dir (matches GPT's
"installable package format"); `catalog/` holds standalone xOPs.

Remaining for this task:
- Salvage the keepers from `XOP WEIGHTS 3.2/` (`_TEMPLATE.md`, `SKILL.md`, the stance scorers,
  `AOP-02-evidence-caution.SCORED.md`) into the spine — `SKILL.md`/`_TEMPLATE.md` belong at root
  or in `standard/`; the scorers belong in `harness/`; the SCORED xOP in `catalog/`.
- Decide whether `packs/writing/` adds the **Skill** half (house-style rewrite) to complete the
  full `Skill + xOP + Guard + Tests` quartet (today it has Guard + Tests + README).
- Add a one-line index in `catalog/README.md` and `packs/README.md`.

## TASK 3 — Reconcile the badge vocabulary (one decision, apply everywhere)

Two systems are currently in the repo:
- existing: **SCORED / HELD** (for xOPs — warranted-gate badges)
- introduced this session: **DESIGNED → RULE-TESTED → HUMAN-EVALUATED → FIELD-VALIDATED**
  (an evidence ladder) + the **Guard** layer

Recommended reconciliation (minimal sprawl): keep **SCORED/HELD** for xOPs; use **RULE-TESTED**
specifically for **Guards** (deterministic, can't be SCORED/HELD since they bear no warrant);
treat the 4-rung ladder as the *evidence* ladder a SCORED claim climbs. Document the mapping in
`STANDARD.md` so a reader never sees two unexplained badge systems. (Ratify with Morgan.)

## TASK 4 — Pre-push hygiene

- Decide `pause.py` / `pause_README.md` (untracked at root) — in the spine or out? If unrelated
  scratch, gitignore or move to `_private/`.
- Review the modified-but-uncommitted tracked files (`README.md`, `PLAN.md`, `REPO_STATE.md`,
  `AGENTS.md`, `verify.sh`, the `examples/coaching_cop/*`) — confirm intended, then commit.
- `essays/xOPs-Make-Loops-Efficient.md` references a sibling `xOPs-Missing-Harness-Primitive.md`
  that doesn't exist — either write that architecture doc or remove the pointer.
- Wire CI: the repo has `verify.sh` + a `.github/` workflow. Add the Guard self-test
  (`python3 packs/writing/guard/check_ai_tells.py --fixtures …`) so the one runnable thing can't
  silently regress. Confirm the clean-room principle (test the artifact as shipped, not the
  working dir — the lesson from the v0.6 packaging break).

## TASK 5 — THE BINDING CONSTRAINT: run the pilot

Everything above is well-formed, not valid. The gate (`fp_on_warranted == 0`) has never been
measured against blind human labels. Per `APPROACH.md` and `PLAN.md`: ≥2 independent labelers,
blind, across the un-pooled tracks, on the pilot stimuli. This is the only step that converts the
whole apparatus from "asserted contracts" to "validated detector," and the only one no model can
do. Do not wrap an SDK / platform around the gate before this runs — a polished platform implies
a validity the kernel does not have.

---

## Copy / positioning checklist (the "Awaken" story)

The public narrative is already disciplined — keep it that way:
- Flagship: `archive/AWAKEN_Flagship_The_Wrong_Pass_Rate.md` (move out of `archive/` into the
  spine if it's the public story — it currently sits in archive).
- Lead with the failure (the wrong-pass-rate), not a standards lecture. The failures/ library is
  in the repo on purpose.
- "well-formed (the skill writes it) ≠ valid (the harness proves it)" stated before any result.
- One Guard is real; say so. Don't let "Lyra wrote you a great xOP" round up to "the gate works."

*Prepared during Cowork cleanup · safe prep done, structural build + pilot are yours to run.*
