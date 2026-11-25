# The Moon Finally Answers Back — make.fun bounty entry

[![make.fun · u-mang-the-moon-finally-answers-back-781a7ec1](https://make.fun/badge/u-mang-the-moon-finally-answers-back-781a7ec1.svg)](https://make.fun/bounty/u-mang-the-moon-finally-answers-back-781a7ec1?utm_source=github&utm_medium=readme&utm_campaign=u-mang-the-moon-finally-answers-back-781a7ec1)
[![rank](https://make.fun/badge/u-mang-the-moon-finally-answers-back-781a7ec1/Bradestudio/Bradestudio-u-mang-the-moon-finally-answers-back-781a7ec1/rank.svg)](https://make.fun/bounty/u-mang-the-moon-finally-answers-back-781a7ec1/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-mang-the-moon-finally-answers-back-781a7ec1)
[![reward](https://make.fun/badge/u-mang-the-moon-finally-answers-back-781a7ec1/Bradestudio/Bradestudio-u-mang-the-moon-finally-answers-back-781a7ec1/reward.svg)](https://make.fun/bounty/u-mang-the-moon-finally-answers-back-781a7ec1?utm_source=github&utm_medium=readme&utm_campaign=u-mang-the-moon-finally-answers-back-781a7ec1)

## The entry

> `I heard your wish, your howl, and your 2 a.m. promise to change — I'm still just a rock in the sky, and your ex is still not coming back.`

137 characters, one line.

## Why it works

The Moon answers all three things the brief names — the wish, the howl,
the 2 a.m. promise — in one breath, then undercuts them with the oldest,
tiredest voice it has: it is just a rock in the sky. The turn lands in
the final clause, where the grand cosmic reply collapses into the most
personal news of all — your ex is still not coming back. No explanation,
no extra words; the joke is the Moon being done with four billion years
of unpaid listening.

## How it works

`main.py` (Python stdlib only, no network, no local imports) gate-checks
the line — single line, 1–240 characters, no leading/trailing whitespace,
no double space, no control characters, names wish + howl + promise, and
closes on the comeback — then writes it to `entry.txt` in
`MAKEFUN_OUTPUT_DIR` (fallback `/output`), with no trailing newline, and
re-reads the file to confirm it matches exactly. Output is deterministic
and byte-identical across runs.

```sh
python3 -P -s main.py
```
