from tkinter import Tk, Canvas, PhotoImage, Button
from pandas import read_csv, DataFrame
from random import choice


BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

try:
    data = read_csv('day_31/data/words_to_learn.csv')
except FileNotFoundError:
    original_data = read_csv('day_31/data/english_words.csv')
    to_learn = original_data.to_dict(orient='records')
else:
    to_learn = data.to_dict(orient='records')

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = choice(to_learn)
    canvas.itemconfig(card_title, text='English', fill='black')
    canvas.itemconfig(card_word, text=current_card['English'], fill='black')
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)
 
def flip_card():
    canvas.itemconfig(card_title, text='Portuguese', fill='white')
    canvas.itemconfig(card_word, text=current_card['Portuguese'],  fill='white')
    canvas.itemconfig(card_background, image=card_back_img)
    
def is_known():
    to_learn.remove(current_card)
    data = DataFrame(to_learn)
    data.to_csv('day_31/data/words_to_learn.csv', index=False)
    next_card()

window = Tk()
window.title('Flashy')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file='day_31/images/card_front.png')
card_back_img = PhotoImage(file='day_31/images/card_back.png')
card_background = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text='', font=('Arial', 35, 'italic'))
card_word = canvas.create_text(400, 300, text='', font=('Arial', 60, 'bold'))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

cross_image = PhotoImage(file='day_31/images/wrong.png')
unknown_button = Button(image=cross_image, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file='day_31/images/right.png')
known_button = Button(image=check_image, highlightthickness=0, command=is_known)
known_button.grid(row=1, column=1)

next_card()

window.mainloop()