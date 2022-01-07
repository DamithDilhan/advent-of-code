from __future__ import annotations
from functools import lru_cache


possible_values = {
    3: 1,
    4: 3,
    5: 6,
    6: 7,
    7: 6,
    8: 3,
    9: 1,
}


def solve1(start_pos: tuple):
    dice = 1
    playerA_score = 0
    playerB_score = 0
    playerA_pos = start_positions[0]
    playerB_pos = start_positions[1]
    iter_num = 0
    while playerA_score < 1000 and playerB_score < 1000:

        playerA_pos = (playerA_pos + (3 * (dice + 1)) - 1) % 10 + 1

        playerA_score += playerA_pos

        dice += 3
        iter_num += 3

        if playerA_score >= 1000:
            break
        playerB_pos = (playerB_pos + (3 * (dice + 1)) - 1) % 10 + 1

        playerB_score += playerB_pos

        dice += 3
        iter_num += 3

    print(f"solution 1 {min(playerA_score, playerB_score) * iter_num}")


def calculate_score(score: int, value: int):

    return (score - value - 1) % 10 + 1


@lru_cache(None)
def dp(end_pos: int, score: int, turn: int, pos: int):

    if turn == 0:
        return 1 if (score == 0 and end_pos == pos) else 0

    if score <= 0:
        return 0
    wins = 0
    for amount in possible_values:
        if score - end_pos >= 21:
            continue

        dp_val = dp(calculate_score(end_pos, amount), score - end_pos, turn - 1, pos)
        wins += possible_values[amount] * dp_val

    return wins


def num_of_wins(playerA: int, playerB: int, is_playerA: int):

    wins = 0
    for end_pos in range(1, 11):
        for score in range(21, 31):
            for turn in range(40):
                for b_end_pos in range(1, 11):
                    for b_score in range(21):
                        wins += dp(end_pos, score, turn, playerA) * dp(
                            b_end_pos,
                            b_score,
                            turn - 1 if is_playerA else turn,
                            playerB,
                        )

    return wins


def solve2(start_pos):
    p1, p2 = start_pos

    p1 = num_of_wins(p1, p2, True)
    p2 = num_of_wins(p2, p1, False)
    print(f"solution 2 {max(p1, p2)}")


if __name__ == "__main__":

    with open("input.txt", "r") as fp:
        content = fp.read().splitlines()

    start_positions = (int(content[0][-1]), int(content[1][-1]))
    solve1(start_positions)
    solve2(start_positions)

