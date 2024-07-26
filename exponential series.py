x = int(input("Enter the value of x - "))
n = int(input("Enter the limit - "))
total = 1
for i in range(1,n+1) :
    total += (x**i)/i
print(round(total,2))
