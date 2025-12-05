import sys


def solve(ranges: list[tuple[int, int]], ids: list[int]) -> int:
    fresh_ids = 0
    for id in ids:
        for range in ranges:
            if range[0] <= id <= range[1]:
                print(f"{id=}")
                fresh_ids += 1
                break
    return fresh_ids


if __name__ == "__main__":
    ranges = []
    ids = []
    for line in sys.stdin.read().splitlines():
        if line.find("-") != -1:
            start, end = map(int, line.split("-"))
            ranges.append((start, end))
        elif line:
            ids.append(int(line))

    print(ids)
    print(ranges)
    print(solve(ranges, ids))
