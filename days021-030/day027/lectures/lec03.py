import tkinter

window = tkinter.Tk()

window.title("🖱️ My first GUI program 🖱️")
window.minsize(width=500, height=300)

label = tkinter.Label(text='I am a Label', font=("Atari Classic Extrasmooth", 12))
label.pack(side='bottom')

window.mainloop()
