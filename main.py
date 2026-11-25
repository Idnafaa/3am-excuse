#!/usr/bin/env python3
"""The 3 AM Excuse — a hardware wallet refuses to sign at 3 AM.

The wallet speaks as a bouncer at last call: the hour is the joke,
not the battery, the firmware, or the cold storage.
"""

import os

EXCUSE = (
    "It's 3 AM \u2014 last call was hours ago, so I'm not letting your "
    "coins leave with a stranger called 'just one more trade'."
)


def main() -> None:
    line = EXCUSE.strip()
    if not line or len(line) > 200 or "\n" in line or "\r" in line:
        raise SystemExit("entry failed the gate: must be 1-200 chars, one line")
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    with open(target, "w", encoding="utf-8") as fh:
        fh.write(line)
    # Read it back: the file the judge sees must pass the same gate.
    with open(target, "r", encoding="utf-8") as fh:
        written = fh.read()
    if written != line or len(written) > 200:
        raise SystemExit("entry failed the gate after writing")


if __name__ == "__main__":
    main()
