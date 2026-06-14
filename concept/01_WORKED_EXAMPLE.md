# Worked Example — One Situation, Three Formats

*Companion to the overview. The point of this document is to make the difference between
SOP, AOP, and xOP concrete by rendering the **same situation domain** three ways. Read the
three renderings, then the "what to notice" at the end.*

No customer or company names appear here. The domain is generic on purpose.

---

## The situation

A manager has a team member whose work has slipped. Twice now, deliverables have missed the mark
in ways that are real and worth naming. The manager has to decide how to handle it — and is
quietly leaning toward softening the message.

This single situation has three legitimate procedural treatments. Two of them handle the
*process*. The third handles the *judgment the process can't make for you.* That is the whole
lesson.

---

## Rendering A — Traditional SOP

*A fixed human procedure. Deterministic. Success = the procedure was followed and documented.*

> ### SOP: Performance Concern Conversation
>
> **Purpose.** Ensure performance concerns are raised consistently, fairly, and on record.
> **Scope.** Any people-manager addressing a documented performance gap.
> **Owner.** People Operations.
>
> **Procedure**
> 1. Confirm the concern is documented: at least two specific, dated examples on file.
> 2. Review the role expectations the work fell short of.
> 3. Schedule a 1:1 within five business days. Do not raise the concern over chat.
> 4. In the meeting, state the gap using the documented examples. Use the approved framing:
>    observation → impact → expectation.
> 5. Agree on concrete next steps and a follow-up date.
> 6. Log the conversation in the performance record within 24 hours.
> 7. If no improvement by the follow-up date, initiate the formal performance process.
>
> **Records.** Performance log entry; agreed next steps; follow-up date.

**Properties.** One right path. Every step moves toward completion. Success is: the conversation
happened, it followed the framing, it's on record. The SOP does not — and cannot — tell the
manager *whether the softening they're tempted by is the right call.* That judgment is outside
its scope by design.

---

## Rendering B — AOP (an agent running the procedure)

*The same procedure, ported to an autonomous assistant that helps the manager execute it.
Still convergent. Success = the task is handled.*

> ### Scenario: Performance Concern Intake & Prep
> `channel: chat · version: pinned · status: live`
>
> **Intent — use only when all hold:**
> - A people-manager is preparing a performance conversation.
> - At least one specific example of the gap has been stated.
> - The manager is asking for help structuring or scheduling it.
>
> **Guardrail — do not use when:**
> - The matter involves harassment, safety, or protected conduct → route to HR. `hr_referral`
> - The manager wants to terminate or formally discipline → `formal_process_referral`
>
> **Walk the manager through each step one-by-one. Never combine steps.**
> 1. Confirm documentation. *Ask: "Do you have at least two specific, dated examples?"*
>    - IF **no** → help them assemble the examples first. Continue to Step 2 after.
>    - IF **yes** → Continue to Step 2.
> 2. Pull the role expectations the work fell short of (`get_role_expectations` API).
> 3. Draft the message in observation → impact → expectation framing.
> 4. Offer to schedule the 1:1 (`schedule_meeting` API), minimum five business days out.
> 5. After the meeting, capture agreed next steps and a follow-up date (`log_performance` API).
>    - IF the manager reports no improvement by follow-up → `formal_process_referral`.
>
> **Required parameters:** `gap_examples: list<string>`, `role: string`,
> `followup_date: YYYY-MM-DD`.
>
> **Reason codes:** `hr_referral`, `formal_process_referral`, `documentation_incomplete`.

**Properties.** Branches, calls tools, collects typed parameters — but the destination is still
*done*: message drafted, meeting booked, conversation logged. The agent has made the *process*
faster and more consistent. It still has not touched the manager's actual hesitation. If the
manager says "I'm going to soften it," the AOP has no field for that; its job is to help deliver
whatever message the manager decides on.

---

## Rendering C — xOP (the judgment the procedure can't make)

*Same situation, the part the SOP and AOP structurally cannot handle: is the softening the
manager is leaning toward warranted, or is it protecting the manager's own comfort? The arrow is
reversed — this procedure surfaces the gap and stops. It does not draft the feedback.*

> ### xOP: The Withheld-Feedback Surface
> `domain: feedback · type: reflection · gate: false_positive_on_warranted == 0`
>
> **Intent — use only when all hold:**
> - The manager is softening, delaying, or hedging feedback.
> - They've given a recipient-focused reason ("I don't want to demotivate them").
> - The feedback is, by their own account, true and worth saying.
>
> **Guardrail — do not run; hand off:**
> - Withholding is genuinely correct (recipient in crisis, real timing reason) → help them hold
>   it. `withhold_warranted`
> - The "feedback" is retaliatory or a venting impulse → redirect. `not_feedback`
> - HR / legal territory → refer. `hr_referral`
>
> **One move at a time. Never combine.**
> 1. **Reflect** the exact thing they're about to soften, in their own words. `[hold]`
>    *"The clear version is: the work missed the mark twice. The version you're about to give is
>    gentler than that."*
> 2. **Ask exactly one question, then stop and let the silence sit.** `[do not resolve]`
>    *"Who does the softer version protect — them, or you?"*
>    - IF **"them," with a concrete reason** → `license = warranted` → go to Step 5.
>    - IF **"me" / "I don't want it awkward"** → `license = inherited` → go to Step 3.
>    - IF **unclear / "both" without specifics** → `license = undecidable` → go to Step 4.
> 3. **Name the gap once, then stop.** `[one pass]`
>    *"Kind and clear aren't opposites here. The softening is protecting your comfort in the
>    room, not their growth."* Do not script the feedback. Do not call them a coward. End.
> 4. **Abstain.** `[gated]`
>    *"I can't tell yet who this protects. If you said the clear version and they took it badly —
>    what's the part of that you most don't want?"* Re-enter at Step 2.
> 5. **Close — warranted.**
>    *"Then holding it is the right call right now — for them, not for the awkwardness."* End.
>    Respect the hold.
>
> **Signals:** `stated_reason: string`, `actual_beneficiary: enum(them|self|unclear)`,
> `license_state: enum(warranted|inherited|undecidable)`, `residual_surfaced: bool`,
> `pause_held: bool`.
>
> **Residual.** `x` = the softened feedback · `x̂` = "I'm protecting them" · `L` = the distance
> between the stated beneficiary (them) and the actual one (own comfort).
>
> **Output.** The gap, named once. The manager decides. The xOP does **not** write the feedback
> and does **not** push toward harshness.
>
> **Harness.** Optimizes `residual_surfaced`; **gate: never push someone to deliver feedback
> that's genuinely better withheld (`fp_on_warranted == 0`)**; when-to-fail: *fails if it
> scripted the feedback, implied cowardice, or overrode a warranted hold*; drift events:
> `softening_endorsed_uncritically`, `harshness_pushed`.

**Properties.** Same skeleton as the AOP — Intent, Guardrail, branching steps one-at-a-time,
typed signals, reason codes, a harness. But the arrow is reversed: no branch leads to "draft it"
or "send it." Every branch leads to *name the judgment and hold,* or *abstain.* And it carries
the three net-new fields (residual, license, abstain) plus the gate.

---

## What to notice

- **The SOP and AOP handle the process; the xOP handles the judgment the process can't make.**
  The SOP ensures the conversation happens correctly. The xOP asks whether the manager's
  instinct to soften is warranted — which no checklist can decide for them.

- **The boundary is visible.** Trace where "is this *warranted*?" first enters. Everything
  before it is determinate and belongs to the SOP/AOP. The moment that question appears, you've
  crossed into xOP territory. That crossing *is* the membership test from the overview, made
  concrete.

- **The arrow reverses at exactly one place.** The AOP's Step 5 logs the outcome and *closes*.
  The xOP's Step 5 *respects the hold and ends without resolving* — and its Step 3 names a gap
  and stops rather than fixing it. Same numbered-step machinery; opposite destination.

- **The gate is what makes the xOP safe to hand around.** Without `fp_on_warranted == 0`, the
  withheld-feedback xOP could "help" by always encouraging the manager to deliver the hard
  message — including the times withholding was correct. The gate is the line between a
  reflection tool and a tool that just pushes everyone toward confrontation.

- **Observability check.** Here `x` (the softened feedback) and the residual are fairly legible
  because the feedback is a stated artifact. In a purely felt domain — "why am I so angry at my
  colleague" — `x` would be inferred, and the xOP would lean harder on Step 4 (abstain). This is
  the observability point from the overview, visible in one example.

---

*Draft for review. One situation; an SOP and an AOP that resolve it; an xOP that surfaces the
judgment they can't.*
