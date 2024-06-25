from random import choice
from hangman_words import word_list
from hangman_arts import logo, stages

print(logo)
word = choice(word_list)
word_length = len(word)
display = []
end_of_the_game = False
lives = 6

for i in range(word_length):
    display += '_'
print(f'{' '.join(display)}')

while not end_of_the_game:

    guess = input('Guess a letter: ').lower()
    
    if guess in display:
      print(f"You've already chosen this letter {guess}")

    for position in range(word_length):
        letter = word[position]
        #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
          display[position] = letter
          
    if guess not in word:
      print(f"You guessed {guess}, that's not in the word. You lose a life.")
      lives -= 1
      if lives == 0:
        end_of_the_game = True
        print("GAME OVER. YOU'VE LOST! HAHAHAHA")
          
    print(f'{' '.join(display)}')
           
    if '_' not in display:
        end_of_the_game = True
        print('You win!')
        
    print(stages[lives])
        