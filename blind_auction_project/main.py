
# HINT: You can call clear() to clear the output in the console.
from art import logo

print(logo)
players = {}
bidding_finished = False


def find_higgest_bidder(bidding_record):
    winner = ""
    max_bid = 0
    for i in players:
        bid_amount = players[i]
        if bid_amount > max_bid:
            max_bid = bid_amount
            winner = i
    print(f"The winner is {winner} with the bid of ${max_bid}")


while not bidding_finished:

    name = input("What is your name : ")
    bid_price = int(input("What is your bid price : "))
    players[name] = bid_price
    choice = input("Are there any other user who want to bid : yes/no : ").lower()
    if choice == "no":
        bidding_finished = True
        find_higgest_bidder(players)
    elif choice == "yes":
        bidding_finished = False



