#!/usr/bin/env python3
"""Everyday Wonder - make.fun entry program.

Writes one sentence (at most 200 characters) about a small moment of
wonder in everyday life to /output/entry.txt, exactly as the gate requires.
Deterministic, no network, no input.
"""

from pathlib import Path

ENTRY = (
    "My phone unlocked before I touched it, and the face on the lock "
    "screen looked faintly disappointed to see me."
)

OUTPUT = Path("/output/entry.txt")


def main() -> None:
    text = ENTRY.strip()
    # One sentence only: no line breaks, no trailing space, within the gate.
    assert 1 <= len(text) <= 200, f"entry is {len(text)} characters"
    assert text.strip() == text and text, "entry must not be only whitespace"
    assert "\n" not in text, "entry must be a single sentence on one line"
    # The twist: the phone recognises its owner before being touched, and
    # the recognised face seems faintly disappointed — the everyday made
    # strange by a glance, grounded in Face ID, a thing everyone has met.
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(text, encoding="utf-8")
    print(f"wrote {len(text)} characters to {OUTPUT}")


if __name__ == "__main__":
    main()
