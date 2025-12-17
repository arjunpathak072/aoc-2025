import sys

grid = [col for col in [list(row) for row in sys.stdin.read().splitlines()]]
col_groups = [""] * max(len(row) for row in grid)

for row in grid:
    for idx, col in enumerate(row):
        col_groups[idx] = col_groups[idx] + col

ans = 0
numbers = []
operation = "+"

for dirty_str_num in col_groups:
    if not dirty_str_num.strip():
        res = 0
        for num in numbers:
            res = (res * num if res else num) if operation == "*" else res + num
        ans += res

        numbers, operation = [], "+"
        continue

    clean_str_num = dirty_str_num
    if dirty_str_num.count("*"):
        clean_str_num = dirty_str_num.replace("*", "")
        operation = "*"
    elif dirty_str_num.count("+"):
        clean_str_num = dirty_str_num.replace("+", "")

    numbers.append(int(clean_str_num.strip()))

res = 0
for num in numbers:
    res = (res * num if res else num) if operation == "*" else res + num
ans += res


print(ans)
