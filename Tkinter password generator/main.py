import json
from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for char in range(randint(8, 10))]
    # for char in range(nr_letters):
    #   password_list.append(random.choice(letters)

    password_symbol = [choice(symbols) for char in range(randint(2, 4))]
    password_numbers = [choice(numbers) for char in range(randint(2, 4))]
    password_list = password_numbers + password_list + password_symbol
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    w_d = website_entry.get()
    p_d = password_entry.get()
    e_d = email_entry.get()
    new_data = {
        w_d: {
            "Email": e_d,
            "Password": p_d
        }
    }

    if len(w_d) == 0 or len(e_d) == 0 or len(p_d) == 0:
        messagebox.showinfo(title="Oops", message="Plz don't leave any fields empty")

    else:
        # load (read) , dump(write a file), update( append)
        try:
            # read file and save it in u
            with open("./data.json", "r") as data1:
                u = json.load(data1)

        except FileNotFoundError:
            # create a new file if not avaliable
            with open("./data.json", "w") as data:
                json.dump(new_data, data)

        else:
            # update the file with new data that contain old data + new data
            u.update(new_data)
            with open("./data.json", "w") as data:
                json.dump(u, data, indent=4)

        finally:
            # run at any cost so it delete entries data
            website_entry.delete(0, END)
            password_entry.delete(0, END)
            # #     data.write(f"{w_d} | {p_d} | {e_d}\n")
            # messagebox.showinfo(title="Data.txt", message="Your data is saved")


# ---------------------------- SEARCH ------------------------------- #
def search():
    website_name = website_entry.get()
    try:
        with open("data.json") as data_file:
            already_data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found")
    else:
        if website_name in already_data:
            web = already_data[website_name]["email"]
            password = already_data[website_name]["password"]
            messagebox.showinfo(title=website_name, message=f"Email:{web}\nPassword:{password}")

        else:
            messagebox.showinfo(title="Not found", message="p;ease put the data first")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("password generator")
window.config(padx=0, pady=0)
canvas = Canvas(window, width=200, height=200)
imgs = PhotoImage(file="logo.png")
# tuple index ou of range : means that before any argument some parameters are missing
canvas.create_image(100, 100, anchor="center", image=imgs)
canvas.grid(row=0, column=1)

# Labels
website = Label(window, text="Website:", )
email = Label(window, text="Email/Username:")
password_label = Label(window, text="Password:", )

website.grid(row=1, column=0)
email.grid(row=2, column=0)
password_label.grid(row=3, column=0)

# Buttons
generate = Button(window, text="Generate Password", border=2, width=19, command=generator, relief="groove",
                  overrelief="solid")
add = Button(window, text="Add", compound="right", border=2, width=20, command=save, relief="groove",
             overrelief="solid")
searcher = Button(window, text="Search", width=19, border=2, command=search, relief="groove", overrelief="solid")

generate.grid(row=3, column=2)
add.grid(row=4, column=1, columnspan=2)
searcher.grid(row=1, column=2)

# Entries:
website_entry = Entry(window, width=35)
email_entry = Entry(window, width=35)
email_entry.insert(0, "usman.ak@gamil.com")
password_entry = Entry(window, width=35)

website_entry.grid(row=1, column=1, )
email_entry.grid(row=2, column=1, )
password_entry.grid(row=3, column=1)

window.mainloop()
