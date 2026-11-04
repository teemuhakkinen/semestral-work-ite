import math
import random
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