# Guard — Broadsheet Token Compliance

**Guard · DESIGNED · Deterministic**

Checks that rendered output conforms to the Awaken Broadsheet token system. These rules are
machine-checkable. They are not xOPs — the answer is determinate, not conditional.

---

## Rules and tests

### Soft ink — never pure black
- **Rule:** text and borders use `#1b1c1c` (warm near-black). Never `#000000` or `rgb(0,0,0)`.
- **Test:** scan rendered CSS/HTML for `#000`, `rgb(0,0,0)`, `rgba(0,0,0,1)` in `color`,
  `border-color`, `stroke` properties on text or structural elements.
- **PASS:** no pure-black values on text or borders.
- **FAIL:** any `#000` in text or border context → flag line + property.

### Flat surfaces — no shadows
- **Rule:** elevation comes from surface shifts (Paper → Paper-2 → Linen → Sand) and 1px
  hairlines. No `box-shadow`, glow, or blur for elevation on interface surfaces.
- **Test:** scan for any non-`none` `box-shadow` on interface surfaces (cards, panels, nav,
  modals). Exclude text-shadow on display type where explicitly documented.
- **PASS:** no `box-shadow` on interface surfaces.
- **FAIL:** any non-none `box-shadow` on a card, panel, nav, or modal element → flag.

### Mono for numbers — not for body
- **Rule:** Geist Mono signals "audited" — numbers, IDs, evidence statuses, plate markers.
  Never set body copy or headings in Geist Mono.
- **Test:** scan for `font-family: 'Geist Mono'` (or equivalent) on paragraph, heading, or
  body-copy selectors.
- **PASS:** Geist Mono on numeric/ID/status/plate elements only.
- **FAIL:** Geist Mono on `p`, `h1–h6`, `.body`, or general prose selectors → flag.

### One accent — never two hues
- **Rule:** the system is warm-neutral; lavender `#8B7EC8` is the one accent, used as
  punctuation. No second hue, no gradient, no colored status pills beyond the system.
- **Test:** extract all non-neutral foreground colors (not ink, graphite, ash, paper, linen,
  sand, line). Count distinct hues. Flag any non-lavender accent.
- **PASS:** at most one accent hue present; that hue is `#8B7EC8` or within design-documented
  tolerance.
- **FAIL:** any non-system color in a foreground role → flag.

---

## What these are not

These are not xOPs. Each has a deterministic answer: the token is right or it isn't. An exception
clause ("Geist Mono is allowed on kicker labels") does not make a rule conditional — it narrows
the deterministic check. A rule is a Guard when the answer can be computed without judgment.

If a question arises that a fixed check cannot resolve — e.g. "does this layout serve the
slide's communicative job?" — that is an xOP, not a Guard.

---

## Fixtures (not yet written)

`tests/fixtures/broadsheet-tokens/` — minimum: one PASS and one FAIL case per rule.
Status: **DESIGNED**. Rule-tested status requires the fixture suite to run and pass.

---

*DESIGNED — deterministic rules ready; fixtures not yet written; RULE-TESTED status requires
fixture coverage.*
