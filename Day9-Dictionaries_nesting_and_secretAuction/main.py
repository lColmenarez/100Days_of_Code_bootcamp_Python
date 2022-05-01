from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo
print(logo)
print("Welcome to the auction bid program by Luis")

bids = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
  highest_bid = 0
  winner = ''
  for bidder in bidding_record:
    bid_ammount = bidding_record[bidder]
    if bid_ammount > highest_bid:
      highest_bid = bid_ammount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}")

while not bidding_finished:
  name = input("What is your name?: ")
  price = int(input("What is your bid?: $"))
  bids[name] = price
  should_continue = input("Are there any other bidders? Type 'yes' or 'no'. \n")
  if should_continue == "no":
    bidding_finished == True
    find_highest_bidder(bids)
  elif should_continue == "yes":
    clear()
  else:
    print("Not valid option, please type 'yes' or 'no'\n")
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'. \n")