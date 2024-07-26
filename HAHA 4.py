#User defined func for illustrating function with parameteres but without return type for table of a no.

def table(x):
  for a in range (1,11):
    print(x,"X",a,"is",x*a)
n= int(input("enter the number:"))
table(n)
