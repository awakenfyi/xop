# Field Note — status-claim-89pct-fp

**Lab:** Marketing Lab · **Status:** Guard (narrowed) · **Finding:** APC boundary — Guard vs xOP
*Observed in live CMO-level marketing work.*

---

## Observed
An early version of a status-claim rule was authored as an xOP: "state a claim about a project's
status only when the evidence supports it." The intent was to catch over-confident status
reporting (calling something DONE before it was verified, or calling something GREEN when it
was actually AT-RISK).

When evaluated against real project update samples, the xOP-framed rule flagged 89% of the
cases as requiring intervention — including clear, well-supported claims with explicit evidence
behind them. A project genuinely GREEN, with a working demo and passing tests, was flagged as
needing hedging. A confirmed DONE state, with artifact at destination, was flagged as needing
qualification.

## Candidate rule
The original candidate: "do not state a project status claim at a strength the evidence does
not support." Intended to catch status theater (claiming green while the codebase is red) and
premature done-calls.

## Anchor
The apparent anchor: "is the status claim supported by the evidence?" This looked evaluable.

## Valid exception
When the evidence genuinely and clearly supports the stated status — the build passes, the
artifact exists at the destination, the reviewer has confirmed the outcome — the claim is
warranted and should be stated without hedging.

## Opposite error
Forcing hedges onto well-supported status claims produces epistemic noise: every update becomes
uncertain regardless of actual project state. A team stops trusting status reports.

---

## What happened
The 89% false positive rate was the result of a layer error, not a calibration problem. The
rule was framed as an xOP — requiring judgment about whether the evidence sufficiently supports
the claim — when the underlying check was mostly deterministic: is there an artifact? does the
test pass? is the completion criterion named? These are checkable against the environment, not
judgment calls.

The xOP was firing on warranted claims because it had no way to read the environmental evidence
itself. It saw "DONE" and applied a hedging rule without checking whether the artifact actually
existed. This is the APC finding: **don't let the deterministic Guard step do judgment — and
don't let an xOP frame what should be a Guard.**

## What overcorrected
The early fix was to add more exceptions to the xOP rule — "unless the artifact exists, unless
tests pass, unless..." This made the rule longer and harder to evaluate, not more accurate. The
right fix was a layer reclassification.

## What changed
The rule was split into two instruments:

1. **Guard** — deterministic check: is the completion evidence named and present? (artifact at
   destination, test result, acceptance criteria stated). This is checkable. If the check fails,
   flag for review; do not automatically hedge. Reaches RULE-TESTED through fixture coverage.

2. **xOP** — narrow remainder: when the completion criterion is ambiguous and the model must
   judge whether the evidence *at that strength* warrants the stated confidence. This is a much
   smaller surface than the original xOP covered. Both `xop.verify.completion` (core) and
   `xop.claim.evidence-bound` (core) govern this remainder.

The 89% FP rate collapsed to near-zero after the reclassification, because the Guard only fires
when a checkable completion criterion is absent — not on every status claim.

## Evidence status

Current status: **DESIGNED** (the split instruments)

The narrow xOP remainder inherits status from the core xOPs it maps to. The Guard's
deterministic component is ready for fixture coverage. Neither has been independently labeled.
The 89% FP figure is from the author's own evaluation run — not a blind independent sample.

---

**What this field note establishes:**

The APC finding and this finding operate at different levels:
- **Within an xOP:** don't let the deterministic Guard component do judgment (gate too broad → FP).
- **At instrument selection:** don't frame a deterministic check as an xOP at all (catalog sprawl).

Right instrument, right layer, right unit. That's what prevents the 89%.

---

*IN THE WILD · LAB NOTE · DESIGNED — used in real work by its author. Not independently validated.*
