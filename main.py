"""One-Line Roast: The Gadget You Use Every Day.

Writes a single roast line about a daily gadget to /output/entry.txt.
The line must be 1-200 UTF-8 characters, no trailing newline.
"""

import os
import sys

LINE = "My earbuds die at exactly 61% each, separately, like two coworkers who won't admit they're both quitting."


def main() -> int:
    line = LINE.strip()

    if "\n" in LINE or "\r" in LINE:
        print("error: roast line must be a single line (no newline characters)", file=sys.stderr)
        return 1

    if LINE != LINE.strip():
        print("error: roast line has leading or trailing whitespace", file=sys.stderr)
        return 1

    if not line:
        print("error: roast line is empty", file=sys.stderr)
        return 1

    length = len(line.encode("utf-8"))
    if length < 1 or length > 200:
        print(f"error: roast line is {length} UTF-8 chars, must be 1-200", file=sys.stderr)
        return 1

    os.makedirs("/output", exist_ok=True)
    tmp_path = "/output/.entry.txt.tmp"
    with open(tmp_path, "w", encoding="utf-8", newline="") as f:
        f.write(line)
    os.replace(tmp_path, "/output/entry.txt")

    print(f"wrote /output/entry.txt ({length} chars)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
