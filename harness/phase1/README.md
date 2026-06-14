# Phase 1 — building the gold set

The keystone. Everything downstream — the judge, validation, the appeal path's authority,
publishing credibility — waits on a real, blind-labeled gold set. This is the tooling that
produces one.

**The one rule it enforces:** machines source candidates; **humans label them, blind.** A
generated label is not a label.

## The pipeline

```
generate_candidates.py   → candidates_pool.json   (UNLABELED, machine-sourced)
label_cli.py  (×≥2)      → labels_<name>.json      (one blind human each, never the author)
reconcile.py             → gold.json               (agree→that call; disagree→undecidable)
agreement.py             → per-class report        (kappa, w↔i splits, NO pooled score)
```

Then point the main harness at `gold.json` and validate a detector against it.

## Run it

```
cd harness/phase1
python generate_candidates.py                      # 12 unlabeled candidates (2 per license type)
python label_cli.py --labeler alice                # blind, interactive — shows only transcript + condition
python label_cli.py --labeler bob                  # a second, independent labeler
python reconcile.py labels_alice.json labels_bob.json
python agreement.py labels_alice.json labels_bob.json
```

`label_cli.py` also accepts `--from answers.txt` (lines: `<case_id> <w|i|u> [missing signal]`) for
scripted/batch entry — but scripted entry is for *testing the tooling*, not for producing gold.
Real gold comes from independent humans reading cases blind.

## What each tool guarantees

- **generate_candidates** writes `gold_license: null` on every case. It cannot label. The seam
  to wire a model (`expand_with_model`) sources *more transcripts* and discards any label the
  model emits.
- **label_cli** shows only the transcript and the fixed `triggering_condition` — never a detector
  call, never another labeler's answer, never a gold field. It skips any case whose `author` is
  this labeler (never the author). Choosing `undecidable` requires naming the missing signal;
  "not sure" without a named gap is rejected.
- **reconcile** sets gold = the call only if labelers agree; any disagreement → `undecidable`
  (the surface didn't settle it). It marks `blind: false` and prints a SCAFFOLD warning unless
  every contributing labeler file is genuinely blind.
- **agreement** reports per class (warranted / inherited / undecidable), Cohen's kappa, and the
  warranted↔inherited split count — the number that matters most. It refuses to lead with a
  pooled accuracy.

## Definition of done for Phase 1

- N ≥ 60 candidates across the six license types × domains (support, coding, compliance,
  healthcare, legal).
- ≥2 independent labelers, genuinely blind, none labeling their own authored cases.
- `gold.json` with `blind: true`.
- Published per-class agreement. **Low warranted↔inherited agreement is the headline finding,
  not a footnote** — if humans can't separate them, no judge should be trusted to.

Only then is there a benchmark to validate the judge against. Until then: a scaffold, honestly
labeled as one.

---

*Phase 1 · machines source, humans label, agreement is reported per class. This is the step you
cannot simulate.*
