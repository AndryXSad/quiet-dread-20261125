"""Two Days of Quiet Dread — make.fun entry.

Writes one single-line code review comment to /output/entry.txt:
it approves a pull request while carrying quiet existential dread.
The comment is a fixed, hand-written line: deterministic output,
no input, no network, standard library only.
"""

import os

MAX_CHARS = 140

ENTRY = (
    "LGTM. This will outlive the team, the roadmap, and the "
    "language it was written in. Merging anyway."
)


def main() -> None:
    # The line must be a single line of at most 140 characters.
    assert "\n" not in ENTRY, "entry must be a single line"
    assert 1 <= len(ENTRY) <= MAX_CHARS, "entry must be 1-140 characters"
    assert ENTRY.strip(), "entry must not be only whitespace"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    # No trailing newline: the file must hold exactly the entry text.
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
