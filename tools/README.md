# tools — paste-into-a-thread xOPs

Portable xOPs you load directly into a model. Distinct from `harness/` (which scores detectors)
and `concept/` (which defines the standard).

- **xop_builder.md** — the generator. A meta-xOP that builds or adapts other xOPs through a
  guided, one-question-at-a-time interview. Modes: create new · create from a transcript
  (sourcing, not labeling) · adapt an existing one (produces a gated variant, never a silent
  overwrite). Enforces the boundary test (refuses non-license-bearing scenarios) and never lets
  the user edit the fixed engine: the three license values, the action mapping, or the gate.

The Pitch Check (a worked, hand-authored xOP) lives at the repo's output root as
`xOP_Pitch_Check.md` — it's the kind of thing the builder emits.
