from pydoc import text
from tkinter import *

import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
window_timer = None


# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    global window_timer
    global REPS
    window.after_cancel(window_timer)
    canvas.itemconfig(timer, text="00:00")
    label.config(text="Timer", fg=YELLOW)
    check_marks.config(text='')
    REPS = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global REPS
    REPS += 1

    if REPS % 8 == 0:
        label.config(text="Break", fg=RED)
        count_down(int(LONG_BREAK_MIN * 60))
    elif REPS % 2 == 0:
        label.config(text="Break", fg=PINK)
        count_down(int(SHORT_BREAK_MIN * 60))
    else:
        label.config(text="Work", fg=GREEN)
        count_down(int(WORK_MIN * 60))


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    minutes = int(count / 60)
    seconds = count % 60

    def refactored(digit):
        if digit < 10:
            return f"0{digit}"
        return digit

    canvas.itemconfig(timer, text=f"{refactored(minutes)}:{refactored(seconds)}")
    if count > 0:
        global window_timer
        window_timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        curr_text = ''
        for _ in range(math.floor(REPS / 2)):
            curr_text += '✔'
        check_marks.config(text=curr_text)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Pomodoro')
window.minsize(width=330, height=330)
window.config(padx=50, pady=50, background=YELLOW)

label = Label(text="Timer", font=(FONT_NAME, 30, 'bold'), foreground=GREEN, background=YELLOW)
label.grid(row=0, column=1)

canvas = Canvas(width=230, height=230, background=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(115, 115, image=tomato_img)
timer = canvas.create_text(115, 135, text="00:00", font=(FONT_NAME, 25, 'bold'), fill='white')
canvas.grid(row=1, column=1)

start_button = Button(text="Start", command=start_timer)
reset_button = Button(text="Reset", command=reset_timer)
start_button.grid(row=2, column=0)
reset_button.grid(row=2, column=2)

check_marks = Label(foreground=GREEN)
check_marks.grid(row=3, column=1)

window.mainloop()
