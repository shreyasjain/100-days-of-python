# import tkinter
#
# t = tkinter.Tk()
#
# t.title("Hello World")
# t.minsize(800, 600)


from tkinter import *
root = Tk()

root.geometry("600x600")
root.title("Hello World")
# root.minsize(600, 600)

label = Label(text="Hello World", justify="center", font=("Arial", 25))
label.grid(column=0, row=0)



input = Entry(width=20)
input.grid(column=3, row=2)

def change_label():
    text = input.get()
    label["text"] = f"{text}"


button = Button(text="Click me", justify="center", command=change_label)
button.grid(column=1, row=1)

new_button = Button(text="New Button")
new_button.grid(column=2, row=0)

# title.place(relx=0.5, rely=0.5, anchor="center")

root.mainloop()