---
name: design-xop
title: Design xOP
summary: Turn any web page into a portable Design xOP (tokens + design-conduct rules), and merge two brands into one blended system.
status: DESIGNED
lab: design
type: lab-xop
---

# Design xOP

Turn any web page into a **Design xOP** — a portable spec that captures a brand's design
*tokens* (what's measurable) and its design-*conduct rules* (what an AI must and must not do to
stay on-brand). Then **merge two Design xOPs** into one blended system.

A Design xOP is an xOP applied to design: the brand is the warrant, the do's are the working
rules, the don'ts are the never-break rules, and each rule carries a **valid exception** and a
**test**. Tokens are the receipts.

> One-line: an xOP is a correction with a valid exception and a test for both directions. A
> Design xOP is the same shape, applied to how an AI designs in a brand.

## Modes

| Command | Does |
|---|---|
| `/design-xop extract <url, screenshot, or pasted CSS>` | Produce a Design xOP (MD + tokens.json) from the page. |
| `/design-xop merge <A> <B>` | Blend two Design xOPs into one, with a stated conflict resolution. |
| `/design-xop apply <design-xop>` | Generate CSS custom properties / Tailwind theme from a Design xOP. |

## What honesty requires (read first)
- **Tokens are observations — receipts.** Colors, sizes, radii, spacing are read off the page and
  must be verifiable against it. Don't invent values; if you can't see it, mark it `inferred`.
- **The narrative + rules are interpretation — `DESIGNED`.** The "voice," do's/don'ts, and
  philosophy are a reading of the page, not facts. Label them as design judgment.
- **A merge is a set of choices, not a discovery.** Every conflict resolved must say *which brand
  won and why*. Never imply the blend is "validated" or "optimal."
- **Attribution + license.** Record the source URL and date. Extract a brand's *system* to learn
  from; don't reproduce its logo, copy, or proprietary assets. This is a study tool, not a cloner.

---

## EXTRACT — page → Design xOP

1. **Read the page.** Prefer a rendered read (screenshot + DOM/CSS). Capture: palette, type
   families + scale, spacing rhythm, border-radii, borders/shadows, component patterns, layout
   grid, imagery treatment, motion.
2. **Derive tokens** (the receipts). Emit a W3C design-tokens `tokens.json` (`$value`/`$type`/
   `$description`) for `color`, `font`, `typography`, `spacing`, `radius`, `surface`.
3. **Write the Design xOP MD** using the template below. Every color/size is a token; every
   "always/never" is a conduct rule with a valid exception and a test.
4. **Status it.** Tokens = observed (cite the URL). Rules/voice = `DESIGNED`. Note anything
   `inferred` (not directly visible).

### Output template (MD)
```
# <Brand> — Design xOP
> <one-line essence>   ·   source: <url> · extracted <date> · tokens: observed · rules: DESIGNED

## Essence (DESIGNED — interpretation)
<2–4 sentences: the design's core move and what carries the voice.>

## Tokens — Colors        (observed)
| Name | Value | Role |
## Tokens — Typography     (observed; families may be substituted)
families · weights · scale (size / line-height / tracking) · opentype features
## Tokens — Spacing & Shape (observed)
base unit · spacing scale · radii (per element) · layout (max-width, section gap, padding)
## Surfaces & Elevation    (observed)
surface levels + the elevation philosophy (shadow vs hairline vs tonal)

## Design-conduct rules (xOP form)
For each rule:
- **Rule** (the working rule / "do")
- **Applies when** (the observable condition)
- **Valid exception** (when the opposite is correct)
- **Never** (the never-break version / "don't")
- **Test** (how to check a generated page obeys it — and catches the opposite error)

## Imagery & Motion          (observed + DESIGNED)
## Quick Start               (CSS custom properties + Tailwind @theme from tokens.json)
```

### Turning a "do/don't" into a rule (the xOP move)
A flat style guide says *"Never use color."* A Design xOP says:

> **Rule** Monochrome — color carries no meaning here.
> **Applies when** Any surface, state, or decorative element.
> **Valid exception** A single accent used as punctuation (≤1 element per screen).
> **Never** Introduce a second hue, gradient, or colored status pill.
> **Test** Scan the rendered page: count distinct hues. >1 accent → FAIL. Zero accent where the
> one CTA should stand out → also FAIL (the opposite error).

That two-direction test is what makes it an xOP, not a mood board.

---

## MERGE — two Design xOPs → one

Merging is reconciliation, and it must be **explicit**. Never silently average two systems.

1. **State the intent.** Which brand is the *base* (structure/identity) and which is the *accent*
   (what you're borrowing)? e.g. "Base: Titan's editorial structure. Borrow: factory.ai's softness."
2. **Resolve each token group** and record the decision + reason in a **merge ledger**:

   | Group | Brand A | Brand B | Decision | Why |
   |-------|---------|---------|----------|-----|
   | Canvas | #fff | #eee | warm cream #fbf9f6 | between the two; softer than A, warmer than B |
   | Ink | #111 | — | #1b1c1c | soften off pure black per "not black" |
   | Type | Geist | Geist | Geist | shared; keep |
   | Radius | 0px | rounded | pills + 24px cards | adopt B's softness |
   | Accent | none | none | one lavender (ours) | the one deliberate divergence |

3. **Reconcile the rules.** When two conduct rules conflict, keep the one that serves the *intent*,
   and rewrite its valid exception to absorb the loser. Conflicting "never"s must be resolved, not
   stacked — a system can't both "never round" and "always round."
4. **Emit the blended Design xOP** (MD + tokens.json) + the merge ledger. Mark `DESIGNED`. Name it.
5. **Apply + check.** Generate the CSS, render a page, and run the rule tests from both parents:
   the blend should pass the rules it chose to keep and consciously break the ones it dropped (and
   say which).

### Merge guardrails
- **One base identity.** A blend with two competing personalities reads as neither. Pick a base.
- **Subtract, don't accumulate.** Borrow one or two moves from B; don't union every token. (This is
  the Lyra rule applied to design: keep what's essential, drop the rest.)
- **Keep one accent.** If both bring color, choose one. Two accents = no accent.
- **Honesty in the name.** Call it a blend ("Titan × factory") and cite both sources.

---

## Definition of done
- [ ] `tokens.json` (W3C format) emitted; values verifiable against the source.
- [ ] Design xOP MD with conduct rules in xOP form (rule · applies-when · valid exception · never · test).
- [ ] Source URL + date recorded; tokens=observed, rules=`DESIGNED`, anything unseen=`inferred`.
- [ ] (merge) a merge ledger with a decision + reason per token group; one base, one accent.
- [ ] `apply` produces CSS/Tailwind that a page can adopt; rule tests run against the render.

*This is a Lab xOP — DESIGNED, used in real design work by its author, not validated doctrine.
See `README.md` and `examples/`.*
