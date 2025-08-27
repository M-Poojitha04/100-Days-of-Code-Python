import pandas
data = pandas.read_csv("nato_phonetic_alphabet.csv")

dictionary = {row.letter:row.code for (index, row) in data.iterrows()}
print(dictionary)

def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        list_of_words = [dictionary[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please")
        generate_phonetic()
    else:
        print(list_of_words)

generate_phonetic()