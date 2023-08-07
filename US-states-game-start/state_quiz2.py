import turtle
import pandas

screen = turtle.Screen()
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

state_data = pandas.read_csv("50_states.csv")
state_list = state_data.state.to_list()
print(state_list)
# print(state_data.state)
# if the guess is amoung the states
guess_states = []
non_guess_state = []
while len(guess_states) != 50:
    guesses_state = screen.textinput(title=f"{len(guess_states)}/50 Correct state :America state", prompt=" guess the right state")
    guesses_state = guesses_state.title()
    if guesses_state == "Exit":
        for x in state_list:
            if x not in guess_states:
                non_guess_state.append(x)
        print(non_guess_state)
        break

    if guesses_state in state_list:
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        states = state_data[state_data.state == guesses_state]
        t.goto(int(states.x), int(states.y))
        t.write(guesses_state)
        if guesses_state in guess_states:
            pass
        else:
            guess_states.append(guesses_state)

        # create a csv file of the remaining


remaining_state=pandas.DataFrame(non_guess_state)
remaining_state.to_csv(f"my remaining states")
turtle.mainloop()