import random

class Mastermind:
    def __init__(self):
        self.code_length = 4  # Length of the secret code
        self.num_colors = 6   # Number of colors (for digits 1-6)
        self.max_attempts = 10  # Maximum number of attempts allowed
        self.secret_code = self.generate_secret_code()
    
    def generate_secret_code(self):
        return [random.randint(1, self.num_colors) for _ in range(self.code_length)]
    
    def evaluate_guess(self, guess):
        correct_position = 0
        correct_color = 0
        code_copy = self.secret_code[:]
        guess_copy = guess[:]
        
        # First pass: Check for correct positions
        for i in range(self.code_length):
            if guess_copy[i] == code_copy[i]:
                correct_position += 1
                code_copy[i] = 0  # Mark as visited
        
        # Second pass: Check for correct colors in wrong positions
        for i in range(self.code_length):
            if guess_copy[i] in code_copy and code_copy[i] != 0:
                correct_color += 1
                code_copy[code_copy.index(guess_copy[i])] = 0  # Mark as visited
        
        return correct_position, correct_color
    
    def play_game(self):
        print("Welcome to Mastermind!")
        print(f"Guess the {self.code_length}-digit code, using numbers from 1 to {self.num_colors}.")
        print(f"You have {self.max_attempts} attempts.")
        
        attempts = 0
        while attempts < self.max_attempts:
            attempts += 1
            print(f"\nAttempt {attempts}:")
            guess = self.get_guess()
            correct_position, correct_color = self.evaluate_guess(guess)
            
            if correct_position == self.code_length:
                print(f"Congratulations! You guessed the code: {''.join(map(str, guess))}.")
                break
            
            print(f"Correct positions: {correct_position}")
            print(f"Correct colors in wrong positions: {correct_color}")
        
        if attempts == self.max_attempts:
            print(f"\nGame over! You've run out of attempts. The secret code was: {''.join(map(str, self.secret_code))}.")
    
    def get_guess(self):
        while True:
            guess_str = input(f"Enter your {self.code_length}-digit guess: ")
            if len(guess_str) != self.code_length or not guess_str.isdigit():
                print(f"Invalid input! Please enter {self.code_length} digits.")
                continue
            guess = [int(char) for char in guess_str]
            if any(num < 1 or num > self.num_colors for num in guess):
                print(f"Invalid input! Please use numbers from 1 to {self.num_colors}.")
                continue
            return guess

if __name__ == "__main__":
    game = Mastermind()
    game.play_game()
