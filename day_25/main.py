import turtle
import pandas

screen = turtle.Screen()
screen.title('U.S. States Game')
image = 'day_25\\blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv('day_25\\50_states.csv')
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f'{len(guessed_states)}/50 States Correct',
                                    prompt="What's another State's name?").title()
    if answer_state == 'Exit':
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv('day_25/states_to_learn.csv')
        break    
        
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        x = int(state_data.x.item())
        y = int(state_data.y.item())
        t.goto(x, y)
        t.write(answer_state)