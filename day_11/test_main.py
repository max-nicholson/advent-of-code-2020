import pytest

from .main import part_one, part_two


EXAMPLE = """\
L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL"""


def test_part_one():
    assert part_one(EXAMPLE.splitlines()) == 37


def test_part_two():
    assert part_two(EXAMPLE.splitlines()) == 26
