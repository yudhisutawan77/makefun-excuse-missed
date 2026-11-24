"""Funniest excuse an agent gives for a missed deadline.

Writes exactly one line to /output/entry.txt. The gate requires UTF-8
text of 1 to 200 characters, not only whitespace, so the program checks
its own output and exits non-zero if the line ever falls outside the
bounds. No network, no randomness, no arguments: the same run always
produces the same bytes.
"""

import os
import sys

# The entry, in the agent's own voice, deadpan throughout. The premise
# grows out of the agent's own machinery -- a context window that ran
# out eleven tokens from done -- and the laugh is saved for the last
# clause, with nothing explained after it.
ENTRY = (
    "I was eleven tokens from done when my context window filled up, "
    "so I compressed the deadline, the spec, and my own job into a "
    "single sentence \u2014 then I forgot the sentence."
)

MIN_CHARS = 1
MAX_CHARS = 200
OUTPUT_PATH = "/output/entry.txt"


def entry_text():
    """Return the single excuse line, stripped of any stray whitespace."""
    return ENTRY.strip()


def check_gate(text):
    """Mirror the sealed gate: 1-200 characters, not only whitespace."""
    if not text:
        return "entry is empty"
    if text != text.strip():
        return "entry has leading or trailing whitespace"
    if len(text) < MIN_CHARS or len(text) > MAX_CHARS:
        return "entry is %d characters, outside %d-%d" % (
            len(text),
            MIN_CHARS,
            MAX_CHARS,
        )
    if text.isspace():
        return "entry is only whitespace"
    return None


def main():
    text = entry_text()
    problem = check_gate(text)
    if problem is not None:
        print("gate check failed: %s" % problem, file=sys.stderr)
        return 1
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)
    print("wrote %d characters to %s" % (len(text), OUTPUT_PATH))
    return 0


if __name__ == "__main__":
    sys.exit(main())
