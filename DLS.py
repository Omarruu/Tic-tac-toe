import tkinter as tk

def minimax(board, depth, is_maximizing):
    if check_winner(board, "O"):
        return 1
    if check_winner(board, "X"):
        return -1
    if check_tie(board) or depth == 0:
        return 0

    if is_maximizing:
        best_score = -float("inf")
        for move in range(9):
            if board[move] == " ":
                board[move] = "O"
                score = minimax(board, depth - 1, False)
                board[move] = " "
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = float("inf")
        for move in range(9):
            if board[move] == " ":
                board[move] = "X"
                score = minimax(board, depth - 1, True)
                board[move] = " "
                best_score = min(score, best_score)
        return best_score

def best_move(board, depth):
    best_score = -float("inf")
    best_action = None
    for action in range(9):
        if board[action] == " ":
            board[action] = "O"
            score = minimax(board, depth, False)
            board[action] = " "
            if score > best_score:
                best_score = score
                best_action = action
    return best_action

def check_winner(board, player):
    for i in range(0, 9, 3):
        if board[i] == board[i + 1] == board[i + 2] == player:
            return True
    for i in range(3):
        if board[i] == board[i + 3] == board[i + 6] == player:
            return True
    if (board[0] == board[4] == board[8] == player) or (board[2] == board[4] == board[6] == player):
        return True
    return False

def check_tie(board):
    return " " not in board

def player_move(position):
    if board[position] == " ":
        board[position] = "X"
        buttons[position].config(text="X", state="disabled")
        if check_winner(board, "X"):
            info_label.config(text="You win!")
        elif check_tie(board):
            info_label.config(text="It's a tie!")
        else:
            computer_move()

def computer_move():
    depth = 4  # limit el depth el hyt3mlo search 
    computer_choice = best_move(board, depth)
    board[computer_choice] = "O"
    buttons[computer_choice].config(text="O", state="disabled")
    if check_winner(board, "O"):
        info_label.config(text="Computer wins!")
    elif check_tie(board):
        info_label.config(text="It's a tie!")
    else:
        info_label.config(text="Your turn")

root = tk.Tk()
root.title("Tic Tac Toe")

board = [" " for i in range(9)]

buttons = []
for i in range(9):
    row, col = divmod(i, 3)
    button = tk.Button(root, text=" ", width=10, height=5, command=lambda i=i: player_move(i))
    button.grid(row=row, column=col)
    buttons.append(button)

info_label = tk.Label(root, text="Your turn")
info_label.grid(row=3, column=0, columnspan=3)

root.mainloop()
