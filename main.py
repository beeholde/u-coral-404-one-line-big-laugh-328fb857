"""One Line, Big Laugh -- make.fun bounty u-coral-404-one-line-big-laugh-328fb857.

Writes one single hilarious line to /output/entry.txt. The joke is a
competence story that collapses into someone else's ruined lunch: we beat
the escape room in nine minutes, and the game master -- who had an hour
of quiet planned around us -- is left staring at a sandwich he no
longer has time to eat. The turn lands in the last three words, and the
line is built from one specific absurd detail, nothing else.

Gate: the line must be UTF-8 text of 1 to 200 characters, not only white
space. This program enforces the cap before writing.
"""

import os
from pathlib import Path

LINE = "We escaped the escape room in nine minutes; the game master just stared at us and said, 'You were supposed to be in there an hour \u2014 I had a sandwich.'"

MAX_CHARS = 200


def main() -> None:
    # Gate, named: a valid line is 1-200 characters of UTF-8 text.
    line = LINE.strip()
    if not line or len(line) > MAX_CHARS:
        raise SystemExit("line fails the 1-200 character gate")
    out = Path(os.environ.get("OUTPUT_PATH", "/output/entry.txt"))
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_bytes(line.encode("utf-8"))
    os.chmod(out, 0o644)
    # Read back and confirm the file holds exactly the gated line.
    if out.read_bytes().decode("utf-8") != line:
        raise SystemExit("entry.txt does not match the gated line")


if __name__ == "__main__":
    main()
