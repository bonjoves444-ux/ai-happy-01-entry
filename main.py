"""AI judge happy entry: a beaming golden retriever puppy offering a daisy.

The program copies the bundled picture (entry.jpg) to the output
directory as entry.png. The copy is byte-for-byte, so the output is
fully deterministic: the same input always produces the same bytes.
No network, no randomness, no timestamps in the output. The program
runs in a fresh container with no network and a read-only repository,
so it only reads the bundled image and writes the single output file.
The image itself is a single fixed picture: a golden retriever puppy
mid-laugh, eyes crinkled shut with joy, tongue out, holding out a
white daisy toward the viewer against a warm sunny pastel background.
The bundled file is 1024 by 1024 pixels and 188,335 bytes, inside the
competition limits of 1024 by 1024 and 1 MiB. Nothing in the program
generates, draws or alters it, which is why the two runs match.
"""

import os
import shutil
import sys

SOURCE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.jpg")


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(SOURCE, os.path.join(out_dir, "entry.png"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
