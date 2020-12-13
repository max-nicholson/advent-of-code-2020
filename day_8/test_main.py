import pytest


from .main import part_one, part_two

PROGRAM = """\
nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6"""

def test_part_one():

    assert part_one(PROGRAM.splitlines()) == 5


def test_part_two():
    assert part_two(PROGRAM.splitlines()) == 8
