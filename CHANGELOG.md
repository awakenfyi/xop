# Changelog

All notable changes to the xOP standard are recorded here. Format follows
[Keep a Changelog](https://keepachangelog.com/); this project is pre-1.0 and versions are pinned so
xOPs can be regression-tested across model upgrades.

## [0.3.0] — 2026-07-01 — the benchmark release

### Added
- **`benchmarks/`** — the three-track suite (WARRANT / LOOP / BRIDGE): gate + floor per track, no pooled scores, seed duets included as author-labeled scaffold.
- **The duet** as the canonical evaluation unit: held-response-constant minimal pairs; `lexical_floor` scores AUC 0.5 by construction.
- **`docs/CONDUCT-DIRECTORY.md`** — the `xops/` folder convention positioned against Eve; hold/drop fixtures per rule; comparison table.
- **`docs/STANDARD-EXPANSION.md`** — the wire format strategy: JSON Schemas, skills-rail wedge, three adapters, conformance suite.
- **Linked `FORMULA.md`** (lyra repo) as the single definition of the residual; READMEs no longer redefine x and x̂.
- **Unified the family table** across xop / xop-kit / lyra (canonical — same text in every README).
- **Opened the pilot**: public recruitment of blind labelers per `LABEL_PROTOCOL.md`; tracked in issues.

### Changed
- `README.md` — v2: leads with the two-directions framing (caved / won't let go), benchmark section with three-track table, per-component status table, pilot-recruiting section.
- **Removed** the not-yet-installable `/xop` skill quickstart (returns when the install path ships — a quickstart that doesn't run is a claim without evidence).

### Status note
Gate remains `DESIGNED`/unvalidated; this release changes what can be *tested*, not what is *proven*.

---

## [Unreleased] — PR 0 cleanup (2026-06-21)

### Fixed
- `catalog/AOP-02-evidence-caution.SCORED.md` → renamed to `AOP-02-evidence-caution.md` (status never
  in filenames; badge updated to `DESIGNED` throughout the file).
- `standard/_TEMPLATE.md`, `packs/README.md`, `packs/writing/README.md`,
  `packs/writing/guard/no-ai-tells.guard.md` — old `SCORED / HELD` badge language replaced with
  evidence ladder (`DESIGNED → RULE-TESTED → HUMAN-EVALUATED`).
- `verify.sh` Gate 4 — now skips absolute-path links (site routes `/cop`, `/xop`, etc.) and `meta/`
  directory, preventing false positives from non-file references.
- `README.md` — removed two hyperlinks to future directories (`skills/xop-author/`, `catalog/profiles/`)
  that don't exist yet; replaced with plain-text notes pointing to where they'll land.
- `CITATION.cff` — title: "license-bearing (warrant-bearing)" → "warrant-bearing" (old terminology).
- `CONTRIBUTING.md` — `REPO_STATE.md` reference updated to `build/inventory.json`; verify.sh
  description corrected from "locked-vocab lint" to "honest-status check".
- `AGENTS.md` — `REPO_STATE.md` reference updated to `build/inventory.json`.

### Changed
- `meta/` added to `.gitignore` and removed from git index (files remain on disk). Internal
  scaffolding is not part of the public standard per the build brief.
- `build/` added to `.gitignore`. Inventory artifacts are generated, not normative.

---

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
