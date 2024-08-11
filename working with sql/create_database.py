import mysql.connector
mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root', 
    password = 'Yogesh@1234'
)

mycursor = mydb.cursor()
mycursor.execute('create database if not exists test1')
mydb.close()





