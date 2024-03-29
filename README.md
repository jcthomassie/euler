# euler

[![tests](https://github.com/jcthomassie/euler/workflows/tests/badge.svg)](https://github.com/jcthomassie/euler/actions)
[![codecov](https://codecov.io/gh/jcthomassie/euler/branch/master/graph/badge.svg)](https://codecov.io/gh/jcthomassie/euler)

Collection of solutions to [Project Euler](https://projecteuler.net/) problems.
Each module contains a solution to a single problem. Any necessary data for
solutions is included in the euler/data directory.

## Installation

Install using [poetry](https://python-poetry.org/docs/#installation):

```s
poetry install
```

**Note**: The `euler solve` command copies the solution to your clipboard using [pyperclip](https://pypi.org/project/pyperclip/). Some platforms may require an additional dependency for this to work (e.g. [xclip](http://manpages.ubuntu.com/manpages/xenial/man1/xclip.1.html) for Ubuntu).

## Usage

Installing the package adds the `euler` entry point.

To solve already completed problems:

```s
euler solve 45 54
[0.08013 sec]    euler.problem_45.solve()       = 1533776805
[0.04725 sec]    euler.problem_54.solve()       = 376
```

To scrape any missing data for problems:

```s
euler scrape 133
 -- Created: 'c:\\users\\jthom\\code\\euler\\euler\\problem_133.py'
 -- Created: 'c:\\users\\jthom\\code\\euler\\tests\\test_problem_133.py'
```
