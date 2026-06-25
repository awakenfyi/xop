# Design xOP

**In the Wild · Design Lab · DESIGNED**

A Lab xOP from real design work: turn any web page into a portable **Design xOP** (tokens +
design-conduct rules), then **merge two brands** into one blended system.

## Why this is an xOP, not a style scraper
A flat style guide lists tokens. A Design xOP makes the brand's do's and don'ts into **conduct
rules in xOP shape** — each with a *valid exception* and a *two-direction test*. "Never use color"
becomes "monochrome, except one accent as punctuation — and the test fails both when a second hue
appears *and* when the one CTA has no accent." That's the xOP move: catch the failure and the
opposite error.

- The **skill** (`SKILL.md`) is the method: `extract`, `merge`, `apply`.
- A **Design xOP** is the output: a brand's design operating rules + tokens.
- Merging two = a new blended brand system, with every decision recorded in a merge ledger.

## Field note 041
- **Observed:** I kept hand-blending reference styles (Titan, factory.ai, Nofilter) into our site by
  eye — slow, and the decisions weren't written down, so they drifted.
- **Candidate rule:** extract each reference as a Design xOP (tokens = receipts, do/don'ts = rules),
  then merge with an explicit ledger — one base identity, borrow one or two moves, keep one accent.
- **Valid exception:** for a from-scratch brand with no references, author the Design xOP directly
  instead of extracting.
- **What helped:** the merge ledger made "why this radius / why this ink" reviewable; "subtract,
  don't accumulate" stopped the blend from becoming a union of every token.
- **Where it overcorrected:** first pass tried to keep *both* brands' personalities — read as
  neither. Fix: name one base, demote the other to an accent.
- **Status:** DESIGNED. Used in real work by its author; not validated, not a universal method.

## Worked example
`examples/awaken-broadsheet.designxop.md` (+ `.tokens.json`) — our own site, produced by merging
**Titan × factory.ai**. It's a real merge: the ledger shows warm cream between Titan's white and
factory's grey, ink softened off pure black, rounded radii adopted, one lavender accent kept. The
live build (`site/awaken/assets/site.css`) is the same system — spec and implementation in sync.

## Honesty boundary
- Tokens are **observed** (verifiable against the source page); the voice + rules are **DESIGNED**
  interpretation; merge decisions are **choices**, not discoveries.
- Record source URL + date. Study a brand's *system*; don't reproduce its logo, copy, or assets.
- A blended Design xOP is named as a blend and attributed to both sources. No claim it's "optimal."

## Files
- `SKILL.md` — the extract / merge / apply skill.
- `examples/awaken-broadsheet.designxop.md` — the dogfood merge (Titan × factory.ai).
- `examples/awaken-broadsheet.tokens.json` — W3C design tokens for it.
