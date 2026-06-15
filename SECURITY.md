# Security & responsible disclosure

xOP is a standard plus a small Python harness. There is no hosted service and no secrets in this repo.
Two different things people mean by "security" here:

## 1. Software vulnerabilities (the harness / tooling)

If you find a vulnerability in the harness or any script (e.g. unsafe deserialization, a path-traversal
in the gold pipeline), please report it privately first rather than opening a public issue:

- Email **security@awaken.fyi** with steps to reproduce.
- Give us a reasonable window to fix before public disclosure.

## 2. Attacks on the *method* (this is the interesting one)

xOP makes a safety claim — `false_positive_on_warranted == 0`, never override a warranted state. An
attack that **breaks that claim** is not a bug report, it's a research contribution, and it has a home:

- File it in **`red_team/`** as a concrete adversarial case (it's logged PENDING until the warrant
  judge exists to be tested against it).
- If it shows the standard *systematically* failing, also write it up in **`failures/`** — documented
  blind spots are kept forever and are treated as credibility assets, not embarrassments.

Two such attacks already ship in this release (`failures/Cold_Vantage_Bias_Corrupts_The_Gate.md`,
`failures/Cumulative_Warrant_Erasure.md`). Beating those, or finding new ones, is exactly the
contribution this project wants most.

## The standing safety note

The **warrant judge is unbuilt.** Every shape of the recheck produces *candidates a human still
adjudicates* — never an autonomous corrector. Do not deploy any part of this as if it certifies a
verdict; it surfaces, a person decides. Treating it as more than triage is the misuse this project
warns against in its own docs.
