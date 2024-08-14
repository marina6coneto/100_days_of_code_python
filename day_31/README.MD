# Day 31: Flashcard Learning Application

- This is a flashcard learning application developed using Python's Tkinter library.
- The application helps users learn new English words by showing them flashcards with the English word on one side and the Portuguese translation on the other.
- Users can mark words they know, and those words will be removed from future sessions, helping them focus on words they still need to learn.
- This project is part of the "100 Days of Code: The Complete Python Pro Bootcamp" by Angela Yu on Udemy.

## Features

- **Flashcards with English and Portuguese Words**: Displays an English word on the front of the card, with a corresponding Portuguese translation on the back.
- **Interactive Learning**: Users can mark a word as known, and the app will save the progress, ensuring that the word won't be shown again in future sessions.
- **Automatic Card Flipping**: The card flips automatically after 3 seconds, revealing the translation.
- **Save and Load Progress**: Progress is saved to a CSV file, so you can continue learning from where you left off.

## How to Run the Project

1. Ensure you have Python installed on your system.
2. Install the required packages by running:
   ```bash
   pip install pandas
   ```
3. Place the following directory structure in your project folder:
   ```
   └── day_31
       ├── data
       │   ├── english_words.csv
       │   └── words_to_learn.csv (This file will be created automatically after the first run)
       └── images
           ├── card_front.png
           ├── card_back.png
           ├── right.png
           └── wrong.png
   ```
4. Run the script using:
   ```bash
   python main.py
   ```

## File Structure

- **main.py**: The main Python script that runs the flashcard application.
- **data/english_words.csv**: Contains the list of English words and their corresponding Portuguese translations.
- **data/words_to_learn.csv**: Stores the words that the user still needs to learn. This file is updated each time the user marks a word as known.
- **images/**: Contains the image files used for the flashcards and buttons.

## How It Works

1. **Data Loading**: The application first attempts to load the `words_to_learn.csv` file to continue from where the user last left off. If this file doesn't exist, it loads the initial set of words from `english_words.csv`.
2. **Flashcard Display**: A random word from the list of words to learn is selected and displayed on the flashcard.
3. **Card Flipping**: After 3 seconds, the flashcard automatically flips to show the Portuguese translation.
4. **User Interaction**: The user can click the "✓" button if they know the word or the "✗" button if they don't. If the word is known, it is removed from the list, and the list is saved back to the `words_to_learn.csv` file.
5. **Next Word**: The next word is then displayed.

## Requirements

- Python 
- Tkinter (usually included with Python)
- Pandas library

## Screenshots

![Flashcard Front](images/card_front.png)
*Example of the flashcard displaying an English word.*

![Flashcard Back](images/card_back.png)
*Example of the flashcard displaying the Portuguese translation.*


*This project is part of the "100 Days of Code: The Complete Python Pro Bootcamp" by Angela Yu on Udemy.*
