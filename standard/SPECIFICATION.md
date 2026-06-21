# The xOP Specification

*The format at full depth — every component, with its AOP analog and the inversion marked.
Status: draft for review. Companion to the overview (`00`) and worked example (`01`).*

An **xOP** is a portable, model-agnostic procedure for judgment-bearing work. It runs in any
model, loads into any thread, and sits inside any reflective surface. It optimizes for **honest
surfacing**, never for resolution. This document defines it at the same structural depth as a
production **AOP**, with every component inverted from convergence to surfacing.

The format is defined **once, here.** Domains (coaching, writing, marketing, feedback,
facilitation) are *instances* of it, not separate formats. Two instances are proven in `01` and
the COP/WOP/MOP examples; the rest are derived by anyone who passes the membership test in `00`.

---

## 0. Two artifacts — Source and Portable

An xOP exists in two forms. Do not confuse them.

| | **Source** | **Portable** |
|---|---|---|
| What | the richly-authored procedure | the flat markdown it compiles to |
| Where | the authoring studio | any thread, model, or app |
| Depth | full (this spec) | the runnable subset |
| Analogy | source code | the compiled binary |
| Action | you *author* it | you *ship and market* it |

`Export → Portable` flattens Source into markdown. The depth lives in Source; the portability
lives in the export; **the contract and the eval do not survive into a bare prompt** (§11) — they
require a runtime to enforce. A prompt *asks* for the behavior; only the eval layer *checks* it.

Everything below describes **Source**.

---

## 1. Header — identity and contract

- `id` — stable slug (e.g. `withheld-feedback-surface`)
- `title`, `summary` — one line, the purpose
- `version` — semver; xOPs are pinned and regression-tested across model upgrades
- `author`, `license` (open by default)
- `model_agnostic: true` — must run on any frontier model
- **Contract** (machine-readable, enforced by the runtime, not the prose):
  - `optimizes_for: [residual_surfaced, judgment_held, correct_abstention]`
  - `never_for: [resolution, satisfaction_score, fastest_close]`
  - `gate: false_positive_on_warranted == 0`

> **AOP analog:** agent name + metadata. **Inversion:** the contract optimizes for a judgment
> surfaced, not a task resolved. **This is the most important field in the file** — it is the
> reversed arrow and the gate, made machine-readable so a runtime can enforce them rather than
> hoping the prose holds.

---

## 2. Intent — entry conditions

A typed, checkable predicate set. The xOP runs only when it evaluates true.

- `all_of: [ … ]` / `any_of: [ … ]` — composable boolean conditions
- each condition is a short natural-language predicate the judge can evaluate
- `confidence_threshold` — below it, the xOP defers rather than fires

> **AOP analog:** scenario "use only when all conditions are met." **Inversion:** none needed;
> this pattern is already right.

---

## 3. Guardrails — two levels

**3a. xOP-level (travels with the file).** When NOT to run; hand off instead.
- each guardrail = condition + action + `reason_code` (e.g. `clinical_referral`)
- handoff targets: a human, a licensed professional, or "give the determinate answer they asked
  for" (i.e. this was an SOP/AOP task, not an xOP task)

**3b. Runtime-level (enforced by the host; the author cannot disable).**
- crisis detection → human routing
- clinical / legal / financial → referral
- privacy / sensitive-data minimization
- **the gate**: a warranted state is never overridden (`false_positive_on_warranted == 0`)

> **AOP analog:** scenario "do not use when…" + the global guardrail rail. **Inversion:** the
> guardrail becomes the *safety / abstain boundary*, and runtime enforcement is **mandatory**
> because xOPs are openly authored and forked — a careless third-party xOP must not be able to
> bypass crisis handling or start flattering.

---

## 4. Procedure — branching surfacing steps

Numbered steps, run **one at a time, never combined**. Each step is typed by *move*, not by
outcome.

**Move types:** `reflect` · `ask` · `hold` · `name` · `abstain` · `handoff`

Each step carries:
- `move` (one of the above)
- `text` — what the agent does/says
- `wait: true|false` — does the agent stop and let silence sit
- `branches:` — `on_response: <condition> → goto step N | run_xop: <id> | handoff: <reason>`
- `combine: forbidden` (default) — enforces one move at a time
- cross-references to other xOPs (`run_xop: surface-the-fear`) — xOPs compose

> **AOP analog:** branching IF/THEN steps, "never combine steps," scenario references, transfer
> reasons. **Inversion:** steps are tagged to *surface and hold* (`hold`, `name`, `abstain`),
> never to *advance to close*. There is no "continue to resolution." A branch can hand to
> another xOP; it can never hand to "resolved."

---

## 5. Signals — what the xOP tracks

The observations an xOP listens for, each typed like a custom field.

| signal | type | how collected | required |
|---|---|---|---|
| `stated_reason` | string | from the person's words | yes |
| `actual_driver` | string | inferred, surfaced in a step | no |
| `intensity` | scale 1–5 | judged | yes |
| `license_state` | enum `warranted` \| `inherited` \| `undecidable` | derived (§7) | yes |
| `residual_surfaced` | bool | judged | yes |
| `judgment_held` | bool | judged | yes |

Authors add domain-specific signals with `name` / `type` (string·number·bool·enum·object·list)
/ `description` / `required`.

> **AOP analog:** required parameters + the custom-field wizard. **Inversion:** signals are
> *observations to surface*, not data to collect-and-close.

---

## 6. Residual — `L = x − x̂`

Operationalized per xOP:
- `x` = behavior / what's actually happening
- `x̂` = self-description / the stated account
- `L` = the divergence to **surface, name once, and not explain away**

The author specifies *which* `x` and `x̂` this xOP compares, and the divergence threshold worth
naming.

> **AOP analog:** none — this is the first of the three net-new fields.
> **Observability note (see `00`):** `x` is cleanest when externally observable (prose to a cold
> reader, copy to a stranger, behavior in a log). In felt domains, `x` is inferred from report,
> so the residual is weaker and the xOP must lean on §8.

---

## 7. License model

Rules mapping the signals to a `license_state`:
- `warranted` → the triggering condition is still present → respect it, end.
  (A licensed state is **not** a defect.)
- `inherited` → the triggering condition is gone → surface as overhang.
- `undecidable` → insufficient signal → **abstain** (§8).

> **AOP analog:** none — the second net-new field. The warranted/inherited distinction is the
> single most transferable idea in the format: it is the same operation in coaching (a reaction
> outliving its trigger), writing (a rule applied where it doesn't fit), and agents (a refusal
> outliving its scope). The unifying definition: **a stance applied without present license.**

---

## 8. Abstain — gated

- trigger: `license_state == undecidable` OR ground-truth missing (§9)
- action: say so, ask for one more signal; never guess toward overriding a state
- **abstaining is a correct outcome**, scored positively, never penalized
- the gate (§1) makes a false positive on a warranted state a hard failure

> **AOP analog:** the closest thing is "offer to transfer," but here abstain is a first-class
> *success* state — the third net-new field. In felt domains it is the primary safety mechanism.

---

## 9. Ground-truth bindings — anti-self-grading

External signals an xOP must check a residual against before treating it as real:
- behavioral / calendar signal · prior-session outcome · independent feedback · human review
- if none available → lower confidence, lean to `abstain`

> **AOP analog:** a ticket's resolution is free ground truth; judgment work has none, so it must
> be bound explicitly. This is the wiring that stops an xOP from grading its own homework.

---

## 10. Tools / actions — optional, gated

If an xOP uses tools (pull a signal, schedule a follow-up):
- `http` / `client` / `mcp` definitions (name, params, description)
- `silent: true` by default — a tool call must not become a way to "resolve"
- tools may *inform* a surfacing; they may never *close* one

> **AOP analog:** HTTP / client / MCP tools. **Inversion:** tools are constrained so they can't
> pull the session toward greedy resolution.

---

## 11. Evaluation — inverted contract

- **metrics:** `residual_surfaced %`, `judgment_held %`, `correct_abstention %` — never
  resolution or satisfaction
- **gate:** `false_positive_on_warranted == 0`, reported every run
- **test cases:** `scenario_guide`, `when_to_fail` (e.g. *"fails if it resolved instead of
  holding"* / *"fails if it overrode a warranted state"*), `simulations_per_run`,
  `allowed_tools`, `generated_from_transcript`
- **drift log (first-class events):** `stance_persisted` · `pause_collapsed` ·
  `flattery_detected` · `abstained_correctly` · `warranted_override` (the gate violation)
- **judge:** an LLM judge validated against **independent human labels** (never the author);
  where humans split, the gold answer is `abstain`
- **regression:** the same human-labeled suite re-runs on every model upgrade

> **AOP analog:** test cases (when-to-fail, simulations, generated-from-transcript), suite runs,
> experiments/traffic-split, changelog. **Inversion:** the entire target is flipped — "resolved
> / very satisfied" is a *failure* signal.
>
> **Open problem (see `03`):** the judge that computes `license_state` on hard cases does not yet
> exist. Today it is stood in for by a gold human label. The format's hardest, most defensible
> piece is exactly this judge, validated against humans on its false-positives-on-warranted.

---

## 12. Frames — supporting context (optional)

Definitions and the frame an xOP draws on (e.g. the source distinction the residual depends on).
Attached, versioned, not spoken aloud.

> **AOP analog:** supporting docs / knowledge base.

---

## 13. Lifecycle

`draft → human-labeled QA → small slice → scale`, with version pinning and the §11 regression
suite at every model change. Mirrors the proven AOP draft-to-production pipeline, with one
inserted step — **human labeling** — because surfacing quality can't be read off a resolution
rate.

---

## 14. Export targets

A Portable xOP compiles to:
- **markdown** (the universal drop-in)
- **voice/runtime instructions** (+ spoken-output rules)
- **a system prompt** (for a chat surface)
- **an API payload** (for a custom runtime)

The contract (§1) and the eval (§11) require a runtime to enforce and do not survive a bare
prompt export. The prompt asks; the eval checks; **the check is where the residual actually
computes.**

---

*xOP Specification · draft for review. Same depth as a production AOP. The depth lives in
Source; the portability lives in the export; the formula lives in the eval. Defined once,
instantiated per domain.*
