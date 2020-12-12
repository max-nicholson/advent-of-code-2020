from itertools import groupby
from typing import List
import os


def read():
    with open(os.path.join(os.path.dirname(__file__), "input.txt"), "r") as f:
        yield from f


def unique_answers(group: List[str]) -> int:
    return len(set(answer for person in group for answer in person))


def common_answers(group: List[str]) -> int:
    answers_by_person = (set(answers) for answers in group)
    common = set.intersection(*answers_by_person)
    return len(common)


def groups(lines):
    cleaned_lines = (line.rstrip() for line in lines)
    for not_empty, group in groupby(cleaned_lines, bool):
        if not_empty:
            yield group


def sum_of_unique_answers(lines):
    return sum(map(unique_answers, groups(lines)))


def sum_of_common_answers(lines):
    return sum(map(common_answers, groups(lines)))


def part_one(lines):
    return sum_of_unique_answers(lines)


def part_two(lines):
    return sum_of_common_answers(lines)


if __name__ == "__main__":
    print(part_one(read()))
    print(part_two(read()))
