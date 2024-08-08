from pandas import read_csv

data = read_csv('day_26/nato_phonetic_alphabet.csv')

phonetic_dict = {row.letter:row.code for (index, row) in data.iterrows()}

def generate_phonetic():
    word = input('Enter a word: ').strip().upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print('Sorry, only letter in the alphabet please.')
        generate_phonetic()
    else:
        print(output_list)
        
generate_phonetic()



