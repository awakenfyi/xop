---
name: web-copy-xop
title: Web Copy xOP — Tell · See · Prove
summary: Write world-class web copy by studying the best AI companies and OSS repos, then forcing every block through three modules — Tell, See, Prove.
status: DESIGNED
lab: Marketing Lab
type: lab-xop
---

# Web Copy xOP — Tell · See · Prove

A reusable operating rule for web copy. It studies how the best AI companies and analog OSS repos
actually write, extracts the pattern, and forces every block of copy through three modules:

> **Tell** — say it plainly. **See** — show it concretely. **Prove** — back it with receipts.

Most copy fails because it does one and skips the others: it *tells* (adjectives, no proof), or it
*shows* (a demo with no claim), or it *proves* (stats nobody asked for). World-class copy does all
three, in order, in every section.

This is an xOP: each module is a conduct rule with a **valid exception** and a **test**. Tokens of
proof are receipts; the framework is `DESIGNED`.

## The pattern, from the corpus (observed)
Read directly this session — the pattern is consistent:
- **Tell** is one plain line that names the category or outcome, no jargon. Linear: *"The product
  development system for teams and agents."* Baseten: *"Inference is everything."* Arcade: *"Ship
  agents. Not auth infrastructure."* Basement: *"We make cool shit that performs."* Often shaped
  *"X for Y"* or *"Verb the outcome."*
- **See** is the real product or artifact, not an adjective. Linear shows live issue threads, diffs,
  and roadmaps as the hero. Baseten shows model cards. Arcade shows the runtime diagram. Factory
  shows a live "software factory" dashboard. Show the thing; don't describe it.
- **Prove** is named receipts. Linear: *"powers over 33,000 product teams"* + quotes from OpenAI,
  Ramp, Opendoor with names and titles. Baseten: customer logos + *"3x faster," "160ms."* Arcade:
  *"built by the people who wrote the spec."* Specific, attributable, falsifiable.

### Reference corpus (study these for any new page)
AI companies: Linear, Baseten, Arcade, Factory, Cursor, Intercom Fin, Vercel, Stripe, Perplexity, Anthropic.
*(Observed directly this session: Linear, Baseten, Arcade, Factory, Basement, and Cursor — the last via
its refero Design xOP export, a clean read of its system. The rest are named for the skill to study at
runtime — read them, don't quote from memory. Intercom Fin and others can be added to the corpus.)*
Analog OSS READMEs: Next.js, Supabase, Tailwind CSS, shadcn/ui, Astro, Bun, Zod, tRPC, LangChain, Hono.
READMEs teach the same shape: one-line *what* (Tell), a copy-paste quickstart / GIF (See), badges +
stars + who-uses-it (Prove).

## The three modules, as conduct rules

### TELL — say it plainly
- **Rule:** open every section with one plain sentence naming the outcome or category. Everyday words.
- **Applies when:** any hero, section heading, or card lead.
- **Valid exception:** a single brand/manifesto line may be evocative ("Subtract the noise") — but it
  sits *beside* a plain Tell, never replacing it.
- **Never:** lead with internal jargon, a formula, or an abstraction the reader hasn't been given yet.
- **Test:** a stranger reads only the first line of the section and can say what it's about. If not, FAIL.
  Opposite-error test: if the line is so plain it's generic boilerplate ("AI for everyone"), also FAIL.

### SEE — show it concretely
- **Rule:** pair every Tell with something the reader can see — a specimen, real example, before/after,
  or product artifact.
- **Applies when:** any claim about what the product is or does.
- **Valid exception:** a pure values/why section may stay prose if the See lands in the next block.
- **Never:** describe a capability in adjectives alone, with nothing concrete shown.
- **Test:** remove all adjectives from the block — does a concrete artifact still carry the point?
  If nothing remains, FAIL.

### PROVE — back it with receipts
- **Rule:** every claim has its proof within one screen — and the proof is scoped to what's true.
- **Applies when:** any superlative, metric, or outcome claim.
- **Valid exception:** none for claims. (A brand line makes no claim, so needs no proof.)
- **Never:** an unbacked superlative ("best-in-class"), a fabricated stat, or borrowed social proof
  you don't have.
- **Test:** highlight every claim; each must have an adjacent receipt. Any claim stronger than its
  evidence = FAIL. (This is the project's core rule, applied to copy.)

## Prove, when you're alpha (the honest case)
awaken.fyi has no customers and no validated metrics yet — so its Prove is **not** logos or "33,000
teams." Its receipts are:
- the **evidence ladder** + current status (DESIGNED / RULE-TESTED), shown honestly;
- the **runnable artifact** ("the de-slop guard passes 12/12 fixtures — mechanical behavior only");
- the **specimen** itself (a real xOP, in full);
- the **alpha admission** ("the pilot hasn't run; DESIGNED is not validated").
Honesty *is* the proof for an alpha project. Borrowed credibility would fail the Prove test.

## Modes
| Command | Does |
|---|---|
| `/xop web-copy draft <page/section>` | Write copy, block by block, each hitting Tell → See → Prove. |
| `/xop web-copy review <copy>` | Score each block: does it Tell, See, and Prove? Flag the missing module. |
| `/xop web-copy study <url>` | Extract a site's Tell/See/Prove pattern (pairs with the Design xOP skill). |

## Output discipline
- One idea per block. Plain words. Sentence case. No mid-sentence bolding.
- Run the de-slop guard on every draft (`packs/writing/guard/check_ai_tells.py`).
- Pair with the **Design xOP** for layout and the **xOP Author** discipline (valid exception + test).

## Definition of done
- [ ] Every section opens with a plain **Tell** a stranger understands in one line.
- [ ] Every Tell is paired with a **See** — a real specimen/artifact, not adjectives.
- [ ] Every claim has an adjacent **Prove**, scoped to actual evidence (no borrowed/fabricated proof).
- [ ] Reviewed against the corpus; de-slop guard PASS; no claim stronger than the evidence record.

*A Lab xOP — DESIGNED, grounded in observed sites, used in real content work. Not validated doctrine.*
