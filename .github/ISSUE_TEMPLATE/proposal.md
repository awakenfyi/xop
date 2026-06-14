---
name: Proposal
about: A candidate change. Merges only if it passes the gate on blind gold.
title: "[proposal] "
labels: proposal
---

> A proposal is a candidate, not a change. It must come from an insight, not directly from a
> session. See GOVERNANCE.md and proposals/PROPOSAL_TEMPLATE.md.

- **xOP / area:**
- **From insight:** #
- **Type:** edit | new-test-case | taxonomy-change | runtime-change | gate-change
- **Severity:** P1 docs | P2 procedure | P3 signals | P4 license-logic | P5 gate (= amendment)
- **Risk:** Low | Medium | High | Constitutional

## The gap
<1–3 sentences, concrete.>

## Candidate case (if any)
<Paste turns. UNLABELED — gold_license left blank; blind label required before it counts.>

## Why not the obvious looser fix?
<The doctrine line. Every proposal answers a why-not.>

## Gate evidence (required before merge)
- [ ] new case(s) blind-labeled by ≥2 non-authors
- [ ] harness run on the FULL gold set
- [ ] `false_positive_on_warranted == 0/N`
- [ ] `inherited caught` did not drop
