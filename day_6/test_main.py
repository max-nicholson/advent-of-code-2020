import pytest

from .main import (
    common_answers,
    sum_of_common_answers,
    sum_of_unique_answers,
    unique_answers,
)


TEST_INPUT = """\
abc

a
b
c

ab
ac

a
a
a
a

b"""


@pytest.mark.parametrize(
    "group,unique",
    [
        (["abc"], 3),
        (["a", "b", "c"], 3),
        (["ab", "ac"], 3),
        (["a", "a", "a", "a"], 1),
        (["b"], 1),
    ],
)
def test_unique_answers(group, unique):
    assert unique_answers(group) == unique


@pytest.mark.parametrize(
    "group,common",
    [
        (["abc"], 3),
        (["a", "b", "c"], 0),
        (["ab", "ac"], 1),
        (["a", "a", "a", "a"], 1),
        (["b"], 1),
    ],
)
def test_common_answers(group, common):
    assert common_answers(group) == common


def test_sum_of_unique_answers():
    assert sum_of_unique_answers(TEST_INPUT.split("\n")) == 11


def test_sum_of_common_answers():
    assert sum_of_common_answers(TEST_INPUT.split("\n")) == 6
