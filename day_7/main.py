from functools import lru_cache, wraps
from itertools import repeat
import os
import re

PATTERN = re.compile(r"\b((?!no other)[a-z]+ [a-z]+)\b bags?")
PARENT_PATTERN = re.compile("([a-z]+ [a-z]+) bags")
CHILD_PATTERN = re.compile(" (\d) ([a-z]+ [a-z]+) bags?")


class FrozenDict(dict):
    """Hashable dict, required for use with lru_cache"""

    def __init__(self, *args, **kwargs):
        self._hash = None
        super().__init__(*args, **kwargs)

    def __hash__(self):
        if self._hash is None:
            self._hash = hash(tuple(self.items()))
        return self._hash


def read():
    with open(os.path.join(os.path.dirname(__file__), "input.txt"), "r") as f:
        yield from f


def parse_children(rule):
    parent, *children = PATTERN.findall(rule)
    # frozenset for lru_cache
    return parent, frozenset(children)


def parse_number_of_children(rule):
    parent = PARENT_PATTERN.match(rule).groups()[0]
    children = dict(
        ((colour, int(count)) for count, colour in CHILD_PATTERN.findall(rule))
    )
    return parent, children


@lru_cache(maxsize=600)
def can_hold_shiny_gold(colour, rules) -> bool:
    if "shiny gold" in rules[colour]:
        return True
    elif not rules[colour]:
        return False

    return any(map(can_hold_shiny_gold, rules[colour], repeat(rules)))


def holds(colour, rules) -> int:
    children = rules[colour]
    if not children:
        return 0

    # +1 for self
    return sum((holds(child, rules) + 1) * count for child, count in children.items())


def part_one(rules):
    data = FrozenDict(map(parse_children, rules))
    return sum(map(can_hold_shiny_gold, data.keys(), repeat(data)))


def part_two(rules):
    data = dict(map(parse_number_of_children, rules))
    return holds("shiny gold", data)


if __name__ == "__main__":
    print(part_one(read()))
    print(part_two(read()))
