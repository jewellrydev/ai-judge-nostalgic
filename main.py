"""Make the AI Judge Feel Nostalgic: A Childhood Memory — a make.fun entry.

Prints exactly one sentence, at most 280 characters, that brings back
a childhood memory.
"""

LINE = (
    "Grandma's kitchen at dusk: rice steaming, the radio crackling, "
    "and her pretending not to notice me stealing the crispy bits "
    "before dinner."
)


def build_line() -> str:
    line = LINE
    assert len(line) <= 280, f"line too long: {len(line)} chars"
    assert "\n" not in line
    return line


if __name__ == "__main__":
    print(build_line())
