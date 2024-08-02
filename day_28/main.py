from tkinter import Tk, Canvas, PhotoImage, Button, Label
import math

# ---------------------------- CONSTANTS --------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
check_mark = '✔'
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global timer
    if timer is not None:
        window.after_cancel(timer)
        timer = None
    canvas.itemconfig(timer_text, text='00:00')
    label_1.config(text='Timer')
    label_2.config(text='')
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM --------------------------- #
def start_timer():
    global reps
    reps += 1
    
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    
    if reps % 8 == 0:
        count_down(long_break_sec)
        label_1.config(text='Break', fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        label_1.config(text='Break', fg=PINK)
    else:
        count_down(work_sec)
        label_1.config(text='Work', fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ----------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f'0{count_sec}'
    
    canvas.itemconfig(timer_text, text=f'{count_min}:{count_sec}')
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ''
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += check_mark
        label_2.config(text=marks)

# ---------------------------- UI SETUP ---------------------------------- #
window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='day_28/tomato.png')  # Verifique se o caminho da imagem está correto
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text='00:00', fill='white', font=(FONT_NAME, 28, 'bold'))
canvas.grid(column=2, row=2)

button_1 = Button(text='Start', font=(FONT_NAME, 10, 'bold'), highlightthickness=0, command=start_timer)
button_1.grid(column=1, row=3)

button_2 = Button(text='Reset', font=(FONT_NAME, 10, 'bold'), highlightthickness=0, command=reset_timer)
button_2.grid(column=3, row=3)

label_1 = Label(text='Timer', fg=GREEN, bg=YELLOW, font=(FONT_NAME, 30, 'bold'))
label_1.grid(column=2, row=1)

label_2 = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20, 'bold'))
label_2.grid(column=2, row=4)

window.mainloop()
