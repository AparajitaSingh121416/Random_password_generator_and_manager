from tkinter import *
from tkinter import messagebox

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nr_letters = random.randint(8, 10)
nr_symbols = random.randint(2, 4)
nr_numbers = random.randint(2, 4)

password_list = []

for char in range(nr_letters):
  password_list.append(random.choice(letters))

for char in range(nr_symbols):
  password_list += random.choice(symbols)

for char in range(nr_numbers):
  password_list += random.choice(numbers)

random.shuffle(password_list)

random_password = ""
for char in password_list:
  random_password += char

print(f"Your password is: {random_password}")

def password_adder():
    password_text.insert(END,random_password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_text.get("1.0", END)
    email = email_text.get("1.0", END)
    password = password_text.get("1.0", END)

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} "
                                                              f"\nPassword: {password} \nIs it ok to save?")
        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                website_text.delete(0, END)
                password_text.delete(0, END)
                email_text.delete(0,END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(pady= 50, padx= 20)

canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=lock_img)
canvas.grid(column=1, row=0)

website_label = Label(text= "Website:", font=("Arial",11,"normal"))
website_label.config(pady= 10)
website_label.grid(column=0, row=1)
email_label = Label(text="Email/Username:", font=("Arial",11,"normal"))
email_label.config(pady=10)
email_label.grid(column=0, row= 2)
password_label = Label(text="Password:", font=("Arial",11,"normal"))
password_label.grid(column =0, row=3)

website_text = Text(height=1, width=35)
website_text.focus()
website_text.grid(column=1,row=1, columnspan = 2)

email_text = Text(height=1, width=35)
email_text.focus()
email_text.grid(column =1, row= 2, columnspan=2)

password_text = Text(height=1, width=21)
password_text.focus()

password_text.grid(column =1, row=3)

generate_password_button = Button(text="Generate Password",command=password_adder)
generate_password_button.grid(column= 2, row= 3)

add_button = Button(text= "Add", height=1, width= 40, command=save)
add_button.grid(column=1, row=4, columnspan = 2)















window.mainloop()