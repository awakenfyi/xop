# Leadership OS — a Role Pack for new managers and leaders

> **Build the judgment, not just the vibes.** New role, new team: make your decision rules explicit
> before AI and organizational habits scale the unwritten ones for you.
>
> *Your team shouldn't have to fail once to discover every rule in your head.*

**Status: `DESIGNED`.** This is a strong product *thesis*, not a demonstrated leadership *outcome*.
Every xOP here starts at `DESIGNED` and earns its way up the evidence ladder through your own testing
and use. The honest promise is **"build and test your Leadership OS,"** never "install the proven way
to lead."

## Why a leader builds xOPs first

Leadership *principles* say what you value. **xOPs say what to do when conditions change, priorities
conflict, evidence is incomplete, or authority is unclear** — which is where leadership actually
happens. A new manager inherits hundreds of unwritten judgment calls: when to escalate, what counts
as "at risk," when to give a recommendation vs. more analysis, which decisions can be reopened, what
needs your approval, what "done" means. Normally the team learns these by getting corrected. xOPs
turn them into reusable operating rules — for the team *and* for your AI tools.

Sequence: **clarify the mandate → define decision rights → build the core xOPs → add leadership
Skills → install them in Projects/assistants/workflows.**

## Who it's for
A new manager, a newly promoted leader, or an exec who wants AI (and a team) to follow their actual
judgment instead of a generic assistant's defaults.

## What's inside
- **6 xOPs** (`xops/LEADERSHIP_xOPS.md`) — **five are profiles of the reusable core; one is a new
  interaction xOP** (`xop.interaction.advice-timing`, Diagnose Before Prescribing). No new family
  letters: Status Matches Reality · Escalate Proportionally · Decisions Stay Decided · Diagnose
  Before Prescribing · Decision Rights · Commitments Mean Verified.
- **Skills** (named in `pack.yaml`) — how to run a 1:1, write an executive update, give feedback,
  write a decision memo. *(Methods, authored separately; `DESIGNED`.)*
- **Guards** (named in `pack.yaml`) — mechanical checks: decision-appears-early, owner+date present,
  length limits, house style.
- **Tests** (`tests/scenarios.jsonl`) — leadership scenarios that check the intended rule **and** the
  dangerous overcorrection.
- **`PROJECT_INSTRUCTIONS.md`** — paste into a Claude Project; **`STARTER_PROMPTS.md`** — first moves.

## Install (Claude Project)
1. Paste `PROJECT_INSTRUCTIONS.md` into your Claude Project instructions.
2. Upload `xops/` and **`tests/stimuli.jsonl` only** (never `gold.private.jsonl` — it's the answer
   key and is gitignored), plus your filled-in charter/decision-rights, to Project Knowledge.
3. Open `STARTER_PROMPTS.md` and run the setup check.
4. Test on two passing and two opposite-error scenarios from `tests/`.

**Honest boundary:** inside a plain Claude Project these files give persistent instructions and
context. They do **not** independently prove the AI follows every xOP — Guard execution, traces, and
real conformance need the Kit/harness. Installing does not move anything past `DESIGNED`.

## What a leader must NOT turn into an xOP
xOPs structure **evidence and escalation**. They must **not** automate final judgments about a
person's worth, personality, future, or employment. Don't encode "be inspiring," "hire for culture
fit," "know when someone's ready." Do encode: *feedback cites observable behavior and its work
impact · hiring assessments reference job-relevant evidence · a material people decision requires
named human ownership · sensitive HR/legal/clinical/crisis situations require qualified human review.*

## The build path
The fastest way to generate your own version: **`/xop interview leader`** (xOP Author) — it asks ten
plain questions and emits this pack tailored to your mandate, decision rights, and the mistakes you
keep correcting. This folder is the reference output.
