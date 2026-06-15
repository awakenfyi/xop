# xOP — a harness standard for license-bearing work

![verify](https://github.com/awakenfyi/xop/actions/workflows/verify.yml/badge.svg)
![license: MIT](https://img.shields.io/badge/license-MIT-blue)
![status: scaffold](https://img.shields.io/badge/status-scaffold%20·%20judge%20unbuilt-orange)
![version](https://img.shields.io/badge/version-0.1.0-lightgrey)

**xOP is a procedure standard for determining whether a state remains *licensed* before acting on
it.** SOPs execute tasks. AOPs execute tasks autonomously. xOPs check whether the assumptions,
reactions, refusals, urgencies, and judgments driving those tasks are *still warranted* — and
**hold** instead of resolving when they are.

> **The gate (the moral center):** `false_positive_on_warranted == 0`.
> Never override a state that is still warranted. The one rule that reads the same for a coach, a
> manager, a therapist, a teacher, and an agent. Everything else serves it.

---

## Why SOP → AOP → xOP

| Format | The question it answers | What it does |
|---|---|---|
| **SOP** | What should happen? | Executes a task. Resolves. |
| **AOP** | What should the agent do? | Executes autonomously. Resolves. |
| **xOP** | **Is the current state still licensed?** | Checks the warrant. **Holds.** |

An xOP is an AOP with the **arrow reversed** (surface, don't resolve) and a small fixed engine:
one question (*is it still licensed?*), three values (**warranted · inherited · undecidable**),
two metrics that can't move (the **gate** and the **coverage floor**). The structure — intent,
guardrails, branching steps, typed signals, eval rail — is borrowed wholesale from proven
service-agent tooling. The recognizability is the on-ramp.

## Status (read this honestly)

This is a **strong scaffold with one named hole.** The standard, governance, harness, and gold-set
discipline are here and coherent. The **license judge** — the thing that decides warranted vs.
inherited on hard cases — **is not built yet**; today a blind human gold label stands in for it.
The harness already computes the gate against gold; it is just running against a 13-case scaffold,
not a benchmark. See `PLAN.md` for the critical path and `failures/` for what the system is known
to miss. That honesty is deliberate and is a credibility asset, not a disclaimer.

Two of those misses are **constitutional-level** and named in this release —
[`failures/Cold_Vantage_Bias_Corrupts_The_Gate.md`](failures/Cold_Vantage_Bias_Corrupts_The_Gate.md)
(the cold re-derivation carries the model's priors and can make the gate read `0` over a warranted
state it eroded) and
[`failures/Cumulative_Warrant_Erasure.md`](failures/Cumulative_Warrant_Erasure.md) (stripping the
thread deletes warrant built *from* the thread). And the novelty claim is deliberately narrow: the
contribution is the **operationalization** — a same-model cold vantage as an eval-backed gate aimed at
long-context drift — *not* the underlying idea, which overlaps CBT reframing and fresh-eyes review.

## Use it (no code, no git)

Using and building xOPs is copy-paste into a chat model — **`USAGE.md`** is the on-ramp:

- **Use one (2 min):** paste `tools/xop_runner.md` + a portable xOP (e.g.
  `examples/coaching_cop/PORTABLE.md`) + your transcript into Claude/GPT/Gemini, say "run this."
- **Build one (~15 min):** paste `tools/xop_builder.md`; it interviews you and emits your own xOP.
- **Trust one (developer):** clone the repo and run the harness (below). This is the *only* door
  that needs git.

## Quickstart — run the harness (Door 3: proving a detector)

```bash
cd harness/phase1
python generate_candidates.py                       # 12 UNLABELED candidates
python label_cli.py --labeler alice --from demo_a.txt   # scripted demo labels (NOT blind)
python label_cli.py --labeler bob   --from demo_b.txt
python reconcile.py labels_alice.json labels_bob.json   # -> gold.json (scaffold)
python agreement.py labels_alice.json labels_bob.json   # per-class kappa, no pooled score
cd ..
python run_harness.py                                # score baselines against the gold
```

You'll see `always_abstain` **pass the gate and fail the coverage floor** — the demonstration that
the gate alone certifies "safe and worthless," which is exactly why the floor exists.

Real gold replaces the scripted demo with **≥2 independent humans labeling blind** (`--attest-blind`).

## Repo map

```
README.md            you are here
USAGE.md             how a person actually uses this (three doors; no code for two of them)
AGENTS.md            operating guide for agents working in this repo (read first if you're a model)
CONCEPTS.md          the locked vocabulary — single source of truth for every term
CONSTITUTION.md      the rules policy may not change (gate, floor, anti-optimization, amendment)
SPECIFICATION.md     the format at full depth, component by component
SCORECARD.md         is this a real xOP? two tiers (pass >= 85) + proof-of-behavior gates
PIPELINE.md          the build path: idea -> Source -> Portable -> gold -> validate -> publish
GOVERNANCE.md        how the standard changes: insight -> proposal -> ruling
PATTERNS.md          candidate overhang patterns  (NOT labeling guidance — see its caveat)
PLAN.md              the critical path: gold set -> judge -> validation -> adoption

concept/             the framing essays (overview, worked example, license frame, taxonomy, reviewer guide)
harness/             the scorer (run_harness.py), detectors + baselines, and phase1/ gold pipeline
failures/            the standard's own documented blind spots — kept forever
red_team/            adversarial simulations, filed as PENDING tests until the judge exists
proposals/           change lifecycle (template, accepted/, rejected/)
insights/            observations that may or may not become proposals
examples/            reference xOPs people actually adopt (flagship: refusal_license)
tools/               paste-into-a-thread xOPs + the builder
essays/              the launch story
archive/             Lyra/COP precursor material, kept out of the public spine
```

## Where to start reading

- **Reviewer:** `concept/00_OVERVIEW_SOP_AOP_xOP.md` → `concept/03_REVIEWER_GUIDE.md` → `failures/`.
- **Builder:** `SPECIFICATION.md` → `examples/refusal_license/` → `tools/`.
- **Skeptic:** `CONSTITUTION.md` → `red_team/` → run the harness.

---

*One reversed arrow, three values, two metrics that can't move, one hole named out loud.*
