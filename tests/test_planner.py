"""Tests for src/planner.py."""

import pytest

from src.planner import recommend_format


def test_nine_players_recommends_groups():
    chosen_format, reason = recommend_format(9)
    assert chosen_format == "groups"


def test_sixteen_players_recommends_bracket():
    chosen_format, reason = recommend_format(16)
    assert chosen_format == "bracket"


def test_one_player_raises_error():
    with pytest.raises(ValueError):
        recommend_format(1)