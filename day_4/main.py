import os
import re

REQUIRED_FIELDS = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
KEY_PATTERN = re.compile("([a-z]{3}):\S+\s")
KEY_VALUE_PATTERN = re.compile("([a-z]{3}):(\S+)\s")

VALID_EYE_COLOURS = {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}
HAIR_COLOR_PATTERN = re.compile("#[0-9a-f]{6}")
PASSPORT_ID_PATTERN = re.compile("\d{9}")
HEIGHT_PATTERN = re.compile("(\d{3})cm|(\d{2})in")


def is_height_valid(height):
    match = HEIGHT_PATTERN.fullmatch(height)
    if not match:
        return False

    cm, inches = match.groups()
    if cm:
        return 150 <= int(cm) <= 193
    elif inches:
        return 59 <= int(inches) <= 76
    else:
        return False


VALIDATE = {
    "byr": lambda x: 1920 <= int(x) <= 2002,
    "iyr": lambda x: 2010 <= int(x) <= 2020,
    "eyr": lambda x: 2020 <= int(x) <= 2030,
    "hgt": is_height_valid,
    "hcl": lambda x: bool(HAIR_COLOR_PATTERN.fullmatch(x)),
    "ecl": lambda x: x in VALID_EYE_COLOURS,
    "pid": lambda x: bool(PASSPORT_ID_PATTERN.fullmatch(x)),
    "cid": lambda x: True,
}


def read():
    with open(os.path.join(os.path.dirname(__file__), "input.txt"), "r") as f:
        yield from f


def has_required_fields(passport):
    fields = KEY_PATTERN.findall(passport)
    return REQUIRED_FIELDS.issubset(fields)


def has_required_fields_and_valid_data(passport):
    valid_fields = set()
    for key, value in KEY_VALUE_PATTERN.findall(passport):
        if VALIDATE[key](value):
            valid_fields.add(key)

    return REQUIRED_FIELDS.issubset(valid_fields)


def count_valid(is_valid_func, iterable):
    valid = 0
    passport = []
    for line in iterable:
        if line == "\n":
            if is_valid_func("".join(passport)):
                valid += 1
            passport = []
            continue

        passport.append(line)

    # Edge case with no \n at EoF
    if passport and is_valid_func("".join(passport)):
        valid += 1

    return valid


def part_one():
    return count_valid(has_required_fields, read())


def part_two():
    return count_valid(has_required_fields_and_valid_data, read())


def test_part_one():
    assert (
        has_required_fields(
            """ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
            byr:1937 iyr:2017 cid:147 hgt:183cm
            \n"""
        )
        is True
    )
    assert (
        has_required_fields(
            """iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
            hcl:#cfa07d byr:1929
            \n"""
        )
        is False
    )
    assert (
        has_required_fields(
            """hcl:#ae17e1 iyr:2013
            eyr:2024
            ecl:brn pid:760753108 byr:1931
            hgt:179cm
            \n"""
        )
        is True
    )
    assert (
        has_required_fields(
            """hcl:#cfa07d eyr:2025 pid:166559648
            iyr:2011 ecl:brn hgt:59in
            \n"""
        )
        is False
    )


def test_part_two():
    invalid = """\
eyr:1972 cid:100
hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926

iyr:2019
hcl:#602927 eyr:1967 hgt:170cm
ecl:grn pid:012533040 byr:1946

hcl:dab227 iyr:2012
ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

hgt:59cm ecl:zzz
eyr:2038 hcl:74454a iyr:2023
pid:3556412378 byr:2007
"""

    valid = """\
pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
hcl:#623a2f

eyr:2029 ecl:blu cid:129 byr:1989
iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

hcl:#888785
hgt:164cm byr:2001 iyr:2015 cid:88
pid:545766238 ecl:hzl
eyr:2022

iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719
"""
    # NB: Need to add "\n" back onto each line after splitting for file-like input
    assert (
        count_valid(
            has_required_fields_and_valid_data,
            [f"{line}\n" for line in invalid.split("\n")],
        )
        == 0
    )
    assert (
        count_valid(
            has_required_fields_and_valid_data,
            [f"{line}\n" for line in valid.split("\n")],
        )
        == 4
    )
    assert VALIDATE["byr"]("2002") is True
    assert VALIDATE["byr"]("2003") is False

    assert VALIDATE["hgt"]("60in") is True
    assert VALIDATE["hgt"]("190cm") is True
    assert VALIDATE["hgt"]("190in") is False
    assert VALIDATE["hgt"]("190") is False

    assert VALIDATE["hcl"]("#123abc") is True
    assert VALIDATE["hcl"]("#123abz") is False
    assert VALIDATE["hcl"]("123abc") is False

    assert VALIDATE["ecl"]("brn") is True
    assert VALIDATE["ecl"]("wat") is False

    assert VALIDATE["pid"]("000000001") is True
    assert VALIDATE["pid"]("0123456789") is False


if __name__ == "__main__":
    test_part_one()
    print(part_one())
    test_part_two()
    print(part_two())
