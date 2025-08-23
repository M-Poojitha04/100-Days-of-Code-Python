import pandas
data = pandas.read_csv("nato_phonetic_alphabet.csv")
#TODO 1. Create a dictionary in this format:
dictionary = {row.letter:row.code for (index, row) in data.iterrows()}
# {"A": "Alfa", "B": "Bravo"}
print(dictionary)
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter a word: ").upper()
list_of_words = [dictionary[letter] for letter in word]

print(list_of_words)