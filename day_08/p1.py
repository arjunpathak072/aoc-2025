import sys
from math import sqrt


def calc_dist(x: int, y: int, z: int, x1: int, y1: int, z1: int) -> float:
    return sqrt((x - x1) ** 2 + (y - y1) ** 2 + (z - z1) ** 2)


class DSU:
    def __init__(self, vertex: int):
        self.parent = list(range(vertex + 2))
        self.size = [1] * (vertex + 1)
        self.parent[vertex + 1] = vertex

    def find_set(self, v: int) -> int:
        if v == self.parent[v]:
            return v
        self.parent[v] = self.find_set(self.parent[v])
        return self.parent[v]

    def union_sets(self, a: int, b: int) -> int | None:
        a, b = self.find_set(a), self.find_set(b)
        if a != b:
            if self.size[a] < self.size[b]:
                a, b = b, a
            self.parent[b] = a
            self.size[a] += self.size[b]

            return self.size[a]
        return None


points = [
    (int(x), int(y), int(z))
    for x, y, z in (row.split(",") for row in sys.stdin.read().splitlines())
]

edges = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        edges.append((calc_dist(*points[i], *points[j]), i, j))
edges.sort()

dsu = DSU(len(points))
for dist, u, v in edges[:1000]:
    if dsu.union_sets(u, v) == len(points):
        print(points[u][0] * points[v][0])

sizes = [dsu.size[i] for i in range(len(points)) if dsu.parent[i] == i]
sizes.sort(reverse=True)
assert len(sizes) >= 3
print(sizes[0] * sizes[1] * sizes[2])
