# CLI runbook — get the xOP repos in order (for Claude Code)

*Paste this to Claude Code, or point it here. Decisions are made; this is execution.
Work top to bottom. The guardrails at the end are not optional — they're the whole point
of the project, and the failure mode to avoid is declaring victory before the pilot runs.*

---

## Context — two repos, two products (not a conflict)

| | Standard | Kit |
|---|---|---|
| Path | `~/Documents/Claude/Projects/xOP` | `~/Documents/Lyra Labs/repos/xop-framework` |
| GitHub | `awakenfyi/xop` | not pushed yet |
| Is | the contract: spec, catalog, failures, positioning, 1 Guard (`no-ai-tells`, 12/12), harness scaffold, stance scorers | the reference implementation: 7 Guards, `base.py`, `xop` CLI, 95/95 fixtures, harness scaffold |
| Gate validated? | **NO — pilot unrun** | **NO — pilot unrun** |

These are two of the four products in `meta/APPROACH.md` (Standard · **Kit** · Conformance · Lyra).

## RULING (TASK 0, resolved)

**Two repos, not a merge.** The Standard stays `awakenfyi/xop`. The Kit ships as a **separate**
repo, **renamed `awakenfyi/xop-kit`** (not "xop-framework" — "framework" re-muddles the
Standard/tool line that `APPROACH.md` exists to keep). Cross-link them. Reason: the Standard must
stand alone and be implementable by anyone — not become "the framework's docs folder."

---

## PHASE 1 — finalize the Standard repo (`awakenfyi/xop`)

1. **Confirm the tree is clean.**
   - `git ls-files | grep -i PERSONAL_IMPERSONAL` → must be empty (the consciousness construct is
     quarantined in `_private/`, gitignored — keep it that way).
   - `git check-ignore "XOP WEIGHTS 3.2/" _private/ v1.1/ gem_gpt_test/` → all must report ignored.
2. **Salvage the keepers** out of the gitignored `XOP WEIGHTS 3.2/` into the spine, then leave the
   rest (the `lyra *.zip` files, the TRIBE PDF) ignored:
   - `_TEMPLATE.md`, `SKILL.md` → repo root (or `standard/`) — the authoring front door
   - `stance_scorers.py`, `stance_report.py` → `harness/`
   - `AOP-02-evidence-caution.SCORED.md` → `catalog/`
   - `keyword_flag_demo.py` → `harness/` (it's the "villain" baseline)
3. **Write index stubs:** `catalog/README.md` (lists the xOPs + badges) and `packs/README.md`
   (lists Work Packs).
4. **Resolve the dangling link:** `essays/xOPs-Make-Loops-Efficient.md` points at
   `xOPs-Missing-Harness-Primitive.md` — either write that architecture doc or remove the pointer.
5. **Verify runnable:**
   - `cd packs/writing/guard && python3 check_ai_tells.py --fixtures fixtures.jsonl` → 12/12
   - `cd harness && python3 run_harness.py` → runs; `always_abstain` passes gate, fails floor
6. **Review + commit** the already-modified tracked files (`README.md`, `PLAN.md`, `REPO_STATE.md`,
   `AGENTS.md`, `verify.sh`, `examples/coaching_cop/*`) and the reorg. One clean commit.

## PHASE 2 — prep the Kit repo (`xop-framework` → `xop-kit`)

1. **Rename** the dir/repo to `xop-kit`. In `setup.py`: fix `name`, and fix the URL
   `lyra-labs/xop-framework` → `awakenfyi/xop-kit`.
2. **Add the MIT `LICENSE` file** (org standard).
3. **Add the repo-state honesty note to the Kit README — highest priority.** Mirror the one in the
   Standard's benchmark essay:
   > *Seven Guards are deterministic and rule-tested (95/95). That tests Guard determinism — NOT
   > whether the gate holds. `fp_on_warranted == 0` has never been validated against blind human
   > labels. The pilot has not run. This is the executor for a standard whose central claim is
   > still unproven. Alpha.*
4. **Align vocabulary to the Standard's locked terms.** Deterministic Guard findings may stay
   PASS/FAIL (they're mechanical). But anywhere the Kit expresses the *warrant* judgment, use
   `warranted · inherited · undecidable` and "the gate" — never "guardrail/filter." No two
   vocabularies for the same concept across the two repos.
5. **Run the full suite** → confirm 95/95 actually passes on the current machine (don't take the
   number on faith — re-run it, clean).
6. Add the four-product framing + a pointer to the Standard.

## PHASE 3 — reconcile the duplicate Guard

There are now two `no-ai-tells`: the Kit's (one of its seven) and the Standard's
`packs/writing/guard/` (12/12). **Make one canonical** so they can't drift:
- The Kit's Guard engine is canonical. Diff the two; fold any improvement from the cowork version in.
- In the Standard repo, `packs/writing/` either (a) imports/points at the Kit's Guard, or (b) keeps
  the standalone script as the *Work Pack example* with a note that the Kit is the engine. Pick one.

## PHASE 4 — cross-link + push (alpha)

1. Standard `README`: add "Reference implementation: `awakenfyi/xop-kit`."
2. Kit `README`: "Implements the xOP Standard: `awakenfyi/xop`."
3. Confirm **neither repo's "what exists" overclaims** — both say one/seven Guards honestly, both
   say the gate is unvalidated.
4. Push both as **alpha**.

---

## Guardrails (carry the discipline — do not skip)

- **well-formed ≠ valid.** The Kit's 95/95 proves the Guards are deterministic. It does **not**
  prove the gate holds. Do not let the README imply otherwise.
- **The pilot is the binding constraint.** ≥2 independent humans labeling blind,
  `fp_on_warranted == 0`, un-pooled axes. Until it runs, everything is well-formed, not valid.
  "v0.2.0 ships" is **not** "validated."
- **No metaphysics in either public repo.** No "witness," consciousness, residual-as-soul. The
  quarantined file stays in `_private/`.
- **Don't declare victory.** Honest alpha with a clear README is the bar — that's correct. A
  polished CLI wrapped around an unvalidated gate that *reads* as finished is the exact failure
  this standard exists to catch. Ship it honest, not impressive.

## "In order" — acceptance checklist

- [ ] Standard: clean tree, keepers salvaged, `catalog/` + `packs/` indexes, guard 12/12 + harness run, dangling link resolved, one clean commit
- [ ] Kit: renamed to `xop-kit`, `setup.py` URL → `awakenfyi`, MIT LICENSE present, repo-state note in README, vocab aligned, 95/95 re-verified
- [ ] One canonical `no-ai-tells`
- [ ] Both READMEs cross-linked; neither claims the gate is validated
- [ ] Both pushed as alpha

*The pilot is the next thing after this, and the only thing that turns the Kit from a tested engine
into a validated detector. It is the work no CLI run can do for you.*
