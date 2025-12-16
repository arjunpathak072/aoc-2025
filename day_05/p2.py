import sys


class Range:
    start: int
    end: int

    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end

    def __str__(self):
        return f"{self.start}-{self.end}"


def solve(ranges: list[Range]) -> int:
    ranges.sort(key=lambda x: x.start)
    merged_ranges = [ranges[0]]

    for range in ranges[1:]:
        if merged_ranges[-1].end < range.start:
            merged_ranges.append(range)
        else:
            merged_ranges[-1].end = max(merged_ranges[-1].end, range.end)

    fresh_ids = 0
    for range in merged_ranges:
        fresh_ids += range.end - range.start + 1

    return fresh_ids


if __name__ == "__main__":
    ranges = []
    ids = []
    for line in sys.stdin.read().splitlines():
        if line.find("-") != -1:
            start, end = map(int, line.split("-"))
            ranges.append(Range(start, end))
        elif line:
            ids.append(int(line))

    print(solve(ranges))
