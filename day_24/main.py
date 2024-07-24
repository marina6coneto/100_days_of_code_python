PLACEHOLDER = '[name]'

with open('day_24/input/names/invited_names.txt') as names_files:
    names = names_files.readlines()
    
    
with open('day_24/input/letters/starting_letter.txt') as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_names = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_names)
        with open(f'day_24/output/readytosend/letter_for_{stripped_names}.txt', mode='w') as completed_letter:
            completed_letter.write(new_letter)
