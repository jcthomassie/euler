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

## Usage

After installing, the `euler` entry point will be added.

To solve an existing problem:

```console
$ euler solve 45
[0.00002 sec]    euler.problem_2.solve()        = 4613732
```

To scrape any missing data for a problem:

```console
$ euler scrape 133
 -- Created: 'c:\\users\\jthom\\code\\euler\\euler\\problem_133.py'
 -- Created: 'c:\\users\\jthom\\code\\euler\\tests\\test_problem_133.py'
```
