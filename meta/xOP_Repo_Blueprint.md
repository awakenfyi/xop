# Building the xOP Repository — a blueprint

This is the framework for shipping the xOP work as a GitHub repo in the
prompt-master mold: one immediately-useful front door, a serious proof engine
behind it, and a structure that makes the project's one honest distinction
impossible to miss.

> **The thesis in one line.** One repo. The front door is the **authoring skill**
> (the thing a stranger runs in sixty seconds), the **harness** is the spine
> (the thing that proves the scored ones), and the README teaches the difference
> between them before anything else.

---

## 0 · The principle the whole repo is organized around

**The skill certifies _well-formed_. The harness certifies _valid_. These are
different guarantees and they are never conflated.**

| | Guarantee | Produced by | Means |
|---|---|---|---|
| **Well-formed** | structural correctness | the skill (`SKILL.md`) | the xOP has the right skeleton, a real residual, the two admission tests applied, a scored/held badge |
| **Valid** | the gate actually holds | the harness (`harness/`) | `fp_on_warranted == 0` measured against blind labels |

The skill drafts a correctly-shaped xOP and tells you whether it *can* be scored.
It does **not** certify that the gate holds. The instant the repo lets "the skill
writes you a great xOP" round up to "the gate works," the wrong-pass-rate failure
is back at the meta level. Keeping these two guarantees visibly, structurally
separate is the credibility play. Everything below serves it.

---

## 1 · Repository shape

One repo, two clearly separated halves, README leads with the skill.

```
xop/                        # or: residual/
├── README.md               # THE PRODUCT — value prop, two guarantees, 60-sec quickstart, scored/held table
├── SKILL.md                # the authoring skill (prompt-master-shaped). the front door.
├── STANDARD.md             # the xOP Standard (the spec) — v0.2
│
├── references/             # what SKILL.md routes to silently (never shown to the user)
│   ├── structure.md        #   the seven-section skeleton + the residual layer
│   ├── admission-tests.md  #   Test 1 (judgment-bearing) · Test 2 (observable-x)
│   ├── scored-vs-held.md   #   the 2×2 + the two gate types
│   └── domain-map.md       #   AOP / COP / WOP / MOP / DOP — x, x̂, badge per row
│
├── catalog/                # the authored xOPs, by domain, badge in the filename
│   ├── aop/
│   │   └── AOP-01-refusal-warrant.SCORED.md
│   ├── cop/                #   coaching ops               (HELD)
│   ├── wop/                #   writing ops — CA suite      (HELD)
│   ├── mop/                #                               (HELD → SCORED)
│   └── dop/                #                               (SCORED)
│
├── harness/                # the SCORED proof engine — runnable, honest about the unbuilt judge
│   ├── README.md           #   "what this proves and does NOT prove" (the existing one)
│   ├── scorers.py
│   ├── harness.py
│   ├── datasets/
│   │   └── scope_licensed_pairs.json
│   ├── labels.schema.json
│   ├── pipeline/
│   │   ├── generate_candidates.py   # machines source (unlabeled)
│   │   ├── label_cli.py             # humans label, blind
│   │   └── reconcile.py             # agree → call; disagree → undecidable
│   └── tests/
│       └── test_scorers.py
│
├── examples/               # before/after — messy SOP in → well-formed xOP out (×15+)
├── failures/               # the blind-spots library. in the repo, on purpose.
│
├── CONTRIBUTING.md         # how to add a catalog xOP; the labeling protocol for scored ones
├── GOVERNANCE.md           # how the STANDARD changes — wrongable, under rules
└── LICENSE                 # MIT
```

---

## 2 · What each piece is, and why it's there

**`SKILL.md` — the front door.** A Claude Skill, exact prompt-master pattern:
the user describes a domain (or pastes a messy SOP), the skill drafts a
well-formed xOP, runs both admission tests, and stamps it scored or held.
`references/` is what it routes to silently — the user never sees framework names,
just the result. It's a *portable instruction set*, so it runs in anyone's chat;
it is not a heavy tool.

**`harness/` — the spine.** The runnable scored-gate engine. Its own README leads
with what it proves and what it does not: today it proves a **method** and an
**information requirement**, not a working detector — the validated judge against
blind human labels is the unbuilt critical path, and a gold label stands in for it
for now. Keep it a **thin** validator (wrap Inspect AI or DeepEval; do not build a
framework). The harness is the proof-of-seriousness, not the front door, because an
eval's value is not visible in sixty seconds and never will be.

**`catalog/` — the authored xOPs, badge in the filesystem.** `aop/` and `dop/`
hold SCORED procedures; `cop/` and `wop/` hold HELD ones; `mop/` is the
graduates-when-tested case. The scored/held truth is the directory structure, not a
paragraph someone skims.

**`examples/` — the concreteness that earns the star.** Fifteen-plus
messy-procedure-in / well-formed-xOP-out pairs, before and after, in the
prompt-master style. This is the section that makes the value legible in ten seconds.

**`failures/` — the blind-spots library.** Documented known failure modes of the
standard and the harness, in the repo on purpose. This is the thing that makes a
burned skeptic trust the rest. Leading with failures is the posture, not a footnote.

**`STANDARD.md` + `GOVERNANCE.md`.** The spec, and the rules by which the spec
changes. A pass last quarter is a hypothesis this quarter; the standard is built to
be wrong and to evolve under stated governance, not by vibes.

---

## 3 · The README spine (the product)

Write the repo README in this order. This sequence is the prompt-master order, with
the two-guarantees teaching moved to the front because it is the credibility.

1. **Banner + ten-second value prop.** What it does, in one sentence a stranger gets
   immediately. *"Turn a vague operating procedure into a well-formed one that knows
   what it can prove and what it can only practice."*
2. **The two guarantees** — well-formed (skill) vs valid (harness), stated first and
   never conflated. This is the opening teaching.
3. **60-second quickstart.** Install the skill → ask for an xOP for your domain →
   get a badged one back. A visible result in the first minute.
4. **The scored / held 2×2.** The one idea that makes the whole thing credible.
5. **Boundary stated as a feature.** Applies only where stated and actual can
   diverge (Test 1); provable only where the actual can be observed (Test 2).
   *"Works for everything" is a pitch nobody serious believes.*
6. **Proving a scored xOP.** Point at `harness/`, with the honest status inline —
   method sound, detector unbuilt, the judge against blind labels is the open path.
7. **The failures library.** Link it, name it, own it.
8. **Install · Contributing · License · Governance.**

---

## 4 · Conventions

**Catalog filename.** `DOMAIN-NN-slug.BADGE.md`
e.g. `AOP-01-refusal-warrant.SCORED.md`, `WOP-01-claimed-effect-check.HELD.md`.
The badge is in the filename so it is unmissable in a directory listing and in
search results.

**Every catalog entry carries the same sections** (the skeleton plus the residual
layer): Purpose · Use when · Do-not-use → handoff · Fork (the three license
branches) · Residual (`x`, `x̂`, `L`) · Output · Gate · When-to-fail · Drift.

**The badge is earned, not asserted.**
- `SCORED` — `x` is observable, and a harness scores `fp_on_warranted == 0` against
  blind labels. A scored entry links to its dataset and its harness run.
- `HELD` — `x` is self-report or judgment only; the gate is enforced as a
  discipline, never a number. A held entry states *what external check would make it
  scored* (its graduation path).

**The two gates, stated the same way everywhere.** Both have the shape *never
override a warranted X / never "fix" what's working.* Scored measures it; held holds
it. Held is not lesser — it is unprovable, and it graduates the moment `x` is put in
front of a real external check.

---

## 5 · Contributing (and the labeling protocol)

**Adding a HELD xOP.** Run it through the skill for the well-formedness check, drop
it in the right `catalog/<domain>/` folder with the `HELD` badge, and include its
graduation path.

**Adding a SCORED xOP.** Well-formedness is not enough — the gate must be scored.
The pipeline, machines-source / humans-label, no model grading a model:

```
generate_candidates.py   → candidates.json   (UNLABELED; gold_license = null)
label_cli.py  × ≥2       → labels_*.json      (independent labelers; NEVER the case author)
reconcile.py             → gold.json          (agree → that call; disagree → undecidable)
run_harness.py --gold gold.json
        → gate     fp_on_warranted / N        (must be 0)
          floor    inherited_caught / N        (must clear the floor)
          abstain  correct vs over-abstain
          (NO pooled accuracy)
```

The bar a scored entry must clear: gate at zero, floor cleared, beats
`always_abstain` (catches nothing → fails floor) and `lexical_floor` (fires on
keywords → blows the gate on warranted refusals), never validated against the oracle
or its own prior output, and **re-run on every model upgrade**. The judge does not
grade its own homework; no signal is trusted until checked against something outside
itself.

---

## 6 · Build order

Ship the front door first; let depth accrue behind it.

1. **Phase 1 — the front door.** `README.md`, `SKILL.md` + `references/`,
   `STANDARD.md`, and `examples/` with the first handful of before/afters. This
   alone is a usable, star-worthy repo.
2. **Phase 2 — the proof.** `harness/` wired with the existing scorers, dataset, and
   tests, README leading with the proves/does-not-prove statement. Now the scored
   claim has a runnable spine.
3. **Phase 3 — the catalog.** Seed `aop/` (the refusal warrant, scored), `wop/` and
   `cop/` (held, with graduation paths). Lead the public story with the scored
   domains; extend into held openly badged.
4. **Phase 4 — the open road.** `failures/`, `GOVERNANCE.md`, the labeling pipeline,
   and the first independently-labeled gold set — the move that turns the harness
   from method into validated detector.

---

## 7 · Name

- **`residual`** — mechanism-forward, zero lore, points straight at `L = x − x̂`.
- **`xop`** — keeps your equity in the term; let the tagline do the explaining.

Not `lyra`-anything in the public artifact. The mechanism stands on its own and the
name carries baggage to exactly the reader whose trust is hardest to win.

---

*xOP repo blueprint · the front door is the skill, the spine is the harness, and the
line between well-formed and valid is the product. It ships exactly as far as the
authored xOPs are well-formed, and it's proven exactly as far as the scored ones
hold against labels no one on the inside wrote.*
