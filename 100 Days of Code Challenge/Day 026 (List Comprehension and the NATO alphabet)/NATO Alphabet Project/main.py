import pandas as pd

nato_alphabet = pd.read_csv('nato_phonetic_alphabet.csv')
# print(nato_alphabet)
phonetic_dict = {
                row.letter: row.code for (index, row) in nato_alphabet.iterrows()
}
# print(phonetic_dict)
word = input("Enter a Word::  ").upper()

your_result = [phonetic_dict[letter] for letter in word]

print(your_result)
