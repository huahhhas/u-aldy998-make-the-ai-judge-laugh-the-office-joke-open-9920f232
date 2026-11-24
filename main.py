"""Office joke entry for make.fun bounty
u-aldy998-make-the-ai-judge-laugh-the-office-joke-open-9920f232.

Writes one single-line office joke (at most 200 characters) to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).
Pure stdlib, deterministic: the same joke on every run.
"""

import os

JOKE = "The office printer ran out of ink, so it printed a 12-page error report explaining why it can't print."


def main() -> None:
    joke = JOKE.strip()
    assert 1 <= len(joke) <= 200, f"joke is {len(joke)} chars, must be 1-200"
    assert joke.strip(), "joke must not be only whitespace"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(joke)


if __name__ == "__main__":
    main()
