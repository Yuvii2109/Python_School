import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',passwd='EdithCozIaim3000Ttlshiwwya',database='employee')
mycursor=mydb.cursor()
mycursor.execute("Alter table employee add column D_name char(20)")
mydb.commit()
mycursor.execute("Alter table employee add column City char(10)")
mydb.commit()
mycursor.execute("update employee set D_name='Research',City='Delhi'where Deptno=10")
mydb.commit()
mycursor.execute("update employee set D_name='HRD',City='Mumbai'where Deptno=20")
mydb.commit()
mycursor.execute("update employee set D_name='Accounting',City='Kolkata'where Deptno=30")
mydb.commit()