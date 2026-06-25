# Cursor — Design xOP
> Warm-paper command center: cream pages, espresso-black type, one rationed accent. A dev tool that reads like a well-set journal.
> source: styles.refero.design (Cursor / cursor.com export, 2026-06-03) · tokens: observed · rules: DESIGNED

*A reference Design xOP. Note how close it is to the awaken Broadsheet — Cursor is, almost exactly, our
warm-paper system with an orange accent instead of lavender. Strong validation of the direction.*

## Essence
95%+ achromatic warm neutrals, so the one accent carries weight. A single humanist-with-mono-DNA
typeface (CursorGothic, weight 400) does all the work via size + tight negative tracking — no bold.
Mono (Berkeley Mono) only for code. The product screenshot, floating with a soft shadow, is the hero.

## Tokens — Colors (observed)
| Name | Value | Role |
|------|-------|------|
| Espresso Ink | `#26251e` | text, dark filled buttons — warm near-black, never pure #000 |
| Page Parchment | `#f7f7f4` | canvas |
| Card Stone | `#e6e5e0` | card / section banding |
| Border Sand | `#d9d5cf` | hairlines |
| Muted Clay | `#7a7974` | secondary text |
| Ember Orange | `#f54e00` | the single accent — interactive moments only (link hover/underline) |

## Tokens — Type / Shape (observed)
- CursorGothic 400 across the board; display 72px at −0.03em; headings 26–36px; body 16px. Mono for code.
- Radii: **buttons pill (9999px)**, cards 8px, tags/inputs 4px. Soft layered shadows on screenshot cards.
- Layout: 1200px, 64px section gaps, alternating Parchment / Card-Stone bands, text+screenshot splits.

## Design-conduct rules (xOP form)
**One accent, rationed**
- Rule: keep the surface 95%+ achromatic warm neutral; the accent appears only on interactive moments.
- Valid exception: a supporting accent (green/gold) on product-chrome illustration, never as status.
- Never: a chromatic background fill or a colored CTA stroke.
- Test: count chromatic fills on a screen; >1 = over-designed = FAIL.

**Warm ink, never black**
- Rule: text + filled buttons use Espresso Ink `#26251e`.
- Never: pure `#000`.
- Test: grep render for `#000`/`rgb(0,0,0)` in text/buttons → FAIL.

**One typeface, one weight**
- Rule: CursorGothic 400 everywhere; emphasis from size + tracking, not bold; mono only for code.
- Valid exception: a rare serif (EB Garamond) for a pull-quote.
- Never: render code in the sans, or add a second sans family.

## What awaken can borrow (the merge note)
Cursor ≈ awaken Broadsheet with an orange accent. Differences worth a decision:
| | Cursor | awaken (current, post-Basement) |
|---|---|---|
| Accent | ember orange `#f54e00` | lavender `#8B7EC8` |
| Buttons | **pill (9999px)** | **sharp (0)** |
| Shadow | soft, on screenshot cards only | none (flat) |
| Section rhythm | alternating Parchment / Card-Stone bands | paper / paper-2 bands ✓ already close |

The live fork: **Cursor's pills + one soft product-card shadow** vs **Basement's sharp + flat**. Both are
world-class warm-paper systems; pick one base and ration the other. (This is a Design xOP merge:
awaken Broadsheet × Cursor × Basement.)

*Status: DESIGNED reference. Tokens observed from the refero export; rules are interpretation.*
