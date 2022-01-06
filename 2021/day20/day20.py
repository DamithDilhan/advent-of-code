from __future__ import annotations


def square2bin(content: list):
    l = len(content) - 1
    value = 0
    for pixel in content:
        if pixel == ".":
            l -= 1
        else:
            value += 2 ** l
            l -= 1

    return value


def get_square(image: list, x: int, y: int, padding: str):
    r_bound = len(image)
    c_bound = len(image[0])

    square = []

    for r in range(-1, 2):
        for c in range(-1, 2):
            if (x + r < 0 or x + r >= r_bound) or (y + c < 0 or y + c >= c_bound):
                square.append(padding)

            else:
                square.append(image[x + r][y + c])

    return square


def getOutput(im_algo: list, image: list, padding: str):
    new_image = []
    for row in range(len(image)):
        new_row = []
        for col in range(len(image[0])):
            square = get_square(image, row, col, padding)
            new_row.append(im_algo[square2bin(square)])
        new_image.append(new_row)

    return new_image


def display(image: list):
    for r in image:
        print("".join(r))


def enlarge(image: list, algo: list, iter=0):
    col_len = len(image[0]) + 2

    if (iter % 2 != 0) and algo[0] == "#" and algo[-1] == ".":
        padding = "#"
    else:
        padding = "."

    template = [[padding] * col_len]

    for row in image:
        template.append([padding] + row + [padding])

    template.append([padding] * col_len)

    return getOutput(algo, template, padding)


def countLitPixels(image: list):
    count = 0
    for row in image:
        for col in row:
            if col == "#":
                count += 1

    return count


if __name__ == "__main__":
    with open("input.txt", "r") as fp:
        content = fp.read().splitlines()

    im_algo = content[0]
    image = [list(i) for i in content[2:]]
    part1 = 0
    for i in range(0, 50):
        image = enlarge(image, im_algo, i)
        if i == 1:
            part1 = countLitPixels(image)

    print(f"part 1 solution {part1} part 2 solution {countLitPixels(image)}")

