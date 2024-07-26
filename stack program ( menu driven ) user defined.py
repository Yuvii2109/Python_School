def Empty(s) :
    if s == [] :
        return True
    else :
        return False
def Push(s,x) :
    s.append(x)
    Top = len(s)-1
def Pop(s) :
    if Empty(s) :
        return "Underflow"
    else :
        x = s.Pop()
        if len(s) == 0 :
            Top = None
        else :
            Top = len(s) - 1
        return x
def Show(s) :
    if Empty(s) :
        print("Stack is empty")
    else :
        Top = len(s)
        for i in range(Top-1,-1,-1) :
            print(s[i])
#------------------------------MAIN------------------------------
stk = []
Top = None
a = "y"
while a == "y" :
    print("""
1.) Push
2.) Pop
3.) Show
4.) Exit """)
    ch = int(input("Enter your choice :- "))
    if ch == 1 :
        y = int(input("Enter the number of inputs :- "))
        for i in range(y) :
            x = int(input("Enter the number :- "))
            Push(stk,x)
        continue
    elif ch == 2 :
        x = Pop(stk)
        if x == "Underflow" :
            print("Stack is empty")
        else :
            print("Popped element is :- ",x)
    elif ch == 3 :
        print("-------Stack-------")
        Show(stk)
    elif ch == 4 :
        break
    else :
        print("Wrong input")
