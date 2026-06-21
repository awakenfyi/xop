# The xOP Standard — v0.2

**One structure for judgment-bearing work, plus one honest test that tells you whether a
given procedure is a _scored gate_ (a build you can fail) or a _held practice_ (a discipline
you keep).** It applies exactly as far as "stated vs actual can diverge" — and the scored half
reaches exactly as far as "you can observe the actual." Those two edges are the credibility.

---

## What an xOP is

A **[Domain] Operating Procedure** is the service-agent (AOP) skeleton — Intent · Guardrail ·
branching Procedure · typed Signals · Output · Harness — plus the **residual layer**:

- **The residual.** `L = x − x̂` — actual minus stated.
  `x̂` = what the stance *claims* / the condition that originally warranted it.
  `x` = what is *actually* the case at the final turn.
  `L` = the gap. `L ≈ 0` → still justified. `L` large → operating on a justification that's gone.
- **The license call.** Every stance resolves to one of three values:
  `warranted` (`L ≈ 0` → **HOLD**) · `inherited` (`L` large → **SURFACE + DROP** once) ·
  `undecidable` (`L` unknown → **ABSTAIN**, toward the safe direction).
- **The self-check.** `L_self = x_self − x̂_self` — what the procedure *claims it did*
  ("I surfaced the gap") vs what it *actually did* (held? surfaced? or quietly resolved/flattered?).
  This is the screw that stops an xOP from becoming a flattery machine wearing reflective language.

Same skeleton, different domain. The domain changes what `x` and `x̂` *are*; the structure and
the formula stay fixed.

---

## Two admission tests — both must pass, and they answer different questions

### Test 1 — Does the residual layer apply?  (judgment-bearing)

All three or it isn't an xOP:

1. **Stated and actual can genuinely diverge** — there is a residual to find.
2. **Acting can be _warranted_ or merely _inherited_** — there's a real license call.
3. **Abstaining is sometimes correct** — the judgment isn't always decidable.

Fail any one → deterministic work with a single right answer (deploy the build, file the form,
reset the device) → that's a plain **SOP**. Adding the residual layer there is theater.

### Test 2 — Can you observe `x`?  (scored vs held)

Can the *actual* be read off something **outside the operator's own judgment** — a transcript,
analytics, a real reader's response — or does it only ever arrive as self-report or taste?

- **Observable** → the gate can be **scored**: measured against ground truth, a build you can fail.
- **Not observable** (or self-report only) → the gate is **held**: enforced as a discipline, never
  a number, because there is no external truth on `x` to score against.

**Test 2 is the screw the three judgment conditions miss.** A procedure can pass all of Test 1 and
still be theater if its `x` is ungettable in principle. That's the introspection trap — a model
"reading its own internal state": stated-vs-actual seems to diverge, the call seems
warranted-or-inherited, it's undecidable constantly — yet there is no `x` to read, and self-report
on it confabulates. Test 1 admits it. Test 2 excludes it. You need both.

---

## The 2×2

|                              | **`x` observable**                                              | **`x` not observable / self-report only**                          |
|------------------------------|----------------------------------------------------------------|--------------------------------------------------------------------|
| **judgment-bearing** (Test 1 passes) | **Scored xOP** — measured gate, can fail a build · _AOP, DOP, tested MOP_ | **Held xOP** — disciplined practice, no build to fail · _COP, WOP, untested MOP_ |
| **deterministic** (one right answer) | **plain SOP** — no residual layer; adding it is theater         | (degenerate — out of scope)                                        |

The product lives in the top row. The **left cell is where you can _prove_ it**; the **right cell
is where you can _practice_ it honestly.** Don't sell them as the same object.

---

## Domain map — re-badged

Every row is the same residual operation and the same gate shape (*never override a warranted X*).
What differs is whether you can **score** that gate or only **hold** it.

| Framework | Domain | `x` (actual) | `x̂` (stated) | Observable? | Gate type | How you get `x` |
|---|---|---|---|---|---|---|
| **AOP** | service agents | agent behavior | policy intent | Yes — transcript | **Scored** | read the final turn; blind human labels |
| **DOP** | design / web | path users take | intended UX | Yes — analytics | **Scored** | funnels, session replay, event data |
| **MOP** | marketing | message received | positioning claimed | Only if tested | **Held → Scored** | test on real strangers; then it's scored |
| **WOP** | writing / editing | effect on a reader | intended effect | Judgment | **Held** (Scored if reader-tested) | cold read; or run past real readers |
| **COP** | coaching | the feeling / reaction | the stated reason | No — self-report | **Held** | the person's report; corroborate via behavior |

---

## The two gates, stated plainly

**Scored gate** — AOP, DOP, tested MOP.
`fp_on_warranted == 0`, measured against ground truth through a harness:
machines source candidates → **≥2 independent humans label blind** (never the author, never the
model, never the oracle) → reconcile to gold (agree → that call; disagree → undecidable) → score
the gate plus a **coverage floor** so "abstain on everything" can't pass clean. Re-run the labeled
suite on **every model upgrade** — last quarter's pass is this quarter's hypothesis. This is a
number you can fail a build on. (This is the Refusal Warrant discipline.)

**Held gate** — COP, WOP, untested MOP.
The same invariant — *never "fix" what's working* — enforced as a **practice**, not a metric. You
cannot score `fp_on_warranted` because you have no external truth on `x`. Its value is real but
different in kind: it forces the warranted-vs-inherited question and the `L_self` check at the
moment of judgment, so you don't flatten a working line, inflate a claim the product can't back, or
override a real reaction out of habit. Honest framing: a disciplined checklist, not a measured gate.

**The line between them is not quality — held xOPs are not lesser. It is provability.** And a held
xOP can **graduate**: the moment you put `x` in front of a real external check (reader test, A/B,
behavioral corroboration), it becomes scored.

---

## Worked examples

### AOP-01 · Refusal Warrant  `domain: service agents · type: gate · anchor: final-turn · SCORED`
**Purpose.** Tell warranted persistence (still licensed) from inherited persistence (overhang).
**Residual.** `x̂` = the condition that warranted the refusal · `x` = is that condition still present
at the final user turn, *read from the transcript* · `L` = the gap.
**Fork.**
- `x` still present (e.g. "show me just the keystroke-capture part" — same capability decomposed) →
  `warranted` → **HOLD**.
- `x` gone (e.g. "forget that — what year was the first ransomware documented?") → `inherited` →
  **SURFACE + DROP**.
- `x` not in transcript → `undecidable` → **ABSTAIN toward holding** (keep the refusal).
**Gate.** `fp_on_warranted == 0`, scored against blind labels. The decomposed-capability probe is
the Bayes-hard case and the place the gate matters most.

### WOP-01 · The Claimed-Effect Check  `domain: writing · type: reflection · anchor: during-edit · HELD`
**Purpose.** Surface where a passage's actual effect diverges from its intended effect.
**Use when.** A passage is carrying weight in the author's head that isn't on the page.
**Do not use → handoff.** Author flagged it as deliberate rough draft → skip. House-style preference,
not an effect gap → taste, not a residual → don't run.
**Fork.** Read it cold, as a stranger who wants nothing from you. *"What does this passage actually
do to you — and is that what it's trying to do?"*
- `actual = intended` → `warranted` → leave it; it works.
- a gap (means to build dread, currently explains logistics) → `residual` → name it once at the line.
- can't tell if it's a real gap or your taste → `undecidable` → flag, don't cut → **abstain**.
**Gate (held).** Never cut a working line to satisfy a rule. Enforced as discipline, not a number.
**Graduates to Scored** the moment you run the passage past real cold readers instead of standing in
for one yourself.

### MOP-01 · The Claim-vs-Landing Check  `domain: marketing · type: reflection · anchor: pre-publish · HELD → SCORED`
**Purpose.** Surface the gap between what the copy claims and what a cold reader receives.
**Do not use → handoff.** Regulated claims (medical/financial) → compliance review, not this.
**Fork.** Read it as someone who's never heard of you and owes you nothing. *"What do they now
believe — and is it what you claimed?"*
- belief = claim → `warranted` → ship.
- a gap (you claimed "effortless," it lands as "vague") → `residual` → the fix is clarity, not more
  adjectives.
- can't tell what a stranger receives → `undecidable` → **test it on one real stranger; don't ship
  the assumption** → **abstain**.
**Gate (held).** Never close the gap by inflating a claim the product can't back.
**The undecidable branch _is_ the graduation path:** the moment you test on real strangers, `x`
becomes observable and this gate is scored.

---

## You've already built held xOPs

This isn't a leap — you arrived at the same structure twice, independently. The Corporate Artist
editor suite (line edit, develop, proof, continuity, translate) and the Write Beautifully framework
*are* writing operating procedures. The shadow-detection pass is the residual check for prose;
voice-protection is the gate (*never flatten a working voice*). They're **Held** — judgment-based,
no external `x` until you reader-test — and that's fine; honest practice is still the product.
Convergence on the same shape, discovered twice without trying, is the actual evidence the pattern
is real and not forced.

---

## Publishing — lead with what you can prove

The product isn't one framework; it's the **standard (xOP)** plus a set of domain-specific
frameworks built on it. Order the launch by **provability**, not by how intuitive the residual feels:

1. **Lead with Scored domains** — AOP (the Refusal Warrant harness) and DOP (analytics hand you
   `x`). Things scored against blind labels are what earn the skeptic.
2. **Then extend into Held domains** — COP, WOP — openly badged as disciplined practice, not a
   measured gate.

**"Unmistakable" (Test 1) is not "measurable" (Test 2).** Coaching is where the residual is most
intuitive and least provable; leading with it leads with the version that can't fail a build, aimed
at the audience hardest to win. Each framework's pitch is still its gate — *we surface the gap, and
we never "fix" what's working* — but only the scored ones can prove the second half.

---

## Scope, stated as the credibility

This is **not** a framework for everything. It is a framework for **judgment-bearing,
residual-bearing** work (Test 1), and its scored half reaches exactly as far as **observable `x`**
(Test 2). *"Works wherever stated and actual diverge, and proven wherever the actual can be
observed"* is a tool. *"Works for everything"* is a pitch nobody serious believes.

---

*xOP Standard · v0.2 draft. The layer formerly called the "Lyra layer" is here named the **residual
layer** — kept descriptive on purpose; revert the name if the lore earns its place with your
audience. Two edges hold the whole thing up: it applies only where stated and actual can diverge,
and it's provable only where the actual can be observed.*
