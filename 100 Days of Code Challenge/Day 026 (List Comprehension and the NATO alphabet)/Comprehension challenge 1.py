# You are going to write a List Comprehension to create a new list called squared_numbers.
# This new list should contain every number in the list numbers but each number should be squared.

numbers = [3, 5, 7, 9, 3, 22, 88, 10]
squared_numbers = [number**2 for number in numbers]
print(numbers)
print(squared_numbers)