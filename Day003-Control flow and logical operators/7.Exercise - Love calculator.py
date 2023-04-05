# Instructions
# Congratulations, you've got a job at Python Pizza. Your first job is to build an automatic pizza order program.

# Based on a user's order, work out their final bill.

# Small Pizza: $15

# Medium Pizza: $20

# Large Pizza: $25

# Pepperoni for Small Pizza: +$2

# Pepperoni for Medium or Large Pizza: +$3

# Extra cheese for any size pizza: + $1

# Example Input
# size = "L"
# add_pepperoni = "Y"
# extra_cheese = "N"
# Example Output
# Your final bill is: $28.

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

# Write your code below this line 👇

small_pizza_bill = 15
medium_pizza_bill = 20
large_pizza_bill = 25

peperoni_for_small_pizza = 2
peperoni_for_medium_and_large_pizza = 3
extra_cheese_price = 1

bill = 0

if size == 'S':
    bill = small_pizza_bill
    if add_pepperoni == 'Y':
        bill += peperoni_for_small_pizza
elif size == 'M':
    bill = medium_pizza_bill
    if add_pepperoni == 'Y':
        bill += peperoni_for_medium_and_large_pizza
elif size == 'L':
    bill = large_pizza_bill
    if add_pepperoni == 'Y':
        bill += peperoni_for_medium_and_large_pizza

if extra_cheese == 'Y':
    bill += extra_cheese_price

print(f"Total Bill to pay: {bill}")
