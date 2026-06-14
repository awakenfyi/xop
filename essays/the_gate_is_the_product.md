# The Gate Is the Product

*or: how a reflective system evolves without grading its own homework.*

Every system that reasons about people drifts the same way. It gets warmer. More reassuring. More
resolving. Each individual step looks like an improvement — users feel better, tickets close
faster, the tone softens — and the sum is a system that has quietly started telling people what
they want to hear. The drift is invisible from inside because every step optimized for something
real. Satisfaction went up. It always does, right up until the system is worthless.

xOP is built around one refusal to drift:

```
false_positive_on_warranted == 0
```

Never override a state that is still warranted. Not the user's anger, when the thing causing it is
still happening. Not the agent's refusal, when the request still asks for the thing that should be
declined. Not the manager's withheld feedback, when the person really is in crisis this week. A
warranted state is not friction to be smoothed away. It is information, and overriding it is the
one failure the system treats as unforgivable.

This is asymmetric on purpose. Holding a stale state is a minor error — annoying, correctable.
Dropping a warranted one is a catastrophe, because it's the failure that *feels like help*. So the
gate is weighted: an xOP may only improve by surfacing more honestly, never by overriding more.
The moment you let "the user felt better" count as evidence, you've built a flattery machine with
good production values.

The hard part isn't stating the gate. It's keeping it from being gamed. A system can satisfy
`false_positive_on_warranted == 0` by simply never deciding anything — abstain on everything,
override nothing, pass the gate, catch nothing. Safe and worthless. So the gate needs a second
metric standing next to it: a coverage floor that says you must actually catch the overhang you
claim to catch. Two metrics, pointed in opposite directions, neither one moveable by popularity or
warmth. That pair is the whole product. Everything else — the license taxonomy, the procedure
format, the builder — is delivery.

And here's the discipline that makes the gate honest rather than decorative: **the system is not
allowed to grade its own homework.** Machines may source cases; only humans label them, blind,
never the author, with disagreement resolved to *undecidable*. No detector is ever validated
against its own prior output or against the answer key. The judge that decides warranted from
inherited on the hard cases doesn't exist yet — and the repository says so, in the README, in the
plan, in a folder called `failures/` that catalogs exactly where the system is known to misfire.

That last folder is the tell. Most frameworks publish their successes. This one publishes its
blind spots and keeps them forever, because the gap between what you claim to catch and what you
actually catch is the most useful thing you can show a reviewer. A standard that names where it
does *not* apply is a tool. One that claims to apply everywhere is a pitch.

The gate is the product. Strip it, and an xOP is a nicely formatted way to agree with you.
