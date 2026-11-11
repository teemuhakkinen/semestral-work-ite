"""Tests for src/bracket.py and src/players.py."""

import pytest

from src.bracket import calculate_byes, create_matchups
from src.players import read_players


# Each tuple is: (number of players, expected number of byes).
# Byes fill the bracket up to the next power of two.
@pytest.mark.parametrize("num_players, expected_byes", [
    (1, 0),   # too few for a tournament, no byes
    (2, 0),   # already a power of two
    (3, 1),   # next power of two is 4
    (5, 3),   # next power of two is 8
    (8, 0),   # already a power of two
    (9, 7),   # next power of two is 16
])
def test_calculate_byes(num_players, expected_byes):
    """calculate_byes returns the number of slots needed to fill the bracket."""
    assert calculate_byes(num_players) == expected_byes


# We test properties instead of exact pairs, because the pairing is random.
@pytest.mark.parametrize("num_players", [2, 3, 5, 8, 9, 13])
def test_matchups_include_every_player_once(num_players):
    """Every player appears in exactly one matchup."""
    players = [f"Player{i}" for i in range(num_players)]
    byes = calculate_byes(num_players)

    matchups = create_matchups(players, byes)

    # Flatten the pairs into one list of names and ignore the None (bye) slots.
    names = [name for match in matchups for name in match if name is not None]
    assert sorted(names) == sorted(players)


def test_matchups_have_correct_number_of_byes():
    """The number of matchups with a bye equals the requested byes."""
    players = ["A", "B", "C", "D", "E"]

    matchups = create_matchups(players, 3)

    bye_matches = [match for match in matchups if match[1] is None]
    assert len(bye_matches) == 3


def test_create_matchups_does_not_modify_input():
    """The original player list stays unchanged."""
    players = ["A", "B", "C", "D", "E"]
    original = players.copy()

    create_matchups(players, 3)

    assert players == original


def test_read_players_strips_whitespace_and_empty_lines(tmp_path):
    """Names are stripped and empty lines are ignored."""
    # tmp_path is a pytest fixture: a temporary folder deleted after the test.
    file = tmp_path / "players.txt"
    file.write_text("Anna\n\n  Bob  \nCecil\n", encoding="utf-8")

    assert read_players(str(file)) == ["Anna", "Bob", "Cecil"]


def test_read_players_missing_file_returns_empty_list(tmp_path):
    """A missing file currently gives an empty list."""
    missing = tmp_path / "does_not_exist.txt"

    assert read_players(str(missing)) == []