# import mysql.connector

# mydb = mysql.connector.connect(
#     host = 'localhost',
#     user = 'root',
#     password = 'Yogesh@1234'
# )

# mycursor = mydb.cursor()
# mycursor.execute('create database if not exists test2.test2_table(c1 int, c2 varchar(50), c3 float)')
# mydb.close() 

import mysql.connector

# Establish the connection
mydb = mysql.connector.connect(
    host="localhost",  # Replace with your host
    user="root",       # Replace with your MySQL username
    password="Yogesh@1234" # Replace with your MySQL password
)

# Create a cursor object
mycursor = mydb.cursor()

# Step 1: Create the database if it doesn't exist
mycursor.execute("CREATE DATABASE IF NOT EXISTS test2")

# Step 2: Select the database
mycursor.execute("USE test2")

# Step 3: Create the table within the selected database
mycursor.execute("CREATE TABLE IF NOT EXISTS test2_table (c1 INT, c2 VARCHAR(50), c3 FLOAT)")

print("Table created successfully!")
