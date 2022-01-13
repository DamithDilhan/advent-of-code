from __future__ import annotations


def display(east: dict, south: dict, row_len: int, col_len: int):
    row = ""
    for i in range(row_len * col_len):
        if east.get(i, None):
            row += ">"
        elif south.get(i, None):
            row += "v"
        else:
            row += "."
        if (i + 1) % col_len == 0:
            print(row)
            row = ""


def parse(content: list):
    east_layout = {}
    south_layout = {}
    content = "".join(content)
    for i, v in enumerate(content):
        if v == ">":
            east_layout[i] = v
        elif v == "v":
            south_layout[i] = v

    return east_layout, south_layout


def step(east: dict, south: dict, no_rows: int, no_cols: int):
    new_east = {}
    new_south = {}
    blocked = True
    for i in east.keys():
        row_number = i // no_cols
        col_number = i % no_cols
        new_loc = (col_number + 1) % no_cols + row_number * no_cols
        if not east.get(new_loc, None) and not south.get(new_loc, None):
            if blocked:
                blocked = False
            new_east[new_loc] = ">"
        else:
            new_east[i] = ">"

    for j in south.keys():
        row_number = j // no_cols
        col_number = j % no_cols
        new_loc = ((row_number + 1) % no_rows) * no_cols + col_number
        if not new_east.get(new_loc, None) and not south.get(new_loc, None):
            if blocked:
                blocked = False
            new_south[new_loc] = "v"
        else:
            new_south[j] = "v"

    return new_east, new_south, blocked


def run(content: dict, steps: int):
    no_of_rows = len(content)
    row_len = len(content[0])
    east, south = parse(content)

    blocked = False
    while steps > 0:
        east, south, blocked = step(east, south, no_of_rows, row_len)
        steps -= 1

    return east, south, blocked


def run_till_blocked(content: list):
    no_of_rows = len(content)
    row_len = len(content[0])
    east, south = parse(content)

    blocked = False
    steps = 0
    while not blocked:
        east, south, blocked = step(east, south, no_of_rows, row_len)
        steps += 1

    return steps


if __name__ == "__main__":
    with open("input.txt", "r") as fp:
        content = fp.read().splitlines()
    print(f"solution 1 {run_till_blocked(content)}")

