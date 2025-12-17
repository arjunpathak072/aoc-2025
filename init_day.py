import os
import sys

day_idx = "0" + sys.argv[1] if len(sys.argv[1]) == 1 else sys.argv[1]
day_path = f"./day_{day_idx}"

try:
    os.mkdir(day_path)
except FileExistsError:
    print(f"Day {day_idx} already exists.")

with open(f"{day_path}/p1.in", "a") as f:
    pass

with open(f"{day_path}/p2.in", "a") as f:
    pass

with open(f"{day_path}/p1.py", "a") as f:
    pass

with open(f"{day_path}/p2.py", "a") as f:
    pass
