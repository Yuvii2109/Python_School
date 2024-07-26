#python program to find the largest number among the three inputted numbers
A = int(input("Enter the first number - "))
B = int(input("Enter the second number - "))
C = int(input("Enter the third number - "))
if (A>B) :
    if (A>C) :
        print(A,"is the largest number")
    else :
        print(C,"is the largest number")
else :
    if (B>C) :
        print(B,"is the largest number")
    else :
        print(C,"is the largest number")
        
    
