# Design OS

**Work Pack · PREVIEW · DESIGNED**

A complete system for AI in brand and design work. Combines Guards (deterministic token checks),
a Composition Skill (how to build the layout system), Design xOPs (conditional judgment rules),
and a Boundary (what stays human).

> **PREVIEW:** the xOP specs are DESIGNED; the Guards need fixtures; the pilot has not run.
> This pack is usable as a reference system for its author's own work. It is not validated for
> team adoption.

---

## What's in this pack

```
packs/design-os/
├── README.md              this file
├── pack.yaml              machine-readable pack manifest
├── guards/
│   └── broadsheet-tokens.guard.md    token compliance (deterministic)
├── skill.md               Composition Skill — how to build the layout system
├── design-xops.md         which Design xOPs apply and when
└── boundary.md            what stays human judgment
```

## The Awaken Broadsheet system

The design system underlying this pack is the Awaken Broadsheet — a merge of Titan
(Wall-Street-broadsheet editorial) × factory.ai (warmth, low-glare canvas). The full merge
ledger and token set are in `labs/design-xop/examples/awaken-broadsheet.designxop.md`.

This pack reclassifies that artifact into typed objects: Guards for the deterministic rules,
a Skill for the build method, xOPs for the conditional judgment calls, and a Boundary for taste.

## Object types (why this matters)

The Broadsheet artifact originally mixed these — tokens described as xOPs because they had an
exception, procedures framed as conduct rules. The reclassification makes each layer
instrumentable and testable on its own terms:

| Layer | What it governs | Instrument | Gate |
|-------|-----------------|------------|------|
| Tokens | `#1b1c1c`, no shadows, Geist Mono for numbers | **Guard** | deterministic fixture |
| Build method | grid, rhythm, modules, the nine-beat spine | **Skill** | method review |
| Conditional judgment | layout fidelity, emphasis, critique | **xOP** | blind human labels |
| Taste / quality | is it beautiful, premium, right for the brand | **Boundary** | human |

## Activation

Use **one primary xOP + at most two supporting** per task.

```
Building a deck:      SOP (deck build) → xop.design.layout-fit (layout step)
Design review:        xop.design.critique-evidence
Adding hero section:  xop.design.emphasis-license
Token compliance:     broadsheet-tokens Guard (deterministic, before any xOP)
```

*MIT licensed · Lyra Labs*
