from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    password_input.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for i in range(nr_letters)]
    password_list += [random.choice(symbols) for i in range(nr_symbols)]
    password_list += [random.choice(numbers) for i in range(nr_numbers)]

    random.shuffle(password_list)

    password = "".join(password_list)

    # The above .join() code replaces the below for loop code. The .join() will turn the above list into a string
    # password = ""
    # for char in password_list:
    #     password += char

    password_input.insert(0, password)
    pyperclip.copy(password)
    print(f"Your password is: {password}")
# ---------------------------- SAVE PASSWORD ------------------------------- #


def write_to_file():
    website_name = website_input.get()
    email_username = email_input.get()
    password = password_input.get()
    # the below message box will be saved as a boolean 'True' or 'False'

    if len(website_name) == 0 or len(email_username) == 0 or len(password) == 0:
        error_msg = messagebox.showerror(title='Error!', message="Please fill in all the details! No empty fields")
    else:
        is_ok = messagebox.askokcancel(title=website_name, message="Do you wish to save these credentials?")
        if is_ok is True:
            with open("data.txt", mode='a') as file:
                file.write(f"{website_name} | {email_username} | {password} \n")

            website_input.delete(0, END)
            email_input.delete(0, END)
            email_input.insert(0, "abc@abc.com")
            password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(pady=50, padx=50)


canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:", font=("Arial", 10))
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:", font=("Arial", 10))
email_label.grid(column=0, row=2)

password_label = Label(text="Password:", font=("Arial", 10))
password_label.grid(column=0, row=3)

website_input = Entry(width=51)
website_input.focus()
website_input.grid(column=1, row=1, columnspan=2)


email_input = Entry(width=51)
email_input.insert(0,"abc@abc.com")
email_input.grid(column=1, row=2, columnspan=2)

password_input = Entry(width=32, show="*")  # The show='*' turns everything written into '*' on the outside
password_input.grid(column=1, row=3)

generate_pass_button = Button(text="Generate Password", width=17, font=("Arial", 8), command=generate_password)
generate_pass_button.grid(column=2, row=3)

add_button = Button(text="Add", width=38, font=("Arial", 10), command=write_to_file)
add_button.grid(column=1, row=4, columnspan=2)














window.mainloop()