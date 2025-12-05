import sys


def solve(grid: list[list[str]]) -> int:
    res = 0
    neighbour_deltas = [
        (-1, 0),
        (0, 1),
        (1, 1),
        (-1, -1),
        (0, -1),
        (1, 0),
        (-1, 1),
        (1, -1),
    ]
    for r_idx, row in enumerate(grid):
        for c_idx, col in enumerate(row):
            count = 0
            if col == "@":
                for n_delta in neighbour_deltas:
                    neighbour = (r_idx + n_delta[0], c_idx + n_delta[1])
                    if (
                        neighbour[0] < 0
                        or neighbour[0] >= len(grid)
                        or neighbour[1] < 0
                        or neighbour[1] >= len(row)
                    ):
                        continue
                    if (
                        grid[neighbour[0]][neighbour[1]] == "@"
                        or grid[neighbour[0]][neighbour[1]] == "x"
                    ):
                        count += 1
                if count < 4:
                    grid[r_idx][c_idx] = "x"
                    res += 1

    for row in grid:
        print("".join(row))
    return res


if __name__ == "__main__":
    content = sys.stdin.read()
    count = 0
    lines = content.splitlines()
    grid = [list(line) for line in lines]
    print(solve(grid))
