#!/usr/bin/env python3
"""The Funniest Sick-Day Excuse — u-zeroxfive-the-funniest-sick-day-excuse-37423a36.

Writes one original sick-day excuse line to /output/entry.txt, with no
trailing newline. Stdlib only, fully deterministic.
"""

import os

LINE = (
    "Can't come in today \u2014 I sneezed so hard I pulled a muscle in my "
    "back, and now I'm flat on the floor renegotiating my spine's contract."
)


def main() -> None:
    assert isinstance(LINE, str)
    assert 1 <= len(LINE) <= 199, f"line must be 1-199 chars, got {len(LINE)}"
    assert "\n" not in LINE and "\r" not in LINE, "line must be a single line"
    assert LINE.strip() == LINE, "line must not be only whitespace"
    data = LINE.encode("utf-8")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "wb") as f:
        f.write(data)


if __name__ == "__main__":
    main()
