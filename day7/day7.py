#!/usr/local/bin/python3.11
import click
import math
import os
from copy import deepcopy
from dataclasses import dataclass, field
from typing import Optional


@dataclass
class File:
    name: str
    size: int


@dataclass
class Directory:
    directories: dict[str, list["Directory"]] = field(default_factory=dict)
    files: dict[str, list[File]] = field(default_factory=dict)
    path: list[str] = field(default_factory=list)
    parent: Optional["Directory"] = None
    total_size: int | None = None

    def size(self):
        if self.total_size is not None:
            return self.total_size
        total = 0
        for file in self.files.values():
            total += file.size
        for directory in self.directories.values():
            total += directory.size()
        self.total_size = total
        return total


CURR_PATH = os.path.dirname(__file__)
INPUT_PATH = os.path.join(CURR_PATH, "input.txt")

ROOT_DIRECTORY = Directory(path=["/"])
LIMIT = 100000


def helper():
    with open(INPUT_PATH, "r") as input_file:
        curr_directory = ROOT_DIRECTORY
        for line in input_file.readlines():
            line = line.strip()
            if line.startswith("$"):
                parts = line.split(" ")
                if parts[1] == "cd":
                    if parts[2] == "/":
                        curr_directory = ROOT_DIRECTORY
                    elif parts[2] == "..":
                        if curr_directory.parent is not None:
                            curr_directory = curr_directory.parent
                    else:
                        if parts[2] not in curr_directory.directories:
                            curr_directory.directories[parts[2]] = Directory(
                                path=deepcopy(curr_directory.path) + [parts[2]], parent=curr_directory
                            )
                        curr_directory = curr_directory.directories[parts[2]]
            elif line.startswith("dir"):
                parts = line.split(" ")
                if dir not in curr_directory.directories:
                    curr_directory.directories[dir] = Directory(
                        path=deepcopy(curr_directory.path) + [parts[1]], parent=curr_directory
                    )
            else:  # file
                parts = line.split(" ")
                size = int(parts[0])
                name = parts[1]
                if name not in curr_directory.files:
                    curr_directory.files[name] = File(name=name, size=size)
        return ROOT_DIRECTORY


def calculate_sizes(within_limits: list[Directory], curr: Directory) -> int:
    sum_size = 0
    for directory in curr.directories.values():
        sum_size += calculate_sizes(within_limits, directory)
    if curr.size() < LIMIT:
        within_limits.append(curr)
    return curr.size() + sum_size


def part1(debug_mode: bool, *args):
    if debug_mode:
        breakpoint()
    filesystem = helper()
    within_limits: list[Directory] = []
    calculate_sizes(within_limits, filesystem)
    return sum([dir.size() for dir in within_limits])


MAX_SIZE = 70000000
NEEDED_SIZE = 30000000


def part2(debug_mode: bool, *args):
    if debug_mode:
        breakpoint()
    filesystem = helper()
    total_size = filesystem.size()  # calculate sizes
    unused_size = MAX_SIZE - total_size
    if unused_size > NEEDED_SIZE:
        return None
    remaining_size = NEEDED_SIZE - unused_size
    candidate_size = math.inf
    stack = [ROOT_DIRECTORY]
    while len(stack) != 0:
        curr = stack.pop()
        if curr.size() > remaining_size and curr.size() < candidate_size:
            candidate_size = curr.size()
        stack += curr.directories.values()
    return candidate_size


@click.command(
    context_settings=dict(
        ignore_unknown_options=True,
        allow_extra_args=True,
    )
)
@click.option("--part", "-p", default=1, type=int, help="The part to run")
@click.option("--debug/--no-debug", "-d", default=False, type=bool, help="The part to run")
@click.pass_context
def main(ctx, part: int, debug: bool):
    if part == 1:
        print(part1(debug, *ctx.args))
    elif part == 2:
        print(part2(debug, *ctx.args))
    else:
        raise ValueError("Invalid part number")


if __name__ == "__main__":
    main()
