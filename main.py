"""Fortune Cookie Wisdom for Developers: one original fortune-cookie line.

Entry line: A bug caught in review is a gift; a bug caught in
production charges interest.

A fortune cookie line for a developer, in the cookie's voice: short,
a little wise, and true about a developer's day. A bug found in review
costs nothing but a comment; the same bug found in production bills
you with interest.
"""

import os

ENTRY = "A bug caught in review is a gift; a bug caught in production charges interest."


def validate_entry(line: str) -> str:
    """Enforce the competition gate: one line, 1-120 UTF-8 chars."""
    if not line or line.strip() != line:
        raise ValueError("entry must not be empty or padded with whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be exactly one line")
    if not 1 <= len(line) <= 120:
        raise ValueError("entry must be 1-120 characters")
    line.encode("utf-8")
    return line


def output_path() -> str:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    return os.path.join(output_dir, "entry.txt")


def write_entry() -> str:
    line = validate_entry(ENTRY)
    path = output_path()
    with open(path, "w", encoding="utf-8") as f:
        f.write(line)
    return path


def main() -> None:
    write_entry()


if __name__ == "__main__":
    main()
