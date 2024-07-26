print("""
1. Check if perfect number
2. Check if armstrong number
3. Display reverse of number
4. Exit
""")
ch = int(input("Enter the choice - "))
if ch <= 3 and ch >= 1 :
    n = int(input("Enter the number - "))
if ch == 1 :
    sum1 = 0
    for i in range(1,n) :
        if(n % i == 0) :
            sum1 = sum1 + i
    if (sum1 == n) :
        
        print("The number is a Perfect number")
    else:
        print("The number is not a Perfect number")
elif ch == 2 :
    sum = 0  
    temp = n   
    while temp > 0:
        digit = temp % 10  
        sum += digit ** 3  
        temp //= 10  
    if n == sum :
        print(n,"is an Armstrong number")  
    else:  
        print(n,"is not an Armstrong number")
elif ch == 3 :
    Reverse = 0    
    while(n > 0) :
        Reminder = n%10    
        Reverse = (Reverse *10) + Reminder    
        n //= 10    
    print("\n Reverse of entered number is = %d" %Reverse)
elif ch == 4 :
    exit
else :
    print("Wrong choice")
