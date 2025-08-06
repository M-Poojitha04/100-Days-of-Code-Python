import random
import art


def number_guessing_game():
    print(art.logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    number_thought = random.randint(1, 100)
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if difficulty == 'easy':
        attempts = 10
    else:
        attempts = 5
    while attempts > 0:
        print(f"You have {attempts} attempts remaining to guess the number.")
        user_guess = int(input("Make a guess: "))
        if user_guess < number_thought and attempts != 1:
            print("Too Low.")
            print("Guess again.")
            attempts = attempts - 1
        elif user_guess > number_thought and attempts != 1:
            print("Too High.")
            print("Guess again.")
            attempts = attempts - 1
        elif user_guess == number_thought:
            print(f"You got it! The answer was {number_thought}.")
            return 0
        else:
            print(f"You've run out of guesses.The number was {number_thought}.")
            return 0
    return 0
number_guessing_game()