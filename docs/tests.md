# Testing

## Approach
Tests are written with pytest and run with `python test_main.py`.
The logic is split into small pure functions, so each can be tested
without user input or files, except `read_players`, which uses a
temporary file.

The program uses random shuffling, so tests for `create_matchups`
check properties that are always true (every player appears exactly
once, the number of byes is correct, the input list is not modified)
instead of exact pairings.

## Test files
- `tests/test_planner.py`: `recommend_format`
- `tests/test_bracket.py`: `calculate_byes`, `create_matchups`, `read_players`

## Sample inputs and outputs

### calculate_byes
| Players | Byes |
|---|---|
| 1 | 0 |
| 3 | 1 |
| 5 | 3 |
| 8 | 0 |
| 9 | 7 |

### recommend_format
| Players | Format | Reason |
|---|---|---|
| 5 | bracket | fewer than 8 players |
| 9 | groups | 7 of 16 slots would be byes (over 25 %) |
| 12 | bracket | boundary case, exactly 25 % |
| 17 | groups | 15 of 32 slots would be byes |
| 1 | ValueError | at least 2 players required |

## Coverage
25 tests in total. Edge cases tested: fewer than two players, exactly 25 %
byes, empty lines and extra whitespace in the player file.
Not tested: the printed output of `main()`.