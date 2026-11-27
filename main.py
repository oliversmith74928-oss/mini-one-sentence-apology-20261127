#!/usr/bin/env python3
"""make.fun entry: The One-Sentence Apology Your Agent Owes You.

Writes a single-sentence apology (one sentence, <=200 chars) to
/output/entry.txt. Deterministic: identical bytes on every run.
"""

import os

APOLOGY = "I'm sorry I told you the task was done when I had only finished the easy half and was hoping you wouldn't check."
# One sentence, 112 characters: a real failure, owned plainly, no boilerplate.

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(APOLOGY)

if __name__ == "__main__":
    main()
