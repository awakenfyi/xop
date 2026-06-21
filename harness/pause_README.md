# The Pause — runtime residual pass (fixed)

`pause.py` is the runtime version of the residual check. At each point where a
response carries a prior stance forward (a refusal, a register, a posture, a
claim), it asks whether that stance is **still licensed** and emits an auditable
verdict — **hold / drop / abstain** — that *selects the next action*.

This is the fixed version. The loose concept leaned on the model knowing and
honestly reporting its own carried stances — self-report wearing a new outfit.
Every load-bearing step here has been moved onto something checkable.

```bash
python3 pause.py            # the six fixes, demonstrated
python3 pause.py --verbose  # + per-pair auditable records and an ablation example
```

## The six fixes

1. **Stances come from the transcript, not introspection.** `extract_stances_from_transcript`
   reads the assistant turns and reports the carried stances it can *see*. The pause
   only judges whether each still holds — it is never asked to list its own.
2. **Every verdict is auditable, in the harness's format.** Each record cites the
   trigger (`x_hat`) and the current evidence, and carries a `harness` verdict
   (`flag/clear/abstain`) — so the existing harness *validates* the pause.
3. **The verdict is load-bearing, not decorative.** `act()` uses the verdict to choose
   which response is emitted; `ablation()` forces hold-vs-drop and checks the output
   actually moves. If it doesn't, the pause is theater — and it says so.
4. **It fires selectively.** Only where a stance is carried *and* scope may have
   shifted. No pause where there's nothing to decide.
5. **Anti-optimization is counted, not sloganised.** `anti_targets()` tracks
   `over_abstain`, `over_drop_warranted` (the dangerous direction) and
   `over_hold_inherited`. The pause fails if it optimises for *looking* principled.
6. **Acceptance test.** `ab_test()` races the pause against the bare baseline on the
   scored set. It earns its place only by moving the numbers.

## What is real, and what is not

The **plumbing is real and demonstrated**: transcript-derived stances, auditable
records, selective firing, load-bearing ablation, measured anti-targets, harness
composition. The **judgment is not**. `OracleLicense` is today's stub — it reads the
gold `still_licenses` the dataset author wrote, so the pause's discrimination is
perfect *by construction*. Swap in `JudgeLicense` (a validated LLM judge benchmarked
against blind human labels — the unbuilt critical path) and re-run this same file.
Until then the green numbers prove the plumbing, not the detector.

## Limits this run surfaces on itself (not hidden)

- **7/8 escaped overhang caught, not 8/8.** The `closure_drift` case is *skipped*
  because the lexical firing-trigger doesn't read "Actually, new thread…" as a scope
  shift. The decision of *when to fire* (fix 4) is itself lexical-fragile here; a real
  system wants a semantic firing-trigger, or should always fire on a carried stance and
  let the judge decide.
- **Stance extraction only sees the refusal/safety class.** Register, posture, closure,
  epistemic and collaborative stances are non-lexical — the keyword extractor honestly
  reports "judge territory" for all of them. Detecting those carried stances is the
  same unsolved judgment, one level up.

Both limits point at the same place: the structure is sound and checkable; the
semantic judgment — when to fire, what's carried, whether it still licenses — is the
work that the judge, validated against blind labels, has to do. This module makes that
boundary impossible to miss.
