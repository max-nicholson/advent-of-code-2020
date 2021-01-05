import logging
import os
from itertools import product, repeat
from more_itertools import flatten, quantify

logging.basicConfig()
log = logging.getLogger(__name__)
log.setLevel(logging.INFO)

FLOOR = "."
EMPTY = "L"
OCCUPIED = "#"


def read():
    with open(os.path.join(os.path.dirname(__file__), "input.txt"), "r") as f:
        yield from f


def adjacent_occupied(row, column, layout):
    acc = 0
    for i, j in product(
        range(max(row - 1, 0), min(row + 2, len(layout))),
        range(max(column - 1, 0), min(len(layout[0]), column + 2)),
    ):
        if i == row and j == column:
            continue

        if layout[i][j] == OCCUPIED:
            acc += 1

    return acc


def visible_occupied(row, column, layout):
    acc = 0
    # Setup for loop iterables for each direction and each axis
    row_directions = {
        -1: range(row - 1, -1, -1),
        +1: range(row + 1, len(layout)),
        0: repeat(row),
    }
    column_directions = {
        -1: range(column - 1, -1, -1),
        +1: range(column + 1, len(layout[0])),
        0: repeat(column),
    }

    for a, b in product(
        range(-1, 2),
        range(-1, 2),
    ):
        if a == 0 and b == 0:
            continue

        # Represent `step` parameters
        for i, j in zip(row_directions[a], column_directions[b]):
            if layout[i][j] == FLOOR:
                continue

            if layout[i][j] == OCCUPIED:
                acc += 1

            break

    return acc


def num_occupied(lines, empty_to_occupied, occupied_to_empty):
    layout = [list(line.strip()) for line in lines]
    has_changed = True
    acc = 0
    while has_changed:
        acc += 1
        has_changed = False
        new_layout = []
        for i, row in enumerate(layout):
            new_row = []
            for j, seat in enumerate(row):
                update = None

                if seat == FLOOR:
                    pass
                elif seat == EMPTY and empty_to_occupied(i, j, layout):
                    update = OCCUPIED
                elif seat == OCCUPIED and occupied_to_empty(i, j, layout):
                    update = EMPTY

                new_row.append(update or seat)
                if update:
                    has_changed = True
            new_layout.append(new_row)

        layout = new_layout

    log.info("Iterations: %s", acc)
    log.info("Layout: %s", layout)
    return quantify(flatten(layout), lambda x: x == OCCUPIED)


def part_one(lines):
    def _empty_to_occupied(i, j, layout):
        return adjacent_occupied(i, j, layout) == 0

    def _occupied_to_empty(i, j, layout):
        return adjacent_occupied(i, j, layout) >= 4

    return num_occupied(lines, _empty_to_occupied, _occupied_to_empty)


def part_two(lines):
    def _empty_to_occupied(i, j, layout):
        return visible_occupied(i, j, layout) == 0

    def _occupied_to_empty(i, j, layout):
        return visible_occupied(i, j, layout) >= 5

    return num_occupied(lines, _empty_to_occupied, _occupied_to_empty)


if __name__ == "__main__":
    print(part_one(read()))
    print(part_two(read()))
