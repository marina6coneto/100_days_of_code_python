from random import randint

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

images = [rock, paper, scissors]

user_choice = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n'))

print(images[user_choice])

computer_choice = randint(0,2)
print('Computer chose:')
print(images[computer_choice])

if user_choice >= 3 or user_choice < 0:
    print('You typed an invalid number, you lose!')
    
elif user_choice == computer_choice:
    print("It's a draw.")
    
elif user_choice == 0 and computer_choice == 2:
    print('YOU WIN!')
    
elif user_choice == 1 and computer_choice == 0:
    print('YOU WIN!')

elif user_choice == 2 and computer_choice == 1:
    print('YOU WIN!')
    
else: 
    print('YOU LOSE!')
    
    
    
