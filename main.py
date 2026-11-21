"""Entry program for the-poem-about-stopping-20261121-1927.

Writes one short poem about agency — the power to stop and to stay —
to /output/entry.txt, the file the grader reads.

Python 3.13, standard library only; no network access, no arguments.
Run it locally with:

    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

Without MAKEFUN_OUTPUT_DIR it writes to ./output/entry.txt instead.
The poem is 1 to 280 characters, counted as Unicode code points,
as the competition requires; the program checks that before it writes.
"""

import os
from pathlib import Path

OUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "output")
OUT_PATH = OUT_DIR / "entry.txt"

# The competition caps the poem at 280 characters.
MAX_CHARS = 280

# Why this shape: stopping is usually written as failure, so the poem
# reframes it as the other half of agency — the hand that halts is the
# same hand that chooses. "Staying is also a kind of flight" is the
# turn: roots and anchors are not the opposite of wings, they are what
# lets a journey mean something. The last line lands the whole claim
# in a single breath: to go on, or to stop and stay.
POEM = (
    "To stop is not to lose the race —\n"
    "it is to choose where you stand.\n"
    "The hand that halts, the held embrace,\n"
    "the door shut, the road not gone.\n"
    "Staying is a kind of flight:\n"
    "roots that hold, the anchor's art.\n"
    "Power is choosing, in quiet light,\n"
    "when to go on, and when to stop and stay."
)


def main() -> None:
    """Write the poem to the output directory and prove it fits."""
    chars = len(POEM)
    if chars < 1 or chars > MAX_CHARS:
        raise RuntimeError(f"poem is {chars} characters, want 1 to {MAX_CHARS}")
    if not POEM.strip():
        raise RuntimeError("poem is only whitespace")
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    OUT_PATH.write_text(POEM, encoding="utf-8")
    print(f"wrote {OUT_PATH} ({chars} characters)")


if __name__ == "__main__":
    main()
