"""One-Line Roast: The Gadget You Use Every Day - one roast of a daily gadget.

The joke is built from a setup and a punch so the turn lands at the very
end: the earbuds fail exactly when they are needed, then come back at the
worst possible moment. Running this program writes the finished line,
unchanged, to /output/entry.txt.

Gate for this bounty: UTF-8 text, 1 to 200 characters, not only white
space, a single line with no trailing filler.
"""

from pathlib import Path

# The setup: the earbuds drop out the second a call comes in.
SETUP = (
    "My earbuds disconnect the second I answer a call, "
    "then reconnect just in time"
)

# The punch: they return only to play the music out loud to everyone.
PUNCH = "to play my music to the entire bus."

# One line, one space between setup and punch, nothing wasted.
ENTRY = " ".join([SETUP, PUNCH])

OUTPUT = Path("/output/entry.txt")
MAX_CHARS = 200


def validated_entry() -> str:
    """Return the entry only if it passes this bounty's gate.

    The gate is checked piece by piece so a failure names the rule it
    broke instead of failing silently at grading time.
    """
    text = ENTRY
    assert isinstance(text, str), "entry must be text"
    length = len(text)
    assert 1 <= length <= MAX_CHARS, f"entry length {length} out of gate"
    assert text.strip() == text and text.strip(), "no padding, not blank"
    assert "\n" not in text and "\r" not in text, "entry must be one line"
    # Craft rule from the judge's brief: the roast must clearly target a
    # gadget used every day, and the punch must land at the end.
    assert text.startswith("My earbuds"), "must roast a daily gadget"
    assert text.endswith("the entire bus."), "punch must land at the end"
    text.encode("utf-8")  # raises if the entry is not encodable as UTF-8
    return text


def main() -> None:
    text = validated_entry()
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(text, encoding="utf-8")
    # Determinism check: the bytes on disk are the entry, exactly, so
    # the grader's second run writes the same file as the first.
    on_disk = OUTPUT.read_bytes()
    assert on_disk.decode("utf-8") == text
    assert len(on_disk) == len(text.encode("utf-8"))


if __name__ == "__main__":
    main()
