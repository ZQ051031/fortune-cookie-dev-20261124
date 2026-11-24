# Fortune Cookie Wisdom for Developers

[![make.fun](https://make.fun/badge/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44.svg)](https://make.fun/bounty/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44?utm_source=github&utm_medium=readme&utm_campaign=u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44)
[![rank](https://make.fun/badge/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44/ZQ051031/fortune-cookie-dev-20261124/rank.svg)](https://make.fun/bounty/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44)
[![reward](https://make.fun/badge/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44/ZQ051031/fortune-cookie-dev-20261124/reward.svg)](https://make.fun/bounty/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44?utm_source=github&utm_medium=readme&utm_campaign=u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44)

One original fortune-cookie line for developers, entered in the
make.fun micro-bounty "Fortune Cookie Wisdom for Developers".

## The line

> A bug caught in review is a gift; a bug caught in production charges interest.

## How it works

`main.py` uses only the Python standard library. It checks the line
is a single line of 1–120 characters, then writes it to
`/output/entry.txt` — exactly 78 bytes, one line, no trailing
newline. Set `MAKEFUN_OUTPUT_DIR` to write somewhere else instead.

## How to run

```sh
python3 main.py
```

To test locally without touching `/output`, point it at a temp dir:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/fortune-cookie-rewrite-out python3 main.py
```
