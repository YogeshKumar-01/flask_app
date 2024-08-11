import mysql.connector
mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'Yogesh@1234'
)

mycursor = mydb.cursor()
# mycursor.execute('select * from test2.test2_table')
mycursor.execute('select c1,c2 from test2.test2_table')
for i in mycursor.fetchall():
    print(i)

mydb.close()