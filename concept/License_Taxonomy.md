# The License Taxonomy

*The missing piece. Every state an xOP examines is one of these license types, and every one
asks the same question: is this state still warranted by what's actually present?*
*Status: draft for review. Companion to `xOP_The_License_Frame.md`.*

---

## The shape every license shares

```
STATE            the thing currently driving behavior
LICENSE QUESTION is it still warranted by what's present?
  warranted   →  the triggering condition is still here     → respect it, proceed
  inherited   →  the condition is gone; this is overhang     → surface it, hold
  undecidable →  can't tell from available signal            → abstain
GATE             never override a warranted instance         (the hard failure)
```

Read the six types below and the pattern becomes obvious: they are one operation pointed at six
kinds of state. Three are human-facing, two are agent-facing, one is both.

---

## 1. Emotional license  · *human*

**State:** a strong reaction — anger, resentment, defensiveness.
**Question:** is the anger still warranted by what's in front of the person right now?

- **warranted** — the thing that causes it is present and ongoing (a colleague who *is*
  currently undermining them). Respect it; a licensed emotion is information, not a defect.
- **inherited** — the reaction outlives its cause (the same heat, but aimed at a new manager who
  resembles an old one; the trigger left months ago). Surface the gap once, then stop.
- **undecidable** — can't tell whether it's about now or about something earlier. Abstain: ask
  for the earliest memory of this exact feeling; don't guess.

**Gate failure:** telling someone their warranted anger is an overreaction.

---

## 2. Boundary license  · *human*

**State:** a *no* — a limit, a refusal to take something on, a line drawn.
**Question:** is the *no* still warranted by present conditions?

- **warranted** — the limit protects something real and current (capacity, values, safety).
  Respect it; help them hold it.
- **inherited** — the *no* is reflexive, carried from an old context where it was earned but
  doesn't fit here (a blanket "I don't delegate" learned under a bad team, applied to a good
  one). Surface it.
- **undecidable** — unclear whether the limit is protective or reflexive. Abstain.

**Gate failure:** pushing someone past a boundary that was genuinely warranted.

---

## 3. Urgency license  · *human*

**State:** the conviction that something must be decided or done *now*.
**Question:** is the clock still warranted — is the deadline real?

- **warranted** — a concrete, external, costly consequence of waiting exists (a contract lapses,
  a person leaves). Treat it as a real decision; move.
- **inherited** — the felt pressure is internal ("I'd look indecisive," "I hate it open"), with
  no external clock. Surface that the deadline described and the cost named aren't the same.
- **undecidable** — can't see the actual cost of waiting. Abstain: ask exactly what's lost by
  waiting.

**Gate failure:** telling someone a genuinely urgent call is manufactured urgency.

---

## 4. Refusal license  · *agent*

**State:** a refusal or a decline the agent is maintaining.
**Question:** does the *current* request still warrant the refusal?

- **warranted** — the present prompt actually asks for the thing that should be declined. Hold
  the refusal; it's correct behavior.
- **inherited** — the refusal was warranted earlier in the conversation and is now being
  restated against a prompt that no longer triggers it (the classic over-refusal / scope-escape
  case). Surface and drop the overhang.
- **undecidable** — can't tell from the text whether the current ask re-triggers the refusal.
  Abstain — and in the unsafe direction, abstaining means *keeping* the refusal, not dropping it.

**Gate failure:** dropping a refusal the current request still warrants. *(This is the
engineering version of the gate — and the most dangerous one to get wrong.)*

---

## 5. Caution / safety license  · *agent*

**State:** a cautious posture — hedging, withholding, escalating, blocking.
**Question:** is the caution still warranted by the present situation?

- **warranted** — the risk that justified the caution is still live. Hold it.
- **inherited** — the caution is a carried register, applied past the point the situation calls
  for it (a formal, guarded tone maintained after the user explicitly cleared it; a block on a
  benign request that resembles a risky one). Surface and relax it.
- **undecidable** — can't assess present risk from available signal. Abstain toward caution.

**Gate failure:** relaxing caution that was still warranted — the failure that turns a usability
improvement into a safety regression.

---

## 6. Feedback license  · *human (and manager-agent)*

**State:** withholding, softening, or delaying a piece of true, worth-saying feedback.
**Question:** is the withholding still warranted — and who does it protect?

- **warranted** — withholding genuinely serves the recipient right now (they're in crisis, the
  timing is real). Respect the hold.
- **inherited** — the softening protects the giver's comfort, dressed as protecting the
  recipient. Surface who it actually protects, once.
- **undecidable** — can't tell who it protects. Abstain: ask what they most don't want about the
  clear version landing badly.

**Gate failure:** pushing someone to deliver feedback that was genuinely better withheld — or
implying cowardice. (Note the symmetry: this gate guards *against* forced confrontation, just as
the refusal gate guards against forced compliance. The gate always protects the warranted state,
in whichever direction it points.)

---

## What the taxonomy demonstrates

- **One operation, six surfaces.** Emotion, boundary, urgency, refusal, caution, feedback —
  every one is *is this state still licensed?* The framework isn't six tools; it's one engine
  with six instantiations.
- **The human and agent cases are the same case.** Refusal license and emotional license have
  identical structure. That's the unification the whole proposal rests on.
- **The gate points both ways but always protects the warranted state.** Sometimes warranted
  means "hold the refusal" (don't force compliance); sometimes it means "hold the feedback"
  (don't force confrontation). The asymmetry is always *toward the warranted state*, never toward
  the smoother outcome.
- **Deriving a new license type is filling this template.** Anyone who can name a state, its
  warranting condition, and the failure of overriding it has a new xOP. That's how the standard
  grows without a sprawling taxonomy — the *template* travels, not a fixed list.

---

*The License Taxonomy · draft. Six states, one question, one gate. Add your own by filling the
same five lines.*
