
import pandas as pd

data = pd.read_csv("nato_phonetic_alphabet.csv")
#print(data.to_dict())

#TODO 1. Create a dictionary in this format:
phonetic_dict = {row.letter:row.code for (index, row) in data.iterrows()}
#print(phonetic_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter a word: ").upper()
nato_word = [phonetic_dict[l] for l in word]
print(nato_word)

