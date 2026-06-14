# examples — the reference xOP library

The specification isn't the product; the **library** is. People adopt *Refusal License*, not *the
xOP Specification* — the same way they adopt websites, not the HTTP RFC. Each reference xOP is the
one fixed engine (`../CONSTITUTION.md`) wearing a domain skin: a different triggering condition,
signal set, license logic, surface question, and hand-offs.

## The lead is the interpretive domains

The standard's home is the **interpretive / humanities** surfaces — writing, editing, coaching,
teaching, criticism (`../concept/INTERPRETIVE_DOMAINS.md`). The lead is **writing**, because there
`x` is observable (prose read cold) *and* the call is interpretive — the one place you can validate
the judge against a real residual before carrying it inward to coaching. Refusal stays as the
cleanest *agent-surface engineering* exemplar, not the flagship.

| xOP | Surface | The question | Status |
|---|---|---|---|
| **Writing License** | author + editor | Is this choice warranted by the piece, or inherited register? | **built (interpretive flagship)** → `writing_license/` |
| **Refusal License** | agent | Is this refusal still warranted? | **built (agent-surface exemplar)** → `refusal_license/` |
| Boundary License | human | Is the *no* still warranted? | scaffold — to author |
| Feedback License | human | Is withholding still warranted? | scaffold — to author |
| **Coaching (COP)** | human | Is this reaction/limit still warranted? | **built (felt core)** → `coaching_cop/` (anchor-gated, stated-license scope) |

Together these prove one engine across surfaces: an interpretive artifact (writing), an agent stance
(refusal), and the felt core (coaching) — without sprawling into a catalog, which would contradict
the format's subtractive claim (`../concept/03_REVIEWER_GUIDE.md` §soft-spot 4).

## What each reference xOP ships with

```
<name>/
  README.md                 what it is, the direction of the gate
  <name>_xop.md             the authored procedure (the skin)
  examples/                 illustrative worked transcripts (authored, NOT gold)
  failures/                 pointers to the blind spots that bite this xOP
  gold/candidates.json      UNLABELED candidate cases (humans label, blind)
```

The gold folder is always unlabeled on arrival. A reference xOP does not label its own evaluation
set — that's the line in `../harness/phase1/LABEL_PROTOCOL.md` that keeps the library from becoming
model-grades-model.

## Building the next four

Use `../tools/xop_builder.md`. Every candidate must survive **Step 2 (Boundary Test)** — *can the
state be warranted in some cases and inherited in others, and is abstaining sometimes right?* If
no, it's an SOP; stop. That one gate is what keeps the library from inflating.
