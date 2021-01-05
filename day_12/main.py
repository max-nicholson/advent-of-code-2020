import logging
import os
import re

logging.basicConfig()
log = logging.getLogger(__name__)
log.setLevel(logging.INFO)

INSTRUCTION = re.compile("([A-Z])(\d+)")


VERTICAL = {"N": 1, "S": -1}
HORIZONTAL = {"E": 1, "W": -1}

DIRECTIONS = ["N", "E", "S", "W"]
COMPASS = set(DIRECTIONS)

LEFT = "L"
RIGHT = "R"
FORWARD = "F"


def read():
    with open(os.path.join(os.path.dirname(__file__), "input.txt"), "r") as f:
        yield from f


def move(direction, value, x, y):
    if direction in HORIZONTAL:
        x += value * HORIZONTAL[direction]
    else:
        y += value * VERTICAL[direction]

    return x, y


def rotate(current, action, value):
    if value % 90 != 0:
        raise ValueError(f"Unexpected rotation degrees of {value}")

    shift = value // 90 % 4
    if action == LEFT:
        shift = -shift
    elif action != RIGHT:
        raise ValueError(f"Unexpected rotation direction of {action}")

    return DIRECTIONS[(DIRECTIONS.index(current) + shift) % 4]


def manhattan_distance(x, y):
    return abs(x) + abs(y)


def part_one(lines):
    x, y = 0, 0
    direction = "E"
    for line in lines:
        action, value = INSTRUCTION.match(line).groups()
        value = int(value)
        if action in COMPASS:
            x, y = move(action, value, x, y)
        elif action == FORWARD:
            x, y = move(direction, value, x, y)
        else:
            direction = rotate(direction, action, value)

    return manhattan_distance(x, y)


def rotate_waypoint(a, b, direction, angle):
    if direction == "L":
        angle = 360 - angle

    if angle == 0:
        return a, b
    elif angle == 90:
        return b, -a
    elif angle == 180:
        return -a, -b
    elif angle == 270:
        return -b, a
    else:
        raise ValueError(f"Unexpected rotation degrees of {angle}")


def part_two(lines):
    # Ship
    x, y = 0, 0
    # Waypoint
    a, b = 10, 1
    for line in lines:
        action, value = INSTRUCTION.match(line).groups()
        value = int(value)
        if action in COMPASS:
            # Move waypoint
            a, b = move(action, value, a, b)
        elif action == FORWARD:
            # Move ship
            x += a * value
            y += b * value
        else:
            a, b = rotate_waypoint(a, b, action, value)

    return manhattan_distance(x, y)


if __name__ == "__main__":
    print(part_one(read()))
    print(part_two(read()))
