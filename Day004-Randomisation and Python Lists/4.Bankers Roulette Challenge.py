# Instructions
# You are going to write a program that will select a random name from a list of names. The person selected will have to pay for everybody's food bill.

# Important: You are not allowed to use the choice() function.

# Line 8 splits the string names_string into individual names and puts them inside a List called names. For this to work, you must enter all the names as names followed by comma then space. e.g. name, name, name

# Example Input
# Angela, Ben, Jenny, Michael, Chloe
# Note: notice that there is a space between the comma and the next name.

# Example Output
# Michael is going to buy the meal today!

import random

names = input("Enter the names of people at the table.\nSeparate ecah name with a comma:: ")


list_names = names.split(",")

print(list_names)

random_number = random.randint(0, len(list_names)-1)

# person_to_pay = random.choice(list_names)
person_to_pay = list_names[random_number]

print(f"{person_to_pay} will pay today's bill!")
