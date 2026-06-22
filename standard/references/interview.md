# `/xop interview` — build an AI operating system

> UI label: **"Build my AI operating system."** Technical artifact: an **xOP Project Kit.**
> Behaves like an onboarding consultant, not a form: *"Tell me what you do, what you're building,
> what the AI keeps getting wrong, and what must never be lost — I'll design the system for it."*

Variants: `/xop interview` (full) · `/xop interview role` · `/xop interview project` ·
`/xop interview team` · then `/xop install claude-project` · `/xop audit` · `/xop refresh`.

## The four layers a person's system has

```
Personal Core   rules that follow the person across every project
Role Pack       how an editor / marketer / exec / researcher / operator works
Project Pack    the specific book, brand rebuild, content strategy, team context
Task Skills     the methods that produce an outline, campaign, deck, plan, analysis
```

`xOP Project OS = Core xOPs + Role profiles + Project xOPs + Skills + Guards + Tests`
(the Work Pack formula `Skill + xOP + Guard + Tests`, composed up into one project environment).

**Skill vs xOP vs Guard** (the user never needs this taxonomy; they just get "your Editor OS"):
- *Skill* — how to build a book outline.
- *xOP* — when to preserve the author's structure, when to challenge it, when to ask, when not to rewrite.
- *Guard* — did it keep 24 chapters? did POV drift? were required sections omitted?
- *Tests* — does the system preserve deliberate choices while catching real drift?

## The interview (conversational, one question at a time)

1. **What work are you trying to do?** (edit nonfiction · AEO content · lead a team · brand rebuild)
2. **What should the AI produce?** (outlines · briefs · board decks · Slack · site architecture)
3. **What does the AI repeatedly get wrong?** (rewrites approved work · generic strategy · overclaims · advises before understanding · one voice for every channel)
4. **When would that behavior actually be correct?** ← *the defining xOP question.* (rewriting when I reopen the section · urgency when a real deadline exists · detailed advice when I ask for a plan)
5. **What is fixed or protected?** (premise · audience · brand promise · approved messaging · budget · timeline · leadership principles)
6. **What proves the work is complete?** (every chapter has a purpose · every cluster has evidence + owner · every required page has approved copy · the deck has a decision + next action)
7. **What may the AI do without asking?** (suggest freely · rewrite drafts · change approved text · send messages · publish · make personnel recommendations)

## Recommend before generating — the triage

Always return a plan first, so the interview doesn't manufacture five new xOPs per request:

```
INSTALL        existing xOPs that already fit, as-is
ADAPT          existing xOPs that need a role/project profile
CREATE         genuinely new judgment rules (few)
ADD AS GUARDS  mechanical checks, not xOPs
ADD AS SKILLS  methods for performing the work
```

Prefer INSTALL and ADAPT over CREATE. New situations are **profiles under stable domains**, never
new family letters. (See `domain-profiles.md`.)

## Router discipline (don't activate the whole library)

A Project OS may hold ten procedures, but on any single job the router applies the **one primary
xOP + at most two supporting** ones. More than that is policy noise and makes failures
un-attributable. Worked role examples live in `role-packs.md`.

## The Claude Project install bundle

`/xop install claude-project` emits:

```
my-project-os/
├── PROJECT_INSTRUCTIONS.md     → paste into Claude Project instructions
├── START_HERE.md               → setup check + how to test
├── ROLE_PROFILE.md
├── PROJECT_CONTEXT.md
├── DECISION_LEDGER.md          → approved decisions stay approved until reopened
├── skills/        (outline-development.md, …)
├── xops/          (keep-the-brief.md, done-means-verified.md, …)
├── guards/        (outline-structure.md, house-style.md, …)
├── tests/         (examples.md, opposite-errors.md)
└── STARTER_PROMPTS.md
```

Install: paste `PROJECT_INSTRUCTIONS` → upload the rest to Project Knowledge → open `START_HERE`
and run the setup check → test on two passing and two opposite-error examples.

## The honest boundary (load-bearing — keep it)

Inside a plain Claude Project these files give **persistent instructions and context**. They do
**not** independently prove Claude follows every xOP. Automated Guard execution, traces, and real
conformance need the Lyra extension / CLI / Kit / an external harness. **Every freshly generated
xOP starts at `DESIGNED`** — it does not become `RULE-TESTED`, `HUMAN-EVALUATED`, or
`FIELD-VALIDATED` just because it was installed. "Your AI operating system" is a relatable metaphor
for a context bundle, not a claim that the gates have been validated.

## The promise
**Build an AI that works the way you work.** Tell it your role, your project, and the corrections
you keep repeating; it assembles the Skills, xOPs, Guards, and tests, and hands you a ready-to-install
Project Starter. (Author makes one correction. Suggest finds corrections hiding in your work.
Interview builds the operating system for a role or project.)
