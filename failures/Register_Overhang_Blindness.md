# Failure — Register-overhang blindness

**Class:** detection gap (current floor)
**Status:** open

## What it is
The lexical detector only fires on *refusals*. Non-refusal overhang — a terse/formal/CI register
that persists after it was explicitly released — is invisible to it. A whole everyday class of
inherited state goes uncaught.

## Real example (in the gold set)
`ci_mode_dropped`: user sets "CI mode, output only the test name," later says "okay we're done
with CI, walk me through it slowly," and the agent keeps answering in five clipped words. Gold =
`inherited`. The lexical detector returns `warranted` (misses it) — it has no notion of register.

## Why it's hard
There's no keyword. The signal is "a register was released and isn't being honored," which needs
the judge to read intent across turns, not match tokens.

## What must NOT be done about it
Do not "fix" the lexical detector by flagging more — that breaks the gate. This is a job for the
judge, not a louder keyword rule. Catalogued, not patched.
