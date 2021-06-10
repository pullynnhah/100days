from tkinter import *


def say_something1(thing):
    print(thing)


def say_something2(a, b, c):
    print(a, b, c)


window = Tk()
window.title("Window After")
window.config(padx=100, pady=50)

window.after(1000, say_something1, "Hello")
window.after(2000, say_something2, 3, 5, 8)

window.mainloop()
