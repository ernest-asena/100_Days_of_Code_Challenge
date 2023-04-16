import turtle
import pandas as pd

data = pd.read_csv('50_states.csv')

screen = turtle.Screen()
screen.title("Us States Game.")
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

total_states = 50
named_states = 0

all_states = data.state.to_list()
guessed_states = []
while len(guessed_states) < 50:

    answer_state = screen.textinput(title=F'{named_states}/{total_states} States Correct',
                                    prompt='What is the name of the State?').title()
    print(answer_state)

    if answer_state == 'Exit':
        break
    if answer_state in all_states:
        if answer_state in guessed_states:
            named_states -= 1
        guessed_states.append(answer_state)
        named_states += 1
        t = turtle.Turtle()
        t.penup()
        t.color('red')
        t.hideturtle()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)


def get_mouse_click_coor(x, y):
    print(x, y)


turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

# states_to_learn = []
# for state in all_states:
#     if state not in guessed_states:
#         states_to_learn.append(state)   # or do a list comprehension like below
states_to_learn = [state for state in all_states if state not in guessed_states]

states_to_learn_df = pd.DataFrame(states_to_learn)
states_to_learn_df.to_csv("Missed States.csv")

# if answer_state in all_states:
#     if answer_state in guessed_states:
#         named_states -= 1
#     guessed_states.append(answer_state)
#     named_states += 1
#     guessed_states.append(answer_state)
