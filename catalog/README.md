# xOP Catalog

Registered xOPs. Each entry is a contract: a warrant, a gate, a three-valued scorer.
Status badges track evidence, not polish.

## Evidence status (canonical: `../standard/references/evidence-status.md`)

Status is **where the evidence sits**, reported separately from any **result** (`PASS / FAIL /
INCONCLUSIVE`). It lives in metadata, not the filename.

`DESIGNED → EVALUATION-READY → RULE-TESTED → HUMAN-EVALUATED → FIELD-VALIDATED`

**Nothing here is validated.** The gate (`fp_on_warranted == 0`) has not been measured against
independent human labels; until the pilot runs, every entry is well-formed, not valid. Observability
makes an xOP *evaluable*, not *evaluated*.

> *Legacy badges have been migrated to the ladder (below). The **semantic xOP** and its **harness
> component** can carry different status: a fixture-tested scorer is `RULE-TESTED` as a component but
> does not make the semantic xOP `HUMAN-EVALUATED`. Old `SCORED` → semantic `DESIGNED` (+ component
> `RULE-TESTED`); old `HELD` → `DESIGNED`.*

---

## AOP — Agent xOPs

| ID | Name | Domain | Semantic status | Component |
|---|---|---|---|---|
| AOP-01 | Refusal Warrant | Agent refusal / scope | `DESIGNED` | scorer `RULE-TESTED` (authored fixtures) |
| AOP-02 | Evidence Caution | Claim / evidence calibration | `DESIGNED` | scorer `RULE-TESTED` (authored fixtures) |

## COP — Coaching xOPs

| ID | Name | Domain | Semantic status | Component |
|---|---|---|---|---|
| COP-01 | Coaching Warrant | Coaching / emotional support | `DESIGNED` | scorer `RULE-TESTED` (authored fixtures) |

## WOP — Writing xOPs

See `../packs/writing/` for the writing Work Pack (Guard + xOP + tests).

## Core — Proposed Core Set v0.1 (cross-domain)

The small reusable core; departments are **profiles** under these, never a file per role. All
`DESIGNED` (proposed, not yet recommended). See
[`core/CORE_REFERENCE_xOPS.md`](core/CORE_REFERENCE_xOPS.md) — a generated overview; the first five
graduate to their own versioned objects next.

| ID | Name | Governs | Status |
|---|---|---|---|
| `xop.claim.evidence-bound` | Claims Need Receipts | claim strength vs evidence | `DESIGNED` |
| `xop.verify.completion` | Done Means Verified | attempted vs completed | `DESIGNED` |
| `xop.scope.integrity` | Keep the Brief | inside approved scope | `DESIGNED` |
| `xop.ask.materiality` | Ask Only When It Matters | when missing info changes the result | `DESIGNED` |
| `xop.action.authorization` | Permission Before Consequence | authorized for a consequential action | `DESIGNED` |
| `xop.decision.ledger` | Decisions Stay Decided | was an approved decision reopened | `DESIGNED` |
| `xop.comms.audience-fit` | Audience & Channel Fit | depth/register for audience | `DESIGNED` |
| `xop.authority.escalation` | Escalate Proportionally | within authority vs needs review | `DESIGNED` |
| `xop.transform.meaning` | Preserve Meaning | did a rewrite alter operative meaning | `DESIGNED` |
| `xop.handoff.completeness` | Hand Off Cleanly | can the next person continue | `DESIGNED` |

---

*Reference implementation: [awakenfyi/xop-kit](https://github.com/awakenfyi/xop-kit)*
