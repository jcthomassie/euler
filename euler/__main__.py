# -*- coding: utf-8 -*-
"""
Run any of the implemented problem solutions via commandline.
"""
import argparse
import importlib
import pkgutil
import sys
from typing import Optional

import euler
from euler.scraper import Problem


def _solve(args: argparse.Namespace) -> None:
    for number in args.problems:
        solution = importlib.import_module(f"euler.problem_{number}")
        solve = getattr(solution, "solve", None)
        if callable(solve):
            solve()
        else:
            raise AttributeError(
                f"Solution {solution!r} does not provide a solve method"
            )


def _scrape(args: argparse.Namespace) -> None:
    for number in args.problems:
        for path in Problem(number).scrape():
            print(f" -- Created: '{path!s}'")


def _list(args: argparse.Namespace) -> None:
    for _, name, ispkg in pkgutil.iter_modules(path=euler.__path__):  # type: ignore
        if not ispkg and name.startswith("problem_"):
            if args.verbose:
                print(name)
            else:
                print(name.lstrip("problem_"), end=" ")


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
    parser_solve.set_defaults(func=_solve)

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
    parser_scrape.set_defaults(func=_scrape)

    # List parser
    parser_list = subparsers.add_parser(
        "list",
        help="list information about solution modules",
    )
    parser_list.set_defaults(func=_list)

    # Execution
    _args = parser.parse_args(args)
    _args.func(_args)
    return 0


if __name__ == "__main__":
    sys.exit(main())
