#!/usr/local/bin/python3.11
import click
import os

CURR_PATH = os.path.dirname(__file__)
INPUT_PATH = os.path.join(CURR_PATH, "input.txt")


def helper(split: bool):
    with open(INPUT_PATH, "r") as input_file:
        split_rucksacks = []
        for line in input_file.readlines():
            line = line.strip()
            if split:
                split_pos = len(line) // 2
                split_rucksacks.append((line[:split_pos], line[split_pos:]))
            else:
                split_rucksacks.append(line)
    return split_rucksacks


def part1(debug_mode: bool, *args):
    if debug_mode:
        breakpoint()
    total = 0
    rucksacks = helper(split=True)
    for r in rucksacks:
        common_letter: str = set(list(r[0])).intersection(set(list(r[1]))).pop()
        if common_letter.islower():
            total += ord(common_letter) - ord("a") + 1
        else:
            total += ord(common_letter) - ord("A") + 27
    return total


def part2(debug_mode: bool, *args):
    if debug_mode:
        breakpoint()
    rucksacks = helper(split=False)
    total = 0
    for i in range(0, len(rucksacks), 3):
        first_rucksack = rucksacks[i]
        second_rucksack = rucksacks[i + 1]
        third_rucksack = rucksacks[i + 2]
        common_letter = (
            set(list(first_rucksack))
            .intersection(set(list(second_rucksack)))
            .intersection(set(list(third_rucksack)))
            .pop()
        )
        if common_letter.islower():
            total += ord(common_letter) - ord("a") + 1
        else:
            total += ord(common_letter) - ord("A") + 27
    return total


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
