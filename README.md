# semestral-work-ite
# Tournament Bracket Planner

## Purpose
A small Python program that reads player names from a text file,
recommends a tournament format (knockout bracket or group stage) based on
the number of players, and generates the first round matchups of a
knockout bracket. Players are shuffled randomly, and byes are given
when the player count is not a power of two.

## Installation
1. Install Python 3.11 or newer.
2. Clone the repository:
   ```
   git clone https://github.com/teemuhakkinen/semestral-work-ite.git
   cd semestral-work-ite
   ```
3. Install dependencies (only needed for running tests):
   ```
   python -m pip install -r requirements.txt
   ```

## Usage
1. Create a text file named `players` in the project root, one name per line.
   Empty lines are ignored.
2. Run the program from the project root:
   ```
   python main.py
   ```

Example input:
```
Anna
Bob
Cecil
Dan
Eve
```

Example output (matchups are random):
```
Recommended format: bracket (...)

--- FIRST ROUND MATCHUPS ---
Match 1: Eve gets a BYE (Advances automatically)
...
```

## Testing
Run all tests with `python test_main.py`.
See [docs/tests.md](docs/tests.md) for the testing approach.

## Limitations
- Only the first round is generated.
- If the group stage is recommended, the program does not generate groups yet.
- The player file name is fixed.
- Duplicate names are not detected.
- Results are not entered, so the bracket does not update.

## License
MIT, see [LICENSE](LICENSE).
