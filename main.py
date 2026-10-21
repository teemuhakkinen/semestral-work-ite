import math
def read_players(filename):
    """
    Reads player names from a given text file.
    Ignores empty lines and removes extra whitespace.
    """
    players = []
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                name = line.strip()
                if name:
                    players.append(name)
        return players
    except FileNotFoundError:
        print(f"Error: Could not find the file '{filename}'.")
        return []
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

if __name__ == "__main__":
    tournament_players = read_players("players")
    player_count = len(tournament_players)
    byes_needed = calculate_byes(player_count)

    print("Tournament players:")
    for player in tournament_players:
        print(f"- {player}")

    print(f"\nTotal players: {player_count}")
    print(f"Byes needed: {byes_needed}")