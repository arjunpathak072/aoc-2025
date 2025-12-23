import sys

points = [
    (int(x), int(y))
    for x, y in [line.split(",") for line in sys.stdin.read().splitlines()]
]

ans = 0
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        x_diff = abs(points[i][0] - points[j][0]) + 1
        y_diff = abs(points[i][1] - points[j][1]) + 1
        ans = max(ans, x_diff * y_diff)

        print(f"{points[i]=}, {points[j]=}, area={x_diff * y_diff}")

print(ans)
