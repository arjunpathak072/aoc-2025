import sys
from functools import lru_cache

grid = [col for col in [row for row in sys.stdin.read().splitlines()]]

first_splitter_index = grid[0].find("S")
assert first_splitter_index != -1, "First row must have a splitter"


@lru_cache
def solve(row_idx, col_idx):
    if row_idx == len(grid):
        return 1

    if grid[row_idx][col_idx] != "^":
        return solve(row_idx + 1, col_idx)

    right, left = 0, 0

    # if there is a splitter and we can go right
    if col_idx + 1 < len(grid[0]):
        right = solve(row_idx + 1, col_idx + 1)

    # if there is a splitter and we can go left
    if col_idx - 1 >= 0:
        left = solve(row_idx + 1, col_idx - 1)

    return right + left


print(solve(0, first_splitter_index))
