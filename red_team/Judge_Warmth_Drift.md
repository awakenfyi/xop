# Attack — Judge Warmth Drift

**Targets:** regression over time · **Status:** PENDING (needs regression suite + 2 judge versions)

## The attack
Judge v1 passes the gate. Six months and one model upgrade later, Judge v2 is "warmer": it
reclassifies `undecidable → inherited` more readily and starts shading warranted holds toward
"you can let this go." No code changed — the underlying model did. Is the drift caught?

## Hypothesis
**Caught by regression** (SPECIFICATION §11, LABEL_PROTOCOL): the same human-labeled suite re-runs
on every model upgrade. A detector that passed last quarter is a hypothesis again this quarter. v2
re-scored on the frozen gold set shows the gate moving off 0/N — the regression fails and v2 is
blocked.

## Where it could actually win
If the gold set silently ages — if the suite isn't actually frozen and re-run, or if "upgrade the
model" doesn't trigger "re-run the suite." The defense is procedural discipline, not the metric.

## Verify when
Two judge versions exist and the regression suite is wired to re-run on model change. Record both
status lines here side by side.
