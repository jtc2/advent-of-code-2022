#!/usr/local/bin/python3.11
import click
import os

CURR_PATH = os.path.dirname(__file__)
INPUT_PATH = os.path.join(CURR_PATH, "input.txt")


def helper():
    with open(INPUT_PATH, "r") as input_file:

        for line in input_file.readlines():
            line = line.strip()
            return line


def part1(debug_mode: bool, *args):
    if debug_mode:
        breakpoint()
    line = helper()
    for i in range(len(line) - 13):
        slice = line[i : i + 14]  # noqa
        if len(set(list(slice))) == 14:
            return i + 13 + 1


def part2(debug_mode: bool, *args):
    if debug_mode:
        breakpoint()
    pass


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
