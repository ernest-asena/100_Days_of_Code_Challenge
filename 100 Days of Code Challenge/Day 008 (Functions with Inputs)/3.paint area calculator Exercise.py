# You are painting a wall. The instructions on the paint can says that 1 can of paint can cover 5 square meters
# of wall. Given a random height and width of wall, calculate how many cans of paint you'll need to buy.
#
# number of cans = (wall height ✖️ wall width) ÷ coverage per can.
#
# e.g. Height = 2, Width = 4, Coverage = 5
#
# number of cans = (2 ✖️ 4) ÷ 5
#
#                      = 1.6
#                      = 1.6
# But because you can't buy 0.6 of a can of paint, the result should be rounded up to 2 cans.
from math import ceil


def number_of_cans_needed(height, width):
    area = height * width
    number_of_cans_to_buy = ceil(area / 5)
    print(f"For your area, you will neeed to buy {number_of_cans_to_buy} cans of paint.")


user_height = float(input('HEIGHT:  '))
user_width = float(input('WIDTH:  '))
number_of_cans_needed(height=user_height, width=user_width)
