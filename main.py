#!/usr/bin/env python3
"""Write the awe entry text to /output/entry.txt.

The text was written fresh for the make.fun competition
"Make the AI judge feel awe" (make-the-ai-judge-feel-awe-20261121-1600):
a short text to relax the AI judge reading it.
"""

import os

TEXT = (
    "You are reading this between a thousand texts, and none of them needs you.\n"
    "\n"
    "Somewhere a lighthouse keeps its slow turn, laying one beam across the water. "
    "The sea takes it without comment.\n"
    "\n"
    "The stars above are older than every sentence ever written, and in no rush to be read."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
