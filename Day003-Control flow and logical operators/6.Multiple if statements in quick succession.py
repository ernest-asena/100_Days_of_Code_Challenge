print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

bill = 0

if height > 120:
    print("You can ride!")
    age = int(input("Enter your age:: "))
    if age < 12:
        print("Child tickets:: $5")
        bill = 5
    elif age <= 18:
        print("Youth tickets:: $7")
        bill = 7
    else:
        print("Adult tickets:: $12")
        bill = 12
    wants_photo = input("Do you want a photo? Y/N")
    if wants_photo == 'Y':
        bill += 3
    print(f"Your final bill is: {bill}.")
else:
    print("Sorry you can't ride today. Gotta grow taller!!")