"""Tests for src/planner.py."""

import pytest

from src.planner import recommend_format


# Each tuple is one test case: (number of players, expected format).
# pytest runs the test function below once for every tuple.
@pytest.mark.parametrize("num_players, expected_format", [
    (5, "bracket"),    # fewer than 8 players: too few for a group stage
    (8, "bracket"),    # exactly 8 players: no byes needed
    (9, "groups"),     # 7 of 16 slots would be byes (over 25 %)
    (12, "bracket"),   # boundary case: 4 of 16 slots, exactly 25 %, not over
    (16, "bracket"),   # full bracket, no byes
    (17, "groups"),    # 15 of 32 slots would be byes
])
def test_recommend_format(num_players, expected_format):
    """The recommended format matches the expected one for each case."""
    chosen_format, reason = recommend_format(num_players)
    assert chosen_format == expected_format


def test_reason_is_not_empty():
    """The function always returns a reason that can be shown to the user."""
    chosen_format, reason = recommend_format(9)
    assert reason != ""


# Fewer than 2 players cannot form a tournament, so an error is expected.
@pytest.mark.parametrize("num_players", [0, 1])
def test_too_few_players_raises_error(num_players):
    """recommend_format raises ValueError when there are fewer than 2 players."""
    with pytest.raises(ValueError):
        recommend_format(num_players)