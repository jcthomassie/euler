# -*- coding: utf-8 -*-
"""Implements programmatic scraping of problems from https://projecteuler.net"""
import os
import textwrap
from typing import Optional

import requests
from bs4 import BeautifulSoup

_OUTDIR = os.path.dirname(__file__)

_URL_TEMPLATE = "https://projecteuler.net/problem={}"
_PATH_TEMPLATE = os.path.join(_OUTDIR, "problem_{}.py")
_TEST_PATH_TEMPLATE = os.path.join(
    os.path.dirname(_OUTDIR), "tests", "test_problem_{}.py"
)
_DATA_TEMPLATE = os.path.join(_OUTDIR, "data", "{}")
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


def test_solution():
    validate_solution(solve, answer=None)
"""


class Problem:
    """
    Handles all scraping, downloading, and formatting for any Project Euler
    problem listed on https://projecteuler.net/archive
    """

    def __init__(self, number: int) -> None:
        self.number = number
        self._soup = None

    @property
    def source_url(self) -> str:
        return _URL_TEMPLATE.format(self.number)

    @property
    def module_path(self) -> str:
        return _PATH_TEMPLATE.format(self.number)

    @property
    def test_module_path(self) -> str:
        return _TEST_PATH_TEMPLATE.format(self.number)

    @property
    def soup(self) -> BeautifulSoup:
        if self._soup is None:
            response = requests.get(self.source_url)
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
        lines.append(self.source_url)
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

    def create_module(self) -> Optional[str]:
        """Create a python module for the problem.

        Does nothing if the module already exists.
        """
        if os.path.isfile(self.module_path):
            return None
        with open(self.module_path, "w", encoding="utf-8") as h:
            h.write(_FILE_TEMPLATE.format(self.module_docstring()))
            return self.module_path

    def create_test_module(self) -> Optional[str]:
        """Create a python module for testing the problem.

        Does nothing if the module already exists.
        """
        if os.path.isfile(self.test_module_path):
            return None
        with open(self.test_module_path, "w", encoding="utf-8") as h:
            h.write(_TEST_FILE_TEMPLATE.format(self.number))
            return self.test_module_path

    def download_files(self) -> list[str]:
        """Download any associated data files for the problem.

        Skips any files that have already been downloaded.

        Returns:
            Paths to files that were downloaded.
        """
        downloads = []
        for url in self.get_data_links():
            # Get local path
            path = _DATA_TEMPLATE.format(os.path.basename(url))
            if os.path.isfile(path):
                continue
            # Copy data from url
            data = requests.get(url)
            with open(path, "w", encoding="utf-8") as h:
                h.write(data.text)
            downloads.append(path)
        return downloads

    def scrape(self) -> list[str]:
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
