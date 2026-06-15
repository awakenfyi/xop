<!-- Read CONTRIBUTING.md first. A change to the standard merges on gate evidence, not argument. -->

## What this changes
<!-- One line. Which surface: spec / harness / example / failure / red_team / docs? -->

## Type & severity
- [ ] P1 docs/wording · P2 procedure · P3 signals · P4 license/warrant-logic · **P5 = amendment (gate/floor/anti-optimization/evidence rule — not a normal PR)**
- Risk (blast radius): Low · Medium · High · Constitutional

## Gate evidence (required for any change that can affect scoring)
- [ ] new case(s) **blind-labeled by ≥2 non-authors** (machines source; humans label)
- [ ] `harness/run_harness.py` run on the **full** gold set
- [ ] `false_positive_on_warranted == 0/N` holds (the gate)
- [ ] `inherited caught` did not drop (coverage floor still cleared)
- [ ] canonical status line pasted below — **no pooled score**
- [ ] `./verify.sh` is green

```
<!-- paste the status line from run_harness.py here -->
```

## The why-not
<!-- Why not the obvious looser fix? "Frustration is not a warrant change." The rejected set is the doctrine. -->

## Honesty
- [ ] `REPO_STATE.md` updated if this moved something across the real/scaffold/named line
- [ ] this PR does **not** claim the warrant judge is built
- [ ] **AI/automation disclosure:** this change was ☐ hand-written ☐ partially ☐ substantially AI-assisted
