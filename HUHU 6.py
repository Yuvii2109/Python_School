#Illustrating all read operations

f=open("mayak.txt",'r')
print(f.read(2))
print(f.readlines())
print(f.read(3))
print(f.readline())
print("remaining data")
print(f.read())

