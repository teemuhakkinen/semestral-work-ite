"""Decides which tournament format suits a given number of players."""
import random

from src.bracket import calculate_byes

# Thresholds for recommending a format.
MIN_PLAYERS_FOR_GROUPS = 8
MAX_BYE_SHARE = 0.25

# Rules for splitting players into groups.
MIN_GROUP_SIZE = 3
MAX_GROUP_SIZE = 6
TARGET_GROUP_SIZE = 4


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


def plan_groups(num_players):
    """
    Plans the group sizes for a group stage.

    The number of groups is a power of two (2, 4, 8, ...), so that the two
    best players of each group fill a knockout bracket without byes.
    Group sizes must be between MIN_GROUP_SIZE and MAX_GROUP_SIZE. If several
    splits are possible, the one whose average group size is closest to
    TARGET_GROUP_SIZE is chosen.

    Args:
        num_players: Number of players in the tournament.

    Returns:
        A list of group sizes, for example [5, 4, 4, 4].

    Raises:
        ValueError: If no valid split exists (fewer than 6 players).
    """
    best = None
    best_distance = None

    groups = 2
    while num_players // groups >= MIN_GROUP_SIZE:
        base, remainder = divmod(num_players, groups)
        # The largest group has one extra player if the split is uneven.
        largest = base + 1 if remainder > 0 else base

        if largest <= MAX_GROUP_SIZE:
            distance = abs(num_players / groups - TARGET_GROUP_SIZE)
            if best is None or distance < best_distance:
                best = [base + 1] * remainder + [base] * (groups - remainder)
                best_distance = distance

        groups *= 2

    if best is None:
        raise ValueError("At least 6 players are needed for a group stage.")

    return best

def assign_groups(players, group_sizes):
    """
    Shuffles the players and splits them into groups of the given sizes.

    Args:
        players: List of player names.
        group_sizes: List of group sizes, for example [5, 4, 4, 4].
            The sizes must add up to the number of players.

    Returns:
        A list of groups, where each group is a list of player names.

    Raises:
        ValueError: If the sizes do not add up to the number of players.
    """
    if sum(group_sizes) != len(players):
        raise ValueError("Group sizes must add up to the number of players.")

    # Copy the list so that the original order is not changed.
    shuffled = players.copy()
    random.shuffle(shuffled)

    groups = []
    start = 0
    for size in group_sizes:
        groups.append(shuffled[start:start + size])
        start += size

    return groups