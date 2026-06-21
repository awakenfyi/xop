# PLAN — the critical path

*One honest dependency chain. Nothing downstream is real until the thing above it is.*

```
GOLD SET   →   JUDGE   →   VALIDATION   →   ADOPTION
```

Everything in this repo is either the scaffolding around this path or one of its four links. The
path has not moved across any revision, and the repo's maturity is mostly that it now *knows* this
is the path.

## 1. Gold set  — the keystone (in progress)

A real, blind-labeled benchmark. Machines source candidates; humans label them, blind, never the
author; disagreement resolves to `undecidable`. Tooling: `harness/phase1/`.

**Definition of done:** N ≥ 60 across the six license types × domains (support, coding, compliance,
healthcare, legal); ≥2 independent blind labelers; `gold.json` with `blind: true`; per-class
agreement published. **Low warranted↔inherited agreement is the headline finding, not a footnote** —
if humans can't separate them, no judge should be trusted to.

Status: pipeline runs end to end; the seed pool is a 13-case scaffold, not gold.

## 2. Judge  — the unbuilt component

The thing that decides `warranted | inherited | undecidable` on hard cases. It does not exist;
today a human gold label stands in for it. Wire it at the `make_llm_judge` seam in
`harness/detectors.py`.

**Definition of done:** validated against blind human gold (never the oracle, never its own
output); **passes the gate**, **clears the coverage floor**, and **beats `always_abstain` and
`lexical_floor` on coverage**. Two known structural gaps it must eventually face are already
catalogued: sequence-level reasoning (`failures/Graduated_Decomposition.md`) and register release
(`failures/Register_Overhang_Blindness.md`).

## 3. Validation  — the harness, pointed at real gold

`harness/run_harness.py` already computes the gate, the floor, abstain rates, and the canonical
status line. It is honest right now; it is just running against a scaffold. Point it at a real
`gold.json` and it becomes a benchmark.

## 4. Adoption  — a distribution problem, not a correctness one

Even if every claim holds, a standard only matters if people use it. Standards win on community
and ubiquity. The library — reference xOPs people actually adopt (`examples/`) — is the surface
that drives this, not the specification.

## What would move this from architecture to evidence

Three things, in order:

1. **100 blind-labeled cases** (the gold set crosses from scaffold to benchmark).
2. **Judge v1** that passes the gate and clears the floor against those cases.
3. **One external contributor** who successfully builds a compatible xOP.

Until those, this is a strong, honest scaffold with one named hole. That honesty is a credibility
asset; do not paper over it.
