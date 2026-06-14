# awaken.fyi — Content Map (the OP-family site)

*Built in the 1-Pager Web Protocol format (TELL/SEE/PROVE/DO · Must do / Must NOT do · locked
vocabulary). This is the brief any designer/copywriter/engineer builds to. Status: v1 draft for
Morgan.*

---

## 0. What awaken.fyi becomes

Today it's a one-pager about Lyra. It becomes **the home of the OP family** — the place that owns
the category. Two layers, one hand:

- **Lyra** — *response discipline.* How a model behaves while doing any task. (The version that
  doesn't perform.)
- **xOP** — *the procedure standard* for work where the job is to **hold a judgment, not resolve
  it.** Its variants are **COP** (coaching), **WOP** (writing). (The version that doesn't resolve.)

The strategic bet: **own "xOP" the way Decagon owns "AOP."** Decagon's AOP *resolves* the ticket.
An xOP *holds*. We extend their own lineage (SOP → AOP → xOP) and claim the step they structurally
can't — the one for non-determinate, judgment-bearing work.

---

## 1. Locked vocabulary (use only this language)

| Use | Locked term | Never say |
|---|---|---|
| The family | **the OP family** — SOP · AOP · **xOP** | "framework," "prompt library" |
| The standard | **xOP** — "the operating procedure for when the outcome isn't determinate" | "xOP tool/app" |
| The variants | **COP** (Coaching OP) · **WOP** (Writing OP) | "the coaching product" |
| The concept (was "license") | **warrant** — "is this stance still *warranted*?" | "license" (collides with OSS LICENSE) |
| The three states | **warranted · inherited · undecidable** | "pass/fail," "good/bad" |
| The one rule | **the gate** — `never override a state that's still warranted` | "guardrail," "filter" |
| Plain-language hook | *"is it still true, or left over?"* | jargon on the consumer pages |
| Credibility line | **"No model grades model. Receipts, not vibes."** | "AI-powered," "magic" |
| Lyra line | "the version that doesn't perform" | — |
| xOP line | "the version that doesn't resolve" | — |

**Note on register:** technical pages use *warrant / warranted / inherited*. Consumer pages (COP,
Home) use the plain hook — *"is it still true, or is it left over from somewhere else?"* — and only
introduce "warrant" once.

---

## 2. Audience clusters (5)

- **C01 · The Operator (non-technical, personal)** — a leader/coach/writer who feels the AI
  flattering them and wants the version that tells the truth. **Lands on:** Home → COP. *Primary for
  the personal story.*
- **C02 · The Builder (technical)** — wants to build/run/validate an xOP. **Lands on:** xOP → Build →
  GitHub.
- **C03 · The Skeptic** — "prove it isn't another wrapper." **Lands on:** Proof (receipts, the gate,
  no-model-grades-model).
- **C04 · The Team Lead** — has internal AI workflows drifting into sycophancy. **Lands on:** Lyra →
  xOP for teams.
- **C05 · The Category Watcher** — knows AOP/Decagon, wonders what's next. **Lands on:** xOP (the
  lineage + the wedge).

---

## 3. Sitemap

```
/                Home — the OP family (Lyra + xOP), one breath each
/xop             xOP — the standard (lineage, the gate, the wedge vs AOP)
/cop             COP — coaching, the PERSONAL flagship (non-technical, dograh-warm)
/library         The variants grid — COP · WOP · Refusal · build-your-own (livekit-agents-ui style)
/build           Build/Use — the two no-code doors (paste builder / paste runner)
/lyra            Lyra — response discipline (existing page, kept)
/proof           Receipts — the gate, the harness, no model grades model
/standard        → github.com/awakenfyi/xop (the canonical definition)
```

Aesthetic north stars: **rumilabs** (calm editorial clarity), **livekit/agents-ui** (the variants
as a clean component grid), **dograh/pricing** (warm, personal, plain-language). Keep the current
dark Lyra palette; xOP gets the lavender accent.

---

## 4. Page brief — HOME (`/`)

**Overview.** First-time visitor (C01/C05). Proves awaken.fyi is one coherent idea — *AI that
stops performing* — delivered as two layers. ~50 words. Lead with the visitor's feeling (the AI
agrees too easily), not our architecture.

**CTAs.** T1 *"See the coaching one"* (→/cop) · T2 *"Read the standard"* (→/xop) · T3 *"Run it free"*
(→/build)

**Must do**
- Land the family in one line: *Lyra = doesn't perform; xOP = doesn't resolve.*
- Make a non-technical person feel it in the first screen.
- Show the gate once, plainly.
- Name COP/WOP as the things you actually pick up.
- Keep it one quiet screen-and-a-half. No feature wall.

**Must NOT do**
- Don't lead with "framework," "protocol," or the harness.
- Don't explain the residual math on Home.
- Don't make it look like a dev tool first.

**Page Construct**
```
TELL   Hero — "AI that stops performing." one line on the two layers.
SEE    The split — Lyra (doesn't perform) | xOP (doesn't resolve), two cards.
PROVE  The gate, shown once: "never override something that's still true."
SEE    The variants you pick up — COP · WOP · Refusal (3 cards).
PROVE  "No model grades model. Receipts, not vibes." (one line + link to /proof)
DO     CTA banner — "Run one free in 2 minutes."
FOOTER Lyra Labs · GitHub · the one-line definition.
```

---

## 5. Page brief — xOP (`/xop`)  ·  page type: **the standard**

**Overview.** C02/C05 land here to understand and adopt. Proves xOP is a real, ownable category —
the next step after SOP/AOP — with one unbreakable rule. ~50 words. Lead with the lineage; it's the
legitimacy.

**CTAs.** T1 *"Build one"* (→/build) · T2 *"Read the spec"* (→GitHub) · T3 *"See a variant"* (→/cop)

**Must do**
- Open with the lineage SOP → AOP → **xOP** as three questions.
- State the wedge against Decagon's AOP explicitly but respectfully: *AOP resolves; xOP holds.*
- Show the gate as the hero artifact (like Lyra shows its score).
- Define "warrant" once; never "license."
- Link the variants as the adopt surface.

**Must NOT do**
- Don't claim the judge is built (it isn't — say "strong scaffold, judge unbuilt").
- Don't say "license."
- Don't bury the one-rule under the schema.

**Page Construct**
```
TELL   Hero — "xOPs: procedures that hold a judgment instead of resolving it."
SEE    Lineage table — SOP/AOP/xOP as three questions (xOP row highlighted).
PROVE  The gate — false_positive_on_warranted == 0, in plain words beneath the code.
SEE    The wedge — "Decagon's AOP resolves. An xOP holds." (a clean 2-col contrast)
SEE    The library — COP · WOP · Refusal + "build your own."
PROVE  "No model grades model" + the honest-status line (scaffold, not benchmark).
DO     CTA — "Build your first xOP" / "Read the standard on GitHub."
```

---

## 6. Page brief — COP (`/cop`)  ·  page type: **the personal flagship**

*This is the page that makes it personal. Warm, plain, dograh-style. No jargon until earned.*

**Overview.** C01 (non-technical) lands here, often from a moment of "my AI just told me what I
wanted to hear." Proves the idea on a human story: a coaching conversation that holds what's real
instead of flattering or fixing. ~50 words. Lead with their experience, not our mechanics.

**CTAs.** T1 *"Try it on your own situation"* (→/build with COP preloaded) · T2 *"Read a real
session"* (→ the CMO worked case) · T3 *"How it works"* (→/xop)

**Must do**
- Open in plain language: *"A coach that won't hype you up or talk you into quitting."*
- Use the real worked example (the CMO session) as the SEE — it's the proof.
- Land the two-direction gate as a human promise: *it won't talk you out of something real, and it
  won't push you toward the exit either.*
- Introduce "warrant" gently, once, as *"is the feeling still earned by what's happening now?"*
- End on agency: *it hands the decision back to you.*

**Must NOT do**
- Don't show YAML, schema, or the harness on this page.
- Don't say "residual," "detector," or "license."
- Don't make it sound clinical or like therapy (name the boundary: it's coaching, not treatment).

**Page Construct**
```
TELL   Hero — "For the conversation about you. A coach that doesn't perform."
SEE    A real session, rendered — the CMO transcript: what it held, what it named, what it refused.
PROVE  The promise — two lines: "won't talk you out of what's real" / "won't push you out the door."
SEE    The three moves, in plain words — hold what's true · name what's carried · ask when unclear.
PROVE  "It hands the decision back to you." (one quiet line)
DO     CTA — "Try it on your own situation — free, no signup."
FOOTER "A COP is an xOP for coaching. Here's the standard underneath →"
```

---

## 7. Page brief — LIBRARY (`/library`)  ·  page type: **the variants grid**

**Overview.** C02/C01 browsing for the one that fits them. Proves this is one engine wearing many
skins — the adopt surface. livekit/agents-ui component-grid feel. ~50 words.

**Must do**
- Grid of variants, each a card: name · the one question it asks · who it's for · "use / build."
- Make "+ build your own" a first-class card.
- Every card runs with the same two no-code doors.

**Must NOT do**
- Don't sprawl into a giant catalog (contradicts the subtractive claim). Ship the few that are real.

**Page Construct**
```
TELL   "One engine. Many skins."
SEE    Grid:
        COP · "is this reaction still warranted?" · coaching · [use] [build]
        WOP · "is this edit warranted, or inherited register?" · writing · [use] [build]
        Refusal · "is this refusal still warranted?" · agents · [use] [build]
        + Build your own · [start]
DO     "Pick one, paste it, run it."
```

---

## 8. Content considerations (sign-off + layering)

**Sign-off**
- Morgan · voice + the one-rule wording (the gate phrasing is load-bearing; lock it).
- Eng · the "scaffold not benchmark" honesty line stays until the judge exists.
- Brand · "warrant" replaces "license" everywhere consumer-facing.

**Audience layering**
- C01 (Operator) — Home hero + the entire COP page. Plain language, the human promise.
- C02 (Builder) — xOP + Build + the GitHub link. Warrant/schema OK here.
- C03 (Skeptic) — Proof page; the gate, the harness, "no model grades model."
- C05 (Category watcher) — the lineage + the AOP wedge on /xop.

**Open naming decisions for Morgan**
1. Confirm **warrant** replaces **license** (recommended). One-shot repo rename available.
2. Repo name: **github.com/awakenfyi/xop** (recommended) vs `xop-standard`.
3. Variant abbreviations: lock **COP / WOP**; decide the agent variant's name (Refusal xOP vs ROP).
```
```
