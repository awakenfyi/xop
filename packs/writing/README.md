# Writing Work Pack — make AI stop sounding like AI

> Pain it fixes: **"My writing comes back sounding like it was written by AI."**
> Not detector-evasion (unprovable, brittle). De-slopping — so *your* voice survives.

A **Work Pack** is the install unit: `Skill + xOP + Guard + Tests`. This pack ships
the Guard and the xOP halves of that; the Skill (house-style rewrite) and a role
bundle come next.

```
Skill   — how to write it           (the playbook)        → coming next
xOP     — when to hold your voice    writing_license       → DESIGNED (../examples/writing_license/)
Guard   — exact tells to never emit  no-ai-tells           → RULE-TESTED (guard/)
Tests   — the receipts               fixtures.jsonl        → 12/12 pass
```

## The two halves, and why you need both

**The Guard (`guard/no-ai-tells`)** is the deterministic net. It scans for the generic
LLM voice across three tiers — reflexive *vocabulary* (`delve`, `tapestry`, `robust`),
boilerplate *constructions* (*"it's not just X, it's Y," "I hope this helps," "In
conclusion"*), and advisory *rhythm* signals. Mechanical, PASS/FAIL, no pilot needed.
It works today.

**The xOP (`writing_license`)** is the judgment. The Guard flags *every* `delve` —
including the rare one a geologist actually needs. Left alone, the Guard would flatten
voice, which is the precise thing `writing_license` forbids ("never override a
warranted authorial choice"). So the Guard finds candidates; the xOP decides which to
keep. **Run the Guard to see the tells; run the xOP — or your own eye — to rule on
them. Never auto-rewrite from the Guard alone.** That pairing is the whole design.

## Use it in 30 seconds

```bash
cd guard
python3 check_ai_tells.py your_draft.md
```

You get every tell with its line number, plus advisory rhythm metrics, plus the
reminder that flags are *candidates*, not verdicts on the writing.

## The badge ladder (honest status, no rounding up)

This pack replaces a single `SCORED` stamp with a four-rung ladder. A claim only
climbs when the evidence for it exists:

| Badge | Means | This pack |
|---|---|---|
| `DESIGNED` | passes the schema + admission tests | writing_license, the (pending) Skill |
| `RULE-TESTED` | mechanical fixtures pass | **no-ai-tells Guard — here now (12/12)** |
| `HUMAN-EVALUATED` | semantic behavior compared to ≥2 blind human labels | not yet — needs the pilot |
| `FIELD-VALIDATED` | measurably reduced rework in real use | not yet |

Result is reported separately as `PASS / FAIL / INCONCLUSIVE` — a pack can be
`HUMAN-EVALUATED` and still `FAIL`. "RULE-TESTED" says the Guard does what it says
mechanically. It does **not** say the de-slopped text reads better to a human — that is
`HUMAN-EVALUATED`, and this pack does not claim it.

## What this pack does NOT claim

- It does not "beat AI detectors." It removes named tells; detection is a separate,
  moving target it makes no promise about.
- It does not certify text is "human-written."
- The Guard does not exercise judgment — a flagged word can be the right word.
- Nothing here is self-certifying — the Guard is `RULE-TESTED` (mechanical fixtures), the semantic xOP is `DESIGNED` until blind human labels exist.
