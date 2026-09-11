#!/usr/bin/env python3
"""
Interview Mock Generator
-------------------------
Uses the 🟢 markers in your master Markdown file to build randomized,
non-repeating mock interviews.

Default behavior:
- Reads completed patterns from the Markdown file.
- Shuffles them into a "deck".
- Gives 10 patterns at a time.
- Never repeats a pattern within the same cycle.
- Saves progress in mock_interview_state.json.
- Automatically starts a new shuffled cycle when the current cycle is exhausted.
- Supports --reset and --status.

Usage:
    python mock_interview.py
    python mock_interview.py --status
    python mock_interview.py --reset
    python mock_interview.py --size 5
"""

from pathlib import Path
import argparse
import json
import random
import re

DEFAULT_MARKDOWN = Path(__file__).with_name("Patterns_Topics_(Re-Organized)(1).md")
STATE_FILE = Path(__file__).with_name("mock_interview_state.json")


def extract_patterns(md_file):
    text = md_file.read_text(encoding="utf-8")
    patterns = []

    for line in text.splitlines():
        if not line.startswith("|"):
            continue

        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 3:
            continue
        if cells[0] == "Pattern ID" or cells[0].startswith(":"):
            continue

        raw_id = cells[0]
        completed = "🟢" in raw_id

        clean_id = re.sub(r"🟢\s*", "", raw_id)
        clean_id = re.sub(r"\*\*", "", clean_id)
        match = re.search(r"\[([^\]]+)\]", clean_id)
        if not match:
            continue

        pattern_id = match.group(1).strip()
        topic = re.sub(r"\*\*", "", cells[1]).strip()

        if topic and topic != "Topic Name":
            patterns.append({
                "id": pattern_id,
                "topic": topic,
                "completed": completed
            })

    return patterns


def load_state():
    if not STATE_FILE.exists():
        return {
            "cycle": 1,
            "deck": [],
            "position": 0,
            "mock_number": 1
        }
    return json.loads(STATE_FILE.read_text(encoding="utf-8"))


def save_state(state):
    STATE_FILE.write_text(
        json.dumps(state, indent=2, ensure_ascii=False),
        encoding="utf-8"
    )


def make_new_deck(completed):
    deck = [p["id"] for p in completed]
    random.shuffle(deck)
    return deck


def reset_state():
    if STATE_FILE.exists():
        STATE_FILE.unlink()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--size", type=int, default=10,
                        help="Number of patterns per mock (default: 10)")
    parser.add_argument("--reset", action="store_true",
                        help="Start a new randomized cycle")
    parser.add_argument("--status", action="store_true",
                        help="Show current revision status")
    parser.add_argument("--file", type=Path, default=DEFAULT_MARKDOWN,
                        help="Path to the master Markdown file")
    args = parser.parse_args()

    if args.size <= 0:
        raise SystemExit("--size must be greater than 0.")

    patterns = extract_patterns(args.file)
    by_id = {p["id"]: p for p in patterns}
    completed = [p for p in patterns if p["completed"]]

    if not completed:
        raise SystemExit("No 🟢 completed patterns found.")

    if args.reset:
        reset_state()
        print("Reset complete. A new randomized cycle will start now.\n")

    state = load_state()

    # Remove IDs that are no longer completed and preserve newly completed IDs.
    completed_ids = {p["id"] for p in completed}
    deck = [pid for pid in state["deck"] if pid in completed_ids]

    # Add newly completed patterns that aren't already in the current deck.
    deck_ids = set(deck)
    new_ids = [pid for pid in completed_ids if pid not in deck_ids]

    if not deck:
        deck = make_new_deck(completed)
        state["position"] = 0
    elif new_ids:
        # Put newly completed patterns into the unused portion and shuffle it.
        unused = deck[state["position"]:]
        used = deck[:state["position"]]
        unused.extend(new_ids)
        random.shuffle(unused)
        deck = used + unused

    state["deck"] = deck

    # If fewer than requested remain in this cycle, finish the current cycle
    # first, then start a fresh randomized cycle for the remainder.
    remaining_in_cycle = len(deck) - state["position"]

    selected_ids = []

    if remaining_in_cycle >= args.size:
        selected_ids = deck[state["position"]:state["position"] + args.size]
        state["position"] += args.size
    else:
        if remaining_in_cycle > 0:
            selected_ids.extend(deck[state["position"]:])
            state["position"] = len(deck)

        # Start next cycle if we still need more patterns.
        if len(selected_ids) < args.size:
            state["cycle"] += 1
            new_deck = make_new_deck(completed)
            state["deck"] = new_deck
            state["position"] = 0

            needed = args.size - len(selected_ids)
            selected_ids.extend(new_deck[:needed])
            state["position"] = needed

    mock_number = state["mock_number"]
    state["mock_number"] += 1
    save_state(state)

    print("=" * 62)
    print(f"MOCK INTERVIEW #{mock_number}")
    print(f"Revision cycle: {state['cycle']}")
    print(f"Patterns per mock: {args.size}")
    print(f"Completed pool: {len(completed)}")
    print("=" * 62)

    for i, pid in enumerate(selected_ids, 1):
        print(f"{i:2}. {pid:<14} — {by_id[pid]['topic']}")

    print("\nProgress:")
    print(f"  Used in current cycle: {state['position']}/{len(completed)}")
    print(f"  Remaining in current cycle: {len(completed) - state['position']}")
    print(f"\nState saved to: {STATE_FILE.name}")


if __name__ == "__main__":
    main()
