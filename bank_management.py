import mysql.connector
import re

mydb = mysql.connector.connect(host="localhost", user="root", password="#GokUl@0498", database="bank_details")
my_cursor = mydb.cursor()


def new_customer():
    while True:
        while True:
            customer_name = input('Enter your name: ')
            if name(customer_name):
                break
        while True:
            input_age = input('Enter your Age: ')
            if age(input_age):
                break
        while True:
            email_id = input('Enter your e-mail id: ')
            if email(email_id):
                break
        while True:
            userid = input('Create your User-id: ')
            if user_id(userid):
                break
        while True:
            password = input('Create your Password: ')
            if create_password(password):
                break
        while True:
            customer_address = input('Enter your Address: ')
            if address(customer_address):
                break
        while True:
            number = input('Enter your Mobile number: ')
            if mobile_number(number):
                break
        while True:
            open_balance = input('Enter your opening account balance amount:')
            opening_balance(open_balance)
            break
        try:
            insert_value = "insert into customers_details (Name, user_id, age, mobile_number, email, address, " \
                           "password, opening_balance) values (%s, %s, %s, %s, %s, %s, %s, %s )"
            values = [
                (customer_name, userid, input_age, number, email_id, customer_address, password, open_balance)]
            my_cursor.executemany(insert_value, values)
            mydb.commit()
            print('Your account is successfully created\n')
        except Exception as e:
            print(e)
        break


def existing_user():
    while True:
        while True:
            existing_user_id = input('\nEnter your user-id: ')
            if existing_user_id.islower():
                if existing_userid(existing_user_id):
                    break
            else:
                print('user-id must be in lowercase')
                return False
        while True:
            password = input('Enter your password: ')
            if existing_password(existing_user_id, password):
                break
        while True:
            try:
                query = "select name FROM customers_details WHERE user_id = %s"
                values = [existing_user_id]
                my_cursor.execute(query, values)
                acc_holder_name = my_cursor.fetchone()
                name = str(acc_holder_name[0])
                print(f"  ****** Welcome {name} ******   \n")
                print(
                    '  i)   Balance enquiry\n  ii)  Deposit\n  iii) Withdraw\n  iv)  Change password\n  v)   Exit ')
            except ValueError:
                print('Account not found!!!')
            try:
                input_option = int(input('\nPlease select your option: '))
            except ValueError:
                print('Value must be number')
            if input_option == 1:
                balance_enquiry(existing_user_id)
                verify = input('Continue banking press y otherwise press n: ')
                exit_(existing_user_id, verify)
            elif input_option == 2:
                deposit(existing_user_id)
                verify = input('Continue banking press y otherwise press n: ')
                exit_(existing_user_id, verify)
            elif input_option == 3:
                withdraw(existing_user_id)
                verify = input('Continue banking press y otherwise press n: ')
                exit_(existing_user_id, verify)
            elif input_option == 4:
                change_password(existing_user_id)
                verify = input('Continue banking press y otherwise press n: ')
                exit_(existing_user_id, verify)
            elif input_option == 5:
                verify = input('\nAre you sure want to Exit?\n Press yes to exit:')
                exit_(existing_user_id, verify)
            else:
                print('Please select correct option')
                return False


def name(customer_name):
    while True:
        if not customer_name.strip():
            print("Input is empty.")
            return False
        elif re.search('[1-9]', customer_name):
            print("Input contains numeric characters.")
            return False
        else:
            return True


def mobile_number(number):
    while True:
        if len(number) < 10 or len(number) > 10:
            print('Mobile number is not valid (Enter a 10 digit number)')
            return False
        elif re.search("[\s]", number):
            print("Not valid ! It should not contain any space")
            return False
        elif number.isnumeric():
            query = 'SELECT mobile_number FROM customers_details WHERE mobile_number = %s'
            value = [number]
            my_cursor.execute(query, value)
            if my_cursor.fetchone():
                print('Mobile number already exist')
                return False
            else:
                return True
        else:
            print('Number is not valid (A number should not contain any characters)')
            return False


def user_id(userid):
    while True:

        if userid.islower():
            query = 'SELECT user_id FROM customers_details WHERE user_id = %s'
            values = [userid]
            my_cursor.execute(query, values)
            if my_cursor.fetchone():
                print('User_id is already exist')
                return False
            else:
                return True
        else:
            print('User_id must be in lowercase letter')
            return False


def create_password(password):
    while True:
        if len(password) < 8:
            print("Not valid ! Total characters should be grater than 8")
            return False
        elif not re.search("[A-Z]", password):
            print("Not valid ! It should contain at least one uppercase letter")
            return False
        elif not re.search("[a-z]", password):
            print("Not valid ! It should contain at least one lowercase letter")
            return False
        elif not re.search("[1-9]", password):
            print("Not valid ! It should contain at least one number")
            return False
        elif not re.search("[~!@#$%^&*]", password):
            print("Not valid ! It should contain at least one special character")
            return False
        elif re.search("[\s]", password):
            print("Not valid ! It should not contain any space")
            return False
        conform_password = input('Re-enter your Password: ')
        if password != conform_password:
            print('Your password is mismatch')
            return False
        else:
            return True


def opening_balance(open_balance):
    while True:
        try:
            if int(open_balance) < 500:
                print('Amount should be greater than 500')
                return False
            else:
                return True
        except ValueError:
            print('Not valid ! Input should be number')
            return False


def age(input_age):
    try:
        while True:
            if int(input_age) >= 18:
                return True
            else:
                print('Age must be 18 or above')
                return False
    except ValueError:
        print('Not valid ! Input should be number')


def email(email_id):
    while True:
        if not email_id.endswith('.com'):
            print('E-mail_id format is not correct')
            return False
        elif email_id.islower():
            query = 'SELECT email FROM customers_details WHERE email = %s'
            value = [email_id]
            my_cursor.execute(query, value)
            if my_cursor.fetchone():
                print('Email-id already exist')
                return False
            else:
                return True
        else:
            print('E-mail_id should not contain any uppercase letter')
            return False


def address(customer_address):
    while True:
        if customer_address.strip():
            return True
        else:
            print('Please fill the address')
            return False


def existing_userid(existing_user_id):
    query = "SELECT user_id FROM customers_details WHERE user_id = %s"
    values = [existing_user_id]
    my_cursor.execute(query, values)
    stored_user_id = my_cursor.fetchone()
    if stored_user_id is None:
        print('User id not found')
        return False
    elif existing_user_id != str(stored_user_id[0]):
        print('User id is incorrect!!')
        return False
    else:
        return True


def existing_password(existing_user_id, password):
    query = "SELECT password FROM customers_details WHERE user_id = %s"
    values = [existing_user_id]
    my_cursor.execute(query, values)
    database_password = my_cursor.fetchone()
    password_comparing = str(database_password[0])
    if password != password_comparing:
        print('Password is incorrect!!')
        return False
    else:
        return True


def balance_enquiry(existing_user_id):
    try:
        query = "SELECT opening_balance FROM bank_details.customers_details WHERE user_id = %s"
        values = [existing_user_id]
        my_cursor.execute(query, values)
        acc_balance = my_cursor.fetchone()
        balance = str(acc_balance[0])
        print(f'\nYour account balance is {balance} $\n')
    except Exception as e:
        print(e)


def deposit(existing_user_id):
    try:
        try:
            deposit_amount = int(input('\nEnter amount for deposit: '))
        except ValueError:
            print('\nValue must be number!!')

        query = "SELECT opening_balance FROM bank_details.customers_details WHERE user_id = %s"
        values = [existing_user_id]
        my_cursor.execute(query, values)
        acc_balance = my_cursor.fetchone()
        balance = int(acc_balance[0])
        update_balance = balance + deposit_amount
        query = "UPDATE customers_details SET opening_balance = %s WHERE user_id = %s"
        values = (update_balance, existing_user_id)
        my_cursor.execute(query, values)
        mydb.commit()
        print(f'\nAvailable balance is {update_balance} $\n')
    except Exception as e:
        print(e)


def withdraw(existing_user_id):
    try:
        try:
            withdraw_amount = int(input('\nEnter amount for withdraw: '))
        except ValueError:
            print('\nValue must be number!!')
        query = "SELECT opening_balance FROM bank_details.customers_details WHERE user_id = %s"
        values = [existing_user_id]
        my_cursor.execute(query, values)
        acc_balance = my_cursor.fetchone()
        balance = int(acc_balance[0])
        update_balance = balance - withdraw_amount
        if update_balance < 0:
            print('Insufficient balance')
            return False
        else:
            query = "UPDATE customers_details SET opening_balance = %s WHERE user_id = %s"
            values = (update_balance, existing_user_id)
            my_cursor.execute(query, values)
            mydb.commit()
            print(f'\nAvailable balance is {update_balance} $\n')
    except Exception as e:
        print(e)


def change_password(existing_user_id):
    old_pass = input('\nEnter your old password:')
    query = "SELECT password FROM customers_details WHERE user_id = %s"
    values = [existing_user_id]
    my_cursor.execute(query, values)
    database_password = my_cursor.fetchone()
    if old_pass == str(database_password[0]):
        password = input('\nPlease enter your new password: ')
        create_password(password)
        query = "UPDATE customers_details SET password = %s WHERE user_id = %s"
        values = (password, existing_user_id)
        my_cursor.execute(query, values)
        mydb.commit()
        print('Password successfully updated ')
    else:
        print('Your old password is not match')


def exit_(existing_user_id, verify):
    if verify == 'y':
        return False
    elif verify == 'yes' or 'n':
        query = "select name FROM customers_details WHERE user_id = %s"
        values = [existing_user_id]
        my_cursor.execute(query, values)
        acc_holder_name = my_cursor.fetchone()
        name = str(acc_holder_name[0])
        print(f'\n***********Thanks for banking {name}***********\n')
        main()
    else:
        print('Enter a correct value')


def main():
    while True:
        print('********WELCOME TO TEX BANK*********')
        print('''
        1: Open new account
        2: Login existing account
             ''')
        try:
            input_value = int(input('Please select the option: '))
            if input_value == 1:
                new_customer()
            elif input_value == 2:
                existing_user()
            else:
                print('Choose a correct option')
        except ValueError:
            print('Please enter a valid input')


# Bank Management
main()
