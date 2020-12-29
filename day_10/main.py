import logging
import os
from collections import Counter
from functools import lru_cache
from itertools import chain, islice, repeat, takewhile, tee

logging.basicConfig()
log = logging.getLogger(__name__)
log.setLevel(logging.INFO)


def read():
    with open(os.path.join(os.path.dirname(__file__), "input.txt"), "r") as f:
        yield from f


def differences(lines):
    jolts = sorted(chain([0], (int(line) for line in lines)))
    jolts.append(jolts[-1] + 3)

    adapters, copied_adapters = tee(jolts)
    next(copied_adapters)
    return (y - x for x, y in zip(adapters, copied_adapters))


def part_one(lines):
    data = Counter(differences(lines))
    return data.get(1) * data.get(3)


@lru_cache(None)
def path(i, adapters):

    log.debug(i)

    if i == len(adapters) - 1:
        return 1

    current = adapters[i]

    remaining_choices = islice(adapters, i + 1, None)

    valid_choices = (
        i + j
        for j, _ in enumerate(
            takewhile(lambda x: x - current <= 3, remaining_choices), start=1
        )
    )

    return sum(map(path, valid_choices, repeat(adapters)))


def part_two(lines):
    jolts = tuple(sorted(chain([0], (int(line) for line in lines))))

    return path(0, jolts)


if __name__ == "__main__":
    print(part_one(read()))
    print(part_two(read()))
    log.info(path.cache_info())
