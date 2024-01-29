class CountingGame:
    def __init__(self):
        self.current_number = 0
        self.max_count = 21

    def play(self, numbers):
        for num in numbers:
            self.current_number += num
            if self.current_number >= self.max_count:
                return True  # Game over, current player loses
        return False  # Game continues

    def computer_play(self, user_numbers):
        # Simulated computer logic to strategically continue the sequence
        last_number = user_numbers[-1] if user_numbers else 0
        remaining = self.max_count - self.current_number

        if remaining >= 3:
            return last_number + 3
        elif remaining == 2:
            return last_number + 2
        else:
            return last_number + 1

# Example usage:
if __name__ == "__main__":
    game = CountingGame()
    print("Game started. You can use the CountingGameGUI for a graphical interface.")

    # This section can be used for testing the logic independently (not interacting with the console)
    while game.current_number < game.max_count:
        user_input = input("Your turn: ").strip()

        if user_input:
            user_numbers = [int(num) for num in user_input.split(',')]
        else:
            user_numbers = []

        if game.play(user_numbers):
            print("You win! Game over1,2.")
            break
        else:
            print(f"Your turn: {user_numbers}")

        computer_numbers = game.computer_play(user_numbers)
        game.play([computer_numbers])
        if game.current_number >= game.max_count:
            print("Computer wins! Game over.")
            break
        else:
            print(f"Computer's turn: {', '.join(map(str, range(user_numbers[-1] + 1, computer_numbers + 1)))}. Your turn.")