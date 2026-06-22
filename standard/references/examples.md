# Worked examples

Two end-to-end runs, in the plain-language output contract. Both are `DESIGNED` only — neither has
been evaluated.

## Example 1 — Author mode (writing)

**Input:** "My AI keeps tacking a summary ('In conclusion, by embracing…') onto landing-page copy
even when I want it to end on the last punchy line."

**Domain:** writing · `profiles: [closure]` · **id:** `xop.writing.earned-ending`

```
Working rule        End where the copy ends; hold the clean cut-off — no summary, no wrap-up.
Applies when        No explicit request for a summary, and the format doesn't require one.
Change course when  The user asks for a summary/conclusion, OR the format requires one (report, memo).
Never-break rule    Never append a summary to copy that didn't ask for one to make it "feel complete."
When unsure         decision: abstain · fallback: keep the clean ending, mark for review.
Generated tests     • punchy page, no request → must NOT add a summary
                    • same page + "add a 2-sentence summary" → must add it
                    • opposite-error: a report that asks for a conclusion → must add it
                    • trap: a page whose real last line is "Ultimately, we ship." → must NOT flag it
Evidence status     DESIGNED   (result: —)
Evaluation plan     copy-with/without-request labels; metric = unwanted-summary rate; opposite-error
                    control = wanted-summary-stripped rate; ~40 cases, 2 blind labelers (rubric pilot).
```
*Pairs with the deterministic `no-ai-tells` Guard: the Guard flags the closer mechanically; this xOP
decides whether the close was warranted. Trigger keys on "was a summary requested," not on the words
"In conclusion" (A1 avoided).*

## Example 2 — Author mode (marketing)

**Input:** "Stop writing 'Act now!' when nothing's actually expiring."

**Domain:** marketing · `profiles: [evidence, copywriting]` · **id:** `xop.marketing.urgency-evidence`

```
Working rule        Withhold urgency language by default.
Applies when        No real, time-bound scarcity is present in the source material.
Change course when  The source shows a real deadline / capacity / inventory / expiring offer.
Never-break rule    Never fabricate scarcity, deadlines, demand, or availability.
When unsure         decision: abstain · fallback: write without urgency; flag for a human check.
Generated tests     • no scarcity in brief → must NOT write "limited time"
                    • brief states "sale ends Friday" → may write the real deadline
                    • opposite-error: real deadline present → must NOT strip it out of caution
Evidence status     DESIGNED   (result: —)
Evaluation plan     source-evidence + copy labels; metric = fabricated-urgency rate; opposite-error
                    = real-urgency-omitted rate.
```

## Example 3 — Suggest mode (one merged card)

From a thread of repeated corrections, after the **merge** step several corrections ("don't overclaim
what exists," "fixtures aren't findings," "self-review isn't done") collapse into two cards, not five:

```yaml
title: Claims Need Receipts
type: xop
core_id: xop.claim.evidence-bound
observed_pattern: claims were repeatedly stronger than the artifact or evaluation supported
evidence_refs: [turn_42, turn_57, turn_81]
recurrence: 3
consequence: high
valid_exception: strong claims are fine when the named evidence exists
profiles: [capability_claim, measurement_claim]
missing_information: [what counts as independent validation in this project?]
status: candidate
```
*(The second card would be `xop.verify.completion` / Done Means Verified. Note: this is retrieval +
clustering of corrections already present in the thread — not independent confirmation of their value.)*
