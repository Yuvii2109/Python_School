# Program to convert multiples of 5 in a list to 5
# Non multiples of 5 to 0
while True :
    L = []
    n = int(input("Number of elements in list :- "))
    if type(n) == int :
        for i in range(0,n) :
            a = int(input("Enter the number :- "))
            L.append(a)
        print(L)
        for i in range(0,n) :
            if L[i]%5 == 0 :
                L[i] = 5
            else :
                L[i] = 0
        print("The new list is ",L)
    elif type(n) == float :
        print("Enter an INTEGER")
    else :
        print("Enter a POSITIVE INTEGER")
    
