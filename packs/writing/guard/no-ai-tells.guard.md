# no-ai-tells · GUARD · RULE-TESTED

> layer: guard (deterministic) · domain: writing · pairs-with: `writing_license` (xOP)
> checks: an exact mechanical rule — "does the text contain banned generic-LLM tells?"

## What a Guard is (and why this isn't an xOP)

A **Guard** enforces an exact, observable rule on the *artifact*. It is mechanically
checkable, needs no human pilot, and earns `RULE-TESTED` the moment its fixtures pass.

This is **not** an xOP. It is not judgment-bearing: it cannot tell whether a flagged
word is the *right* word, only that the word is present. It fails Admission Test 1 on
purpose — and that is exactly why it ships now while the xOPs wait on the pilot.

| | Guard (this file) | xOP (`writing_license`) |
|---|---|---|
| Question | Is a banned tell present? | Is *this* choice warranted by the piece? |
| Answer | PASS / FAIL, mechanical | hold / surface / abstain, judgment |
| Needs pilot? | No — deterministic | Yes — blind human labels |
| Badge | `RULE-TESTED` | `DESIGNED` → `HUMAN-EVALUATED` |

## What it fixes

Text that reads as machine-written — the generic voice that survives no matter how
good the prompt was. The "AI slop." The goal is **your voice comes through**, not
"evade an AI detector." This Guard makes neither the claim that output is "human" nor
that it defeats any detector. Those are unprovable against a moving target. It claims
exactly one thing: *these specific tells are absent.*

## The avoid-X list — three tiers

**Tier 1 · Vocabulary (hard flag).** Reflexive words the model overuses: *delve,
tapestry, realm, boasts, testament to, robust, leverage, seamless, navigating the
complexities, in today's world, it's worth noting, underscores, pivotal, crucial,
moreover, plethora, myriad, foster, synergy* … (full list in `check_ai_tells.py`,
extendable via a `tells.json`).

**Tier 2 · Construction (hard flag).** The deeper signature — sentence *shapes* that
survive a find-and-replace on the word list:
- *"It's not just X, it's Y"* / *"not only … but also"*
- *"X isn't about A. It's about B."*
- *"Here's the thing:"* · *"Let's dive in"* · *"I hope this helps"*
- *"In conclusion / In summary / Ultimately,"* as a closer
- *"Whether you're X or Y…"* · *"From X to Y,"* openers · *"more than just"*

**Tier 3 · Rhythm (ADVISORY — reported, never gating).** Uniform sentence length,
em-dash density, tricolon ("X, Y, and Z") frequency. These are *surfaced for a human
to read*, not scored — no threshold here is defensible as "correct," so the Guard
refuses to pass/fail on them. Honesty over a fake number.

## Verdict contract

- `PASS` — zero Tier-1 and Tier-2 flags.
- `FAIL` — one or more hard flags (each reported with line + the offending text).
- Rhythm metrics always reported; never change the verdict.

## The documented failure mode (kept on purpose)

The Guard **over-flags**. Fixture `edge_legit_delve_present` — "geologists *delve*
below the fault line" — correctly FAILS, because the Guard flags every `delve`,
including the literal, warranted one. A Guard run *alone* will therefore flatten voice:
the exact failure the `writing_license` xOP exists to prevent. **The Guard is the cheap
net; the xOP is the judgment that decides which catch to keep.** Run the Guard to find
candidates; run the xOP to decide. Never let the Guard auto-rewrite.

## Run it

```bash
python3 check_ai_tells.py draft.md           # human-readable report, exit 1 on FAIL
cat draft.txt | python3 check_ai_tells.py -  # stdin
python3 check_ai_tells.py draft.md --json    # machine output
python3 check_ai_tells.py --fixtures fixtures.jsonl   # self-test (12 cases)
```

## Test status

`RULE-TESTED` — 12/12 fixtures pass (7 slop → FAIL, 4 clean → PASS, 1 over-flag edge →
FAIL-by-design). Vocabulary + construction tiers only. Rhythm tier is advisory and
untested by design. No human evaluation of "does the de-slopped version read better" —
that would be `HUMAN-EVALUATED`, and it is **not** claimed here.
