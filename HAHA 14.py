def evenoddcount(tup) :
    counteven = 0
    countodd = 0
    for a in tup :
        if a%2 == 0 :
            counteven += 1
        else :
            countodd += 1
    return counteven,countodd





tup = ()
n = int(input("Enter the number of elements to be taken - "))
for i in range(n) :
    num = int(input("Enter the number - "))
    tup += (num,)
totcount = evenoddcount(tup)
print("even count - ",totcount[0],"odd count - ",totcount[1])

