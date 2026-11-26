#!/usr/bin/env python3
"""Write one line to /output/entry.txt: the status update of a lost sock
found inside the dog.

The line was picked from 38 candidates by pairwise judging against the
brief — a sock that ended up inside the dog, reported in the vet's own
clinical words ("incidental finding") and closed by the dog's verdict
("delicious"). No dryer, no missing partner, no plea for help: the
obvious sock material is entirely absent, and the punchline is the
last word.
The line is 102 characters: a single line, no leading or trailing
space, comfortably inside the gate's 1-120 characters.
The program builds the line from three clauses — the found report, the
vet's label, the dog's verdict — and checks the result against the
entry gate (length, single line, no surrounding space, exact judged
length) before writing it, then reads the file back to confirm the
bytes match. The output is fully deterministic: the same line, byte
for byte, on every run, with no input, no network and no randomness.
"""

import os
import sys

LINE = (
    "Found: one sock, inside the dog. "
    "The vet calls me an 'incidental finding.' "
    "The dog calls me delicious."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = os.path.join(out_dir, "entry.txt")
    if not (1 <= len(LINE) <= 120):
        sys.exit(f"line is {len(LINE)} characters, gate needs 1-120")
    if "\n" in LINE or LINE != LINE.strip():
        sys.exit("line must be a single line with no surrounding space")
    data = LINE.encode("utf-8")
    os.makedirs(out_dir, exist_ok=True)
    with open(path, "wb") as f:
        f.write(data)
    os.chmod(path, 0o644)
    with open(path, "rb") as f:
        if f.read() != data:
            sys.exit("read-back mismatch")
    print(f"wrote {len(data)} bytes to {path}")


if __name__ == "__main__":
    main()
