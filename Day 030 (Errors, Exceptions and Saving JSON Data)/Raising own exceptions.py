# try:
#     file = open('a_file.txt', 'r')
#     dict_try = {'key': 'value'}
#     dict_try['key']
# except FileNotFoundError:
#     file = open('a_file.txt', 'w')
#     file.write('something')
# except KeyError as error_message:
#     print(F'The key {error_message} does not exist.')
# else:
#     content=file.read()
#     print(content)
# finally:
#     raise TypeError("There is nno error actually. I made this up.")
#

height = float(input("Enter HEIGHT:: "))

if height > 3:
    raise ValueError("Height should not be over 3 meters.")

weight = float(input("Enter WEIGHT:: "))


bmi = weight / height ** 2
print(bmi)