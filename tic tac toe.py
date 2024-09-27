import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.board = [None] * 9
        self.current_player = "X"
        self.buttons = [tk.Button(root, text="", font="Arial 20", width=5, height=2, command=lambda i=i: self.make_move(i)) for i in range(9)]
        
        for i, button in enumerate(self.buttons):
            button.grid(row=i // 3, column=i % 3)
    
    def make_move(self, i):
        if self.board[i] is None:
            self.board[i] = self.current_player
            self.buttons[i].config(text=self.current_player)
            if self.check_winner():
                messagebox.showinfo("Game Over", f"{self.current_player} wins!")
                self.reset_game()
            elif None not in self.board:
                messagebox.showinfo("Game Over", "It's a draw!")
                self.reset_game()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                                (0, 3, 6), (1, 4, 7), (2, 5, 8),
                                (0, 4, 8), (2, 4, 6)]
        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != None:
                return True
        return False
    
    def reset_game(self):
        for i in range(9):
            self.board[i] = None
            self.buttons[i].config(text="")
        self.current_player = "X"

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
