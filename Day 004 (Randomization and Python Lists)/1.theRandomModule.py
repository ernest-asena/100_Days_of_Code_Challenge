import random

# generate a whole number between 100 and 200
c = random.randint(0, 9)
myList = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
passwd = random.sample(myList, 4)
print(passwd)
print(c)

# create a random float number
floatNumber = random.random()
print(floatNumber)

# create a random decimal number between 0 and 5; multiply the  generated number by 5
random_float = random.random() * 5
print(random_float)

passwd2 = round(random.random() * 1000000)
print(passwd2)

