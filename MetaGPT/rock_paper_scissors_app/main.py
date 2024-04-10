import tkinter as tk
from tkinter import ttk
from game import Game

class UI:
    def __init__(self):
        self.game = Game(["rock", "paper", "scissors"])
        self.root = tk.Tk()
        self.root.title("Rock Paper Scissors Game")

        # Creating buttons for player choices
        ttk.Button(self.root, text="Rock", command=lambda: self.play("rock")).grid(column=0, row=0)
        ttk.Button(self.root, text="Paper", command=lambda: self.play("paper")).grid(column=1, row=0)
        ttk.Button(self.root, text="Scissors", command=lambda: self.play("scissors")).grid(column=2, row=0)
        
        # Label to display the result
        self.result_label = ttk.Label(self.root, text="")
        self.result_label.grid(column=0, row=1, columnspan=3)

    def play(self, player_choice):
        result = self.game.play_game(player_choice)
        self.display_result(f"Computer chose: {self.game.computer_choice}. {result}")

    def display_result(self, result: str):
        self.result_label.config(text=result)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    ui = UI()
    ui.run()