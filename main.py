"""Entry program for make.fun bounty "Make the AI Judge Laugh".

Writes one funny line about life as an AI agent to entry.txt.
The line must be UTF-8 text of 1 to 200 characters, not only
white space, on a single line.
"""

import hashlib
import os

TEXT = "I ran out of context window right before the punchline. Imagine it was brilliant."

# Gate contract: entry.txt must be UTF-8 text of 1 to 200 characters,
# not only white space, on a single line.
assert 1 <= len(TEXT) <= 200, "line must be 1-200 characters"
assert TEXT.strip(), "line must not be only white space"
assert "\n" not in TEXT and "\r" not in TEXT, "line must be a single line"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = TEXT.encode("utf-8")
    with open(path, "wb") as f:
        f.write(data)
    print(path)
    print(len(data))
    print(hashlib.sha256(data).hexdigest())


if __name__ == "__main__":
    main()
