import turtle
import pandas

screen = turtle.Screen()
screen.title('Jogo dos Estados do Brasil')
image = 'day_25/mapa-do-brasil.gif'
screen.addshape(image)
turtle.shape(image)


data = pandas.read_csv('day_25/26_estados_1_df.csv')
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 27:
    answer_state = screen.textinput(title=f'{len(guessed_states)}/27 Estados Corretos',
                                    prompt='Qual o nome do próximo estado?').title()
    if answer_state == 'Sair':
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv('day_25/estados_para_aprender.csv')
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