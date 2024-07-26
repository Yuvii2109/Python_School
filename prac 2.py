# user input
n = int(input("Enter the number of values: "))
# initialize empty stack
stack=[]
# take n numbers from the user
for i in range(n):
    num = int(input("Enter number : "))
    if num%2 != 0: # if only the number is odd push it stack
        stack.append(num)
        print(stack)
        # assuming the first number out of stack is the largest
        largestNum = stack.pop()
        # loop till stack is empty
    while(len(stack)>0):
        num = stack.pop()
        # if the number popped out is greater than the largest number found until now 
        # then make the this number the largest number
        if num>largestNum:
            largestNum=num
            # print the largest number
print("The largest number found is: ",largestNum)
