n = int(input("Enter a number to find its factors - "))
print(1, end = ' , ') #1 is a factor of every number
factor = 2
while factor <= n/2 :
    if n % factor == 0 :
        print(factor, end = ' , ')
    factor += 1 
print(n, end = ' , ') #every number is a factor of itself
