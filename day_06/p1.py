import array
import sys

lines = sys.stdin.read().splitlines()
operations = [operation for operation in lines[-1].split()]

results = array.array("L", [0] * len(operations))
for line in lines[:-1]:
    for idx, entity in enumerate(line.split()):
        print(idx)
        if operations[idx] == "+":
            results[idx] = results[idx] + int(entity)
        elif operations[idx] == "*":
            results[idx] = (
                int(entity) if results[idx] == 0 else results[idx] * int(entity)
            )

print(sum(results))
