import sys
from typing import List


def parse_command(containers: List[List[str]], command: str) -> None:
    _, qty, _, source, _, dest = command.split()
    source_idx = int(source) - 1
    dest_idx = int(dest) - 1
    for _ in range(int(qty)):
        containers[dest_idx].append(containers[source_idx].pop())


def parse_command2(containers: List[List[str]], command: str) -> None:
    _, qty, _, source, _, dest = command.split()
    source_idx = int(source) - 1
    dest_idx = int(dest) - 1
    temp = [containers[source_idx].pop() for _ in range(int(qty))]
    containers[dest_idx].extend(temp[::-1])


def main(filename: str):
    with open(filename, "r") as fp:
        lines = [line for line in fp.readlines()]

        # parse container starting position
        container_pos_delimiter = " 1   2   3   4   5   6   7   8   9 \n"
        line_map = [
            i for i, char in enumerate(container_pos_delimiter) if char.isnumeric()
        ]
        containers = [[] for _ in line_map]
        for line in lines[: lines.index(container_pos_delimiter)]:
            i: int
            c: str
            for i, c in filter(lambda x: x[1].isalpha(), enumerate(line)):
                containers[line_map.index(i)].append(c)

        containers = [container[::-1] for container in containers]

        for line in lines[10:]:
            # change to parse_command2 for part 2
            parse_command(containers, line)

        print("".join(container.pop() for container in containers))


if __name__ == "__main__":
    main(sys.argv[1])
