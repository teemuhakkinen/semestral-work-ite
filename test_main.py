"""Runs the whole test suite."""

import sys

import pytest

if __name__ == "__main__":
    # Run all tests in the tests/ folder and use pytest's result
    # (0 = all passed) as the exit code of this script.
    sys.exit(pytest.main(["tests"]))