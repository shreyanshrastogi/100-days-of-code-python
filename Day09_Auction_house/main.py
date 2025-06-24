bidding = {}

def ask(a):
    name= input("name of the bidder: ")
    while True:
        try:
            bid= int(input("give bid: "))
            break
        except ValueError:
            print("please enter valid bid-")
    a[name]=bid
def highest_bidder(bidding):
    max_bid = 0
    bidder_name = ""
    for key in bidding:
        if bidding[key] > max_bid:
            max_bid = bidding[key]
            bidder_name = key
    return max_bid,bidder_name

while True:
    ask(bidding)
    over=input("are there any other bids?: yes or no? \n").strip().lower()
    if over =="no":
        break
    print("\n"*5)

max_bid,bidder_name=highest_bidder(bidding)
print(f"{bidder_name} is the winner with the bid of {max_bid}")



