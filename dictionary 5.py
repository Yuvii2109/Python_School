''' Write a program to store student information - Name , Class ,
section , percentage in the form of dictionary and display the
information on the basis of admission number '''

d = {}
n = int(input("Enter the number of records : "))
for i in range(n) :
    Adm_No = input("Enter the Admission Number : ")
    Name = input("Enter the Name : ")
    Class = input("Enter the Class : ")
    Sec = input("Enter the Section : ")
    Per = input("Enter the percentage : ")
    D = (Name , Class , Sec , Per)
    d[Adm_No] = D
print(d)
