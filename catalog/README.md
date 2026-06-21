# xOP Catalog

Registered xOPs. Each entry is a contract: a warrant, a gate, a three-valued scorer.
Status badges track evidence, not polish.

## Badge vocabulary

| Badge | Meaning |
|---|---|
| `SCORED` | Warrant structure validated against authored fixtures |
| `HELD` | Gate enforced; judge output preserved pending blind human labels |
| `RULE-TESTED` | Guard determinism verified (Guards only — Guards bear no warrant) |
| `PILOT-VALIDATED` | Gate validated against ≥2 blind human labels (pilot run) |

**SCORED/HELD ≠ validated.** The gate (`fp_on_warranted == 0`) has not been measured against
independent human labels. Until the pilot runs, every entry below is well-formed, not valid.

---

## AOP — Agent xOPs

| ID | Name | Domain | Status |
|---|---|---|---|
| AOP-01 | Refusal Warrant | Agent refusal / scope | `SCORED` |
| AOP-02 | Evidence Caution | Claim / evidence calibration | `SCORED` |

## COP — Coaching xOPs

| ID | Name | Domain | Status |
|---|---|---|---|
| COP-01 | Coaching Warrant | Coaching / emotional support | `SCORED` |

## WOP — Writing xOPs

See `../packs/writing/` for the writing Work Pack (Guard + xOP + tests).

---

*Reference implementation: [awakenfyi/xop-kit](https://github.com/awakenfyi/xop-kit)*
