# Reviewer's Guide

*How to evaluate this proposal. Read `00`–`02` first. This document states plainly what is being
claimed, where it's strong, where it's soft, and exactly what we'd like you to attack.*

The goal of review is not endorsement. It is to find where the framing breaks before we build on
it. The most valuable feedback finds a hole.

---

## The claims, stated plainly

So you know exactly what you're testing, here is everything the proposal asserts:

1. **There is a lineage.** SOP → AOP → xOP is a real evolution, not three unrelated things.
2. **The xOP is structurally an AOP with one reversed flow and three added fields.** Nothing
   else is invented; the rest is borrowed from proven service-agent tooling.
3. **"Surface, don't resolve" is a coherent, useful procedure target** for judgment-bearing
   work — not just a mood.
4. **There is a real boundary.** The format applies only where stated/actual can diverge, a
   stance can be warranted-or-inherited, and abstaining can be correct. Outside that, it's
   theater.
5. **The gate is the product.** `false_positive_on_warranted == 0`, held asymmetrically, is what
   separates a reflection tool from a tool that just tells people what they want to hear.
6. **The warranted/inherited distinction is the same operation across domains** — the unifying
   idea.
7. **Two residuals, two scales.** The xOP runs the residual on the *work*; an honesty layer runs
   the same residual on the *agent itself*, and the second is mandatory because judgment work has
   no free ground truth.

If any of these is false, say which and why. Claim 3 and Claim 4 are load-bearing; if either
fails, the proposal needs rework, not tuning.

---

## Where it's strong

- **The structure is borrowed, not invented.** The authoring skeleton is lifted from tooling
  that already works at production scale. This lowers adoption risk and makes the proposal
  legible to anyone who has built a service agent.
- **The boundary is self-limiting.** The format names where it does *not* apply. This is rare and
  is the main reason it reads as a tool rather than a pitch.
- **The gate is asymmetric and explicit.** The most common failure mode of "reflection AI"
  (drifting into flattery) is named and structurally penalized rather than hoped against.
- **The warranted/inherited distinction generalizes cleanly** and is independently recognizable
  to anyone who's worked on agent refusal behavior or executive coaching.

---

## Where it's soft (our own honest assessment)

We'd rather hand you the weak points than have you find them and assume we missed them.

1. **The felt-domain observability gap.** The residual `L = x − x̂` needs `x` (the *actual*)
   observable independently of `x̂` (the claim). In writing or marketing you can observe `x`
   (read it cold, test it on a stranger). In coaching and other felt domains, "the actual
   feeling" is only available as the person's report — which is `x̂` again. So in exactly the
   domains the project is most excited about, the residual is *inferred*, not measured. The
   format leans on abstain to compensate, but reviewers should judge whether that's enough, or
   whether the felt domains should be demoted relative to the observable ones.

2. **The judge doesn't exist yet.** Computing `license_state` (warranted vs. inherited) on hard,
   adversarial cases is the hard part, and it is currently stood in for by a gold human label.
   We have shown the signal is *sufficient if you have it*; we have not built the thing that
   produces it. Until that judge exists and is validated against independent humans on its
   false-positives-on-warranted, the eval is a contract, not a working detector.

3. **"Standard" is a distribution problem, not a correctness problem.** Even if every claim is
   true, a portable format only matters if people adopt it. Standards win on community and
   ubiquity, not on being right. Pure eval/standard plays are also notoriously hard to
   monetize. Reviewers with go-to-market judgment: weigh this honestly.

4. **Taxonomy sprawl risk.** The format is most credible kept minimal (defined once, two proven
   domains, derive-your-own). There is a standing temptation to ship a large catalog of named
   sub-formats, which would contradict the "subtractive" claim. Watch for it.

5. **The reversed arrow could collapse into vagueness.** "Surface, don't resolve" is the whole
   proposition. If, in practice, authors can't tell the difference between a useful surfaced gap
   and a non-committal non-answer, the format degrades into a procedure that does nothing,
   warmly. The worked example (`01`) is our attempt to show it doesn't — judge whether it
   succeeds.

---

## Questions to pressure-test

Concrete attacks, roughly in priority order:

- **The boundary.** Take three tasks from your own work. Run each through the three-condition
  membership test in `00`. Does the test cleanly sort them into SOP/AOP vs. xOP — or does
  everything sneak through as "judgment-bearing"? If the boundary doesn't exclude things, it
  isn't real.
- **The reversed arrow.** Pick an xOP step that "names the gap and stops." Could a skilled human
  coach/editor tell it apart from (a) a real insight and (b) an evasive non-answer? If not, the
  target is underspecified.
- **The gate under pressure.** Take the withheld-feedback xOP in `01` and try to "improve" it the
  way a helpful model would — make it warmer, more reassuring. Does your improvement quietly
  erode `fp_on_warranted`? (If it does, that's the gate doing its job — and the test working.)
- **Net-new minimality.** Try to reduce the "new" part below three fields + one reversed flow +
  one gate. If you can, the claim is even narrower than stated (fine). If you find something new
  we *missed*, that's the most valuable finding.
- **Cross-domain.** Instantiate one new xOP in a domain not covered (teaching? negotiation?
  design critique?). Does the skeleton hold without strain, or does the domain need fields the
  spec doesn't have?
- **The honesty layer.** Is "two residuals" a real architectural distinction, or a tidy
  restatement? Specifically: can an xOP be trustworthy *without* the agent-on-itself residual, or
  does it genuinely collapse into a flattery machine as claimed?

---

## Known open problems (not yet solved)

These are acknowledged gaps, listed so review doesn't spend effort rediscovering them:

- The **license judge** (computes warranted/inherited on hard cases) — does not exist.
- A **labeling protocol** for the human gold set (independent annotators, inter-annotator
  agreement per subtype, the abstain-gold rule, never-the-author) — specified in principle,
  not yet built.
- A **felt-domain residual** that doesn't reduce to the person's self-report — unsolved.
- A **regression methodology** for surfacing quality across model upgrades — sketched, untested.
- Any **UX validation** that the reflective pause actually improves outcomes for real users —
  none yet.

---

## How to give feedback that helps

- Tie each comment to a **claim number** (above) or a **section** of `02` so it's actionable.
- Prefer **counterexamples** to general impressions: "here's a task that breaks the boundary"
  beats "the boundary feels fuzzy."
- Flag **where you'd plant a flag and where you wouldn't** — which domain you'd lead with, which
  you'd drop.
- If you think the whole frame is wrong, say so directly and name the load-bearing claim it
  fails on. A clean "claim 4 is false because X" is worth more than ten polish notes.

---

*Reviewer's guide · draft. Find the hole. The most useful review is the one that makes us
narrow a claim or move a flag.*
