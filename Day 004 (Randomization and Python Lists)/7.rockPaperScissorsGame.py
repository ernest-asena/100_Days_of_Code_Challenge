import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
while True:
    print("Welcome to the Rock Paper Scissors Game!")
    options = ['rock', 'paper', 'scissors']
    User_choice = input("Let's Get Started. Make a Choice. Rock, Paper or Scissors.\nYOUR "
                        "CHOICE::  ")
    User_choice = User_choice.lower()

    Computer_choice = random.choice(options)

    if User_choice == 'rock':
        print(f'YOU CHOSE ROCK: {rock}')
    elif User_choice == 'paper':
        print(f'YOU CHOSE PAPER:  {paper}')
    elif User_choice == 'scissors':
        print(f'YOU CHOSE SCISSORS: {scissors}')
    else:
        print('What are you doing boy')

    if Computer_choice == options[0]:
        print(f'Computer Chose Rock: {rock}')
    elif Computer_choice == options[1]:
        print(f"Computer Chose Paper: {paper}")
    elif Computer_choice == options[2]:
        print(f"Computer chose Scissors: {scissors}")

    if User_choice == Computer_choice:
        print("WELL YOU ARE NOT VERY EASY TO BEAT. IT IS A DRAW!")
    elif User_choice != Computer_choice:
        if User_choice == 'rock' and Computer_choice == 'paper':
            print("BETTER LUCK NEXT TIME. YOU LOSE.")
        elif User_choice == 'rock' and Computer_choice == 'scissors':
            print('CONGRATULATIONS MASTER. YOU WIN!!! HATS OFF TO YOU!')
        elif User_choice == 'paper' and Computer_choice == 'rock':
            print('CONGRATULATIONS MASTER. YOU WIN!!! HATS OFF TO YOU!')
        elif User_choice == 'paper' and Computer_choice == 'scissors':
            print("BETTER LUCK NEXT TIME. YOU LOSE.")
        elif User_choice == 'scissors' and Computer_choice == 'rock':
            print("BETTER LUCK NEXT TIME. YOU LOSE.")
        elif User_choice == 'scissors' and Computer_choice == 'paper':
            print('CONGRATULATIONS MASTER. YOU WIN!!! HATS OFF TO YOU!')

        play_again = input("Play again? (y/n): ")
        if play_again.lower() != "y":
            break
