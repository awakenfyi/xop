# xOP

![license: MIT](https://img.shields.io/badge/license-MIT-blue)
![status: alpha](https://img.shields.io/badge/status-alpha-orange)
![version](https://img.shields.io/badge/version-0.1.0--alpha-lightgrey)

## You correct the same thing every session. Write it once.

Prompts tell AI **what** you want. Skills teach it **how** to do the work. But you still end up
repeating the same corrections — *don't call it done before it's checked, don't water down the
strategy, don't invent urgency, don't reopen a decision we already made.*

An **xOP** is that correction, written once and reusable: a small operating rule that says **when it
applies, when it should change, and the one thing it must never override.**

> Describe the mistake once. Build the rule.

---

## The 30-second version

An xOP captures a single recurring judgment:

- **Working rule** — what the AI should hold
- **Applies when** — the condition that makes it right
- **Change course when** — what should flip it
- **Never-break rule** — the line it can't cross
- **When unsure** — what it does if it can't tell

That's different from teaching it *how* to write a memo. It's teaching it *when* the rule applies and
when to back off.

## What an xOP looks like

Give it a correction you keep repeating:

> *"Don't say the work is complete until every requested item is verified."*

You get back a clean, reusable rule:

```
Done Means Verified

Applies when        the AI is about to report work as fixed, sent, or complete
Change course when  every acceptance condition has observable evidence
When unsure         report what's done and what's still unverified — don't round up
Never-break rule    never represent attempted work as completed work

Evidence status     DESIGNED   (well-formed; not yet independently validated)
```

*Authoring produces a well-formed candidate. It does not establish that the rule works in practice.*

## Quickstart — what works right now

The **xOP Kit** (reference implementation) is installable today:

```bash
git clone https://github.com/awakenfyi/xop-kit
cd xop-kit
python3 -m pip install -e .

# Scan text against all Guards
echo "Great question! I'd be happy to help." | python3 cli.py scan --pack writing -

# Run the full fixture suite (95/95)
python3 cli.py test
```

> **Note:** `pip install -e .` installs the `xop` entry point to your Python user bin
> (`~/Library/Python/3.x/bin/` on macOS). Add that to your PATH or use `python3 cli.py` directly.

The `xop-author` skill (`/xop`, `/xop suggest`, `/xop interview`) installs as a Claude Project.
The install path (`skills/xop-author/`) is built in Phase 7 — not yet available as a clean install.

## What we're building it for

**Leadership** · **Marketing** · **Research** · **Writing** · **Operations** · **Agents** — anywhere
the same correction keeps coming up. Bundled into **Work Packs** like a Leadership OS or a Reliable
Delivery OS. *(Packs and commands not yet clean-install-tested are marked `PLANNED`.)*

## How the pieces fit

```
Prompt      what do you want?
Skill       how should the work be done?
xOP         when should the rule apply, change, or stop?
Guard       did an exact, mechanical rule fail?
Harness     what runs and traces the system?
Evidence    what actually shows it worked?
```

xOP is the **judgment** layer. Guards check exact rules; Skills teach the method; the harness runs
it; evidence says whether it held.

## What this is — honestly

This is **alpha, in the wild.** Every xOP starts at `DESIGNED` — it has a coherent shape and a plan
to test it. That is *not* the same as proven. Status climbs a ladder, and we never skip rungs:

`DESIGNED → EVALUATION-READY → RULE-TESTED → HUMAN-EVALUATED → FIELD-VALIDATED`

No install, no polished doc, and no authoring step advances that status by itself — only evidence
does. There's no single metric or pilot that validates every xOP: deterministic checks can reach
`RULE-TESTED`, while semantic xOPs need their own evaluation plans. We publish the misses too.
**No model output becomes ground truth** (models may generate candidates and act as measured,
fallible judges). **Receipts, not vibes.**

## Where to go

- **Create one** — once the `xop-author` skill is installed: `/xop` (author) · `/xop suggest` (find
  them in your work) · `/xop interview` (build an operating system for your role). The skill is in
  `standard/SKILL.md`; the `skills/xop-author/` install path is built in Phase 7.
- **Browse the rules** — the [Proposed Core Set v0.1](catalog/core/) (ten cores, all `DESIGNED`).
- **See the experiments** — domain xOPs, prototype packs, and field notes live in **[xOP Labs →](https://github.com/awakenfyi/xop-labs)** (Creative xOPs, Design + Marketing labs, Leadership OS, all `DESIGNED`).
- **Install a system** — ready-made [Work Packs](packs/) (writing guard available now; others in xOP Labs).
- **Read the standard** — [`standard/`](standard/) for the spec, evidence ladder, and failure patterns.
- **Kick the tires** — the reference implementation lives in **[awakenfyi/xop-kit](https://github.com/awakenfyi/xop-kit)** (validator, runtime, CLI).

## The family

- **xOP Standard** — the open format for reusable AI operating rules *(this repo)*
- **xOP Kit** — makes them testable and runnable *([awakenfyi/xop-kit](https://github.com/awakenfyi/xop-kit))*
- **Lyra** — the inference core this standard is built on: coherence metric, drift memory, `L = x − x̂` *([awakenfyi/lyra](https://github.com/awakenfyi/lyra))*
- **Work Packs** — turn rules into complete systems for real jobs *(Leadership OS, Reliable Delivery OS, …)*

## You don't have to be a developer

You need to know your work well enough to notice four things: what the AI keeps getting wrong, when
that same behavior would actually be *right*, what evidence should change the call, and what must
never be lost in the fix. That's an xOP.

---

*MIT licensed · contributions welcome ([CONTRIBUTING.md](CONTRIBUTING.md)) · the standard evolves
under [GOVERNANCE.md](GOVERNANCE.md). Alpha standard + experimental catalog — every public claim is
limited to the evidence attached to each component.*
