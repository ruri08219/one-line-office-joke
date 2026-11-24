"""One-line office joke entry for make.fun.

Writes the joke to /output/entry.txt (UTF-8), then re-reads the file
and asserts the bytes round-trip exactly.
"""

from pathlib import Path

JOKE = "My calendar blocked 'focus time' so my manager booked over it with a meeting called 'Quick Sync About Focus Time.'"

MAX_CHARS = 200


def main() -> None:
    # Validate before writing: an invalid joke must fail without
    # creating or overwriting the output file.
    assert "\n" not in JOKE, "joke must be a single line"
    assert "\r" not in JOKE, "joke must be a single line"
    assert 1 <= len(JOKE) <= MAX_CHARS, "joke must be 1-200 chars"
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    data = JOKE.encode("utf-8")
    out.write_bytes(data)
    assert out.read_bytes() == data, "round-trip mismatch"


if __name__ == "__main__":
    main()
