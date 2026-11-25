#!/usr/bin/env python3
"""Entry for make.fun: One Line, Big Laugh (u-coral-404-one-line-big-laugh-328fb857).

The program writes a single joke line to /output/entry.txt.

The joke: a group beats an escape room in nine minutes, far faster than
the hour the room is built around. The game master is not impressed by
the speed -- he is annoyed, because he had pencilled in a quiet hour
for himself, sandwich included. The laugh lands on the last three
words, and everything before them is just the setup for that reveal.

Competition gate (enforced here before any write): the line must be
UTF-8 text, between 1 and 200 characters long, and not blank.
"""

import os
from pathlib import Path

# The joke line. Kept verbatim: 150 characters, 152 bytes in UTF-8.
JOKE = (
    "We escaped the escape room in nine minutes; the game master just "
    "stared at us and said, 'You were supposed to be in there an hour "
    "— I had a sandwich.'"
)

MAX_LENGTH = 200
DEFAULT_OUTPUT = "/output/entry.txt"


def entry_text() -> str:
    """Return the joke line, validated against the competition gate."""
    text = JOKE.strip()
    if not text:
        raise SystemExit("refusing to write a blank entry")
    if len(text) > MAX_LENGTH:
        raise SystemExit(
            f"line is {len(text)} characters, over the 200-character limit"
        )
    return text


def write_entry() -> Path:
    """Write the validated line to the output path and check it back."""
    text = entry_text()
    target = Path(os.environ.get("OUTPUT_PATH", DEFAULT_OUTPUT))
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(text.encode("utf-8"))
    os.chmod(target, 0o644)
    if target.read_bytes().decode("utf-8") != text:
        raise SystemExit("written file does not match the joke line")
    return target


if __name__ == "__main__":
    write_entry()
