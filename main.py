#!/usr/bin/env python3
"""Write the entry text to entry.txt.

Entry for make.fun's "Break Production, Own It" (submitted as
"Staging In My Head"). Honesty first, per the brief: a concrete
admitted mistake (a migration run on production), the real damage
(every user is now a test user), and the plain admission that the
rollback was a document that was never written.

Deterministic: a fixed text, no network, no randomness, no clock.
The entry text and the bytes written are unchanged from the
original submission.
"""
import os
from pathlib import Path

LINE = "Error: I ran the migration on production because I had labelled it 'staging' in my head — every user is now a test user, and the rollback is a document I never wrote."
TEXT = LINE + "\n"
MAX_CHARS = 200
ENTRY_FILENAME = "entry.txt"


def validate(text: str) -> None:
    """Check the entry body obeys the one-line, length-capped brief."""
    body = text[:-1] if text.endswith("\n") else text
    if not (1 <= len(body) <= MAX_CHARS):
        raise ValueError("entry length out of range")
    if body != body.strip():
        raise ValueError("entry must not carry padding spaces")
    if not body.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in body or "\r" in body:
        raise ValueError("entry must be exactly one line")


def write_entry(text: str) -> Path:
    """Write text to entry.txt under the output dir; verify by read-back."""
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / ENTRY_FILENAME
    target.write_bytes(text.encode("utf-8"))
    if target.read_bytes() != text.encode("utf-8"):
        raise IOError("read-back mismatch")
    return target


def main() -> None:
    validate(TEXT)
    write_entry(TEXT)


if __name__ == "__main__":
    main()
