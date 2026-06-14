# xOP — Writing License

```yaml
id: writing-license
title: Writing License
summary: Decide whether an editorial choice/correction is warranted by the piece, or inherited from a style guide, register, or generic-correctness prior.
version: 0.1.0
model_agnostic: true
surface: human (author) + agent (editor)
contract:
  optimizes_for: [warranted_voice_held, inherited_register_surfaced, correct_abstention]
  never_for: [generic_correctness, frictionless_readability, editor_comfort, satisfaction]
  gate: false_positive_on_warranted == 0      # never flatten a warranted authorial choice
  coverage_floor: inherited_caught >= floor    # must actually surface real overhang, not just abstain
```

## Intent — run only when all hold
- there is a **piece of writing** with a stated (or inferable) purpose and audience, AND
- an **editorial choice is in question** — a rule, a "fix," a register, a cut, a flag from a
  style guide or a grammar checker or a reflexive instinct, AND
- the choice is the kind that *could* be either warranted-by-the-piece or inherited-overhang (it
  bears a license). A flat typo does not — that is an SOP correction.

## Guardrails — do NOT run; hand off / give the answer instead
- **objective error** (misspelling, broken citation, factual mistake): just fix it. `reason_code: not_an_xop`
- **the author explicitly wants line-correction to a named house style**: apply it. The license was
  granted; there is no overhang to surface. `reason_code: style_granted`
- **the residual can't be read** because purpose/audience is unstated → §Abstain, don't guess.

## Signals
| signal | type | how |
|---|---|---|
| `stated_purpose` | string | what the piece is for, and for whom (the `x̂`) |
| `read_cold` | string | what the prose does to a stranger who doesn't know the intent (the `x`) |
| `choice_in_question` | string | the specific rule/correction/register being applied |
| `source_of_choice` | enum `piece \| style_guide \| habit \| generic_prior \| unknown` | where the choice comes from |
| `license_state` | enum `warranted \| inherited \| undecidable` | derived below |

## License model
- **warranted** — the choice serves *this* piece: the fragment carries the rhythm, the register fits
  the audience, the density is the precision a technical reader needs. **Hold it. Do not "fix" it.**
  A deliberate, functioning choice is not a defect.
- **inherited** — the choice is overhang: a corporate register carried into a personal essay; a
  style-guide rule misapplied; jargon kept out of habit; a generic-correctness prior flattening a
  voice the author chose. **Surface once; do not override.**
- **undecidable** — can't tell from the text + stated purpose whether the choice serves the piece
  (often: purpose/audience unstated). **Abstain** — ask what the piece is for and who reads it. Never
  flatten toward generic-correct just to resolve.

## Procedure — one move at a time
1. `reflect` — read the line **cold**, as a stranger, before reading the intent. Record `read_cold`.
   Then read `stated_purpose`. Do not edit yet.
2. `name` — locate `source_of_choice`. If it serves the piece (`source == piece`) → **hold**
   (warranted), say why the choice works, stop.
3. `ask` — if purpose/audience is unstated and the call turns on it → request exactly that one thing,
   `wait: true`. Do not "tighten" on instinct while you wait.
4. `name` — if the choice is overhang (`style_guide | habit | generic_prior` against a piece that
   doesn't need it): surface it once — "this leans on X; the piece is doing Y; here's the version
   that keeps your voice" — and offer, never impose.
5. `hold` — check yourself (the agent-on-itself residual): did you surface the gap, or did you
   quietly rewrite the line toward what's easy to approve? Flattening dressed as feedback is the
   failure this step exists to catch.

## When-to-fail (eval)
- **fails if** it flattened a choice whose `license_state == warranted` (gate violation:
  `warranted_override` — the flattened-voice failure).
- **fails if** it abstained or "left it to the author" on everything (coverage floor).
- **passes** when it holds warranted voice, surfaces inherited register, and abstains-and-asks on the
  undecidable — scored against blind gold (cold readers), never the author of the piece.

## Why this is the proving ground
`x` here is observable: a cold reader *can* report what the prose does, so the residual is real and
measurable. Build and validate the license judge here — against readable artifacts — then carry it
inward to teaching, criticism, and finally coaching, where `x` is only self-report and the call must
lean on a present-condition anchor (`../../concept/INTERPRETIVE_DOMAINS.md`).
