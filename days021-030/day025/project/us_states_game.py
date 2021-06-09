import turtle

import pandas as pd

FONT = ("Atari Classic Extrasmooth", 6, "normal")

screen = turtle.Screen()
screen.title("🇺🇸 U.S. States Game 🇺🇸")
screen.setup(width=725, height=491)
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

writer = turtle.Turtle(visible=False)
writer.pu()
writer.speed(0)

choice = screen.textinput(title='Which game?',
                          prompt="Type 'full' to play with all the states else you will play\n"
                                 "with the states you didn't guess correctly last time:").lower()

if choice == 'full':
    states_df = pd.read_csv('50_states.csv', index_col='state')
else:
    states_df = pd.read_csv('states_to_learn.csv', index_col='state')
    known_df = pd.read_csv('states_known.csv', index_col='state')
    writer.color('red')
    for index, row in known_df.iterrows():
        writer.goto(row.x, row.y)
        writer.write(index, font=FONT)
    writer.color('black')

guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f'{len(guessed_states)}/{states_df.shape[0]} States Correct',
                                    prompt="Enter a state's name? ")
    if answer_state is None:
        break

    answer_state = answer_state.title()
    if answer_state in states_df.index:
        guessed_states.append(answer_state)
        state = states_df.loc[answer_state]
        writer.goto(state.x, state.y)
        writer.write(answer_state, font=FONT)


condition = states_df.index.isin(guessed_states)
to_learn_df = states_df[~condition]
states_known_df = states_df[condition]

to_learn_df.to_csv('states_to_learn.csv')
states_known_df.to_csv('states_known.csv', mode='a', header=False)

