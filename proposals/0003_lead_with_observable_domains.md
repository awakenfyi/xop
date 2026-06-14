# Proposal 0003 — Lead V1 with observable domains (anchor the felt ones)

- **xOP:** standard-wide (scope / domain policy)
- **From insight:** external review (Gemini, 2026-05-31) — "deprecate the felt domains"
- **Type:** taxonomy-change (scope) + docs
- **Severity:** P2 for the launch-sequencing part; **P4** for the felt-deprecation part (it touches
  the unification claim — flagged, not merged as a doc tweak)
- **Risk:** Medium (launch lead) / High (full deprecation)
- **Status:** PROPOSED — **partially accepted, reframed.** Full deprecation rejected.

---

## What the gap is
The residual `L = x − x̂` needs `x` (the actual) observable independently of `x̂` (the claim). In
felt domains (coaching, emotional, feedback) `x` is only available as self-report — `x̂` again. The
review concluded: cut coaching/emotional/feedback for V1; ship only domains with an externally
verifiable artifact (refusal, compliance, code, copy).

## The proposed change (reframed)
**Accepted:** lead the V1 launch with the **observable/agent surface** — refusal, caution/safety,
compliance, code, copy. `x` is readable by a cold stranger; the gate has measurable mechanics;
this is the surface that earns enterprise credibility. (`examples/refusal_license/` is already the
flagship.)

**Rejected as drafted:** *deleting* emotional/boundary/feedback license from the taxonomy.
Replaced with a surgical guard:

> A felt-domain xOP is valid only if it can name a **datable present-condition anchor** — a
> checkable fact in the transcript about whether the triggering condition is *currently present*
> ("took credit in yesterday's meeting" = present → warranted; "a job five years ago" = absent →
> inherited). **No anchor → the xOP must route to `abstain`, never to a license call.**

## Why not the obvious fix (full deprecation)?
*Why not just cut the felt domains and remove the circular logic entirely?* Two reasons:

1. **It guts the central claim.** The License Frame's load-bearing idea is "one engine, six
   surfaces — the human and agent cases are the same case." Three of the six are felt. Delete them
   and the unification — the thing that makes this a standard rather than an agent-refusal tool —
   collapses. That is a P4 change to the core claim, not a P1/P2 doc edit; it cannot ride in as a
   scope trim.
2. **The circularity critique is over-applied.** The frame already demoted the residual to "one
   species of license-detection, not the genus." License can be read from present conditions
   *directly*, without the residual. The anchor guard above kills the genuinely circular cases
   (pure interior states with no datable evidence) while keeping the felt cases that *do* carry
   checkable present-condition evidence. That is more precise than deletion and consistent with the
   frame's own move.

## Expected impact
```
gate:      none. Routing un-anchored felt cases to abstain cannot create a warranted override.
           (It will RAISE over-abstention in felt domains — correct, and bounded by 0002's floor.)
adoption:  up — V1 ships on the measurable surface; felt domains kept but disciplined, not deleted.
claim:     preserved — the six-surface unification survives.
```

## Dissent (recorded)
The reviewer's dissent — that keeping felt domains at all invites engineering skepticism — is kept.
Counter-position on record: skepticism is answered by the **anchor guard + abstain**, not by
amputation. If V1 telemetry shows felt-domain abstain rates so high the domains are inert, revisit
deprecation then, with evidence. Do not pre-amputate the unification on a priori grounds.

## Ruling
- [x] **Merge the anchor requirement** (P2) → add the datable present-condition anchor to `SPECIFICATION §7`.
- [ ] **Reject full felt-domain deprecation** (P4) → moved toward `rejected/` unless resubmitted
  with evidence and reviewed as a change to the unification claim.

## SUPERSEDED IN PART — 2026-05-31 (see insights/0002)
The "lead V1 with **observable enterprise** domains" half of this proposal is **reversed** by founder
directive (`insights/0002_lead_with_interpretive_domains.md`,
`concept/INTERPRETIVE_DOMAINS.md`). The lead is the **interpretive** domains, entered through the
**writing** surface (observable artifact + interpretive call). The anchor requirement and the
rejection of felt-domain deprecation both stand — only the lead surface changed. The refusal xOP
remains the agent-surface engineering exemplar, not the flagship.
