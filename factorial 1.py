n = int(input("Enter the the number - "))
if n == 0 :
    print("factorial - 1 ")
else :
    for i in range(1,n+1) :
        fact = fact*i
    print("factorial - ",fact)
