import random
# Dictionaries (or dict in Python) are a way of storing elements just like you would in a Python list. But,
# rather than accessing elements using its index, you assign a fixed key to it and access the element using the key.
# What you now deal with is a "key-value" pair, which is sometimes a more appropriate data structure for many problem
# instead of a simple list. You will often have to deal with dictionaries when doing data science, which makes
# dictionary comprehension a skill that you will want to master.
# A dictionary in Python is a collection of items accessed by a specific key rather than by index. What does this mean?

# Imagine a dictionary in the real world... when you need to look up the meaning of a word, you try to find the
# meaning using the word itself and not the possible index of the word. Python dictionaries work with the same
# concept, the word whose meaning you are looking for is the key and the meaning of the word is the value,
# you do not need to know the index of the word in a dictionary to find its meaning.

# Dictionary comprehension is a method for transforming one dictionary into another dictionary. During this
# transformation, items within the original dictionary can be conditionally included in the new dictionary and each
# item can be transformed as needed.

# A good list comprehension can make your code more expressive and thus, easier to read. The key with creating
# comprehensions is to not let them get so complex that your head spins when you try to decipher what they are
# actually doing. Keeping the idea of "easy to read" alive.

names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
# student_scores = {new_key:new_value for item in names}
student_scores = {student:random.randint(1, 100) for student in names}
print(student_scores)

# Return a dictionary with students who passed only
# passed_students = {new_key:new_value for (key, value) in dictionary.items}
passed_students = {
    student:score for (student, score) in student_scores.items() if score > 60
}
print('passed students:', passed_students)
failed_students = {
    student:score for (student, score) in student_scores.items() if score < 60
}

print('failed students: ', failed_students)