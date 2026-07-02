# Making xOP the Layer Standard

*How xOP becomes the industry contract between skills and harnesses. July 2026.*

---

## The claim to own

The 2026 stack has settled into layers with names: prompts say **what**, skills say **how** (SKILL.md is now a de-facto convention), harnesses **run** the loop (Claude Code, OpenAI Agents SDK, LangGraph), evals **score** afterward. There is exactly one unnamed layer: the contract that decides, *during* the loop, whether to keep going, change course, ask, stop, or hand off. Every harness improvises it; no two agree; none of it is portable.

That's the position statement, one line:

> **Skills teach the work. xOPs bound the judgment. Harnesses enforce the contract.**

Standards don't win by being the best framework. They win by being the *interface* everyone else's framework speaks — TCP, OpenAPI, MCP. So the expansion strategy is: stop being a framework, become a wire format.

## Move 1 — Freeze a tiny wire format (the actual standard)

Everything needed already exists in xop-kit as Python dataclasses. Extract it into **versioned JSON Schemas** — the xOP Protocol v1.0 — and let the prose spec orbit them:

| Schema | Already exists as | What it standardizes |
|---|---|---|
| `GuardReport` | `guards/base.py` | finding: rule, tier, severity, location, context |
| `Disposition` | `xops/base.py` | judgment: keep / replace / delete / abstain + warrant + gate_status |
| `ReleaseDecision` | orchestrator | RELEASE / RETRY / HOLD / HALT / INVALID — never the same field as a disposition |
| `xop.yaml` header | spec §1 | the contract block: `optimizes_for / never_for / gate` |
| Exit contract | loops essay | exit codes + stderr feedback shape for any hook system |

Rule of standards: the spec that fits on five pages gets adopted; the one that needs a constitution gets admired. Keep the constitution — it governs *your* catalog — but the wire format must be implementable by a stranger in an afternoon, in any language, without reading a single essay.

## Move 2 — Attach to the skills rail (the wedge)

Skills are the fastest-spreading convention in the ecosystem, and they have a known hole: a skill says how to do the work, and nothing says when the work should stop, hold, or escalate. That's the wedge, and it's one line of frontmatter:

```yaml
# SKILL.md
name: quarterly-close-narrative
xops:
  - done-means-verified
  - claims-need-receipts
gate: false_positive_on_warranted == 0
```

A skill that declares its xOPs is a skill with a conduct contract; a harness that reads the field enforces it. Campaign line: **"No skill without a stop condition."** Ship it first in your own plugins, then propose the field as a convention PR to the skill-spec ecosystems. Even if upstream never merges it, tooling that *reads* the field makes it real — that's how `.editorconfig` and `agents.md` happened.

## Move 3 — Three adapters or it isn't a standard

One ecosystem is a feature. Three is a standard. Reference adapters, thin by design:

1. **Claude Code / Cowork** — Guards as a stop hook (exit 0/2 + stderr report), the release controller as the loop's exit condition. Your home turf; ship first.
2. **OpenAI Agents SDK** — xOP as a guardrail/handoff policy object speaking the same JSON.
3. **LangGraph** — a release-control node: any graph can route RELEASE/RETRY/HOLD/HALT on a GuardReport edge.

Plus the **MCP server** (scan/judge/release as tools) so anything MCP-speaking gets the contract without an adapter at all. Each adapter is a weekend of code precisely because the wire format is small — that's the test that Move 1 was done right.

## Move 4 — Conformance is the moat

What made OpenAPI and USB standards rather than suggestions: a conformance suite and a mark. You already have the DNA (95/95 fixtures, fail-closed dataclasses). Extend it upward into **harness conformance**:

A harness is *xOP-conformant* if it: enforces the gate as a hard stop, never lets a disposition and a release decision share a field, routes ABSTAIN → HOLD (never silent-ship), separates evaluator failure (INVALID) from evaluation results, and passes the public fixture suite. Ship `xop conformance <endpoint>` in the kit; publish the passing list; let vendors self-certify against a suite they can't game because the fixtures are blind-labeled duets. The gate is the one clause competitors can't copy without becoming you — a "flexible gate" is a different (and worse) product, visibly.

## Move 5 — Give the standard away, keep the receipts

One-person repos don't become standards; neutral processes do. Sequence: freeze v1.0 under an RFC process (GOVERNANCE.md is already most of this — proposals modify policy, only the gate can merge, popularity can't); recruit two or three named co-maintainers from *other* orgs (an evals person, a harness person); consider a `/spec` split so the protocol lives apart from Lyra Labs' catalog and brand. What stays yours forever: the catalog of validated xOPs, the benchmark, the labeled gold, the Lyra runtime — the receipts. The protocol becomes everyone's; the evidence stays the business.

## Move 6 — Export the vocabulary on schedule

Standards travel as words before they travel as schemas. The exportables, in launch order: **the duet** (the instrument — ships with the benchmark), **overhang / warranted / inherited / undecidable** (the states — ship in every adapter's log output so developers *see* them daily), **RELEASE / RETRY / HOLD / HALT** (the verbs — already the most adoptable piece; a LangGraph dev who's never read the spec will still name their edges this), and **the gate** (the value — the thing conference talks argue about). When someone who's never heard of Lyra Labs writes "this looks like overhang" in a code review, the standard has happened.

## What could kill it (name the risks now)

**The platform absorbs the layer.** Anthropic or OpenAI ships native "conduct contracts" and the wire format becomes theirs. Defense: be embedded in their ecosystems first (Move 3), be the conformance authority (Move 4), and hold the only blind-labeled evidence (Move 5). Standards bodies survive platforms by owning the test, not the runtime.

**Spec sprawl.** The repo's instinct is more concepts, more essays, more governance. Every page added to the protocol halves the number of strangers who implement it. The five-page rule is a gate too.

**Unproven gate at scale.** The pilot still comes first. A standard whose central claim fails its own benchmark is over; a standard that published the failure and revised is credible. Sequencing is unchanged: receipts, then rails, then RFC.

## The 6-month shape

Month 1–2: JSON Schemas frozen (v1.0-rc), Claude Code adapter shipped in your own plugins, pilot running.
Month 2–4: OpenAI + LangGraph adapters, MCP server, conformance suite public, benchmark launched.
Month 4–6: v1.0 freeze under RFC, co-maintainers named, `xops:` frontmatter convention proposed upstream, first external conformant harness announced.

The one-sentence version of the whole strategy: **make the contract so small that adopting it is easier than arguing with it, and keep the evidence so rigorous that competing with it means running your benchmark.**
