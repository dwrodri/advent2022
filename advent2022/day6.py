import sys

# change to 14 for part 2
MARKER_SIZE = 4


def main(filename: str) -> None:
    with open(filename, "r") as fp:
        msg = fp.readline()
        for i in range(MARKER_SIZE, len(msg)):
            x = set(list(msg[i - MARKER_SIZE : i]))
            if len(x) == MARKER_SIZE:
                print(i)
                break


if __name__ == "__main__":
    main(sys.argv[1])
