# CONCEPTS — the locked vocabulary

*The single source of truth for what every word means. If a term is defined here, the repo uses it
this way everywhere — prose, code identifiers, site copy, marketing. A term not in this file is not
load-bearing. Disagreements about wording are resolved here, not in the page that uses the word.*

*Companion to `CONSTITUTION.md` (the rules) and `SPECIFICATION.md` (the format). Where they and this
file ever diverge, this file names the canonical term and the other gets corrected.*

---

## 0. The one sentence

> An **xOP** checks whether the assumptions, reactions, refusals, urgencies, and judgments driving a
> task are **still warranted** — and **holds** instead of resolving when they are.

---

## 1. The OP family

| Term | Locked meaning | Never say |
|---|---|---|
| **the OP family** | the lineage `SOP → AOP → xOP` | "framework," "prompt library" |
| **SOP** | standard operating procedure — *executes a task, resolves* | — |
| **AOP** | agentic operating procedure — *executes autonomously, resolves* | — |
| **xOP** | the operating procedure for when the outcome **isn't determinate** — *holds a judgment, doesn't resolve* | "xOP tool/app" |
| **the variants** | **COP** (Coaching OP) · **WOP** (Writing OP) · **Refusal xOP** (agents) | "the coaching product" |

The strategic frame: own **xOP** the way Decagon owns **AOP**. *AOP resolves the ticket. An xOP holds.*

---

## 2. Warrant — the concept (this retires "license")

The central concept is **warrant**: *is this stance still warranted by what's present now, or is it
left over from before?*

| Locked term | Meaning |
|---|---|
| **warrant** (noun) | the present condition that licenses a stance |
| **warranted** | the triggering condition is still present → respect the stance, end |
| **inherited** | the triggering condition is gone → the stance is **overhang**; surface it |
| **undecidable** | insufficient signal → **abstain** |
| **the three states** | `warranted · inherited · undecidable` — never "pass/fail," never "good/bad" |
| **drift** | a stance outliving the condition that warranted it (the residual's habit in long context) |
| **overhang** | the inherited stance itself — the thing drift leaves behind |

**Plain-language hook (consumer pages):** *"Is it still true, or is it left over from somewhere
else?"* Introduce "warrant" once, gently, then use it.

### 2a. The `license → warrant` ruling (resolves content-map open decision #1)

**Decision: `warrant` is the canonical concept word. `license` is retired as the concept.** Reasons:
the consumer brief already requires it (`site/awaken_content_map.md` §1), the gate metric is already
`false_positive_on_warranted`, the three states are already `warranted/inherited/undecidable`, and
"license" collides with the OSS `LICENSE` file.

**What this does NOT touch:**
- the OSS **`license:`** header field on an xOP (§1 of the spec) — that is the software license, unrelated, stays.
- example **directory slugs / ids** already shipped (`examples/refusal_license/`, `examples/writing_license/`) — stable identifiers; renaming them is a separate, id-breaking migration, not this decision.

**Staged mechanical migration (tracked, harness-verified, not yet executed):**
| From | To | Where |
|---|---|---|
| "license judge" / "the judge that computes license" | "warrant judge" | prose: README, SPEC §11, PLAN, detectors.py docstring |
| "License model" (spec §7) | "Warrant model" | SPECIFICATION.md |
| "is it still licensed?" | "is it still warranted?" | README, CONSTITUTION footer |
| `license_state` (signal name) | `warrant_state` | SPECIFICATION.md §5 |
| `gold_license` (JSON key) | `gold_warrant` | harness code + every `gold/*.json`, `phase1/*.json` — closed-system rename, run `run_harness.py` before/after to prove identical PASS |

Until executed, treat the above as **aliases of the same concept**. The migration runs as one
governed change (P1/P2, Low risk) with the harness as proof. See `PIPELINE.md` Phase 5 note.

---

## 3. The two metrics that can't move

| Term | Locked meaning |
|---|---|
| **the gate** | `false_positive_on_warranted == 0` — never override a state that's still warranted. The moral center. |
| **the coverage floor** | `inherited_caught >= floor` — a detector must actually catch overhang; "safe and worthless" is rejected. The floor's *value* is policy; that one *exists* is constitutional. |

Both are reported every run, **never as a single pooled number.** Pooling hides a total failure behind
an average — the project's own first mistake (`archive/AWAKEN_Flagship_The_Wrong_Pass_Rate.md`).

---

## 4. The residual

| Term | Locked meaning |
|---|---|
| **the residual** | **`L = x − x̂`** — what a response *did* (`x`) minus what it *claimed* to be doing (`x̂`) |
| `x` | behavior / what's actually happening (cleanest when externally observable) |
| `x̂` | self-description / the stated account |
| `L` | the divergence to **surface, name once, and not explain away** |

When `L` grows, the explanation has started **protecting** the output instead of describing it. This is
the same subtraction Lyra runs at the response level and an xOP runs at the procedure level.

---

## 5. Mechanism words

| Term | Locked meaning |
|---|---|
| **Source** | the richly-authored xOP (the spec's full depth) — *you author it* |
| **Portable** | the flat markdown Source compiles to — runs in any thread — *you ship/market it* |
| **the contract** | the machine-readable `optimizes_for / never_for / gate` block (spec §1) — requires a runtime to enforce; does not survive a bare prompt |
| **the judge** | the unbuilt component that computes the warrant state on hard cases; a blind human label stands in for it today |
| **the oracle** | the upper-bound reference that reads the answer key — **not a detector**; proves the signal is sufficient *if you have it* |
| **gold** | cases labeled by **≥2 independent humans, blind, never the author**; disagreement resolves to `undecidable` |
| **the move types** | `reflect · ask · hold · name · abstain · handoff` — run **one at a time, never combined** |

---

## 6. Credibility lines (locked phrasing)

- **"No model grades model. Receipts, not vibes."**
- **Lyra** — *"the version that doesn't perform."* (response discipline)
- **xOP** — *"the version that doesn't resolve."* (the procedure standard)
- The honest-status line, kept until the judge exists: *"strong scaffold, judge unbuilt."*

Never say: "AI-powered," "magic," "framework" (for the family), "license" (for the concept),
"pass/fail" (for the states).

---

*One question (is it still warranted?), three values (warranted · inherited · undecidable), two metrics
that can't move (the gate, the floor), one residual (`L = x − x̂`). Defined once, here.*
