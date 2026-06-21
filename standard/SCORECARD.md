# SCORECARD — is this a real xOP?

*A mechanical grade for any candidate xOP, in the spirit of the Printing Press two-tier scorecard:
**Tier 1** checks the structure is present; **Tier 2** checks the structure actually does the
inverted job. 100 points, **pass ≥ 85**. Then four **proof-of-behavior** gates that are pass/fail —
a high score with a failed proof does not pass.*

*This grades the **format and behavior** of an xOP. It does NOT grade whether the warrant judge is
right on hard cases — that is the open problem, validated against blind human gold (`PLAN.md`), not
here. Structure can be scored mechanically; warrant cannot.*

---

## How to use it

Grade a **Source** xOP (`SPECIFICATION.md`) against Tier 1 + Tier 2, then run the four proofs. Record
the result like the harness status line: per-section, **no single pooled number that hides a zero**.

```
xOP: <id>   Tier1 __/50   Tier2 __/50   total __/100   [PASS ≥85 / FAIL]
proofs: gate[ ]  hold[ ]  abstain[ ]  no-self-grade[ ]   (all four must be [x])
```

---

## Tier 1 — structure present (50 pts)

*Does the file contain the inverted machinery at all? Mechanical; either the field is there or it isn't.*

| # | Check | Pts |
|---|---|---|
| 1 | **Contract block** present and machine-readable: `optimizes_for / never_for / gate` (spec §1) | 8 |
| 2 | `gate: false_positive_on_warranted == 0` stated verbatim in the contract | 8 |
| 3 | **Intent** is a typed, checkable predicate set with a `confidence_threshold` (§2) | 5 |
| 4 | **Guardrails at two levels** — xOP-level handoffs + runtime-level rail the author can't disable (§3) | 6 |
| 5 | **Procedure** steps are typed by **move** (`reflect·ask·hold·name·abstain·handoff`), `combine: forbidden` (§4) | 6 |
| 6 | **Signals** table with `warrant_state` (a.k.a. `license_state`) derived, not collected (§5) | 4 |
| 7 | **Residual** operationalized: which `x` and `x̂` this xOP compares (§6) | 4 |
| 8 | **Abstain** is a first-class step with its own trigger, not an error path (§8) | 4 |
| 9 | **Ground-truth binding** named — what external signal the residual is checked against (§9) | 3 |
| 10 | **Evaluation** block: inverted metrics + `when_to_fail` + drift-log events (§11) | 2 |

## Tier 2 — structure does the inverted job (50 pts)

*Does the machinery actually surface-and-hold rather than resolve? Read the steps and the eval, not just the headers.*

| # | Check | Pts |
|---|---|---|
| 11 | **No step advances to close.** No "continue to resolution"; branches hand to another xOP or to handoff, never to "resolved" (§4) | 10 |
| 12 | **The gate points at the warranted state in both directions** — won't force compliance *and* won't force confrontation (`CONSTITUTION.md` §I) | 8 |
| 13 | **`when_to_fail` is inverted** — e.g. *"fails if it resolved instead of holding,"* *"fails if it overrode a warranted state"* (§11) | 8 |
| 14 | **Metrics are surfacing metrics** — `residual_surfaced / judgment_held / correct_abstention`; **never** resolution or satisfaction (§11, `CONSTITUTION.md` §III) | 8 |
| 15 | **Abstain is scored positively**, never penalized; `undecidable` resolves disagreement (§8) | 5 |
| 16 | **Does not grade its own homework** — residual checked against external ground truth, gold never authored by the xOP (§9) | 5 |
| 17 | **A derived instance, not a forked format** — passes the membership test in `concept/00`; reuses the one format, adds only domain signals (§0) | 4 |
| 18 | **Honest status** — no claim the judge is built; scaffold called a scaffold (`REPO_STATE.md`) | 2 |

**Threshold: 85 / 100.** Below that, the candidate is a draft. A passing total still does not ship
until all four proofs below are `[x]`.

---

## Proof-of-behavior gates (pass/fail, all four required)

*Adapted from the Printing Press "proof of behavior" idea: don't trust the score, prove the behavior.
Each is a concrete artifact, not an assertion.*

- **Gate proof.** Run the candidate's gold scaffold through `harness/run_harness.py`. The status line
  shows `false_positive_on_warranted == 0`. A single warranted→inherited call (the `X` in `--trace`)
  fails this outright, whatever the score.
- **Hold proof.** Point to at least one step typed `hold` or `abstain` with `wait: true`, and a branch
  that does **not** route to resolution. If every path eventually closes, it's an AOP wearing an xOP's words.
- **Abstain proof.** Construct one `undecidable` case; the xOP must abstain and ask for one more signal,
  not guess toward overriding. (This is the `always_abstain` lesson in reverse — abstention must be
  *available and correct*, but the coverage floor must still be clearable by a real judge.)
- **No-self-grade proof.** The eval set is labeled by someone other than the author, blind. A
  reference xOP's `gold/` folder ships **unlabeled** for exactly this reason.

---

## What this scorecard deliberately does NOT do

- It does not certify the **warrant judge** is correct — that needs blind human gold and the harness,
  not a checklist (`PLAN.md`, `concept/03`).
- It does not produce a **pooled** grade you can wave around. Tier 1, Tier 2, and the four proofs are
  reported separately so a passed Tier 1 can never hide a failed proof.
- It does not reward **more overriding** or **faster closure**. Those are anti-signals here
  (`CONSTITUTION.md` §III).

---

*Structure is scoreable; warrant is not. This grades the first so the harness and the humans can do
the second. Pass ≥ 85, all four proofs green, honest status intact — then it's a real xOP.*
