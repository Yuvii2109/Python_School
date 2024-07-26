print("""
1. Convert temperature from C to F
2. Convert temperature from F to C
3. Convert temperature from C to K
4. convert temperature from K to C
5. exit
""")
ch = int(input("Enter your choice (1-5) - "))
if ch >= 1 and ch <= 4:
    T = int(input("Enter the temperature - "))
if ch == 1:
    temp = 9/5*T+32
    print("Temperature in F - ",temp)
elif ch == 2:
    temp = 5/9*(T-32)
    print("Temperature in C - ",temp)
elif ch == 3:
    temp = T+273
    print("Temperature in K - ",temp)
elif ch == 4:
    temp = T-273
    print("Temperature in C - ",temp)
elif ch == 5:
    exit
else:
    print("Wrong Choice")
    
    


