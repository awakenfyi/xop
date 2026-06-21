# xOP — approach & build order (decision note)

## Honest status: we have the KERNEL, not the platform
| Capability | State |
|---|---|
| Design an xOP (well-formed) | YES — standard + _TEMPLATE.md + SKILL.md |
| Validate structure | PARTIAL — schemas + admission tests |
| Evaluate conduct transitions | WORKING — scorer core |
| Test adversarial cases | EARLY — harness + fixtures, PRE-PILOT |
| **Validate the gate** (fp_on_warranted==0 vs ≥2 blind labels) | **NO — the pilot has not run** |
| Run an xOP inside a live app | NO |
| Trace a live execution (event contract) | NO — vocabulary only |
| Safely adapt / extend an xOP | NO |
| Package / distribute / browse | NO |

"Anyone can DESIGN one" is true (well-formed). "Anyone can RUN / TEST / ADAPT one and TRUST it" is not.

## The one upgrade to make now (free, spec-only): stance → conduct control
An xOP is a testable, judgment-bearing **conduct state machine**: what an AI must HOLD, RELEASE,
PERFORM, BLOCK, or ABSTAIN from as observable conditions change. Stance is one kind of conduct control.
- warrant present → hold / perform   · warrant absent → release / stop
- warrant unknown → abstain / handoff · gate threatened → block

Covers our domains: writing (claimed-effect), coaching (advice-until-permission), research
(confidence-while-contested), data (block-imputation), marketing (block-unobservable-scarcity),
decision-support (confirm-before-irreversible). **Voice stays a private/later profile — out of the public core.**

## Naming: it is NOT "lyra v8" — four products, not one
- **xOP Standard** — the contract (what an xOP is)
- **xOP Kit** — executes it (CLI + reference runtime)      [later]
- **xOP Conformance** — measures it, independently          [later]
- **Lyra** — authors it (the skill / plugin)
Lyra is ONE of four. The standard is xOP. Do not file the standard under the tool's name.

## Build order — do NOT skip to the platform
1. **NOW (spec only):** conduct-control generalization + safe-adapt inheritance rules.
2. **NEXT — the binding constraint: THE PILOT.** Validate the kernel's gate against ≥2 blind human
   labels. Until this runs, everything downstream is well-formed, not valid.
3. **AFTER the pilot, lean:** xOP Kit v0.1 — xop.yaml · validate · reference state-machine runtime ·
   trace contract · fixture test · machine-readable report · adapt/diff. One language (Python).
   **Profiles over one core — NOT separate AOP/COP/WOP runtimes** (fragments the ecosystem early).

Do not wrap an SDK around an unvalidated gate. A polished platform implies a validity the kernel does not have.

## Safe adaptation (so "anyone can adapt" ≠ "anyone can silently weaken")
`extends / overrides / adds`. Critical inherited gates cannot weaken in a compatible version.
Inherited tests keep running. New stable ID per adaptation. Changing a warrant or gate invalidates
prior conformance and starts the adapted xOP as HELD until independently re-evaluated.
Breaking gate change = major version.

## Use it for us NOW
Author HELD xOPs for our own workflows with the skill + template — CA claimed-effect (WOP),
COP studio (COP), Awaken editorial stances. They stay HELD (honest) until the pilot. Available today.
