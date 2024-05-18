import tkinter as tk
import random
from tkinter import messagebox

# Function to choose rock, paper, or scissors for the computer
def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return 'tie'
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return 'user'
    else:
        return 'computer'

# Main application class
class RockPaperScissorsApp:
    def __init__(self, root):
        self.root = root
        self.user_score = 0
        self.computer_score = 0
        self.initialize_ui()

    def initialize_ui(self):
        self.root.title("Rock-Paper-Scissors Game")
        self.root.configure(bg='light blue')  # Set the background color of the window

        # Instructions
        instructions = tk.Label(self.root, text="Choose rock, paper, or scissors:", bg='light blue', fg='black')
        instructions.pack()

        # Buttons for user to make a choice
        tk.Button(self.root, text="Rock", bg='orange', fg='black', command=lambda: self.play_round('rock')).pack()
        tk.Button(self.root, text="Paper", bg='white', fg='black', command=lambda: self.play_round('paper')).pack()
        tk.Button(self.root, text="Scissors", bg='light green', fg='black', command=lambda: self.play_round('scissors')).pack()

        # Label to display the result
        self.result_label = tk.Label(self.root, text="", bg='light blue', fg='black')
        self.result_label.pack()

        # Label to display the scores
        self.score_label = tk.Label(self.root, text="User: 0 | Computer: 0", bg='light blue', fg='black')
        self.score_label.pack()

    def play_round(self, user_choice):
        computer_choice = get_computer_choice()
        winner = determine_winner(user_choice, computer_choice)
        result_text = f"Your choice: {user_choice}\nComputer's choice: {computer_choice}\n"

        if winner == 'tie':
            result_text += "It's a tie!"
        elif winner == 'user':
            self.user_score += 1
            result_text += "You win!"
        else:
            self.computer_score += 1
            result_text += "You lose!"

        self.result_label.config(text=result_text)
        self.score_label.config(text=f"User: {self.user_score} | Computer: {self.computer_score}")

        # Ask if the user wants to play another round
        if messagebox.askyesno("Play Again", "Do you want to play another round?"):
            self.result_label.config(text="")
        else:
            self.root.destroy()

# Create the main window and pass it to the RockPaperScissorsApp
root = tk.Tk()
app = RockPaperScissorsApp(root)
root.mainloop()
