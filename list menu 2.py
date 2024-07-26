L = []
while True :
    print("""
1. Input an element and a location from the user and insert the element at the entered location in the list.
2. Input a location from the user and remove the element from that location in the list.
3. Input an element from the user and find its location in the list.
4. Display the list in sorted order without sorting the list.
5. Display the list in reverse order without reversing the list.
6. Display the list
7. Exit """)
    ch = int(input("Enter your choice (1-7) :- "))
    if ch == 1 :
        n = int(input("Enter the number of elements to be inserted :- "))
        for i in range(0,n) :
            a = int(input("Enter the number to be inserted :- "))
            b = int(input("Enter the index you want to give to the element :- "))
            if b > (n-1) :
                print("Invalid index ")
            elif b < -n :
                print("Invalid index ")
            else :
                L.insert(b,a)
        print(L)
    elif ch == 2 :
        loc = int(input("Enter the location of the element you want to remove :- "))
        if loc > (n-1) :
            print("Invalid index")
        elif loc < (-n) :
            print("Invalid index")
        else :
            del L[loc]
        print(L)
    elif ch == 3 :
        ele = int(input("Enter the element :- "))
        if ele in L :
            L.index(ele)
            break
        else :
            print("Enter an element from the list")
        print("Index of ",ele," is ",L.index(ele))
    elif ch == 4 :
        for x in range(0,len(L)):
            for y in range(0,len(L)-1-a):
                if L[y]>L[y+1]:
                    L[y],L[y+1]=L[y+1],L[y]
        print(L)
    elif ch == 5 :
        print(L[::-1])
    elif ch == 6 :
        print(L)
    elif ch == 7 :
        exit
    else :
        print("Enter a vaild choice ")
