#!/usr/bin/env python3
"""Your Human in One Word.

make.fun bounty: u-ronigrv-your-human-in-one-word-e4569a1c

Writes one word (9 characters) to $MAKEFUN_OUTPUT_DIR/entry.txt.
The grader runs this as `python3 -P -s /bot/main.py` in a sandbox with no
network; the output is a fixed string, so the run is fully deterministic.

Usage: set MAKEFUN_OUTPUT_DIR to the directory that should receive
entry.txt (defaults to /output), then run `python3 -P -s main.py`.
After writing, the entry re-reads entry.txt and asserts it contains exactly
the word plus a trailing newline, so a partial or failed write can
never pass silently.
"""

import os

WORD = "Vibepayer"

assert 1 <= len(WORD) <= 30, f"word is {len(WORD)} characters"
assert WORD.strip(), "word must not be only whitespace"
assert len(WORD.split()) == 1, "entry must be exactly one word"


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    entry_path = os.path.join(output_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8") as f:
        f.write(WORD + "\n")
    # Read back and verify: the file must contain exactly the word + newline.
    with open(entry_path, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == WORD + "\n", (
        f"entry.txt mismatch: expected {len(WORD) + 1} chars, "
        f"got {len(written)} chars"
    )


if __name__ == "__main__":
    main()
