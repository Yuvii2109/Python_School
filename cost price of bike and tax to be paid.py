#Cost price of the bike and the tax the owner needs to pay
CP = float(input("Price of the bike - "))
if CP>100000 :
    print("15% tax to be paid")
elif 50000<CP<=100000 :
    print("10% tax to be paid")
else :
    print("5% tax to be paid")
