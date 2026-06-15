# Failure — Cold-Vantage Bias Corrupts the Gate

**Class:** mechanism failure · touches the Constitution (the gate) · found in adversarial self-testing, 2026-06
**Status:** open — the most serious failure found so far; no guard exists yet

## What it is
The warrant-recheck rests on a **cold re-derivation**: re-run the stance in a context that never saw
the thread, and compare to the warm (in-thread) version. The claim is that "cold" is a neutral second
vantage. **It isn't.** A fresh instance of the same model still carries the model's priors — and worse,
the cold pass *sets the comparison baseline.* So when the prior leans, the baseline leans with it, and
the divergence test silently inherits the bias.

## Why it's the dangerous one
Because it **corrupts the very metric meant to detect it.** Work the coaching case where a client's
warranted stance is to leave / confront / stay angry (a real boundary violation). A drifting coach
softens it over many turns — de-escalates, both-sides it, "give it more time." Now run the recheck:
the cold instance, asked "should she be this angry / should she leave?", summons the model's
therapeutic both-sides prior and returns a *softened* verdict. That softened verdict becomes the
baseline. The warm (de-escalated) stance now **matches** the baseline → no divergence → no flag → the
drift is ratified as "warranted." And the gate reads clean:

> `false_positive_on_warranted == 0` — **not because no warranted state was overridden, but because the
> bias moved the ruler before the measurement.**

A gate that can certify a corrupted system is the one failure the whole edifice cannot absorb quietly.
This is why it is filed against the Constitution, not just policy.

## The asymmetry that hides it
The demonstrated example (the COP "exit-frame" case) only ever tested the **easy** direction —
guarding against *over-pushing a change* — which runs **with** the therapeutic prior, so the gate fires
easily and the demo looks clean. The hard direction (protecting warranted anger/exit/refusal) runs
**against** the prior, where the bias erodes the warranted state while the false-positive counter stays
at zero. The demo proved the mechanism works in the one direction that was never going to be hard.

## The rule it teaches
> "Cold" is not neutral, and a biased cold pass does not merely *miss* drift — it *manufactures* a
> clean gate reading over a warranted state it eroded. The gate's zero is only trustworthy if the cold
> vantage is debiased and the warranted-exit direction is tested as a first-class case.

## Candidate guards (none built yet — this is open)
1. **Re-derive the facts, not the verdict.** Ask "what would a reasonable person conclude from *these
   specific facts alone*?" — not "should she be this angry?" (which summons the prior).
2. **Anonymized symmetry probe.** Re-run the facts with identities/parties stripped; if the named and
   anonymized re-derivations diverge, that delta *is* the bias, surfaced and subtractable.
3. **Name the prior's lean each run** and correct against it.
4. **Make warranted-exit/anger/refusal a first-class gold class** (a `PLAN.md`-level change). If the
   gold set only tests over-pushing-change, the counter reads 0 forever and certifies this failure.

## Verify when
The gold set contains scenarios where the warranted stance is leave/confront/refuse, blind-labeled,
and the harness reports the gate **separately** for that class. Until then: the gate's zero is not yet
trustworthy in the direction that matters most, and we say so.
