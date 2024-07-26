import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',passwd='EdithCozIaim3000Ttlshiwwya',database='employee')
mycursor=mydb.cursor()
mycursor.execute("select * from employee")
r=mycursor.fetchone()
while r is not None:
    print(r)
    r=mycursor.fetchone()
