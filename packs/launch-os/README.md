# Launch OS

**Work Pack · PLANNED · DESIGNED**

> **PLANNED:** this pack is scaffolded. The xOP specs are DESIGNED; no Guards have fixtures;
> the pilot has not run. Not yet usable as a system.

A complete system for AI in product marketing launch work. Combines Guards (deterministic
compliance checks), marketing xOPs (conditional judgment rules), and a Boundary (what stays
human).

---

## Scope

Launch execution: the work from approved positioning through live assets. Not brand strategy
(that's an earlier human decision). Not creative direction (Boundary). The layer between
"positioning is approved" and "assets are live, instrumented, and owned."

## What would be in this pack

```
packs/launch-os/
├── README.md              this file
├── pack.yaml              machine-readable manifest (see below)
├── guards/
│   └── launch-checklist.guard.md     asset / approval / owner / instrumentation
└── boundary.md            what stays human
```

## xOPs that apply

| ID | Title | Governs |
|----|-------|---------|
| `xop.claim.evidence-bound` (profile: marketing) | Claims Need Receipts | every factual, comparative, performance claim in launch copy |
| `xop.marketing.urgency-evidence` | No Made-Up Urgency | urgency / scarcity language in launch CTAs |
| `xop.decision.ledger` (profile: positioning) | Positioning Stays Decided | downstream launch assets preserve approved audience + differentiation |
| `xop.verify.completion` (profile: launch) | Done Means Verified | an asset is not complete until it exists at destination with owner and instrumentation |

Full specs in `catalog/profiles/marketing/` and `catalog/core/`.

## What this pack does not cover

Creative quality, campaign strategy, channel mix, pricing decisions. Those are human.

*PLANNED — scaffold only. Build order: xOP specs first (done), Guards + fixtures second,
pilot third.*
