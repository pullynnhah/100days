from tkinter import *


def button_clicked():
    print("I got clicked!")


window = Tk()

window.title("🖱️ My first GUI program 🖱️")
window.minsize(width=500, height=300)

label = Label(text='I am a Label', font=("Atari Classic Extrasmooth", 12))
label.pack()

label['text'] = "I am  still a Label"
label.config(text="Nope, Still a Label")

button = Button(text="Click Me!", command=button_clicked)
button.pack()

window.mainloop()
