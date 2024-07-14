from turtle import Turtle, Screen
from random import choice

colours = ['medium aquamarine', 'medium violet red',
           'spring green', 'dodger blue', 'orange red',
           'light sea green', 'salmon', 'blue' ]
directions = [0, 90, 180, 270]

turtle = Turtle()
turtle.pensize(10)
turtle.speed(10)

for i in range(200):    
    turtle.color(choice(colours))
    turtle.forward(30)
    turtle.setheading(choice(directions))

screen = Screen()
screen.exitonclick()
