"""Decides which tournament format suits a given number of players."""
from src.bracket import calculate_byes
MIN_PLAYERS_FOR_GROUPS = 8
MAX_BYE_SHARE = 0.25
def recommend_format(num_players):
    """
    Recommends a tournament format for the given number of players.

    Returns a tuple (format, reason), where format is "bracket" or "groups"
    and reason is a short explanation that can be shown to the user.
    Raises ValueError if there are fewer than 2 players.
    """
    if num_players < 2:
        raise ValueError("A tournament needs at least 2 players.")

    if num_players < MIN_PLAYERS_FOR_GROUPS:
        return "bracket", f"{num_players} players is too few for group stage"

    byes = calculate_byes(num_players)
    slots = num_players + byes

    if byes / slots > MAX_BYE_SHARE:
        return "groups", f"{byes} of {slots} first round slots would be byes"

    return "bracket", f"only {byes} of {slots} first round slots would be byes"
