import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',passwd='EdithCozIaim3000Ttlshiwwya',database='employee')
mycursor=mydb.cursor()
n=int(input("Enter the number of records to be added - "))
for a in range(n):
    Eno=int(input("Enter the employee no - "))
    Name=input("Enter the employee name - ")
    Designation=input("Enter the designation - ")
    Salary=int(input("Enter the salary - "))
    Deptno=int(input("Enter the department number - "))
    mycursor.execute("INSERT INTO EMPLOYEE values('{}','{}','{}','{}','{}')".format(Eno,Name,Designation,Salary,Deptno))
mydb.commit()
print("Records inserted")
