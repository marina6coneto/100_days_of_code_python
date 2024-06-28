from art import logo
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    
print(logo)

bids = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
    highest_bid = 0
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
    print(f'The winner is {bidder} with a bid of ${highest_bid}')
    
while not bidding_finished:
    name = input('What is your name?\n ')
    price = int(input('What is your bid? $\n'))
    bids[name] = price
    should_continue = input('Are there any other bidders? type "yes" or "no" ').strip().lower()
    if should_continue == 'no':
        bidding_finished = True
        find_highest_bidder(bids)
    elif should_continue == 'yes':
        clear()
