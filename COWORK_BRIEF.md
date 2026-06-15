# xOP — Project Distill / Cowork Brief

*A portable handoff for anyone (technical or not) picking this up cold. Distilled from the working
thread of 2026-06-14. Captures decisions, rejections, current state, and exact next steps — not a
summary.*

> **xOP in one breath:** a procedure standard for judgment-bearing work — work where the job is to
> check whether a stance is **still warranted** and **hold** it, not to resolve a ticket. SOPs and
> AOPs resolve. An xOP holds. The one rule (the gate): `false_positive_on_warranted == 0` — never
> override a state that's still warranted.
>
> **Status line (say it honestly):** strong scaffold, **the warrant judge is unbuilt** — a blind
> human label stands in for it today. The harness, governance, spec, and examples are real.

---

## 1. The Story

The thread started as "get the Lyra formulas and xOPs right for awaken.fyi, update GitHub, in Matt
van Horn's Printing-Press style." On inspection, the **formulas were already consistent**
(`L = x − x̂`, drift, the gate) — so "getting it right" was reframed to **locking the vocabulary and
adopting Matt's structure**. We built a Printing-Press-style agent spine (4 new files), locked the
one real inconsistency (`license → warrant`) without executing the risky rename, committed everything
**locally (not pushed)** with the harness verified green before and after. The thread then moved to
strategy: a "value above the line" framing that **validates xOP as defensible**, a conclusion that
the real distribution surface is a **skill (like Lyra), not a CLI**, and Cowork as the **adoption
surface, not a place to relocate the repo**. It ended here — with this brief.

---

## 2. Decisions Made

1. **Scope = restructure + lock vocab + commit-ready local.** Not a formula fix.
   *Why:* the math was already consistent across spec/protocol; the real gap was the `license/warrant`
   word drift. *Rejected:* a formula-only audit (nothing to fix), a blind global rename (see §4).

2. **`license → warrant` is LOCKED as the canonical concept word — but the mechanical rename is NOT
   executed.** Recorded authoritatively in `CONCEPTS.md` §2a.
   *Why:* it's cross-cutting (~50 files incl. harness code + gold JSON), and the repo's own
   Constitution says load-bearing changes are deliberate, not silent. The OSS `license:` header field
   and shipped example dir-slugs (`refusal_license/`, `writing_license/`) are **out of scope**.
   *Until run, treat the two words as aliases.*

3. **Excluded `v1.1/` (stale full-repo snapshot) and `gem_gpt_test/` (scratch) from git** — kept on
   disk, gitignored. *Why:* baking a stale duplicate into a standard's first commit fights the repo's
   "clean public spine" ethos. Fully reversible (`git add` them to undo).

4. **git init, branch `main`, one commit (`4e8cd9e`), NO push, no remote.** *Why:* Morgan said "prep
   everything first" — reviewable locally before anything goes public.

5. **Built the Printing-Press-style agent spine** (4 new files; see §6).

6. **xOP-as-skill is the real distribution move — model it on Lyra, not Printing Press.**
   *Why:* Printing Press / MagicPath skills drive a **binary** that does deterministic work; xOP's core
   is a **judgment the model performs** (no binary). That's the Lyra shape. Morgan already ships Lyra as
   a Claude Code plugin in the **`lyra-labs`** marketplace — xOP is the next sibling. The existing
   `tools/xop_runner.md` + `tools/xop_builder.md` are ~80% of the skill bodies already.
   *Constraint:* the skill MUST carry the honest-status discipline (surface, don't certify; abstain is
   valid; judge unbuilt) — a one-command "INHERITED ✓" would over-claim, the exact failure the repo warns of.

7. **No factory.ai-style `curl | sh` CLI for the core** — it would be install-theater (installing a
   markdown runner dressed as a heavyweight tool). *Narrow yes:* a clean dev install for the **harness**
   (`pip install` / `curl|sh`) is legitimate — that's the "trust one, developer" door. A thin `xop`
   CLI is optional Phase-2 polish, the **last** thing to build.

8. **Cowork = the adoption/use surface, not where the source relocates.** *Why:* Cowork is a working
   surface, not a repo host — the standard stays in git either way. Split by layer: the
   **standard + harness** stay in Claude Code (dev tooling); the **use + adoption layer** (the
   `/xop-run`, `/xop-build` skills, COP coaching, non-technical collaborators) is Cowork's sweet spot.
   Don't "move" — **ship the skill, and Cowork becomes one place it lands.**

9. **The "above the line" strategy validates xOP.** Post-Google-release, model access / generic agents
   / prompt-to-app are commodity. Value survives above the line — and xOP maps to **all five** cards:
   *a point of view* (the hold thesis), *trust* (the gate, no-self-grading), *proprietary context*
   (gold sets, failure docs, the judge), *industry-specific workflows* (COP/WOP/Refusal), *owned
   distribution* (awaken.fyi + lyra-labs + the skill). **Four are in hand; the gap is owned distribution.**

---

## 3. Decisions Still Open

| # | Open question | Lean | What resolves it |
|---|---|---|---|
| O1 | Run the `license → warrant` migration now, or defer? | Lean: run it behind a verify gate | A harness-verified before/after showing identical PASS |
| O2 | `site/` placement — keep in the xop repo or move to `awakenfyi/awaken-site`? | Lean: move to awaken-site | Morgan's call on repo boundaries |
| O3 | Create `awakenfyi/xop` — public, or private-first? | Not yet done (prep-only) | Morgan greenlight to publish |
| O4 | Build `verify.sh` (the 6-gate pre-publish check)? | Lean: yes, build first | Offered, not yet built |
| O5 | Scaffold the `xop` skill into `lyra-labs`? | Lean: yes — it's the distribution | Offered, not yet built |
| O6 | A thin `xop` CLI? | Lean: later/optional | Only after the skill ships |

---

## 4. Things Tried and Rejected *(do not re-litigate without new info)*

- **Blind global `license → warrant` sed rename.** Rejected: would break example dir-slugs
  (`refusal_license/`), collide with the OSS `license:` field, and risk corrupting the harness gold
  JSON. Salvage: do it as a *token-scoped, harness-verified* migration instead (§3 O1).
- **A formula-only audit.** Rejected: the formulas were already consistent — nothing to fix.
- **Committing `v1.1/` and `gem_gpt_test/`.** Rejected: stale snapshot + scratch; cuts against the
  clean public spine. Kept on disk, gitignored.
- **A `curl -fsSL …/xop | sh` installer for the xOP core.** Rejected: install-theater; mismatches
  xOP's nature (portable judgment, not a binary). Salvage: legitimate only for the **harness** dev door.
- **"Move the whole project to Cowork."** Rejected/reframed: you don't relocate a git repo into Cowork.
  The move is "ship the skill; Cowork is a landing surface."

---

## 5. Working Commands & Instructions (copy-paste ready)

**Run / verify the harness** (Python is `python3` here; `gold.json` is a derived artifact, gitignored):
```bash
cd harness
python3 run_harness.py          # gate + floor + per-class confusion, NO pooled score
python3 run_harness.py --trace  # per-case  gold -> call  (X marks a gate violation)
python3 test_harness.py         # harness invariants — expect "all invariants hold."
```
Expected baseline (13-case **scaffold**, not a benchmark): `always_abstain` **passes the gate, fails
the floor**; `lexical_floor` **violates the gate**. Both reading "FAIL" is the *intended teaching
outcome*, not a bug.

**Rebuild the gold scaffold from scratch:**
```bash
cd harness/phase1
python3 generate_candidates.py
python3 label_cli.py --labeler alice --from demo_a.txt
python3 label_cli.py --labeler bob   --from demo_b.txt
python3 reconcile.py labels_alice.json labels_bob.json   # -> gold.json (blind:false)
```

**The verification discipline (applies to prose AND code — the standing instruction):**
> Bind every claim to a ground truth that isn't your own say-so (no self-grading); watch the residual
> `L = x − x̂` — did you do what you claimed? **Before building:** read the actual source not your
> memory of it; establish the baseline; size the risk don't assume it. **After building:** re-run the
> same check (residual = 0); verify every pointer (file/command/section actually exists and says what
> you claimed). A wrong section number or a cited-but-missing file is as false as a failing test — just
> harder to notice. "Receipts, not vibes" applies to copy as much as code.

**The 6-gate pre-publish check (design for `verify.sh` — not yet built):**
1. Harness gate — `run_harness.py` gate clean, floor reported, no pooled score.
2. Invariants — `test_harness.py` all hold.
3. Reproducible gold — rebuild `gold.json` from the `phase1/` pipeline.
4. Reference integrity — every internal file/section link resolves (this caught a missing
   `tools/builder_failures.md`).
5. Locked-vocab lint — grep for retired terms (`license`-as-concept, "pass/fail" for states,
   "framework" for the family, any "judge is built") against `CONCEPTS.md`.
6. Fresh-clone dogfood — clone to a temp dir, follow the README quickstart as a cold reader, confirm it runs.

---

## 6. References & Source Material

**Created this thread:** `AGENTS.md` (agent operating guide), `CONCEPTS.md` (locked vocabulary +
`license→warrant` ruling §2a), `SCORECARD.md` (two-tier "is this a real xOP?" + proof-of-behavior
gates), `PIPELINE.md` (idea→Source→Portable→gold→validate→publish), this `COWORK_BRIEF.md`.
**Edited:** `README.md` (repo map), `REPO_STATE.md` (honesty manifest), `.gitignore` (exclude v1.1/, gem_gpt_test/).

**Templates / strategy referenced:**
- `github.com/mvanhorn/cli-printing-press` — the structural template (AGENTS/scorecard/phase pipeline; but it's a *binary generator* — copy its packaging, not its CLI shape).
- `github.com/magicpathai/agent-skills` — example of the `npx skills add` / SKILL.md mechanism.
- factory.ai `curl -fsSL …/cli | sh` — the pipe-to-shell install pattern (rejected for xOP core).
- The "above the line / commodity — now free" strategy image (post-Google-release value framing).

**Existing awakenfyi GitHub org** (Morgan is `awakenfyi` on `gh`): `lyra`, `lyra-protocol`,
`lyra-verb` ("L = x − x̂"), `lyra-marketplace`, `auto-awakening`, `awaken-site`. **No `xop` repo yet** —
the content map names `github.com/awakenfyi/xop` as its intended home.

**Internal source (already in repo):** `SPECIFICATION.md`, `CONSTITUTION.md`, `GOVERNANCE.md`,
`PLAN.md`, `USAGE.md`, `site/awaken_content_map.md`, `archive/AWAKEN_Flagship_The_Wrong_Pass_Rate.md`
(the "Wrong Pass Rate" essay = the NOI), `archive/LYRA_POSITIONING.md`, `examples/refusal_license/`
(flagship), `harness/`.

---

## 7. Current State

**Where it ended:** local git repo, branch `main`, one commit `4e8cd9e`, **100 files staged, nothing
pushed, no remote configured.** Harness green-as-designed. `v1.1/` + `gem_gpt_test/` on disk but
gitignored. `license→warrant` locked in `CONCEPTS.md` §2a, **not yet executed**. The warrant judge
remains the one named, unbuilt hole.

**Ready to use right now:** the standard (`SPECIFICATION.md`), the harness, the four new spine files,
the reference xOP (`examples/refusal_license/`), the paste-into-a-thread runner/builder (`tools/`).

**Start-here for a cold pickup:** read `AGENTS.md` → `CONCEPTS.md` → this brief. Then `README.md` for
the human on-ramp. Run `cd harness && python3 run_harness.py` to see the gate in action.

**Next steps, in order (Morgan's call to greenlight):**
1. Build `verify.sh` (the 6 gates above) — de-risks everything after it.
2. Run the `license→warrant` migration behind that gate.
3. Scaffold the `xop` skill into the `lyra-labs` marketplace (the real distribution; the
   above-the-line gap).
4. Decide `site/` placement (→ `awaken-site`?).
5. Create `awakenfyi/xop` and push.
6. (Optional, last) a thin `xop` CLI.

**Blocking nothing** technically — every next step is a greenlight decision, not a dependency.

---

*One question (is it still warranted?), three values (warranted · inherited · undecidable), two metrics
that can't move (the gate, the floor), one residual (`L = x − x̂`). The model is the cheap part; the
standard, the trust, and the distribution are the expensive parts — and they're above the line.*
