import tkinter as tk

def find_best_move():
    best_score = -float("inf")
    best_move = (-1, -1)
    for i in range(3):
        for j in range(3):
            if board[i][j] == "":
                board[i][j] = "X"
                score = dfs(board, False)
                board[i][j] = ""
                if score > best_score:
                    best_score = score
                    best_move = (i, j)
    return best_move

def dfs(board, is_maximizing):
    if check_winner("X"):
        return 1
    elif check_winner("O"):
        return -1
    elif check_tie():
        return 0

    if is_maximizing:
        best_score = -float("inf")
        for i in range(3):
            for j in range(3):
                if board[i][j] == "":
                    board[i][j] = "X"
                    score = dfs(board, False)
                    board[i][j] = ""
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = float("inf")
        for i in range(3):
            for j in range(3):
                if board[i][j] == "":
                    board[i][j] = "O"
                    score = dfs(board, True)
                    board[i][j] = ""
                    best_score = min(score, best_score)
        return best_score



board = [["" for k in range(3)] for k in range(3)]


root = tk.Tk()
root.title("Tic Tac Toe")


buttons = []
for i in range(3):
    row = []
    for j in range(3):
        button = tk.Button(root, text="", width=10, height=5)
        button.configure(command=lambda button=button, i=i, j=j: make_move(button, i, j))
        button.grid(row=i, column=j)
        row.append(button)
    buttons.append(row)


info_label = tk.Label(root, text="Your turn")
info_label.grid(row=3, column=0, columnspan=3)


current_player = "O"
game_over = False


def make_move(button, i, j):
    global current_player, game_over

    if board[i][j] == "" and not game_over:
        board[i][j] = "O"
        button.config(text="O", state="disabled")
        current_player = "X"
        info_label.config(text="Computer's turn")

        
        if check_winner("O"):
            info_label.config(text="You win!")
            game_over = True
        elif check_tie():
            info_label.config(text="It's a tie!")
            game_over = True
        else:
            best_move = find_best_move()
            board[best_move[0]][best_move[1]] = "X"
            buttons[best_move[0]][best_move[1]].config(text="X", state="disabled")
            current_player = "O"
            info_label.config(text="Your turn")

            if check_winner("X"):
                info_label.config(text="Computer wins!")
                game_over = True
            elif check_tie():
                info_label.config(text="It's a tie!")
                game_over = True

def check_winner(player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)):
            return True
        if all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False


def check_tie():
    return all(board[i][j] != "" for i in range(3) for j in range(3))

root.mainloop()
