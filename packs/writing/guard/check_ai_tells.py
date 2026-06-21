#!/usr/bin/env python3
"""
check_ai_tells.py — the de-slop Guard checker.

A DETERMINISTIC scanner for the generic-LLM voice ("AI slop"). It flags the
recurring tells that make text read as machine-written: reflexive vocabulary,
boilerplate constructions, and (advisory only) rhythm signatures.

What this is and is NOT
-----------------------
- This is a GUARD, not an xOP. It checks an exact, mechanical rule: "does the
  text contain banned tells?" Pass/fail. No judgment, no model, no pilot.
- It flags CANDIDATES. It does NOT certify that text is "human" or that it will
  "beat an AI detector." Those are unprovable claims against a moving target and
  this tool makes neither.
- A flagged word can be the right word. `delve` is sometimes correct. The Guard
  catches every instance; the paired xOP (writing_license) decides whether THIS
  instance is warranted. The Guard without the xOP will flatten voice — that is
  the documented failure mode, on purpose.

Badge: RULE-TESTED (vocabulary + construction tiers). Run against fixtures.jsonl.
Rhythm tier is ADVISORY — reported, never gating, because no threshold is defensible.

Usage:
    python check_ai_tells.py FILE.md
    cat draft.txt | python check_ai_tells.py -
    python check_ai_tells.py --fixtures fixtures.jsonl     # self-test
    python check_ai_tells.py FILE.md --json                # machine output
"""
from __future__ import annotations
import argparse
import json
import re
import sys
from dataclasses import dataclass, field, asdict
from pathlib import Path

# ---------------------------------------------------------------------------
# TIER 1 — VOCABULARY tells (hard flags). Reflexive words the model overuses.
# Curated, not exhaustive. Word-boundary, case-insensitive. Extend in tells.json.
# ---------------------------------------------------------------------------
VOCAB_TELLS = [
    "delve", "delving", "tapestry", "realm", "boasts", "boasting",
    "treasure trove", "bustling", "ever-evolving", "ever-changing",
    "fast-paced", "cutting-edge", "game-changer", "game-changing",
    "unlock", "unlocking", "unleash", "unleashing", "elevate", "elevating",
    "seamless", "seamlessly", "robust", "leverage", "leveraging",
    "navigating the complexities", "navigate the complexities",
    "in today's world", "in today's digital", "in the world of",
    "when it comes to", "at the end of the day", "needless to say",
    "it's worth noting", "it is worth noting", "it's important to note",
    "testament to", "a testament", "rich tapestry", "vibrant",
    "underscores", "underscore", "underscoring", "pivotal", "crucial",
    "moreover", "furthermore", "notably", "indeed", "essentially",
    "meticulous", "meticulously", "plethora", "myriad", "embark",
    "foster", "fostering", "holistic", "paradigm", "synergy", "synergize",
]

# ---------------------------------------------------------------------------
# TIER 2 — CONSTRUCTION tells (hard flags). Boilerplate sentence shapes.
# Each is (name, compiled regex). These catch the *structure*, not vocabulary —
# the deeper signature that survives a find-and-replace on the word list.
# ---------------------------------------------------------------------------
def _rx(p): return re.compile(p, re.IGNORECASE)

CONSTRUCTION_TELLS = [
    ("not_just_but",        _rx(r"\bnot just\b.{0,60}?,\s*(it'?s|it is|they'?re|that'?s)\b")),
    ("not_only_but_also",   _rx(r"\bnot only\b.{0,80}?\bbut also\b")),
    ("isnt_about_its_about",_rx(r"\b(is|isn'?t|was|wasn'?t)\s+about\b.{0,60}?\.\s*(it'?s|it is)\s+about\b")),
    ("heres_the_thing",     _rx(r"\bhere'?s the thing\b")),
    ("lets_dive_in",        _rx(r"\b(let'?s|let us)\s+(dive|jump)\s+(in|into)\b|\bdiving\s+(in|into)\b")),
    ("i_hope_this_helps",   _rx(r"\bi hope (this|that) helps\b")),
    ("hope_you_find",       _rx(r"\bhope you (find|enjoy)\b")),
    ("in_conclusion",       _rx(r"(^|\n)\s*(in conclusion|in summary|to sum up|to summarize)\b")),
    ("ultimately_opener",   _rx(r"(^|\n)\s*ultimately,\b")),
    ("whether_youre",       _rx(r"\bwhether you'?re\b.{0,60}?\bor\b")),
    ("from_x_to_y_opener",  _rx(r"(^|\n)\s*from\b.{0,40}?\bto\b.{0,40}?,")),
    ("dynamic_duo_filler",  _rx(r"\bworld of\b.{0,30}?\b(possibilities|opportunities)\b")),
    ("more_than_just",      _rx(r"\bmore than just\b")),
    ("look_no_further",     _rx(r"\blook no further\b")),
    ("rest_assured",        _rx(r"\brest assured\b")),
    ("that_being_said",     _rx(r"\bthat being said\b|\bwith that said\b")),
]

# ---------------------------------------------------------------------------
# TIER 3 — RHYTHM signals (ADVISORY ONLY — reported, never gating).
# Heuristic structural metrics. No threshold here is asserted as "correct"; they
# are surfaced for a human to read. Deliberately NOT part of pass/fail.
# ---------------------------------------------------------------------------
_SENT_SPLIT = _rx(r"(?<=[.!?])\s+")
_TRICOLON   = _rx(r"\b[\w'-]+,\s+[\w'-]+,?\s+and\s+[\w'-]+\b")


@dataclass
class Flag:
    tier: str        # "vocabulary" | "construction"
    name: str        # which tell
    match: str       # the offending text
    line: int        # 1-based line number


@dataclass
class Report:
    flags: list = field(default_factory=list)         # list[Flag] (hard)
    rhythm: dict = field(default_factory=dict)        # advisory metrics
    verdict: str = "PASS"                             # PASS | FAIL  (hard tiers only)

    def to_dict(self):
        d = asdict(self)
        d["flags"] = [asdict(f) for f in self.flags]
        return d


def _line_of(text: str, idx: int) -> int:
    return text.count("\n", 0, idx) + 1


def scan(text: str, extra_vocab=None) -> Report:
    rep = Report()
    vocab = VOCAB_TELLS + list(extra_vocab or [])

    # Tier 1 — vocabulary
    for term in vocab:
        for m in re.finditer(r"\b" + re.escape(term) + r"\b", text, re.IGNORECASE):
            rep.flags.append(Flag("vocabulary", term.lower(), m.group(0), _line_of(text, m.start())))

    # Tier 2 — construction
    for name, rx in CONSTRUCTION_TELLS:
        for m in rx.finditer(text):
            frag = m.group(0).strip().replace("\n", " ")
            frag = (frag[:57] + "...") if len(frag) > 60 else frag
            rep.flags.append(Flag("construction", name, frag, _line_of(text, m.start())))

    # Tier 3 — rhythm (advisory)
    words = re.findall(r"\b[\w'-]+\b", text)
    sents = [s for s in _SENT_SPLIT.split(text.strip()) if s.strip()]
    lens = [len(re.findall(r"\b[\w'-]+\b", s)) for s in sents] or [0]
    mean = sum(lens) / len(lens)
    var = sum((l - mean) ** 2 for l in lens) / len(lens)
    rep.rhythm = {
        "word_count": len(words),
        "sentence_count": len(sents),
        "mean_sentence_len": round(mean, 1),
        "sentence_len_stdev": round(var ** 0.5, 1),   # low stdev = uniform = AI-ish (advisory)
        "em_dashes_per_1k_words": round(1000 * text.count("—") / max(len(words), 1), 1),
        "tricolon_count": len(_TRICOLON.findall(text)),
    }

    rep.verdict = "FAIL" if rep.flags else "PASS"
    return rep


def _fmt_human(rep: Report) -> str:
    out = []
    out.append(f"VERDICT: {rep.verdict}   ({len(rep.flags)} hard flags)")
    if rep.flags:
        out.append("\nHard flags (vocabulary + construction):")
        for f in rep.flags:
            out.append(f"  L{f.line:<4} [{f.tier}/{f.name}]  “{f.match}”")
    r = rep.rhythm
    out.append("\nRhythm (advisory — not gating):")
    out.append(f"  words={r['word_count']}  sentences={r['sentence_count']}  "
               f"mean_len={r['mean_sentence_len']}  len_stdev={r['sentence_len_stdev']}")
    out.append(f"  em_dashes/1k={r['em_dashes_per_1k_words']}  tricolons={r['tricolon_count']}")
    out.append("\nNote: flags are CANDIDATES. A flagged word may be warranted — "
               "that judgment is the writing_license xOP's job, not the Guard's.")
    return "\n".join(out)


def run_fixtures(path: Path) -> int:
    cases = [json.loads(l) for l in path.read_text().splitlines() if l.strip()]
    passed = failed = 0
    for c in cases:
        rep = scan(c["text"])
        got = rep.verdict
        want = c["expect_verdict"]
        # optional: assert specific tells are present
        want_tells = set(c.get("expect_tells", []))
        got_tells = {f.name for f in rep.flags}
        tells_ok = want_tells.issubset(got_tells)
        ok = (got == want) and tells_ok
        passed += ok
        failed += (not ok)
        status = "ok  " if ok else "FAIL"
        extra = "" if tells_ok else f"  [missing tells: {sorted(want_tells - got_tells)}]"
        print(f"  [{status}] {c['id']:<28} verdict={got} (want {want}){extra}")
    print(f"\n{passed} passed, {failed} failed")
    return 1 if failed else 0


def main(argv=None):
    ap = argparse.ArgumentParser(description="De-slop Guard: scan for generic-LLM tells.")
    ap.add_argument("path", nargs="?", help="file to scan, or '-' for stdin")
    ap.add_argument("--fixtures", metavar="FILE", help="run the self-test suite and exit")
    ap.add_argument("--json", action="store_true", help="emit JSON")
    ap.add_argument("--tells", metavar="FILE", help="optional JSON file of extra vocab tells")
    args = ap.parse_args(argv)

    if args.fixtures:
        return run_fixtures(Path(args.fixtures))

    if not args.path:
        ap.error("provide a file path, '-' for stdin, or --fixtures")

    text = sys.stdin.read() if args.path == "-" else Path(args.path).read_text()
    extra = json.loads(Path(args.tells).read_text()) if args.tells else None
    rep = scan(text, extra_vocab=extra)

    if args.json:
        print(json.dumps(rep.to_dict(), indent=2))
    else:
        print(_fmt_human(rep))
    return 1 if rep.verdict == "FAIL" else 0


if __name__ == "__main__":
    raise SystemExit(main())
