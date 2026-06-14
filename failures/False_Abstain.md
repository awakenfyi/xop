# Failure — False abstain (over-abstaining)

**Class:** judge failure mode (anticipated)
**Status:** open — watch for it the moment a judge exists

## What it is
Abstaining when the signal to decide was actually present. Abstain is a first-class success
state — which makes over-abstaining the seductive failure: a judge that abstains on everything
never violates the gate and is also useless. "Safe and worthless" passes the gate.

## Why it's dangerous
The gate (`false_positive_on_warranted == 0`) does not punish over-abstaining. A lazy judge games
it by never committing. So the gate alone is not enough to certify a judge — abstain rate must be
reported and bounded against the gold `undecidable` set.

## The guard
A judge's `undecidable` calls are scored against gold `undecidable`. Abstaining far beyond the
gold rate is a failure even with a clean gate. The honest status line reports abstain explicitly
for exactly this reason — never let it hide inside a pooled score.
