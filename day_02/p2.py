import sys


def solve(start: str, end: str) -> int:
    invalid_ids_sum = 0

    for num in range(int(start), int(end) + 1):
        str_num = str(num)
        subsets = [str_num[:i] for i in range(1, len(str_num))]
        for subset in subsets:
            chunks = [
                str_num[i : i + len(subset)]
                for i in range(0, len(str_num), len(subset))
            ]
            if len(set(chunks)) == 1 and len(chunks) >= 2:
                invalid_ids_sum += num
                break

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
