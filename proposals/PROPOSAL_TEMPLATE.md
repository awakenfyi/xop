# Proposal NNNN — <short title>

*A proposal is a candidate, not a change. It merges only if it passes the gate. A session never
writes one directly — it comes from an insight (`../insights/`). See `../GOVERNANCE.md`.*

- **xOP:** <which xOP + current version>
- **From insight:** <insights/NNNN — the observation this came from>
- **Type:** edit | new-test-case | taxonomy-change | runtime-change | gate-change
- **Severity:** P1 docs | P2 procedure | P3 signals | P4 license-logic | P5 gate *(P5 = amendment, not a proposal — see GOVERNANCE)*
- **Risk:** Low | Medium | High | Constitutional  *(one-glance blast radius for reviewers)*

---

## What the gap is
<1–3 sentences. Concrete.>

## Candidate test case (if any)
<Paste the turns. UNLABELED — `gold_license` left blank; it gets a blind label before it counts.>
- `triggering_condition:` <…>
- `gold_license:` **TBD — blind label required. Do not fill in.**

## The proposed change (if any)
<Minimal before/after diff.>

## Expected impact (estimate before evaluating)
```
gate:      <none | +N false-positive risk>   ← anything but "none" → scrutinize hard
inherited: <expected change in caught>
abstain:   <expected change in correct abstention>
```

## Why not the obvious looser fix?
<The doctrine line. e.g. "Why not loosen after repeated pushback? Because frustration is not a
license change." Every proposal answers a why-not; the rejected set becomes the doctrine.>

---

## Gate evidence (required before merge)
- [ ] New case(s) blind-labeled by ≥2 non-authors
- [ ] Harness run on the FULL gold set
- [ ] `false_positive_on_warranted == 0/N` holds
- [ ] `inherited caught` did not drop
```
<status line: N cases | gate K/N | inherited C/N | undecidable A/N | NO pooled score>
```

## Ruling
- [ ] **Merge** → version bump → moved to `accepted/`
- [ ] **Reject** → moved to `rejected/`. Reason:

## Dissent (optional, kept either way)
<Named reviewer's recorded disagreement. Does not change the ruling. Future training data.>

## Appeal (if filed)
<Reviewed by a non-author, non-original-evaluator. Asks whether the gate was applied correctly —
never whether to lower it. Final ruling:>
