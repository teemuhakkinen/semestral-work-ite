import math
import random
from src.players import read_players
def calculate_byes(num_players):
    """
    Calculates the number of byes needed to make the bracket valid.
    Uses the next power of 2.
    """
    if num_players <= 1:
        return 0

    next_power_of_2 = 2 ** math.ceil(math.log2(num_players))
    byes = next_power_of_2 - num_players

    return byes

def create_matchups(players, byes_count):
    """
    Shuffles players and creates the first round matchups.
    Assigns 'Bye' to the required number of players.
    """
    # Tehdään kopio listasta, jotta alkuperäinen ei tuhoudu, ja sekoitetaan se
    shuffled_players = players.copy()
    random.shuffle(shuffled_players)

    matchups = []

    # 1. Jaetaan ensin vapaataipaleet (Byes)
    for i in range(byes_count):
        lucky_player = shuffled_players.pop(0)
        matchups.append((lucky_player, None))

    # 2. Jaetaan loput pelaajat normaaleihin ottelupareihin
    while len(shuffled_players) >= 2:
        player1 = shuffled_players.pop(0)
        player2 = shuffled_players.pop(0)
        matchups.append((player1, player2))

    return matchups

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