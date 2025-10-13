# https://adventofcode.com/2024/day/19

import doctest


def your_function(file: str):
    """
    Example input:
        r, wr, b, g, bwu, rb, gb, br

        brwrr
        bggr
        gbbr
        rrbgbr
        ubwu
        bwurrg
        brgr
        bbrgwb

    Task:
        Load patterns (first line)
        Load designs (from the third line)
        Match patterns to designs and count valid designs.

    Example:
        brgr can be made with br, g, and r.
        bbrgwb is impossible.

    >>> your_function("input.txt")
    6
    >>> your_function("input_full.txt")
    272
    """
    with open(file, "r") as f:
        input_data = f.readlines()

    # YOUR CODE HERE


def your_function_harder(file: str):
    """
    Example input:
        r, wr, b, g, bwu, rb, gb, br

        brwrr
        bggr
        gbbr
        rrbgbr
        ubwu
        bwurrg
        brgr
        bbrgwb

    Task:
        Load patterns (first line)
        Load designs (from the third line)
        Match patterns to designs and count how many valid designs can be created (output is the sum).

    Example:
        brgr can be made in two different ways: b, r, g, r or br, g, r. -> 2
        bbrgwb is impossible. -> 0

    >>> your_function("input.txt")
    16
    >>> your_function("input_full.txt")
    1041529704688380
    """
    with open(file, "r") as f:
        input_data = f.readlines()

    # YOUR CODE HERE


if __name__ == "__main__":
    import time

    start = time.time()
    doctest.testmod()
    end = time.time()
    print(f"Doctests completed in {end - start:.2f} seconds.")
