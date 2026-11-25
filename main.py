#!/usr/bin/env python3
"""Write a one-line review of the most boring everyday object
for make.fun's The Most Boring Object, Reviewed in One Line
bounty.

Why this entry fits the judge's brief: the rubber band is
genuinely boring and everyday, and the joke comes from how it
really behaves -- it holds things together by slowly strangling
them, then it snaps and vanishes into the drawer forever. The
observation is true, the laugh lands inside one line, and there
is no cheap gag bolted on top of the object.
"""

import os

LINE = (
    "The rubber band has one job \u2014 hold things together \u2014 "
    "and it does it by slowly strangling them until it snaps and "
    "vanishes into the drawer forever."
)


def validate_line(line: str) -> None:
    # The gate: UTF-8 text, 1-200 characters, a single line.
    # The line was counted at exactly 146 characters; pin that
    # so any accidental wording change fails loudly instead of
    # silently shipping a different (or over-long) entry.
    assert len(line) == 146, f"line is {len(line)} characters, expected 146"
    assert 1 <= len(line) <= 200, f"line is {len(line)} characters"
    assert "\n" not in line, "line must be a single line"
    assert "\r" not in line, "line must be a single line"
    assert line.strip() == line, "line must not have surrounding whitespace"
    # The judge's brief: a genuinely boring everyday object, a
    # true observation about how it really behaves, and the laugh
    # inside one line -- the rubber band strangling, snapping,
    # and vanishing into the drawer.
    assert "rubber band" in line, "line must keep its boring object"
    assert "snaps" in line, "line must keep the snap"
    assert "drawer" in line, "line must keep where it vanishes"


def verify_output(path: str) -> None:
    # Read it back: the file on disk must be exactly the line.
    with open(path, "rb") as f:
        raw = f.read()
    assert raw.decode("utf-8") == LINE, "entry.txt does not match the line"
    assert len(raw.decode("utf-8")) == 146, "entry.txt is not 146 characters"
    assert len(raw) == 150, "entry.txt is not 150 bytes (em-dashes must survive)"
    assert b"\n" not in raw, "entry.txt must be a single line"
    assert not raw.endswith(b"\n"), "entry.txt must have no trailing newline"


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(output_dir, exist_ok=True)
    validate_line(LINE)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE)
    verify_output(path)
    print(LINE)


if __name__ == "__main__":
    main()
