# awaken Broadsheet — Design xOP
> Editorial broadsheet on warm paper: clean geometric sans, mono for numbers, one lavender accent.
> source: a merge — Titan (styles.refero.design) × factory.ai · assembled 2026-06-21 · tokens: observed (from our build) · rules: DESIGNED

*This is a worked **merge** example for the Design xOP skill. It's our own site system, produced by
blending two source Design xOPs. The merge ledger below shows every decision.*

## Merge intent
- **Base (structure + identity):** Titan — Wall-Street-broadsheet editorial: type-first, pill
  buttons, rounded cards, mono for numbers, hairline borders, no shadows.
- **Borrow (one move):** factory.ai — *softness*: a warm, low-glare canvas and a softened ink that
  is never pure black.
- **Keep (ours):** a single lavender accent, used as punctuation — the one deliberate divergence
  from Titan's pure monochrome.

## Merge ledger
| Group | Titan | factory.ai | Decision | Why |
|-------|-------|-----------|----------|-----|
| Canvas | `#ffffff` | `#eeeeee` (warm light) | **`#fbf9f6`** warm cream | between the two; softer than white, warmer than grey |
| Ink | `#111111` | softened (not black) | **`#1b1c1c`** | honor "not black"; warm near-black |
| Secondary text | `#615e5b` graphite | — | **`#615e5b`** | keep Titan's warm graphite |
| Card surface | `#e9eaeb` linen | soft grey | **`#eeeae3`** warm linen | warm the linen to match the cream canvas |
| Type | Geist + Geist Mono | clean sans | **Geist + Geist Mono** | shared choice; keep |
| Display | Geist 700 sans | sans | **Geist 700, −0.045em** | adopt Titan's sans display (drop our earlier serif) |
| Radius | pills 160px / cards 32px | rounded | **pills 999px / cards 24px** | adopt rounded; tighten cards for density |
| Mono usage | numbers only | — | **numbers, IDs, statuses, plates** | keep mono as the "audited" signal |
| Accent | one black CTA | none | **one lavender `#8B7EC8`** | our brand; same "single accent as punctuation" logic |
| Elevation | zero shadow | flat | **zero shadow** | both agree; depth via hairlines + surface shifts |

## Tokens — Colors (observed, from our build)
| Name | Value | Role |
|------|-------|------|
| Ink | `#1b1c1c` | text, structural hairlines — soft warm near-black, never pure #000 |
| Graphite | `#615e5b` | secondary text |
| Ash | `#8a8784` | tertiary / fine print |
| Paper | `#fbf9f6` | warm cream canvas |
| Paper-2 | `#f4f1ec` | section wash |
| Linen | `#eeeae3` | card surface |
| Sand | `#e3ddd3` | accent surface / divider |
| Line | `#dcd7ce` | hairline |
| Accent | `#8B7EC8` | the single accent — used as punctuation |

## Tokens — Typography (observed)
- **Geist** — all UI + display. Weights 400 / 500 / 600 / 700. Display 40–60px at −0.045em;
  section headings 28–40px / 600 at −0.03em; body 16–18px / 400.
- **Geist Mono** — numbers, IDs, evidence statuses, plate markers (`PL. 0X`), code. Weights 400/500.
- Scale: 12 (label) · 14 · 16 (body) · 18 · 20 · 24 · 28 (stat) · 40 (heading) · 60 (display).

## Tokens — Spacing & Shape (observed)
- Base 4px · section gap 80px · card padding 24px · element gap 16px · max-width 1200px.
- Radii: buttons/nav/chips **999px** (pill) · cards/panels **24px** · tags/status **999px** ·
  inputs **12px** · small panels **18px**.

## Surfaces & Elevation
Paper → Paper-2 → Linen → Sand, with 1px hairlines. **Zero shadows** — depth from surface shifts
and borders, never z-axis.

## Design-conduct rules (xOP form)
**Monochrome + one accent**
- Rule: the system is warm-neutral; color carries no meaning except the one accent.
- Applies when: any surface, state, or decorative element.
- Valid exception: lavender `#8B7EC8` as punctuation — sparingly, where one thing must stand out.
- Never: a second hue, gradient, or colored status pill.
- Test: count distinct hues on the render; >1 accent = FAIL; zero accent on the primary CTA = FAIL.

**Soft ink, never black**
- Rule: text and hairlines use `#1b1c1c`.
- Applies when: any ink usage.
- Valid exception: none needed — the softness is the brand.
- Never: pure `#000000` for text or borders.
- Test: grep the render for `#000`/`rgb(0,0,0)` in text/border → FAIL.

**Mono is for numbers**
- Rule: Geist Mono signals "audited" — numbers, IDs, statuses, plate markers.
- Applies when: a value is numeric, an identifier, or an evidence status.
- Valid exception: short editorial labels (kicker/plate) may use mono for the technical register.
- Never: set body copy or headings in mono.
- Test: any paragraph/heading in mono → FAIL.

**Flat, no shadows**
- Rule: separation comes from hairlines + surface shifts.
- Applies when: any need to distinguish a surface or set an element apart.
- Valid exception: none.
- Never: `box-shadow`, glow, or blur for elevation.
- Test: any non-`none` box-shadow on an interface surface → FAIL.

**Type does the work**
- Rule: hierarchy from size/weight/tracking, not chrome.
- Applies when: establishing emphasis or structure.
- Valid exception: a single hairline or surface shift to group content.
- Never: decorative dividers, drop-shadow cards, or icon clutter to fake hierarchy.
- Test: a section that reads flat without its decoration = PASS; one that collapses = FAIL.

## Quick Start (CSS custom properties)
See `awaken-broadsheet.tokens.json` for the machine-readable tokens; the live implementation is
`site/awaken/assets/site.css`. This Design xOP and that stylesheet are the same system — one is the
spec, the other the build.

*Status: DESIGNED. A blend, openly attributed to Titan × factory.ai. Not a claim that this is the
optimal system — it's the one we chose, with reasons recorded.*
