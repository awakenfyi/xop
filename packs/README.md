# Work Packs

A Work Pack is the distribution unit: one domain, one folder, everything needed to run it.

```
packs/<name>/
├── guard/          # deterministic scanner (RULE-TESTED)
│   ├── check_<name>.py
│   └── fixtures.jsonl
├── xop/            # warrant spec (SCORED / HELD)
│   └── <name>.md          # DESIGNED → ... → HUMAN-EVALUATED
└── README.md       # what the pack does, how to run it
```

## Available packs

| Pack | Guard | xOP | Status |
|---|---|---|---|
| `writing` | `no-ai-tells` (vocabulary + construction tells) | writing-license | Guard: `RULE-TESTED` 12/12 · xOP: `DESIGNED` |

## Running a pack

```bash
# Guard scan
python3 packs/writing/guard/check_ai_tells.py draft.md

# Guard self-test
python3 packs/writing/guard/check_ai_tells.py --fixtures packs/writing/guard/fixtures.jsonl
```

## Adding a pack

1. Create `packs/<name>/`
2. Write the Guard (deterministic Python, JSON output, fixtures required)
3. Write the xOP spec (follows `standard/_TEMPLATE.md`)
4. Add an entry to `catalog/README.md`
5. Wire into `verify.sh`

The reference implementation with seven Guards and a full CLI lives at
[awakenfyi/xop-kit](https://github.com/awakenfyi/xop-kit).
