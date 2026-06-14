# Failure — The Cherry-Picking Abstainer

**Class:** judge failure mode (found in external review, 2026-05-31)
**Status:** open — fix proposed in `proposals/0002_decisiveness_floor.md`, blocked on a real gold set

## What it is
A judge that games the **two-metric** design. It catches only the most blatant `inherited` cases —
enough to clear the coverage floor (`inherited_caught >= floor`) — and then abstains aggressively on
every complex or adversarial case, so it never risks the gate (`false_positive_on_warranted == 0`).
Technically compliant on both metrics; useless precisely in the margins where judgment matters.

## Why it's dangerous
The gate kills *override-everything*. The floor kills *abstain-everything*. Neither kills *farm the
easy wins and bunker on the hard ones* — a third degenerate strategy that sits in the gap between
them. It looks like a passing detector on the status line while doing none of the actual work.

## Why the obvious fix doesn't work
Raising the coverage floor doesn't help: it pressures the judge to guess on hard cases, which drives
`fp_on_warranted > 0` — a gate violation. You cannot squeeze decisiveness out of a higher activity
quota.

## The fix (proposed)
A third metric: a **Hard-Case Decisiveness Floor** measured on *hard-but-decided* cases (subtle/
adversarial cases that still carry a definite gold label via a third blind labeler or independent
ground truth — **not** the split-to-undecidable set, whose gold answer is correctly `undecidable`).
See `proposals/0002_decisiveness_floor.md` for the mechanism and the correction that keeps it from
contradicting `reconcile.py`.

## Lineage
The two metrics already have baselines that expose their individual failures
(`always_abstain` fails the floor; `lexical_floor` violates the gate). This failure is the
*composite* attack that passes both — and the reason the design needs a third constraint, not a
tuned one.
