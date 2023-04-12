# What Causes IndexError. 
# This error occurs when an attempt is made to access an item in a list at an index which is out of bounds. 
# The range of a list in Python is [0, n-1], where n is the number of elements in the list

# In Python, an "index error" occurs when you try to access an element in a sequence (such as a list or a string) using an index that is out of range. This means that the index you have specified is either too large or too small for the sequence you are trying to access.


# Here is an example of an index error:



# my_list = [1, 2, 3]
# print(my_list[3])

# In this case, the list my_list contains three elements, and we are trying to access the fourth element (with index 3). Since the list only has three elements, an index error will occur.


# To avoid index errors, you should always make sure that the index you are using is within the range of the sequence you are trying to access. One way to do this is to use the len() function to find the length of the sequence, and then make sure that your index is less than the length of the sequence. For example:



# my_list = [1, 2, 3]
# if len(my_list) > 3:
#     print(my_list[3])
# else:
#     print("Index out of range!")

# In this case, we use the len() function to check if the length of my_list is greater than 3. Since the length of the list is only 3, we print a message indicating that the index is out of range instead of trying to access the fourth element.

dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]

fruits = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes"]
vegetables = ["Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]

print(dirty_dozen)