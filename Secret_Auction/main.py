from art import logo

# Display the Secret Auction ASCII logo
print(logo)


def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    # Loop through each bidder in the dictionary to find the highest bid
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")


# Dictionary to store each bidder's name and bid amount
bids = {}
continue_bidding = True

while continue_bidding:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    bids[name] = price

    should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
    if should_continue == "no":
        continue_bidding = False
        find_highest_bidder(bids)
    elif should_continue == "yes":
        # Clear the terminal screen so the next bidder cannot see previous bids
        print("\n" * 20)
