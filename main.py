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

if __name__ == "__main__":
    # Testataan koodin toimintaa
    tournament_players = read_players("players")
    print("Tournament players:")
    for player in tournament_players:
        print(f"- {player}")