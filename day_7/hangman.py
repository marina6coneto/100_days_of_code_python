from random import choice
from hangman_words import word_list
from hangman_arts import logo, stages

print(logo)
word = choice(word_list)
word_length = len(word)
display = ['_' for _ in range(word_length)]
end_of_the_game = False
lives = 6
guessed_letters = []  

print(' '.join(display))

while not end_of_the_game:

  guess = input('Guess a letter: ').lower()

  if guess in guessed_letters:
    print(f"You've already chosen the letter '{guess}'. Try again.")
    continue

  guessed_letters.append(guess)

  if guess not in word:
    print(f"You guessed '{guess}', that's not in the word. You lose a life.")
    lives -= 1
    if lives == 0:
      end_of_the_game = True
      print(f"GAME OVER. YOU'VE LOST! The word was '{word}'.")
      break

  for position in range(word_length):
    letter = word[position]
    if letter == guess:
      display[position] = letter

  print(' '.join(display))

  if '_' not in display:
    end_of_the_game = True
    print('CONGRATULATIONS! You win!')

  print(stages[lives])
