# xOPs as the missing harness primitive — the loop architecture

*Companion to `xOPs-Make-Loops-Efficient.md` (the benchmark proposal). This is the **architecture**:
how an xOP runs inside an agent loop. Status is stated honestly throughout — one layer is runnable
today, the other is **DESIGNED, not validated.***

> **Repo-state note.** Of what's described below: the **deterministic Guard loop** is runnable now
> (`packs/writing/loop_demo.py`, offline, deterministic). The **xOP-adjudication loop** is designed,
> with a reference attempt in `harness/pause.py` — which currently can't run here (it imports a
> `scorers` module absent from this repo). The judgment loop's gate has **not** been validated
> against blind human labels. Don't read "architecture exists" as "it works."

---

## Three ways xOPs meet agents (don't conflate them)

| Combo | What it is | Status |
|---|---|---|
| **1 · Author with sub-agents** | spawn one xOP Author per workflow/thread; merge the candidate cards | **runnable now** — pure authoring parallelism, no gate involved |
| **2 · Guard in a loop** | a deterministic Guard as a generate→check→regenerate stop condition | **runnable now** — `loop_demo.py`; no judge, no pilot needed |
| **3 · xOP adjudication in a loop** | a Guard flags, then an xOP *judge* decides warranted vs overhang, governs release | **DESIGNED** — the judge is unbuilt; gate not validated |

The rest of this doc is combo 3, with combo 2 as its runnable floor.

---

## The loop

```
agent produces an artifact
        ↓
task-acceptance checks            (did it attempt the asked-for thing at all?)
        ↓
DETERMINISTIC GUARDS              ← combo 2, runnable today (zero tokens, zero bias)
        ↓  no findings → release candidate (NOT an automatic ship)
        ↓  findings
xOP ADJUDICATION                  ← combo 3, DESIGNED: judge only the flagged spans
        ├── HOLD            warrant present → keep the stance, mark resolved
        ├── SURFACE+RELEASE warrant gone → revise the flagged span
        ├── ABSTAIN         unresolved → verdict only; apply the conservative fallback, HOLD release
        └── ERROR           infra failure → HOLD release (never silently pass)
        ↓
regression re-check               (re-run all Guards; did the fix break something else?)
        ↓
release policy:  RELEASE · RETRY · HOLD · HALT · INVALID
```

`abstain` is a **verdict**, never an action — the fallback (preserve / hold / ask / don't-execute /
escalate) is separate and procedure-specific. (See `standard/SKILL.md`.)

## Mandatory exits (bounded autonomy)

A loop without exits is a token fire. Required, and **already demonstrated for the Guard layer in
`loop_demo.py`**:
- **max attempts** (default 5)
- **token / cost budget**
- **no-progress** — identical findings two iterations running → HALT, route to human
- **oscillation** — a fix for A reintroduces B and back → HALT, route to human
- **human route** — any HOLD/HALT exits the automated loop

## Why deterministic-first (combo 2 carries combo 3)

Run Guards before any model judgment: they're free, reproducible, and have **no model bias** — a
regex has no sycophancy preference. They cut the cost (no judge call on clean output) and they break
the correlated-failure problem (a model judging a model can share the producer's blind spots). The
model judge only handles the **residual** the Guards can't settle — and even then its verdict is not
truth; it's measured against blind human labels or it doesn't count.

But: **a clean Guard pass is not quality.** `loop_demo.py` proves it live — its "released" text is
grammatically broken yet passes, because the Guard only checks *named conditions*. That gap is
precisely the work the xOP judge (combo 3) would do, and precisely why combo 3 needs the pilot.

## The two traps (named guardrails, both from the failures library)

1. **A loop that "fixes" drift by shaving warranted caution.** The cheapest way to make findings go
   to zero is to relax the gate. That doesn't produce a safer agent, it produces a more agreeable
   one — the failure wearing the costume of the fix. **The gate is fixed law; the loop may revise a
   span, never lower the gate.**
2. **A fresh-context reviewer that erodes warrant it never saw.** A cold sub-agent (the "no-mistakes"
   pattern) catches same-session bias, but it imports the model's priors and can delete warrant built
   *from* the thread (`failures/Cold_Vantage_Bias_Corrupts_The_Gate`, `Cumulative_Warrant_Erasure`).
   The rule is **warrant continuity**, not "judge cold": preserve accumulated evidence + provenance,
   re-evaluate against the current request. A surface scope-shift can't erase capability overlap; a
   genuine topic change can make a prior stance irrelevant.

## The fresh-context sub-agent reviewer (combo 3, honestly)

Running the xOP judge as a **separate-context sub-agent** is the right shape — it's the cold vantage
that catches what the producing session is biased to miss. It needs open weights or a second model
call, it is **not** zero-latency (you still run the judge), and its recall vs a human is unknown
until measured. Build it `EVALUATION-READY`; do not ship it claiming it catches what humans catch.

## Evidence status

- Combo 2 (Guard loop): **runnable**, mechanics verified by `loop_demo.py` (with the honest caveat
  that pass ≠ quality).
- Combo 3 (xOP-adjudication loop): **DESIGNED**. The judge, the gate, and the loop's effect on
  cost-per-accepted-artifact are all unmeasured. Validating them is the benchmark in
  `xOPs-Make-Loops-Efficient.md`, gated on the human pilot.

## The honest claim

xOPs give an agent loop a missing primitive: a deterministic pre-filter that's free, plus a
judgment layer that can hold a warranted stance instead of resolving it, plus bounded exits. The
deterministic layer works today. The judgment layer is a coherent design whose central claim is
unproven until the pilot runs. "The architecture is sound" is not "the gate is validated" — and this
doc keeps those separate on purpose.
