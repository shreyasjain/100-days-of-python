import random
from tkinter import *
from tkinter import messagebox


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
    numbers = list("0123456789")
    symbols = list("!#$%&()*+")
    LEN = 4
    password = ''

    for _ in range(LEN):
        password+=random.choice(letters)

    for _ in range(LEN):
        password+=random.choice(symbols)

    for _ in range(LEN):
        password+=random.choice(numbers)

    password_input.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def add_details():
    w = website_input.get()
    u = username_input.get()
    p = password_input.get()

    if len(w)==0 or len(u)==0 or len(p)==0:
        return messagebox.showerror("Attention", "Please dont leave any field empty !")

    acknowledged =messagebox.askokcancel("Success",
                           f"Are you sure to save these details:\nWebsite: {w}\nUsername: {u}\nPassword: {p}.")

    if acknowledged:
        with open('data.txt', 'a') as file:
            file.write(f"Website: {w} | UserName: {u} | Password:{p}\n")

        website_input.delete(0, len(w))
        # username_input.delete(0, len(u))
        password_input.delete(0, len(p))


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.geometry("400x400")
window.config(pady=20, padx=20)
# Image
canvas = Canvas()
canvas.config(height=200, width=200)
main_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=main_img)
canvas.grid(row=0, column=0, columnspan=3)
# Form
website_label = Label(text="Website:")
website_label.grid(padx=5, pady=5, row=1, column=0)

website_input = Entry(justify='left', name="website-input", width=42)
website_input.grid(padx=5, pady=5, row=1, column=1, columnspan=2)

username_label = Label(text="Username:")
username_label.grid(padx=5, pady=5, row=2, column=0)

username_input = Entry(justify='left', name="username-input", width=42)
username_input.insert(index=0, string="shreyasjain@gmail.com")
username_input.grid(padx=5, pady=5, row=2, column=1, columnspan=2)

password_label = Label(text="Password:")
password_label.grid(padx=5, pady=5, row=3, column=0)

password_input = Entry(justify='left', name="password-input", width=21)
password_input.grid(padx=5, pady=5, row=3, column=1)

generate_button = Button(text='Generate', width=14, command=generate_password)
generate_button.grid(padx=5, pady=5, row=3, column=2)

add_button = Button(text='Add', width=35, command=add_details)
add_button.grid(padx=5, pady=5, row=4, column=1, columnspan=2)

window.mainloop()
