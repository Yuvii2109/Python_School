print("""
      1. add
      2. Subtract
      3. Mulitply
      4. Divide
      5. Remainder
      6. Power
      7. exit
      """)
ch=int(input("enter your choice(1-7) : "))
if ch >=1 and ch<=6:
    a=int(input("enter First number : "))
    b=int(input("Enter Second number : "))
if ch==1:
    c=a+b
    print("Sum = ",c)
elif ch==2:
    c=a-b
    print("Difference = ",c)
elif ch==3:
    c=a*b
    print("Product = ",c)
elif ch==4:
    c=a/b
    print("Quotient = ",c)
elif ch==5:
    c=a%b
    print("Remainder = ",c)
elif ch==6:
    c=a**b
    print("power = ",c)
elif ch==7:
    exit
else:
    print("Wrong Choice")
