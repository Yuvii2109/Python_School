price = float(input("enter price - "))
if price >= 10000:
    d = 5
elif price >= 5000:
    d = 2.5
else:
    d = 0
disamt = price*d/100
net = price-disamt
print("discount amount - ",disamt)
print("net amount - ",net)
