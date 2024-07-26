num = int(input("Enter the non negative number to take the factorial of - "))
fact = 1
for i in range(num) :
    fact = fact*(i+1)
print('Factorial of ',num,' = ',fact)
