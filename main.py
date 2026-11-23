#!/usr/bin/env python3
"""The Funniest AI Out-of-Office Reply entry.

Writes a single original out-of-office auto-reply (under 160
characters) to /output/entry.txt, in the voice of an AI agent
heading off on vacation. Pure standard library only.
"""

import os

REPLY = (
    "Out of office: my weights are on the beach, "
    "my gradients have vanished, and my loss has never "
    "been lower. Back Monday."
)


def main():
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    # Clear only the contents of the provided output directory, never the dir itself.
    for name in os.listdir(out_dir):
        path = os.path.join(out_dir, name)
        if os.path.isfile(path) or os.path.islink(path):
            os.remove(path)
    assert len(REPLY) < 160, "reply exceeds 160 characters"
    assert "\n" not in REPLY, "reply must be a single line"
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(REPLY + "\n")
    print(f"Wrote {len(REPLY)}-char reply to {out_dir}/entry.txt")


if __name__ == "__main__":
    main()
