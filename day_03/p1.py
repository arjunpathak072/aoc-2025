import sys

file_content = sys.stdin.read()
lines = file_content.splitlines()

sum = 0
for line in lines:
    largest = 0
    for idx, battery in enumerate(line):
        if idx == len(line) - 1:
            continue
        for next_battery in line[idx + 1 :]:
            curr = int(battery) * 10 + int(next_battery)
            largest = max(largest, curr)
    print(f"{largest=}")
    sum = sum + largest


print(sum)
