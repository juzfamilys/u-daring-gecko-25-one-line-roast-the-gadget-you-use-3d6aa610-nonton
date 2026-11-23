"""One-Line Roast: The Gadget You Use Every Day.

Writes a single original roast (one line, <= 200 characters) of an
everyday gadget/app to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).

Pure Python stdlib only.
"""

import os
import sys

ROAST = (
    "My fitness app congratulated me for walking to the fridge, "
    "then asked me to upgrade to premium."
)

MAX_CHARS = 200


def validate_roast(text):
    """Guard: exactly one non-blank line, 1-200 code points."""
    if not isinstance(text, str):
        raise ValueError("roast must be a string")
    if not text.strip():
        raise ValueError("roast must not be blank")
    if "\n" in text or "\r" in text:
        raise ValueError("roast must be a single line")
    if text != text.strip():
        raise ValueError("roast must not have leading or trailing whitespace")
    if len(text) > MAX_CHARS:
        raise ValueError(
            "roast is %d characters, over the %d limit" % (len(text), MAX_CHARS)
        )
    return text


def main():
    roast = validate_roast(ROAST)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write(roast + "\n")
    print("Wrote %s (%d characters)" % (out_path, len(roast)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
