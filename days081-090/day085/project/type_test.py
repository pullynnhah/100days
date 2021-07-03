# ------------------------------------------------------- IMPORTS ---------------------------------------------------- #
import json
import random
import textwrap
import time

from tkinter import *
from tkinter import messagebox

# ------------------------------------------------------ CONSTANTS --------------------------------------------------- #
TITLE_FONT = ('Emilio 20', 36)
TEST_FONT = ('Manjari', 16, "bold")


# ------------------------------------------------------ FUNCTIONS --------------------------------------------------- #
def gen_quotes():
    with open('data.json') as file:
        return json.load(file)['quotes']


def gen_text():
    global extra_time, test, start_time
    extra_time = 0
    test_text.delete('1.0', END)
    test = ' '.join(random.sample(quotes, k=1))
    test_label['text'] = textwrap.fill(test, width=80)
    start_time = time.time()


def calc_speed():
    global start_time, extra_time
    end_time = time.time()
    test_result = test_text.get('1.0', END).strip()
    if test == test_result:
        minutes = (extra_time + end_time - start_time) / 60
        result = len(test) / (minutes * 5)
        messagebox.showinfo(title=f'{round(result)} WPM', message=f'You made {result:.2f} Words Per Minute.')
    else:
        extra_time = end_time - start_time
        messagebox.showerror(title="Text doesn't match test", message=f'You made mistakes fix them before calculating.')
        start_time = time.time()


# ----------------------------------------------------- VARIABLES ---------------------------------------------------- #
quotes = gen_quotes()
test = ''
extra_time = 0
test_size = 0
start_time = 0

# ------------------------------------------------------ UI SETUP ---------------------------------------------------- #
window = Tk()
window.title('💻 Type Test 💻')
window.config(padx=50, pady=50)

title_label = Label(window, text='Typing Test', font=TITLE_FONT)
title_label.grid(column=0, row=0, columnspan=2, pady=(0, 50))

test_label = Label(window, text='', font=TEST_FONT)
test_label.grid(column=0, row=1, columnspan=2)

test_text = Text(window, font=TEST_FONT, width=60, height=10)
test_text.grid(column=0, row=2, columnspan=2)

gen_button = Button(window, text='Generate Test', font=TEST_FONT, command=gen_text)
gen_button.grid(column=0, row=3, pady=(25, 0))
calc_button = Button(window, text='Calculate Speed', font=TEST_FONT, command=calc_speed)
calc_button.grid(column=1, row=3, pady=(25, 0))

window.mainloop()
