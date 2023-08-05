import pytest


def pytest_addoption(parser: pytest.Parser) -> None:
    parser.addoption(
        "--include-solved",
        action="store_true",
        default=False,
        help="run solved problem tests",
    )


def pytest_configure(config: pytest.Config) -> None:
    config.addinivalue_line("markers", "solved: module solution has been verified")


def pytest_collection_modifyitems(
    config: pytest.Config, items: list[pytest.Item]
) -> None:
    if config.getoption("--include-solved"):
        return
    skip_solved = pytest.mark.skip(reason="use --include-solved to run")
    for item in items:
        if "solved" in item.keywords:
            item.add_marker(skip_solved)
