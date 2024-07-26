def sum(n):
    sum = 0
    for i in range(n+1):
        sum += i
    return sum
n = int(input("Enter n = "))
print(sum(n))
print(sum(10))
print(sum(20))
x = sum(n)
print(x)

