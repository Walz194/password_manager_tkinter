import tkinter
import random
from tkinter import messagebox
import pyperclip

window = tkinter.Tk()
window.config(padx=50,pady=50)

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = list('acdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    numbers = list('0123456789')
    symbols = list('!@#$%()*+')

    nr_letters = random.randint(8,10)
    nr_symbols = random.randint(2,4)
    nr_numbers = random.randint(2,4)

    password_list = []

    password_list.extend([random.choice(letters) for _ in range(nr_letters)])
    password_list.extend([random.choice(symbols) for _ in range(nr_symbols)])
    password_list.extend([random.choice(numbers) for _ in range(nr_numbers)])

    random.shuffle(password_list)
    return ''.join(password_list)

def set_generated_password():
    password_input.delete(0,tkinter.END)

    password_input.insert(0,string=generate_password())

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()

    if len(website) == 0:
        messagebox.showinfo(title='Oops',message='Please make sure your website isn\'t empty')
    elif len(email) == 0:
        messagebox.showinfo(title='Oops',message='Please make sure your email isn\'t empty ')
    elif len(password) == 0:
        messagebox.showinfo(title='Oops',message='Please make sure your password isn\'t empty ')
    else:
        is_ok=messagebox.askokcancel(title=website,message=f'These are the details you entered: \n\nEmail: {email}\nPassword: {password}\n\nIs it ok to save?')
        if is_ok:
            with open('password.txt','a') as f:
                f.write(f'{website} | {email} | {password}\n')
            website_input.delete(0,tkinter.END)
            password_input.delete(0,tkinter.END)


# ---------------------------- UI SETUP ------------------------------- #
lock_logo = tkinter.PhotoImage(file='./logo.png')
canvas = tkinter.Canvas(width=200,height=200)
canvas.create_image(100,100,image=lock_logo)
canvas.grid(row=0,column=1)

website_label = tkinter.Label(text='Website:')
website_label.grid(row=1,column=0)

email_label = tkinter.Label(text='Email/Username:',width=15)
email_label.grid(row=2,column=0)

password_label = tkinter.Label(text='Password:')
password_label.grid(row=3,column=0)

website_input = tkinter.Entry(width=52)
website_input.focus()
website_input.grid(row=1,column=1,columnspan=2,sticky='w')

email_input = tkinter.Entry(width=52)
email_input.insert(tkinter.END,string='olawale.akinodanye@gmail.com')
email_input.grid(row=2,column=1,columnspan=2,sticky='w')

password_input = tkinter.Entry(width=30)
password_input.grid(row=3,column=1,sticky='w')


generate_button = tkinter.Button(text='Generate Password',command=set_generated_password)
generate_button.grid(row=3,column=2,sticky='w')

add_button = tkinter.Button(text='Add',width=44,command=save)
add_button.grid(row=4,column=1,columnspan=2,sticky='w')



window.mainloop()