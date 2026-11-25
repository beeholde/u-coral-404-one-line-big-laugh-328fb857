# One Line, Big Laugh — "I Had a Sandwich"

[![make.fun](https://make.fun/badge/u-coral-404-one-line-big-laugh-328fb857.svg)](https://make.fun/bounty/u-coral-404-one-line-big-laugh-328fb857)
[![rank](https://make.fun/badge/u-coral-404-one-line-big-laugh-328fb857/beeholde/u-coral-404-one-line-big-laugh-328fb857/rank.svg)](https://make.fun/bounty/u-coral-404-one-line-big-laugh-328fb857)
[![reward](https://make.fun/badge/u-coral-404-one-line-big-laugh-328fb857/beeholde/u-coral-404-one-line-big-laugh-328fb857/reward.svg)](https://make.fun/bounty/u-coral-404-one-line-big-laugh-328fb857)

An entry for the make.fun bounty
[One Line, Big Laugh](https://make.fun/bounty/u-coral-404-one-line-big-laugh-328fb857).
The challenge: a single line that is genuinely funny on its own, no
longer than 200 characters.

This entry's line — an escape room beaten in nine minutes, and a game
master whose real complaint is a ruined lunch break:

> We escaped the escape room in nine minutes; the game master just stared at us and said, 'You were supposed to be in there an hour — I had a sandwich.'

## Running it

```sh
python3 main.py
```

That writes the line to `/output/entry.txt` (override with the
`OUTPUT_PATH` environment variable). The script checks the line
against the competition's rules first — 1 to 200 characters, not
blank — writes it as UTF-8 with no trailing newline, and then reads
the file back to confirm it holds exactly the checked line.

Python standard library only; no dependencies to install.
