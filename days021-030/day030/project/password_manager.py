# ------------------------------------------------------ IMPORTS ----------------------------------------------------- #
import json

from tkinter import *
from tkinter import messagebox
from random import choice, shuffle, randint

from pyperclip import copy

# ---------------------------------------------------- CONSTANTS ----------------------------------------------------- #
FONT = ("Atari Classic Extrasmooth", 8)
LETTERS = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
           'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')

NUMBERS = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
SYMBOLS = ('!', '#', '$', '%', '&', '(', ')', '*', '+')


# ------------------------------------------------- PASSWORD GENERATOR ----------------------------------------------- #
def gen_password():
    password_entry.delete(0, END)
    letters = [choice(LETTERS) for _ in range(randint(8, 10))]
    numbers = [choice(NUMBERS) for _ in range(randint(2, 4))]
    symbols = [choice(SYMBOLS) for _ in range(randint(2, 4))]

    password = letters + numbers + symbols
    shuffle(password)
    final_password = ''.join(password)
    copy(final_password)
    password_entry.insert(0, final_password)


# --------------------------------------------------- SAVE PASSWORD -------------------------------------------------- #
def save_file(a_data):
    try:
        with open('data.json') as file:
            data = json.load(file)
    except FileNotFoundError:
        with open('data.json', 'w') as file:
            json.dump(a_data, file, indent=4)
    else:
        with open('data.json', 'w') as file:
            data.update(a_data)
            json.dump(data, file, indent=4)


def save():
    website = website_entry.get()
    user = user_entry.get()
    password = password_entry.get()
    if len(website) != 0 and len(user) and len(password) != 0:
        new_data = {
            website: {
                'email/username': user,
                'password': password
            }
        }
        message = f'This are the details entered:\nEmail/Username: {user}\nPassword: {password}\nIs it ok to save? '
        is_ok = messagebox.askokcancel(title=website, message=message)
        if is_ok:
            save_file(new_data)
            website_entry.delete(0, END)
            password_entry.delete(0, END)
    else:
        messagebox.showerror(title="🚨 Empty field 🚨", message="You left some field(s) empty. Please try again!")


# --------------------------------------------------- SEARCH PASSWORD -------------------------------------------------- #
def find_password():
    website = website_entry.get()
    if len(website) == 0:
        message = "Please make sure the field 'Website' is not empty."
        messagebox.showerror(title="🚨 Empty field 🚨", message=message)
    else:
        try:
            with open('data.json') as file:
                data = json.load(file)
        except FileNotFoundError:
            message = "No Data File Found"
            messagebox.showerror(title="📂 File Not Found 📂", message=message)
        else:
            info = data.get(website)
            if info is None:
                message = "No details for the website exists"
                messagebox.showerror(title='💻 Website Not Found 💻', message=message)
            else:
                web = f'Website Info'
                user = f'Email/Username: {info["email/username"]}'
                password = f'Password: {info["password"]}'
                messagebox.showinfo(title=web, message=f'{user}\n{password}')



# ------------------------------------------------------ UI SETUP ---------------------------------------------------- #
window = Tk()
window.title("🔐 Password Manager 🔐")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

website_title = Label(text='Website:', font=FONT)
website_title.grid(column=0, row=1)

user_title = Label(text='Email/Username:', font=FONT)
user_title.grid(column=0, row=2)

password_title = Label(text='Password:', font=FONT)
password_title.grid(column=0, row=3)

website_entry = Entry(width=20, font=FONT)
website_entry.grid(column=1, row=1)
website_entry.focus()

user_entry = Entry(width=40, font=FONT)
user_entry.grid(column=1, row=2, columnspan=2)
user_entry.insert(END, "paula@email.com")

password_entry = Entry(width=20, font=FONT)
password_entry.grid(column=1, row=3)

gen_button = Button(text="Generate Password", font=FONT, command=gen_password)
gen_button.grid(column=2, row=3)

save_button = Button(width=38, text="Add", font=FONT, command=save)
save_button.grid(column=1, row=4, columnspan=2)

search_button = Button(width=17, text='Search', font=FONT, command=find_password)
search_button.grid(column=2, row=1)
window.mainloop()
