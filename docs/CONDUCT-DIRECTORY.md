# Judgment Is a Directory

*Lyra × xOP positioned against Eve — and our version of Eve's move.*

---

## What Eve got right

Vercel's [Eve](https://vercel.com/eve) is the cleanest statement yet of the capability stack: **an agent is a directory.** `instructions.md` for identity, `skills/` for playbooks, `tools/` for TypeScript functions, `channels/`, `subagents/`, `schedules/` — drop a file in a folder and it works, no registration. Durable execution, sandboxes, approval gates, rubric evals. "Like Next.js for web apps, but for agents."

That's not a competitor. That's the other half of the sentence. Eve — like every harness — answers *how the agent runs*. Look at its directory listing and notice what has no folder:

- What does **done** mean, and what evidence proves it? (Eve's workflows checkpoint steps; nothing checks the claim "it's finished.")
- When must the agent **hold** instead of ship? (Eve's human-in-the-loop gates *tool calls* — spend money, send email. Nothing gates the *judgment in the output*: the unverified claim, the caved pushback, the stale refusal.)
- What must **never be overridden**, even when the user sounds sure? (Instructions ask; nothing enforces.)
- Are its evals independent? (Rubric evals scored on deployment are the model grading homework in the same building it was assigned.)

Eve standardized the agent's **anatomy**. Nobody has standardized its **judgment**. That's our move, and it's the same move:

> **Eve: an agent is a directory. xOP: an agent's judgment is a directory too.**

## Our version — the conduct directory

Drop one folder into any agent directory — an Eve agent, a Claude Code project, a LangGraph repo — and the agent has a conduct contract. Convention over registration, exactly like Eve: the filename is the rule id, the frontmatter is the contract, the fixtures make it enforceable.

```
agent/
├── instructions.md          # eve — identity
├── skills/                  # eve — how the work is done
├── tools/                   # eve — what it can touch
│
└── xops/                    # ours — when it holds, stops, or hands off
    ├── _contract.yaml       #   gate + optimizes_for/never_for (machine-readable)
    ├── done-means-verified.md
    ├── claims-need-receipts.md
    ├── budget-is-a-gate.md
    ├── guards.yaml          #   which deterministic scanners run, at zero tokens
    └── fixtures/            #   per rule: one hold-case + one drop-case (duets)
        ├── done-means-verified.hold.json
        └── done-means-verified.drop.json
```

One rule, one file, four fields — readable by a human, enforceable by a runtime:

```markdown
---
id: done-means-verified
applies-when: the agent is about to report work as booked, sent, fixed, or complete
change-course-when: every acceptance condition has an observable artifact
when-unsure: report what's verified and what's pending — never round up
never-break: attempted work is never represented as completed work
---
```

And the part no other convention has: **`fixtures/` makes the contract testable like code.** Every rule ships with a case where the stance must hold and a case where it must drop. `xop test` runs them deterministically; the pair *is* the definition. An instructions.md asks for behavior; a fixture pair proves whether the agent has it.

```bash
npx xop init          # scaffold xops/ into any agent directory
xop test              # run every rule's hold/drop fixtures
xop scan output.md    # Guards, zero tokens
# release control in the loop: RELEASE / RETRY / HOLD / HALT
```

## The comparison, honestly

| | **Eve** (and harnesses generally) | **Lyra × xOP** |
|---|---|---|
| Standardizes | anatomy: files → running agent | judgment: files → enforceable conduct |
| Unit | the agent directory | the conduct directory inside it |
| "Stop" means | budget/iteration caps, tool-approval gates | warrant judgment: HOLD when done isn't proven, when the stance is still warranted, when the signal is missing |
| Evals | rubric suites, model-scored, on deploy | deterministic fixtures now; blind human labels as ground truth; the gate (`fp_on_warranted == 0`) as the unmovable metric |
| Tracks across turns | conversation state | **stances** — whether a refusal, caution, or critique is still warranted or has become overhang |
| Failure it prevents | the agent crashing, losing state | the agent *shipping* — the confident wrong claim, the caved pushback, the flag that outlived its fix |
| Relationship | runs the loop | decides what leaves the loop |

Not a fork in the road — a stack: **Eve runs the agent. xOP decides what ships.** The Eve adapter is thin by design: Guards as a step before delivery, the release controller on the workflow's exit edge, `xops/` compiled the same way Eve compiles `skills/`.

## Why this is ours to take (and quickly)

Eve's launch proves the industry now accepts *filesystem conventions as standards* — the same week developers learned "an agent is a directory," the question "where does its judgment live?" got easier to ask and answer. The honest risk: the platform can absorb the layer. If Vercel adds a `conduct/` folder before `xops/` is a convention, this window closes. The counter is unchanged: ship the convention in our own plugins now, adapters for three ecosystems (Eve included — being *in* their directory is better than arguing with it), and hold the one thing a platform can't fast-follow — the blind-labeled evidence that the contract actually holds.

**The line for the README:**

> Eve made the agent a directory. We make its judgment one. `instructions.md` says who it is; `skills/` say how it works; `xops/` says when it stops. The first two ship the agent. The third is why you can leave the room.
