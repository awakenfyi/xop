# awaken.fyi — Broadsheet × Arcade flare — Design xOP
> Minimalist editorial base, with arcade.dev *energy* borrowed and translated into our palette.
> sources: awaken Broadsheet (Titan × factory.ai) + arcade.dev · assembled 2026-06-21 · tokens: observed · rules: DESIGNED
> note: rk.dev could not be read (client-rendered; fetch + browser timed out) — not included; add its export later.

## Merge intent
- **Base (identity, 80%):** the awaken Broadsheet — warm paper, Geist, mono numbers, one lavender
  accent, hairlines, no shadows. Restraint is the brand.
- **Borrow (flare, 20%):** arcade.dev's *confidence and energy* — not its neon. One dramatic dark
  band, one rationed glow, a bolder display, a single motion beat.
- **Hard line:** arcade's lime→magenta gradient and dark-default UI do **not** come across. The flare
  is rationed and recolored to lavender. Minimalism wins every tie.

## Merge ledger
| Group | Broadsheet (base) | arcade.dev | Decision | Why |
|-------|-------------------|-----------|----------|-----|
| Canvas | warm cream `#fbf9f6` | near-black | **stay cream** | base identity; dark is rationed, not default |
| Accent | one lavender `#8B7EC8` | lime→magenta gradient | **lavender only**; gradient allowed *once*, in lavender→transparent | translate arcade's energy into our hue; never neon |
| Dark surface | footer + one statement card | whole UI | **one "Signal" band per page** | borrow the drama, ration it to a single section |
| Display | Geist 700, −0.045em | huge, ultra-tight | **bump hero to 64–72px, −0.05em** | adopt arcade's confident scale on the hero only |
| Glow | none | neon glow everywhere | **one soft lavender radial, behind the dark band only** | a single flare moment, not ambient |
| Motion | none | video bg, animated | **one reveal beat** (the pause/flip), `prefers-reduced-motion` honored | borrow life, keep it quiet |
| Structure | plates, rail, ladder | three-walls, tabs, FAQ | **keep ours**; already arcade-adjacent | both are editorial-structured; no change |

## Tokens added on top of the Broadsheet
| Name | Value | Role |
|------|-------|------|
| Signal Ink | `#15151a` | the one dark "Signal" band background (cooler than footer ink for drama) |
| Glow | `radial-gradient(60% 60% at 70% 30%, rgba(139,126,200,.30), transparent 70%)` | the single rationed lavender glow, behind dark bands only |
| Display-XL | Geist 700 · clamp(48px,7vw,72px) · −0.05em | hero only |

## Design-conduct rules (xOP form) — the flare, governed
**Flare is rationed**
- Rule: arcade energy appears at most once per page — one dark "Signal" band with one lavender glow.
- Applies when: a page needs a moment of drama (hero or a single pivotal section).
- Valid exception: the home may use two (hero + closing CTA) since it carries the brand.
- Never: dark-default the whole page, or place more than one glow in view.
- Test: count dark bands + glows per page; >1 (>2 on home) = FAIL; a flat page with zero energy on the
  hero where the brand should land = also FAIL (opposite error).

**Neon never; lavender always**
- Rule: arcade's confidence comes through, its colors do not.
- Applies when: any accent, gradient, or glow.
- Valid exception: a single lavender→transparent radial behind a dark band.
- Never: lime, magenta, multi-stop neon, or any second hue.
- Test: scan for hues other than the lavender family → FAIL.

**Motion is one quiet beat**
- Rule: borrow arcade's life as a single reveal (the pause/evidence-flip), not ambient animation.
- Applies when: the one interaction that explains the product.
- Valid exception: none beyond that one beat.
- Never: looping gradients, video backgrounds, parallax, autoplaying motion.
- Test: `prefers-reduced-motion` disables it; more than one animated element = FAIL.

**Restraint wins ties**
- Rule: when flare and minimalism conflict, minimalism wins.
- Applies when: any judgment call between energy and quiet.
- Valid exception: the hero, where confidence is the point.
- Never: let "flare" become the default texture of the site.
- Test: remove the flare — the page still reads as complete and on-brand = PASS.

## Apply
A reference build of the flare (dark Signal band + one lavender glow + bold display, restraint
elsewhere) can be generated from these tokens onto `site/awaken/`. Recommended placement: the home
hero and the closing CTA only — everywhere else stays the clean Broadsheet.

*Status: DESIGNED. An openly-attributed blend (Broadsheet × arcade.dev). The flare is borrowed energy,
recolored and rationed — not a reproduction of arcade's neon system.*
