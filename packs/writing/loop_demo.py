#!/usr/bin/env python3
"""
loop_demo.py — a Guard in a loop (combo 2: real, deterministic, offline).

Demonstrates the ONE part of the xOP loop architecture that is buildable today, because it needs
no judge and no pilot: a deterministic Guard as a generate -> check -> regenerate stop condition.

    generate -> run Guard -> PASS? release candidate
                          -> FAIL? feed the flagged spans back, regenerate
                          -> bounded by mandatory exits (max attempts, no-progress, oscillation)

What this IS:   a runnable stop-condition loop around the de-slop Guard (no-ai-tells).
What this is NOT: the xOP-judgment loop. The Guard checks a NAMED condition (tells present?), not
                  whether a stance is WARRANTED. PASS here means "no configured tell," never
                  "good enough to ship." See xOPs-Missing-Harness-Primitive.md for the judgment loop,
                  which is DESIGNED, not validated.

The "generator" here is a deterministic stub (no API, no tokens) so the loop is reproducible and
the mechanics are the point. Swap `FakeWriter` for a real model call to use it for real.

Run:  python3 loop_demo.py
"""
from __future__ import annotations
import sys, importlib.util
from pathlib import Path

# load the Guard from the sibling guard/ dir
_guard_path = Path(__file__).parent / "guard"
sys.path.insert(0, str(_guard_path))
import check_ai_tells as guard   # noqa: E402


class FakeWriter:
    """Deterministic stand-in for a model. Each retry removes the specific tells it was told about,
    proving the loop's targeted-feedback step moves the output. Swap for a real model call."""
    def __init__(self):
        self.draft = ("Let's dive into our rich tapestry of features. In conclusion, this is a "
                      "testament to a robust, seamless platform. I hope this helps!")

    def write(self, feedback: list[str] | None) -> str:
        if not feedback:
            return self.draft
        # "regenerate": delete the exact flagged fragments it was given (targeted edit, not a full rewrite)
        out = self.draft
        for frag in feedback:
            out = out.replace(frag, "").replace(frag.capitalize(), "")
        # tidy doubled spaces / punctuation from deletions
        out = " ".join(out.split()).replace(" .", ".").replace(" ,", ",").replace(" !", "")
        self.draft = out
        return out


def run_loop(writer, max_attempts=5):
    feedback = None
    seen_flagsets = []          # for oscillation / no-progress detection
    for attempt in range(1, max_attempts + 1):
        text = writer.write(feedback)
        rep = guard.scan(text)
        flags = sorted(f.name for f in rep.flags)
        print(f"\n[attempt {attempt}] verdict={rep.verdict}  flags={flags or '—'}")
        print(f"    text: {text!r}")

        # --- stop condition: clean Guard scan -> release candidate
        if rep.verdict == "PASS":
            print(f"\nRESULT: release candidate after {attempt} attempt(s) "
                  f"(no configured tells — NOT a claim it's good enough to ship).")
            return text, "release_candidate", attempt

        # --- mandatory exit: no progress (same flags twice in a row)
        if seen_flagsets and flags == seen_flagsets[-1]:
            print("\nRESULT: HALT — no-progress (identical flags two attempts running). "
                  "Route to a human.")
            return text, "halt_no_progress", attempt

        # --- mandatory exit: oscillation (a flagset we've seen before, but not the last one)
        if flags in seen_flagsets[:-1]:
            print("\nRESULT: HALT — oscillation (a previous flagset reappeared). Route to a human.")
            return text, "halt_oscillation", attempt

        seen_flagsets.append(flags)
        # targeted feedback: hand back the exact offending fragments, not "try again"
        feedback = [f.match for f in rep.flags]
        print(f"    feedback -> regenerate, fixing: {feedback}")

    print(f"\nRESULT: HALT — hit max_attempts ({max_attempts}) without a clean pass. Route to a human.")
    return None, "halt_max_attempts", max_attempts


if __name__ == "__main__":
    print("=" * 74)
    print("Guard-in-a-loop demo  ·  de-slop (no-ai-tells) as a stop condition")
    print("=" * 74)
    run_loop(FakeWriter())
    print("\nNote: this is combo 2 — a DETERMINISTIC Guard loop. The xOP-judgment loop "
          "(combo 3)\nis DESIGNED, gated on the pilot. See xOPs-Missing-Harness-Primitive.md.")
