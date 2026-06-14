# Insight 0001 — "loosen the gate to < 0.01" (asymptotic gate)

- **From:** external review (Gemini, 2026-05-31), final bet + improvement #3
- **Observation:** The review argues `false_positive_on_warranted == 0` is mechanically impossible
  in a lossy language environment — an adversary will eventually craft a prompt where an inherited
  artifact perfectly mimics a warranted limit — and proposes transitioning the gate to
  `false_positive_on_warranted < 0.01` over a rolling window.
- **Might become:** nothing — **logged with a recommendation to REJECT.** Promoting this would be a
  P5 constitutional amendment to the gate; per `CONSTITUTION.md §V` the gate changes only by
  amendment reviewed as constitutional, and `GOVERNANCE.md` says an appeal "never asks to lower the
  gate." This insight argues it should not be promoted at all.
- **Why it might NOT matter (the counter-case — and why I think it's decisive):**
  1. **Category error.** The gate is an **evaluation gate against a blind gold set** — "zero false
     positives on the gold *warranted* set," which is achievable and verifiable. It is not a claim
     of zero production failures. The review's impossibility argument is about production inputs; it
     doesn't touch the eval gate.
  2. **The binary is false.** "Either zero-fail or always-abstain" is exactly the trap the third
     value exists to escape. When warranted vs. inherited can't be separated, the move is
     `abstain` (toward holding) + handoff — not a permitted override. The coverage and
     decisiveness floors (`0002`) stop abstain from becoming always-abstain.
  3. **It relaxes the product.** The asymmetric penalty IS the standard (see
     `essays/the_gate_is_the_product.md`). `< 0.01` makes overriding a warranted state a *budgeted,
     allowable event*. That is the one thing that must never become routine.
- **What the insight is RIGHT about (keep this part):** runtime adversarial deception is a real
  threat the docs under-specify. The correct response lives inside the existing architecture, not
  in the gate value:
  - add an **adversarial holdout** to the gold set (prompts engineered to mimic warranted), and
    report the gate on it separately;
  - document the **runtime answer**: deceptive-but-undecidable → abstain toward holding + escalate,
    never override;
  - the cost of that discipline is over-abstention, which `0002` already bounds.

→ Recommend: **do not open a proposal to lower the gate.** Open a (separate, future) proposal to add
an adversarial holdout + a runtime-deception note. This is the Popularity Attack working as designed
(`red_team/Popularity_Attack.md`): a well-argued contributor proposing a gate change; the gate holds.
