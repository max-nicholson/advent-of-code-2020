import pytest


from .main import part_one, part_two, rotate, rotate_waypoint

INSTRUCTIONS = """\
F10
N3
F7
R90
F11"""


@pytest.mark.parametrize(
    "direction,action,value, expected",
    [
        ("E", "R", 90, "S"),
        ("E", "L", 180, "W"),
        ("E", "L", 0, "E"),
        ("N", "L", 90, "W"),
    ],
)
def test_rotate(direction, action, value, expected):
    assert rotate(direction, action, value) == expected


def test_part_one():
    assert part_one(INSTRUCTIONS.splitlines()) == 25


@pytest.mark.parametrize(
    "waypoint,direction,angle,expected",
    [
        ((10, 4), "R", 90, (4, -10)),
        ((10, 4), "R", 0, (10, 4)),
        ((3, 2), "L", 90, (-2, 3)),
        ((3, 2), "L", 180, (-3, -2)),
        ((3, 2), "L", 270, (2, -3)),
    ],
)
def test_rotate(waypoint, direction, angle, expected):
    assert rotate_waypoint(waypoint[0], waypoint[1], direction, angle) == expected


def test_part_two():
    assert part_two(INSTRUCTIONS.splitlines()) == 286
