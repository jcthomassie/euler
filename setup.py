# -*- coding: utf-8 -*-
import io
import os
import platform
from glob import glob
from setuptools import setup, find_packages

from euler import __author__, __email__, __version__

###############################################################################
#                            PACKAGE METADATA                                 #
###############################################################################
NAME = "euler"
VERSION = __version__
AUTHOR = __author__
EMAIL = __email__
DESCRIPTION = "Python implementations of Project Euler solutions."
URL = "https://github.com/jcthomassie/euler"
REQUIRES_PYTHON = ">=3.6"
REQUIRED = [
    "numba",
    "numpy",
    "pyperclip",
    "beautifulsoup4",
]
PACKAGES = find_packages()

# Import the README and use it as the long-description.
here = os.path.abspath(os.path.dirname(__file__))
try:
    with io.open(os.path.join(here, "README.md"), encoding="utf-8") as f:
        long_description = "\n" + f.read()
except FileNotFoundError:
    long_description = DESCRIPTION

req_str = "\n*     ".join(REQUIRED)
print(
    "* * * * * * * * * Installing Package! * * * * * * * * * *\n"
    f"* Name = {NAME}\n"
    f"* Version = {VERSION}\n"
    f"* Author = {AUTHOR}\n"
    f"* Email = {EMAIL}\n"
    f"*\n* {DESCRIPTION}\n*\n"
    f"* Requirements:\n*     {req_str}\n*\n"
    "* * * * * * * * * * * * * * * * * * * * * * * * * * * * *"
)

###############################################################################
#                               RUN SETUP                                     #
###############################################################################
setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    packages=PACKAGES,
    install_requires=REQUIRED,
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "euler = euler.__main__:main",
        ]
    },
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
)

print(f"\n********** Finished Installing '{NAME}' **********")
