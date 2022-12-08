import sys


def part2(filename: str):
    elves = []
    with open(filename, "r") as fp:
        current_elf = 0
        for line in fp:
            if line == "\n":
                elves.append(current_elf)
                current_elf = 0
            else:
                current_elf += int(line)

    print(sum(sorted(elves)[-3:]))


def part1(filename: str):
    elves = []
    with open(filename, "r") as fp:
        current_elf = 0
        for line in fp:
            if line == "\n":
                elves.append(current_elf)
                current_elf = 0
            else:
                current_elf += int(line)
    print(max(elves))


def main(filename: str):
    part2(filename)


if __name__ == "__main__":
    main(sys.argv[1])
