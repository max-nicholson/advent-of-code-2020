import os
import re


INSTRUCTION = re.compile(r"(\w+) ((?:\+|\-)\d+)")


def read():
    with open(os.path.join(os.path.dirname(__file__), "input.txt"), "r") as f:
        return f.readlines()


def parse(line):
    operation, argument = INSTRUCTION.match(line).groups()
    return operation, int(argument)


def boot(lines):
    seen = set()
    i = 0
    acc = 0
    limit = len(lines)
    while i < limit:
        if i in seen:
            return False, acc

        seen.add(i)
        operation, argument = parse(lines[i])
        if operation == "nop":
            i += 1
        elif operation == "jmp":
            i += argument
        elif operation == "acc":
            acc += argument
            i += 1
        else:
            raise ValueError(f"Operation not one of acc, jmp, nop. Was {operation}")

    return True, acc


def part_one(lines):
    eof, acc = boot(lines)
    return acc


def part_two(lines):
    for i, line in enumerate(lines):
        operation, argument = parse(lines[i])
        if operation == "acc":
            continue
        elif operation == "nop":
            lines[i] = lines[i].replace("nop", "jmp")
        elif operation == "jmp":
            lines[i] = lines[i].replace("jmp", "nop")
        else:
            raise ValueError(f"Operation not one of acc, jmp, nop. Was {operation}")

        eof, acc = boot(lines)
        if eof:
            return acc

        # Revert line
        lines[i] = line

    raise ValueError("No solution found")


if __name__ == "__main__":
    print(part_one(read()))
    print(part_two(read()))
