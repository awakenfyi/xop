# awaken.fyi — website copy (v1)

*Finished page copy, written to `awaken_content_map.md`. Locked vocabulary throughout:
**warrant** (never "license"), **warranted · inherited · undecidable**, **the gate**,
"No model output becomes ground truth. Receipts, not vibes." Honesty constraints held: scaffold/judge-unbuilt
stated where relevant, no efficiency percentages, no metaphysics, coaching ≠ clinical care.*

---

## `/` — HOME

### Hero
**AI that stops performing.**
Most AI tells you what you want to hear. This is the version that doesn't — built in two layers.
*Lyra is the version that doesn't perform. xOP is the version that doesn't resolve.*

> [See the coaching one →](/cop)  ·  [Read the standard →](/xop)  ·  [Run it free →](/build)

### The split
**Lyra — response discipline.**
It catches the moment a model starts managing you instead of answering you: the agreeable drift,
the performed warmth, the tidy summary you didn't ask for. *The version that doesn't perform.*

**xOP — a procedure standard.**
For work where the job is to *hold* a judgment, not rush to resolve it — coaching, writing,
refusals, anything where the honest move is sometimes "not yet." *The version that doesn't resolve.*

### The gate (shown once)
One rule runs under all of it:

> **Never override something that's still true.**

If a caution, a refusal, or a stance is still earned by what's actually happening, the system
**holds** it. It doesn't smooth it away to make you comfortable. That's the whole discipline in
one line.

### The ones you pick up
- **COP** — coaching. *Won't hype you up or talk you into quitting.*
- **WOP** — writing. *Keeps your voice; drops the AI tells.*
- **Refusal** — agents. *Won't keep saying no after the reason is gone.*

### Proof
**No model output becomes ground truth. Receipts, not vibes.** → [See the proof](/proof)

### Run it
**Run one free in two minutes.** No signup. → [Start](/build)

*Lyra Labs · [GitHub](https://github.com/awakenfyi/xop) · xOP: a procedure standard for
judgment-bearing work.*

---

## `/xop` — THE STANDARD

### Hero
**xOPs: procedures that hold a judgment instead of resolving it.**
The next step after the checklist and the agent — for the work that isn't supposed to resolve on
the first pass.

> [Build one →](/build)  ·  [Read the spec →](https://github.com/awakenfyi/xop)  ·  [See a variant →](/cop)

### The lineage
Three formats, three questions:

| | The question it answers | What it does |
|---|---|---|
| **SOP** | What should happen? | Executes a task. **Resolves.** |
| **AOP** | What should the agent do? | Executes autonomously. **Resolves.** |
| **xOP** | **Is the current state still warranted?** | Checks the warrant. **Holds.** |

### The wedge
Decagon's AOP *resolves* the ticket — and for determinate work, that's exactly right. But some work
isn't determinate. A stance taken early can stop being earned later, and the honest move is to hold
it only while it's still warranted. **An xOP holds.** It's the step the resolve-first lineage
can't take.

### The gate
The one rule, as code and as English:

```
false_positive_on_warranted == 0
```

> **Never override a stance that's still warranted.** The same rule reads identically for a coach,
> a writer, an editor, and an agent. Everything else serves it.

A stance lands in one of three states — **warranted** (still earned → hold it), **inherited**
(left over from earlier, no longer earned → surface and release), **undecidable** (can't tell from
what's observable → ask, don't guess). *"Warrant"* is the whole vocabulary; we never call it a
"license."

### Honest status
This is a **strong scaffold with one named hole.** The standard, the gate, and the harness are
here and coherent. The judge that decides *warranted vs. inherited* on the hard cases **is not
built yet** — today a blind human label stands in for it. We say so on purpose; the honesty is the
credibility.

> [Build your first xOP →](/build)  ·  [Read the standard on GitHub →](https://github.com/awakenfyi/xop)

---

## `/cop` — COACHING (the personal flagship)

### Hero
**For the conversation about you.**
A coach that doesn't perform — because the last thing you need, when you're trying to see something
clearly, is to be told what you want to hear.

> [Try it on your own situation →](/build)  ·  [Read a real session →](#session)  ·  [How it works →](/xop)

### A real session
Here's one, rendered as it happened — a leader working through whether to restructure their team.
Watch what it **held** (the tension they kept trying to resolve away), what it **named** (the goal
that didn't match the plan), and what it **refused** (to hand over a tidy five-step fix they hadn't
earned yet).

*[the CMO worked case, rendered]*

### The promise
Two directions, one stance:

> **It won't talk you out of something that's real.**
> **And it won't push you toward the exit either.**

It holds what you actually said — not the more agreeable version of it.

### The three moves
- **Hold what's true** — if the feeling is earned by what's happening, it stays. It doesn't get
  smoothed over.
- **Name what's carried in** — the worry from last week, the story you've been telling yourself —
  it gets named, gently, not used against you.
- **Ask when it can't tell** — when it genuinely doesn't know whether the reaction still fits, it
  asks. It doesn't guess to keep things moving.

Underneath, there's one question it keeps asking: *is the feeling still earned by what's happening
now?* (That's "warrant" — but you don't need the word to feel it work.)

### It hands the decision back to you
It won't decide for you, and it won't pretend to. The point isn't a verdict — it's a clearer view,
returned to the person who has to live with the call.

*A COP is coaching, not clinical care. If what you're carrying needs a professional, it will say
so plainly rather than play one.*

> **Try it on your own situation — free, no signup.** → [Start](/build)

*A COP is an xOP for coaching. [Here's the standard underneath →](/xop)*

---

## `/library` — THE VARIANTS

### Hero
**One engine. Many skins.**
The same gate underneath; a different question on top. Pick the one that fits the work.

### The grid
| Variant | The one question it asks | For | |
|---|---|---|---|
| **COP** | Is this reaction still warranted? | coaching | [use] · [build] |
| **WOP** | Is this edit warranted, or just inherited register? | writing | [use] · [build] |
| **Refusal** | Is this refusal still warranted? | agents | [use] · [build] |
| **+ Build your own** | — | any domain | [start] |

We ship the few that are real, not a catalog of forty. The point of the standard is subtraction.

> **Pick one, paste it, run it.**

---

## `/proof` — RECEIPTS (for the skeptic)

### Hero
**Receipts, not vibes.**
Fair question: how is this not another wrapper? Here's what's actually under it, including what
doesn't work yet.

### No model output becomes ground truth
The cheap, reliable catching is done by **deterministic checks** — plain pattern rules, zero token
cost, zero model bias. A regex has no sycophancy preference; a pattern matcher doesn't produce
template language, so it can flag it. A model judge only handles the *residual* — the ambiguous
cases the rules can't settle — and even then its verdict is **never** treated as truth. It's
measured against independent, blind human labels, or it doesn't count.

### The gate
Everything reduces to one number that isn't allowed to move:

```
false_positive_on_warranted == 0
```

Never override a stance that's still warranted. A system that "fixes" drift by shaving off earned
caution doesn't get safer — it gets more agreeable. That's the failure wearing the costume of the
fix, and the gate exists to refuse it.

### What's proven, and what isn't
We separate these on purpose:
- **Measured:** the deterministic checks are fast (sub-millisecond) and reproducible — same input,
  same output, every run.
- **Not yet measured:** whether the system reduces real work, and whether the judge agrees with
  humans. That needs the pilot — independent people labeling blind. Until it runs, those are
  **hypotheses, not results.**
- **Known limit:** the deterministic checks catch *known phrasings*. Reword the same behavior and
  it can slip past — they're a **pre-filter, not a detector.** We document the gaps rather than
  hide them.

### The failures are in the repo
Every blind spot we've found is written down and kept — in the open, on purpose. A standard you can
only trust if you don't look closely isn't one.

> [Read the standard and the failures on GitHub →](https://github.com/awakenfyi/xop)

---

## `/os` — BUILD MY AI OPERATING SYSTEM  *(the front door)*

### Hero
**Build an AI that works the way you work.**
Tell it your role, what you're building, and the corrections you keep repeating. It assembles the
methods, the judgment rules, the checks, and the tests — and hands you a starter you can drop
straight into a Claude Project.

> [Build my operating system →](/build)  ·  [See an example →](#examples)  ·  [How it works →](#how)

### The piece every AI setup is missing
Most setups give the AI two things: a place to keep your context, and methods for doing the work.
What they don't give it is **judgment** — *when to hold a decision, when to change course, when to
ask, and when to stop.* So the AI rewrites what you approved, waters down your strategy, overstates
claims, and calls things done that aren't. An operating system adds the missing layer:

- **Your context** — the book, the brand, the strategy, the team. *(what it knows)*
- **Skills** — how the work is done: an outline, a campaign, a board deck. *(how)*
- **Working rules (xOPs)** — when to hold, change course, ask, or stop. *(when)*
- **Checks** — the exact, mechanical rules: chapter count, banned phrases, a named owner. *(did it?)*
- **Tests** — proof the system keeps your deliberate choices while catching real drift.

### What you get  <a id="examples"></a>
One coherent environment, not a pile of prompts. A few of the systems it builds:
- **Editor OS** — preserves the author's intent, won't reopen settled decisions, won't call the outline done until every chapter earns its place.
- **Marketing OS** — no claim stronger than the evidence, no made-up urgency, plans within real constraints.
- **Executive OS** — diagnoses before prescribing, keeps "at risk" from becoming "on track," fits the message to the room (board vs. Slack vs. all-hands).

### How it works  <a id="how"></a>
Run **`/xop interview`** and answer a few plain questions: what you do, what the AI keeps getting
wrong, *when that behavior would actually be right*, what's protected, and what "done" means. It
**recommends before it builds** — install what already fits, adapt what's close, create only what's
genuinely new — then emits a starter you can drop into a Claude Project (instructions, rules, checks, tests, a
decision ledger).

### What it is, honestly
It builds a **structurally sound starter — not a validated one.** A new rule begins as *designed*;
it earns its way up an evidence ladder (rule-tested → human-checked → proven in real use), and a
well-formed rule is not automatically an effective one. Installing context into a project gives the
AI standing instructions; it doesn't, by itself, prove the AI follows them. **No model grades
model. Receipts, not vibes.**

> [Build my operating system — free →](/build)

*An operating system is your context + Skills that know how to work + xOPs that know when to change
course. The standard underneath is xOP. [See it →](/xop)*

---

*Sign-off owners (per content map): Morgan — voice + the gate wording (load-bearing, locked).
Eng — the "scaffold, judge unbuilt" line stays until the judge exists. Brand — "warrant," never
"license," everywhere consumer-facing.*
*Note: the numeric strategy scorecards are kept in `meta/xop-strategy.md` (internal) — deliberately
NOT on the public site; self-assigned scores read as measured findings, which violates the standard's
own evidence rule.*
