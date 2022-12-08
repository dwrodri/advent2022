import sys
from typing import Set


def range_string_to_set(r: str) -> Set[int]:
    start, end = map(int, r.split("-"))
    return set(range(start, end + 1))


def fully_contains(line) -> bool:
    first, second = map(range_string_to_set, line.split(","))
    return first.issubset(second) or second.issubset(first)


def any_contains(line) -> bool:
    first, second = map(range_string_to_set, line.split(","))
    return first.isdisjoint(second)


def main(filename: str):
    with open(filename, "r") as fp:
        print(sum(1 for line in fp if not any_contains(line)))


if __name__ == "__main__":
    main(sys.argv[1])
