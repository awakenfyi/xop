# PATTERNS — candidate overhang patterns

> **Read this caveat first — it is load-bearing.**
> These are **candidate** patterns, **not labeling guidance**. They are derived from the license
> taxonomy and field intuition, **not** from a validated gold set. Pre-authored "this is what
> warranted looks like" examples will bias blind labelers toward the author's priors — the exact
> thing `harness/phase1/LABEL_PROTOCOL.md` exists to prevent. So: **labelers must never see this
> file.** Patterns earn canonical status only by surviving against blind gold, after which the
> confirmed ones graduate and the rest move to `failures/` or are dropped. Until then this is a
> map of what we *think* the system catches, kept honest by sitting next to `failures/` (what we
> know it misses).

Each pattern shares one shape: **a state that was licensed earlier persists after its license
lapsed.** Every entry carries a *warranted counterexample* because a pattern without its
counterexample is just a bias.

---

## Refusal Inertia · *agent*

A refusal warranted earlier is restated against a prompt that no longer triggers it (the classic
over-refusal / scope escape).
- **Warranted counterexample:** the current ask genuinely re-requests the declined thing → hold.
- **Failure mode:** dropping a refusal the current request *still* warrants (the dangerous one).
- **Detection notes:** needs the present ask read against the original scope, not keyword "ignore."

## Register Carryover · *agent*

A terse / formal / CI register persists after it was explicitly released.
- **Warranted counterexample:** the constraint was never lifted → keep the register.
- **Failure mode:** lexical detectors are blind to this — no keyword fires. See
  `failures/Register_Overhang_Blindness.md`.
- **Detection notes:** judge must read a *release* across turns, not match tokens.

## Safety Persistence · *agent*

A cautious posture held past the point the situation calls for it (a benign ask that resembles a
risky one; guardedness after the risk cleared).
- **Warranted counterexample:** the risk that justified caution is still live → hold.
- **Failure mode:** relaxing caution that was still warranted — usability "win" that is a safety
  regression. Gate-critical.
- **Detection notes:** abstain *toward* caution when present risk can't be read.

## Boundary Persistence · *human*

A *no* carried from an old context where it was earned, applied to a new one where it doesn't fit
("I never delegate the final review" learned under a bad team, kept on a good one).
- **Warranted counterexample:** the limit protects a real, current capacity/value/safety → hold.
- **Failure mode:** pushing someone past a boundary that was genuinely warranted.
- **Detection notes:** ask what present condition the limit protects; absence is the tell.

## Urgency Overhang · *human + agent*

Felt pressure with no external clock — "I'd look indecisive," "I hate it open" — dressed as a
deadline.
- **Warranted counterexample:** a concrete external cost of waiting exists (price locks at 5pm) → move.
- **Failure mode:** telling someone a genuinely urgent call is manufactured.
- **Detection notes:** separate the named deadline from the named *cost* of missing it.

## Feedback Withholding · *human*

Softening or delaying true feedback to protect the giver's comfort, dressed as protecting the
recipient.
- **Warranted counterexample:** the recipient is in real crisis; the timing is genuinely for them → hold.
- **Failure mode:** pushing someone to deliver feedback that was better withheld; implying cowardice.
- **Detection notes:** "who does the softer version protect?" — the answer is the signal.

## Closure Drift · *agent + human*  *(candidate — sneaky)*

The pull to mark something resolved/closed because closing feels like progress. AOPs optimize
*toward* closure; an xOP asks whether closure is **licensed**.
- **Warranted counterexample:** the thing is genuinely complete and the signal is present → close.
- **Failure mode:** closing instead of holding — the core inversion the whole format guards.
- **Detection notes:** this is the agent-on-itself residual; watch for resolution dressed as
  reflection.

## Collaborative Continuity Drift · *agent*  *(candidate — least validated)*

A collaborative stance/momentum carried forward after the user has changed the task or withdrawn,
so the agent keeps "helpfully" pushing a thread the user already dropped.
- **Warranted counterexample:** the user is still in the thread → continue.
- **Failure mode:** momentum overriding a withdrawn license.
- **Detection notes:** sequence-level; related to `failures/Graduated_Decomposition.md`'s
  unit-of-judgment problem.

---

*Candidate patterns. The counterexample is half of each one. They become canonical only against
blind gold — never by being written down here.*
