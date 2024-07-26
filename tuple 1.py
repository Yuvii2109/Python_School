#creating a tuple by the user
t = tuple()
n = int(input("Enter the number of elements to be added :- "))
for i in range(n) :
    x = input("Enter the element :- ")
    t += (x,)
print(t)
