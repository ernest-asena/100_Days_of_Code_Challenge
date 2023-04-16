height = int(input('Enter your height in cm.\nHEIGHT::  '))
bill = 0
if height >= 120:
    print('You can ride!')
    age = int(input('Enter your age in numbers.\nAGE::  '))
    if age < 12:
        bill = 5
        print('Child Ticket. You pay $5.')
    elif 12 <= age <= 18:  # elif age <=18 will also work just fine
        bill = 7
        print("Youth Ticket. You pay $7")
    else:
        bill = 12
        print('Adult Ticket. You pay $12.')

    wants_photo = input('Would you like a photo as well?\nPlease type Y or N:  ')
    wants_photo = wants_photo.capitalize()

    if wants_photo == 'Y':
        bill += 3
    print(f'Your total bill will be {bill}.')
    # else:
    #     print(f'Your total bill will be {bill}')

else:
    print('Sorry. You are not tall enough to ride!')
