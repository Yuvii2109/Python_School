d1 = dict()
i = 1
n = int(input("Enter the number of entries : "))
while i <= n :
     nam = input("Enter name of the historical site : ")
     c = input("Enter the country : ")
     city = input("Enter the city : ")
     area = input("Enter the area : ")
     arc = input("Enter the architectural design : ")
     built = input("Built by : ")
     web = input("Enter the website : ")
     cost = input("Enter the visiting price : ")
     d1[nam] = (c,city,area,arc,built,web,cost)
     i += 1
     l = d1.keys()
     print("\nName\t\t","Country\t\t","City\t\t","Area\t\t","Architectural Design\t\t","Built by\t\t","Website\t\t","Cost\t\t")
     for i in l :
         z = d1[i]
         print('\n',i,'\t\t',end = "")
         for j in z :
             print(j,'\t\t',end = "\t\t")
         break
