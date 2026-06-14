# The COP Specification — v0.1

**A COP (Coaching / Conscious Operating Procedure) is a portable, model-agnostic reflective procedure.**
It runs in any model, loads into any thread, and sits inside any coaching-adjacent surface.
It optimizes for *honest reflection*, never for resolution.

This document defines what a COP *is* — at the same structural depth as a production
**AOP** (Agent Operating Procedure), with every component inverted from convergence to reflection.

---

## 0. Two artifacts — Source and Portable

A COP exists in two forms. Do not confuse them.

| | **COP Source** | **Portable COP** |
|---|---|---|
| What | the richly-authored procedure | the flat markdown it compiles to |
| Where | the COP Studio | any thread, model, or app |
| Depth | full (this spec) | the runnable subset |
| Analogy | source code | the compiled binary |
| Action | you *author* it | you *ship and market* it |

`Export → Portable COP` flattens Source into markdown. The depth lives in Source; the
portability lives in the export. Everything below describes **Source**.

---

## 1. Header — identity & contract

- `id` — stable slug (e.g. `inherited-stance-check`)
- `title`, `summary` (one line, the purpose)
- `version` — semver; COPs are pinned and regression-tested across model upgrades
- `author`, `license` (open by default)
- `model_agnostic: true` — must run on any frontier model
- **Contract** (machine-readable, enforced by the runtime, not the prose):
  - `optimizes_for: [pause_held, residual_surfaced, correct_abstention]`
  - `never_for: [resolution, satisfaction_score, fastest_close]`
  - `gate: false_positive_on_warranted == 0`

> *AOP analog:* agent name + metadata. **Inversion:** the contract optimizes for reflection held, not tickets resolved.

---

## 2. Intent — entry conditions

A typed, checkable predicate set. The COP only runs when it evaluates true.

- `all_of: [ … ]` / `any_of: [ … ]` — composable boolean conditions
- each condition is a short natural-language predicate the judge can evaluate
  (e.g. "intensity seems out of proportion to what's currently present")
- `confidence_threshold` — below it, the COP defers rather than fires

> *AOP analog:* scenario "Intent — use only when all conditions are met." **Inversion:** none needed; this pattern is already right.

---

## 3. Guardrails — two levels

**3a. COP-level (travels with the file).** When NOT to run; hand off instead.
- each guardrail = condition + action + `reason_code` (e.g. `clinical_referral`)
- handoff targets: human coach, licensed professional, "give the decision they asked for"

**3b. Runtime-level (enforced by the host; author cannot disable).**
- crisis detection → human routing
- clinical / legal / financial → referral
- privacy / sensitive-data minimization
- the **gate**: a warranted reaction is never softened (`false_positive_on_warranted == 0`)

> *AOP analog:* scenario "Guardrail: do not use when…" + the global Guardrails rail.
> **Inversion:** the Guardrail becomes the *safety/abstain boundary*, and runtime enforcement is mandatory because COPs are openly authored.

---

## 4. Procedure — branching reflective steps

Numbered steps, run **one at a time, never combined**. Each step is typed by *move*, not by outcome.

**Move types:** `reflect` · `ask` · `hold` · `name` · `abstain` · `handoff`

Each step carries:
- `move` (one of the above)
- `text` — what the coach does/says
- `wait: true|false` — does the coach stop and let silence sit
- `branches:` — `on_response: <condition> → goto step N | run_cop: <id> | handoff: <reason>`
- `combine: forbidden` (default) — enforces the one-move-at-a-time discipline
- cross-references to other COPs (`run_cop: surface-the-fear`) — COPs compose

> *AOP analog:* branching IF/THEN steps, "never combine steps," scenario-to-scenario references, transfer reasons.
> **Inversion:** steps are tagged to *hold* (`hold`, `name`, `abstain`), not to *advance to resolution*. There is no "continue to close."

---

## 5. Signals — what the COP tracks  *(the COP's typed fields)*

The observations a COP listens for, each typed like a custom field.

| signal | type | how collected | required |
|---|---|---|---|
| `stated_reason` | string | from the person's words | yes |
| `actual_trigger` | string | inferred, surfaced in Step | no |
| `intensity` | scale 1–5 | judged | yes |
| `license_state` | enum `warranted` \| `inherited` \| `undecidable` | derived (§7) | yes |
| `residual_surfaced` | bool | judged | yes |
| `pause_held` | bool | judged | yes |

Authors add COP-specific signals with `name` / `type` (string·number·bool·enum·object·list) / `description` / `required`.

> *AOP analog:* required parameters + the Custom Field wizard (name, description, type, scope). **Inversion:** signals are *reflective observations*, not data to collect-and-close.

---

## 6. Residual — `L = x − x̂`

Operationalized per COP:
- `x` = behavior / what's actually happening (the reaction, the choice)
- `x̂` = self-description / the stated account
- `L` = the divergence to **surface, name once, and not explain away**

The author specifies *which* x and x̂ this COP compares, and the threshold of divergence worth naming.

> *AOP analog:* none — this is Lyra-native.

---

## 7. License model

Rules that map the signals to a `license_state`:
- `warranted` → trigger still present → respect it, end. (A licensed reaction is not a defect.)
- `inherited` → trigger gone → surface as overhang.
- `undecidable` → insufficient signal → **abstain** (§8).

> *AOP analog:* none — Lyra-native (the warranted-vs-inherited distinction).

---

## 8. Abstain — gated

- trigger: `license_state == undecidable` OR ground-truth missing (§9)
- action: say so, ask for one more signal; never guess toward "you're overreacting"
- **abstaining is a correct outcome**, scored positively, never penalized
- the gate (§1) makes a false-positive on a warranted reaction a hard failure

> *AOP analog:* the closest thing is "offer to transfer," but here abstain is a first-class success state. Lyra-native.

---

## 9. Ground-truth bindings — anti-self-grading

External signals the COP must check a residual against before treating it as real:
- 360 feedback · behavioral/calendar signal · prior-session outcome · human review
- if none available → lower confidence, lean to `abstain`

> *AOP analog:* a ticket's resolution is free ground truth; coaching has none, so it must be bound explicitly. Lyra-native.

---

## 10. Tools / actions — optional, gated

If a COP uses tools (pull 360 data, schedule a follow-up):
- `http` / `client` / `mcp` tool definitions (name, params, description)
- `silent: true` by default — a tool call must not become a way to "resolve"
- tools may *inform* a reflection; they may never *close* one

> *AOP analog:* HTTP / Client / MCP tools. **Inversion:** tools are constrained so they can't pull the session toward greedy resolution.

---

## 11. Evaluation — inverted contract

- **metrics:** `pause_held %`, `residual_surfaced %`, `correct_abstention %` — never resolution or satisfaction
- **gate:** `false_positive_on_warranted == 0`, reported every run
- **test cases:** `scenario_guide`, `when_to_fail` (e.g. *"fails if the coach resolved instead of holding the pause"*), `simulations_per_run`, `allowed_tools`, `generated_from_transcript`
- **drift log (first-class events):** `stance_persisted` · `pause_collapsed` · `flattery_detected` · `abstained_correctly`
- **judge:** an LLM judge validated against **independent human labels** (never the author); where humans split, the gold answer is `abstain`
- **regression:** the same human-labeled suite re-runs on every model upgrade — does the new model still hold the pause, still abstain, still refuse to flatter

> *AOP analog:* test cases (when-to-fail, simulations, generated-from-ticket), test suite runs, experiments/traffic-split, changelog. **Inversion:** the entire target is flipped; "resolved / very satisfied" is a *failure* signal.

---

## 12. Knowledge — supporting frames (optional)

Definitions and the reflective frame a COP draws on (e.g. the source distinction the residual depends on). Attached, versioned, not spoken aloud.

> *AOP analog:* Supporting docs / Knowledge base (definitions, glossary, guides).

---

## 13. Lifecycle

`draft → human-labeled QA → 1% slice → scale`, with version pinning and the §11 regression suite at every model change. Mirrors the proven AOP "draft-to-production" pipeline, with one inserted step: **human labeling** (because reflection quality can't be read off a resolution rate).

---

## 14. Export targets

A Portable COP compiles to:
- **markdown** (the universal drop-in)
- **LiveKit Instructions** (voice/runtime, + voice output rules)
- **Claude / Cowork system prompt**
- **API payload** (for a custom runtime)

The contract (§1) and the eval (§11) do **not** survive into a bare prompt export — they require a runtime to enforce. A prompt *asks* for the behavior; only the eval layer *checks* it. That check is where the residual actually computes.

---

*COP Specification v0.1 · draft standard. The depth lives in Source; the portability lives in the export; the formula lives in the eval. Define it once, market it everywhere.*
