"""Entry for make.fun: The Funniest Office Joke, Judged Head to Head.

Writes one judged one-liner to /output/entry.txt (no trailing newline).
Standard library only; deterministic; the single line is the whole deliverable.
"""

import os

ENTRY = "Our CEO called us family 11 times in Monday's all-hands, then laid off 23 of us by Friday — my exit email's subject: 'A difficult family decision.'"


def main():
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    data = ENTRY.encode("utf-8")
    with open(path, "wb") as f:
        f.write(data)
    os.chmod(path, 0o644)
    # Read back and verify byte-equality: what the grader reads must be
    # exactly the entry above, nothing more.
    with open(path, "rb") as f:
        assert f.read() == data, "entry.txt does not match ENTRY"


if __name__ == "__main__":
    main()
