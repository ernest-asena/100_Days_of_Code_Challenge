print("Welcome to the roller coaster!")
height = int(input("What is your height in cm? "))

if height > 120:
    print("You can ride!")
    age = int(input("Enter age: "))
    if age < 12:
        print("You pay $5")
    elif age <= 18:
        print("You pay $7")
    else:
        print("You pay $12")
else:
    print("Sorry, you gotta grow taller!!")