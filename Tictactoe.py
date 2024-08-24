import tkinter as tk
from tkinter import messagebox
import random

def initialize_board():
    return [['-' for _ in range(3)] for _ in range(3)]

def check_win(board, mark):
    # Check rows and columns
    for i in range(3):
        if all(board[i][j] == mark for j in range(3)) or all(board[j][i] == mark for j in range(3)):
            return True
    # Check diagonals
    if all(board[i][i] == mark for i in range(3)) or all(board[i][2-i] == mark for i in range(3)):
        return True
    return False

def check_draw(board):
    return all(cell != '-' for row in board for cell in row)

def on_button_click(row, col):
    global current_player

    if board[row][col] == '-':
        board[row][col] = current_player
        buttons[row][col].config(text=current_player, state="disabled")

        if check_win(board, current_player):
            messagebox.showinfo("Tic Tac Toe", f"Player {current_player} wins!")
            reset_board()
        elif check_draw(board):
            messagebox.showinfo("Tic Tac Toe", "It's a draw!")
            reset_board()
        else:
            if current_player == 'X':
                current_player = 'O'
                computer_turn()
            else:
                current_player = 'X'

def computer_turn():
    global current_player
    available = [(i, j) for i in range(3) for j in range(3) if board[i][j] == '-']
    if available:
        row, col = random.choice(available)
        board[row][col] = 'O'
        buttons[row][col].config(text='O', state="disabled")

        if check_win(board, 'O'):
            messagebox.showinfo("Tic Tac Toe", "Computer wins! Better luck next time!")
            reset_board()
        elif check_draw(board):
            messagebox.showinfo("Tic Tac Toe", "It's a draw!")
            reset_board()
        else:
            current_player = 'X'

def reset_board():
    global board, current_player
    board = initialize_board()
    current_player = 'X'
    for row in range(3):
        for col in range(3):
            buttons[row][col].config(text='', state="normal")

# Initialize the game
root = tk.Tk()
root.title("Tic Tac Toe")

board = initialize_board()
current_player = 'X'

# Create the 3x3 grid of buttons
buttons = [[None for _ in range(3)] for _ in range(3)]
for row in range(3):
    for col in range(3):
        buttons[row][col] = tk.Button(root, text='', font=('Arial', 24), width=5, height=2,
                                      command=lambda r=row, c=col: on_button_click(r, c))
        buttons[row][col].grid(row=row, column=col)

# Start the Tkinter main loop
root.mainloop()
