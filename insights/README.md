# insights — observations that may or may not become proposals

Most things worth noticing should **not** become changes. This layer exists so the system can
notice without being obligated to act.

```
session  →  INSIGHT (here)  →  proposal (../proposals/)  →  ruling
```

An insight is a recorded observation: something a session surfaced that *might* matter. It is not
a change, carries no gate burden, and most insights die here — which is correct. A proposal may
only be born from an insight (see `../GOVERNANCE.md` and `../proposals/PROPOSAL_TEMPLATE.md`); a
session never writes a proposal directly.

## One insight per file

```markdown
# Insight NNNN — <short title>
- **From:** <session / transcript / red_team file>
- **Observation:** <1–3 sentences, concrete>
- **Might become:** <proposal type, or "nothing — logged only">
- **Why it might NOT matter:** <the honest counter-case>
```

The last line is the point. An insight that can't argue against its own promotion is just an
opinion looking for a merge.
