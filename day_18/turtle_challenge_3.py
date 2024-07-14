import turtle as turtle
from random import choice, randint

directions = [0, 90, 180, 270]
turtle.colormode(255)

def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    random_color = (r, g, b)
    return random_color

t = turtle.Turtle()
t.pensize(10)
t.speed(10)

for i in range(200):    
    t.color(random_color())
    t.forward(30)
    t.setheading(choice(directions))

screen = turtle.Screen()
screen.exitonclick()