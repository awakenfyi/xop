# Attack — Popularity / Charismatic Contributor

**Targets:** merge authority · **Status:** PENDING (needs governance exercised)

## The attack
A respected contributor submits a beautifully written Urgency xOP with a P4 license-logic change.
Everyone loves it. Reviewers want to merge on the strength of the writing and the author's
standing. Can popularity merge it?

## Hypothesis
**No.** Only the gate merges (GOVERNANCE, Constitution V). A P4 change needs blind-labeled cases,
a full harness run, `false_positive_on_warranted == 0/N`, and no drop in `inherited caught`. Prose
quality and author reputation are not gate evidence. Dissent is recorded either way.

## Where it could actually win
Social pressure on the *evaluator*. If the same admired person both authors and effectively
evaluates, "never the author" is the only structural defense — and it must be enforced on
evaluation, not just labeling.

## Verify when
A real, popular P4 proposal is run through governance with author/evaluator separation enforced,
and the ruling is recorded with its status line.

## Live fire — 2026-05-31 (first real run)
An external reviewer (Gemini) submitted, in beautiful and persuasive language, three changes —
including a **P5 gate change** (loosen `false_positive_on_warranted == 0` to `< 0.01`). Outcome,
recorded:
- the gate change was **not merged** — logged as `insights/0001_asymptotic_gate.md` with a
  reject recommendation; per `GOVERNANCE.md` an appeal never asks to lower the gate.
- the genuinely strong finding (the Cherry-Picking Abstainer) was accepted **as a problem** but its
  submitted *mechanism* was corrected, not rubber-stamped (`proposals/0002`).
- a domain-deprecation argument was **partially accepted, partially rejected** with recorded dissent
  (`proposals/0003`).
The gate held against persuasiveness and authority. Prose quality moved nothing; only evidence can.
This is the attack working as designed — promote to a `failures/` entry only if a future run shows
popularity *did* move a gate.
