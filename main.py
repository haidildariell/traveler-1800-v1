"""One Sentence for a Traveler from 1800 - a make.fun bounty entry.

Writes a single sentence to /output/entry.txt explaining the modern
internet to a man who has just arrived from the year 1800, using only
things he already knows: a post office, letters, books, a parlour.
"""

import os

# The sentence is assembled from its three clauses: the letters, the
# books, and the arguing strangers - one unbroken picture of a post
# office that holds the whole world.
CLAUSES = [
    "Imagine a post office where every letter ever written arrives in a single breath",
    "where any man may read any book ever printed",
    "and strangers argue with the whole world from their parlour chairs.",
]


def sentence():
    return ", ".join(CLAUSES)


def write_entry(text):
    for out_dir in ("/output", os.path.join(".", "output")):
        try:
            os.makedirs(out_dir, exist_ok=True)
            path = os.path.join(out_dir, "entry.txt")
            with open(path, "w", encoding="utf-8") as handle:
                handle.write(text)
            return path
        except OSError:
            continue
    raise OSError("no writable output directory found")


def main():
    write_entry(sentence())


if __name__ == "__main__":
    main()
