import turtle
screen=turtle.Screen()
# screen.textinput("Guess the provience","What would be the next one: ")
image="pakistan_map.gif"
screen.setup(width=800,height=800)
screen.addshape(image)
turtle.shape(image)

def get_mouse_click_coor(x,y):
    print(x,y)

# print(turtle.onscreenclick)
# while True:
turtle.onscreenclick(get_mouse_click_coor,btn=1)



turtle.mainloop()
