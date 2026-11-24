"""A single fortune-cookie line for developers, written for the
make.fun micro-bounty of the same name.

The fortune, in the cookie's voice:

    A bug caught in review is a gift; a bug caught in production
    charges interest.

The idea is simple: a bug spotted while a teammate reads your code
costs you nothing more than a comment. The same bug slipping through
to production keeps billing you, with interest, until you fix it.
"""

import os

FORTUNE = "A bug caught in review is a gift; a bug caught in production charges interest."


def check_line(text: str) -> str:
    """Check the fortune meets the bounty rules: one line, 1-120 chars."""
    if not text:
        raise ValueError("fortune must not be empty")
    if text != text.strip():
        raise ValueError("fortune must not start or end with whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("fortune must be a single line")
    if len(text) < 1 or len(text) > 120:
        raise ValueError("fortune must be between 1 and 120 characters long")
    text.encode("utf-8")
    return text


def entry_path() -> str:
    """Resolve where entry.txt goes, honouring MAKEFUN_OUTPUT_DIR."""
    directory = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(directory, exist_ok=True)
    return os.path.join(directory, "entry.txt")


def main() -> None:
    """Validate the fortune and write it out with no trailing newline."""
    line = check_line(FORTUNE)
    path = entry_path()
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(line)


if __name__ == "__main__":
    main()
