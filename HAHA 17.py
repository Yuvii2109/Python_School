#main for calculating area of rectangle

def area_rect(length,breadth):
    return length*breadth

def main():
    l=int(input("Enter length : "))
    b=int(input("Enter breadth : "))
    a=area_rect(l,b)
    print("area is",a)

if __name__=="__main__":
    main()
