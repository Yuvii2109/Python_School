D = {}
while True :
    print("""
1. Create
2. Display
3. Search Subject
4. Search topper
5. Exit
""")
    ch == int(input("Enter the choice (1-5) : "))
    if ch == 1 :
        n = 11
        for i in range(1,n) :
            a = input("Enter the subject name : ")
            b = input("Enter the name of the topper : ")
            D[a] = b
    elif ch == 2 :
        print("Subject : Topper")
        for k,v in D.items() :
            print(k," : ",v)
    elif ch == 3 :
        nam = input("Enter the name of the topper student to search for the subject : ")
        for k,v in D.items() :
            if v == nam :
                print(v," has topped in ",k)
                break
        else :
            print("No such name exists in the list")
    elif ch == 4 :
        sub = input("Enter the name of the subject to search for the topper : ")
        for k,v in D.items() :
            if k == sub :
                print("The topper of ",k," is ",v)
                break
        else :
            print("No such subject exists in the list")
    elif ch == 5 :
        exit
    else :
        print("Wrong choice ")
