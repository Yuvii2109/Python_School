print("""
1. Check if a number is positive or negative
2. Check if the number is even or odd
3. Check if a number is divisible by 3 or not
4. Exit
""")
ch = int(input("Enter your choice ( 1-4 ) - "))
if ch >= 1 and ch <= 3:
    x = int(input("Enter the number - "))
if ch == 1:
    if x > 0:
        print("It is a positive number")
    elif x == 0:
        print("You have entered a zero which is neither negative nor positive")
    else:
        print("It is a negative number")
elif ch == 2:
    if x%2 == 0:
        print("It is an even number")
    elif x == 0:
        print("You have entered a zero which is neither even nor odd")
    else:
        print("It is an odd number")
elif ch == 3:
    if x%3 == 0:
        print("The number is divisible by 3")
    else:
        print("The number is not divisible by 3")
elif ch == 4:
    exit
else:
    print("You have entered the wrong choice")
