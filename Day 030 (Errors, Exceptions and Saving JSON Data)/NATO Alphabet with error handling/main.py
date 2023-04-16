import pandas as pd

nato_alphabet = pd.read_csv('nato_phonetic_alphabet.csv')
# print(nato_alphabet)
phonetic_dict = {
    row.letter: row.code for (index, row) in nato_alphabet.iterrows()
}


# print(phonetic_dict)
# try:

def generate_phonetic():
    word = input("Enter a Word::  ").upper()

    try:
        your_result = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Sorry. Only letters are allowed.")
        generate_phonetic()
    else:
        print(your_result)

