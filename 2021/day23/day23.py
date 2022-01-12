from __future__ import annotations
import heapq


def display(content: list):
    for row in content:
        print(row)


def parse(content: list, room_size: int):
    rooms = ["".join(i.split("#")).strip() for i in content[2 : 2 + room_size]]
    hallway = "".join(content[1].split("#")).strip()
    return "".join(map("".join, zip(*rooms))) + hallway


def get_door(room: int, room_size: int):
    return 4 * room_size + 2 * (room // room_size + 1)


def walk(src: int, dst: int):
    step = -1 if src > dst else 1
    return range(src + step, dst + step, step)


def change_state(state: str, a: int, b: int):
    if a > b:
        a, b = b, a
    return state[:a] + state[b] + state[a + 1 : b] + state[a] + state[b + 1 :]


def calculate_energy(index: str, distance: int):
    return distance * 10 ** "ABCD".index(index)


def check_hallway(state: str, door: int, room_size: int):
    doors = tuple(range(get_door(0, room_size), get_door(4 * room_size, room_size), 2))
    for end_pos in (4 * room_size, len(state) - 1):
        for pos, i in enumerate(walk(door, end_pos)):
            if state[i] != ".":
                break
            if i not in doors:
                yield pos + 1, i


def moves(state: str, room_size: int):
    for room, final in zip(range(0, 4 * room_size, room_size), "ABCD"):
        door = get_door(room, room_size)

        for pos, cell in enumerate(state[room : room + room_size]):
            if cell != ".":

                if cell != final or any(
                    state[room + i] != final for i in range(pos + 1, room_size)
                ):
                    for start, end in check_hallway(state, door, room_size):
                        yield start + pos + 1, room + pos, end
                break

    for hall in range(4 * room_size, len(state)):
        ap = state[hall]
        if ap != ".":
            room = "ABCD".index(ap) * room_size
            door = get_door(room, room_size)
            if all(state[i] == "." for i in walk(hall, door)):
                distance = abs(hall - door)
                for pos in range(room_size - 1, -1, -1):
                    cell = state[room + pos]
                    if cell == ".":
                        yield distance + pos + 1, hall, room + pos

                    elif cell != ap:
                        break


def solve(state: str, room_size):
    to_do = [(0, state)]
    done = {state: 0}

    final = "".join(x * room_size for x in "ABCD") + "." * 11

    while to_do:
        energy, state = heapq.heappop(to_do)

        if final == state:
            return energy
        for distance, src, dest in moves(state, room_size):
            new_state = change_state(state, src, dest)
            new_energy = energy + calculate_energy(state[src], distance)
            if done.get(new_state, float("inf")) > new_energy:
                # print(new_state)
                heapq.heappush(to_do, (new_energy, new_state))
                done[new_state] = new_energy


def solve1(content: list):
    state = parse(content, 2)
    print(f"solution 1 {solve(state, 2)}")


def solve2(content: list):
    content = content[:3] + ["  #D#C#B#A#  ", "  #D#B#A#C#  "] + content[3:]
    state = parse(content, 4)

    print(f"solution 2 {solve(state, 4)}")


if __name__ == "__main__":
    with open("input.txt", "r") as fp:
        content = fp.read().splitlines()

    solve1(content)
    solve2(content)

