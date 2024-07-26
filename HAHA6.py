#Handling of variable length arguments

def sum(*b) :
    c = 0
    for i in b :
        c += i 
    print(c)

sum(10,20,3,4,6)
