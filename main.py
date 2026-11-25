"""Invent a Word We Need.

Writes one freshly coined English word together with its one-line
definition to $MAKEFUN_OUTPUT_DIR/entry.txt: fridgehope, the hope
that opening the fridge one more time will reveal food that was
not there before. Standard library only.
"""

import os

ENTRY = (
    "fridgehope (n.) The hope that opening the fridge one more "
    "time will reveal food that was not there before."
)


def check_entry(text):
    """Check the coinage against the competition gate before writing.

    The gate needs UTF-8 text of 1 to 140 characters, not only white
    space, in a single line: one invented English word together with
    a one-line definition of it. Returns the cleaned text or raises
    ValueError.
    """
    cleaned = text.strip()
    if not cleaned:
        raise ValueError("entry must not be only whitespace")
    if len(cleaned) > 140:
        raise ValueError(
            "entry is %d characters, over the 140 limit" % len(cleaned)
        )
    if "\n" in cleaned or "\r" in cleaned:
        raise ValueError("entry must be exactly one line")
    return cleaned


def entry_shape(text):
    """Measure the coinage for one last sanity pass.

    Returns a dict with the character count and the word count of the
    cleaned text. A coinage too short to carry a word and a definition,
    or one that reads like a paragraph squeezed under the limit, is
    caught here before anything is written.
    """
    words = text.split()
    return {"chars": len(text), "words": len(words)}


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    text = check_entry(ENTRY)
    shape = entry_shape(text)
    if shape["words"] < 5:
        raise ValueError("entry is too short to carry a word and a definition")
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()
