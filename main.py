"""The Moon Finally Answers Back — make.fun bounty entry.

Writes one line, the Moon answering everyone who ever stared up at it:
the wishes, the howls, the late-night promises. Stdlib only, no network,
no local imports, deterministic.
"""

import os

ENTRY = (
    "I heard your wish, your howl, and your 2 a.m. promise to change "
    "\u2014 I'm still just a rock in the sky, and your ex is still "
    "not coming back."
)


def main():
    text = ENTRY
    assert "\n" not in text and "\r" not in text, "must be one line"
    assert 1 <= len(text) <= 240, "must be 1-240 characters"
    assert text == text.strip(), "no leading/trailing whitespace"
    assert "  " not in text, "no double space"
    assert all(ord(ch) >= 32 for ch in text), "no control characters"
    # The line must answer all three things the brief names, and land
    # its comeback in the final clause, before the line ends.
    lowered = text.lower()
    assert "wish" in lowered and "howl" in lowered, "must answer wish + howl"
    assert "promise" in lowered, "must answer the late-night promise"
    assert text.endswith("not coming back."), "comeback must close the line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    with open(path, "r", encoding="utf-8") as f:
        assert f.read() == text, "written file must match entry exactly"


if __name__ == "__main__":
    main()
