#S = 1 + x2 + x3 + x4 ... xn
n=int(input("Enter the number of terms - "))
x=int(input("Enter the value of x - "))
sum1 = 1
for i in range(2,n+1) :
    sum1 += (x**i)
print("The sum of series is",round(sum1,2)) 
