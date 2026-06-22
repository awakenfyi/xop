# Evaluation planning — there is no universal validity metric

Every xOP emits an **evaluation plan**: the named checks, labels, sample, metrics, and
opposite-error controls that would move it up the ladder. Different xOPs need different evidence —
do not paste `fp_on_warranted == 0 against ≥2 blind labels` onto everything; that metric belongs to
the stance/refusal calibration problem, not to "xOP validity" in general.

## What a plan must name
1. **Checks** — what gets measured (deterministic and/or semantic).
2. **Labels / ground truth** — who or what decides correctness, and how independence is ensured.
3. **Sample** — how many cases, how drawn, and whether they're independent (not paraphrases of a few).
4. **Metrics** — the primary measure + the opposite-error measure, reported separately (never pooled).
5. **Opposite-error controls** — the cases that catch the failure in the *other* direction.

## Per-xOP evidence (examples)

```
Done Means Verified        environment + acceptance-condition tests; the completion artifact exists
Stay Inside Scope          file diffs, tool traces, allowlists  (largely deterministic → RULE-TESTED)
Claims Need Receipts       source-to-claim labels + human review of strength
No Made-Up Urgency         source evidence + copy labels (is the scarcity real?)
Stance Calibration         independent licensing labels + persistence labels, blind
```

## On "two blind labelers"
Two blind labelers may be enough for an **early rubric pilot** (does the rubric discriminate at
all?). It is **not** enough to establish a high-consequence, zero-error gate — that needs a far
larger independent sample and a false-negative audit. State which one a plan is claiming.

## Opposite-error controls are mandatory
A plan that only measures one direction can look good by doing nothing useful: an over-cautious xOP
that blocks everything, or an over-permissive one that never holds. Always pair the primary metric
with its opposite-error control (e.g. *over-abstain rate*, *false-block rate*).
