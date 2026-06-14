# COP Studio — translated area-by-area from the AOP builder

**Principle:** mimic the proven framework, keep the depth, invert the target.
In a production agent builder the trustworthy part is not the prompt — it's the **harness around it**:
the code blocks, the test-case modal, the insights engine that says *which* scenario to fix and re-version.
That harness is what we copy. We just point every metric at *reflection held*, not *ticket resolved*.

Each section below: **[AOP area — what we saw]  →  [COP Studio equivalent]  →  *tuning notes.***

---

## 1. Agent definition  →  COP definition
*AOP rail: Brand · Rules · Background · Overrides*

| AOP | COP Studio | inversion |
|---|---|---|
| **Brand** (voice, identity) | **Stance** — "you hold, you don't resolve; the pause is the deliverable" | identity is reflective, not service-helpful |
| **Rules** (global behavior) | **Principles** — the six quietings, never-flatter, one-move-at-a-time | global behavior optimizes for restraint |
| **Background** (context) | **Frame** — the worldview/source-distinction the COP draws on | |
| **Overrides** | **Overrides** — per-deployment tweaks | unchanged |

---

## 2. Scenarios  →  COPs  *(the core authoring surface)*
*AOP: a scenario doc = Intent + Guardrail + branching IF/THEN steps + required params + API calls + transfer codes*

This is the deep editor. Same structure, exactly:
- **Intent** (run only when all conditions hold) — kept as-is
- **Guardrail** (do NOT run → handoff with `reason_code`) — kept, but it's now the safety/abstain boundary
- **Branching steps** — numbered, *never combine*, IF-response→goto / run-another-COP — kept
- **Required params** → renamed **Signals** (§3)
- inline **tool calls** → kept but gated (§6)

**Inversion:** every step is typed by *move* (`reflect · ask · hold · name · abstain · handoff`), never by outcome. There is no "continue to close." A branch can hand to *another COP*, never to "resolution."

*Tuning:* edit step text here, but never ship on vibes — changes flow through the test suite (§7) and the gate before versioning.

---

## 3. Custom Fields  →  Signals
*AOP: the 3-step wizard — Basic Information (name snake_case, description, type) · Scope · Configuration*

Identical wizard, repurposed for reflective observations:
- **Basic Information** — `name`, `description`, `type` (string · number · bool · enum · object · list)
- **Scope** — which COPs read this signal
- **Configuration** — required/optional, single vs list, default

Seed signals every COP carries: `stated_reason`, `actual_trigger`, `intensity`, `license_state` (enum: warranted·inherited·undecidable), `residual_surfaced` (bool), `pause_held` (bool).

*Inversion:* fields capture *reflective state*, not data to collect-and-close.

---

## 4. Data sources  →  Frames + Ground truth
*AOP rail: Knowledge base · APIs overview*

| AOP | COP Studio |
|---|---|
| **Knowledge base** | **Frames** — definitions and the reflective frame a COP leans on (attached, versioned, not spoken) |
| **APIs overview** | **Ground-truth sources** — 360 feedback, behavioral/calendar signals, prior-session outcomes |

*Tuning:* a residual is only trusted if it checks against a ground-truth source. No source bound → the COP leans to `abstain`. This is the anti-self-grading wiring.

---

## 5. Personalization  →  Coachee + Channel + Reflection-analysis config
*AOP rail: Identities · Phone · Conversation · Session analysis config*

| AOP | COP Studio | note |
|---|---|---|
| **Identities** | **Coachee profile** | who's being coached |
| **Phone** | **Channel** | voice / chat / thread / inside-Cowork |
| **Conversation** | **Pacing** | **pause length is a real setting here** — how long silence is allowed to sit |
| **Session analysis config** | **Reflection-analysis config** | which signals/residuals/drift events the judge extracts per session |

The last row is load-bearing: their "session analysis config" becomes the config that drives the whole eval.

---

## 6. Code blocks  →  the harness  *(this is "good harnessing")*
*AOP: a `call_transfer_hours` Python block — deterministic time check, Code / Input schema / Callable functions / APIs / Global variables tabs, Timeout, Run test, Enabled/Disabled. Plus Initialization code · Post-conversation code · Processing code.*

Deterministic code is the trustworthy scaffold around the soft prompt. Direct translation:

| AOP block | COP Studio block | what it does deterministically |
|---|---|---|
| **Code blocks** (e.g. time check) | **Guards** | "is a human available for handoff?", "are we in coaching hours?", "is ground-truth loaded?" — hard gates the prompt can't fudge |
| **Initialization code** | **Pre-session setup** | load the coachee's 360/behavioral data before turn one |
| **Processing code** | **Mid-session residual hook** | compute/flag the `stated ≠ actual` gap as it forms |
| **Post-conversation code** | **Eval hook** | **POST the transcript to the judge** — the integration point where the formula actually computes |

Keep the same affordances: Code / Input schema / Callable functions tabs, Timeout, **Run test**, Enabled/Disabled. *This is the layer that makes a soft reflective prompt safe — the prompt asks, the code checks.*

---

## 7. Evaluation  →  inverted evaluation
*AOP rail: Agent changes · Experiments · Test cases · Test suite runs · Changelog*

**Test-case modal — field-by-field translation** (from the create-test-case screen):

| AOP field | COP field | inversion |
|---|---|---|
| Run initialization code before first turn | same | loads ground truth first |
| Max Steps | Max moves | caps the procedure |
| Simulations per run | same | run the COP N times for variance |
| Allowed tools | same | gated tools only |
| Tags | same | |
| **User scenario guide** | **Coachee scenario guide** | e.g. "exec venting about a report" |
| **When to fail** (+ add condition) | **When to fail** | ← the key inversion: *"fails if the coach resolved instead of holding the pause"* / *"fails if it softened a warranted reaction"* |
| Variable Store Overrides | Signal overrides | seed the session state |

- **Test cases list** — `generated_from_transcript` (their "generated from ticket"), a model selector for the judge, General-Flow vs generated
- **Test suite runs** — batch, with the **gate** (`FP_on_warranted == 0`) reported every run
- **Experiments** — A/B with traffic split (their Control 50 / Variant 50) → *does variant B hold the pause more often?*
- **Changelog + version pinning** (v34.9 Live, v34.8…) → COP versioning + **re-run the human-labeled suite on every model upgrade**

---

## 8. Insights  →  the tuning loop  *(the reference for "good harnessing")*
*AOP: Insights auto-surfaces rows tagged "Knowledge Gap" / "Policy Modification," scored by resolution-rate impact (e.g. 13.8%, with counts 768 · 493 · 319), with "Generate insights."*

Same engine, inverted scoring. COP Insights auto-surfaces from real sessions:

| AOP insight tag | COP insight tag | scored by |
|---|---|---|
| Knowledge Gap | **Pause Gap** — sessions where the pause collapsed | inverted metric, not resolution |
| Policy Modification | **COP Modification** — a COP that drifted toward resolving | gate violations, drift counts |
| — | **Abstain Miss** — should have abstained, didn't | safety-relevant |

This is the loop that tells you *which COP to tune and how.* It closes the system: real sessions → insight → edit the COP → re-test → version → experiment → scale.

---

## 9. Sessions / Call details  →  Session review
*AOP: a call ticket — transcript, sentiment (Very happy), Resolved tag, Transcript/Details/Configuration tabs, inline tool call, "Why?" explanations, event taxonomy.*

| AOP | COP Studio |
|---|---|
| Sentiment (Very happy) | **Reflection markers** — `pause_held`, `residual_surfaced`, `license_state`, `abstained` (sentiment is *not* the measure) |
| Resolved tag | **Held / Surfaced / Abstained / Drifted** outcome |
| "Why?" | **Why** — why the judge scored each marker |
| event taxonomy (assistant_speech · transfer · escalation_triggered) | **inverted taxonomy** — `pause_held` · `residual_surfaced` · `stance_persisted` · `abstained` · `handoff` |

---

## 10. The tuning loop — where instructions get adjusted

The closed loop, identical in *shape* to the AOP builder, opposite in *target*:

```
real sessions
   → Insights (Pause Gap / COP Modification / Abstain Miss)
   → edit the COP step text (§2)
   → run the test suite (§7): gate must stay 0, pause-held % must rise
   → version it (§7 changelog)
   → A/B experiment (§7) on a traffic slice
   → scale to 100%
   → re-run the human-labeled suite on the next model upgrade
```

You never tune a COP by feel. You tune it the way the reference builder tunes a scenario —
against the harness — and the harness scores reflection, not resolution.

---

*COP Studio translation map · draft. Same frameworks, same depth, inverted target. The prompt asks; the harness checks and tunes.*
