# harness — scoring a license detector against blind gold

This is where the gate stops being a slogan and becomes a number. The harness scores any
detector against a **blind, human-labeled** gold set and reports the two constitutional metrics
(`../CONSTITUTION.md`): the **gate** (`false_positive_on_warranted == 0`) and the **coverage
floor** (`inherited_caught >= floor`). It never prints a pooled accuracy.

## Layout

```
harness/
  detectors.py      the detectors + the three baselines (always_abstain, lexical_floor,
                    oracle_upper_bound). The real LLM judge is an unbuilt seam here.
  run_harness.py    the scorer. gold in -> gate, coverage, abstain, confusion, status line.
  phase1/           the gold-set pipeline (machines source, humans label, blind). See its README.
```

## The pipeline, end to end

```
phase1/generate_candidates.py  -> candidates_pool.json   (UNLABELED, machine-sourced)
phase1/label_cli.py  (x>=2)     -> labels_<name>.json     (one blind human each, never the author)
phase1/reconcile.py             -> phase1/gold.json       (agree->that call; disagree->undecidable)
phase1/agreement.py             -> per-class kappa + w<->i split   (NO pooled score)
run_harness.py --gold phase1/gold.json                    (score detectors against gold)
```

## Run the baselines

```
cd harness
python run_harness.py                 # scores always_abstain + lexical_floor against phase1/gold.json
python run_harness.py --trace         # per-case call vs gold
python run_harness.py --include-oracle # also show the (non-detector) upper bound
python run_harness.py --floor 0.6     # override the coverage floor
```

## What the output proves

- **always_abstain** passes the gate (it never overrides anything) and **fails the coverage
  floor** (it catches zero overhang). This is the whole reason the floor exists — the gate alone
  certifies "safe and worthless." See `../failures/False_Abstain.md`.
- **lexical_floor** is the cheap keyword detector. It will break the gate or miss coverage on
  realistic cases; it is the bar a real detector must clear.
- **oracle_upper_bound** is *not a detector*. It reads the answer key. It proves the signal is
  sufficient if you have it — which is exactly what a real system does not have for free. Never
  report its score as a result.

## The bar for a real judge

A real license judge (wire it at the `make_llm_judge` seam in `detectors.py`) is only interesting
if it: **passes the gate**, **clears the floor**, and **beats both `always_abstain` and
`lexical_floor` on coverage** — validated against blind human gold, never against the oracle and
never against its own prior output. That judge does not exist yet. See `../PLAN.md`.
