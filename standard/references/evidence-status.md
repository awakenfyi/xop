# Evidence status — the ladder

An xOP's status is **where its evidence sits**, reported separately from the **result** of any
evaluation that has run. Status lives in metadata, never in the filename (use a stable id, e.g.
`xop.claim.evidence-bound`). There is no universal validity metric — each xOP names its own checks in
its evaluation plan (`evaluation-planning.md`).

## The five rungs

| Status | Means |
|---|---|
| **DESIGNED** | well-formed shape: stance, warrant, observable signal, fork, gate, anti-optimization, when-to-fail. Admission tests applied, trigger tracks warrant. *(All fresh candidates start here.)* |
| **EVALUATION-READY** | an evaluation plan exists: named checks, labels, sample, metrics, and opposite-error controls are specified and runnable. |
| **RULE-TESTED** | deterministic/mechanical checks pass on published fixtures (the Guard side, or fixture-level structure). |
| **HUMAN-EVALUATED** | the semantic judgment has been compared against independent, blind human labels. |
| **FIELD-VALIDATED** | the xOP measurably reduced the target failure in real use. |

## The result (separate axis)

Report the outcome of whatever evaluation has run, never folded into the status:

`PASS` · `FAIL` · `INCONCLUSIVE`

A candidate can be `HUMAN-EVALUATED` and still `FAIL`. "RULE-TESTED" says the mechanical checks pass;
it does **not** say the rule helps in practice — that's `FIELD-VALIDATED`.

## What observability buys, and what it doesn't

An observable warrant makes an xOP **evaluable** — it can climb the ladder. It does **not** establish
that a working evaluator exists, that the evaluator agrees with humans, that the dataset is adequate,
that the gate was measured, or that the result passed. Don't let "the signal is observable" round up
to "the gate holds." (This is the scope-persistence package's own distinction: having the semantic
signal ≠ having a detector that computes it.)
