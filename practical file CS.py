'''Ques 1:
Write a Python Program to Declare a Stack list and display the following
menu:
1. Push
2. Pop
3. Display
4. Exit
Ans:'''
s=[]
ch="y"
while ch=="y":
print("1. PUSH operation")
print("2. POP operation")
print("3. Display")
print("4. Exit")
choice=int(input("Enter your choice"))
if choice==1:
n=input("Enter any number")
s.append(n)
elif choice ==2:
if (s==[]):
print("Stack is empty")
else:
print("Deleted element is :",s.pop())
elif choice ==3:
l=len(s)
for i in range(l-1,-1,-1): #Display elements from top to 0th index
print(s[i])
elif choice ==4:
break
else:
print("Wrong input, enter again")
ch=input("Do you wish to continue")
