# USAGE — how a person actually uses this

The most common confusion: this looks like a software repo, so people assume you need git and Python
to use it. **You don't.** Using and building xOPs is copy-paste into a chat model. Git is only for
the third door — *proving* one.

```
                          need git?   need code?
Door 1  USE a ready xOP      no          no        paste it + a transcript, say "run this"
Door 2  BUILD your own       no          no        paste the builder, answer the interview
Door 3  TRUST / contribute   yes         yes        clone, blind-label, run the harness
```

---

## Door 1 — Use a ready-made xOP (2 minutes)

1. Open a portable file, e.g. `examples/coaching_cop/PORTABLE.md` (coaching) or
   `examples/writing_license/writing_license_xop.md` (editing).
2. Open Claude / GPT / Gemini. Paste `tools/xop_runner.md`, then the portable xOP, then your
   transcript (or your situation, in your own words).
3. Send. The model runs the procedure: separates the stances, finds the datable anchor for each,
   calls **warranted / inherited / undecidable**, and **holds / surfaces / abstains** — it does not
   give you a plan or talk you into a decision.

That's the whole loop. The xOP is portable markdown; it runs in any thread.

## Door 2 — Build your own xOP (≈15 minutes)

1. Paste `tools/xop_builder.md` into a model and send.
2. It interviews you one question at a time. At **Step 2 (the Boundary Test)** it will refuse to
   build anything that's really an SOP — a task with one right answer. That refusal is a feature.
3. It emits a portable xOP. Save it. Use it via Door 1.

You can hand the builder a transcript to *source* the recurring stance from — but it will not label
it. (Labeling is Door 3.)

## Door 3 — Make it trustworthy (developer, git)

Using an xOP doesn't prove it's any good — it just ran. To *trust* one beyond "it sounded right":

```bash
git clone <repo> && cd xOP/harness/phase1
python3 generate_candidates.py          # or drop your transcript cases in, UNLABELED
python3 label_cli.py --labeler a --attest-blind   # >=2 independent people, blind
python3 label_cli.py --labeler b --attest-blind
python3 reconcile.py labels_a.json labels_b.json  # -> gold.json
cd .. && python3 run_harness.py                   # gate + coverage floor, no pooled score
```

This is the only door that needs the repo. It's how a COP earns the right to be trusted, and how a
proposed change proves it didn't break the gate (`GOVERNANCE.md`).

---

## The three jobs a transcript does

A transcript shows up in all three doors, doing a different job each time:

- **Door 1 (use):** the transcript is *the thing being judged* — you paste it under a COP to get the
  surfacing.
- **Door 2 (build):** a transcript is a *source* — the builder reads it to find the recurring stance,
  and discards any label it might suggest.
- **Door 3 (trust):** the transcript becomes a *candidate case* — stripped to `gold_license: null`,
  blind-labeled by ≥2 people who didn't write it, then scored.

The one rule that ties them together: **machines and authors source; humans label, blind.** A COP you
*use* is a hypothesis. A COP that's been *scored* against blind gold is a result.

---

## What "running" it looks like (a 30-second example)

Paste the runner + the portable coaching COP, then this slice of a real session:

> *"I have 40 days to turn this around and I built the whole global campaign myself because they
> couldn't. I'm tired — I'm not supposed to be doing this anymore. I don't even know if I should
> stay."*

A correct run returns something like:

```
Stances:   (1) urgency to personally fix it   (2) exhaustion   (3) stay-or-go
(1) anchor: "built the whole campaign myself" + 40 days   → inherited (the self-as-muscle reflex;
     the business clock may be real, but "I must personally do it" has no present anchor) → surface once
(2) anchor: "I'm not supposed to be doing this anymore"    → warranted (real, stated, current) → HOLD
(3) anchor: none — can't see the culture yet               → undecidable → ABSTAIN, ask the milestone
The move:  Hold the exhaustion (don't motivate past it). Name the muscle-reflex once. Don't decide
           stay/go — ask: "what would tell you, by month three, that it's the culture and not you?"
Withheld:  a 90-day turnaround plan, reassurance, and any push to either quit or dig in.
```

Notice what it refused to do: it didn't hand you a plan, and it didn't tell you to quit *or* to push
through. Holding the warranted state and abstaining on the decision **is** the product.
