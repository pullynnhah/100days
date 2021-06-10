# ------------------------------------------------------ IMPORTS ----------------------------------------------------- #
from tkinter import *

# ---------------------------------------------------- CONSTANTS ----------------------------------------------------- #
PINK = "#ff737c"
RED = "#ff2a00"
GREEN = "#1c8c0f"
DARK_GREEN = "#002500"
YELLOW = "#ffd966"
FONT = "Make Wonderful Moments Script"
FONT_CLOCK = "Bonbon"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECK_MARK = "✔️"

# ------------------------------------------------ GLOBAL VARIABLES -------------------------------------------------- #
reps = 0
timer = None
allow_button = True


# --------------------------------------------------- TIMER RESET ---------------------------------------------------- #
def reset_timer():
    global reps, allow_button
    reps = 0
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text='00:00')
    title_label.config(text='Timer')
    check_label.config(text='')
    allow_button = True


# ------------------------------------------------- TIMER MECHANISM -------------------------------------------------- #
def start_timer():
    global reps, allow_button

    if allow_button:
        reps += 1

        if reps % 8 == 0:
            title_label.config(text='Break', fg=RED)
            secs = LONG_BREAK_MIN * 60
        elif reps % 2 == 0:
            title_label.config(text='Break', fg=PINK)
            secs = SHORT_BREAK_MIN * 60
        else:
            title_label.config(text='Work', fg=GREEN)
            secs = WORK_MIN * 60
        allow_button = False

        count_down(secs)


# ----------------------------------------------- COUNTDOWN MECHANISM ------------------------------------------------ #
def format_time(time):
    minutes = time // 60
    seconds = time % 60
    return f'{minutes:02d}:{seconds:02d}'


def format_checkmarks(num_checkmarks):
    global timer
    num_rows = num_checkmarks // 5
    remaining = num_checkmarks % 5

    rows = [CHECK_MARK * 5] * num_rows
    rows.append(CHECK_MARK * remaining)
    return '\n'.join(rows)


def count_down(number):
    global timer, allow_button
    canvas.itemconfig(timer_text, text=format_time(number))
    if number >= 0:
        timer = window.after(1000, count_down, number - 1)
    else:
        check_label.config(text=format_checkmarks((reps + 1) // 2))
        allow_button = True
        start_timer()


# ----------------------------------------------------- UI SETUP ----------------------------------------------------- #
window = Tk()
window.title("🍅 Pomodoro 🍅")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 135, text='00:00', fill=DARK_GREEN, font=(FONT_CLOCK, 50))
canvas.grid(column=1, row=1)

title_label = Label(text="Timer", font=(FONT, 60), fg=GREEN, bg=YELLOW)
title_label.grid(column=1, row=0)

start_button = Button(text='Start', font=(FONT, 24), fg=DARK_GREEN,
                      bg=YELLOW, highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text='Reset', font=(FONT, 24), fg=DARK_GREEN,
                      bg=YELLOW, highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

check_label = Label(font=(FONT, 24), fg=GREEN, bg=YELLOW)
check_label.grid(column=1, row=3)

window.mainloop()
