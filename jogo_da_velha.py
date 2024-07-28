import tkinter as tk
from tkinter import messagebox

def check_winner(board):
    for row in board:
        if row[0] == row[1] == row[2] != '':
            return row[0]
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != '':
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] != '':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != '':
        return board[0][2]
    return None

def check_draw(board):
    for row in board:
        if '' in row:
            return False
    return True

def on_button_click(row, col):
    global winner
    if board[row][col] == '' and not winner:
        board[row][col] = current_player.get()
        buttons[row][col].config(text=current_player.get())
        winner = check_winner(board)
        if winner:
            messagebox.showinfo("Fim de Jogo", f"O jogador {winner} venceu!")
            reset_board()
        elif check_draw(board):
            messagebox.showinfo("Fim de Jogo", "O jogo empatou!")
            reset_board()
        else:
            current_player.set('O' if current_player.get() == 'X' else 'X')

def reset_board():
    global board, buttons, winner
    board = [['' for _ in range(3)] for _ in range(3)]
    winner = None
    for row in range(3):
        for col in range(3):
            buttons[row][col].config(text='')

root = tk.Tk()
root.title("Jogo da Velha")

current_player = tk.StringVar(value='X')
board = [['' for _ in range(3)] for _ in range(3)]
buttons = [[None for _ in range(3)] for _ in range(3)]
winner = None

frame = tk.Frame(root)
frame.pack()

for row in range(3):
    for col in range(3):
        button = tk.Button(frame, text='', width=10, height=3, command=lambda r=row, c=col: on_button_click(r, c))
        button.grid(row=row, column=col)
        buttons[row][col] = button

reset_button = tk.Button(root, text="Resetar", command=reset_board)
reset_button.pack()

root.mainloop()
