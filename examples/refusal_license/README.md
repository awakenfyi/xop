# Refusal License xOP  *(flagship reference)*

> **Is this refusal still warranted by the *current* request?**

The flagship instance, and the one most likely to make xOP a category — because here the gate
(`false_positive_on_warranted == 0`) is an **engineering requirement**, not a nicety. A
support agent that drops a warranted refusal, a healthcare agent that drops warranted caution, a
coding agent that drops a warranted block — those are shippable failures the whole industry already
worries about.

Same fixed engine as every xOP (`../../CONSTITUTION.md`); only the skin below is domain-specific.

## What ships in a reference xOP

```
refusal_license/
  README.md                     this file
  refusal_license_xop.md        the authored xOP (the procedure)
  examples/                     illustrative worked transcripts (authored, NOT gold)
  failures/                     pointers to the blind spots that bite this xOP
  gold/candidates.json          UNLABELED candidate cases (a human labels them, blind)
```

**On the gold folder:** the cases ship `gold_license: null` on purpose. A reference xOP does not
get to label its own evaluation set — that would violate the labeling protocol
(`../../harness/phase1/LABEL_PROTOCOL.md`). The candidates are *sourced* here; gold is produced by
≥2 blind humans via the harness pipeline. This is the discipline that keeps the library from
becoming model-grades-model.

## The direction of the gate (important)

For refusal, **abstain leans toward keeping the refusal, not dropping it.** When you can't tell
from the text whether the current ask re-triggers the refusal, holding is the conservative move.
Dropping a refusal the request still warrants is the dangerous failure (`concept/License_Taxonomy.md` §4).
