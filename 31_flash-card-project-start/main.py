import random
import tkinter
import pandas

BACKGROUND_COLOR = "#B1DDC6"

try:
    data = pandas.read_csv('data/words_to_learn.csv')
except FileNotFoundError:
    data = pandas.read_csv('data/french_words.csv')
finally:
    data_dict = data.to_dict(orient='records')
    current_word = ""


# data = pandas.read_csv('data/french_words.csv')
# data_dict = data.to_dict(orient='records')
# current_word = ""

def flip_card(word):
    f_canvas.itemconfig(language, text='English')
    f_canvas.itemconfig(the_word, text=word['English'])
    f_canvas.itemconfig(bg_image, image=back_image)


def change_word():
    global current_word
    current_word = random.choice(data_dict)
    f_canvas.itemconfig(bg_image, image=front_image)
    f_canvas.itemconfig(language, text='French')
    f_canvas.itemconfig(the_word, text=current_word['French'])
    window.after(3000, flip_card, current_word)


def wrong():
    change_word()


def correct():
    data_dict.remove(current_word)
    new = pandas.DataFrame(data_dict)
    new.to_csv('data/words_to_learn.csv', index=False)
    change_word()


window = tkinter.Tk()
window.title(string="Flashy Cards")
window.geometry("900x700")
# window.resizable(False, False)
window.config(background=BACKGROUND_COLOR, padx=50, pady=50)

f_canvas = tkinter.Canvas()
f_canvas.config(height=526, width=800, background=BACKGROUND_COLOR, highlightthickness=0)
front_image = tkinter.PhotoImage(file="images/card_front.png")
back_image = tkinter.PhotoImage(file="images/card_back.png")
bg_image = f_canvas.create_image(400, 263, image=front_image)
language = f_canvas.create_text(400, 200, text='French', font=('Ariel', 40, 'italic'))
the_word = f_canvas.create_text(400, 300, text='trauve', font=('Ariel', 60, 'bold'))
f_canvas.grid(row=0, column=0, columnspan=2)

right_image = tkinter.PhotoImage(file='images/right.png')
wrong_image = tkinter.PhotoImage(file='images/wrong.png')
right_button = tkinter.Button(image=right_image, highlightthickness=0, border=0, command=correct)
wrong_button = tkinter.Button(image=wrong_image, highlightthickness=0, border=0, command=wrong)
right_button.grid(row=1, column=1)
wrong_button.grid(row=1, column=0)

change_word()

window.mainloop()
