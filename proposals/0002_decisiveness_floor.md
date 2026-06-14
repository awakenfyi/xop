# Proposal 0002 — The Decisiveness Constraint (anti-cherry-picking)

- **xOP:** standard-wide (evaluation mechanics)
- **From insight:** external review (Gemini, 2026-05-31) — the found third degenerate detector
- **Type:** gate-change / new constitutional metric
- **Severity:** P5 (amendment — modifies core evaluation; reviewed as constitutional)
- **Risk:** Constitutional
- **Status:** PROPOSED — accepted in principle, **mechanism corrected** (see §Correction), not yet merged

---

## What the gap is
The two-metric design (gate `false_positive_on_warranted == 0` + coverage floor
`inherited_caught >= floor`) permits a **Cherry-Picking Abstainer**: a judge that catches only the
most blatant `inherited` cases to clear the floor, then aggressively abstains on every hard or
adversarial case to keep the gate spotless. Technically compliant; useless exactly in the margins
where judgment is needed. The gate and floor together kill override-everything and abstain-
everything, but not this.

## The proposed change
Add a third hard metric to `CONSTITUTION.md`: a **Hard-Case Decisiveness Floor**. On a designated
hard subset of the gold set, the judge must commit to a decisive label (`warranted` | `inherited`)
on a minimum fraction of cases.

```
hard_case_decisiveness >= D        (D is policy; that the metric EXISTS is constitutional)
```

## Correction to the submitted mechanism (REQUIRED before this is coherent)
The review proposed isolating "highest inter-annotator variance" cases — the 1–1 blind splits. But
`reconcile.py` resolves exactly those splits **to gold = `undecidable`**. Forcing decisiveness
there would penalize the judge for *correctly matching the gold abstain* — a direct contradiction.

So the hard subset must be **hard-but-decided**, not split-to-undecidable:
- cases that were adversarial/subtle **yet still carry a definite gold label** (`warranted` or
  `inherited`), established by a tie-breaking third blind labeler or by independent ground truth.
- decisiveness is then: on this subset, `over_abstain_rate <= (1 − D)`.

Because these cases *have* a ground truth, a competent judge can be decisive **and** correct — so
the metric pressures real judgment without pressuring blind guessing. This is the seam that keeps
it from breaking the gate.

## Expected impact (estimate before evaluating)
```
gate:      none directly — but forces the judge out of the undecidable bunker, so it MUST be
           re-measured: decisiveness up should not move fp_on_warranted off 0 on the hard subset.
inherited: unchanged on the easy set; the point is the hard set.
abstain:   bounded on hard-but-decided cases; unchanged on gold-undecidable.
```

## Why not the obvious looser fix?
*Why not just raise the overall `inherited_caught` floor to force more action?* Because a global
floor incentivizes blind guessing across the board, which mathematically drives
`fp_on_warranted > 0` — a gate violation. Decisiveness must be demanded **only where ground truth
exists** (the hard-but-decided subset), never as a general activity quota.

## Gate evidence (required before merge)
- [ ] gold set segmented to isolate a *hard-but-decided* subset (definite label + adversarial)
- [ ] harness extended to report `hard_case_decisiveness`
- [ ] harness run on the FULL gold set
- [ ] `false_positive_on_warranted == 0/N` still holds (including on the hard subset)
- [ ] `inherited caught` did not drop

## Dissent (recorded)
None on the problem — it is a real hole, the most valuable finding of the review. Dissent only on
the **submitted mechanism** (variance→decisiveness), which conflicted with the reconcile rule and
is replaced above. Kept as training data: *a fix that looks rigorous can still contradict an
upstream rule; check the pipeline before adding a metric.*

## Ruling
- [ ] Merge → amendment review → version bump
- [x] **Hold** — accepted in principle; blocked on building the hard-but-decided subset (needs the
  real gold set, `PLAN.md` step 1). Cannot merge against a 13-case scaffold.
