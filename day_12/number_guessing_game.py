from art import logo
from random import randint

def get_difficulty():
    while True:
        difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").strip().lower()
        if difficulty == 'easy':
            return 10
        elif difficulty == 'hard':
            return 5
        else:
            print('Invalid choice. Please choose between "easy" or "hard".')

print(logo)
print('Welcome to the Number Guessing Game!')
print("I'm thinking of a number between 1 and 100.")

attempts = get_difficulty()
computer_number_choice = randint(1, 100)
is_game_off = False

while not is_game_off and attempts > 0:
    try:
        user_number_guess = int(input('Make a guess: '))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if user_number_guess == computer_number_choice:
        print(f'You got it! The answer was {computer_number_choice}')
        is_game_off = True
    elif user_number_guess < computer_number_choice:
        attempts -= 1
        print('Too low')
    elif user_number_guess > computer_number_choice:
        attempts -= 1
        print('Too high')

    if attempts > 0 and not is_game_off:
        print('Guess again.')
        print(f'You have {attempts} attempts remaining to guess the number.')
    elif attempts == 0:
        print(f'You have run out of attempts. The number was {computer_number_choice}. Better luck next time!')

print('Game Over')
