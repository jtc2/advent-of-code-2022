#!/usr/local/bin/python3.11
import click
import os

CURR_PATH = os.path.dirname(__file__)
INPUT_PATH = os.path.join(CURR_PATH, "input.txt")


def get_calories_list() -> list[int]:
    with open(INPUT_PATH, "r") as file:
        curr_calories = 0
        calories_list = []
        for line in file.readlines():
            line = line.strip()
            if line == "":
                calories_list.append(curr_calories)
                curr_calories = 0
                continue
            curr_calories += int(line)
        calories_list.append(curr_calories)
    return calories_list


def part1(debug_mode: bool, *args):
    if debug_mode:
        breakpoint()

    return max(get_calories_list())


def part2(debug_mode: bool, *args):
    if debug_mode:
        breakpoint()
    calories_list = get_calories_list()
    first_max = max(calories_list)
    calories_list.remove(first_max)
    second_max = max(calories_list)
    calories_list.remove(second_max)
    third_max = max(calories_list)
    return first_max + second_max + third_max


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
