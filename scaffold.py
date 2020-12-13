#!/usr/bin/env python

import argparse
import shutil


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("day", type=int, choices=range(1, 32))

    args = parser.parse_args()
    day = args.day

    # TODO get input using requests. Need to authenticate first before hitting URL

    shutil.copytree("template", f"day_{day}")
    print(f"Day {day} setup")


if __name__ == "__main__":
    main()
