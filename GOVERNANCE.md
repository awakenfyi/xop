# GOVERNANCE

*How the standard changes without corrupting itself. Policy lives here; the rules policy may not
touch live in `CONSTITUTION.md`. This document is the evolution path: observation → insight →
proposal → ruling → version bump.*

---

## The chain

```
session   ── something happened worth noticing
  → insight     (insights/)        most observations stop here. an insight is not a change.
  → proposal    (proposals/)       a candidate change, with a gate-evidence requirement.
  → ruling                          merge (→ accepted/) or reject (→ rejected/). both are kept.
```

Most observations should **never** become proposals. The `insights/` layer exists so the system
can notice things without being obligated to act on them. A proposal is a candidate, not a change;
it merges only if it passes the gate on a blind gold set.

## Proposal classes

Use `proposals/PROPOSAL_TEMPLATE.md`. Every proposal declares a **type** and a **severity**:

| Severity | Scope | Path |
|---|---|---|
| P1 | docs / wording | proposal |
| P2 | procedure text | proposal |
| P3 | signals | proposal |
| P4 | license-logic | proposal (scrutinize gate impact hard) |
| **P5** | **the gate, the floor's existence, anti-optimization, evidence rule** | **amendment, not a proposal** — reviewed as a constitutional change |

**Risk** (blast radius) is tagged separately: Low · Medium · High · Constitutional.

## Gate evidence (required before any merge)

A proposal cannot merge on argument. It merges on evidence:

- [ ] new case(s) **blind-labeled by ≥2 non-authors**
- [ ] harness run on the **full** gold set (`harness/run_harness.py`)
- [ ] `false_positive_on_warranted == 0/N` holds
- [ ] `inherited caught` did not drop (coverage floor still cleared)
- [ ] status line recorded (the canonical one from `run_harness.py`; **no pooled score**)

## Dissent

A named reviewer's recorded disagreement is **kept either way** — it does not change the ruling,
and it becomes training data and the seed of future failure docs. (Proposal 0001's dissent is how
`failures/Graduated_Decomposition.md` exists.)

## Appeals

An appeal is reviewed by a **non-author, non-original-evaluator**. It asks one question only:
**was the gate applied correctly?** It never asks whether to *lower* the gate. The gate is not
appealable; only its application is. Final ruling is recorded on the proposal.

## "Why not the obvious looser fix?"

Every proposal answers a **why-not**. "Why not loosen after repeated pushback? Because frustration
is not a license change." The accumulated why-nots in `proposals/rejected/` become the doctrine —
the standard's memory of caution it refused to shed.

---

*Sessions generate evidence; evidence generates proposals; proposals modify policy; policy never
modifies itself. The rejected set is the doctrine.*
