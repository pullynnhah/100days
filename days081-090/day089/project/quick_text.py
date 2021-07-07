# ------------------------------------------------------ IMPORTS ----------------------------------------------------- #
from tkinter import *
from tkinter import messagebox

# ------------------------------------------ CONSTANTS / GLOBAL VARIABLES  ------------------------------------------- #
TITLE_FONT = ('Aesthetic Violet', 40)
LABEL_FONT = ('Manjari', 16)
TEXT_FONT = ('Manjari', 12)
WAIT_TIME = 5000
timer = None


# ---------------------------------------------------- FUNCTIONS ----------------------------------------------------- #
def clean_text():
    text.delete('1.0', END)
    text.focus()
    start_timer()


def start_timer(*_ignore):
    global timer
    if timer is None:
        timer = window.after(WAIT_TIME, clean_text)
    window.after_cancel(timer)
    timer = window.after(WAIT_TIME, clean_text)


def start():
    text.focus()
    start_timer()


def save():
    global timer
    if timer is not None:
        window.after_cancel(timer)
        timer = None
    filename = file.get()
    full_text = text.get('1.0', END)
    with open(f'texts/{filename}.txt', 'w') as f:
        print(full_text, file=f)
    file.delete(0, END)
    text.delete('1.0', END)
    file.focus()
    messagebox.showinfo(title=filename, message='Text saved with success!')


# ----------------------------------------------------- UI SETUP ----------------------------------------------------- #

window = Tk()
window.title('⏲️ Quick Text ⏲️')
window.config(padx=50, pady=50)

title = Label(text='Quick Text', font=TITLE_FONT)
title.grid(column=0, row=0, columnspan=2, pady=(0, 20))

file_label = Label(text='Filename', font=LABEL_FONT)
file_label.grid(column=0, row=1, sticky=W)

file = Entry(width=50, font=TEXT_FONT)
file.grid(column=0, row=2, columnspan=2, pady=(0, 20))
file.focus()

text_label = Label(text='Your text', font=LABEL_FONT)
text_label.grid(column=0, row=3, sticky=W)

text = Text(height=10, width=50, font=TEXT_FONT)
text.grid(column=0, row=4, columnspan=2, pady=(0, 20))

start = Button(text='START', command=start, font=LABEL_FONT)
start.grid(column=0, row=5)

save = Button(text='SAVE', command=save, font=LABEL_FONT)
save.grid(column=1, row=5)

window.bind_all('<Key>', start_timer)
window.mainloop()
