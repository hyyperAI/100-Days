import turtle
import pandas

screen = turtle.Screen()
image = "blank_states_img.gif"
# add image in turtle directory of shapes because turtle only allow to shape which is added in his directory
screen.addshape(image)
# after adding shape we acess it by turtle.shape( name of the image, square or ant other that is present in directory)
turtle.shape(image)
state_data = pandas.read_csv("50_states.csv")
x = state_data.state.to_list()
print(x)
# screen.title("Name of the States")
# convert guess to title case
except_state=[]
guess_states = []
while len(guess_states) != 50:
    user_input = screen.textinput(title=f"{len(guess_states)}/50 Correct state", prompt="What's the other state")
    user_input=user_input.title()
    if user_input=="exit":
        except_state=[item for item in x if item not in guess_states]
        # for item in x:
        #     # x == states names '' list
        #     if item not in guess_states:
        #         # if item is not in guess_states then write it in except_state
        #         # guess_states is list of the name of the user guess
        #         except_state.append(item)
        break
    if user_input in x:
        guess_states.append(user_input)
        t = turtle.Turtle()
        status = state_data[state_data.state == user_input]
        # state_data.state access the state details of user's guess
        t.penup()
        t.hideturtle()
        t.goto(int(status.x), int(status.y))
        t.write(user_input)



print(except_state)
x2=pandas.DataFrame(except_state)
x2.to_csv()
turtle.mainloop()
# create a csv file that generate file name other than the given



