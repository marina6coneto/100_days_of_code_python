from art import logo
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    
print(logo)

bids = {}
bidding_started = True

def find_highest_bidder(bidding_record):
    highest_bid = 0
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f'The winner is {winner} with a bid of ${highest_bid}')
    
while bidding_started:
    name = input('What is your name?\n ')
    price = int(input('What is your bid? $\n'))
    bids[name] = price
    should_continue = input('Are there any other bidders? type "yes" or "no" ').strip().lower()
    if should_continue == 'no':
        bidding_starded = False
        find_highest_bidder(bids)
    elif should_continue == 'yes':
        clear()
