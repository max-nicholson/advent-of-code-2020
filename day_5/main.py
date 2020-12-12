import os

ROWS = 128
COLUMNS = 8


def read():
    with open(os.path.join(os.path.dirname(__file__), "input.txt"), "r") as f:
        yield from f


class Seat:
    def __init__(self, boarding_pass):
        self.boarding_pass = boarding_pass
        self.row_id = boarding_pass[:7]
        self.column_id = boarding_pass[7:10]

    def __str__(self):
        return self.boarding_pass

    def binary_search(self, text, UPPER_CHAR, LOWER_CHAR, UPPER):
        lower, upper = 0, UPPER - 1
        for char in text:
            median = (upper + lower) // 2
            if char == UPPER_CHAR:
                upper = median
            elif char == LOWER_CHAR:
                lower = median + 1
            else:
                raise ValueError(
                    f"Character not {LOWER_CHAR} or {UPPER_CHAR}, was {char}"
                )

        return upper

    @property
    def row(self):
        return self.binary_search(self.row_id, "F", "B", ROWS)

    @property
    def column(self):
        return self.binary_search(self.column_id, "L", "R", COLUMNS)

    @property
    def id(self):
        return self.row * 8 + self.column


def part_one(lines):
    return max((Seat(boarding_pass).id for boarding_pass in lines))


def part_two(lines):
    occupied = set((Seat(boarding_pass).id for boarding_pass in lines))
    lower = 1 * 8 + 0
    upper = (ROWS - 2) * 8 + COLUMNS
    for i in range(lower, upper):
        if all((i not in occupied, i - 1 in occupied, i + 1 in occupied)):
            return i

    raise ValueError("No spaces")


if __name__ == "__main__":
    print(part_one(read()))
    print(part_two(read()))
