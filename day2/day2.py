#!/usr/local/bin/python3.11
import click
import os

CURR_PATH = os.path.dirname(__file__)
INPUT_PATH = os.path.join(CURR_PATH, "input.txt")


WINS = [("A", "Y"), ("B", "Z"), ("C", "X")]

TIES = [("A", "X"), ("B", "Y"), ("C", "Z")]

PLAY_SCORE = {"X": 1, "Y": 2, "Z": 3}

WIN = 0
TIE = 1
LOSS = 2
MAPPING = {"A": ("Y", "X", "Z"), "B": ("Z", "Y", "X"), "C": ("X", "Z", "Y")}


def helper():
    with open(INPUT_PATH, "r") as input_file:
        plays = []
        for line in input_file.readlines():
            line = line.strip()
            plays.append(tuple(line.split(" ")))
    return plays


def part1(debug_mode: bool, *args):
    if debug_mode:
        breakpoint()
    plays = helper()

    score = 0
    for play in plays:
        score += PLAY_SCORE[play[1]]
        if play in WINS:
            score += 6
        elif play in TIES:
            score += 3
    return score


def part2(debug_mode: bool, *args):
    if debug_mode:
        breakpoint()
    plays = helper()

    score = 0
    for play in plays:
        idx = WIN
        if play[1] == "X":
            idx = LOSS
        elif play[1] == "Y":
            idx = TIE
        your_play = MAPPING[play[0]][idx]
        score += PLAY_SCORE[your_play]
        new_play = (play[0], your_play)
        if new_play in WINS:
            score += 6
        elif new_play in TIES:
            score += 3
    return score


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
