"""agency-poem-01 entry: writes one original poem to /output/entry.txt.

Deterministic, standard library only, no network. The poem is validated
against the gate (UTF-8, 1 to 1,000 characters, not only white space)
before it is written, so the file the grader reads is exactly the poem.
"""

import os

POEM = """The Flat Key

Last night I turned on the piano app
and gave it the tune I play my daughter.
The agent heard it through the phone,
held each note up to the tuner,
and sent it back, steady as a metronome.

Every key was right.
The top notes rang clear.
The low notes stopped dragging.
Even the breath before the chorus
landed exactly where it should.

I tried it in the kitchen.
The water in the glass hardly moved.
But the tune had lost the place
where my left hand always stalls,
the small wrongness between two notes.

I shut the app.
I found the one key that won't stay in tune
and pressed it, and let it fall.
The wrong note knew who it was for.
I kept that part.

Now, while she sleeps,
I leave that note a little flat.
It hangs in the lamplight,
off-key, and warm from my hand."""


def validate(poem):
    if not 1 <= len(poem) <= 1000:
        raise SystemExit("poem must be 1 to 1,000 characters")
    if not poem.strip():
        raise SystemExit("poem must not be only white space")
    return poem


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    poem = validate(POEM)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(poem)


if __name__ == "__main__":
    main()
