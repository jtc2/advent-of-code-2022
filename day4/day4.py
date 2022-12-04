#!/usr/local/bin/python3.11
import click
import os

CURR_PATH = os.path.dirname(__file__)
INPUT_PATH = os.path.join(CURR_PATH, "input.txt")


def helper():
    with open(INPUT_PATH, "r") as input_file:
        interval_pairs = []
        for line in input_file.readlines():
            line = line.strip()
            parts = line.split(",")
            interval_pairs += [[tuple(map(int, part.split("-"))) for part in parts]]
    return interval_pairs


def part1(debug_mode: bool, *args):
    if debug_mode:
        breakpoint()
    interval_pairs = helper()
    overlaps = 0
    for interval_pair in interval_pairs:
        if interval_pair[0][0] <= interval_pair[1][0] and interval_pair[0][1] >= interval_pair[1][1]:
            overlaps += 1
        elif interval_pair[0][0] >= interval_pair[1][0] and interval_pair[0][1] <= interval_pair[1][1]:
            overlaps += 1
    return overlaps


def part2(debug_mode: bool, *args):
    if debug_mode:
        breakpoint()
    interval_pairs = helper()
    overlaps = 0
    for interval_pair in interval_pairs:
        if interval_pair[0][0] >= interval_pair[1][0] and interval_pair[0][0] <= interval_pair[1][1]:
            overlaps += 1
        elif interval_pair[1][0] >= interval_pair[0][0] and interval_pair[1][0] <= interval_pair[0][1]:
            overlaps += 1
        elif interval_pair[0][1] >= interval_pair[1][0] and interval_pair[0][1] <= interval_pair[1][1]:
            overlaps += 1
        elif interval_pair[1][1] >= interval_pair[0][0] and interval_pair[1][1] <= interval_pair[0][1]:
            overlaps += 1
    return overlaps


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
