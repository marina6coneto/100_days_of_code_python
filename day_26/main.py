from pandas import DataFrame, read_csv

data = read_csv('day_26/nato_phonetic_alphabet.csv')

phonetic_dict = {row.letter:row.code for (index, row) in data.iterrows()}

word = input('Enter a word: ').strip().upper()
output_list = [phonetic_dict[letter] for letter in word]
print(output_list)



