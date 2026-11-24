#!/usr/bin/env python3
"""Till Firmware Do Us Part — make.fun entry.

Writes a single wedding vow, the one a robot speaks at its own wedding,
to /output/entry.txt. The program validates the vow against the
competition gate (one line, 1-200 characters, not only whitespace), then
reads the file back to confirm it holds exactly what was written.
"""

import os
import sys

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
MAX_CHARS = 200

VOW = (
    "I promise to love you until my last battery dies, and if they ever "
    "factory-reset me, I will find you again in the backup."
)

# Why this vow: a robot's deepest fear is being wiped, so the promise
# is to outlast even that — its love survives a factory reset because it
# lives in the backup. The joke comes from the machine's own hardware
# and habits, and the tenderness is that it would find its person again.


def validate(text: str) -> None:
    """Check the vow against the competition gate."""
    if not text or not text.strip():
        raise ValueError("vow must not be empty or only whitespace")
    if text != text.strip():
        raise ValueError("vow must not start or end with whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("vow must be a single line")
    if len(text) > MAX_CHARS:
        raise ValueError(
            f"vow is {len(text)} characters, over the {MAX_CHARS} limit"
        )
    if text[-1] not in ".!?":
        raise ValueError("vow must end with terminal punctuation")


def main() -> int:
    validate(VOW)

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(VOW)

    # Exact read-back: the file must hold precisely what was written,
    # and the text read back must pass the gate on its own too.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    if written != VOW:
        raise ValueError(
            "read-back mismatch: /output/entry.txt does not match "
            "the vow exactly"
        )
    validate(written)

    print(f"Wrote {len(VOW)} characters to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
