import turtle
import pandas

screen = turtle.Screen()
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)


all_states = pandas.read_csv('./50_states.csv')

states_list = all_states.state.to_list()


guessed_states = []


while len(guessed_states) < 50:

    answer_state = screen.textinput(title='Guess The State '+ str(len(guessed_states)) + '/50', prompt="What's the other state? ").title()
    if answer_state in guessed_states:
        pass

    elif answer_state in states_list:
        guessed_states.append(answer_state)
        answer_row = all_states[all_states['state'] == answer_state]
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(int(answer_row['x']), int(answer_row['y']))
        t.write(answer_state)
    
    elif answer_state == 'Exit':
        break

states_to_learn = []
for state in states_list:
    if state not in guessed_states:
        states_to_learn.append(state)
print(states_to_learn)
states_to_learn_df = pandas.DataFrame(states_to_learn)
states_to_learn_df.to_csv('states_to_learn.csv')







