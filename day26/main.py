
import pandas as pd

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

data = pd.read_csv("nato_phonetic_alphabet.csv")
print(data.head())

nato_dict = {}
for (index, row) in data.iterrows():
    nato_dict[row.letter] = row.code

print(nato_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

user_input = ""
while not user_input.isalpha():
    user_input = input("Please provide the word to translate: ").upper()

code_list = []
for letter in user_input:
    code_list.append(nato_dict[letter])

print(code_list)





