# Password Generator Project

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\nEnter Here:  "))
nr_symbols = int(input(f"How many symbols would you like?\nEnter Here: "))
nr_numbers = int(input(f"How many numbers would you like?\nEnter Here: "))

# Easy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91


# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

passwd_letters = random.sample(letters, nr_letters)
passwd_symbols = random.sample(symbols, nr_symbols)
passwd_numbers = random.sample(numbers, nr_numbers)

# print(passwd_numbers)
# print(passwd_symbols)
# print(passwd_letters)


Generated_Password = passwd_letters + passwd_numbers + passwd_symbols

print("Your passWord is:\n: ")
print(*Generated_Password, sep='')

print("****************")
random.shuffle(Generated_Password)
print()
print()
print("Shuffled Password is:\n:")
print(*Generated_Password, sep='')

print('######################## INSTRUCTOR METHOD ############################')
# ################################### INSTRUCTOR METHOD1 #############################
passwd2 = ''
for letter in range(1, nr_letters + 1):
    passwd2 += random.choice(letters)

for symbol in range(1, nr_symbols + 1):
    passwd2 += random.choice(symbols)

for number in range(1, nr_numbers + 1):
    passwd2 += random.choice(numbers)

print(f'YOUR PASSWORD IS: {passwd2}')

############################## METHOD2 TWO WITH SHUFFLING #####################
print("############ INSTRUCTOR METHOD TWO WITH DIFFERENT WAY TO TURN IT INTO STRING#####################")
passwd3 = []
for letter in range(1, nr_letters + 1):
    passwd3.append(random.choice(letters))

for symbol in range(1, nr_symbols + 1):
    passwd3.append(random.choice(symbols))

for number in range(1, nr_numbers + 1):
    passwd3.append(random.choice(numbers))

random.shuffle(passwd3)
# turn it into a string

pass_shuffled = ""
for char in passwd3:
    pass_shuffled += char

print(f'YOUR PASSWORD IS: {pass_shuffled}')
