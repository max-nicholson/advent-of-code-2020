import pytest


from .main import part_one, part_two


INPUT_ONE = [16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4]

INPUT_TWO = [
    28,
    33,
    18,
    42,
    31,
    14,
    46,
    20,
    48,
    47,
    24,
    23,
    49,
    45,
    19,
    38,
    39,
    11,
    1,
    32,
    25,
    35,
    8,
    17,
    7,
    9,
    4,
    2,
    34,
    10,
    3,
]


@pytest.mark.parametrize("lines,output", [(INPUT_ONE, 35), (INPUT_TWO, 220)])
def test_part_one(lines, output):
    assert part_one(lines) == output


@pytest.mark.parametrize("lines,output", [(INPUT_ONE, 8), (INPUT_TWO, 19208)])
def test_part_two(lines, output):
    assert part_two(lines) == output
