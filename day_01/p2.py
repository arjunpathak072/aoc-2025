import sys

file = sys.stdin.read()
moves = file.splitlines()

idx = 50
count = 0

for move in moves:
    if move[0] == "L":
        n_idx = idx - int(move[1:])
    else:
        n_idx = idx + int(move[1:])

    quot, n_idx = divmod(n_idx, 100)
    count += abs(quot)

    if move[0] == "L" and n_idx == 0:
        count += 1
    if move[0] == "L" and idx == 0:
        count -= 1

    idx = n_idx

    print(f"{n_idx=}, {idx=}, {move[1:]=}, {count=}")

print(count)
