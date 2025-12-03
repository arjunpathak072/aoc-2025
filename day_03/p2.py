import sys


def solve(
    curr_idx: int, to_pick: int, batteries: str, memo: dict[tuple[int, int], str]
) -> str:
    if to_pick == 0:
        return ""

    if (curr_idx, to_pick) in memo:
        return memo[(curr_idx, to_pick)]

    if curr_idx + 1 == len(batteries):
        return batteries[curr_idx]

    pick_val = batteries[curr_idx] + solve(curr_idx + 1, to_pick - 1, batteries, memo)

    remaining = len(batteries) - curr_idx
    not_pick_val = -1
    if remaining:
        not_pick_val = solve(curr_idx + 1, to_pick, batteries, memo)

    memo[(curr_idx, to_pick)] = str(max(int(pick_val), int(not_pick_val)))
    return str(max(int(pick_val), int(not_pick_val)))


print(sum)

if __name__ == "__main__":
    file_content = sys.stdin.read()
    res = 0
    for line in file_content.splitlines():
        curr_res = solve(0, 12, line, {})
        res += int(curr_res)

    print(res)
