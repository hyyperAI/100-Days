import math
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 0.1
SHORT_BREAK_MIN = 0.2
LONG_BREAK_MIN = 10
reps = 0
main = None


# ---------------------------- TIMER RESET ------------------------------- #

# pause
def pause():
    global main, reps
    reps -= 1
    window.after_cancel(main)
    label1.config(text="Paused")
    # canvas.itemconfig(timer_text, text="00:00")


# reset the whole process means: start timer from begining
def reset():
    global main
    window.after_cancel(main)
    global reps
    reps = 0
    canvas.itemconfig(timer_text, text="00:00")
    label2.config(text="✓")
    label1.config(text="Timer")


# ---------------------------- TIMER MECHANISM ------------------------------- #
# for start
def start_countdown():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        label1.config(text="Break for 20 minutes", fg="RED")

    elif reps % 2 == 0:
        count_down(short_break_sec)
        label1.config(text="Break for 5 minutes", fg="YELLOW")

    else:
        count_down(work_sec)
        label1.config(text="WORK TIME", fg="GREEN")


# convert sec * 60=n min

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

# getting time in minute and second , for minute count/60
# for sec time%60

def count_down(timer):
    count_min = math.floor(timer / 60)
    count_sec = timer % 60

    # for adding zero in single digit numbers
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")

    # recursive function
    if timer > 0:
        global main
        main = window.after(1000, count_down, timer - 1)
    else:
        start_countdown()
        print(reps)
        # reps and  working sessions : 4-2,6-3, 8-4
        mark = ""
        working_session = int(reps / 2)
        for item in range(working_session):
            mark += "✓"
        label2.config(text=mark, fg="GREEN")


# ---------------------------- UI SETUP ------------------------------- #
# window features
window = Tk()
window.title("Time Application")
window.config(padx=100, pady=50, bg=PINK)

# 2 text

label1 = Label(text="TIMER", font=(FONT_NAME, 25), bg=PINK, fg=GREEN)
label1.grid(column=1, row=0)

label2 = Label(text="✓", font=(FONT_NAME, 10, "bold"), bg=PINK, fg=GREEN)
label2.grid(column=1, row=3)

# 2 button

button1 = Button(width=5, text="START", bg=PINK, command=start_countdown)
button2 = Button(width=5, text="RESET", bg=PINK, command=reset)
button3 = Button(width=5, text="PAUSE", bg=PINK, command=pause)
button2.grid(row=3, column=0)
button1.grid(row=3, column=2)
button3.grid(row=4, column=0)

# image processing

canvas = Canvas(width=250, height=250, bg=PINK, highlightthickness=0)
photo = PhotoImage(file="tomato.png")
canvas.create_image(120, 120, image=photo)
timer_text = canvas.create_text(120, 120, text="00:00", fill=GREEN, font=(FONT_NAME, 35, "bold"))

# canvas.pack()
canvas.grid(row=1, column=1)

window.mainloop()
