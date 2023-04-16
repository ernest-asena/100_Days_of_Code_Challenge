# You are going to write a program that tests the compatibility between two people.
#
# To work out the love score between two people:

# Take both people's names and check for the number of times the letters in the word TRUE occurs.
# Then check for the number of times the letters in the word LOVE occurs. Then combine these numbers to make
# a 2 digit number.

# For Love Scores less than 10 or greater than 90, the message should be:
# "Your score is **x**, you go together like coke and mentos."

# For Love Scores between 40 and 50, the message should be:
# "Your score is **y**, you are alright together."

# Otherwise, the message will just be their score. e.g.:
# "Your score is **z**."

name_one = input('Enter your name:\nNAME::::      ')
name_two = input('Enter your partner:\nNAME::::      ')
name_two.lower()
name_one.lower()

T = name_one.count('t') + name_two.count('t')
R = name_one.count('r') + name_two.count('r')
U = name_one.count('u') + name_two.count('u')
E = name_one.count('e') + name_two.count('e')

digit_one = T + R + U + E

L = name_one.count('l') + name_two.count('l')
O = name_one.count('o') + name_two.count('o')
V = name_one.count('v') + name_two.count('v')
E = name_one.count('e') + name_two.count('e')

digit_two = L + O + V + E

love_match = str(digit_one) + str(digit_two)

# print(love_match)


if int(love_match) < 10 or int(love_match) > 90 and int(love_match) < 100:
    print(f'Your score is {love_match}, you go together like coke and mentos.')
elif 40 <= int(love_match) <= 50:
    print(f'Your score is {love_match}, you are alright together.')
elif int(love_match) > 100:
    print("That went wild!!!!. You actually have a match of over 100%.")
else:
    print(f'Your score is {love_match}')


# i could have used string concatenation at the beginning to join the two names so that i just check for
# occurrence of letters once.
#  i could also shorten that if statement and especially the conversion on love_match data type
