# Randomized 10-Pattern Interview Mock Generator

This tool reads the 🟢 completion markers from your master Markdown file.

Detected currently:
- Total patterns: 148
- Completed patterns: 109
- Remaining patterns: 39

## Files

- `mock_interview.py` — generator
- `Patterns_Topics_(Re-Organized)(1).md` — your master pattern list

## First run

Put both files in the same folder and run:

```bash
python mock_interview.py
```

It will generate 10 completed patterns.

Run it again:

```bash
python mock_interview.py
```

It will generate the NEXT 10 from the shuffled deck.

### Important

The program does NOT independently sample 10 patterns every time.

Instead it:

1. Shuffles the entire completed pool.
2. Deals 10 patterns.
3. Saves its position.
4. Deals the next 10 on the next run.
5. Continues until every completed pattern has appeared once.
6. Automatically reshuffles and starts a new cycle.

Therefore, a pattern cannot repeat within the same cycle.

## Useful commands

Generate 10:
```bash
python mock_interview.py
```

Generate a different batch size:
```bash
python mock_interview.py --size 5
```

Check that the Markdown file is being interpreted correctly:
```bash
python mock_interview.py --status
```

Start over with a new random cycle:
```bash
python mock_interview.py --reset
```

## Completing new patterns

When you finish another pattern, simply add 🟢 to that pattern in the Markdown file.

On the next run, the script detects the newly completed pattern automatically.

## State

The script creates:

`mock_interview_state.json`

Do NOT delete this file unless you intentionally want to reset your revision cycle.
