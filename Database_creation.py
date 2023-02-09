import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="pass123",
    database="bank_details")
print(mydb)
my_cursor = mydb.cursor()
try:
    my_cursor.execute('create database bank_details')
    print('Database is created')
except FileExistsError:
    print('File already exist')
try:
    table = my_cursor.execute('create table customers_details(Name varchar(50), user_id varchar(50), age int(100),'
                              'mobile_number bigint, email varchar(200), address varchar(300),password varchar(100), '
                              'opening_balance bigint)')
    print('Table created')
except Exception as e:
    print(e)



