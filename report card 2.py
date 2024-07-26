name = input("enter name - ")
m1 = float(input("enter marks in subject 1 - "))
m2 = float(input("enter marks in subject 2 - "))
m3 = float(input("enter marks in subject 3 - "))
m4 = float(input("enter marks in subject 4 - "))
m5 = float(input("enter marks in subject 5 - "))
total = m1+m2+m3+m4+m5
avg = total/5
print("name                     - ",name)
print("total marks              - ",total)
print("average marks            - ",avg)
if avg >= 33:
    if avg >= 40:
        if avg >= 50:
            if avg >= 60:
                if avg >= 70:
                    if avg >= 80:
                        if avg >= 90:
                            g = "A+"
                        else:
                            g = "A"
                    else:
                        g = "B+"
                else:
                    g = "B"
            else: 
                 g = "C+"
        else:
             g = "C"
    else:
         g = "D"
else:
    g = "E"
print("grade                     - ",g)
