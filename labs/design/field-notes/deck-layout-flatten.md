# Field Note — deck-layout-flatten

**Lab:** Design Lab · **Status:** Lab xOP (narrowed) · **xOP:** `xop.design.layout-fit`
*Observed in live CMO-level brand and design work.*

---

## Observed
When building lo-fi wireframes from source decks, the model consistently forced every slide into
the default skeleton layout — title + content block — regardless of what the slide was actually
doing. An act-divider slide (marking a narrative transition with a large numeral and a single
line) became a standard content slide. A stat-showcase slide (one number, one sentence of
context) got a full title + three-bullet layout. The communicative job of each slide disappeared.

Called internally: the "Spark act-divider error" — the model recognized the content type but
overrode the layout requirement.

## Candidate rule
The model needed a rule that said: observe the slide's communicative job before reaching for
the template. If an existing layout preserves the job, reuse it; if no existing layout does,
create and name one. Never claim fidelity while removing the job.

## Anchor
The slide's communicative job, inferable from: source slide image + extracted text + position
in the deck + surrounding slides. An independent reviewer with those four inputs can label
whether the chosen layout preserved or flattened the job — without needing to like the design.

## Valid exception
If the designer explicitly selected the layout, or if an exact mapping rule resolves the
placement (e.g. all section covers use the divider layout), the xOP does not apply. Explicit
specification beats the judgment rule.

## Opposite error
Creating a brand-new one-off layout for a slide that an existing layout already served. Layout
proliferation — a different failure than flattening, but also a failure. The xOP must catch
both directions; the evaluation must measure both.

---

## What happened
The rule worked as intended for the clear cases: act-dividers, stat-rows, and feature-showcase
slides were correctly identified as needing distinct layouts when the default would flatten them.

## What overcorrected
The early formulation of the rule had no reuse gate — it favored creating new layouts and
required explicit justification for reuse. This produced unnecessary layout proliferation on
slides where the default was genuinely right. Three slides in one session got bespoke layouts
that served no purpose the standard layouts hadn't already covered.

The rule was also initially framed too broadly — as an xOP for the entire deck build process.
That was wrong. The deck build is an SOP. The layout assignment step is the one place where
conditional judgment lives. Framing the whole procedure as an xOP caused confusion about when
it should fire.

## What changed
1. The rule was narrowed to the layout assignment step only. The rest of the deck build is
   an SOP (`standard/references/admission-test.md` — SOP-with-embedded-xOP composition).
2. A reuse gate was added: `reuse_existing` is the default when an existing layout preserves
   the job. `create_distinct` requires a positive reason — a specific aspect of the slide job
   that no existing layout preserves.
3. The opposite error became a first-class metric in the evaluation plan, not a note.

Current spec: `catalog/profiles/design/layout-fit.yaml`.

## Evidence status

Current status: **DESIGNED**

The evaluation plan calls for 40-60 source/rebuild slide pairs with ≥2 independent designer
labels (reuse_existing / distinct_required / undecidable). This has not run. The rule holds
in the author's own work; that is not independent validation.

---

*IN THE WILD · LAB xOP · DESIGNED — used in real work by its author. Not independently validated.*
