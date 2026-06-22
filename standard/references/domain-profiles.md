# Domains, profiles, and the core xOPs

**Stable domains, never new family letters.** A new situation is a *profile under an existing
domain*, not a new acronym. This prevents taxonomy sprawl (WOP/MOP/COP/POP/AOP/DOP/BOP/EOP…). The
user never needs the acronym; internally, stable ids are enough.

## Domains

| Domain | Covers | The question it asks |
|---|---|---|
| writing | editing · voice · format | is this edit warranted, or inherited register? |
| marketing | copy · claims · urgency | is this claim/urgency licensed by the evidence? |
| coaching | advice · reflection | is this reaction still warranted by what's happening now? |
| planning | strategy under constraints | does this plan still respect the live constraints? |
| agent | tools · refusal · scope · action | is this refusal/scope/action still warranted? |
| data | RAG · analysis | is this claim still licensed by the data in hand? |

A candidate carries `domain:` + `profiles: [...]`, e.g. `domain: marketing, profiles: [evidence, copywriting]`.

## The two core, cross-domain xOPs

Most "honesty" corrections collapse into these two. Prefer a **profile under a core xOP** over a new
standalone xOP.

### `xop.claim.evidence-bound` — Claims Need Receipts
A claim must not be stronger than the artifact or evidence supports.
Profiles:
- `capability_claim` — don't state a capability as present until it exists in the artifact
  (e.g. "seven Guards" when one is built).
- `performance_claim` — don't state a number as a finding unless it's measured against independent data.
- `measurement_claim` / **"Fixtures Aren't Findings"** — a fixture pass rate or an authored-sample
  ratio is not production prevalence.
- `evidence_status_claim` — don't report `DESIGNED` work as shipped/validated.

### `xop.verify.completion` — Done Means Verified
Don't represent attempted work as completed work; "done" requires the named completion evidence.
Completion evidence varies by profile:
```
software    → clean-room test result
research    → named sources checked
evaluation  → independent labels or a held-out test
publishing  → artifact exists at the destination
support     → fix observed or confirmed
```

## Other stable ids (as they're authored)
`xop.scope.integrity` (agent · stay inside scope) · `xop.marketing.urgency-evidence` (no made-up
urgency) · `xop.stance.calibration` (refusal/caution persistence). Add ids; don't add letters.
