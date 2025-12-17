import sys
from copy import deepcopy

grid = [col for col in [row for row in sys.stdin.read().splitlines()]][2:]

first_splitter_index = grid[0].find("^")
assert first_splitter_index != -1, "First row must have a splitter"

state = [0] * len(grid[0])
state[first_splitter_index] = 1


split_count = 0
for row in grid:
    next_state = deepcopy(state)
    for idx, x in enumerate(state):
        if x and row[idx] == "^":
            split_count += 1
            next_state[idx] = 0

            if idx + 1 < len(grid[0]):
                next_state[idx + 1] = next_state[idx + 1] or 1

            if idx - 1 >= 0:
                next_state[idx - 1] = next_state[idx - 1] or 1

    state = next_state

print(split_count)
