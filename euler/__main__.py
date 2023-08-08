# -*- coding: utf-8 -*-
"""
Run any of the implemented problem solutions via commandline.
"""
import argparse
import importlib
import pkgutil
import re
import sys
from typing import Optional

import euler
from euler.scraper import Problem


def _euler_solve(args: argparse.Namespace) -> None:
    for number in args.problems:
        solution = importlib.import_module(f"euler.problem_{number}")
        solve = getattr(solution, "solve", None)
        if callable(solve):
            solve()
        else:
            raise AttributeError(
                f"Solution {solution!r} does not provide a solve method"
            )


def _euler_scrape(args: argparse.Namespace) -> None:
    for number in args.problems:
        for path in Problem.from_number(number).scrape():
            print(f" -- Created: '{path!s}'")


def _euler_list(args: argparse.Namespace) -> None:
    module_re = re.compile(r"^problem_(?P<number>\d+)$")
    modules: list[tuple[int, str]] = []
    for _, name, is_pkg in pkgutil.iter_modules(path=euler.__path__):
        if not is_pkg and (match := module_re.fullmatch(name)):
            modules.append((int(match.group("number")), name))
    for number, name in sorted(modules):
        if args.verbose:
            print(name)
        else:
            print(number, end=" ")


def main(args: Optional[list[str]] = None) -> int:
    if args is None:
        args = sys.argv[1:]
    # Top-level parser
    parser = argparse.ArgumentParser(prog="EULER")
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="print extra information",
    )
    subparsers = parser.add_subparsers()

    # Solution parser
    parser_solve = subparsers.add_parser(
        "solve",
        help="run completed problem solutions",
    )
    parser_solve.add_argument(
        "problems",
        type=int,
        nargs="+",
        help="problem numbers to run",
    )
    parser_solve.set_defaults(func=_euler_solve)

    # Scraper parser
    parser_scrape = subparsers.add_parser(
        "scrape",
        help="scrape data for unsolved problems",
    )
    parser_scrape.add_argument(
        "problems",
        type=int,
        nargs="+",
        help="problem numbers to scrape",
    )
    parser_scrape.set_defaults(func=_euler_scrape)

    # List parser
    parser_list = subparsers.add_parser(
        "list",
        help="list information about solution modules",
    )
    parser_list.set_defaults(func=_euler_list)

    # Execution
    _args = parser.parse_args(args)
    _args.func(_args)
    return 0


if __name__ == "__main__":
    sys.exit(main())
