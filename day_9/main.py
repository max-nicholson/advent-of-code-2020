import os
from itertools import islice


def read():
    with open(os.path.join(os.path.dirname(__file__), "input.txt"), "r") as f:
        return [int(line.strip()) for line in f]


def part_one(lines, size):
    heap = set(lines[:size])

    for i in range(size, len(lines)):
        num = lines[i]
        if num >= max(heap) * 2:
            return num

        for j in heap:
            if num - j in heap:
                break
        else:
            return num

        heap.remove(lines[i - size])
        heap.add(num)

    raise ValueError("No solution")


def part_two(lines, target):
    for i, num in enumerate(lines):
        tot = num
        for j in range(i + 1, len(lines)):
            tot += lines[j]
            if tot == target:
                series = lines[i : j + 1]
                return min(series) + max(series)
            elif tot > target:
                break

    raise ValueError("No solution")


if __name__ == "__main__":
    invalid_number = part_one(read(), 25)
    print(invalid_number)
    print(part_two(read(), invalid_number))
