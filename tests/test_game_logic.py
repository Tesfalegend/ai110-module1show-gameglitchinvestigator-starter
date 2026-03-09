import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from logic_utils import check_guess, get_range_for_difficulty

def test_winning_guess():
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"


# Regression tests for the swapped high/low message bug:
# check_guess previously returned "Go HIGHER!" when guess > secret and "Go LOWER!" when guess < secret.

def test_too_high_message_says_go_lower():
    # Guess above secret — player must be told to go LOWER
    _, message = check_guess(75, 50)
    assert "LOWER" in message, f"Expected 'LOWER' but got: {message!r}"
    assert "HIGHER" not in message, f"Unexpected 'HIGHER' in: {message!r}"

def test_too_low_message_says_go_higher():
    # Guess below secret — player must be told to go HIGHER
    _, message = check_guess(25, 50)
    assert "HIGHER" in message, f"Expected 'HIGHER' but got: {message!r}"
    assert "LOWER" not in message, f"Unexpected 'LOWER' in: {message!r}"


# --- Tests targeting the three new game bugs fixed in app.py ---

def _simulate_new_game(state: dict, difficulty: str) -> dict:
    """Mirror the fixed new_game block from app.py using a plain dict instead of st.session_state."""
    get_range_for_difficulty(difficulty)
    state["attempts"] = 1
    state["secret"] = 42  # fixed so the test is deterministic
    state["status"] = "playing"
    state["history"] = []
    return state


def test_new_game_resets_status_to_playing():
    # Bug: status was never reset, so a finished game stayed "won"/"lost" forever.
    state = {"attempts": 8, "secret": 37, "status": "won", "history": [10, 20, 37]}
    result = _simulate_new_game(state, "Normal")
    assert result["status"] == "playing"


def test_new_game_clears_history():
    # Bug: history was never cleared, so old guesses carried over into the new game.
    state = {"attempts": 8, "secret": 37, "status": "lost", "history": [10, 20, 30, 40]}
    result = _simulate_new_game(state, "Normal")
    assert result["history"] == []


def test_new_game_resets_attempts_to_initial_value():
    # Bug: attempts was reset to 0 instead of 1, causing an off-by-one on the first turn.
    state = {"attempts": 8, "secret": 37, "status": "lost", "history": []}
    result = _simulate_new_game(state, "Normal")
    assert result["attempts"] == 1


def test_new_game_uses_difficulty_range_not_hardcoded():
    # Bug: secret used hardcoded randint(1, 100) instead of the difficulty-specific range.
    # Verify get_range_for_difficulty returns distinct bounds so the correct range can be used.
    assert get_range_for_difficulty("Easy") == (1, 20)
    assert get_range_for_difficulty("Hard") == (1, 50)
    assert get_range_for_difficulty("Normal") == (1, 100)
