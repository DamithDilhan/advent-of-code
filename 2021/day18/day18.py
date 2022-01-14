from __future__ import annotations
from functools import reduce


def parse_pairs(content: list):
    for line in content:
        iteration = iter(line)
        assert next(iteration) == "["
        yield number_recursion(iteration)


def number_recursion(iteration: iter):
    char = next(iteration)
    if char == "[":
        left = number_recursion(iteration)
        char = next(iteration)
    else:
        left, char = parse_number(char, iteration)
    assert char == ","
    char = next(iteration)
    if char == "[":
        right = number_recursion(iteration)
        char = next(iteration)
    else:
        right, char = parse_number(char, iteration)
    assert char == "]"
    return (left, right)


def parse_number(char: str, iteration: iter):
    n = 0
    while char.isnumeric():
        n = n * 10 + int(char)
        char = next(iteration)

    return n, char


def reduce_number(char: tuple):
    reduced = False
    while not reduced:
        char, reduced, *_ = explode_pair(char, 0)
        if reduced:
            char, reduced = split_pair(char)
    return char


def explode_pair(char: int | tuple, depth: int):
    if not isinstance(char, int):
        left, right = char
        if depth >= 4:
            return 0, False, left, right
        else:
            left, reduced, explode_l, explode_r = explode_pair(left, depth + 1)

            if not reduced:
                if explode_r != 0:
                    right = add_left(right, explode_r)
                    explode_r = 0
            else:
                right, reduced, explode_l, explode_r = explode_pair(right, depth + 1)
                if explode_l != 0:
                    left = add_right(left, explode_l)
                    explode_l = 0

            if not reduced:
                return (left, right), False, explode_l, explode_r
    return char, True, 0, 0


def add_left(char: int | tuple, exp: int):
    if isinstance(char, int):
        return char + exp
    else:
        a, b = char
        return add_left(a, exp), b


def add_right(char: int | tuple, exp: int):
    if isinstance(char, int):
        return char + exp
    else:
        a, b = char
        return a, add_right(b, exp)


def split_pair(char: int | tuple):
    if isinstance(char, int):
        if char >= 10:
            a = char // 2
            return (a, char - a), False
    else:
        left, right = char
        left, reduced = split_pair(left)
        if reduced:
            right, reduced = split_pair(right)
        if not reduced:
            return (left, right), False
    return char, True


def add_pairs(pair_a, pair_b):
    return reduce_number((pair_a, pair_b))


def get_magnitude(snail_number: tuple):
    if isinstance(snail_number, int):
        return snail_number
    left, right = snail_number
    return 3 * get_magnitude(left) + 2 * get_magnitude(right)


def parse_snailnumber(content: list):
    snailnumbers = map(reduce_number, parse_pairs(content))
    return snailnumbers


def solve1(content: list):
    snail_number = parse_snailnumber(content)
    snail_number = reduce(add_pairs, snail_number)
    reduced_snailnumber = reduce(add_pairs, snail_number)
    print(f"solution 1 {get_magnitude(reduced_snailnumber)}")


def solve2(content: list):

    snail_number = parse_snailnumber(content)
    snail_number = list(map(reduce_number, snail_number))

    max_number = float("-inf")
    for i, pair1 in enumerate(snail_number):
        for j, pair2 in enumerate(snail_number):
            if i == j:
                continue
            new_max = get_magnitude(add_pairs(pair1, pair2))
            if new_max > max_number:
                max_number = new_max

    print(f"solution 2 {max_number}")


if __name__ == "__main__":
    with open("input.txt", "r") as fp:
        content = fp.read().splitlines()

    solve1(content)
    solve2(content)
