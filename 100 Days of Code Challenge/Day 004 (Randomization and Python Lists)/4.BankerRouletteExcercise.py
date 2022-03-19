# You are going to write a program which will select a random name from a list of names.
# The person selected will have to pay for everybody's food bill.
#
# Important: You are not allowed to use the choice() function.
#
# Line 8 splits the string names_string into individual names and puts them inside a List called names.
# For this to work, you must enter all the names as name followed by comma then space. e.g. name, name, name

import random
names = input('Enter the names here.\nType your name followed by a comma.\nNAMES:  ')
# print(names)
names_formatted = names.split(',')
# print(names_formatted)
random_no = random.randint(0, len(names_formatted))

person_to_pay_bill = names_formatted[random_no]

print(f'{person_to_pay_bill} to pay the bill!')

# the random.choice() could do the same thing here.
