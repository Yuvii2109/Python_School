print("""
1. Natural numbers from 1 to n
2. Even numbers from 2 to n
3. Sum of odd numbers from 1 to n
4. Odd numbers in reverse order from n to 1
5. Exit
""")
ch = int(input("Enter the choice (1-5) - "))
if ch <= 4and ch >= 1 :
    n = int(input("Enter the value of the last number - "))
if ch == 1 :
    for i in range(1,n) :
        print(i)
elif ch == 2 :
    for i in range(2,n,2) :
        print(i)
elif ch == 3 :
    sum = 0
    for i in range(1,n+1,2) :
        sum += i
    print("Sum of odd numbers = ",sum)
elif ch == 4 :
    for i in range(n,1,-2) :
        print(i)
elif ch == 5 :
    exit
else :
    print("Wrong choice")
