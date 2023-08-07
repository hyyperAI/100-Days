from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
X = 100
indexes = None
# <---------------------------DATA------------------------->
data = pandas.read_csv("./data/french_words.csv")


def current_card():
    global X, indexes,flip
    window.after_cancel(flip)
    indexes = (random.randint(0, X))
    X = X - 1
    french_word = data["French"][indexes]
    canvas.itemconfig(language, text="French")
    canvas.itemconfig(words, text=french_word)
    canvas.itemconfig(card_bg_img, image=card_front_img)
    flip=window.after(3000, next_card)


def next_card():
    global indexes

    english_word = data["English"][indexes]
    canvas.itemconfig(language, text="English")
    canvas.itemconfig(words, text=english_word)
    canvas.itemconfig(card_bg_img, image=card_back_img)

def create():
    global indexes
    # Delete
    print()
    print(len(data.drop(index=indexes)))
    current_card()



# <-----------------------------UI AND UX--------------------------------->
window = Tk()
window.title("Flashy")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)
flip=window.after(3000, current_card)

# Canvas text and photo
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0, borderwidth=0)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="./images/card_back.png")
card_bg_img = canvas.create_image(400, 263, image=card_front_img)
canvas.grid(row=0, column=0, columnspan=3)
language = canvas.create_text(400, 153, text="Title", font=("Ariel", 40, "italic"))
words = canvas.create_text(400, 350, text="Word", font=("Ariel", 40, "italic"))

# Buttons

wrong = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong, borderwidth=0, highlightthickness=0, command=current_card)
right = PhotoImage(file="images/right.png")
right_button = Button(image=right, borderwidth=0, highlightthickness=0,command=create)

wrong_button.grid(row=1, column=0)
right_button.grid(row=1, column=2)

window.mainloop()
