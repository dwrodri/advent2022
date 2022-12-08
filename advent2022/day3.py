import sys
from collections import Counter


def char_to_priority(char: str) -> int:
    table = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return table.find(char) + 1


def get_shared_item(rucksack: str) -> str:
    upper, lower = rucksack[: len(rucksack) // 2], rucksack[len(rucksack) // 2 :]
    overlap = set(upper).intersection(set(lower)).pop()
    return overlap


def sort_string(s: str) -> str:
    return "".join(sorted(s))


def get_shared_item2(first: str, second: str, third: str) -> str:
    print("\n".join(map(sort_string, [first, second, third])))
    overlap = set(first).intersection(set(second)).intersection(set(third)).pop()
    print(overlap)
    print("")
    return overlap


def part2(filename: str):
    with open(filename, "r") as fp:
        lines = [line.strip() for line in fp]
        total = 0
        counter = 0
        for i in range(0, len(lines), 3):
            total += char_to_priority(get_shared_item2(*lines[i : i + 3]))
            counter += 1
        print(counter, total)


def part1(filename: str):
    with open(filename, "r") as fp:
        print(sum(char_to_priority(get_shared_item(rucksack)) for rucksack in fp))


def main(filename: str):
    part2(filename)


if __name__ == "__main__":
    main(sys.argv[1])
