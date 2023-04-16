import random
from noguessart import logo

# Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).


EASY_LEVEL = 10
HARD_LEVEL = 5

random_no = random.randint(1, 100)
print(logo)
print("I am thinking of a number between 1 and 100.\nSelect a difficulty level below and see if you can get it Right.")
difficulty = input('What difficulty level will you play?\nHARD/EASY?  ').lower()

if difficulty == 'easy':
    guesses = 10
    win = 'not win'
    while guesses > 0 and win != 'win':
        print(f'You have {guesses} remaining.')
        user_guess = int(input('PLEASE ENTER YOUR NUMBER HERE:\nGUESS::   '))
        if user_guess == random_no:
            win = 'win'
            print(f'YOU WIN. THE NUMBER WE WANTED WAS {random_no}.')
        elif user_guess < random_no:
            print('Your guess is lower than my number.')
            guesses -= 1
        else:
            print('Your Guess is higher than my number.')
            guesses -= 1

        if guesses == 0:
            print("You have run out of guesses to make. You LOSE!")
            print(f"The number we wanted was {random_no}")

if difficulty == 'hard':
    guesses = 5
    win = 'not win'
    while guesses > 0 and win != 'win':
        print(f'You have {guesses} attempts Remaining.')
        user_guess = int(input('PLEASE ENTER YOUR NUMBER HERE:\nGUESS::   '))
        if user_guess == random_no:
            win = 'win'
            print(f'YOU WIN. THE NUMBER WE WANTED WAS {random_no}.')
        elif user_guess < random_no:
            print('Your guess is lower than my number.')
            guesses -= 1
        else:
            print('Your Guess is higher than my number.')
            guesses -= 1

        if guesses == 0:
            print("You have run out of guesses to make. You LOSE!")
            print(f"The number we wanted was {random_no}.")


