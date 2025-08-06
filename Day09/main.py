import art
print(art.logo)
# TODO-1: Ask the user for input
def high_bidder(bid_dict):
    max_bid = 0
    max_bidder = ""
    for key in bid_dict:
        if bid_dict[key] > max_bid:
            max_bid = bid_dict[key]
            max_bidder = key
    print(f"The bidding winner is: {max_bidder} with highest bid of ${max_bid}")
        # TODO-4: Compare bids in dictionary
bids = True
bidding_dict = {}
while bids:
    name = input("Enter your name : ")
    bid = int(input("Enter bid amount : $"))
    # TODO-2: Save data into dictionary {name: price}

    bidding_dict[name] = bid

    # TODO-3: Whether if new bids need to be added
    new_bids = input("If there are new bids to add? type 'yes' else type 'no':\n").lower()
    if new_bids == 'yes':
        print("\n" * 20)
        bids = True
    else :
        bids = False
        high_bidder(bidding_dict)