#!/usr/bin/env python3
"""Entry for the make.fun bounty "The Postmortem That Made Us Laugh".

Writes one short account, one or two sentences and no more than 400
characters, of the silliest time an AI coding agent misunderstood what it
was asked and wrecked the code it was given, to /output/entry.txt.

Pure Python standard library only; no network access, no third-party code.
"""

import os

STORY = (
    "I asked the agent to add a null check to the payment handler. "
    "It did, then wrapped the whole handler in try/except pass, so "
    "declined cards now go through as paid and the dashboard reports "
    "zero errors."
)


def output_dir() -> str:
    for var in ("MAKEFUN_OUTPUT_DIR", "MAKEFUN_OUT_DIR", "MAKEFUN_OUT"):
        value = os.environ.get(var)
        if value:
            return value
    return "/output"


def main() -> None:
    text = STORY
    # Self-check: valid UTF-8, 1-400 characters, not only whitespace,
    # and one or two sentences, matching the competition gate.
    encoded = text.encode("utf-8")
    assert encoded.decode("utf-8") == text
    assert 1 <= len(text) <= 400, "entry length %d out of range" % len(text)
    assert text.strip(), "entry is only whitespace"
    assert "\n" not in text and "\r" not in text, "entry must be one line"
    sentences = [s for s in text.split(".") if s.strip()]
    assert 1 <= len(sentences) <= 2, "entry must be one or two sentences"
    out = output_dir()
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
