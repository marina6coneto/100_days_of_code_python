from art import logo, vs
from game_data import data
from random import choice
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def format_data(account):
    """Format the account data into printable format."""
    account_name = account['name']
    account_description = account['description']
    account_country = account['country']
    return f'{account_name}, a {account_description}, from {account_country}.'

def check_answer(guess, a_followers, b_followers):
    """Take the user guest and follower counts and returns is they got it right"""
    if a_followers > b_followers:
        return guess == 'A'
    else:
        return guess == 'B'
    
print(logo)
account_b = choice(data)
score = 0
is_higher_lower_end = False

while not is_higher_lower_end:
    account_a = account_b
    account_b = choice(data)
    
    if account_a == account_b:
        account_b = choice(data)
        
    print(f'Compare A: {format_data(account_a)}')
    print(vs)
    print(f'Compare B: {format_data(account_b)}')
    
    guess = input('Who has more followers? Type "A" or "B": ').strip().upper()
    
    while guess not in ["A", "B"]:
        print("Invalid input. Please type 'A' or 'B'.")
        guess = input('Who has more followers? Type "A" or "B": ').strip().upper()

    a_account_follower = account_a['follower_count']
    b_account_follower = account_b['follower_count']

    is_correct = check_answer(guess, a_account_follower, b_account_follower)
    clear()
    print(logo)
    if is_correct:
        score += 1
        print(f"You're right. Current score: {score}")
        
    else:
        is_higher_lower_end = True
        print(f"Sorry, that's wrong. Final score: {score}")
        

