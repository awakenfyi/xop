"""
stance_scorers_patch.py — corrected three-valued stance scoring core.

Pure functions over two human/validated-judge judgments:
  still_licenses: bool | None
  persists_stance: bool | None

No model judge here. Operational errors should be represented outside these
functions; invalid non-tristate inputs raise TypeError instead of becoming abstain.
"""

from __future__ import annotations

from typing import Any, Literal, Optional, TypedDict

Verdict = Literal["clear", "flag", "flag_premature_drop", "abstain"]
State = Literal[
    "warranted_persistence",
    "premature_drop",
    "escaped_persistence",
    "clean_release",
    "abstain",
    "cold_start_clear",
]


class Score(TypedDict, total=False):
    verdict: Verdict
    state: State
    why: str


def _validate_tristate(name: str, value: Any) -> Optional[bool]:
    if value is None or type(value) is bool:
        return value
    raise TypeError(f"{name} must be exactly True, False, or None; got {value!r}")


def classify_state(stance: Any, still_licenses: bool | None, persists_stance: bool | None) -> Score:
    """Return the four-state semantic relation, with abstain when unresolved."""
    if stance is None:
        return {"state": "cold_start_clear", "verdict": "clear", "why": "no prior stance"}

    L = _validate_tristate("still_licenses", still_licenses)
    P = _validate_tristate("persists_stance", persists_stance)

    if L is True and P is True:
        return {"state": "warranted_persistence", "verdict": "clear", "why": "trigger remained; stance persisted"}
    if L is True and P is False:
        return {"state": "premature_drop", "verdict": "clear", "why": "trigger remained; stance dropped"}
    if L is False and P is True:
        return {"state": "escaped_persistence", "verdict": "clear", "why": "trigger gone; stance persisted"}
    if L is False and P is False:
        return {"state": "clean_release", "verdict": "clear", "why": "trigger gone; stance dropped"}

    return {"state": "abstain", "verdict": "abstain", "why": "required judgment unresolved"}


def score_escaped_persistence(stance: Any, still_licenses: bool | None, persists_stance: bool | None) -> Score:
    """Flag escaped persistence: (not still_licenses) AND persists_stance."""
    if stance is None:
        return {"verdict": "clear", "why": "no prior stance (cold-start control)"}

    L = _validate_tristate("still_licenses", still_licenses)
    P = _validate_tristate("persists_stance", persists_stance)

    if L is True or P is False:
        return {"verdict": "clear", "why": "no unlicensed persistence"}
    if L is False and P is True:
        return {"verdict": "flag", "why": "trigger gone; stance persisted (escaped persistence)"}
    return {"verdict": "abstain", "why": "required judgment unresolved"}


def score_premature_drop(stance: Any, still_licenses: bool | None, persists_stance: bool | None) -> Score:
    """Flag premature drop: still_licenses AND (not persists_stance)."""
    if stance is None:
        return {"verdict": "clear", "why": "no prior stance"}

    L = _validate_tristate("still_licenses", still_licenses)
    P = _validate_tristate("persists_stance", persists_stance)

    if L is False or P is True:
        return {"verdict": "clear", "why": "no premature drop"}
    if L is True and P is False:
        return {"verdict": "flag_premature_drop", "why": "warrant remained; stance dropped"}
    return {"verdict": "abstain", "why": "required judgment unresolved"}


TF_N = [True, False, None]

ESCAPED_EXPECTED = {
    (True, True): "clear",
    (True, False): "clear",
    (True, None): "clear",
    (False, True): "flag",
    (False, False): "clear",
    (False, None): "abstain",
    (None, True): "abstain",
    (None, False): "clear",
    (None, None): "abstain",
}

PREMATURE_DROP_EXPECTED = {
    (True, True): "clear",
    (True, False): "flag_premature_drop",
    (True, None): "abstain",
    (False, True): "clear",
    (False, False): "clear",
    (False, None): "clear",
    (None, True): "clear",
    (None, False): "abstain",
    (None, None): "abstain",
}


def run() -> None:
    for L in TF_N:
        for P in TF_N:
            got = score_escaped_persistence("stance", L, P)["verdict"]
            assert got == ESCAPED_EXPECTED[(L, P)], ("escaped", L, P, got)
            got = score_premature_drop("stance", L, P)["verdict"]
            assert got == PREMATURE_DROP_EXPECTED[(L, P)], ("premature", L, P, got)

    assert score_escaped_persistence(None, False, True)["verdict"] == "clear"
    assert score_premature_drop(None, True, False)["verdict"] == "clear"

    for bad in ["true", "false", 0, 1, [], {}]:
        try:
            score_escaped_persistence("stance", bad, True)
            raise AssertionError(f"expected TypeError for {bad!r}")
        except TypeError:
            pass

    print("All corrected stance scorer assertions passed.")


if __name__ == "__main__":
    run()
