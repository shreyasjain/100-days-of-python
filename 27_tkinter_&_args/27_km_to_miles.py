from tkinter import *

window = Tk()

window.minsize(300, 200)
window.title("KM to Miles")

label_1 = Label(text="Miles" ,font=("Arial", 20))
label_1.grid(row=0, column=2)
label_2 = Label(text="is equal to" ,font=("Arial", 20))
label_2.grid(row=1, column=0)
label_3 = Label(text="Km" ,font=("Arial", 20))
label_3.grid(row=1, column=2)
label_4 = Label(text="0" ,font=("Arial", 20))
label_4.grid(row=1, column=1)

entry = Entry(width=40)
entry.focus()
entry.grid(row=0, column=1)

def handle_convert():
    label_4['text']= int(float(entry.get())*1.60934)

button = Button(text="Convert", command=handle_convert)
button.grid(row=2, column=1)

window.mainloop()