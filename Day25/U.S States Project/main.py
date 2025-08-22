import turtle
from turtle import Turtle
import pandas
screen = turtle.Screen()
screen.title("U.S. States Game")

img = "blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)
tim = Turtle()
tim.hideturtle()
tim.penup()
guessed_states = []
data = pandas.read_csv("50_states.csv")
list_of_states = data.state.to_list()
while len(guessed_states) <= 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state name?").title()
    if answer_state == "Exit":
        missed_states = []
        for state in list_of_states:
            if state not in guessed_states:
                missed_states.append(state)
        states_not_guessed = pandas.DataFrame(missed_states)
        states_not_guessed.to_csv("states_to_learn.csv")
        break
    if answer_state in list_of_states:
        ans_row = data[data["state"] == answer_state]
        x_cor = ans_row.x.item()
        y_cor = ans_row.y.item()
        tim.goto(x_cor,y_cor)
        tim.write(answer_state)
        guessed_states.append(answer_state)


screen.exitonclick()