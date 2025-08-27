import json
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8,10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0,password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_name_entry.get()
    email = email_name_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops",message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json","r") as data_file:
                # Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
                website_name_entry.delete(0, END)
                password_entry.delete(0,END)
# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = website_name_entry.get()
    try:
        with open("data.json") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found")
    else:
        if website in data:
            messagebox.showinfo(title=website, message=f"Email: {data[website]["email"]}\nPassword: {data[website]["password"]}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists")
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100,100, image=logo_img)
canvas.grid(column=1, row=0)

website_name_label = Label()
website_name_label.config(text="Website: ")
website_name_label.grid(column=0, row=1)

website_name_entry = Entry(width=21)
website_name_entry.focus()
website_name_entry.grid(column=1, row=1)

email_name_label = Label()
email_name_label.config(text="Email/Username: ")
email_name_label.grid(column=0, row=2)

email_name_entry = Entry(width=39)
email_name_entry.insert(END,"poojitha@gmail.com")
email_name_entry.grid(column=1, columnspan=2, row=2)

password_label = Label()
password_label.config(text="Password: ")
password_label.grid(column=0, row=3)

password_entry = Entry(width=21)
password_entry.grid(column=1,row=3)

generate_btn = Button()
generate_btn.config(text="Generate Password", command=generate_password)
generate_btn.grid(column=2, row=3)

add_btn = Button()
add_btn.config(text="Add", width=34,command=save)
add_btn.grid(column=1,columnspan=2, row=4)

search_btn = Button()
search_btn.config(text="Search", command=find_password, width=14)
search_btn.grid(column=2, row=1)

window.mainloop()
