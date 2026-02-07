import pytest
from tictactoe_gui import check_winner

def test_horizontal_win():
    """Verify detection of a horizontal win."""
    board = ["X", "X", "X", "4", "5", "6", "7", "8", "9"]
    assert check_winner(board) == "X"

def test_cats_game():
    """Verify detection of a 'Cats game' (tie)."""
    board = ["X", "O", "X", "X", "O", "O", "O", "X", "X"]
    assert check_winner(board) == "Tie"

def test_no_winner_yet():
    """Verify None is returned when the game is in progress."""
    board = ["X", "O", "3", "4", "5", "6", "7", "8", "9"]
    assert check_winner(board) is None