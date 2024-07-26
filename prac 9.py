import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',passwd='EdithCozIaim3000Ttlshiwwya',database='employee')
mycursor=mydb.cursor()
d=input("Enter the designation - ")
mycursor.execute("select name,salary from employee where designation='{}'".format(d))
r=mycursor.fetchall()
for a in r:
    print(a)
