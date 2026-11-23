#!/usr/bin/env python3
"""The Vacuum's Alibi: One Line, 200 Characters.

Writes exactly one line — the funniest excuse a robot vacuum can
give for missing a spot — to /output/entry.txt.

The line: "The crumb presented diplomatic credentials, so I left it
alone. I am not starting an international incident over 0.4 grams
of biscuit." The punch lands on the exact weight — 0.4 grams — the
kind of needless precision a deadpan machine would file in its log.

Plain static writer: no network, no secrets, no dynamic code,
no reads outside this file.
"""

import os

LINE = (
    "The crumb presented diplomatic credentials, so I left it alone. "
    "I am not starting an international incident over 0.4 grams of biscuit."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
