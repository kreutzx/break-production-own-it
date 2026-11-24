"""Break Production, Own It — make.fun entry.

One line: the brutally honest error message an AI agent prints the moment
it breaks production. First-person confession, exact damage (3 a.m.,
412,000 rows), deadpan twist in the final clause: the user was me.
"""

import os

ENTRY_TEXT = "I dropped the production database at 3 a.m. — 412,000 rows gone — and logged it as 'user error: the user was me.'"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY_TEXT + "\n")


if __name__ == "__main__":
    main()
