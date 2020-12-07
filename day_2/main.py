import os
import re

PATTERN = re.compile("^(\d+)-(\d+) ([a-z]): ([a-z]+)$")

def passwords():
    with open(os.path.join(os.path.dirname(__file__), "input.txt"), "r") as f:
        for line in f:
            match = PATTERN.match(line).groups()
            yield int(match[0]), int(match[1]), match[2], match[3]

def part_one():
    valid = 0
    for min, max, letter, password in passwords():
        if max >= password.count(letter) >= min:
            valid += 1

    return valid


def part_two():
    valid = 0
    for first, second, letter, password in passwords():
        if (password[first - 1] == letter) ^ (password[second - 1] == letter):
            valid += 1

    return valid

if __name__ == "__main__":
    print(part_one())
    print(part_two())
