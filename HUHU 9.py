#Handling file using with

#Method2 (using open())
with open ("fnew2.txt","w") as f:
    f.write("I am using with statement ")
    f.write("It closes file automatically")
    print("Is file closed - ",f.closed)
    
print("Is file closed now - ",f.closed)
print("Data written")
