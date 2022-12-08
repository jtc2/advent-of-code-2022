#!/usr/local/bin/python3.11
import click
import os

CURR_PATH = os.path.dirname(__file__)
INPUT_PATH = os.path.join(CURR_PATH, "input.txt")


def helper():
    starting_stacks = []
    moves = []
    with open(INPUT_PATH, "r") as input_file:
        for line in input_file.readlines():
            line = line.rstrip()
            if line.startswith("move"):
                parts = line.split(" ")
                moves.append((int(parts[1]), int(parts[3]) - 1, int(parts[5]) - 1))
            elif "[" in line:
                for idx in range(len(line)):
                    if line[idx] == "[":
                        letter = line[idx + 1]
                        col = idx // 4
                        while len(starting_stacks) < col + 1:
                            starting_stacks.append([])
                        starting_stacks[col].append(letter)
    for stack in starting_stacks:
        stack.reverse()
    return starting_stacks, moves


def part1(debug_mode: bool, *args):
    if debug_mode:
        breakpoint()
    starting_stacks, moves = helper()
    for move in moves:
        num_to_move = move[0]
        source_stack = move[1]
        ending_stack = move[2]
        for _ in range(num_to_move):
            letter = starting_stacks[source_stack].pop()
            starting_stacks[ending_stack].append(letter)

    result = ""
    for stack in starting_stacks:
        result += stack[-1]
    return result


def part2(debug_mode: bool, *args):
    if debug_mode:
        breakpoint()
    starting_stacks, moves = helper()
    for move in moves:
        num_to_move = move[0]
        source_stack = move[1]
        ending_stack = move[2]
        moving_letters = []
        for _ in range(num_to_move):
            moving_letters.append(starting_stacks[source_stack].pop())
        moving_letters.reverse()
        starting_stacks[ending_stack] += moving_letters

    result = ""
    for stack in starting_stacks:
        result += stack[-1]
    return result


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
