#Passing argument/parameter to a function
#mutable/immutable datatype handling in a function

def modify(lst):    #Formal parameter/argument
    print(id(lst))
    lst[1]=45
    print(id(lst))
    print("list inside the func:",lst)
    
list1=[10,20,30]     #Actual parameter/argument
print(id(list1))
modify(list1)
print("list is:",list1)
