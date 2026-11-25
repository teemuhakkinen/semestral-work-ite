"""Main entry point for the tournament planner."""

from src.players import read_players
from src.bracket import calculate_byes, create_matchups
from src.planner import recommend_format, plan_groups, assign_groups


def main():
    """Read players, recommend a format and display the tournament plan."""
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
        group_sizes = plan_groups(len(players))
        groups = assign_groups(players, group_sizes)

        print("\n--- GROUP STAGE ---")
        print(f"{len(groups)} groups, the best 2 of each advance")
        for index, group in enumerate(groups, 1):
            print(f"Group {index}: {', '.join(group)}")


if __name__ == "__main__":
    main()