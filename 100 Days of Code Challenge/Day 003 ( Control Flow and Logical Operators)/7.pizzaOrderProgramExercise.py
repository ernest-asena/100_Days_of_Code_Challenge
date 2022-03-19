# Congratulations, you've got a job at Python Pizza. Your first job is to build an automatic
#  pizza order program.
# Based on a user's order, work out their final bill.
# Large Pizza: $25
# Medium Pizza: $20
# Small Pizza: $15
# Pepperoni for Small Pizza: +$2
# Pepperoni for Medium or Large Pizza: +$3
# Extra cheese for any size pizza: + $1

L_price = 25
M_price = 20
S_price = 15
peperoni_for_small_pizza = 2
peperoni_for_other = 3
extra_cheese = 1
print('Welcome to The NSCantina Pizza Joint!!')
pizza_size = input("What size of pizza would you like? L, S, M.\nSIZE::  ")
add_cheese = input("Would you like extra cheese for $1?\nY or N:  ")
add_peperoni = input("Would you like to add Peperoni?\nY or N:  ")

bill = 0
if pizza_size == 'L':
    bill = L_price
elif pizza_size == 'S':
    bill = S_price
else:
    bill = M_price

if add_cheese == 'Y':
    bill += 1

if add_peperoni == 'Y':
    if pizza_size == 'S':
        bill += 2
    else:
        bill += 3
print(f'Your Total bill is ${bill}.')



