#Scope of a variable

x = 10   #Global variable 

def somevalue():
    global x
    x = 20
    print("Inside function - ",x)
    
somevalue()
print("Outside function - ",x)
