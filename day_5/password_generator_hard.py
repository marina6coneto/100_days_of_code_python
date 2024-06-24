from random import choice
from random import shuffle
print('Welcome to the PyPassoword Generator')

letters = int(input('How many letters would you like in your password? '))
symbols = int(input('How many symbols would you like in your password? '))
numbers = int(input('How many numbers would you like in your password? '))

l = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
     'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

s = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')',
    '_', '+', '{', '}', '|', ':', '"', '<', '>', '?',
    '[', ']', ';', "'", ',', '.', '/', '`', '~']

n = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

password_list = []

for char in range(1, letters + 1):
    password_list += choice(l)
     
for num in range(1,  numbers + 1):
    password_list += choice(n)
    
for sym in range(1, symbols + 1):
    password_list += choice(s)
    
shuffle(password_list)

password = ''
for new_password in password_list:
    password += new_password
    
print(f'Your password: {password}')
