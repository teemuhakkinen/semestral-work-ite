from src.players import read_players
from src.bracket import calculate_byes, create_matchups
from src.planner import recommend_format


def main():
    players = read_players("players")

    try:
        chosen_format, reason = recommend_format(len(players))
    except ValueError as error:
        print(error)
        return

    print(f"Recommended format: {chosen_format} ({reason})")

    if chosen_format == "bracket":
        byes_needed = calculate_byes(len(players))
        first_round = create_matchups(players, byes_needed)

        print("\n--- FIRST ROUND MATCHUPS ---")
        for index, match in enumerate(first_round, 1):
            if match[1] is None:
                print(f"Match {index}: {match[0]} gets a BYE (Advances automatically)")
            else:
                print(f"Match {index}: {match[0]} VS {match[1]}")
    else:
        print("Group stage is not implemented yet.")


if __name__ == "__main__":
    main()