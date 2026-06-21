# AGENTS.md — operating guide for agents working in this repo

*Read this before you touch anything. It is the short version of how this repo thinks, what it will
not let you do, and the exact commands that prove your change didn't break the one thing that matters.
Humans: see `README.md` and `USAGE.md`. Agents: this page, then `CONCEPTS.md`.*

---

## What this repo is, in one breath

**xOP is a procedure standard for judgment-bearing work** — work where the job is to check whether a
stance is **still warranted** and **hold** it, not to resolve a ticket. SOPs and AOPs resolve. An xOP
holds. (`README.md` for the long version; `CONCEPTS.md` for every locked term.)

This is a **strong scaffold with one named hole**: the **warrant judge** is not built. Today a blind
human label stands in for it. Never write as if it exists.

## The one rule you cannot touch

```
the gate:  false_positive_on_warranted == 0
```

Never override a state that is **still warranted**. Everything in this repo serves this. It is
**constitutional** (`CONSTITUTION.md` §I) — you may not weaken it, average it away, or "improve" the
system by shedding warranted caution. A change that relieves friction by dropping a warranted state is
a **regression**, not a fix.

## Speak the locked vocabulary

`CONCEPTS.md` is the single source of truth for wording. The load-bearing ones:

- The concept is **warrant**, not "license." Three states: **`warranted · inherited · undecidable`** — never "pass/fail."
- **drift** = a stance outliving the condition that warranted it. **overhang** = what it leaves behind.
- The residual is **`L = x − x̂`**. Two metrics that can't move: **the gate** and **the coverage floor**.
- **abstain is a correct outcome**, scored positively. **No pooled score**, ever.
- xOP — *"the version that doesn't resolve."* Lyra — *"the version that doesn't perform."*

## Honesty discipline (this is a credibility asset, not a disclaimer)

`REPO_STATE.md` is the honesty manifest — what's built, what's scaffold, what's only named. Keep it
accurate or delete it. When you add something, update it. Specifically, **never**:

- claim the judge is built, or report the **oracle** (`oracle_upper_bound`) as if it were a detector — it reads the answer key;
- **pool** the gate, floor, coverage, and abstain into one number — pooling hid a total failure once (`archive/AWAKEN_Flagship_The_Wrong_Pass_Rate.md`); the harness refuses to;
- let a machine **label** a case — machines source candidates, humans label them blind, never the author (`CONSTITUTION.md` §IV);
- validate a detector against the oracle or against its own prior output.

## Prove your change — the harness is the dogfood

Any change that could affect scoring runs the harness. Python is `python3` here.

```bash
cd harness
python3 run_harness.py                 # gate + floor + per-class confusion, no pooled score
python3 run_harness.py --trace         # per-case  gold -> call  (X marks a gate violation)
python3 test_harness.py                # the harness's own tests
```

Expected baseline (a 13-case **scaffold**, not a benchmark): `always_abstain` **passes the gate,
fails the floor** ("safe and worthless," correctly rejected); `lexical_floor` **violates the gate**.
Both reading "FAIL" is the *intended teaching outcome*, not a bug. If your change makes a real detector
violate the gate, stop.

Rebuild the gold scaffold from scratch (`gold.json` is a derived artifact, gitignored):

```bash
cd harness/phase1
python3 generate_candidates.py
python3 label_cli.py --labeler alice --from demo_a.txt
python3 label_cli.py --labeler bob   --from demo_b.txt
python3 reconcile.py labels_alice.json labels_bob.json   # -> gold.json (scaffold; blind:false)
```

## How work changes the standard (governance)

Policy never edits itself (`CONSTITUTION.md` §V). The chain (`GOVERNANCE.md`):

```
session → insight (insights/) → proposal (proposals/) → ruling (accepted/ | rejected/)
```

Most observations **stop at insight** — an insight is not a change. A proposal merges only on **gate
evidence** (blind labels, full harness run, gate clean, floor still cleared, status line recorded),
never on argument. The four constitutional clauses change only by a named **P5 amendment**. The
rejected set is the doctrine — keep it.

## Authoring or validating an xOP

- The format is `SPECIFICATION.md` (defined once; domains are *instances*, not new formats).
- To take one from idea → adopted, follow **`PIPELINE.md`** (the phases) and grade it with
  **`SCORECARD.md`** (two tiers, pass ≥ 85, plus the proof-of-behavior gates).
- The flagship reference is `examples/writing_license/` (interpretive); `examples/refusal_license/` is the agent-surface exemplar. Reference-xOP gold folders ship **unlabeled** —
  an xOP does not label its own eval set.

## Map

```
AGENTS.md         you are here — how to work in this repo
CONCEPTS.md       the locked vocabulary (single source of truth)
SCORECARD.md      is this a real xOP? two tiers + proof-of-behavior gates
PIPELINE.md       idea → Source → Portable → gold → validate → publish
README · USAGE    the human on-ramps (three doors; two need no code)
CONSTITUTION      the rules policy may not change   ·   GOVERNANCE  how policy changes
SPECIFICATION     the format at full depth          ·   REPO_STATE  the honesty manifest
harness/          the scorer + baselines + phase1/ gold pipeline
examples/         reference xOPs people adopt        ·   failures/  documented blind spots, kept forever
```

---

*If you remember one thing: the gate is the product. A change that makes the agent more agreeable by
overriding a warranted state has not improved this system — it has defeated it.*
