from __future__ import annotations


def solve(instructions: list, highest: bool = True):
    op1 = []
    op2 = []
    for step in range(0, len(instructions), 18):
        if instructions[step + 4].split(" ")[2] == "1":
            op1.append(int(instructions[step + 15].split(" ")[2]))
            op2.append(None)
        else:  # instructions[step +4].split(" ")[2] == "26"
            op2.append(int(instructions[step + 5].split(" ")[2]))
            op1.append(None)

    model_number = [0] * 14
    stack = []
    for i, (plus, minus) in enumerate(zip(op1, op2)):
        if plus:
            stack.append((i, plus))
        else:
            ia, a = stack.pop()
            if highest:
                model_number[ia] = min(9, 9 - (a + minus))
                model_number[i] = min(9, 9 + (minus + a))
            else:
                model_number[ia] = max(1, 1 - (a + minus))
                model_number[i] = max(1, 1 + (minus + a))

    return "".join(map(str, model_number))


def solve1(content: list):
    print(f"solution 1 {solve(content)}")


def solve2(content: list):
    print(f"solution 2 {solve(content,highest=False)}")


if __name__ == "__main__":
    with open("input.txt", "r") as fp:
        content = fp.read().splitlines()

    solve1(content)
    solve2(content)
