# Tournament Bracket Planner

## Purpose

A simple Python program that helps tournament organizers choose a suitable tournament format based on the number of players.

The program recommends either a knockout bracket or a group stage and randomly assigns players to matches or groups.

## Installation

Requirements: Python 3.11 or newer.

Clone the repository:

```bash
git clone https://github.com/teemuhakkinen/semestral-work-ite.git
cd semestral-work-ite
```

Install the testing dependency:

```bash
python -m pip install -r requirements.txt
```

## Usage

1. Add player names to the `players` file, one name per line.
2. Run the program:

```bash
python main.py
```

The program displays the recommended tournament format, the reason for its selection, and the generated matchups or groups.

## Program Logic

- Fewer than 2 players: error.
- Fewer than 8 players: knockout bracket.
- Otherwise, if more than 25% of the bracket slots are byes, a group stage is recommended.
- Groups contain 3–6 players, with a target size of 4.

The two best players from each group are intended to advance.

## Diagrams

- [Program Flowchart](docs/diagrams/program_flow.png)
- [Module Diagram](docs/diagrams/module_diagram.png)
- [Sequence Diagram](docs/diagrams/sequence_diagram.png)

## Testing

Run all automated tests:

```bash
python test_main.py
```

See [tests.md](docs/tests.md) for the testing approach and examples.

## Limitations

- Only the first knockout round is generated.
- Individual group matches are not generated.
- Match results are not recorded.
- The input filename is fixed.

## License

MIT License. See [LICENSE](LICENSE).