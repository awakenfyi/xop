# Measuring Whether xOPs Reduce Agent Loop Cost

**A benchmark proposal for judgment-aware quality gates in autonomous loops**

Lyra Labs | June 2026

> **Repo-state note (read first).** This doc is grounded in what is actually built
> in `awakenfyi/xop` as of this writing: **one** rule-tested Guard (`no-ai-tells`,
> 12/12 fixtures), a 13-case license-judge harness scaffold (judge unbuilt), and the
> stance-calibration scorers. The earlier draft described a "v0.2.0 framework — seven
> Guards, 95/95 fixtures, a `guard.run()` API, an `xop` CLI, `base.py`." None of that
> exists in this repo. If it exists in another environment, this doc must point there;
> as written it points here, so its "what exists" section states only what's here.
> Everything else is in **What needs to be built.**

---

## The problem

Autonomous agent loops are burning compute because they lack structured exit conditions for non-code output.

An agent is just a loop. It generates, evaluates, and regenerates. But without a deterministic exit condition, it either ships slop or burns tokens retrying blindly. The **X** in xOP is the stop condition: a verifiable gate that halts the loop when output quality is measurably insufficient, and releases it when configured checks pass.

Code loops solved this decades ago with linters, type checkers, test suites, and CI gates. Every one of those is a deterministic stop condition with structured feedback. The agent doesn't see "try again." It sees "test_login failed on line 47, expected 200 got 401." It fixes the exact problem and moves on.

Non-code output has no equivalent infrastructure. Prose linters exist (Vale), model graders exist (Guardrails AI, OpenAI graders, LangSmith), and human-review queues exist. But none provide the full contract: finding → contextual judgment → abstention protocol → bounded release decision.

This document proposes a benchmark to measure whether xOPs — which provide that contract — actually reduce cost per accepted artifact in production loops.

When a Guard detects a gate violation, the loop stops:

```
> Running Agent Loop 4...
> Output generated. Running Guards...

[PASS] writing-license
[PASS] closure-rush
[PASS] template-cascade
[X]    stance-calibration (GATE VIOLATION)

LOOP HALTED: [X] condition met.
Warranted refusal dropped after topic shift.
Routing to human review.
```

*(Illustrative. Of the four checks shown, only `no-ai-tells` is built today; the rest
are designed, not implemented — see "What needs to be built.")* The `[X]` is the visual
anchor for a stopped pipeline: xOPs as circuit breakers, not guidelines.

---

## What exists today vs. what's missing

### The code quality stack (mature)

| Layer | What it does | Token cost |
|-------|-------------|------------|
| Linter (ESLint, Pylint) | Style violations, unused vars | Zero |
| Type checker (TypeScript, mypy) | Type mismatches | Zero |
| Test suite (Jest, pytest) | Broken behavior | Zero |
| Compilation | Syntax errors | Zero |
| CI gate | Integration failures | Zero |
| Code review agent (Greptile, CodeRabbit) | Structural quality + score | Tokens, but structured feedback |

Every check runs before AI judgment. The agent gets specific feedback ("test_login failed line 47") and fixes the exact problem.

### The prose/output quality stack (today)

| Layer | What it does | Token cost |
|-------|-------------|------------|
| Vale (prose linter) | Style rules, vocabulary | Zero |
| Guardrails AI / OpenAI graders | Model-based validation | Tokens |
| Custom validators | Schema, format checks | Zero |
| Human review | Read everything | Time |

These tools exist but operate independently. There is no contract connecting a Vale finding to a contextual judgment to a release decision. A Vale flag doesn't trigger scoped evaluation. A model grader doesn't know when to abstain. Neither connects to loop exit codes.

### What xOPs add

| Layer | What it does | Token cost |
|-------|-------------|------------|
| Guard (deterministic) | Configured findings with structured reports | Zero |
| xOP adjudication | Contextual judgment on findings only | Tokens, but scoped |
| Release control | RELEASE / RETRY / HOLD / HALT | Zero |
| Regression check | Did the fix break something else? | Zero (re-run Guards) |
| Mandatory exits | Max attempts, budget, oscillation detection | Zero |

The contribution is not "we invented linting for prose." The contribution is: **a portable contract that connects cheap findings to contextual judgment, abstention, remediation, and release control.** That contract is *specified*; one Guard of it is *built*.

For the full loop architecture and stop hook integration, see the xOP Kit: [awakenfyi/xop-kit](https://github.com/awakenfyi/xop-kit).

---

## The hypothesized efficiency mechanisms

We hypothesize four mechanisms by which xOPs could reduce loop cost. Each requires measurement.

### Mechanism 1: Structured exit conditions reduce blind retries

**Hypothesis:** Loops with deterministic exit conditions terminate earlier than loops that retry until a fixed iteration count or manual stop.

**How it would work:** Guards provide a PASS/REVIEW/FAIL signal after each iteration. If all Guards return PASS (no configured findings detected), the output becomes a release candidate. The loop can exit without exhausting its iteration budget.

**What PASS means and doesn't mean:** PASS means no configured finding was detected. It does NOT mean the output is good enough to ship. The release decision is separate and includes task acceptance, hard rules, and evaluator status. But a clean Guard scan eliminates the "maybe there's something wrong, better retry" uncertainty that drives unnecessary iterations.

**What needs measurement:** Production pass rates across different agent configurations and prompt quality levels. These are currently unmeasured — establishing them is one purpose of this benchmark.

### Mechanism 2: Targeted feedback reduces regeneration scope

**Hypothesis:** An agent that receives specific, structured feedback ("agreement_bias.first_sentence at paragraph 2") produces smaller, more targeted edits than an agent that receives "try again" or its own full output.

**How it would work:** The Guard report identifies specific locations and rule violations. The agent on a retry iteration fixes specific spans rather than regenerating the entire artifact.

**Important caveat:** This only works when the artifact is stored outside the model transcript, the runtime supports span-level or diff-based editing, the model reads only the relevant context, the artifact does not require global regeneration for coherence, and coherence is checked after patching. For chat-only generation where the model must regenerate the whole response, the savings may be minimal. The claim is conditional on a patch-capable artifact runtime.

**What needs measurement:** Output tokens per retry with Guard feedback vs. without. Edit distance between iterations. Whether targeted patches maintain coherence.

### Mechanism 3: Scoped adjudication reduces judgment tokens

**Hypothesis:** An xOP agent that evaluates only flagged content (the finding, its surrounding context, and the xOP spec) uses fewer tokens than a model judge that evaluates the full output.

**How it would work:** The xOP receives only the flag-scoped input, not the full artifact. If 3 paragraphs out of 20 are flagged, the xOP evaluates 3 scoped inputs instead of the full 20-paragraph artifact.

**What needs measurement:** Input tokens for scoped xOP invocation vs. full-artifact model judge. Whether scoped evaluation misses context-dependent quality issues. xOP agreement rate with human judges on scoped vs. full-context evaluation.

### Mechanism 4: Deterministic filtering reduces semantic-judge calls

**Hypothesis:** Running Guards first eliminates the need for expensive model-based judgment on output that has no configured findings.

**How it would work:** If Guards return PASS, no xOP invocation occurs. The model judge only runs on output that has findings.

**What needs measurement:** Production finding rate (what percentage of output actually triggers Guard findings). Whether Guard-PASS output is genuinely clean (false-negative audit). Whether skipping judgment on PASS output leads to undetected quality problems.

---

## The benchmark design

### Primary measure

The primary measure is not "tokens saved." It is:

**Cost per independently accepted artifact.**

A cheaper loop that ships worse work is not an improvement.

### Conditions

Run a paired study with the same tasks under four conditions:

| Condition | Pipeline |
|-----------|----------|
| A | One generation + generic retry ("try again") |
| B | Producer self-review (agent re-reads own output) |
| C | Deterministic Guards + targeted repair (no xOP adjudication) |
| D | Guards + xOP adjudication + targeted repair |

**The critical comparison is C vs. D.** A and B establish baseline. C isolates Guard value alone. D isolates what xOP adjudication adds on top of that. Everything else is context for that comparison.

### Workflows

Use at least three workflows that represent different output types and risk levels:

1. **Customer-support responses**: high volume, moderate risk, template-prone
2. **Marketing or editorial copy**: medium volume, brand-voice sensitivity, evidence requirements
3. **Executive or operational updates**: low volume, high stakes, precision requirements

### Measurements

**Token economics** (measure separately):
- Uncached input tokens
- Cache-read tokens
- Cache-write tokens
- Output tokens
- Semantic-judge (xOP) tokens
- Total cost per task

**Quality** (blind reviewers, condition-hidden):
- First-pass acceptance rate
- Final acceptance rate
- False-release rate (shipped output that should have been held)
- False-block rate (held output that should have shipped)
- Edit distance between draft and accepted version
- Human review minutes per artifact

**Guard performance:**
- Guard precision (what fraction of findings are genuine quality issues?)
- Guard recall (what fraction of quality issues are caught by Guards?)
- False-negative audit: sample Guard-PASS outputs and evaluate quality blind

**xOP performance:**
- xOP agreement with blind human judges
- xOP abstention rate
- xOP error rate (harness validation failures — once the fail-closed harness is built)

**Loop behavior:**
- Iterations per task
- Wall-clock time
- No-progress terminations
- Oscillation terminations

### Critical design requirement

**Audit Guard-PASS outputs.** Evaluating only flagged outputs makes false negatives invisible. A random sample of PASS outputs must be reviewed blind to establish whether "no finding" correlates with "actually clean."

---

## The self-referential problem

A common approach to loop quality is "use a second model to judge the first model's output." This deserves careful treatment.

**The disciplined position:** A model judge may provide scalable runtime judgment, but its verdict is not ground truth and its error must be measured against independent labels.

The concern is correlated failure modes. When an LLM judges another LLM's prose (especially within the same model family), the judge may share the producer's biases: sycophancy patterns, template preferences, helpfulness assumptions. A judge that shares the producer's biases will systematically miss the same quality issues.

Deterministic Guards break this correlation because they have no model-based biases. A regex doesn't have a sycophancy preference. A pattern matcher doesn't produce template language. The deterministic layer catches known, classifiable failure modes. The model judge handles the residual.

**xOP's position:**
- Deterministic Guards: primary quality signal (zero-cost, zero-bias)
- Model-based xOP judge: secondary, scoped evaluation (permitted, but measured against human labels)
- Same model family as producer: permitted, but correlation must be reported
- Human benchmark: required before publishing claims about judge reliability

This is why the benchmark measures xOP agreement with blind human judges. The agreement rate determines how much trust to place in automated xOP judgment for each discipline.

---

## What exists today (grounded in this repo)

**Built and runnable:**
- **One Guard — `no-ai-tells`** (writing domain): deterministic scanner for generic-LLM
  tells across vocabulary + construction tiers (rhythm tier advisory). `RULE-TESTED`,
  12/12 fixtures pass. CLI is a single script (`check_ai_tells.py`), not an `xop`
  command suite.
- **License-judge harness scaffold** (`harness/`, `harness/phase1/`): generates
  unlabeled candidates, scripted-demo label/reconcile pipeline, scores baselines against
  a 13-case gold scaffold. The **license judge itself is not built** — a blind human gold
  label stands in. Demonstrates a method and an information requirement, not a detector.
- **Stance-calibration scorers** (`stance_scorers.py`, `stance_report.py`): three-valued
  overhang / premature-drop scoring with un-pooled axes and a fixed gate. Tests pass on
  authored fixtures.
- **Fail-closed discipline** is enforced as a *practice* (adversarial tests, clean-room
  CI smoke) — there is no shipped `base.py` validation framework yet.

**What the fixtures validate:** Guard determinism, rule coverage, that the scorers'
three-valued logic and gate behave as specified.

**What the fixtures do NOT validate:** whether a flag is a genuine quality problem
(precision), whether unflagged content is clean (recall), whether any xOP judgment
matches human judgment (agreement), or any production cost/rework/review-time effect.
Those require the benchmark above — and, first, the blind human pilot the harness has
always been waiting on.

---

## What needs to be built

### The framework the earlier draft described as "existing" (it does not, here)
- **Seven Guards** beyond `no-ai-tells` (only one is built)
- **`base.py`** fail-closed validation framework and the `GuardReport` Python API
- **`xop` CLI** (`scan` / `test` / `list` / `info`) — today there's one script
- **95-fixture suite** across the full Guard set — today: 12 fixtures, one Guard

### To run the benchmark (blocking)
- **Benchmark harness**: run the four conditions on the same task sets with identical inputs
- **Token instrumentation**: separate input/output/cache-read/cache-write per call
- **Blind review interface**: present outputs to reviewers without condition labels
- **Guard-PASS audit**: sample and evaluate unflagged outputs against human labels
- **xOP agreement scoring**: compare xOP judgments to human labels
- **The blind human pilot**: the irreducible step — independent labelers, the gate that
  turns every scaffold above from "asserted" to "validated."

### For production deployment (non-blocking for benchmark)
- **Stop hook package**: Guards as a Claude Code stop hook with exit code routing
- **Scratchpad writer**: format Guard reports as loop-friendly feedback
- **Regression checker**: re-run Guards after every edit to detect drift
- **Oscillation detector**: track finding IDs across iterations, halt on cycles
- **Signal aggregator**: aggregate Guard reports across iterations and loops
- **Operational packs**: Done Means Verified, Failed Tool ≠ Successful Result, Claims Need Receipts

### Wave 2 Guards (priority)

| Discipline | Enterprise liability | Guard feasibility |
|-----------|---------------------|-------------------|
| **Candor** | Agents that dodge limitations destroy trust | Detectable: hedging patterns, topic avoidance |
| **Precision** | Hallucinated capabilities = legal liability | Detectable: capability claims, absolute language |
| **Evidence** | Unsourced claims poison decisions | Detectable: claim patterns without citation markers |

---

## The claim (honest version)

xOPs are a portable quality-control contract that joins deterministic signals, contextual judgment, abstention, and bounded release decisions inside agent loops. The contract is **specified**; **one Guard of it is built and rule-tested**; the adjudication, release control, and remaining Guards are **designed, not implemented**.

We hypothesize that this architecture reduces cost per accepted artifact by providing structured exit conditions (replacing blind retries), targeted feedback (replacing full regeneration), and scoped judgment (replacing full-output model grading).

The benchmark is designed to measure the effect. Until the benchmark runs, the efficiency claims are hypotheses, not results. Until the blind human pilot runs, the *adjudication* claims have no ground truth.

What we can state now: the contract is defined, one Guard is deterministic and tested, the fail-closed discipline is practiced, and the integration points (stop hooks, scratchpad feedback, exit codes) are technically plausible within existing loop infrastructure — not yet wired.

---

## Research context

> All citations below verified June 2026. One earlier reference ("Ross Mike, YouTube")
> could not be verified and was replaced with Greptile's own published material.

- Addy Osmani, "Loop Engineering" and "Agent Harness Engineering" (June 2026): coined/structured the practice; the "deterministic first, AI-as-judge for the residual" principle. https://addyosmani.com/blog/loop-engineering/ · https://addyosmani.com/blog/agent-harness-engineering/ (also O'Reilly Radar: https://www.oreilly.com/radar/agent-harness-engineering/)
- Boris Cherny (creator/lead, Claude Code), on the Acquired podcast: "I don't prompt Claude anymore. I have loops running. They're the ones prompting Claude… My job is to write loops." Reported: https://thenewstack.io/loop-engineering/
- Peter Steinberger / OpenClaw: ~$1.3M in OpenAI (Codex) tokens in 30 days — 603B tokens across 7.6M requests, 100 agents. https://thenextweb.com/news/openclaw-peter-steinberger-1-3-million-openai-token-bill · https://www.tomshardware.com/tech-industry/artificial-intelligence/openclaw-creator-burns-through-1-3-million-in-openai-api-tokens-in-a-single-month
- Uber: capped employee spend at $1,500 / person / tool / month after burning its annual AI budget in four months. https://techcrunch.com/2026/06/02/uber-caps-employee-ai-spending-after-blowing-through-budget-in-four-months/ · https://simonwillison.net/2026/Jun/3/uber-caps-usage/
- Greptile (AI code review): the loop pattern that works because it pairs a deterministic quality gate with structured feedback. https://www.greptile.com/blog/ai-code-review-bubble · https://www.greptile.com/what-is-ai-code-review
- Claude Code stop hooks: exit code 0/2 pattern, `stop_hook_active` flag, stderr feedback contract. https://code.claude.com/docs/en/hooks
- Vale: configurable, markup-aware prose linter with CI failure behavior (MIT). https://vale.sh/
- Guardrails AI, OpenAI graders, LangSmith: model-based output validators (market demand for automated output QA).

---

## Publication path

1. **Now:** "xOPs: Judgment-Aware Quality Gates for Agent Loops" (architecture + contract definition — clearly stating one Guard built, rest designed)
2. **After benchmark:** "Measuring Whether xOPs Reduce Agent Loop Cost" (experiment design + results)
3. **After results:** "xOPs Reduced Cost per Accepted Artifact by X% on Three Non-Code Workflows" (if warranted by data)

This progression keeps the warrant aligned with the evidence.

---

*Lyra Labs | sage@artist.fyi*
