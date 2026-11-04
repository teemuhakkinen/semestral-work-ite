from src.players import read_players
from src.bracket import calculate_byes, create_matchups

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

if __name__ == "__main__":
    tournament_players = read_players("players")
    player_count = len(tournament_players)

    if player_count < 2:
        print("Not enough players for a tournament!")
    else:
        byes_needed = calculate_byes(player_count)
        first_round = create_matchups(tournament_players, byes_needed)

        print("\n--- FIRST ROUND MATCHUPS ---")
        for index, match in enumerate(first_round, 1):
            if match[1] == None:
                print(f"Match {index}: {match[0]} gets a BYE (Advances automatically)")
            else:
                print(f"Match {index}: {match[0]} VS {match[1]}")