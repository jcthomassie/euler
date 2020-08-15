import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--skip-unknown",
        action="store_true",
        default=False,
        help="skip testing problems without a known solution",
    )


def pytest_collection_modifyitems(config, items):
    if config.getoption("--skip-unknown"):
        skip_unknown = pytest.mark.skipif("SOLUTION is None")
        for item in items:
            item.add_marker(skip_unknown)
