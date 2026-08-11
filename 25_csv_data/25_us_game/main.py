from turtle import Screen, Turtle
import pandas
from state import State

screen = Screen()
turtle = Turtle()

screen.title("US State Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
data_to_list = data.state.to_list()

guessed_answers = []

while len(guessed_answers) <= 50:
    state_input = screen.textinput("Guess the state.", "What's another states name ? ").title()
    state_data = data[data.state.str.fullmatch(state_input)]
    print(state_data)
    if state_data.size==0:
        print("The state doesn't exist")
        continue
    else:
        xcord = state_data.x.item()
        ycord = state_data.y.item()
        text = state_data.state.item()
        state_obj = State(text, xcord, ycord)
        guessed_answers.append(text)

        missing_data = filter(lambda x: x not in guessed_answers, data_to_list)
        pandas.DataFrame(missing_data).to_csv("missing_states.csv")

# screen.exitonclick()