from art import monalisa_image,monalisa_word
from clearScreen import ScreenClear

print('Welcome to this silent Auction where we will sell you the Mona Lisa.\nYeah, like that would ever happen!')
print(monalisa_image)

bids = {}
next_bidder = True
while next_bidder:
    print(monalisa_word)
    name = input("Hello. Please enter your name.\nNAME::  ").upper()
    bid = float(input(f'{name}.What is your bid?\nPlease enter the amount you would like to bid with.\nThe highest '
                      f'bidder goes '
                      'home with the Mona Lisa.\nYOUR BID:   $'))
    bids[name] = bid

    done = input("Is there anyone left to bid? Y/N\nMORE BIDDERS?  ").lower()
    if done == 'n':
        next_bidder = False
    ScreenClear()

print('**********************************************************************************')
print('HERE ALL THE BIDS PLACED TONIGHT!!!')
for bid in bids:
    print(bid, end=' ')
    print(bids[bid])
print('**********************************************************************************')

max_bid = 0
for bid in bids:
    if bids[bid] > max_bid:
        max_bid = bids[bid]
        max_bidder = bid

print(bids)
print('Gentlemen. We have a winner!!!The highest bidder was:,', max_bidder, 'who bid ', max_bid, '.')
print(f'{max_bidder} will go home with the Mona Lisa!!!')
print('**********************************************************************************')
