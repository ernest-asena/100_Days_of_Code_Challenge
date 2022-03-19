# Take a look inside file1.txt and file2.txt. They each contain a bunch of numbers, each number on a new line.
# You are going to create a list called result which contains the numbers that are common in both files.
with open('file1.txt', 'r') as file_one:
    list_1 = file_one.readlines()

with open('file2.txt', 'r') as file_two:
    list_2 = file_two.readlines()


result = [int(item) for item in list_1 if item in list_2]
print(result)

