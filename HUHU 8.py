#Correct method
#To perform addition of 2 numbers using a file


f = open("fnew.txt","w")
num1 = int(input("Enter the first no - "))
num2=int(input("Enter the second no - "))
sum1=num1+num2
f.write("\nNumber 1 - "+str(num1))
f.write("\nNumber 2 - "+str(num2))
f.write("\nSum of the 2 numbers - "+str(sum1))
f.close()


