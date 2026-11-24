"""Alien Field Notes: The Two Day Earth Review.

Writes one original line -- a review of planet Earth left by an alien
tourist -- to ${MAKEFUN_OUTPUT_DIR:-/output}/entry.txt.

Deterministic: no network, no wall-clock, no randomness. The line is a
fixed string, at most 200 characters, plain UTF-8 text, one line only.
"""

import os

LINE = (
    "Lovely planet. 71% of it is ocean and not a soul lives there \u2014 "
    "prime waterfront wasted on fish. Four stars, would orbit again."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(LINE)


if __name__ == "__main__":
    main()
