from tkinter import Tk, Canvas, PhotoImage, Button, Label, Entry, END, messagebox
from random import choice, randint, shuffle
import pyperclip
import json

# -------------------------- PASSWORD GENERATOR ----------------------------- #

def generator_password():
    
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
               'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
               'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
               'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
   
    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)

    password = "".join(password_list)
    input_3.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = input_1.get()
    email = input_2.get()
    password = input_3.get()
    new_data = {
        website: {
            'email': email,
            'password': password,
        }
        
    }  
    
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title='Oops',
                            message="Please, make suke you haven't left any fiels empty.")
    else:
        try:        
            with open('day_30/data.json', 'r') as data_file:
                #Reading old data            
                data = json.load(data_file)
        except FileNotFoundError:
            with open('day_30/data.json', 'w') as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            #Update old data with new data
            data.update(new_data)
            with open('day_30/data.json', 'w') as data_file:
                #Saving update data
                json.dump(data, data_file, indent=4)
        finally:  
            input_1.delete(0, END)
            input_3.delete(0, END)  
            
# ---------------------------- FIND PASSWORD  ------------------------- #

def find_password():
    website = input_1.get()
    try:
        with open('day_30/data.json') as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title='ERROR', message='No Data File Found')
    else:
        if website in data:
            email = data[website]['email']
            password = data[website]['password']
            messagebox.showinfo(title=website,
                                message=f'Email: {email}\nPassword: {password}')
        else:
            messagebox.showinfo(title='ERROR',
                                message=f'No details for {website} exists.')
            
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
photo = PhotoImage(file='day_30/logo.png')
canvas.create_image(100,100, image=photo)
canvas.grid(column=2, row=1)

#Labels
label_1 = Label(text='Website:', font=('Arial',  10 ))
label_1.grid(column=1, row=2)

label_2 = Label(text='Email/Username:', font=('Arial',  10 ))
label_2.grid(column=1, row=3)

label_3 = Label(text='Password:', font=('Arial',  10 ))
label_3.grid(column=1, row=4)

#Buttons
button_1 = Button(text='Generate Password', font=('Arial',  10 ),
                  highlightthickness=0, width=14, command=generator_password)
button_1.grid(column=3, row=4)

button_2 = Button(text='Add', font=('Arial',  10 ),
                  highlightthickness=0, width=40, command=save)
button_2.grid(column=2, row=5, columnspan=2)

search_button = Button(text='Search', font=('Arial', 10),
                       highlightthickness= 0, width=14, command=find_password)
search_button.grid(column=3, row=2)

#Inputs
input_1 = Entry(width=33)
input_1.grid(column=2, row=2)
input_1.focus()

input_2 = Entry(width=53)
input_2.grid(column=2, row=3, columnspan=2)
input_2.insert(0, 'santoscmarina@hotmail.com')

input_3 = Entry(width=33)
input_3.grid(column=2, row=4)

window.mainloop()
