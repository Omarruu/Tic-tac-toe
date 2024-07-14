import tkinter as tk

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
    if player_board[position] == " " and computer_board[position] == " ":
        player_board[position] = "X"
        buttons[position].config(text="X", state="disabled")
        if check_winner(player_board, "X"):
            info_label.config(text="You win!")
        elif check_tie(player_board):
            info_label.config(text="It's a tie!")
        else:
            computer_move()

def computer_move():
    available_positions = [i for i, value in enumerate(player_board) if value == " " and computer_board[i] == " "]
    if available_positions:
        computer_choice = available_positions[0]  # awl available position y2ablo y7ot fih
        computer_board[computer_choice] = "O"
        buttons[computer_choice].config(text="O", state="disabled")
        if check_winner(computer_board, "O"):
            info_label.config(text="Computer wins!")
        elif check_tie(player_board) or check_tie(computer_board):
            info_label.config(text="It's a tie!")
        else:
            info_label.config(text="Your turn")

root = tk.Tk()
root.title("Tic Tac Toe")

player_board = [" " for i in range(9)]
computer_board = [" " for i in range(9)]

buttons = []
for i in range(9):
    row, col = divmod(i, 3)
    button = tk.Button(root, text=" ", width=10, height=5, command=lambda i=i: player_move(i))
    button.grid(row=row, column=col)
    buttons.append(button)

info_label = tk.Label(root, text="Your turn")
info_label.grid(row=3, column=0, columnspan=3)

root.mainloop()
