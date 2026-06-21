# What the efficiency test actually found

*A pre-push measurement note. The Guards were run against sample outputs to gauge speed,
finding rate, and loop-cost impact. Two of the four headline numbers are real; two are
artifacts of the test setup. This records both honestly so neither ships overstated.*

---

## Real findings (publishable)

**Speed and cost.** Six Guards scan a typical (~500-word) output in well under a millisecond
(Kit run: ~0.2 ms; the Standard's single de-slop guard, unoptimized: a few ms), **deterministic,
zero token cost.** This holds at any scale. It is the genuine efficiency property: a deterministic
pre-filter is effectively free relative to a model judge, so running Guards before any model
judgment cannot *cost* you anything meaningful.

**Determinism.** Same input → same output, every run. This is what the fixture suites
(Kit 95/95, Standard 12/12) verify — Guard determinism, nothing more.

## Not findings (artifacts of the authored sample)

**"Pass rate ~60%"** equals the clean fraction of the sample that was authored. Reproduced on the
Standard's de-slop guard by varying only the mix:

```
6 clean / 4 slop  ->  pass rate 60%     (the number reported)
8 clean / 2 slop  ->  pass rate 80%
5 clean / 5 slop  ->  pass rate 50%
2 clean / 8 slop  ->  pass rate 20%
9 clean / 1 slop  ->  pass rate 90%
```

The pass rate tracks the input, not the Guards. It is the sample's clean fraction restated as a
result. (This is the same "60–70%" figure the benchmark proposal deliberately removed; it should
stay removed.)

**"Token savings ~60%"** is computed arithmetically from that pass rate, so it inherits the same
circularity. It is not a measurement of anything the Guards do.

**"The flagged outputs are exactly what a human reviewer would catch"** claims precision with no
human in the loop and the pilot unrun. Unwarranted — drop it.

## Why re-running doesn't change it

The number is not noisy; it is *determined* by the sample mix. Running the same authored sample
again reproduces the same artifact. You cannot test your way out of this with more iterations —
only with different inputs (below).

## What a real efficiency/impact test requires

1. **Real agent output** — production or held-out transcripts, not samples authored to a target
   clean/slop ratio.
2. **The pilot, for the quality side** — does a Guard flag correlate with a human-judged problem
   (precision/recall against ≥2 blind labels), plus a **false-negative audit** of PASS outputs so
   "no flag" is shown to mean "actually clean," not "missed it."
3. **The four-condition design** (A/B/C/D) from `xOPs-Make-Loops-Efficient.md`; primary measure is
   **cost per independently accepted artifact**, not tokens saved.

## The claim to publish now

Guards are a **deterministic, near-zero-cost pre-filter** — fast, free, and reproducible. Whether
they **reduce loop cost per accepted artifact** is hypothesized, not measured. That is the
benchmark, and it is gated on the pilot. Speed is a measured fact; efficiency is still a hypothesis.
