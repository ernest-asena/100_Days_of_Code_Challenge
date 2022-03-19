print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
# checkout ascii.co.uk/art
direction1 = input('You are at a crossroad here!! Which direction would you like to go? Left or Right?\n::::  ')
direction1 = direction1.lower()
if direction1 == 'right':
    print('For some reason, Game over!!')
else:
    swim_or_wait = input('Well here is a lake. Will you swim to the other side or wait for a boat?\nSwim or Wait?:  ')
    swim_or_wait = swim_or_wait.lower()
    if swim_or_wait == 'swim':
        print('Game over. The sharks have eaten your ass bitch')
    elif swim_or_wait == 'wait':
        door_choice = input('Choose one door.\nRed, Blue or Yellow?:  ')
        door_choice.lower()
        if door_choice == 'red':
            print('Game over. The house is wicked.')
        elif door_choice == 'blue':
            print('Game over. The house is too cold.')
        elif door_choice == 'yellow':
            print('*****CONGRATULATIONS!!!!! You FOUND THE TREASURE!!.*****')

