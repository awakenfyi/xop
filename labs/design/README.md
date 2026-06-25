# Design Lab

**Lab xOP · DESIGNED**

Operating rules for AI in brand, design, and conversion work. An xOP won't give a model taste —
that stays human judgment. It can stop the model from overriding the brief, reverting to generic
patterns, reopening approved decisions, forcing content into the wrong layout, or adding decoration
where signal should be.

*Observed in live brand and design work.*

## The line

**xOPs govern creative conduct, not creative taste.**

- **Taste** — is this beautiful, original, moving, premium? → **human judgment** (a Boundary).
- **Conduct** — did it preserve the brief? was the claim supported? was urgency real? did the
  layout serve the slide's job? was a settled decision silently reopened? → **xOP territory.**

> Design systems tell AI what the brand is made of. Skills teach it how to do the work. xOPs govern
> the moments where judgment matters — when to preserve, when to adapt, when to challenge, when to
> ask, when to stop. *Design xOPs do not automate taste; they stop AI from overriding the brief,
> the evidence, the system, or the human decision without a reason.*

## The xOP Admission Test

A candidate is an xOP when **all five** hold:
1. **A recurring branch decision** — not just a sequence of work.
2. **The correct branch changes with observable conditions** — layout depends on the slide's job.
3. **A fixed check can't fully decide it** — a parser can count layouts but can't always tell
   whether the layout preserves the slide's communicative job.
4. **There's a legitimate opposite error** — flatten every slide → fail; invent a layout per slide
   → opposite fail.
5. **There's an external evaluation path** — source artifact, brief, decision ledger, or independent
   review.

**Classification:** fixed answer → Guard · method/sequence → Skill/SOP · conditional judgment → xOP ·
human-owned taste/authority → Boundary · complete system → Work Pack.

Full gate in `standard/references/admission-test.md`.

## Anchor table — how design xOPs become valid

Every design xOP attaches to an observable, so people can disagree about whether they *love* the
work while still labeling the decision.

| Design concern | Observable anchor |
|---|---|
| Layout fidelity | slide job, hierarchy, surrounding narrative |
| Emphasis | element rank relative to neighbors for the page goal |
| Critique quality | cited basis: task, hierarchy, accessibility, design-system rule |
| Scope drift | brief, approved sections, artifact diff |
| Component reuse | requirements vs existing component capability |

> Bad question: *is this page beautiful?* (taste) · Design xOP question: *did the layout preserve
> the slide's communicative job and hierarchy?* (evaluable conduct).

## The Design xOP set

| ID | Title | Anchor | Full spec |
|----|-------|--------|-----------|
| `xop.design.layout-fit` | Layout Follows the Job | slide job + hierarchy | `catalog/profiles/design/layout-fit.yaml` |
| `xop.design.emphasis-license` | Emphasis Must Be Earned | element rank vs neighbors | `catalog/profiles/design/emphasis-license.yaml` |
| `xop.design.critique-evidence` | Critique With Evidence | cited checkable basis | `catalog/profiles/design/critique-evidence.yaml` |

All three are **DESIGNED**. None have cleared the pilot.

Consolidation (prevents catalog sprawl): "Content Before Template" is a profile/application of
Layout Follows the Job, not a new primitive. "Reuse Before Reinvention" is its opposite-error
side, not a second xOP.

## The Broadsheet

The Awaken Broadsheet (Titan × factory.ai merge) is split into typed objects in
`packs/design-os/`: token Guards (deterministic), a Composition Skill (how to build), the Design
xOPs (conditional judgment), and a Boundary (taste stays human). Original preserved in
`labs/design-xop/examples/awaken-broadsheet.designxop.md`.

## Field Notes

`field-notes/` — honest records of what happened, what overcorrected, and what changed.

```
Observed         what kept going wrong in real work
Candidate rule   the xOP or Guard that seemed to fix it
Anchor           the observable that makes it checkable
Valid exception  when the rule would be wrong
Opposite error   the other direction of failure
What happened    what the tool actually did
What overcorrected  where the fix created new problems
What changed     the revision, retirement, or narrowing
Evidence status  where it stands on the ladder
```

Misses are published. That's what makes the rest credible.

*IN THE WILD · LAB xOP · DESIGNED — used in real work by its author. Not independently validated.*
