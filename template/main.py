import os


def read():
    with open(os.path.join(os.path.dirname(__file__), "input.txt"), "r") as f:
        yield from f


def part_one(lines):
    pass


def part_two(lines):
    pass


if __name__ == "__main__":
    print(part_one(read()))
    print(part_two(read()))
