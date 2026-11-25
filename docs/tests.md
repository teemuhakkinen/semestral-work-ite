# Testing

## Testing Approach

The program uses pytest to test its main functions separately.

The tests verify player file reading, bye calculations, tournament format recommendations, matchups and group creation.

Since player assignment is random, the tests check that every player appears exactly once instead of expecting specific matchups.

## Test Examples

| Function | Input | Expected output |
|---|---|---|
| `calculate_byes` | 8 players | 0 byes |
| `calculate_byes` | 5 players | 3 byes |
| `recommend_format` | 9 players | Groups |
| `recommend_format` | 12 players | Bracket |
| `recommend_format` | 1 player | ValueError |
| `plan_groups` | 17 players | [5, 4, 4, 4] |
| `read_players` | Missing file | Empty list |
| `create_matchups` | 5 players, 3 byes | 4 matchups, including 3 byes |
| `assign_groups` | 6 players, sizes [3, 3] | Two groups of 3 players |

## Running the Tests

Run all tests from the project root:

```bash
python test_main.py
```

## Test Coverage

The tests cover normal inputs, boundary cases, invalid inputs and random player assignment.

All main modules are tested, but terminal output is not tested automatically.