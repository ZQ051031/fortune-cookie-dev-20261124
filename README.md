# Fortune Cookie Wisdom for Developers

One original fortune-cookie line for a developer, written for the
make.fun micro-bounty "Fortune Cookie Wisdom for Developers".

## The line

> A bug caught in review is a gift; a bug caught in production charges interest.

## How it works

`main.py` (standard library only) writes the line to `/output/entry.txt`
— exactly 78 bytes, one line, no trailing newline. It honours the
`MAKEFUN_OUTPUT_DIR` environment variable when set.

Run it with:

```sh
python3 main.py
```
