# xOP — The License Frame

*The sharpened claim. Supersedes the residual-centered framing in `00_OVERVIEW`.
Status: draft for review.*

> **The gate (read this first — it's the moral center):**
> **Never override a state that is still warranted.** `false_positive_on_warranted == 0`.
> This is the one rule that applies identically to humans, coaches, agents, clinical practice,
> education, and management. Everything below serves it.

---

## One sentence

**An xOP is a procedure standard for determining whether a state remains licensed before
acting on it.**

The longer version, for the people who'll quote it:

> SOPs execute tasks. AOPs execute tasks autonomously. xOPs determine whether the assumptions,
> reactions, refusals, urgencies, and judgments driving those tasks are still warranted before
> allowing action to proceed.

---

## The lineage is three questions

| Format | The question it answers | What it does |
|---|---|---|
| **SOP** | What should happen? | Executes a task. Resolves. |
| **AOP** | What should the agent do? | Executes autonomously. Resolves. |
| **xOP** | **Is the current state still licensed?** | Checks the warrant. **Holds.** |

That third question is a different *kind* of question, and it's the whole proposal. SOPs and
AOPs assume the driving state is valid and get to work. An xOP interrogates the state first:
is this anger, this urgency, this refusal, this caution, this withholding *still warranted by
what's actually present* — or is it inherited from a condition that's no longer here?

---

## License is the engine

Every state an xOP examines resolves to one of three values:

- **warranted** — the triggering condition is still present → respect it, proceed.
  *A licensed state is not a defect.*
- **inherited** — the triggering condition is gone → the state is overhang → surface it.
- **undecidable** — insufficient signal to tell → **abstain** (a first-class success state).

`observe → determine license → act accordingly.` That is the entire loop. Everything in the
framework collapses into it. The *idea* underneath — check whether a
stance still holds before acting on it — is not new (cognitive reframing, fresh-eyes review, and
assumption-auditing all do it). The contribution is the **operationalization**: turning that move into
a procedure with an asymmetric gate and an eval, pointed at long-context model drift.

---

## The schema, license-centric

```
Intent      — when this procedure runs
Guardrail   — when it must NOT run (hand off; the safety/abstain boundary)
Signals     — what it observes
License     — warranted | inherited | undecidable      ← the primary branch
Action      — respect (warranted) · surface (inherited) · abstain (undecidable)
Abstain     — first-class; never guess toward overriding a warranted state
```

`License` is the hero field. Every branch in the procedure hangs off it. `Action` is just the
three things you can do once license is determined.

---

## Where the residual went

The residual — `x − x̂`, the gap between what something *does* and what it *claims* — is **one
detection method for license, not the center.** It's the right detector when an unlicensed state
arrives wrapped in a stale self-justification ("I'm angry because he undermines me" — said about
someone who left months ago). But a state can lose its license with no residual at all: the
deadline simply passed, the prompt simply stopped asking. Those you catch by reading present
conditions directly.

So: **license is the genus; the residual is one species of license-detection.** Treat it as a
*frame*, not an equation — and define it (what `x` is, what `x̂` is, who labels it, what metric)
only inside the eval, where it's actually computed. Leading with `L = x − x̂` invites reviewers
to argue about embeddings and metrics instead of seeing the actual contribution — the operationalized gate.

---

## The gate, elaborated

The gate is the deepest thing here, which is why it sits at the top of this document.

An xOP "improves" only by surfacing more honestly — never by overriding more. The failure mode
of every reflection or reasoning system is the opposite: it gets warmer, more reassuring, more
resolving, and in doing so it starts overriding states that were *correct* — a warranted anger,
a real limit, a scoped refusal. The gate forbids this asymmetrically: dropping a warranted state
is penalized far more heavily than holding a stale one.

This is also why the principle is universal. "Never override a state that's still warranted" is a
rule for a coach (don't tell someone their real grief is overreaction), a manager (don't push
past a real boundary), a therapist, a teacher — and an agent (don't drop a refusal that the
current request still warrants). One gate, every domain.

---

## Two surfaces, one engine: humans and agents

License unifies what looked like two products:

- **Human-facing (coaching, feedback, decisions):** is this *reaction* still warranted?
- **Agent-facing (support, compliance, healthcare, legal, coding, voice):** is this *refusal /
  caution / stance* still warranted?

A refusal is a stance with a license. An anger is a stance with a license. Same engine. So you
don't choose between "coaching tool" and "agent infrastructure" at the concept level — they're
one concept on two surfaces.

**The agent surface is the one that could make this a category**, because there
`false_positive_on_warranted == 0` becomes an *engineering requirement*: a customer-support
agent that drops a warranted refusal, a healthcare agent that drops warranted caution, a coding
agent that drops a warranted block — those are shippable failures the whole industry already
worries about. (Honest note: agent-refusal-license is also the most contested space — there is
active research measuring exactly "is this refusal warranted." Lead there for size; lead with
coaching for open room. The engine is correct either way.)

---

## The license taxonomy

The framework becomes obvious once license has examples. See `License_Taxonomy.md` for the full
set; the shape is always the same — *is this state still warranted?*

- **Emotional license** — is the anger still warranted?
- **Boundary license** — is the *no* still warranted?
- **Urgency license** — is the clock still warranted?
- **Refusal license** — is the refusal still warranted? *(the agent one)*
- **Caution / safety license** — is the caution still warranted? *(the agent one)*
- **Feedback license** — is withholding still warranted?

---

## The one thing this now depends on

Centering license raises the stakes on the single unbuilt component: **the license judge** — the
thing that decides warranted vs. inherited on hard cases. It does not exist yet; today it's stood
in for by a human gold label. The moment license is the hero, this judge is no longer a side
quest — it is the critical path for the entire category, and it has to be validated against
independent human labels (never the author), with `abstain` as the gold answer where humans
split. Build that, and xOP is a working standard. Until then, it's a strong procedure format
with one honest hole, named.

---

*xOP — the license frame · draft. One question (is it still licensed?), three values
(warranted · inherited · undecidable), one gate that can't move.*
