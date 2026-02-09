import FreeSimpleGUI as sg
import random

def check_winner(board):
    win_conditions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8), 
        (0, 3, 6), (1, 4, 7), (2, 5, 8), 
        (0, 4, 8), (2, 4, 6)             
    ]
    for a, b, c in win_conditions:
        if board[a] == board[b] == board[c] and board[a] in ["X", "O"]:
            return board[a]
    if all(spot in ["X", "O"] for spot in board):
        return "Tie"
    return None

def update_button(window, key, text):
    btn = window[key]
    if btn is not None:
        btn.update(text=text, disabled=True)  # ✅ Button uses 'text='

def update_status(window, status):
    status_elem = window["-STATUS-"]
    if status_elem is not None:
        status_elem.update(value=status)  # ✅ Text uses 'value='

def reset_board(window, board):
    for i in range(9):
        key = str(i)
        update_button(window, key, "")
    update_status(window, "Your Turn (X)")
    board[:] = [""] * 9

def main():
    sg.theme('DarkGrey8') 
    
    layout = [
        [sg.Text("Your Turn (X)", key="-STATUS-", font=("Arial", 14))],
        [sg.Button("", size=(5, 2), key="0"), sg.Button("", size=(5, 2), key="1"), sg.Button("", size=(5, 2), key="2")],
        [sg.Button("", size=(5, 2), key="3"), sg.Button("", size=(5, 2), key="4"), sg.Button("", size=(5, 2), key="5")],
        [sg.Button("", size=(5, 2), key="6"), sg.Button("", size=(5, 2), key="7"), sg.Button("", size=(5, 2), key="8")],
        [sg.Button("Reset", key="-RESET-"), sg.Button("Exit", key="-EXIT-")]
    ]

    window = sg.Window("Tic-Tac-Toe", layout)
    board = [""] * 9
    game_active = True

    while True:
        result = window.read()
        if result is None:
            break
        event, values = result
        
        if event in (sg.WIN_CLOSED, "-EXIT-"):
            break
        
        if event == "-RESET-":
            reset_board(window, board)
            game_active = True
            continue

        if game_active and event in [str(i) for i in range(9)]:
            pos = int(event)
            if board[pos] == "":
                board[pos] = "X"
                update_button(window, event, "X")
                game_active = False

                res = check_winner(board)
                if res:
                    msg = "It's a tie!" if res == "Tie" else f"Player {res} wins!"
                    update_status(window, msg)
                    sg.popup(msg)
                else:
                    comp_move = random.choice([i for i, s in enumerate(board) if s == ""])
                    board[comp_move] = "O"
                    update_button(window, str(comp_move), "O")
                    game_active = False

                    res = check_winner(board)
                    if res:
                        msg = "It's a tie!" if res == "Tie" else f"Player {res} wins!"
                        update_status(window, msg)
                        sg.popup(msg)

    window.close()

if __name__ == "__main__":
    main()
