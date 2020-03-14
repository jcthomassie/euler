"""
Run any of the implemented problem solutions via commandline.
"""
import argparse
import importlib
import sys

def main(args=None):
    if args is None:
        args = sys.argv[1:]
    parser = argparse.ArgumentParser(description="Run Project Euler solutions.")
    parser.add_argument(
        "problem",
        type=int,
        help="problem number to run"
    )
    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="print extra information"
    )
    _args = parser.parse_args(args)
    solution = importlib.import_module(f"euler.problem_{_args.problem}")
    solution.solve()


if __name__ == "__main__":
    sys.exit(main())
