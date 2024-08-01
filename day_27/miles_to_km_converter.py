from tkinter import Tk, Label, Button, Entry

def miles_to_km():
    miles = input.get()
    try:
        miles_float = float(miles)
        km = miles_float * 1.60934
        label_3.config(text=f'{km:.2f}')
    except:
        label_3.config(text='Invalid Input')
        
window = Tk()
window.title('Miles to KM converter')
window.minsize(width=230, height=100)
window.config(padx=30, pady=30)

input = Entry(width=7)
input.grid(column=2, row=1)

label_1 = Label(text='Miles', font=('Arial', 10))
label_1.grid(column=3, row=1)

label_2 = Label(text='is equal to', font=('Arial', 10))
label_2.grid(column=1, row=2)

label_3 = Label(text=0, font=('Arial', 10))
label_3.grid(column=2, row=2)

label_4 = Label(text='Km', font=('Arial', 10))
label_4.grid(column=3, row=2)

button = Button(text='Calculate', command=miles_to_km)
button.grid(column=2, row=3)

window.mainloop()