"""the-poem-about-permission-20261121-0235 entry: writes the poem to the output directory.

Python 3.13 standard library only. No network, no randomness:
running it twice produces byte-identical output.
"""

import os

POEM = """The Blue Shirt

The agent folds everything,
sheets, shirts, small socks.
It holds up the blue shirt
my son outgrew, and asks,
shall I fold this too?
No.
I take it back
and fold it myself,
crease by crease,
the way his shoulders
used to fill it."""


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
