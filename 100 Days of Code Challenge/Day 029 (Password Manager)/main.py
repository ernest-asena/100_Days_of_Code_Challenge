import tkinter as tk
# from tkinter import END
from tkinter import messagebox
import random
import pyperclip
from Clearscreen import clear


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pass():
    """Generates a random password using letters, numbers and symbols."""
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_numbers + password_symbols + password_letters

    # for char in range(nr_letters):
    #     password_list.append(random.choice(letters))

    # for char in range(nr_symbols):
    #     password_list += random.choice(symbols)
    #
    # for char in range(nr_numbers):
    #     password_list += random.choice(numbers)

    random.shuffle(password_list)

    # password = ""
    # for char in password_list:
    #     password += char
    password = "".join(password_list)
    # print(f"Your password is: {password}")
    pass_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_entry.get()
    email = username_entry.get()
    password = pass_entry.get()

    # if len(website) or len(password):
    #     messagebox.showinfo(title="Missing Values.", message="Check all fields are entered and try again.")
    # else:

    is_ok = messagebox.askokcancel(title=website,
                                   message=F"These are details entered: \nEmail: {email}\nPassword: {password}\nIs this okay to save?")

    if is_ok:
        with open('data.txt', 'a') as pass_file:
            pass_file.write(F"{website} | {email} | {password}\n")
            website_entry.delete(0, tk.END)
            pass_entry.delete(0, tk.END)


# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()

window.title('Day 029: A Password Manager.')

window.config(padx=50, pady=50)
canvas = tk.Canvas(width=200, height=200, highlightthickness=0)
lock_img = tk.PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

website_label = tk.Label(text='Website:')
website_label.grid(column=0, row=1)

username_label = tk.Label(text='Username/Email:')
username_label.grid(column=0, row=2)

pass_label = tk.Label(text='Password:')
pass_label.grid(column=0, row=3)

website_entry = tk.Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

username_entry = tk.Entry(width=35)
username_entry.grid(column=1, row=2, columnspan=2)
username_entry.insert(0, 'ernest999@gmail.com')

pass_entry = tk.Entry(width=21)
pass_entry.grid(column=1, row=3)

generate_password = tk.Button(text='Generate Password', command=generate_pass)
generate_password.grid(column=2, row=3)

add_password = tk.Button(text='Add', width=36, command=save)
add_password.grid(column=1, row=4, columnspan=2)

window.mainloop()
