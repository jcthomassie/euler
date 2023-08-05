# -*- coding: utf-8 -*-
"""Implements programmatic scraping of problems from https://projecteuler.net"""
import os
import textwrap
from dataclasses import dataclass
from pathlib import Path
from typing import Optional, Self

import requests
from bs4 import BeautifulSoup

_OUTDIR = Path(__file__).parent
_FILE_TEMPLATE = '''# -*- coding: utf-8 -*-
"""
{}
"""
from .utils import print_result


@print_result
def solve() -> int:
    raise NotImplementedError()


if __name__ == "__main__":
    solve()
'''
_TEST_FILE_TEMPLATE = """from euler.problem_{} import solve

from .utils import validate_solution


def test_solution() -> None:
    validate_solution(solve, answer=None)
"""


@dataclass
class Problem:
    """
    Handles all scraping, downloading, and formatting for any Project Euler
    problem listed on https://projecteuler.net/archive
    """

    number: int
    url: str
    path_module: Path
    path_test_module: Path

    _soup: BeautifulSoup | None = None

    @classmethod
    def from_number(cls, number: int) -> Self:
        return cls(
            number=number,
            url=f"https://projecteuler.net/problem={number}",
            path_module=_OUTDIR / f"problem_{number}.py",
            path_test_module=_OUTDIR.parent / "tests" / f"test_problem_{number}.py",
        )

    @property
    def soup(self) -> BeautifulSoup:
        if self._soup is None:
            response = requests.get(self.url)
            self._soup = BeautifulSoup(response.text, "html.parser")
        return self._soup

    def get_data_links(self) -> list[str]:
        """Get urls for associated problem data."""
        links = []
        for link in self.soup.find_all("a"):
            href = link.get("href")
            if href is None:
                continue
            if href.startswith("project/resources/"):
                links.append(f"https://projecteuler.net/{href}")
        return links

    def get_title(self) -> str:
        """Get the problem title."""
        tag = self.soup.find("h2")
        return tag.string  # type: ignore

    def get_statement(self) -> str:
        """Get the problem statement."""
        tag = self.soup.select(".problem_content")[0]
        return tag.get_text()  # type: ignore

    def module_docstring(self) -> str:
        """Assemble the module docstring.

        Includes problem title and statement formatted in a reasonable manner.
        """
        lines = []
        lines.append(self.get_title())
        lines.append("=" * len(lines[-1]))
        lines.append(self.url)
        for block in self.get_statement().split("\n"):
            block = block.strip()
            if not block:
                continue
            lines.append("")
            lines.extend(
                textwrap.wrap(
                    block,
                    expand_tabs=True,
                    break_long_words=False,
                    width=80,
                )
            )
        return "\n".join(lines)

    def create_module(self) -> Optional[Path]:
        """Create a python module for the problem.

        Does nothing if the module already exists.
        """
        if self.path_module.exists():
            return None
        with self.path_module.open("w", encoding="utf-8") as h:
            h.write(_FILE_TEMPLATE.format(self.module_docstring()))
            return self.path_module

    def create_test_module(self) -> Optional[Path]:
        """Create a python module for testing the problem.

        Does nothing if the module already exists.
        """
        if self.path_test_module.exists():
            return None
        with self.path_test_module.open("w", encoding="utf-8") as h:
            h.write(_TEST_FILE_TEMPLATE.format(self.number))
            return self.path_test_module

    def download_files(self) -> list[Path]:
        """Download any associated data files for the problem.

        Skips any files that have already been downloaded.

        Returns:
            Paths to files that were downloaded.
        """
        downloads = []
        for url in self.get_data_links():
            # Get local path
            path = _OUTDIR / "data" / os.path.basename(url)
            if path.exists():
                continue
            # Copy data from url
            data = requests.get(url)
            with open(path, "w", encoding="utf-8") as h:
                h.write(data.text)
            downloads.append(path)
        return downloads

    def scrape(self) -> list[Path]:
        """Scrape problem data, create python module, and copy any associated files.

        Returns:
            Paths to files that were created.
        """
        paths = []
        module = self.create_module()
        if module is not None:
            paths.append(module)
        test_module = self.create_test_module()
        if test_module is not None:
            paths.append(test_module)
        paths.extend(self.download_files())
        return paths
