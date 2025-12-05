import sys

removed = 0


def print_grid(grid: list[list[str]]):
    for line in grid:
        print("".join(line))


def mark_index(grid: list[list[str]], r: int, c: int):
    if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[r]) or grid[r][c] == ".":
        return None

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
    count = 0
    row = grid[r]

    for n_delta in neighbour_deltas:
        neighbour = (r + n_delta[0], c + n_delta[1])
        if (
            neighbour[0] < 0
            or neighbour[0] >= len(grid)
            or neighbour[1] < 0
            or neighbour[1] >= len(row)
        ):
            continue
        if grid[neighbour[0]][neighbour[1]] == "@":
            count += 1

    if count < 4:
        grid[r][c] = "."
        global removed
        removed += 1
        for n_delta in neighbour_deltas:
            neighbour = (r + n_delta[0], c + n_delta[1])
            if (
                neighbour[0] < 0
                or neighbour[0] >= len(grid)
                or neighbour[1] < 0
                or neighbour[1] >= len(row)
            ):
                continue
            mark_index(grid, neighbour[0], neighbour[1])


def solve(grid: list[list[str]]) -> int:
    res = 0
    for r_idx, row in enumerate(grid):
        for c_idx, col in enumerate(row):
            mark_index(grid, r_idx, c_idx)

    print_grid(grid)
    print(removed)
    return res


if __name__ == "__main__":
    content = sys.stdin.read()
    count = 0
    lines = content.splitlines()
    grid = [list(line) for line in lines]
    solve(grid)
