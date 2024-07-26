print("""
1. Positive or negative
2. Table of numbers( 10 terms )
3. Exit
""")
ch = int(input("Enter the choice ( 1-3 ) - "))
if ch >= 1 and ch <= 2 :
    n = int(input("Enter the number - "))
if ch == 1 :
    if n == 0 :
        print("You have entered a zero")
    elif n > 0 :
        print(n ," is a positive number")
    elif n < 0 :
        print(n ," is a negative number")
    else :
        exit
elif ch == 2 :
    for i in range(1,11) :
        pro = i*n
        i += 1
        print(pro)
elif ch == 3 :
    exit
else :
    print("Wrong choice")
