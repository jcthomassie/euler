# -*- coding: utf-8 -*-
"""
Implements programmatic scraping of problems from https://projecteuler.net
and creation of template python modules for problems.
"""
import os
import textwrap

import requests
from bs4 import BeautifulSoup

_OUTDIR = os.path.dirname(__file__)

_URL_TEMPLATE = "https://projecteuler.net/problem={}"
_PATH_TEMPLATE = os.path.join(_OUTDIR, "problem_{}.py")
_DATA_TEMPLATE = os.path.join(_OUTDIR, "data", "{}")
_FILE_TEMPLATE = '''# -*- coding: utf-8 -*-
"""
{}
"""
from .utils import print_result

@print_result
def solve():
    return

if __name__ == "__main__":
    solve()
'''


class Problem:
    """
    Handles all scraping, downloading, and formatting for any Project Euler
    problem listed on https://projecteuler.net/archive
    """

    def __init__(self, number: int):
        self.number = number
        self._soup = None

    @property
    def source_url(self):
        return _URL_TEMPLATE.format(self.number)

    @property
    def module_path(self):
        return _PATH_TEMPLATE.format(self.number)

    @property
    def soup(self):
        if self._soup is None:
            response = requests.get(self.source_url)
            self._soup = BeautifulSoup(response.text, "html.parser")
        return self._soup

    def get_data_links(self):
        """
        Get a list of urls for associated problem data.
        """
        links = []
        for link in self.soup.find_all("a"):
            href = link.get("href")
            if href.startswith("project/resources/"):
                links.append(f"https://projecteuler.net/{href}")
        return links

    def get_title(self) -> str:
        """
        Get the problem title.
        """
        tag = self.soup.find("h2")
        return tag.string

    def get_statement(self) -> str:
        """
        Get the problem statement.
        """
        tag = self.soup.select(".problem_content")[0]
        return tag.get_text()

    def module_docstring(self) -> str:
        """
        Assemble the module docstring. Includes problem title and statement
        formatted in a reasonable manner.
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
                    block, expand_tabs=True, break_long_words=False, width=80,
                )
            )
        return "\n".join(lines)

    def create_module(self):
        """
        Create a python module for the problem, using the standard module
        template. Does nothing if the module already exists.
        """
        if os.path.isfile(self.module_path):
            return
        with open(self.module_path, "w", encoding="utf-8") as h:
            h.write(_FILE_TEMPLATE.format(self.module_docstring()))
            return self.module_path

    def download_files(self):
        """
        Download any associated data files for the problem. Skips any files
        that have already been downloaded. Returns a list of files that were
        downloaded.
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

    def scrape(self):
        """
        Scrape problem data, create python module, and copy any associated
        files. Returns a list of files that were created.
        """
        paths = []
        module = self.create_module()
        if module is not None:
            paths.append(module)
        paths.extend(self.download_files())
        return paths
