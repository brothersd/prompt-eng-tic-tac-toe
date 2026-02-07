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

def main():
    sg.theme('DarkGrey8') 
    
    # ✅ STRING KEYS ONLY - NO INTEGERS
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
        # ✅ CRITICAL: Check for None BEFORE unpacking
        result = window.read()
        if result is None:
            break
        event, values = result
        
        # Handle window closure
        if event in (sg.WIN_CLOSED, "-EXIT-"):
            break
            
        # Handle Reset
        if event == "-RESET-":
            board = [""] * 9
            for i in range(9):
                key = str(i)
                elem = window[key]
                if elem is not None:
                    elem.update(text="", disabled=False)  # ✅ Button uses 'text='
            status_elem = window["-STATUS-"]
            if status_elem is not None:
                status_elem.update(value="Your Turn (X)")  # ✅ Text uses 'value='
            game_active = True
            continue

        # Human Move
        if game_active and event in [str(i) for i in range(9)]:
            pos = int(event)
            if board[pos] == "":
                board[pos] = "X"
                btn = window[event]
                if btn is not None:
                    btn.update(text="X", disabled=True)  # ✅ Button uses 'text='
                
                res = check_winner(board)
                if res:
                    msg = "It's a tie!" if res == "Tie" else f"Player {res} wins!"
                    status_elem = window["-STATUS-"]
                    if status_elem is not None:
                        status_elem.update(value=msg)  # ✅ Text uses 'value='
                    sg.popup(msg)
                    game_active = False
                else:
                    # Computer Move
                    available = [i for i, s in enumerate(board) if s == ""]
                    if available:
                        comp_move = random.choice(available)
                        board[comp_move] = "O"
                        comp_key = str(comp_move)
                        btn = window[comp_key]
                        if btn is not None:
                            btn.update(text="O", disabled=True)  # ✅ Button uses 'text='
                        
                        res = check_winner(board)
                        if res:
                            msg = "It's a tie!" if res == "Tie" else f"Player {res} wins!"
                            status_elem = window["-STATUS-"]
                            if status_elem is not None:
                                status_elem.update(value=msg)  # ✅ Text uses 'value='
                            sg.popup(msg)
                            game_active = False

    window.close()

if __name__ == "__main__":
    main()