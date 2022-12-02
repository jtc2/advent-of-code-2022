#!/usr/local/bin/python3.11
import click
import os
from datetime import datetime
from dateutil.tz import gettz
from textwrap import dedent


@click.command()
@click.option("--day", "-d", default=datetime.now(gettz("America/New_York")).day, type=int, help="The day to use.")
def main(day: int):
    day_str = str(day)
    dir_path = "day" + day_str
    file_path = os.path.join(dir_path, "day" + day_str + ".py")
    if os.path.exists(dir_path):
        raise ValueError("Day already created")
    os.mkdir(dir_path)
    with open(file_path, "w") as day_file:
        day_file.write(
            dedent(
                """\
                #!/usr/local/bin/python3.11
                import click


                def part1(debug_mode: bool, *args):
                    if debug_mode:
                        breakpoint()
                    pass


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
                        part1(debug, *ctx.args)
                    elif part == 2:
                        part2(debug, *ctx.args)
                    else:
                        raise ValueError("Invalid part number")


                if __name__ == "__main__":
                    main()
                """
            )
        )


if __name__ == "__main__":
    main()
