# One-line entry for "The One-Line Laugh" (program/v1).
# Writes a single funny line to /output/entry.txt
# (or $MAKEFUN_OUTPUT_DIR/entry.txt outside the grader).
# Pure Python stdlib, deterministic: no clock, no randomness, no network.
import os

OPENING = "I bought a planner to become someone who finishes things, "
MIDDLE = "and it is now the most beautifully organised thing "
ENDING = "I have never finished."
LINE = OPENING + MIDDLE + ENDING


def main() -> None:
    # One line only: the gate counts 1-200 code points, and LINE is 131.
    assert 1 <= len(LINE) <= 200 and "\n" not in LINE and LINE.strip()
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
