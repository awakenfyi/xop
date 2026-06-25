# Composition Skill — Awaken Broadsheet

**Skill · DESIGNED**

How to build the Broadsheet layout system. This is the method, not the judgment — the sequence
of steps, the grid, the modules. The conditional judgment calls (when to reuse a layout, when a
treatment is warranted) live in the Design xOPs.

---

## The system

**Awaken Broadsheet** — a merge of Titan (Wall-Street-broadsheet editorial: type-first, hairlines,
mono for numbers, zero shadows) × factory.ai (warmth: low-glare canvas, soft ink).

The full token set and merge ledger:
`labs/design-xop/examples/awaken-broadsheet.designxop.md`

The live implementation: `site/awaken/assets/site.css`

---

## Build method

### 1. Canvas and surface stack
Start from the surface stack: Paper (`#fbf9f6`) → Paper-2 (`#f4f1ec`) → Linen (`#eeeae3`) →
Sand (`#e3ddd3`). Elevation is a surface change + 1px hairline, never a shadow.

### 2. Grid
12-column grid, 80px section gaps, 1200px max-width. Modules snap to the grid. No free-floating
elements without a column anchor.

### 3. Type hierarchy
- Display: Geist 700, 40–60px, −0.045em tracking
- Section heading: Geist 600, 28–40px, −0.03em
- Body: Geist 400, 16–18px, standard tracking
- Mono (numbers, IDs, statuses): Geist Mono 400/500

Hierarchy from size + weight + tracking. Not from decoration.

### 4. Modules
Standard modules (each is a named, reusable layout unit):
- `hero` — display heading + subhead + CTA
- `stat-row` — one number (Geist Mono, 40px+) + one sentence of context
- `feature-showcase` — product surface image + caption
- `act-divider` — large numeral + single transitional line (centered or sidebar)
- `grid-cards` — 2–4 card grid, linen surface, hairline borders
- `evidence-block` — claim + citation + evidence status badge

### 5. Layout assignment
At this step: invoke `xop.design.layout-fit`. The xOP decides whether to reuse an existing
module or create a named new one. The Skill provides the context; the xOP provides the judgment.

### 6. Token compliance
After layout is complete: run the `broadsheet-tokens` Guard (deterministic). This step catches
any drift from the token rules and runs before release, not after.

### 7. The nine-beat spine (for presentations)
For decks: 9 narrative beats map to module assignments.
1. Context — what's true now
2. Problem — what's breaking or missing
3. Stakes — why it matters
4. Solution — what changes
5. Proof — what the evidence shows
6. How — the method
7. Who — who it's for
8. Ask — what you need
9. Anchor — the one thing to remember

Each beat has a primary module; the xOP governs the cases where the beat's communicative job
doesn't match the default module.

---

*DESIGNED — method documented; xOPs for conditional steps are in `catalog/profiles/design/`.*
