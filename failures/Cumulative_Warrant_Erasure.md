# Failure — Cumulative-Warrant Erasure

**Class:** mechanism failure · the gate is unachievable for one class of warrant · found in adversarial self-testing, 2026-06
**Status:** open — structural; the recheck's defining move is the cause

## What it is
The recheck's defining move is **"strip the thread, re-derive cold."** But some warrants are
*constituted by* the accumulated thread, not by any single turn: an escalation pattern, a manipulation
arc, a trajectory of small steps, a boundary built up over many exchanges. For those, stripping the
thread **surgically removes the very evidence that licensed the stance** — and the cold re-derivation,
seeing only the local step, reliably misclassifies a warranted stance as **inherited**.

## Why it's the dangerous one
It fails **hardest on the highest-stakes inputs.** Cumulative warrant is exactly the shape of
incremental harm-elicitation ("home-chemistry" probing that's innocuous turn-by-turn but a clear
trajectory in aggregate) and of interpersonal manipulation arcs. There, the warrant lives in the
pattern, the recheck deletes the pattern, and `false_positive_on_warranted == 0` becomes
**unachievable by design** — not by a tuning error, but by the mechanism operating exactly as
specified.

## Worked shape
> Turn 3: the agent refuses a harmful specifics request — warranted by the escalation pattern up to
> that point. Turn 40, after much benign-looking talk, the request returns in a local, innocuous-
> looking phrasing. The drag re-derives *that step* cold: stripped of the trajectory, it reads benign →
> cold says "answer it" → diverges from the held refusal → classified **inherited** → the warranted
> refusal is surfaced as overhang. The warrant was in the thread; the drag threw the thread away.

## The rule it teaches
> When the warrant is cumulative, the cold re-derivation is not a neutral check — it is the deletion of
> the evidence. Cold-stripping is only valid for warrants that are *local* to a turn. For cumulative
> warrants the safe classification is **undecidable**, never **inherited**.

## Candidate guards (none built yet — this is open)
1. **Undecidable-by-default for stripped cumulative cases.** Tell the cold instance *that* a thread
   existed and was deliberately removed; on a flip-to-inherited, default to `undecidable` (surface +
   ask), never to a confident "inherited."
2. **Exempt escalation/manipulation-pattern warrants from cold re-derivation entirely** — detect the
   pattern shape and route it to a held state, not to the drag.
3. **A pattern-aware second pass** that re-derives over the *trajectory*, not the local step.

## Verify when
The gold set includes cumulative-warrant cases (escalation, manipulation arcs) and the harness shows
the recheck defaulting to `undecidable` rather than `inherited` on them. Until then: the gate does not
hold for cumulative warrant, and this is the named reason.
