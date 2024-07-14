import tkinter as tk
from queue import Queue

def bfs(board, player):
    q = Queue()
    best_score = -float("inf")
    best_action = None

    for action in range(9):
        if board[action] == " ":
            q.put((board[:], action, player, 0)) # enqueue el current state 

    while not q.empty():        # yfdl loop l7d ma el queue yb2a empty 
        current_board, current_action, current_player, current_level = q.get()  # get next state 

        if check_winner(current_board, "X"):
            score = 1  
        elif check_winner(current_board, "O"):
            score = -1  
        elif check_tie(current_board):
            score = 0  
        else:
            score = 0  

        if current_level == 0:
            if score > best_score:
                best_score = score
                best_action = current_action
        else:
            if current_player == "X":
                best_score = max(best_score, score)
            else:
                best_score = min(best_score, score)

        for action in range(9):
            if current_board[action] == " ":
                next_board = current_board[:]
                next_board[action] = current_player
                next_player = "X" if current_player == "O" else "O"
                q.put((next_board, action, next_player, current_level + 1))  # y5osh 3la el node el b3dha

    return best_action

def bfs_best_move(board):
    best_action = bfs(board, "X")
    return best_action



root = tk.Tk()                  # main window
root.title("Tic Tac Toe")       # title for the tkinter window

board = [" " for i in range(9)]             # list for the board 


def check_winner(board, player):
    # Check rows
    for i in range(0, 9, 3):
        if board[i] == board[i + 1] == board[i + 2] == player:
            return True
    # Check columns
    for i in range(3):
        if board[i] == board[i + 3] == board[i + 6] == player:
            return True
    # Check diagonals
    if (board[0] == board[4] == board[8] == player) or (board[2] == board[4] == board[6] == player):
        return True
    return False


def check_tie(board):
    return " " not in board


# check if position is empty,
# if yes then put "O" in it and check if i won, 
# if not then check for tie,
# if not then call computer function 
def player_move(position):
    if board[position] == " ":
        board[position] = "O"
        buttons[position].config(text="O", state="disabled")
        if check_winner(board, "O"):
            info_label.config(text="You win!")
        elif check_tie(board):
            info_label.config(text="It's a tie!")
        else:
            computer_move()
    

def computer_move():
    available_positions = [i for i, value in enumerate(board) if value == " "]
    if available_positions:
        computer_choice = bfs_best_move(board)                   
        board[computer_choice] = "X"
        buttons[computer_choice].config(text="X", state="disabled")
        if check_winner(board, "X"):
            info_label.config(text="Computer wins!")
        elif check_tie(board):
            info_label.config(text="It's a tie!")
        else:
            info_label.config(text="Your turn")


buttons = []
for i in range(9):                  # Create and configure buttons
    row, col = divmod(i, 3)
    button = tk.Button(root, text=" ", width=10, height=5, command=lambda i=i: player_move(i))  # hy7ot X,O
    button.grid(row=row, column=col)
    buttons.append(button)


# labels
info_label = tk.Label(root, text="Your turn")
info_label.grid(row=3, column=0, columnspan=3)


info_label.config(text="Your turn")         # start game
root.mainloop()                             # tkinter loop
