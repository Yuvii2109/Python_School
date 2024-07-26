d1 = dict()
i = 1
while true :
    print('''
  a Create 
  b Display
  c Search on country  
  d Search on city 
  e Search on architectural design
  f Display website with name , country , city
  g exit 
  ''' )
    ch = int(input("Enter the choice (a-g) : "))
    if ch == a :
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
     elif ch == b :
         l = d1.keys()
         print("\nName\t\t","Country\t\t","City\t\t","Area\t\t","Architectural Design\t\t","Built by\t\t","Website\t\t","Cost\t\t")
         for i in l :
             z = d1[i]
             print('\n',i,'\t\t',end = "")
             for j in z :


                 print(j,'\t\t',end = "\t\t")
     elif ch == c :
         x = input("Enter the country to be searched : ")
         for i in l :
             if i == x :
                 print("\nName\t\t","Country\t\t","City\t\t","Area\t\t","Architectural Design\t\t","Built by\t\t","Website\t\t","Cost\t\t")
                 
        
      
