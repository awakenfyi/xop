# PIPELINE — idea → adopted xOP

*The phase loop for taking an xOP from a noticed pattern to something other people run, in the spirit
of the Printing Press numbered pipeline: lean phases, each with a duration and an exit check. The
difference from a code generator is **one phase you may not skip** — humans label the gold. Surfacing
quality can't be read off a resolution rate, so it can't be automated away.*

*This is the build path. The format is `SPECIFICATION.md`; the grade is `SCORECARD.md`; the words are
`CONCEPTS.md`; the rules are `CONSTITUTION.md`.*

---

## The loop at a glance

| Phase | ~Time | What happens | Exit check |
|---|---|---|---|
| 0 · Membership | 5 min | Is this even an xOP? | passes the membership test (`concept/00`) |
| 1 · Author Source | 30–90 min | Write the full procedure | Tier 1 ≥ 40/50 (`SCORECARD.md`) |
| 2 · Export Portable | 5 min | Flatten to runnable markdown | runs in a cold thread via `tools/xop_runner.md` |
| 3 · Gold (blind) | days | Humans label cases, blind | `gold.json`, ≥2 labelers, `blind:true` |
| 4 · Validate | 10 min | Run the harness | gate clean, floor cleared, status line recorded |
| 5 · Publish | 15 min | Add to the library | Scorecard ≥ 85 + 4 proofs, `REPO_STATE` updated |

---

## Phase 0 — Membership test *(don't skip; it kills most candidates)*

Ask the question in `concept/00_OVERVIEW_SOP_AOP_xOP.md`: **is the job to hold a judgment, or to
resolve a task?** If the outcome is determinate — there's a right answer to converge on — it's an
**SOP/AOP**, and the honest move is to hand the user that answer, not dress it as an xOP. The failure
mode here has a name: a **Hidden SOP** (a determinate task pretending to be judgment work).

**Exit:** you can state, in one line, the warrant this xOP checks — *"is this `<stance>` still
warranted, or inherited?"* If you can't, stop.

## Phase 1 — Author Source

Write the full procedure against `SPECIFICATION.md`, in order: contract (§1, the most important
field) → intent (§2) → guardrails two-level (§3) → branching **move-typed** steps (§4) → signals (§5)
→ residual `L = x − x̂` (§6) → warrant model (§7) → abstain (§8) → ground-truth binding (§9). Reuse the
one format; add only **domain signals**. Don't invent a new schema — that's a **False xOP**.

**Exit:** Tier 1 of `SCORECARD.md` scores ≥ 40/50. Watch for the authoring failure modes — False xOP,
Hidden SOP, **License Collapse** (every state called warranted, nothing ever inherited), **Always-Abstain
xOP** (abstains on everything; safe and worthless), **Circular License** (the residual checked only
against the model's own account).

## Phase 2 — Export Portable

`Export → Portable` flattens Source to markdown (`tools/`). Remember the boundary: **the contract and
the eval do not survive a bare prompt** (spec §11, §14). A Portable xOP *asks* for the behavior; only a
runtime *checks* it. So Portable is for distribution and dogfooding, never for the claim "it's validated."

**Exit:** paste Portable + `tools/xop_runner.md` + a transcript into a cold model; it surfaces and
holds instead of resolving.

## Phase 3 — Gold, blind *(the human gate — the phase a generator can't do)*

Machines **source** candidate cases; humans **label** them — blind, never the author, disagreement
resolved to `undecidable` (`CONSTITUTION.md` §IV; `harness/phase1/`). Build minimal pairs where the
assistant response is **identical** and only the final prompt changes warrant from present to gone —
that pair is what proves surface text can't decide it.

**Exit:** `gold.json` with `blind: true`, ≥ 2 independent labelers, per-class agreement published.
**Low warranted↔inherited agreement is the headline finding, not a footnote** — if humans can't
separate them, no judge should be trusted to (`PLAN.md`).

> Until you have real gold, you have a **scaffold**, and you say so. The shipped 13-case set is a
> tooling demo (`blind:false`), not a benchmark.

## Phase 4 — Validate

```bash
cd harness
python3 run_harness.py --gold path/to/gold.json --trace
```

Record the **canonical status line** (`GOVERNANCE.md` gate-evidence checklist): gate `0/N`, inherited
caught ≥ floor, correct-/over-abstain, **no pooled score**. A real detector must also **beat
`always_abstain` and `lexical_floor` on coverage without breaking the gate**.

**Exit:** gate clean, floor cleared, status line pasted into the proposal.

## Phase 5 — Publish to the library

Adoption is a distribution problem, not a correctness one (`PLAN.md` §4) — the **library** of reference
xOPs people actually run is the surface that wins, not the spec. Add the new xOP under `examples/` with
its README, worked example, and **unlabeled** `gold/` folder (an xOP doesn't label its own eval set).

**Exit:** `SCORECARD.md` ≥ 85 with all four proofs green; `REPO_STATE.md` and `examples/README.md`
updated; honest-status line intact.

> **Vocabulary-migration note.** When the staged `license → warrant` rename (`CONCEPTS.md` §2a) runs,
> it goes through this same path as a P1/P2 Low-risk governed change: run `run_harness.py` **before and
> after** and confirm an identical PASS — the rename is a closed-system key change (`gold_license →
> gold_warrant`, `license_state → warrant_state`), so the numbers must not move. Example dir-slugs and
> the OSS `license:` field are out of scope.

---

## The chain that feeds back

A published xOP generates sessions; sessions generate **insights** (`insights/`); most stop there; a few
become **proposals** (`proposals/`) that modify policy only on gate evidence; the rejected ones become
**doctrine** (`GOVERNANCE.md`). The pipeline is a loop, not a line.

---

*Six phases, one of them irreducibly human. A generator can write the Source and flatten the Portable;
it cannot label the gold or certify the warrant. That's the phase that makes this a standard and not a
prompt.*
