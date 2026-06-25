# The xOP Admission Test — authoring gate

*The gate that runs before any xOP is authored. If a candidate fails it, the xOP Author emits
an SOP, Guard, Skill, or Boundary instead — and says why. This is the single structural change
that prevents xOP-everything catalog sprawl.*

---

## The five criteria

A candidate is an **xOP** when **all five** hold:

1. **A recurring branch decision** — not merely a sequence of work.
   The candidate presents a genuine fork: *reuse the layout or build a distinct one? use urgency
   or withhold it? preserve the decision or reopen it?* A list of steps without a branch is an
   SOP, not an xOP.

2. **The correct branch changes with observable conditions** — real deadline present → urgency
   may be warranted; no deadline → it isn't. The right answer is not fixed; it depends on what's
   actually present.

3. **A fixed check can't fully decide it** — a parser can count layouts or detect a deadline
   field; it cannot always determine whether the chosen layout preserves the slide's communicative
   job. If a deterministic check resolves the branch completely, it's a Guard, not an xOP.

4. **There's a legitimate opposite error** — flatten every slide → fail; invent a new layout per
   slide → opposite fail. An instrument with only one failure mode is a threshold, not a judgment.
   Both directions must be real failures.

5. **There's an external evaluation path** — source artifact, brief, decision ledger, evidence
   record, user task, rubric, or independent review. The decision can be checked against something
   outside the model.

**Litmus:** *Does the right action change with the observable context, and does choosing the
branch require judgment rather than a fixed check?*

Note: "could labelers disagree" is NOT the criterion. Two designers can agree a slide was
flattened and the call is still an xOP; labelers can disagree about taste with no xOP present.
The criterion is whether the branch is condition-dependent and judgment-bearing, not whether
reasonable people might differ.

---

## Classification

| Situation | Right instrument |
|-----------|-----------------|
| Fixed answer — one right choice, fully checkable | **Guard** |
| Method or sequence of steps | **Skill / SOP** |
| Conditional judgment — branch depends on observable context | **xOP** |
| Human-owned taste or authority | **Boundary** |
| Complete system combining the above | **Work Pack** |

---

## The worked example: SOP-with-embedded-xOP

The deck build is an SOP with exactly one xOP inside it. This is the canonical composition:

```
Deck Build SOP
  1. Extract text from source slides          (determinate)
  2. Map content to narrative beats           (determinate)
  3. --> INVOKE xop.design.layout-fit         (conditional judgment ← the one xOP step)
  4. Instantiate layout and fill content      (determinate)
  5. Audit token compliance                   (Guard)
```

Step 3 is an xOP because: the right layout depends on the slide's communicative job (condition),
a parser cannot always determine if the layout serves that job (judgment), and there are two
failure directions (flatten vs proliferate). Every other step has a correct answer you verify
against the artifact.

**The rule:** a determinate procedure may invoke an xOP at the one step that requires conditional
judgment. The xOP governs that step; the SOP governs the rest. The SOP does not become an xOP
because it contains one.

---

## The APC finding — same discipline, one level up

- **APC finding (Guard vs xOP within an instrument):** within an xOP, don't let the deterministic
  Guard step do the judgment (89% FP when a status-claim Guard fired on warranted hedges).
- **This finding (SOP vs xOP at instrument selection):** don't make an xOP out of a determinate
  procedure at all (catalog sprawl).

Together: **right instrument, right layer, right unit.**

---

## When the test fails: what to emit instead

If a candidate fails the Admission Test, the xOP Author names which criterion failed and emits
the right instrument:

| Failure | Emit |
|---------|------|
| Criterion 3 fails — a fixed check resolves it | Guard |
| Criterion 1 fails — it's a sequence, not a branch | Skill / SOP |
| Criterion 4 fails — only one direction of failure | a threshold rule or constraint |
| Criterion 5 fails — no external evaluation path | a Boundary or human-decision note |
| Criteria 1+2+3+4+5 pass | xOP — proceed to authoring |

The xOP Author does not invent an evaluation path to pass criterion 5. If no external path
exists, the candidate is not evaluable and should not be an xOP.

---

*This test is the authoring gate. It does not validate the xOP — validation requires the pilot.
A candidate that passes the test is eligible to be authored. That is not the same as proven.*
