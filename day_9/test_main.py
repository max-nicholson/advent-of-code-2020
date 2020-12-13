import pytest


from .main import part_one, part_two


DATA = [
    35,
    20,
    15,
    25,
    47,
    40,
    62,
    55,
    65,
    95,
    102,
    117,
    150,
    182,
    127,
    219,
    299,
    277,
    309,
    576,
]


def test_part_one():
    assert part_one(DATA, 5) == 127


def test_part_two():
    assert part_two(DATA, 127) == 62
