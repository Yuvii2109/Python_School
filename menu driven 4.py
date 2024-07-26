print("""
1. Check if even or odd
2. Check if prime or composite
3. Display sum of digits
4. Exit
""")
ch = int(input("Enter the choice (1-4) - "))
if ch <= 3 and ch >= 1 :
    n = int(input("Enter the number - "))
if ch == 1 :
    if n == 0 :
        print("your have entered a zero")
    elif n%2 == 0 :
        print("you have entered an even number")
    else :
        print("you have entered an odd number")
elif ch == 2 :
    if n > 1 :
        for i in range(2,n) :
            if (n % i) == 0 :
                
                print(n,"is a composite number")   
                break  
        else :
            print(n,"is a prime number")  
         
    else :
         print(n,"is a composite number")
elif ch == 3 :
    sum = 0
    for i in str(n) :
        sum += int(i)
    print(sum)
elif ch == 4 :
    exit
else :
    print("Wrong Choice")
    
