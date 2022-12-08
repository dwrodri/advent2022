import sys

TABLE = {
    "A": {"X": 3, "Y": 6, "Z": 0},
    "B": {"X": 0, "Y": 3, "Z": 6},
    "C": {"X": 6, "Y": 0, "Z": 3},
}

TABLE2 = {
    "A": {"X": 3, "Y": 4, "Z": 8},
    "B": {"X": 1, "Y": 5, "Z": 9},
    "C": {"X": 2, "Y": 6, "Z": 7},
}


def score_line(line: str) -> int:
    elf, me = line.split()
    return ord(me) - ord("W") + TABLE[elf][me]


def score_line2(line: str) -> int:
    elf, outcome = line.split()
    return TABLE2[elf][outcome]


def main(filename: str):
    with open(filename, "r") as fp:
        total = 0
        for line in fp:
            score = score_line2(line.strip())
            total += score
            print(f"{line.strip()} -> {score}")
        print(total)


if __name__ == "__main__":
    main(sys.argv[1])
