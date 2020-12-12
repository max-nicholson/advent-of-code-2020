import pytest

from .main import holds, parse_children, parse_number_of_children, part_one, part_two

TEST_INPUT = """light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags."""


@pytest.mark.parametrize(
    "rule, parent, children",
    [
        (
            "bright white bags contain 1 shiny gold bag.",
            "bright white",
            {"shiny gold"},
        ),
        (
            "muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.",
            "muted yellow",
            {"shiny gold", "faded blue"},
        ),
        ("faded blue bags contain no other bags.", "faded blue", set()),
    ],
)
def test_parse_children(rule, parent, children):
    assert parse_children(rule) == (parent, children)


def test_part_one():
    assert part_one(TEST_INPUT.split("\n")) == 4


@pytest.mark.parametrize(
    "rule, parent, total_children",
    [
        (
            "bright white bags contain 1 shiny gold bag.",
            "bright white",
            {"shiny gold": 1},
        ),
        (
            "muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.",
            "muted yellow",
            {"shiny gold": 2, "faded blue": 9},
        ),
        ("faded blue bags contain no other bags.", "faded blue", {}),
    ],
)
def test_parse_number_of_children(rule, parent, total_children):
    assert parse_number_of_children(rule) == (parent, total_children)


@pytest.mark.parametrize(
    "colour, total",
    [
        ("faded blue", 0),
        ("dotted black", 0),
        ("vibrant plum", 11),
        ("dark olive", 7),
        ("shiny gold", 32),
    ],
)
def test_holds(colour, total):
    rules = {
        "bright white": {"shiny gold": 1},
        "dark olive": {"dotted black": 4, "faded blue": 3},
        "dark orange": {"bright white": 3, "muted yellow": 4},
        "dotted black": {},
        "faded blue": {},
        "light red": {"bright white": 1, "muted yellow": 2},
        "muted yellow": {"faded blue": 9, "shiny gold": 2},
        "shiny gold": {"dark olive": 1, "vibrant plum": 2},
        "vibrant plum": {"dotted black": 6, "faded blue": 5},
    }
    assert holds(colour, rules) == total


def test_part_two():
    assert part_two(TEST_INPUT.split("\n")) == 32
