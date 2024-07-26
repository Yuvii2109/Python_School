import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',passwd='EdithCozIaim3000Ttlshiwwya',database='employee')
mycursor=mydb.cursor()
mycursor.execute('select * from employee')
r=mycursor.fetchall()
print("%5s %20s %20s %8s %6s %20s %10s"%('ENO','Name','Designation','Salary','Deptno','D_Name','City'))
for i in r:
      print("%5d %20s %20s %8d %6d %20s %10s"%(i[0],i[1],i[2],i[3],i[4],i[5],i[6]))
