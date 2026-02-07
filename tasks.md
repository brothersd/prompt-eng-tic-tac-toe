<task>
Create a Dockerfile to containerize the Python Tic-Tac-Toe terminal game.
</task>

<context>
The game is a simple terminal-based Python script. It requires user input and prints the board to the console.
</context>

<requirements>
1. Use a lightweight base image (like `python:3.9-slim`).
2. Ensure the container stays open for user interaction (interactive terminal mode).
3. Set the working directory to `/app`.
4. Include a command to run the main script (e.g., `python main.py`).
</requirements>

<output_format>
- Provide the Dockerfile code.
- Provide the specific `docker build` and `docker run` commands needed to play the game interactively.
</output_format>

############################################

<task>
Implement the human player interaction logic for the Python Tic-Tac-Toe game.
</task>

<context>
We already have `initialize_board()` and `display_board(board)`. Now we need to handle user choices and input validation.
</context>

<instructions>
1. Create a function `choose_marker()` that asks the user if they want to be "X" or "O" and returns the chosen markers for both the human and computer.
2. Create a function `get_human_move(board)` that:
    - Prompts the user to enter a move (1-9).
    - Validates that the input is a number and the chosen spot is not already taken.
    - Returns the updated board.
</instructions>

<source_material>
- User input: Ask the user if they want to be "x" or "o".
- Human Player: Need to tell the user how to enter their move.
</source_material>

<constraints>
- Use a `while` loop for input validation to ensure the user provides a valid move before proceeding.
- Do not implement the computer's move logic yet.
</constraints>

<output_format>
Provide the Python code within triple backticks.
</output_format>

#######################################

<task>
Implement the computer player logic for the Python Tic-Tac-Toe game.
</task>

<context>
The board is a list of 9 strings ("1"-"9" or "X"/"O"). We have already handled human input; now the computer needs to select an available spot.
</context>

<instructions>
1. Create a function `get_computer_move(board, computer_marker)` that:
    - Identifies all currently available spots (spots that do not contain "X" or "O").
    - Selects one of those spots at random.
    - Updates the board with the computer's marker.
    - Returns the updated board.
</instructions>

<source_material>
- Computer Player: Randomly generates a move.
- Computer Player: Needs to know spots available, or, if randomly generated move is valid or not.
- AI is --- random move.
</source_material>

<constraints>
- Use the Python `random` module.
- Ensure the computer does not try to play in a spot already occupied by "X" or "O".
- Provide a print statement so the human player knows what move the computer chose.
</constraints>

<output_format>
Provide the Python code within triple backticks.
</output_format>
##########################################

<task>
Create a test suite using pytest for the Python Tic-Tac-Toe game.
</task>

<context>
The game logic is modular with functions for initialization, move validation, and win checking. We need to verify these work as expected without manual play.
</context>

<instructions>
1. Write tests for `initialize_board()` to ensure it returns a list of 9 strings.
2. Write tests for `check_winner()` covering:
    - A horizontal win.
    - A vertical win.
    - A diagonal win.
    - A "Cats game" (tie) scenario.
    - A continuing game (no winner yet).
</instructions>

<constraints>
- Use `pytest` fixtures if necessary.
- Mocking is not required for the logic functions, just pass specific board states (lists) to the functions.
</constraints>

<output_format>
Provide the Python code for `test_tic_tac_toe.py` within triple backticks.
</output_format>

############################################

<task>
Convert the existing terminal-based Tic-Tac-Toe logic into a GUI application using Tkinter.
</task>

<context>
We have the core logic (board representation, win checking, and random AI). We now want to replace the `input()` and `print()` functions with a window, buttons, and labels.
</context>

<instructions>
1. Create a `TicTacToeGUI` class.
2. Use a 3x3 grid of Tkinter Buttons to represent the board.
3. When a user clicks a button:
    - Update the button text with the player's marker.
    - Check for a winner or tie.
    - If the game continues, trigger the computer's random move automatically.
4. Use a Label to display the game status (e.g., "Your Turn", "Computer Wins", "Tie").
5. Include a "Reset" button to restart the game.
</instructions>

<constraints>
- Keep the `check_winner` logic the same.
- Use the `random` module for the computer's move.
- Disable buttons once they are clicked or when the game ends.
</constraints>

<output_format>
Provide the full Python code within triple backticks.
</output_format>