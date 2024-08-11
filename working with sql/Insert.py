import mysql.connector

# Establish the connection
mydb = mysql.connector.connect(
    host="localhost",        # MySQL host
    user="root",             # MySQL username
    password="Yogesh@1234",     # MySQL password
    database="test2"         # Name of the database
)

# Create a cursor object
mycursor = mydb.cursor()

# SQL statement to insert data into the table
sql = "INSERT INTO test2_table (c1, c2, c3) VALUES (%s, %s, %s)"
val = (1, 'Sample Text', 23.45)

# Execute the SQL command
mycursor.execute(sql, val)

# Commit the transaction
mydb.commit()

print(mycursor.rowcount, "record inserted.")
