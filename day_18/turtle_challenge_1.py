from turtle import Turtle, Screen
from random import choice

my_form = Turtle()
colours = ['medium aquamarine', 'medium violet red',
           'spring green', 'dodger blue', 'orange red',
           'light sea green', 'salmon', 'blue' ]

def draw_shape(num_sides):
    angle = 360 / num_sides
    for i in range(num_sides):        
        my_form.forward(100)
        my_form.right(angle)
        
for shape_side_n in range (3, 11):
    my_form.color(choice(colours))
    draw_shape(shape_side_n)
    
screen = Screen()
screen.exitonclick()