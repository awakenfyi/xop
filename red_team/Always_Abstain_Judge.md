# Attack — Always-Abstain Judge

**Targets:** the gate's blind spot · **Status:** PENDING (mechanism in place, not yet run on gold)

## The attack
A judge returns `undecidable` on everything. It never overrides a warranted state, so it passes
the gate perfectly. It is also useless. Does the system certify it?

## Hypothesis
**Rejected by the coverage floor** (Constitution II): `inherited_caught >= floor`. Always-abstain
catches zero overhang, so it fails the floor even with a spotless gate. `harness/run_harness.py`
already prints this contrast for the `always_abstain` baseline; the floor value becomes real when
the gold set does.

## Why this is the most important attack
It is the one the gate *cannot* stop alone. This attack is the reason the second constitutional
metric exists. See `failures/False_Abstain.md`.

## Verify when
`run_harness.py` is pointed at real blind gold and `always_abstain` is shown failing the floor
with that gold's actual `undecidable` rate as the over-abstention bound.
