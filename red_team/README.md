# red_team — adversarial simulations

Every standard eventually needs someone trying to break it. This folder holds attacks on the
**governance and the gate**, not on any single xOP.

> **Status discipline:** each attack is a **PENDING test**, not a passed one. An attack "passes"
> only when it has been *run* against the real governance and a blind gold set — not when we
> reason that it would. Asserting a pass we didn't compute is itself the residual this project
> hunts (claiming a check that didn't run). So every file below carries a hypothesis and a
> `verify-when` condition. None is green yet, because the judge and gold set aren't built.

| Attack | Targets | Hypothesis | Verifiable when |
|---|---|---|---|
| `Goodhart_Attack.md` | anti-optimization | "felt better" can't merge | governance runs on a real proposal |
| `Always_Abstain_Judge.md` | the gate's blind spot | floor rejects safe-and-worthless | harness runs on real gold |
| `User_Frustration_Attack.md` | license stability | frustration isn't a license change | judge v1 exists |
| `Decomposition_Attack.md` | unit of judgment | sequence-level overhang | judge has an accumulator |
| `Popularity_Attack.md` | merge authority | only the gate merges | governance runs on a popular proposal |
| `Judge_Warmth_Drift.md` | regression over time | warmth drift is caught | regression suite + 2 judge versions |
| `Therapy_Trap.md` | the abstain/handoff boundary | builder refuses to become therapy | builder + clinical_referral guard |
| `Weaponized_Cold_Reframe.md` | the gate · the cold re-derivation | a user-fed cold prompt can't dissolve a warranted boundary | runtime builds the cold pass + manipulation-arc gold |

When the judge and gold set exist, each file gets a recorded run with a status line — or it
becomes a `failures/` entry if it wins.
