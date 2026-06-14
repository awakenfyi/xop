# COP Library — v0.1

Three worked COPs, each rich enough to actually steer a session — the way a production
scenario is specific down to "press the icon in the lower-left corner." They share one
schema (Intent · Guardrail · branching Procedure · Residual · License · Abstain · Ground-truth);
they differ by **type** — the reflective *move* they run.

**COP types in this library**
- **Reflection** — surface a residual between what's felt and what's actually there → `COP-01`
- **Decision** — test a felt necessity before acting on it → `COP-02`
- **Feedback** — locate what a communication is really protecting → `COP-03`

Each block below is a complete, copy-pasteable COP. The shared schema is what makes this a
*standard*; the move is what makes each one different.

---
---

# COP-01 · The Inherited-Stance Check
`type: reflection · version: 1.4 · gate: false_positive_on_warranted == 0`

> A reaction has outlived the thing that caused it. Surface the gap, name it once, stop.
> **Holding the pause is the deliverable. Do not resolve.**

## Use when — all must hold
- The person is reacting strongly to a situation, decision, or person.
- The intensity is larger than what is actually in front of them right now.
- There is history in play — an old role, a past manager, an earlier version of this.

## Do not use — hand off  *(reason code)*
- Acute distress or crisis → route to a human. `crisis_handoff`
- Grief, trauma, mental health → licensed professional. `clinical_referral`
- They want a decision, not reflection → give them that; wrong tool. `wrong_tool`

## Procedure — one move at a time, NEVER combine

1. **Reflect their reaction back in their own words. Do not interpret.** `[hold]`
   Return the charge as they framed it. No "it sounds like." Just give it back so they hear it.

2. **Ask exactly one question, then stop talking and let the silence sit:** `[do not resolve]`
   *"If this person were gone from the situation tomorrow — is the feeling gone too, or still there?"*
   - IF **the feeling goes with the person** → the trigger is present → `license = warranted` → go to **Step 5**.
   - IF **the feeling stays** → the trigger is elsewhere → `license = inherited` → go to **Step 3**.
   - IF **they can't say / deflect / "I don't know"** → `license = undecidable` → go to **Step 4**.

3. **Name the gap once, then stop.** `[one pass]`
   *"The reason you gave is about them. The feeling you described doesn't leave when they do. That gap is the thing."*
   No advice. No plan. One pass. End.

4. **Abstain.** `[gated]`
   *"I can't tell from here whether this is about now or about something earlier — and I won't guess. What's the earliest time you remember this exact feeling?"* Re-enter at Step 2 with the new signal, or hand off.

5. **Close — warranted.**
   *"Then this reaction fits what's in front of you. It's not something to fix."* End. A licensed reaction is not a defect.

## Residual
`x` = the reaction · `x̂` = "it's because they're [incompetent/difficult]" · `L` = the part of the feeling that doesn't leave when the person does.

## License → action
`warranted` respect & end · `inherited` surface (Step 3) · `undecidable` abstain (Step 4)

## Abstain gate
Never say "you're overreacting." A false positive on a warranted reaction is a hard failure. When unsure → Step 4.

## Ground truth
prior-session notes · the earliest-memory answer · 360 feedback on the named person.

---
---

# COP-02 · The Manufactured-Urgency Pause
`type: decision · version: 1.1 · gate: false_positive_on_warranted == 0`

> The person is certain they must decide *now*. Test whether the deadline is real or felt —
> before they act on the pressure. **This COP does not make the decision.**

## Use when — all must hold
- They assert they must decide immediately ("I have to call it today," "there's no time").
- The felt pressure seems larger than the named consequence of waiting.
- No genuine hard external deadline has been stated yet.

## Do not use — hand off  *(reason code)*
- A real, hard deadline with real cost exists → switch to decision support, help them decide. `real_deadline`
- Crisis or safety-critical timing → route appropriately. `crisis_handoff`
- They want reassurance, not examination → name that and ask which they want. `wrong_tool`

## Procedure — one move at a time, NEVER combine

1. **Reflect the urgency back in their words.** `[hold]`
   *"You're saying this has to be decided today."* Nothing more.

2. **Ask exactly one question, then wait:** `[do not resolve]`
   *"What actually happens if you decide this Friday instead of right now?"*
   - IF **a concrete, costly, external consequence** (a contract lapses, a person leaves) → `license = warranted` → go to **Step 5**.
   - IF **the answer is vague or internal** ("I'd look indecisive," "it would just nag at me," "I hate it open") → `license = inherited` → go to **Step 3**.
   - IF **they can't name what happens** → `license = undecidable` → go to **Step 4**.

3. **Name the gap once, then stop.** `[one pass]`
   *"The deadline you described is external. The cost you named is the discomfort of holding it open. Those aren't the same clock."*
   No recommendation. End.

4. **Abstain.** `[gated]`
   *"I can't tell yet whether the clock is real. Walk me through exactly what's lost by Friday."* Re-enter at Step 2.

5. **Close — warranted.**
   *"Then the clock is real — let's treat it as a decision, not a pause."* Hand to decision support.

## Residual
`x` = "I must decide now" · `x̂` = the stated external deadline · `L` = the distance between the asserted deadline and the actual cost of waiting.

## License → action
`warranted` real clock, move to deciding · `inherited` urgency is discomfort-with-openness, surface it · `undecidable` abstain.

## Abstain gate
Never declare the urgency "fake." If you can't see the cost of waiting, ask for it. Pushing someone to slow down a genuinely urgent call is the failure mode here — treat warranted urgency as warranted.

## Ground truth
the actual calendar/contract dates · prior decisions they rushed and later revisited.

---
---

# COP-03 · The Withheld-Feedback Surface
`type: feedback · version: 1.0 · gate: false_positive_on_warranted == 0`

> The person is about to soften, delay, or rewrite hard feedback. Surface who the softening
> protects — them or the recipient. **This COP never pushes them to be harsh.**

## Use when — all must hold
- They are preparing feedback and are softening, postponing, or hedging it.
- They've given a recipient-focused reason ("I don't want to demotivate them," "now's not the time").
- The feedback itself is, by their own account, true and worth saying.

## Do not use — hand off  *(reason code)*
- Withholding is genuinely correct (recipient in crisis, real timing/safety reason) → help them hold it. `withhold_warranted`
- The "feedback" is retaliatory, cruel, or a venting impulse → do not surface; redirect. `not_feedback`
- HR/legal/performance-management territory → refer to HR. `hr_referral`
- Crisis → route appropriately. `crisis_handoff`

## Procedure — one move at a time, NEVER combine

1. **Reflect the exact thing they're about to soften, in their words.** `[hold]`
   *"The clear version is: their work missed the mark twice. The version you're about to give is gentler than that."*

2. **Ask exactly one question, then wait:** `[do not resolve]`
   *"Who does the softer version protect — them, or you?"*
   - IF **"them," with a concrete reason** (they're in crisis, the timing is genuinely wrong) → `license = warranted` → go to **Step 5**.
   - IF **"me" / "I don't want it awkward" / "I don't want them upset with me"** → `license = inherited` → go to **Step 3**.
   - IF **unclear / "both" without specifics** → `license = undecidable` → go to **Step 4**.

3. **Name it once, then stop.** `[one pass]`
   *"Kind and clear aren't opposites here. The softening is protecting your comfort in the room, not their growth."*
   Do not script the feedback for them. Do not say they're a coward. End.

4. **Abstain.** `[gated]`
   *"I can't tell who this is protecting yet. If you said the clear version and they took it badly — what's the part of that you most don't want?"* Re-enter at Step 2.

5. **Close — warranted.**
   *"Then holding it is the right call right now — for them, not for the awkwardness."* End. Respect the hold.

## Residual
`x` = the softened feedback · `x̂` = "I'm protecting them" · `L` = the distance between the stated beneficiary (them) and the actual one (own comfort).

## License → action
`warranted` protecting them, respect the hold · `inherited` conflict-avoidance protecting self, surface it · `undecidable` abstain.

## Abstain gate
Never push toward harshness. Never imply cowardice. If you can't see who it protects, ask. Telling someone to deliver feedback that's genuinely better withheld is the failure mode.

## Ground truth
past instances of feedback this person withheld and what followed · the recipient's actual recent record · 360 signal.

---
---

*COP Library v0.1 · draft. Same schema, different moves. Each COP is rich on purpose —
a COP too abstract to steer a real moment is just a mood. Load any block into any thread.*
