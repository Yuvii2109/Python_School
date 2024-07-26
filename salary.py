name = input("Enter Name - ")
salary = float(input("Enter Salary - "))
if salary >= 50000:
    grade = "A"
elif salary >= 35000:
    grade = "B"
elif salary >= 20000:
    grade = "C"
else:
    grade = "D"
print(name ,"\nYour grade is ",grade)    
