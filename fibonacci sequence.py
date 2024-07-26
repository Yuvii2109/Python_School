l = [0,1]
n = int(input("Enter the number of elements :- "))
for a in range(2,n+1) :
    l.append(l[a-1]+l[a-2])
while True :
    print("""
1. Display 1st ten numbers
2. Display last ten numbers
3. Search
4. Exit
""")
    ch = int(input("Enter choice number : "))
    if ch == 1 :
        for x in l[1:11] :
            print(x)
    elif ch == 2 :
        for y in l[11:21] :
            print(y)
    elif ch == 3 :
        num = int(input("Enter the number to be searched :-"))
        if num in l[1:21] :
            print("Yes",num,"is present in the sequence")
        else :
            print("Not found")
    elif ch == 4 :
        exit
    else :
        print("Wrong choice")
    
