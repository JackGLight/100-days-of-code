import tkinter as tk
from tkinter import messagebox
import random
import string
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = string.ascii_letters
    digits = string.digits
    symbols = "!#$%&()*+"

    # Ensure good mix
    password_chars = (
        random.choices(letters, k=8) +
        random.choices(digits, k=4) +
        random.choices(symbols, k=4)
    )

    random.shuffle(password_chars)
    password = "".join(password_chars)

    password_box.delete(0, tk.END)
    password_box.insert(0, password)

    # Optional but very nice UX
    window.clipboard_clear()
    window.clipboard_append(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_box.get().strip().lower()
    email = email_box.get()
    password = password_box.get()

    if not website or not password:
        messagebox.showwarning(
            title="Oops",
            message="Please don't leave the website or password empty."
        )
        return

    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {}

    data.update(new_data)

    with open("data.json", "w") as file:
        json.dump(data, file, indent=4)

    website_box.delete(0, tk.END)
    password_box.delete(0, tk.END)
# ---------------------------- Check Password ------------------------------- # 
               # data = json.load(file)
            # print(data)

def search_info():
    website = website_box.get().strip().lower()

    if not website:
        messagebox.showwarning(title="Oops", message="Please enter a website to search.")
        return

    try:
        with open("data.json", "r") as file:
            data = json.load(file)

        email = data[website]["email"]
        password = data[website]["password"]

        messagebox.showinfo(
            title=website,
            message=f"Website: {website}\nEmail: {email}\nPassword: {password}"
        )
        window.clipboard_clear()
        window.clipboard_append(password)

    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No data file found yet. Save a password first.")

    except KeyError:
        messagebox.showerror(title="Not found", message="There is no password saved for that website.")

    except json.JSONDecodeError:
        messagebox.showerror(title="Error", message="Your data file is not valid JSON. Try resetting data.json.")

# ---------------------------- UI SETUP ------------------------------- #

#Window
window = tk.Tk()
window.title('Password Manager')
window.config(padx=20, pady=20)

#Image
canvas = tk.Canvas(width=200, height=200)
myimg = tk.PhotoImage(file='logo.png')
canvas.create_image(0, 0, image=myimg, anchor='nw')
canvas.grid(row=0 ,column=1)

#Website label 
website_label = tk.Label(
    text="Website:", font=('Arial', 12))
# website_label.config(padx=10, pady=10)
website_label.grid(row=1, column=0)

#Email/Username label 
email_label = tk.Label(
    text="Email/Username:", font=('Arial', 12))
# email_label.config(padx=10, pady=10)
email_label.grid(row=2, column=0)

#Password label 
password_label = tk.Label(
    text="Password:", font=('Arial', 12))
# password_label.config(padx=10, pady=10)
password_label.grid(row=3, column=0)

#Website entry 
website_box = tk.Entry(width=35)
website_box.focus()
website_box.grid(row=1, column=1)

#Email / username entry 
email_box = tk.Entry(width=35)
email_box.insert(0, 'jack@email.com')
email_box.grid(row=2, column=1, columnspan=2)

#Password entry 
password_box = tk.Entry(width=21)
password_box.grid(row=3, column=1)

#generate password button
pass_button = tk.Button(text='Generate Password', width=12, command=generate_password)
pass_button.grid(row=3, column=2)

#add button
add_button = tk.Button(text='Add', width=36, command=save_password)
add_button.grid(row=4, column=1, columnspan=2)

#search button
search_button = tk.Button(text='Search', command=search_info)
search_button.grid(row=1, column=2)


window.mainloop()




# with open("data.txt", "a") as file:
    # file.write(f"{website},{username},{password}\n")