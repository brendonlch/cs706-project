import random
from typing import List

class Game:
    def __init__(self, options: List[str]):
        if not options:
            raise ValueError("Options cannot be empty")
        self.options = options
        self.player_choice = ""
        self.computer_choice = ""

    def play_game(self, player_choice: str) -> str:
        if player_choice not in self.options:
            raise ValueError(f"Invalid choice. Please choose from {self.options}")
            
        self.player_choice = player_choice
        self.computer_choice = random.choice(self.options)
        
        # Determine the result based on traditional rock-paper-scissors rules
        if self.player_choice == self.computer_choice:
            result = "It's a tie"
        elif (self.player_choice == "rock" and self.computer_choice == "scissors") or \
             (self.player_choice == "paper" and self.computer_choice == "rock") or \
             (self.player_choice == "scissors" and self.computer_choice == "paper"):
            result = "Player wins"
        else:
            result = "Computer wins"
        
        # Return the result string
        return result