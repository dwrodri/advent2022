import sys
from typing import List, Tuple, Union, Generator


class FileObj:
    def __init__(self, name: str, size: str = "0", contents=[]) -> None:
        self.name = name
        self.size = int(size)
        self.contents: List[FileObj] = contents

    def get_size(self) -> int:
        calculated = self.size + sum(content.get_size() for content in self.contents)
        return calculated if calculated > 10000 or len(self.contents)== 0 else 0

def parse_line(line: str) -> FileObj:


def find_next_cd(lines: List[str]) -> int:
    for i, line in enumerate(lines):
        if line[:4] == "$ cd":
            return i
    return -1


def walk_cmd_history(lines: List[str]) -> Generator[Tuple[str, List[str]], None, None]:
    i = 0
    while 0 < i < len(lines):
        if "$ cd" == lines[i][:4]:
            yield lines[i].split()[-1], lines[i + 2 : find_next_cd(lines[i:])]
            i = find_next_cd(lines[i:])
            continue


def main(filename: str) -> None:
    with open(filename, "r") as fp:
        for batch in walk_cmd_history([line.strip() for line in fp.readlines()]):



if __name__ == "__main__":
    main(sys.argv[1])
