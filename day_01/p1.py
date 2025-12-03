import sys

file = sys.stdin.read()
moves = file.splitlines()

idx = 50

count = 0
for move in moves:
    if move[0] == "L":
        idx = (idx - int(move[1:])) % 100
    else:
        idx = (idx + int(move[1:])) % 100

    if idx == 0:
        count += 1

print(count)
