from tkinter import *
import mysql.connector
import re

mydb = mysql.connector.connect(host="localhost", user="root", password="pass123", database="bank_details")
my_cursor = mydb.cursor()

root = Tk()
root.geometry('500x550')
root.resizable(False, False)
root.title('Tex bank management')


# Commands
def display_error(error_message):
    label = Label(root, text=error_message)
    label.grid(row=11, column=0, columnspan=2)


def validate_input():
    name = input_name.get()
    if not name.strip():
        display_error('Input is empty.')
        return False
    elif re.search('[1-9]', name):
        display_error('Input contains numeric characters.')
        return False

    age = input_age.get()
    try:
        if int(age) <= 18:
            display_error('Age must be 18 or above')
            return False
    except ValueError:
        display_error('Not valid ! Input should be number')
        return False

    user_id = input_user_id.get()
    if user_id.islower():
        query = 'SELECT user_id FROM customers_details WHERE user_id = %s'
        values = [user_id]
        my_cursor.execute(query, values)
        if my_cursor.fetchone():
            display_error('User_id is already exist')
    else:
        display_error('User_id must be in lowercase letter')
        return False

    password = input_password.get()
    if len(password) < 8:
        display_error('Not valid ! Total characters should be grater than 8')
    elif not re.search("[A-Z]", password):
        display_error('Not valid ! It should contain at least one uppercase letter')
    elif not re.search("[a-z]", password):
        display_error('Not valid ! It should contain at least one lowercase letter')
    elif not re.search("[1-9]", password):
        display_error('Not valid ! It should contain at least one number')
    elif not re.search("[~!@#$%^&*]", password):
        display_error('Not valid ! It should contain at least one special character')
    elif re.search("[\s]", password):
        display_error('Not valid ! It should not contain any space')

    conform_password = input_conform_password.get()
    if password != conform_password:
        display_error('Your password is mismatch')
        return False

    email = input_email.get()
    if not email.endswith('.com'):
        display_error('E-mail_id format is not correct')
        return False
    elif email.islower():
        query = 'SELECT email FROM customers_details WHERE email = %s'
        value = [email]
        my_cursor.execute(query, value)
        if my_cursor.fetchone():
            display_error('Email-id already exist')
            return False
    else:
        display_error('E-mail_id should not contain any uppercase letter')
        return False

    number = input_mobile_no.get()
    if len(number) < 10 or len(number) > 10:
        display_error('Mobile number is not valid (Enter a 10 digit number)')
        return False
    elif re.search("[\s]", number):
        display_error('Not valid ! It should not contain any space')
        return False
    elif number.isnumeric():
        query = 'SELECT mobile_number FROM customers_details WHERE mobile_number = %s'
        value = [number]
        my_cursor.execute(query, value)
        if my_cursor.fetchone():
            display_error('Mobile number already exist')
            return False
    else:
        display_error('Number is not valid (A number should not contain any characters)')
        return False

    address = input_address.get()
    if not address.strip():
        display_error('Please fill the address')
        return False

    balance = input_balance.get()
    try:
        if int(balance) < 500:
            display_error('Amount should be greater than 500')
            return False
    except ValueError:
        display_error('Not valid ! Input should be number')
        return False

    try:
        insert_value = "insert into customers_details (Name, user_id, age, mobile_number, email, address, " \
                       "password, opening_balance) values (%s, %s, %s, %s, %s, %s, %s, %s )"
        values = [(name, user_id, age, number, email, address, password, balance)]
        my_cursor.executemany(insert_value, values)
        mydb.commit()
        display_error('Your account is successfully created')
    except Exception as e:
        display_error(e)


def button():
    validate_input()
    input_name.delete(0, END)
    input_age.delete(0, END)
    input_user_id.delete(0, END)
    input_password.delete(0, END)
    input_conform_password.delete(0, END)
    input_email.delete(0, END)
    input_mobile_no.delete(0, END)
    input_address.delete(0, END)
    input_balance.delete(0, END)


# label names
label_title = Label(root, text='WELCOME TO YOUR BANK', font=('Helvetica bold', 15))
label_title.grid(row=0, column=0, columnspan=2, pady=15)
label_name = Label(root, text='Enter your name', font=2)
label_name.grid(row=1, column=0, pady=10)
label_age = Label(root, text='Enter your age', font=2)
label_age.grid(row=2, column=0, pady=10)
label_user_id = Label(root, text='Create your user_id', font=2)
label_user_id.grid(row=3, column=0, pady=10)
label_password = Label(root, text='Create your password', font=2)
label_password.grid(row=4, column=0, pady=10)
label_conform_password = Label(root, text='Re-enter your password', font=2)
label_conform_password.grid(row=5, column=0, pady=10)
label_email = Label(root, text='Enter your email-id', font=2)
label_email.grid(row=6, column=0, pady=10)
label_mobile_no = Label(root, text='Enter your mobile-no', font=2)
label_mobile_no.grid(row=7, column=0, pady=10)
label_address = Label(root, text='Enter your address', font=2)
label_address.grid(row=8, column=0, pady=10)
label_balance = Label(root, text='Enter initial amount to deposit', font=2)
label_balance.grid(row=9, column=0, pady=10)

# input fields
input_name = Entry(root, width=40, borderwidth=2)
input_name.grid(row=1, column=1, padx=30)
input_age = Entry(root, width=40, borderwidth=2)
input_age.grid(row=2, column=1, padx=30)
input_user_id = Entry(root, width=40, borderwidth=2)
input_user_id.grid(row=3, column=1, padx=30)
input_password = Entry(root, width=40, borderwidth=2)
input_password.grid(row=4, column=1, padx=30)
input_conform_password = Entry(root, width=40, borderwidth=2)
input_conform_password.grid(row=5, column=1, padx=30)
input_email = Entry(root, width=40, borderwidth=2)
input_email.grid(row=6, column=1, padx=30)
input_mobile_no = Entry(root, width=40, borderwidth=2)
input_mobile_no.grid(row=7, column=1, padx=30)
input_address = Entry(root, width=40, borderwidth=2)
input_address.grid(row=8, column=1, padx=30)
input_balance = Entry(root, width=40, borderwidth=2)
input_balance.grid(row=9, column=1, padx=30)

# Signup button
button = Button(root, text='Sign up', padx=50, borderwidth=4, command=button)
button.grid(row=10, column=0, columnspan=2, pady=10)

root.mainloop()
