# Marketing Lab

**Lab xOP · DESIGNED**

Operating rules for AI in marketing copy, campaign execution, and brand consistency. An xOP
won't write the copy — it governs the moments where judgment matters: is this claim supported?
is this urgency real? did the copy drift from the approved positioning?

## The Lab xOPs

| ID | Title | Anchor | Status |
|----|-------|--------|--------|
| `xop.claim.evidence-bound` (profile: marketing) | Claims Need Receipts | source-to-claim relationship | DESIGNED |
| `xop.marketing.urgency-evidence` | No Made-Up Urgency | verified deadline / scarcity | DESIGNED |
| `xop.decision.ledger` (profile: positioning) | Positioning Stays Decided | decision ledger + reopen authority | DESIGNED |

Full specs in `catalog/profiles/marketing/`.

## The line

The marketing layer splits:
- *How to write a brief, a campaign doc, an email* → **Skill**
- *Tone, word count, required disclosures* → **Guard** (deterministic)
- *When a claim is supported, when urgency is real, when positioning has drifted* → **xOP** (conditional judgment)
- *Whether the copy is persuasive, on-brand, brilliant* → **Boundary** (human)

## Admission gate

Before filing a marketing candidate as an xOP, run the Admission Test
(`standard/references/admission-test.md`). Most marketing checklists are SOPs or Guards, not
xOPs. The test asks: does the right branch change with observable conditions, and can a fixed
check resolve it? If a parser can fully decide it, it's a Guard.

## Field Notes

`field-notes/` contains honest records of what worked, what over-fired, and what changed.
The 89%-FP status-claim miss is filed there — the most important field note in this lab,
because it shows the exact error the Admission Test prevents: using an xOP where a Guard was
the right instrument.

*IN THE WILD · LAB xOP · DESIGNED — used in real work by its author. Not independently validated.*
