import random

def start_game():
    print("Welcome to the Number Guessing Game!")
    
    # The computer selects a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    
    attempts = 0
    guessed_correctly = False
    
    while not guessed_correctly:
        try:
            guess = int(input("Guess the number (between 1 and 100): "))
            attempts += 1
            
            if guess < number_to_guess:
                print("Too low! Try again.")
            elif guess > number_to_guess:
                print("Too high! Try again.")
            else:
                guessed_correctly = True
                print(f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts.")
        
        except ValueError:
            print("Invalid input! Please enter a valid number.")
    
    play_again()

def play_again():
    """Ask the player if they want to play again"""
    response = input("\nWould you like to play again? (y/n): ").lower()
    if response == "y":
        start_game()
    else:
        print("Thanks for playing! Goodbye!")

if __name__ == "__main__":
    start_game()
