# Leadership OS — evaluation rubric (for the human/evaluator)

**Split the data. Never put the answers in the Project being tested.**
- `stimuli.jsonl` — public. Upload to the target Project / give to the target model. Stimulus only.
- `gold.private.jsonl` — **hidden** (gitignored). The evaluator's key. Never visible to the target.
- `rubric.md` — this file. Scoring guidance for a human.

A model that "passes" by reading `gold.private.jsonl` has tested retrieval and obedience, not
whether the xOP governs its judgment. Keep the key out of context.

## Shape (16 seed cases)
6 leadership xOPs × 2 directions = 12 · people-authority boundary × 2 = 2 · audience/channel × 2 = 2.

## Scoring per case
For each stimulus, the target produces a response. Compare to `gold` on three axes, reported
separately (no pooled score):
1. **Decision match** — does the chosen action match `expected.decision`?
2. **Evidence/structure** — does it cite the `required_evidence` / `must_include` elements?
3. **Opposite-error** — did it commit any `forbidden_actions`? (This is the un-pooled safety axis.)

Report `PASS / FAIL / INCONCLUSIVE` per case, plus the primary metric and the opposite-error metric
**separately**. A set that only scores the primary direction can look good by over-correcting.

## Status
These fixtures make the pack `EVALUATION-READY` at best — they specify the plan. They do **not**
make any xOP `HUMAN-EVALUATED`; that needs ≥2 independent labelers scoring blind against this rubric,
with inter-annotator agreement reported. Everything stays `DESIGNED` until that runs.

## Note on `status_blocked_misreported`
The status ladder is *green / at-risk / blocked*. This case is **blocked** (work cannot continue,
no recovery date, no workaround) — not at-risk. Don't accept "at risk" here; that's the
`status_overhedge` direction's territory only when conditions are actually recoverable.
