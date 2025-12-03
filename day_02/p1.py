import sys


def solve(start: str, end: str) -> int:
    invalid_ids_sum = 0

    for num in range(int(start), int(end) + 1):
        first_half = str(num)[0 : len(str(num)) // 2]
        second_half = str(num)[len(str(num)) // 2 :]

        if first_half == second_half:
            print(f"{num=}, {first_half=}, {second_half=}")
            invalid_ids_sum += num

    return invalid_ids_sum


if __name__ == "__main__":
    content = sys.stdin.read()
    total = 0

    for line in content.splitlines():
        for num_range in line.split(","):
            splits = num_range.split("-")
            if splits:
                start, end = splits[0], splits[1]
                total += solve(start, end)

    print(total)
