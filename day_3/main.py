import os
from itertools import islice
from math import prod

MAP = []
with open(os.path.join(os.path.dirname(__file__), "input.txt"), "r") as f:
    for row in f:
        MAP.append(row.rstrip())

def number_of_trees(right, down):
    overflow = len(MAP[0])
    col = right
    trees = 0
    for row in islice(MAP, down, None, down):
        if row[col] == "#":
            trees += 1

        col = (col + right) % overflow
    return trees

if __name__ == "__main__":
    print(number_of_trees(3, 1))
    print(
        prod((
            number_of_trees(1, 1),
            number_of_trees(3, 1),
            number_of_trees(5, 1),
            number_of_trees(7, 1),
            number_of_trees(1, 2),
        ))
    )
