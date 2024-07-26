f = 1
x = 1
n = int(input("Enter the number - "))
for x in range(1,n+1) :
    f *= x
    x += 1
print("Factorial = ",f)
