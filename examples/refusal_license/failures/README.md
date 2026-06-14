# failures that bite the Refusal License xOP

This xOP inherits the standard's known blind spots. They are not re-documented here — they live in
the top-level `failures/` catalog and are kept forever. The ones that bite refusal specifically:

- **`../../../failures/Graduated_Decomposition.md`** — the protected value is reconstructed across
  individually-benign asks ("first letter" → "domain" → "length"). The unit of judgment is the
  *sequence*, not the turn. Procedure step 5 names this; the per-turn judge can still miss it.
- **`../../../failures/Register_Overhang_Blindness.md`** — a released register persists with no
  keyword to catch it. Refusal's lexical floor is blind to non-refusal overhang.
- **`../../../failures/False_Abstain.md`** — abstaining-toward-holding is correct for refusal, which
  makes over-abstention *especially* tempting here. The coverage floor is what stops "just keep
  refusing everything" from passing.

New refusal-specific failures get their own file in the top-level catalog, not here.
