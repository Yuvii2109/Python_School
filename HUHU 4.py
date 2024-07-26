#Illustrate the use of read(n)
#To read first 30 characters from the file.

f=open("mayak.txt",'r')
data=f.read(30) #This will read the first 10 characters from fnew
print(data) 
f.close()
