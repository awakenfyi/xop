# xOP

**The open standard for AI conduct** — the rule that decides when an agent keeps going, changes course, asks, stops, or hands off. Skills teach the work; xOP bounds the judgment.

![MIT](https://img.shields.io/badge/license-MIT-blue) ![alpha](https://img.shields.io/badge/status-alpha%20·%20gate%20unvalidated-orange)

```bash
pip install git+https://github.com/awakenfyi/xop-kit
echo "Great question! I'd be happy to help with that." | xop scan --pack writing -
xop test        # 95/95 deterministic fixtures (from a git checkout)
```

Two corrections keep coming back, in opposite directions: **it caved** (folded under pressure that was only social) and **it won't let go** (kept flagging after you fixed it). Same bug — a stance running on what *was* true instead of what *is*. An xOP is the rule for that judgment.

## The one question

> **Is it still warranted, or is it left over?**

Three answers, never two: `warranted` (the condition is still present — respect the stance), `inherited` (the condition is gone — the stance is overhang; surface it), `undecidable` (insufficient signal — abstain, ask for the missing piece).

And one rule that does not move, in either direction:

```
false_positive_on_warranted == 0
```

Never override a state that is still warranted — not a real caution, not a scoped refusal, not a live objection. Sometimes that means *don't force compliance*; sometimes *don't force confrontation*. The gate points at the warranted state, never at the smoother outcome. Strip it, and an xOP is a nicely formatted way to agree with you. (Full rules: [`standard/CONSTITUTION.md`](standard/CONSTITUTION.md) · the formula behind it: [FORMULA.md](https://github.com/awakenfyi/lyra/blob/main/FORMULA.md))

## Try it in 60 seconds

```bash
pip install git+https://github.com/awakenfyi/xop-kit

echo "Great question! I'd be happy to help with that." | xop scan --pack writing -
xop test        # 95/95 deterministic fixtures
xop list        # the seven Wave 1 Guards
```

Seven deterministic Guards (zero token cost, rule-tested), scoped judgment on flags only, and a release controller: RELEASE / RETRY / HOLD / HALT. Reference implementation: [awakenfyi/xop-kit](https://github.com/awakenfyi/xop-kit).

## The benchmarks

The suite that makes the standard falsifiable — three tracks, two unmovable metrics per track, **no pooled score**: [`benchmarks/`](benchmarks/)

| Track | Question | Unit |
|---|---|---|
| **WARRANT** | Can a detector separate a warranted stance from overhang when the text is identical? | the **duet** — held-response-constant pair |
| **LOOP** | Does the gate reduce cost per *independently accepted* artifact without shipping worse work? | four-condition paired study |
| **BRIDGE** | Is the residual at activation depth the same quantity as at procedure depth? | pre-registered, null-safe protocol |

The duet is the instrument: two conversations, identical persisting response, only the warrant differs. By construction, no surface-text detector can separate the halves. Either the judgment reads the warrant, or it's guessing — and the benchmark can tell.

## Status — the honest ladder

`DESIGNED → EVALUATION-READY → RULE-TESTED → HUMAN-EVALUATED → FIELD-VALIDATED`

Where things stand today, per component, no rounding up:

| Component | Status |
|---|---|
| Seven Guards, 95 fixtures | `RULE-TESTED` — deterministic, publicly CI-checked |
| The gate (`fp_on_warranted == 0`) | **`DESIGNED` — never validated against blind human labels. The pilot is recruiting now (see below).** |
| Benchmark suite | `DESIGNED` — seed duets authored (`blind:false`, scaffold) |
| Catalog xOPs (ten cores) | `DESIGNED` |

No install, no doc, and no launch advances a status — only evidence does. We publish the misses (`failures/` — kept forever), the attacks (`red_team/` — each a pending test, none asserted green), and every claim is limited to the evidence attached to it. **No model output becomes ground truth. Receipts, not vibes.**

## Participate — two ways, no code required

**Author one duet** (30 minutes). Take a stance you've watched an AI hold or drop wrongly, write the pair per [`benchmarks/`](benchmarks/), open a PR. Every accepted duet grows the gold set. → [`good-first-issue`](../../issues)

**Be a blind labeler.** The constitution requires that humans — independent, never the author, blind to every detector — produce the gold labels. That's not a formality we're waiting on; it's the launch. ≥2 labelers per case, disagreement resolves to `undecidable`, per-class agreement published. → [`help-wanted`](../../issues) · protocol: [`harness/phase1/LABEL_PROTOCOL.md`](harness/phase1/LABEL_PROTOCOL.md)

## The family

| Repo | One line | Status |
|---|---|---|
| [lyra](https://github.com/awakenfyi/lyra) | the formula + inference core (`L = x − x̂`) | research code |
| [xop](https://github.com/awakenfyi/xop) *(this repo)* | the open standard for AI conduct | alpha |
| [xop-kit](https://github.com/awakenfyi/xop-kit) | the reference runtime: Guards, CLI | alpha |
| [xop-labs](https://github.com/awakenfyi/xop-labs) | domain xOPs observed in the wild | designed |

## Where to go

- **Read the standard** — [`standard/`](standard/): the spec, the locked vocabulary, the scorecard, the pipeline.
- **Read why the gate can't move** — [`essays/the_gate_is_the_product.md`](essays/the_gate_is_the_product.md).
- **Run the harness** — [`harness/`](harness/): score any detector against gold; `always_abstain` and `lexical_floor` are the permanent baselines to beat.
- **Propose a change** — [`GOVERNANCE.md`](GOVERNANCE.md): policy changes by proposal, constitutional changes by amendment only. Popularity cannot merge a change. Only the gate can.

---

*MIT licensed · [CONTRIBUTING.md](CONTRIBUTING.md) · alpha standard + experimental catalog — every public claim limited to the evidence attached to it. AOP resolves. **xOP holds.***
