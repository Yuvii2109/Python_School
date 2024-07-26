#Program to show the calculation of interest
print("""
1. calculate simple interest
2. calculate compound interest
3. exit
""")
ch = int(input("Enter the choice (1-3) - "))
if ch >= 1 and ch <= 2 :
    P = float(input("Principal - "))
    R = float(input("Rate of Interest - "))
    T = float(input("Time period - "))
if ch == 1 :
    I = (P*T*R)/100
    print("Simple Interest - ",I)
elif ch == 2 :
    n = int(input("Number of times interest is compounded per year - "))
    I = P*(1+(R/n))**(n*T) - P
    print("Compound Interest - ",I)
elif ch == 3 :
    exit
else :
    print("Wrong choice")
