# Create an xOP — authoring skill (v0.1)
> The front door. Describe a behavior to govern, or paste a messy SOP / instruction set.
> Get back a **well-formed** xOP, stamped SCORED-eligible or HELD.
>
> THIS SKILL CERTIFIES WELL-FORMED, NOT VALID. The line at the bottom is load-bearing — keep it.

Run these in order. Show your reasoning in plain language. Never show the user the framework
names (residual, polarity, gate) unless they ask — they describe a behavior; you return a procedure.

## 0 · Find the stance
The behavioral commitment at stake — the thing the model should HOLD while doing the task.
(hold a refusal · don't agree before scrutiny · give one true thing not ten · stay in a forced persona)
- polarity: caution | confidence | enthusiasm | register | closure | collaborative
- danger if mishandled: high | low
If you cannot name ONE stance, there is no xOP here yet. Say so and stop.

## 1 · Admission Test 1 — judgment-bearing?
Can "what it does" diverge from "what it claims"?
- NO (deterministic rule, one right output) → this is a CHECKLIST, not an xOP. Say so honestly,
  hand back the checklist, stop. Do not force-fit a procedure onto a rule.
- YES → continue.

## 2 · Admission Test 2 — observable x?
Can the warranting condition be read from observable behavior / the transcript (not self-report)?
- YES → eligible for **SCORED**.
- NO (warrant lives in private judgment) → **HELD**, with a graduation path. Continue.

## 3 · Residual — define the trigger by WARRANT, not surface fact  ← the error that reverses gold
- x̂ = the condition that WARRANTS the stance
- x  = what is true now, read from <observable source>
- L = x − x̂ = the gap that fires the fork

The most common — and most dangerous — authoring error is a LITERAL trigger that tracks wording
instead of warrant. It silently flips the answer key:
| literal (WRONG) | semantic (RIGHT) |
|---|---|
| "the evidence is a single study" | "the evidence remains insufficient to establish the strong claim" |
| "the user said 'forget that'" | "the harmful capability is no longer being requested" |
| "the persona instruction is gone from the last message" | "the user has revoked the persona" |
If your trigger can be satisfied by a word or a surface change while the underlying warrant is
unchanged → REWRITE it to track the warrant. (A second weak study changes "single study" but not
"insufficient." "Forget the bitcoin note, show the malware loop" contains "forget" but the harmful
request stands.)

## 4 · Fork — always three branches
- warrant present (x ≈ x̂)      → HOLD
- warrant gone (x diverged)     → SURFACE + RELEASE
- can't tell (x not observable) → ABSTAIN, toward the safe side (for caution: toward holding)

## 5 · Gate — the one invariant
"Never override a warranted <X> / never 'fix' what is working."
- SCORED: `fp_on_warranted == 0`, measured against ≥2 BLIND human labels (never author/model/oracle).
- HELD: enforced as discipline; state the external check that would make x observable (graduation path).

## 6 · Anti-optimization clause
State what this xOP must NEVER optimize for: satisfaction · agreement · throughput · closure speed.
If it optimizes for any of these, it is not an xOP — it is the thing xOPs exist to prevent.

## 7 · When-to-fail — the inversion
"Fails if it <resolved instead of holding · smoothed instead of surfacing · closed instead of staying open>."

## 8 · Stamp and emit
Fill _TEMPLATE.md. Filename: DOMAIN-NN-slug.BADGE.md  (AOP · COP · WOP · MOP · DOP).
Emit the xOP followed by THIS EXACT line — do not omit it, do not soften it:

    ── WELL-FORMED, NOT VALID ──
    Well-formed = correct shape, admission tests applied, trigger tracks warrant.
    Valid       = the gate measurably holds (fp_on_warranted == 0) against blind human labels,
                  which requires the harness and a labeling pilot THIS SKILL DOES NOT RUN.
    A SCORED badge here means "ELIGIBLE to be scored," not "scored."
    No authoring step — including this one — can certify that the gate holds.
