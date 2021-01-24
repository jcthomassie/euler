from pathlib import Path
from typing import Iterator

import pytest
import requests_mock
from pytest_mock import MockerFixture

from euler.scraper import Problem

PROBLEM = 1
PROBLEM_TITLE = "Multiples of 3 and 5"
PROBLEM_URL = "https://projecteuler.net/problem=1"
PROBLEM_HTML = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8" />
<meta name="author" content="Colin Hughes" />
<meta name="description" content="A website dedicated to the fascinating world of mathematics and programming" />
<meta name="keywords" content="programming,mathematics,problems,puzzles" />
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Problem 1 - Project Euler</title>
<link rel="shortcut icon" href="favicon.ico" />
<link rel="stylesheet" type="text/css" href="themes/20201111/style_main.css" />
<link rel="stylesheet" type="text/css" href="themes/20201111/style_default.css" />
<script src="js/mathjax_config.js"></script>
<script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script type="text/javascript" id="MathJax-script" async
   src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js">
</script></head>

<body>

<div id="container">
<div id="header" class="noprint">
   <img src="themes/20201111/logo_default.png" alt="" />
<div id="info_panel">
&nbsp;&nbsp;&nbsp;<a href="search"><img src="images/icons/search_engine.png" alt="Search Problems" title="Search Problems" class="icon"></a>&nbsp;&nbsp;&nbsp;&nbsp;<a href="rss2_euler.xml"><img src="images/icons/rss.png" alt="RSS Feed" title="RSS Feed" class="icon"></a>
</div><!--end_info_panel-->
</div> <!--end_header-->
<div id="navigation" class="nav noprint">
<a href="about" title="About"  accesskey="h">About</a>
<a href="archives" title="Archives"  accesskey="1">Archives</a>
<a href="recent" title="Recent"  accesskey="2">Recent</a>
<a href="news" title="News"  accesskey="3">News</a>
<a href="register" title="Register"  accesskey="4">Register</a>
<a href="sign_in" title="Sign In"  accesskey="5">Sign In</a>
   <a class="hamburger" id="hamburger">
         <div class="bar"></div>
         <div class="bar"></div>
         <div class="bar"></div>
   </a>

</div> <!--end_nav-->

<div id="content">

<div class="center print"><img src="images/print_page_logo.png" alt="projecteuler.net" class="no_border"></div>
<h2>Multiples of 3 and 5</h2><div id="problem_icons" class="noprint"><a href="minimal=1"><img src="images/icons/file_html.png" title="Show HTML problem content" class="icon"></a>&nbsp;<span class="tooltip"><img src="images/icons/info.png" class="icon"><span class="tooltiptext_right">Published on Friday, 5th October 2001, 06:00 pm; Solved by 965835;<br>Difficulty rating: 5%</span></div><div id="problem_info"><h3>Problem 1</h3></div>
<div class="problem_content" role="problem">
<p>If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.</p>
<p>Find the sum of all the multiples of 3 or 5 below 1000.</p>
</div><br>
<br></div> <!--end_content-->
</div> <!--end_container-->

<div id="footer" class="noprint">
Project Euler: <a href="copyright">Copyright Information</a> | <a href="privacy">Privacy Policy</a>
</div> <!--end_footer-->
<div id="modal_window">
   <div id="modal_content" class="message_body">
   <p>The page has been left unattended for too long and that link/button is no longer active. Please refresh the page.</p>
   </div>
</div> <!--end_modal_window-->
<script src="js/general.js"></script>

</body>
</html>
"""


class TestProblem:
    @pytest.fixture
    def project_euler_html(self, requests_mock: requests_mock.Mocker) -> Iterator[None]:
        requests_mock.get(PROBLEM_URL, text=PROBLEM_HTML)
        yield

    @pytest.fixture
    def problem(self, project_euler_html: None) -> Iterator[Problem]:
        yield Problem(PROBLEM)

    def test_source_url(self, problem: Problem) -> None:
        assert problem.source_url == PROBLEM_URL

    def test_module_path(self, problem: Problem) -> None:
        import euler.problem_1

        assert problem.module_path == euler.problem_1.__file__

    def test_test_module_path(self, problem: Problem) -> None:
        import tests.test_problem_1

        assert problem.test_module_path == tests.test_problem_1.__file__

    def test_get_title(self, problem: Problem) -> None:
        assert problem.get_title() == PROBLEM_TITLE

    def test_create_module(
        self, problem: Problem, mocker: MockerFixture, tmp_path: Path
    ) -> None:
        out = tmp_path / "problem.py"
        mocker.patch(
            "euler.scraper.Problem.module_path",
            new=mocker.PropertyMock(return_value=out),
        )
        problem.create_module()
        assert out.is_file()

    def test_create_test_module(
        self, problem: Problem, mocker: MockerFixture, tmp_path: Path
    ) -> None:
        out = tmp_path / "test_problem.py"
        mocker.patch(
            "euler.scraper.Problem.test_module_path",
            new=mocker.PropertyMock(return_value=out),
        )
        problem.create_test_module()
        assert out.is_file()
