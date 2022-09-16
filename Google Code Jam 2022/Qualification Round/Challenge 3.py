# t = int(input())
# answers = []
# for x in range(t):
#     n = int(input())
#     dice = str(input()).split()
#     for y in range(len(dice)):
#         dice[y] = int(dice[y])
#     dice.sort()
#     ans = 0
#     for z in range(1, len(dice) + 1):
#         if z > dice[z - 1] and z != dice[z - 1]:
#             continue
#         elif z <= dice[z - 1]:
#             ans += 1
#         else:
#             continue
#     answers.append(ans)

# for a in range(1, len(answers) + 1):
#     print(f"Case #{a}: {answers[a-1]}")

from __future__ import annotations


def _d1000000(dices: list[int]) -> int:
    """"""
    rev_sorted_dices = sorted(dices, reverse=True)
    while True:
        for i, d in zip(range(len(rev_sorted_dices), 0, -1), rev_sorted_dices):
            if i > d:
                break
        else:
            break
        rev_sorted_dices.pop()
    return len(rev_sorted_dices)


def _main() -> None:
    t = int(input())
    for i in range(1, t + 1):
        # `N` not needed
        int(input())
        dices = list(map(int, input().split()))
        length = _d1000000(dices)
        print(f"Case #{i}: {length}")


if __name__ == "__main__":
    _main()
