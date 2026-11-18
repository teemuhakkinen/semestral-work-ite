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

# Each tuple is: (number of players, expected group sizes).
@pytest.mark.parametrize("num_players, expected_sizes", [
    (6, [3, 3]),
    (9, [5, 4]),
    (12, [3, 3, 3, 3]),
    (17, [5, 4, 4, 4]),
])
def test_plan_groups(num_players, expected_sizes):
    """plan_groups returns the expected group sizes."""
    assert plan_groups(num_players) == expected_sizes


def test_plan_groups_too_few_players():
    """Fewer than 6 players cannot be split into groups."""
    with pytest.raises(ValueError):
        plan_groups(5)

def test_assign_groups_include_every_player_once():
    """Every player ends up in exactly one group."""
    players = [f"Player{i}" for i in range(17)]

    groups = assign_groups(players, [5, 4, 4, 4])

    names = [name for group in groups for name in group]
    assert sorted(names) == sorted(players)


def test_assign_groups_have_requested_sizes():
    """The groups have the sizes that were asked for."""
    players = [f"Player{i}" for i in range(12)]

    groups = assign_groups(players, [3, 3, 3, 3])

    assert [len(group) for group in groups] == [3, 3, 3, 3]


def test_assign_groups_does_not_modify_input():
    """The original player list stays unchanged."""
    players = ["A", "B", "C", "D", "E", "F"]
    original = players.copy()

    assign_groups(players, [3, 3])

    assert players == original


def test_assign_groups_wrong_total_raises_error():
    """Sizes that do not add up to the player count raise ValueError."""
    with pytest.raises(ValueError):
        assign_groups(["A", "B", "C"], [2, 2])