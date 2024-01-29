import tkinter as tk
from tkinter import Entry, Button, Label, StringVar, Text, Scrollbar
from counting_game import CountingGame

class CountingGameGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Counting Game")

        self.game = CountingGame()
        self.user_input = StringVar()
        self.computer_moves = StringVar()

        # Widgets
        Label(self.master, text="Your turn:").pack()
        self.user_entry = Entry(self.master, textvariable=self.user_input)
        self.user_entry.pack()
        Button(self.master, text="Submit", command=self.submit).pack()

        # Text area for displaying game state
        self.text_area = Text(self.master, height=10, width=30, wrap=tk.WORD)
        self.text_area.pack()

        # Scrollbar for text area
        scrollbar = Scrollbar(self.master, command=self.text_area.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.text_area.config(yscrollcommand=scrollbar.set)

        # Start the game with the user's turn
        self.update_game_state("Your turn.")

        # Adjust window size
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()
        quarter_width = screen_width // 4
        quarter_height = screen_height // 4
        self.master.geometry(f"{quarter_width}x{quarter_height}+{quarter_width}+{quarter_height}")

    def submit(self):
        try:
            # Split numbers by commas and convert to integers
            user_numbers = [int(num.strip()) for num in self.user_input.get().split(',')]
            if not user_numbers or any(num < 1 or num > 3 for num in user_numbers):
                self.update_game_state("Invalid input. Please enter 1-3 numbers.")
                return

            if self.game.play(user_numbers):
                self.update_game_state("You win! Game over.")
                self.reset_game()
            else:
                self.update_game_state(f"Your turn: {user_numbers}")
                self.user_entry.delete(0, tk.END)  # Clear the input textbox
                self.computer_turn()

        except ValueError:
            self.update_game_state("Invalid input. Please enter valid numbers.")

    def computer_turn(self):
        computer_numbers = self.game.computer_play()
        self.game.play([computer_numbers])

        if self.game.current_number >= self.game.max_count:
            self.update_game_state("Computer wins! Game over.")
            self.reset_game()
        else:
            self.update_game_state(f"Computer's turn: {computer_numbers}. Your turn.")

    def reset_game(self):
        self.game = CountingGame()
        self.user_input.set("")
        self.update_game_state("Game reset. Enter numbers to continue.")

    def update_game_state(self, message):
        current_state = self.text_area.get("1.0", tk.END)
        self.text_area.delete("1.0", tk.END)
        self.text_area.insert(tk.END, f"{message}\n{current_state}")

if __name__ == "__main__":
    root = tk.Tk()
    app = CountingGameGUI(root)
    root.mainloop()
