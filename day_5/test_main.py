import pytest

from .main import Seat, part_one


@pytest.mark.parametrize(
    "boarding_pass,row",
    [
        ("FBFBBFFRLR", 44),
        ("BFFFBBFRRR", 70),
        ("FFFBBBFRRR", 14),
        ("BBFFBBFRLL", 102),
    ],
)
def test_row(boarding_pass, row):
    assert Seat(boarding_pass).row == row


@pytest.mark.parametrize(
    "boarding_pass,column",
    [
        ("FBFBBFFRLR", 5),
        ("BFFFBBFRRR", 7),
        ("FFFBBBFRRR", 7),
        ("BBFFBBFRLL", 4),
    ],
)
def test_column(boarding_pass, column):
    assert Seat(boarding_pass).column == column


@pytest.mark.parametrize(
    "boarding_pass,seat_id",
    [
        ("FBFBBFFRLR", 357),
        ("BFFFBBFRRR", 567),
        ("FFFBBBFRRR", 119),
        ("BBFFBBFRLL", 820),
    ],
)
def test_id(boarding_pass, seat_id):
    assert Seat(boarding_pass).id == seat_id


def test_part_one():
    assert part_one(["FBFBBFFRLR", "BFFFBBFRRR", "FFFBBBFRRR", "BBFFBBFRLL"]) == 820
