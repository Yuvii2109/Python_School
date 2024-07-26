print( """
      1. Area of circle
      2. Area of rectangle
      3. Circumference of circle
      4. Area of square
      5. exit
      """ )
ch = int(input("Enter the choice number - "))
if ch == 1 :
    r = int(input("Enter the radius of the circle - "))
    a = 3.14*(r**2)
    print("Area of the circle is - ",a)
elif ch == 2 :
    l = int(input("Enter the length of the rectangle - "))
    b = int(input("Enter the width of the rectangle - "))
    a = l*b
    print("Area of the rectangle is - ",a)
elif ch == 3 :
    r = int(input("Enter the radius of the cicle - "))
    c = 2*3.14*r
    print("Circumference of the circle is - ",c)
elif ch == 4 :
    l = int(input("Enter the length of the side of the square - "))
    a = l**2
    print("Area of the square is - ",a)
elif ch == 5 :
    exit
else :
    print("invalid option")
