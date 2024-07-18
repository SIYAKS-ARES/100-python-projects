import os
from art import logo

print(logo)
print("Welcome to the Secret Auction")
# auction = []
auction = {}

def blind_auction(name, bid):
    bid_dict = {name: bid}
    # auction.append(bid_dict)
    auction.update(bid_dict)

is_continue = True
while is_continue:
    name = input("What is your name? ")
    bid = int(input("What is your bid? $"))
    bid_dict = blind_auction(name, bid)
    choice = input("Are there any other bidders? Type 'yes' or 'no'\n")

    if choice == "no":
        is_continue = False
    else:
        is_continue = True
        os.system('clear')


# print(f"Auction results: {auction}")

highest_bid = 0
winner = ""

for bidder in auction:
    # bid_amount = list(bidder.values())[0]
    bid_amount = auction[bidder]
    if bid_amount > highest_bid:
        highest_bid = bid_amount
        # winner = list(bidder.keys())[0]
        winner = bidder

print(f"The winner is {winner} with a bid of ${highest_bid}")