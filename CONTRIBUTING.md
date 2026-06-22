# Contributing to xOP

Thanks for considering it. xOP is a standard, so contributing here is a little different from a
normal code repo: **you don't merge a change by arguing for it — you merge it by passing the gate on
evidence.** This page is the short version; the full rules live in `GOVERNANCE.md` and `CONSTITUTION.md`.

First read: **`AGENTS.md`** (how this repo thinks) and **`CONCEPTS.md`** (the locked vocabulary). If
you use a word this repo has retired — "license" for the concept, "pass/fail" for the states,
"framework" for the OP family — a reviewer will ask you to change it.

## The one rule you cannot touch

```
the gate:  false_positive_on_warranted == 0
```

Never propose a change that "improves" the system by overriding a state that's still warranted. Under
this repo's Constitution that is a regression, not a fix. The gate and the coverage floor are
**constitutional** — they change only by a named P5 amendment, never folded into a normal proposal.

## What you can contribute

| You found… | File it as | Where |
|---|---|---|
| Something worth noticing | an **insight** | `insights/` |
| A candidate change to policy | a **proposal** (needs gate evidence) | `proposals/` (use `PROPOSAL_TEMPLATE.md`) |
| A way the standard fails | a **failure doc** (kept forever) | `failures/` |
| An attack on the method | a **red-team entry** (filed PENDING until the judge exists) | `red_team/` |
| A new reference xOP | an **example** | `examples/` (ships with an *unlabeled* gold folder) |

Most observations should **stop at an insight.** An insight is not a change.

## How a proposal merges (gate evidence — required)

A proposal cannot merge on argument. It merges on a harness run (`GOVERNANCE.md`):

- [ ] new case(s) **blind-labeled by ≥2 non-authors** (machines source cases; humans label them)
- [ ] `harness/run_harness.py` run on the **full** gold set
- [ ] `false_positive_on_warranted == 0/N` holds
- [ ] `inherited caught` did not drop (coverage floor still cleared)
- [ ] the canonical status line recorded — **no pooled score**
- [ ] a **why-not**: why not the obvious looser fix? (the rejected set is the doctrine)

## Before you open a PR

Run the release gate locally:

```bash
./verify.sh            # harness + invariants + reference integrity + honest-status check
```

It must be green. CI runs the same checks on every PR.

## AI / automation disclosure

Much of this repo is built with AI assistance, and that's fine — but **say so.** If a PR was
substantially AI-generated, note it in the description (the PR template asks). An xOP repo that hid
its own automation would be failing its own honesty rule.

## The honesty rule

`build/inventory.json` is the current baseline evidence manifest — what's built, what's scaffold,
what's only named. If your change moves something across that line, update it in the same PR (a
`NORMATIVE.md` will formalize this in Phase 0). Never claim the **warrant judge** is built — it
isn't, and saying so is the one thing that breaks this project's credibility.

---

*Sessions generate evidence; evidence generates proposals; proposals modify policy; policy never
modifies itself. Welcome.*
