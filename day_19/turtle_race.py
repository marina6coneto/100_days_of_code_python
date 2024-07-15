from turtle import Turtle, Screen
from random import randint

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

user_bet = screen.textinput(title='Make your bet!',
                            prompt='Which turtle will win the race? Enter a colour: ')
while user_bet not in colors:
    user_bet = screen.textinput(title='Invalid Color',
                     prompt="Please enter one of the following colors: red, orange, yellow, green, blue, purple.")
    
y_position = [-60, -30, 0, 30, 60, 90]
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle('turtle')
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(-230, y_position[turtle_index])
    all_turtles.append(new_turtle)

is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            break
        
        rand_distance = randint(0, 10)
        turtle.forward(rand_distance)

if winning_color == user_bet.lower().strip():
    winner_message = f"You've won! The {winning_color} turtle is the winner."
else:
    winner_message = f"You've lost. The {winning_color} turtle is the winner."

winner_turtle = Turtle()
winner_turtle.hideturtle()
winner_turtle.penup()
winner_turtle.goto(0, 0)
winner_turtle.write(winner_message, align="center", font=("Arial", 16, "bold"))

screen.exitonclick()

