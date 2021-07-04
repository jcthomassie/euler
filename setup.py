# -*- coding: utf-8 -*-
"""Install the euler package, along with all required dependencies.

Extras:
    - dev: Required to run linting, formatting, and type checking.
    - tests: Required to perform tests.
"""
import codecs
import os

from setuptools import find_packages, setup

NAME = "euler"
AUTHOR = "Julian Thomassie"
AUTHOR_EMAIL = "julianthomassie@gmail.com"
DESCRIPTION = "Python implementations of Project Euler solutions."
URL = "https://github.com/jcthomassie/euler"

REQUIRES_PYTHON = ">=3.9"
REQUIRES = [
    "numpy",
    "pyperclip",
    "requests",
    "beautifulsoup4",
]
EXTRAS_REQUIRE = {
    "dev": ["black", "isort", "flake8", "mypy", "types-requests"],
    "tests": ["pytest", "pytest-cov", "pytest-mock", "requests-mock"],
}
EXTRAS_REQUIRE["dev"] += EXTRAS_REQUIRE["tests"]


def read(rel_path: str) -> str:
    here = os.path.abspath(os.path.dirname(__file__))
    with codecs.open(os.path.join(here, rel_path), "r") as f:
        return f.read()


def get_version(rel_path: str) -> str:
    for line in read(rel_path).splitlines():
        if line.startswith("__version__"):
            quote = '"' if '"' in line else "'"
            return line.split(quote)[1]
    raise RuntimeError("Unable to locate version string.")


if __name__ == "__main__":
    setup(
        name=NAME,
        version=get_version("euler/__init__.py"),
        description=DESCRIPTION,
        long_description=read("README.md"),
        long_description_content_type="text/markdown",
        author=AUTHOR,
        author_email=AUTHOR_EMAIL,
        python_requires=REQUIRES_PYTHON,
        url=URL,
        packages=find_packages(),
        install_requires=REQUIRES,
        extras_require=EXTRAS_REQUIRE,
        include_package_data=True,
        entry_points={"console_scripts": ["euler = euler.__main__:main"]},
        classifiers=[
            "Programming Language :: Python",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.9",
        ],
    )
