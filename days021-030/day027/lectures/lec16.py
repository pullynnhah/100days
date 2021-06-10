from tkinter import *


def button_clicked():
    label.config(text=user_input.get())


window = Tk()

window.title("🖱️ My first GUI program 🖱️")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)

label = Label(text='I am a Label', font=("Atari Classic Extrasmooth", 12))
label.config(padx=50, pady=50)
label.grid(column=0, row=0)


label['text'] = "I am  still a Label"
label.config(text="Nope, Still a Label")

button1 = Button(text="Click Me 1!", command=button_clicked)
button1.grid(column=1, row=1)


button2 = Button(text="Click Me 2!", command=button_clicked)
button2.grid(column=2, row=0)

user_input = Entry(width=10)
user_input.grid(column=3, row=2)

window.mainloop()
