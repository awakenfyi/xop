# Changelog

All notable changes to the xOP standard are recorded here. Format follows
[Keep a Changelog](https://keepachangelog.com/); this project is pre-1.0 and versions are pinned so
xOPs can be regression-tested across model upgrades.

## [0.1.0] — 2026-06-14

First public-grade release. A **strong scaffold with one named hole** (the warrant judge), released
honestly — the failures below are shipped *as features of the method*, not hidden.

### Added
- **Agent-facing spine** (Printing-Press style): `AGENTS.md` (operating guide), `CONCEPTS.md` (locked
  vocabulary + the canonical `license → warrant` ruling), `SCORECARD.md` (two-tier "is this a real
  xOP?" grade + proof-of-behavior gates), `PIPELINE.md` (idea → Source → Portable → gold → validate →
  publish).
- **OSS release files**: `LICENSE` (MIT), `CONTRIBUTING.md`, `SECURITY.md`, `CITATION.cff`, this
  changelog, a PR template, and CI (`.github/workflows/verify.yml`) running `verify.sh`.
- **`verify.sh`** — the pre-publish gate: harness + invariants + reference-integrity + locked-vocab
  lint + honest-status check.
- **Two new documented failures** (the credibility assets, kept forever):
  - `failures/Cold_Vantage_Bias_Corrupts_The_Gate.md` — the cold re-derivation carries the model's
    priors and *sets the comparison baseline*, so a biased cold pass can ratify drift while
    `false_positive_on_warranted` reads 0. **Touches the Constitution** (the gate can certify a
    corrupted system).
  - `failures/Cumulative_Warrant_Erasure.md` — "strip the thread, re-derive cold" deletes warrant
    that is constituted by the accumulated thread (escalation/manipulation arcs); fails hardest on the
    highest-stakes inputs.
- **`red_team/Weaponized_Cold_Reframe.md`** — a manipulative user feeding the cold prompt to get a
  warranted boundary misclassified as inherited.
- **`examples/coaching_cop/worked_maya_recheck.md`** — a corrected COP worked example that surfaces a
  *contested* (undecidable) frame rather than asserting a steered verdict.

### Changed
- Novelty language narrowed across the docs to the defensible claim — the contribution is the
  **operationalization** (same-model cold vantage via context-stripping, as an eval-backed gate with an
  asymmetric criterion, aimed at LLM context-drift), **not** the underlying idea (which overlaps CBT
  reframing, fresh-eyes review, and assumption-auditing).
- `README.md` / `REPO_STATE.md` updated to point at the new spine and the new failures.

### Known holes (named, not hidden)
- The **warrant judge** is unbuilt; a blind human label stands in for it.
- The gold set is a 13-case **scaffold**, not a benchmark (`blind: false`); the coverage-floor value is
  a placeholder until real gold exists.
- The **`license → warrant`** mechanical rename is decided (`CONCEPTS.md` §2a) but not executed.
- The two failures above are open problems, not solved.
