import random

def guess_the_number():
    lower_limit = 1
    upper_limit = 100
    secret_number = random.randint(lower_limit, upper_limit)
    attempts = 0

    print(f"Welcome to the Number Guessing Game! Guess a number between {lower_limit} and {upper_limit}.")

    while True:
        try:
            player_guess = int(input("Enter your guess: "))
            attempts += 1

            if player_guess < lower_limit or player_guess > upper_limit:
                print(f"Please guess a number between {lower_limit} and {upper_limit}.")
            elif player_guess < secret_number:
                print("Higher! Try again.")
            elif player_guess > secret_number:
                print("Lower! Try again.")
            else:
                print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")


