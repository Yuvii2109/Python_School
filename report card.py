name = input("enter name - ")
m1 = float(input("enter marks in subject 1 - "))
m2 = float(input("enter marks in subject 2 - "))
m3 = float(input("enter marks in subject 3 - "))
m4 = float(input("enter marks in subject 4 - "))
m5 = float(input("enter marks in subject 5 - "))
total = m1+m2+m3+m4+m5
avg = total/5
print("name               - ",name)
print("total marks        - ",total)
print("average marks      - ",avg)
if avg >= 90:
    g = "A+"
elif avg >= 80:
    g = "A"
elif avg >= 70:
    g = "B+"
elif avg >= 60:
    g = "B"
elif avg >= 50:
    g = "C+"
elif avg >= 40:
    g = "C"
elif avg >= 33:
    g = "D"
else:
    g = "E"
print("grade              - ",g)
