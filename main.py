from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- SEARCH ENTRIES ------------------------------- #
def find_password():
    website_name = website_input.get()

    try:
        # Read the JSON file as shown below
        with open("data.json", mode='r') as file:
            # data_check is turned into a dictionary by Python
            data_check = json.load(file)
            if website_name in data_check:
                messagebox.showinfo(title=website_name, message=f"Email: {data_check[website_name]["username"]}\nPassword: {data_check[website_name]["password"]}")
            else:
                messagebox.showerror(title="Warning", message=f"No details for '{website_name}' exists")
    except FileNotFoundError:
        messagebox.showerror(title="Warning", message="No data file exists")


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
    # We will create a new empty nested dictionary called "new_data"
    new_data = {
        website_name:{
            "username": email_username,
            "password": password,
        }
    }


    if len(website_name) == 0 or len(email_username) == 0 or len(password) == 0:
        error_msg = messagebox.showerror(title='Error!', message="Please fill in all the details! No empty fields")
    else:
        # the below message box will be saved as a boolean 'True' or 'False'
        is_ok = messagebox.askokcancel(title=website_name, message="Do you wish to save these credentials?")
        if is_ok is True:
            # with open("data.txt", mode='a') as file:
            #     file.write(f"{website_name} | {email_username} | {password} \n")
            ## Instead of writing to a text file as above, we will write to a JSON file as below
            try:
                with open("data.json", mode='r') as file:
                #The most important inputs are the objects you want to dump and the file you want to dump it to
                # we will dump the "new_data" dictionary into the JSON file, fist input is the empty dict we want to dump to and the second input is the data file we want to put it inot called "file"
                # The "indent" is to make the JSON file more readable
                # json.dump(new_data, file, indent=4)
                # To read from a JSON file we use 'json.load(pass in the file name or path = 'file')
                # We also need to change the 'with open("data.json", mode='r') as file:'
                # This new loaded data will be stored in a variable called 'data' (which is a dictionary)
                    data = json.load(file)  # Save this file to variable 'data' which converts it into a dictionary
                    data.update(new_data)  # Updating the dictionary variable with new inputed data
            except FileNotFoundError:
                # An error usually occurs if the json file is empty, so we need to first write to it then this 'except' error won't occur and it'll execute the 'try' cmd
                with open("data.json", mode='w') as file:
                    json.dump(new_data, file, indent=4)

            else:
                with open("data.json", mode='w') as file:
                    json.dump(data, file, indent=4)  # saving updated data

            finally:
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

website_input = Entry(width=32)
website_input.focus()
website_input.grid(column=1, row=1)

search_button = Button(text="Search Database", width=17, font=("Arial", 8), command=find_password)
search_button.grid(column=2, row=1)

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