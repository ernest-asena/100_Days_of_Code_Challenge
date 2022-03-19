# You are going to use Dictionary Comprehension to create a dictionary called result that takes each word in the
# given sentence and calculates the number of letters in each word.
# Do NOT Create a dictionary directly. Try to use Dictionary Comprehension instead of  a Loop.
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
sentence = sentence.split()
print(sentence)

word_length = {
    word:len(word) for word in sentence
}
print(word_length)


# Count how many times each word occurs!
word_count = {
    word:sentence.count(word) for word in sentence
}

print(word_count)

# To get count of each letter;

sentence = list(sentence)
# print(sentence)
# print(sentence.count('w'))
letter_count = {
    letter: sentence.count(letter) for letter in sentence if letter != ' '
}

print(letter_count)