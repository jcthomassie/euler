# euler

Collection of solutions to [Project Euler](https://projecteuler.net/) problems.
Each module contains a solution to a single problem. Any necessary data for
solutions is included in the euler/data directory.

## Installation

Clone the repository:

```console
$ git clone https://<USERNAME>@github.com/jcthomassie/euler.git
```

Install the package and all requirements for development:

```console
$ pip install -r requirements.txt
$ pip install -e .[dev]
```

**Note**: The solve function automatically copies the solution value to your clipboard using [pyperclip](https://pypi.org/project/pyperclip/). If you are on Linux, [xclip](http://manpages.ubuntu.com/manpages/xenial/man1/xclip.1.html) is required for this functionality to work.

## Usage

Installing the package adds the `euler` entry point.

To solve already completed problems:

```console
$ euler solve 45 54
[0.08013 sec]    euler.problem_45.solve()       = 1533776805
[0.04725 sec]    euler.problem_54.solve()       = 376
```

To scrape any missing data for problems:

```console
$ euler scrape 133
 -- Created: 'c:\\users\\jthom\\code\\euler\\euler\\problem_133.py'
 -- Created: 'c:\\users\\jthom\\code\\euler\\tests\\test_problem_133.py'
```
