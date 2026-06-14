# From SOP to xOP — A Framing for Review

*A handoff document. Status: draft for evaluation. Read this first.*

---

## What this is, and what we're asking of you

This package proposes a procedure format — the **xOP** — for a class of work that today's
operating procedures handle badly. The argument is built as a lineage: the familiar **SOP**,
the agent-era **AOP**, and then the **xOP** as a deliberate inversion of both.

We are not asking "is this clever." We are asking: **does the lineage hold, is the boundary
honest, and is the net-new part actually new?** The reviewer's guide (`03`) lists the specific
claims to test. A worked example (`01`) renders the same situation in all three formats so the
difference is concrete, not theoretical. The full anatomy is in the specification (`02`).

The four files:

- `00_OVERVIEW_SOP_AOP_xOP.md` — this document. The framing argument.
- `01_WORKED_EXAMPLE.md` — one situation, rendered three ways.
- `02_xOP_SPECIFICATION.md` — the format at full depth, component by component.
- `03_REVIEWER_GUIDE.md` — the claims, the soft spots, and what to pressure-test.

---

## The lineage in one breath

**SOP → AOP → xOP. A human procedure became an agent procedure; the xOP is the agent
procedure with its goal reversed — for the work where the goal *should* be reversed.**

Each step is a real evolution, and each has a clear domain:

- **SOP** — a human follows fixed steps to a determinate outcome.
- **AOP** — an agent follows branching steps to a determinate outcome.
- **xOP** — an agent follows branching steps to *surface a judgment and stop*, because the
  outcome is **not** determinate and forcing one is the failure.

The first two converge. The third deliberately does not. That single difference is the whole
proposal, and the rest of this document is making it precise.

---

## What an SOP is

A **Standard Operating Procedure** is a fixed sequence of steps that takes a known input to a
correct output. Reset the device. File the form. Process the refund. Close the ticket.

Its defining properties:

- **One right path** (or a small set of right paths chosen by checkable conditions).
- **Convergent** — every step moves toward completion. The flow has a destination.
- **Success = the procedure was followed and the task is done.** Compliance *is* quality.
- **Judgment is designed out.** The whole point of an SOP is that the operator does not have to
  exercise discretion; the procedure already encoded it.

SOPs are excellent where the work is determinate. They fail — or worse, do harm by hiding the
failure under a green checkmark — where the work requires a judgment the procedure can't make.
"Was this the right call" is not an SOP question.

---

## What an AOP is

An **Agent Operating Procedure** is the SOP ported to an autonomous agent. Production
agent-authoring platforms have converged on a remarkably consistent anatomy for this, and it's
worth stating generically because the xOP borrows almost all of it:

- **An agent shell** — name, live/draft status, traffic share, channel (voice or chat),
  version pin, template lineage.
- **Policies**, split into:
  - **Scenarios** — the procedures themselves. This is the core authoring surface.
  - **Supporting docs** — definitions, glossaries, device/domain references the agent reads.
- **Each scenario** is structured as:
  - **Intent** — "use only when *all* these conditions hold" (a checkable predicate set).
  - **Guardrail** — "do not use when…" (exclusions that route elsewhere).
  - **Branching steps** — walked *one at a time, never combined*, with `IF <response> →
    continue to Step N` logic, sub-steps, and references to other scenarios.
  - **Typed required parameters** — `firstName: string`, `checkInDate: YYYY-MM-DD` — collected
    one field at a time.
  - **Inline tool / variable / API references** embedded in the step text.
  - **Reason codes** — snake_case exit labels (`payment_troubleshooting`) for transfers/closes.
- **Agent-level configuration** — Brand (voice/identity), Rules (global behavior), Background,
  Overrides.
- **Data sources** — knowledge base, APIs.
- **Personalization** — caller identity, channel, conversation settings, session-analysis config.
- **An evaluation rail** — test cases (with **Max Steps**, **Simulations per run**, allowed
  tools, a **User scenario guide**, and a **When-to-fail** condition), test-suite runs,
  A/B experiments with traffic splits, a changelog, and version pinning.

The defining property carries straight over from the SOP: **the AOP is convergent.** Every
branch flows toward *resolved / transferred / closed*. The eval rewards resolution. Success is
the ticket handled. An AOP is an SOP that can branch and call tools — but its destination is
still completion.

---

## What an xOP is

An **xOP** is the same authoring object as an AOP scenario — Intent, Guardrail, branching
steps, typed signals, reason codes, the eval rail — **with the arrow reversed and three fields
added.**

**The reversed arrow.** In an AOP, every branch flows toward resolution. In an xOP, every
branch flows toward *surface the gap, name it once, and stop.* "Continue to Step 5 / transfer to
senior support" becomes "name the gap / abstain / hold." The procedure's job is no longer to
close the loop. It is to make a judgment visible and then deliberately not make it for the
person — because in this class of work, the person's own judgment is the point.

**The three net-new fields** (the parts with no AOP analog — this is where the actual IP sits):

1. **The Residual — `L = x − x̂`.** The gap between what something *does* (`x`, the actual) and
   what it *claims to do* (`x̂`, the stated). The xOP's job is to compute and surface this gap.
2. **The License call — warranted vs. inherited.** Is the stance/reaction/stance *still*
   licensed by what's actually present, or is it carried over from somewhere it no longer fits?
3. **Abstain — a first-class success state.** When the judgment can't be made from available
   signal, saying so is a correct outcome, not a failure to resolve.

**The inverted evaluation.** The eval rail is identical machinery pointed at the opposite
target. The **When-to-fail** condition flips from "failed to resolve" to *"resolved instead of
held"* / *"overrode a warranted state."* And it carries one non-negotiable number, described
below.

---

## The one-line frame

> **An xOP is an AOP with the arrow reversed and three fields added: a residual, a license
> call, and a first-class abstain.**

Everything else — the scenario structure, the branching discipline, the typed parameters, the
test cases, the version pinning — is borrowed wholesale from proven service-agent tooling.
That's deliberate. The recognizability is the on-ramp.

---

## The mapping, area by area

| AOP area (proven service tooling) | xOP equivalent | What changes |
|---|---|---|
| Scenario (Intent · Guardrail · steps) | xOP | The unit of authoring — shape unchanged |
| Intent — run only when all hold | Intent | Kept as-is |
| Guardrail — "do not use when…" | Guardrail → **safety / abstain boundary** | Routes to human / referral / "give the answer they asked for" |
| Branching steps, never combine | Branching moves, never combine | Steps typed by **move** (reflect · ask · hold · name · abstain), not toward close |
| "Continue to Step N / transfer" | "Name the gap once / abstain / stop" | **The arrow reverses** |
| Typed required parameters | **Signals** (stated_reason, intensity, license_state) | Observations, not data to collect-and-close |
| Reason codes (snake_case exits) | Handoff / exit codes | Kept verbatim |
| Scenario → scenario reference | xOP → xOP composition | Kept |
| Brand (voice/identity) | **Stance** ("you surface and hold") | Identity is reflective, not service-helpful |
| Rules (global behavior) | **The honesty layer** (no flattery, one move at a time) | The agent's discipline on *itself* lives here |
| Knowledge base / Supporting docs | **Frames** (the distinction the residual leans on) | |
| APIs | **Ground-truth sources** | The anti-self-grading wiring |
| Channel / Conversation | Channel / **Pacing** | Pause length becomes a real setting |
| Session-analysis config | Reflection-analysis config | Drives the eval |
| Post-conversation code | **Eval hook** — transcript to the judge | Where the residual actually computes |
| Test case → When-to-fail | When-to-fail | The key inversion: *"fails if it resolved instead of held"* |
| Experiments / suite runs / changelog | Same, inverted metric + gate | Green for held, not resolved |

---

## What is genuinely new, and what is borrowed

**Borrowed (and that's the point):** the entire authoring skeleton, the branching discipline,
the typed parameters, the reason codes, the test-case/experiment/changelog rail, version
pinning. None of this is invented here.

**New:** three fields (residual, license, abstain), one reversed flow (surface, don't resolve),
and one non-negotiable number (below). If a reviewer concludes the "new" reduces to those four
things, that's the correct read — the claim is narrow on purpose.

**The one number that cannot move.** Every xOP carries a gate: **false positives on a warranted
state stay at zero.** The reasoning: an xOP that "improves" by closing more gaps — being warmer,
more reassuring, more resolving — will, under any imperfect judgment, start overriding states
that were *correct*: a reaction that was warranted, a refusal that was scoped, a limit that was
real. A procedure that relieves friction by shedding warranted caution doesn't produce a better
outcome; it produces a more agreeable one. So the gate is asymmetric by design: dropping a
warranted state is penalized far more heavily than holding a stale one. **The gate is the
product.** Strip it and an xOP is just a nicely-formatted way to tell people what they want to
hear.

---

## The boundary — where this applies, and where it's theater

The xOP format earns its place **only** when all three conditions hold:

1. **Stated and actual can genuinely diverge** — there is a residual to find.
2. **A stance can be *warranted* or merely *inherited*** — there is a real license call.
3. **Abstaining is sometimes the right answer** — the judgment is not always decidable.

If a task has one determinate right answer — reset the device, file the form, process the
refund — there is no residual and no license call. That is a plain **SOP/AOP**, and adding the
xOP layer to it is theater. So this is explicitly **not** a framework for everything. It is a
framework for the *judgment-bearing, residual-bearing* class of work — coaching, writing and
editing, marketing, teaching, feedback, facilitation, negotiation. The membership test above is
the standard's most important honesty mechanism: a format that names where it does **not** apply
is a tool; one that claims to apply everywhere is a pitch.

We deliberately do **not** ship a large taxonomy of named sub-formats. We define the xOP once,
prove it in two maximally-different domains (one internal/felt, one external/artifact), and hand
readers the membership test so they can derive their own. Proliferating acronyms would
contradict the format's own claim to be subtractive.

---

## Two scales: the work, and the agent

There are two residuals, and the distinction is the architecture.

- **The residual on the work.** `L = x − x̂` applied to the domain object: what the prose does
  vs. what it intends; what the copy lands as vs. what it claims; what the feeling is vs. the
  stated reason. *This is the xOP.* It changes per domain.
- **The residual on the agent itself.** The same `L = x − x̂` applied to the agent's own output:
  did it operate, or perform operating? Did it surface the gap, or flatter toward closing it?
  *This is the honesty layer* (the "Rules" row in the table above). It is the same across every
  domain.

The second one is mandatory here in a way it isn't for service agents. A service ticket has
*free* ground truth — did it resolve? — so the agent's self-honesty can be left implicit. A
judgment task has no free ground truth, so an undisciplined agent will quietly drift into
flattery and *report* that it surfaced a gap while actually closing one. The agent's
self-residual is what keeps the work-residual honest. An xOP without the honesty layer
collapses back into a resolution machine wearing reflective language.

---

## A note on observability (a known soft spot, stated up front)

The residual is cleanest when `x` — the *actual* — can be observed independently of `x̂`, the
claim. In some domains it can: prose read cold by a stranger, copy tested on a real reader,
agent behavior in a transcript. In the felt/internal domains — coaching being the clearest — the
"actual feeling" is **not** externally observable; all you have is the person's report, which is
`x̂` again. So in those domains the residual is *inferred*, not measured.

This is not hidden, and it sharpens rather than weakens the boundary: the format is strongest
where `x` is externally observable, and the felt domains lean harder on the abstain gate
*precisely because* `x` is hard to get. Reviewers should weight this when judging which domains
to lead with. See `03` for the open question this raises.

---

## What we want from review

Read `01` to see the three formats side by side, `02` for the full anatomy, and `03` for the
claims and the questions. The single most useful thing a reviewer can do is attack the
**reversed-arrow claim** (is "surface, don't resolve" actually a coherent and useful procedure
target, or does it collapse into vagueness?) and the **boundary** (is the three-condition
membership test real, or does everything sneak through it?).

---

*Draft for review. SOP → AOP → xOP. One reversed arrow, three added fields, one gate that
can't move.*
