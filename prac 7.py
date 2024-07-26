import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',passwd='EdithCozIaim3000Ttlshiwwya',database='employee')
mycursor=mydb.cursor()
eno=int(input("enter the employee number - "))
mycursor.execute("select * from employee where Eno='{}'".format(eno))
r=mycursor.fetchall()
if r==[]:
    print('Not found')
else:
    for a in r:
        print(a)
