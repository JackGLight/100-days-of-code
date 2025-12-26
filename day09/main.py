'''
Day 9 Secret Auction game 
'''

"""Get the highest bid and return the amount and who bid it"""
def compare_bids(bids):
    highest_bidder = max(bids, key=bids.get)
    return highest_bidder, bids[highest_bidder]


"""initialize more bidders as yes and an empty dict of bids"""
more_bidders = "yes"
bids = {}

"""main loop to collect bidders and bids before confirming no more bidders"""
while not more_bidders == "no":

    bidder = input("Please enter your name")
    bid = float(input("What is your bid amount?: $"))

    bids[bidder] = bid

    more_bidders = input("Are there more bidders?\n").lower()
    print("\n" * 50)

winner, winning_amount = compare_bids(bids)
print(f"The winner is {winner}")
print(f"With a winning bid of ${winning_amount}")