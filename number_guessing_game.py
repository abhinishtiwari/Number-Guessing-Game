import random

def display_options():
    print("\nSelect a difficulty level:")
    print("1. Easy (1-50, 10 chances)")
    print("2. Medium (1-100, 8 chances)")
    print("3. Hard (1-500, 6 chances)")
    print("4. Expert (1-1000, 5 chances)")

def get_difficulty():
    while True:
        try:
            choice = int(input("Enter the number of your choice (1-4): "))
            if choice in [1, 2, 3, 4]:
                return choice
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def set_game_parameters(difficulty):
    if difficulty == 1:
        return 50, 10
    elif difficulty == 2:
        return 100, 8
    elif difficulty == 3:
        return 500, 6
    elif difficulty == 4:
        return 1000, 5

def play_level(level):
    print(f"\nLevel {level}:")
    display_options()
    difficulty = get_difficulty()
    upper_bound, max_attempts = set_game_parameters(difficulty)
    
    number_to_guess = random.randint(1, upper_bound)
    
    print(f"I have selected a number between 1 and {upper_bound}. You have {max_attempts} attempts to guess it!")
    
    attempts = 0
    while attempts < max_attempts:
        try:
            guess = int(input(f"Attempt {attempts + 1}: Enter your guess: "))
            
            if guess < 1 or guess > upper_bound:
                print(f"Please guess a number between 1 and {upper_bound}.")
                continue
            
            attempts += 1
            
            if guess < number_to_guess:
                print("Too low! Try again.")
            elif guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number {number_to_guess} in {attempts} attempts.")
                return True
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
    print(f"Sorry, you've used all {max_attempts} attempts. The number was {number_to_guess}.")
    return False

def main():
    print("Welcome to the Number Guessing Game!")
    print("You need to win all 10 levels to be the ultimate champion!")

    for level in range(1, 11):
        if not play_level(level):
            print("Game Over. You didn't complete all levels.")
            return
    
    print("\n🎉 Congratulations! You've won all 10 levels! 🎉")
    print("You're an ultimate champion of the Number Guessing Game!")

if __name__ == "__main__":
    main()
